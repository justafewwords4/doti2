import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def cf(monto: float, info: bool = False):
    """Transacción en efectivo de casa a felipe"""

    contenido = f"""{graba.now} Traspaso
    Assets:Cash:Casa\t\t$-{monto:,.2f}
    Assets:Cash:Felipe"""

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def co(monto: float, info: bool = False):
    """Transacción en efectivo de casa a olga"""

    contenido = f"""{graba.now} Traspaso
    Expenses:Oga  \t\t${monto:,.2f}
    Assets:Cash:Casa"""

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def fo(monto: float, info: bool = False):
    """Transacción en efectivo de felipe a olga"""

    contenido = f"""{graba.now} Traspaso
    Assets:Cash:Felipe\t\t$-{monto:,.2f}
    Assets:Cash:Olga"""

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def of(monto: float, info: bool = False):
    """Transacción en efectivo de olga a felipe"""

    contenido = f"""{graba.now} Traspaso
    Assets:Cash:Olga\t\t$-{monto:,.2f}
    Assets:Cash:Felipe"""

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
