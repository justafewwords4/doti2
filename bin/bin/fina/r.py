import os
from datetime import timedelta

import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)

extra_commands = " --pretty"


@app.command()
def diario(dias: int = 5, profundidad: int = 2):
    """=== Reporte === Muestra el balance de los últimos n días"""
    dd = graba.now - timedelta(days=dias)
    comando = f"hledger is -D -{profundidad} -S -b {dd}" + extra_commands
    os.system(comando)


@app.command()
def anual(anios: int = 4, profundidad: int = 2):
    """=== Reporte === Muestra el balance de los últimos n años"""
    aa = graba.now - timedelta(days=365 * anios)
    comando = f"hledger is -Y -{profundidad} -S -b {aa}" + extra_commands
    os.system(comando)


@app.command()
def balance():
    """=== Reporte === Muestra el balance de las cuentas"""
    comando = "hledger balancesheet" + extra_commands
    os.system(comando)


@app.command()
def semanal(semanas: int = 4, profundidad: int = 2):
    """=== Reporte === Muestra el balance de las últimas n semanas"""
    ss = graba.now - timedelta(days=7 * semanas)
    comando = f"hledger is -W -{profundidad} -S -b {ss}" + extra_commands
    os.system(comando)


@app.command()
def mensual(meses: int = 4, profundidad: int = 2):
    """=== Reporte === Muestra el balance de los últimos meses"""
    mm = graba.now - timedelta(days=30 * meses)
    comando = f"hledger is -M -{profundidad} -S -b {mm}" + extra_commands
    os.system(comando)


if __name__ == "__main__":
    app()
