# Python Standard Library imports
from collections import namedtuple
import sys
import re

# Internal module imports
from .exceptions import SNMPValueError, SNMPUnknownHost, SNMPTimeout

# External module imports
# import sh if available. If sh is imported on Windows, it raises an ImportError
try:
    import sh  # External module sh. Does not work on windows
    from sh import ErrorReturnCode, CommandNotFound
except ImportError:
    import pbs as sh  # External module pbs. Predecessor to and functionally identical to sh. Works on windows.
    from pbs import ErrorReturnCode, CommandNotFound
# Perform a basic test during import to ensure net-snmp is installed.
try:
    sh.Command('snmpget')()
except (OSError, CommandNotFound):
    sys.tracebacklimit = 0
    raise ImportError('Net-SNMP does not appear to be installed on this system, '
                      'or the Net-SNMP commands are not on your PATH')
except ErrorReturnCode:
    pass

# This named tuple will be used as the return value for every snmp command. that way users will be able to access all of
#  the return values with dot notation. (ex. result.value)
SNMPResult = namedtuple('SNMPResult', ['mib', 'oid', 'type', 'value'])


# This is the baseline command shared by all of the user-accessible snmp commands
def snmp_command(command, ip, oid, *args):
    cmd = sh.Command(command)
    options = list(args)
    options.extend([ip, oid])
    try:
        result = cmd(*options)
    except ErrorReturnCode as e:

        # If the word timeout shows up in the error message returned from the shell command, we should raise a
        # timeout error
        if re.search('Timeout', e.stderr):
            host = re.search('Timeout: No Response from (.*)\.', e.stderr, re.MULTILINE).group(1)
            raise SNMPTimeout(host)

        # If the phrase Unknown host shows up in the error message returned from the shell command, we should raise an
        # unknownhost error
        elif re.search('Unknown host', e.stderr):
            host = re.search('Unknown host \((.*?)\)', e.stderr, re.MULTILINE).group(1)
            raise SNMPUnknownHost(host)

        # If we get any other error message from the shell command, we should re-raise it since we don't know how to
        # handle it.
        else:
            raise

    else:
        return result
