import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def tc(monto: float, info: bool = False):
    """Pagar tarjeta de crédito"""
    contenido = f"""{graba.now} Pago tarjeta de crédito
    Assets:Bancos:Bancomer               $-{monto:,.2f}
    Liabilities:Crédito Bancomer
    """
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def cajero(monto: float, info: bool = False):
    """Saca efectivo de la cuenta de Bancomer"""
    contenido = f"""{graba.now} Retiro cajero Bancomer | Casa
    Assets:Bancos:Bancomer\t\t$-{monto:,.2f}
    Assets:Cash:Casa\t\t\t ${monto:,.2f}"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def bb(monto: float, info: bool = False):
    """Traspasa dinero de Bancomer a banorte"""
    contenido = f"""{graba.now} Traspaso
    Assets:Bancos:Bancomer\t\t$-{monto:,.2f}
    Assets:Bancos:Banorte"""
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
