import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def suegra(monto: float = 3000, info: bool = False):
    """Catorcena doña Marta"""

    contenido = f"""{graba.now} Ayudas | Suegra
    Assets:Bancos:Bancomer               $-{monto:,.2f}
    Expenses:Suegra
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def ofrenda(monto: float, info: bool = False):
    """Ofrendas"""

    contenido = f"""{graba.now} Ofrendas
    Expenses:Ofrendas                         ${monto:,.2f}
    Assets:Cash:Felipe
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
