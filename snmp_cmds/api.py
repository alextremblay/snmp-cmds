from .commands import snmpget, snmpgetbulk, snmpwalk, snmptable


class Session(object):
    def __init__(self, hostname, community, version):
        raise NotImplementedError
