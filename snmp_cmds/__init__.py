from .commands import snmpset, snmptable, snmpgetsome, snmpget, snmpwalk
from .exceptions import SNMPError, SNMPWriteError, SNMPInvalidAddress, \
    SNMPTimeout, SNMPTableError
from .api import Session

# Run a test on import to ensure the net-snmp binaries are installed.
from subprocess import run, DEVNULL
from os import getenv
if not getenv("READTHEDOCS"): # DON'T run this check if we're building
    # documentation on ReadTheDocs
    try:
        run('snmpget', stdout=DEVNULL, stderr=DEVNULL)
    except (FileNotFoundError, OSError):
        raise ImportError(
            'Net-SNMP does not appear to be installed on this system, '
            'or the Net-SNMP commands are not on your PATH'
        )
del run, DEVNULL
