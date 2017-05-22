"""
This module provides a Session class for making multiple SNMP requests to the 
same device. If you plan on making relatively few SNMP requests to relatively 
many SNMP targets, you may want to check out commands.py instead.
"""
# imports for type-checking purposes
from typing import Union as OneOf, Optional, List, Tuple, Dict

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
                 port: OneOf[str, int] = 161,
                 read_community: str = 'public',
                 write_community: str = 'private',
                 timeout: OneOf[int, str] = 3):
        self.ipaddress = ipaddress
        self.port = port
        self.read_community = read_community
        self.write_community = write_community
        self.timeout = timeout

    def get(self, oid: str) -> Optional[str]:
        """
        A simple convenience wrapper around :func:`~snmp_cmds.commands.snmpget`

        Runs the equivalent of '``snmpget -Oqv -Pe -t {timeout} -r 0 -v 2c 
        -c {community} {host} {oid}``' and parses the result. if the 
        response from the server is a ``No Such Object`` or a 
        ``No Such Instance`` error, this function returns :obj:`None`. 
        Otherwise, it returns the value retrieved from the server

        :param oid: the Object IDentifier to request from the target SNMP 
            server
        :return: the value stored at that OID on the target SNMP server if 
            successful, :obj:`None` otherwise
        :raises `~snmp_cmds.exceptions.SNMPTimeout`: if the target SNMP 
            server fails to respond
        :raises `~snmp_cmds.exceptions.SNMPInvalidAddress`: if the 
            hostname or IP address supplied is not valid or cannot be 
            resolved
        :raises `~snmp_cmds.exceptions.SNMPError`: if the underlying 
            Net-SNMP command produces an unknown or unhandled error
        """
        return snmpget(ipaddress=self.ipaddress, port=self.port, oid=oid,
                       community=self.read_community, timeout=self.timeout)

    def get_some(self, oids: List[str]) -> Optional[List[Tuple[str, str]]]:
        """
        A simple convenience wrapper around 
        :func:`~snmp_cmds.commands.snmpgetsome`

        Runs Net-SNMP's 'snmpget' command on a list of OIDs, and returns 
        a list of tuples of the form (oid, result).

        :param oids: a list of Object IDentifiers to request from the target 
            SNMP server
        :return: a list of tuples of the form (oid, result)
        :raises `~snmp_cmds.exceptions.SNMPTimeout`: if the target SNMP server 
            fails to respond
        :raises `~snmp_cmds.exceptions.SNMPInvalidAddress`: if the hostname or
            IP address supplied is not valid or cannot be resolved
        :raises `~snmp_cmds.exceptions.SNMPError`: if the underlying 
            Net-SNMP command produces an unknown or unhandled error
        """
        return snmpgetsome(ipaddress=self.ipaddress, port=self.port, oids=oids,
                           community=self.read_community, timeout=self.timeout)

    def get_table(self, oid: str, sortkey: Optional[str] = None
                  ) -> OneOf[List[Dict[str, str]], Dict[str, Dict[str, str]]]:
        """
        A simple convenience wrapper around 
        :func:`~snmp_cmds.commands.snmptable`
        
        Runs Net-SNMP's 'snmptable' command on a given OID, converts the results
        into a list of dictionaries, and optionally sorts the list by a 
        given key.

        :param oid: the Object IDentifier to request from the target SNMP server
        :param sortkey: the key within each dict upon which to sort the list of 
            results
        :return: a list of dicts, one for each row of the table. The keys of 
            the dicts correspond to the column names of the table.
        :raises `~snmp_cmds.exceptions.SNMPTimeout`: if the target SNMP server 
            fails to respond
        :raises `~snmp_cmds.exceptions.SNMPInvalidAddress`: if the hostname or
            IP address supplied is not valid or cannot be resolved
        :raises `~snmp_cmds.exceptions.SNMPError`: if the underlying 
            Net-SNMP command produces an unknown or unhandled error
        :raises `~snmp_cmds.exceptions.SNMPTableError`: if the requested OID 
            is not a valid table
        """
        return snmptable(ipaddress=self.ipaddress, port=self.port, oid=oid,
                         community=self.read_community, timeout=self.timeout,
                         sortkey=sortkey)

    def walk(self, oid: str) -> Optional[List[Tuple[str, str]]]:
        """
        A simple convenience wrapper around :func:`~snmp_cmds.commands.snmpwalk`
        
        Runs Net-SNMP's 'snmpget' command on a list of OIDs, and returns a list 
        of tuples of the form (oid, result).

        :param oid: the Object IDentifier to request from the target SNMP 
            server 
        :return: a list of tuples of the form (oid, result)
        :raises `~snmp_cmds.exceptions.SNMPTimeout`: if the target SNMP server 
            fails to respond
        :raises `~snmp_cmds.exceptions.SNMPInvalidAddress`: if the hostname or
            IP address supplied is not valid or cannot be resolved
        :raises `~snmp_cmds.exceptions.SNMPError`: if the underlying 
            Net-SNMP command produces an unknown or unhandled error
        """
        return snmpwalk(ipaddress=self.ipaddress, port=self.port, oid=oid,
                        community=self.read_community, timeout=self.timeout)

    def set(self, oid: str, value_type: str, value: str) -> str:
        """
        A simple convenience wrapper around :func:`~snmp_cmds.commands.snmpset`
        
        Runs Net-SNMP's 'snmpset' command on a given OID, and returns the result 
        if successful.

        :param oid: the Object IDentifier to request from the target SNMP 
            server
        :param value_type: the SNMP value type to set. can be one of 
            (i/u/t/a/o/s/x/d/b)
        :param value: the value to set
        :return: the value that was set on the SNMP target
        :raises `~snmp_cmds.exceptions.SNMPTimeout`: if the target SNMP server 
            fails to respond
        :raises `~snmp_cmds.exceptions.SNMPInvalidAddress`: if the hostname or
            IP address supplied is not valid or cannot be resolved
        :raises `~snmp_cmds.exceptions.SNMPError`: if the underlying 
            Net-SNMP command produces an unknown or unhandled error
        :raises `~snmp_cmds.exceptions.SNMPWriteError`: if the snmpset 
            operation failed for a known reason. The message associated with 
            this error should always contain information regarding the reason 
            for the error.
        """
        return snmpset(ipaddress=self.ipaddress, port=self.port, oid=oid,
                       community=self.read_community, timeout=self.timeout,
                       value_type=value_type, value=value)
