from .commands import snmpget


class Session(object):
    def __init__(self, hostname, community, version):
        self.agent = hostname
        self.v2_community_string = community
        self.version = '2c' if version == 2 else version

    def get(self, oid):
        return snmpget(self.agent, oid, self.version, self.v2_community_string)
