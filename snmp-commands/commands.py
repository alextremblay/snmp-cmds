# TODO: Module Docs
"""
"""

from collections import namedtuple
import sys
import re
sys.path.append('modules')

# import sh if available. If sh is imported into a module on Windows, it raises an ImportError
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


class SNMPTimeout(Exception):
    """
    Exception raised when an SNMP command times out connecting to host.
    """

    def __init__(self, ip):
        self.IP = ip
        self.message = "Timeout while trying to connect to {ip}\n Either the device is offline, or the " \
                       "SNMP credentials provided were incorrect.".format(ip=ip)
        super(SNMPTimeout, self).__init__(self.message)


class SNMPUnknownHost(Exception):
    """
    Exception raised when an SNMP command is unable to identify a host host.
    """

    def __init__(self, ip):
        self.IP = ip
        self.message = "Unknown host: " + ip
        super(SNMPUnknownHost, self).__init__(self.message)


# This named tuple will be used as the return value for every snmp command. that way users will be able to access all of
#  the return values with dot notation. (ex. result.value)
_SNMPResult = namedtuple('SNMPResult', ['mib', 'oid', 'type', 'value'])


# This is the baseline command shared by all of the user-accessible snmp commands
# TODO: implement more thorough error handling
# TODO: implement handling results, instead of just passing them up
def _snmp_command(command, *args):
    cmd = sh.Command(command)
    try:
        result = cmd(*args)
    except ErrorReturnCode as e:
        print(e.stderr)
        if re.search('Timeout', e.stderr):
            host = re.search('Timeout: No Response from (.*)\.', e.stderr, re.MULTILINE).group(1)
            raise SNMPTimeout(host)
        elif re.search('Unknown host', e.stderr):
            host = re.search('Unknown host \((.*?)\)', e.stderr, re.MULTILINE).group(1)
            raise SNMPUnknownHost(host)
        else:
            raise
    else:
        return result


def snmpget(agent, oid, version=None, community_string=None):
    options = []
    if version:
        options.extend(['-v', version])
    if community_string:
        options.extend(['-c', community_string])

    options.extend([agent, oid])

    return _snmp_command('snmpget', *options)


print(snmpget('10.13.112.10', '.1.3.6.1.2.1.1.5.0', version='3', community_string=''))
