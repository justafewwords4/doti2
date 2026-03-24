import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def agua(monto: float, proveedor: str = "Don Nico", info: bool = False):
    """Pago del agua Puebla"""

    contenido = f"""{graba.now} * Pipa de agua | {proveedor}
    Expenses:Casa Puebla:Pipa Agua            ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def telmex(monto: float = 549, info: bool = False):
    """Pago del telefono de la  casa en puebla"""

    contenido = f"""{graba.now} * Telmex
    Expenses:Casa Puebla:Telmex            ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def pipa(monto: float, info: bool = False):
    """Pipa de agua"""

    contenido = f"""{graba.now} * Agua Potable | Ayuntamiento
    Expenses:Casa Puebla:Agua            ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def mantto(monto: float = 800, info: bool = False):
    """Pagar Mantenimiento casa Puebla"""

    contenido = f"""{graba.now} Casa Puebla | Mantenimiento
    Expenses:Casa Puebla:Mantenimiento                   ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def gas(monto: float, info: bool = False):
    """Pagar gas casa Puebla"""

    contenido = f"""{graba.now} Casa Puebla | Gas
    Expenses:Casa Puebla:Gas                   ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def luz(monto: float, info: bool = False):
    """Pagar luz de Puebla"""

    contenido = f"""{graba.now} Puebla | CFE
    Expenses:Casa Puebla:CFE                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
