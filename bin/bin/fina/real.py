import typer

from . import graba

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

app = typer.Typer(context_settings=CONTEXT_SETTINGS, no_args_is_help=True)


@app.command()
def seguros(info: bool = False):
    """Agrega los movimientos de los seguros"""
    contenido = f"""{graba.now} A07069
    Assets:Bancos:Bancomer        $-281.51
    Expenses:Autos:Seguros         $281.51

{graba.now} A07069
    Assets:Bancos:Bancomer        $-162.00
    Expenses:Autos:Seguros         $162.00

{graba.now} A07069
    Assets:Bancos:Bancomer         $-67.00
    Expenses:Autos:Seguros          $67.00

{graba.now} A07069
    Assets:Bancos:Bancomer      $-1,089.17
    Expenses:Salud:Seguros       $1,089.17

{graba.now} A07069
    Assets:Bancos:Bancomer        $-387.40
    Expenses:Autos:Seguros         $387.40

{graba.now} A07069
    Assets:Bancos:Bancomer        $-405.11
    Expenses:Autos:Seguros         $405.11
    """

    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def bono(monto: float = 19241.00, info: bool = False):
    """Agrega el bono"""
    contenido = f"""{graba.now} Bono
    Income:Pemex               $-{monto:,.2f}
    Assets:Bancos:Bancomer      ${monto:,.2f}
    """
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


@app.command()
def catorce(monto: float = 28773.91, info: bool = False):
    """Agrega la catorcena"""
    contenido = f"""{graba.now} Catorcena
    Income:Pemex               $-{monto:,.2f}
    Assets:Bancos:Bancomer      ${monto:,.2f}
    """
    if info:
        print(contenido)
    else:
        graba.graba(contenido)


if __name__ == "__main__":
    app()
