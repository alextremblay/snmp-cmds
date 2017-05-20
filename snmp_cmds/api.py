"""
This module provides a Session class for making multiple SNMP requests to the 
same device. If you plan on making relatively few SNMP requests to relatively 
many SNMP targets, you may want to check out commands.py instead.
"""
# imports for type-checking purposes
from typing import Union, Optional, List, Tuple, Dict

# Internal module imports
from .commands import snmpget, snmpgetsome, snmpwalk, snmptable, snmpset


class Session(object):
    """
    This class represents an open session to a single SNMP target device. 
    Once instantiated, it can be used to make easy and convenient calls to 
    get or set information on that target.
    """
    def __init__(self,
                 ipaddress: str,
                 port: Union[str, int] = 161,
                 read_community: str = 'public',
                 write_community: str = 'private',
                 timeout: Union[int, str] = 3):
        self.ipaddress = ipaddress
        self.port = port
        self.read_community = read_community
        self.write_community = write_community
        self.timeout = timeout

    def get(self, oid: str) -> Optional[str]:
        return snmpget(ipaddress=self.ipaddress, port=self.port, oid=oid,
                       community=self.read_community, timeout=self.timeout)

    def get_some(self, oids: List[str]) -> Optional[List[Tuple[str, str]]]:
        return snmpgetsome(ipaddress=self.ipaddress, port=self.port, oids=oids,
                           community=self.read_community, timeout=self.timeout)

    def get_table(self, oid: str,
                  sortkey: Optional[str] = None) -> List[Dict[str, str]]:
        return snmptable(ipaddress=self.ipaddress, port=self.port, oid=oid,
                         community=self.read_community, timeout=self.timeout,
                         sortkey=sortkey)

    def walk(self, oid: str) -> Optional[List[Tuple[str, str]]]:
        return snmpwalk(ipaddress=self.ipaddress, port=self.port, oid=oid,
                        community=self.read_community, timeout=self.timeout)

    def set(self, oid: str, value_type: str, value: str) -> str:
        return snmpset(ipaddress=self.ipaddress, port=self.port, oid=oid,
                       community=self.read_community, timeout=self.timeout,
                       value_type=value_type, value=value)
