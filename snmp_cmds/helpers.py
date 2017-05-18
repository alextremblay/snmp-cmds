# Standard Library imports
from ipaddress import ip_address
from socket import getaddrinfo, gaierror

# Internal module imports
from .exceptions import SNMPError, SNMPTimeout, SNMPInvalidAddress


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
        raise SNMPInvalidAddress(ipaddress)


def check_for_timeout(cmderr: bytes, host: str) -> None:
    """
    look for a timeout condition in the completed command's output and raise 
    an error if needed
    :param cmderr: the called process's stderr output
    :param host:
    """
    if b'No Response from' in cmderr:
        raise SNMPTimeout(host)


def handle_unknown_error(cmdstr: str, cmderr: bytes) -> None:
    """
    Catch-all for any unhandled error message coming from one of the net-smnp 
    commands. Raises an SNMPError showing the snmp command attempted, and the 
    error message received.
    :param cmdstr: the full command sent to subprocess
    :param cmderr: the called process's stderr output
    """
    raise SNMPError(
        "The SNMP command failed. \nAttempted Command: {0}\n Error received: "
        "{1}".format(cmdstr, cmderr)
    )
