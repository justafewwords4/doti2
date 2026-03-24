import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def ryc(monto: float, info: bool = False):
    """Compras en RYC para la despensa, desde Assets:Bancos:Banorte"""

    contenido = f"""{graba.now} Despensa | RYC
    Expenses:Despensa:Carne - Pollo                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def costco(monto: float, info: bool = False):
    """Compra de despensa en Costco"""

    contenido = f"""{graba.now} Despensa | Costco
    Expenses:Despensa:Abarrotes                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def bonafont(garrafones: int = 5, precio: float = 52, info: bool = False):
    """Agrega las botellas bonafont"""

    contenido = f"""{graba.now} Agua | Bonafont
    Expenses:Despensa:Agua         ${garrafones*precio:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def chatarra(des: str, monto: float, info: bool = False):
    """Compra de comida chatarra"""

    contenido = f"""{graba.now} Chatarra | {des}
    Expenses:Comida chatarra                         ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def mercado(monto: float, descripcion: str = "Frutas y verduras", info: bool = False):
    """Comprar despensa en el mercado"""
    contenido = f"""{graba.now} Despensa | {descripcion}
    Expenses:Despensa                  ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def frutas(monto: float, des: str = "Mercado", info: bool = False):
    """Comprar frutas y verduras"""
    contenido = f"""{graba.now} {des} | Frutas y verduras
    Expenses:Despensa:Frutas y verduras           ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def tortilla(monto: float = 80, info: bool = False):
    """Comprar tortilla"""

    contenido = f"""{graba.now} Despensa | Tortilla
    Expenses:Despensa:Abarrotes                         ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def walmart(monto: float, info: bool = False):
    """Agregar gasto a despensa walmart, desde Liabilities:Crédito Bancomer"""

    contenido = f"""{graba.now} Despensa | Walmart
    Expenses:Despensa:Abarrotes                     ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
