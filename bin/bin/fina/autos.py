import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def crv(monto: float, info: bool = False):
    """Pago de estacionamiento crv"""

    contenido = f"""{graba.now} Estacionamiento | CRV
    Expenses:Autos:Estacionamiento                         ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def civic(monto: float, info: bool = False):
    """Pago de estacionamiento civic"""

    contenido = f"""{graba.now} Estacionamiento | Civic
    Expenses:Autos:Estacionamiento                         ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def manttocivic(monto: float, info: bool = False):
    """Mantenimiento Civic"""

    contenido = f"""{graba.now} Mantenimiento | Civic
    Expenses:Autos:Mantenimiento                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def manttocrv(monto: float, info: bool = False):
    """Mantenimiento CRV"""

    contenido = f"""{graba.now} Mantenimiento | CRV
    Expenses:Autos:Mantenimiento                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def parkicrv(monto: float, info: bool = False):
    """Pago de estacionamiento"""

    contenido = f"""{graba.now} Estacionamiento | Parkimovil CRV
    Expenses:Autos:Estacionamiento                         ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def parkicivic(monto: float, info: bool = False):
    """Pago de estacionamiento"""

    contenido = f"""{graba.now} Estacionamiento | Parkimovil Civic
    Expenses:Autos:Estacionamiento                         ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)

@app.command()
def gas(descripcion:str, monto: float, info: bool = False):
    """Gasolina"""

    contenido = f"""{graba.now} Gasolina | {descripcion}
    Expenses:Autos:Estacionamiento                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
