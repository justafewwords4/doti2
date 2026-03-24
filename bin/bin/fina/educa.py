import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def gabi(monto: float = 1500, info: bool = False):
    """$1,500.00 para Gabi"""
    contenido = f"""{graba.now} Gabi | Beca
    Assets:Cash:Casa                        $-{monto:,.2f}
    Expenses:Gabi
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def uvm(monto: float = 5001, info: bool = False):
    """Pagar la mensualidad de Gabi"""

    contenido = f"""{graba.now} UVM | Mensualidad Gabi
    Expenses:Educación:Gabi                        ${monto:,.2f}
    Liabilities:Crédito Bancomer
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def david(monto: float = 3000, info: bool = False):
    """Pagar la mensualidad de Gabi"""

    contenido = f"""{graba.now} Wisdowm | Mensualidad David
    Assets:Bancos:Banorte                        ${monto:,.2f}
    Expenses:Educacion:David
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
