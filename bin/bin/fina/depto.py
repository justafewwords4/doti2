import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)

@app.command()
def agua(monto: float, info: bool = False):
    """Agua del departamento"""

    contenido = f"""{graba.now} Departamento | Agua
    Expenses:Departamento:Agua                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)

@app.command()
def leti(monto: float = 700, info: bool = False):
    """Pagar la limpieza del departamento"""

    contenido = f"""{graba.now} Departamento | Leti
    Expenses:Departamento:Limpieza                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def luz(monto: float, info: bool = False):
    """Pagar la luz del departamento"""

    contenido = f"""{graba.now} Departamento | CFE
    Expenses:Departamento:CFE                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def mantto(monto: float = 650, info: bool = False):
    """Pagar mantto del edificio"""

    contenido = f"""{graba.now} Departamento | Mantto
    Expenses:Departamento:Mantto                         ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def telmex(monto: float = 752, info: bool = False):
    """Pago del telefono del departamento"""

    contenido = f"""{graba.now} Telmex
    Expenses:Departamento:Telmex                  ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def fondo(monto: float = 650, info: bool = False):
    """Pago del fondo de reserva"""

    contenido = f"""{graba.now} Departamento | Fondo de reserva
    Expenses:Departamento:Fondo Reserva                  ${monto:,.2f}
    Assets:Bancos:Banorte
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
