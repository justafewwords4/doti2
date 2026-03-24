import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def gabi(monto: float = 200, info: bool = False):
    """Compra tiempo aire para Gabi"""
    contenido = f"""{graba.now} Tiempo aire | Gabi
    Assets:Bancos:Banorte\t\t\t$-{monto:,.2f}
    Expenses:Tiempo Aire"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def felipe(monto: float = 200, info: bool = False):
    """Compra tiempo aire para Felipe"""
    contenido = f"""{graba.now} Tiempo aire | Felipe
    Assets:Bancos:Banorte\t\t\t$-{monto:,.2f}
    Expenses:Tiempo Aire"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def olga(monto: float = 200, info: bool = False):
    """Compra tiempo aire para Olga"""
    contenido = f"""{graba.now} Tiempo aire | Olga
    Assets:Bancos:Banorte\t\t\t$-{monto:,.2f}
    Expenses:Tiempo Aire"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def david(monto: float = 200, info: bool = False):
    """Compra tiempo aire para David"""
    contenido = f"""{graba.now} Tiempo aire | David
    Assets:Bancos:Banorte\t\t\t$-{monto:,.2f}
    Expenses:Tiempo Aire"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
