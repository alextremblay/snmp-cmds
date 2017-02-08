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
