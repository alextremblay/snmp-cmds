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

    Exception raised when an SNMP command is unable to identify a host.

    """

    def __init__(self, ip):
        self.IP = ip
        self.message = "Unknown host: " + ip
        super(SNMPUnknownHost, self).__init__(self.message)


class SNMPValueError(Exception):
    """

    Exception raised when an SNMP command returns a 'No Such Object' or 'No Such Instance' message

    """

    def __init__(self, mib, oid, ip):
        self.mib = mib
        self.oid = oid
        self.ip = ip
        self.message = "No value was found at this OID on this device. \n " \
                       "OID={0}::{1} \n Device={2}".format(self.mib, self.oid, self.ip)
        super(SNMPValueError, self).__init__(self.message)
