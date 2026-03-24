import os
from datetime import date, timedelta

now = date.today()
ledger_file = "/home/felipe/.hledger.journal"


def graba(contenido):
    """Graba el contenido al archivo `ledger_file`"""

    print(contenido)
    contenido = "\n" + contenido
    os.system(f"echo '{contenido}' >> {ledger_file}")
