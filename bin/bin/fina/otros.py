"""Otros Gastos"""

import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def propina(des: str, monto: float, info: bool = False):
    """Agregar gasto a propinas, desde Assets:Cash:Felipe"""

    contenido = f"""{graba.now} Propinas | {des}
    Expenses:Propinas                            ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def perdida(monto: float, info: bool = False):
    """Pérdidas de dinero"""

    contenido = f"""{graba.now} Pérdidas 
    Expenses:Perdidas                            ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def wood(monto: float = 372.72, info: bool = False):
    """Ofrenda David Wood y Bible project"""

    contenido = f"""{graba.now} David Wood y Bible Project
    Expenses:Ofrendas                            ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
