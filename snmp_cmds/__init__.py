
# Run a test on import to ensure the net-snmp binaries are installed.
from subprocess import run, DEVNULL
try:
    run('snmpget', stdout=DEVNULL, stderr=DEVNULL)
except (FileNotFoundError, OSError):
    raise ImportError(
        'Net-SNMP does not appear to be installed on this system, '
        'or the Net-SNMP commands are not on your PATH'
    )
del run, DEVNULL
