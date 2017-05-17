# Standard Library imports
from ipaddress import ip_address
from socket import getaddrinfo, gaierror

# imports for type-hinting purposes
from subprocess import CompletedProcess

# Internal module imports
from .exceptions import SNMPError


def validate_ip_address(ipaddress: str) -> str:
    """
    convert the IP Address string into an IPv4Address or IPv6Address
    then back into a string. This is a cheap and easy way to do IP
    address validation. If the string is not a valid address,
    a ValueError will be raised
    """
    try:
        ipaddr = getaddrinfo(ipaddress, None)[0][4][0]
        ipaddr = ip_address(ipaddr)
        return str(ipaddr)
    except (gaierror, ValueError):
        raise SNMPError("Invalid Address: {0} does not appear to be a valid "
                        "hostname / IP address".format(ipaddress))


def check_for_timeout(cmd: CompletedProcess, ipaddress: str, port: str) -> None:
    """
    look for a timeout condition in the completed command's output and raise 
    an error if needed
    :param cmd: 
    :param ipaddress: 
    :param port: 
    :return: 
    """
    if b'No Response from' in cmd.stderr:
        raise SNMPError(
            "Timeout: no response received from {0}:{1}".format(
                ipaddress, port)
        )


def handle_unknown_error(cmdstr: str, cmd: CompletedProcess) -> None:
    """
    Catch-all for any unhandled error message. Raises an Error showing the 
    snmp command attempted, and the error message received.
    :param cmdstr: 
    :param cmd: 
    :return: 
    """
    raise ChildProcessError(
        "The SNMP command failed. \nAttempted Command: {0}\n Error received: "
        "{1}".format(cmdstr, str(cmd.stderr))
    )
