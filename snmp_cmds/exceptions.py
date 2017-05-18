class SNMPError(Exception):
    """
    We'll use this error class or a subclass anytime we receive an error from 
    an underlying net-snmp command we run
    """


class SNMPTableError(SNMPError):
    """
    This error will be thrown when the snmptable command is called with an 
    OID that isn't a table
    """
    def __init__(self, oid):
        self.oid = oid
        self.message = "The snmptable command could not identify {oid} as a \
table. Please be sure the OID is correct, and that your net-snmp installation \
has a MIB available for that OID.".format(oid=oid)
        super().__init__(self.message)


class SNMPTimeout(SNMPError):
    """
    Exception raised when an SNMP command times out connecting to host.
    """

    def __init__(self, ip):
        self.IP = ip
        self.message = "Timeout while trying to connect to {ip}\n Either the \
device is offline, or the SNMP credentials provided were incorrect."\
            .format(ip=ip)
        super().__init__(self.message)


class SNMPInvalidAddress(SNMPError):
    """
    Exception raised when the address validation helper function failed to 
    identify the host as either a valid hostname or a valid IP address.
    """

    def __init__(self, host):
        self.host = host
        self.message = "{0} does not appear to be a valid hostname / IP \
address".format(host)
        super().__init__(self.message)


class SNMPWriteError(SNMPError):
    """
    Exception raised when a call to snmpset fails with an snmpset-specific 
    error message
    """
