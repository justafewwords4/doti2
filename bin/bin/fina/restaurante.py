import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def feliz(
    monto: float,
    ban: bool = True,
    info: bool = False,
):
    """Agrega un movimiento a restaurantes | Pollo Feliz"""
    origen = ""
    if ban:
        origen = "Assets:Bancos:Banorte"
    else:
        origen = "Liabilities:Crédito Bancomer"

    contenido = f"""{graba.now} Pollo Feliz
    Expenses:Restaurantes:Comida                        ${monto:,.2f}
    {origen}                              """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def carbon(monto: float, info: bool = False):
    """Compra en carbón y taco"""

    contenido = f"""{graba.now} Restaurantes | Carbón y Taco
    Expenses:Restaurantes:Carbón y Taco                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)

@app.command()
def macdonalds(monto: float, info: bool = False):
    """Hamburguesas macdonalds"""

    contenido = f"""{graba.now} Restaurantes | MacDonalds
    Expenses:Restaurantes:MacDonalds            ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)

@app.command()
def samborns(monto: float, info: bool = False):
    """Compra en Samborns"""

    contenido = f"""{graba.now} Restaurantes | Samborns
    Expenses:Restaurantes:Samborns                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
