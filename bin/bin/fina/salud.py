import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def medicina(des: str, monto: float, info: bool = False):
    """Compra de medicamento, el nombre del medicamento va en descripción"""

    contenido = f"""{graba.now} Medicamento | {des}
    Expenses:Salud:Medicamentos                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def consulta(des: str, monto: float, info: bool = False):
    """Consulta con el médico, la descripción contiene el nombre de quien fue al médico"""

    contenido = f"""{graba.now} Consulta | {des}
    Expenses:Salud:Consulta                  ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def dentista(des: str, monto: float, info: bool = False):
    """Consulta con el médico, la descripción contiene el nombre de quien fue al dentista"""

    contenido = f"""{graba.now} Dentista | {des}
    Expenses:Salud:Dentista                  ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
