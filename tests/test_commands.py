"""
For these tests, we will use a local snmpsim instance loaded up with snmprec 
files for a cisco chassis, a cisco switch, a nortel stack, and a nortel switch
"""
import pytest

from snmp_cmds import commands, exceptions

SNMP_SRV_ADDR = '127.0.0.1'
SNMP_SRV_PORT = '10000'
IFTABLE_OID = '.1.3.6.1.2.1.2.2'
SYSDESCR_OID = '.1.3.6.1.2.1.1.1.0'

snmp_commands = [
    commands.snmpget,
    commands.snmpgetbulk,
    commands.snmpwalk,
    commands.snmptable,
]


def test_snmp_invalid_address():
    """
    all snmp commands should implement the check_invalid_address function
    """
    for command in snmp_commands:
        with pytest.raises(exceptions.SNMPInvalidAddress) as excinfo:
            command('public', 'invalid-hostname', 'some-irelevant-oid')
        assert 'does not appear to be a valid' in str(excinfo.value)


@pytest.mark.slow
def test_snmp_timeout():
    """
    all snmp commands should implement the check_timeout function
    """
    for command in snmp_commands:
        with pytest.raises(exceptions.SNMPTimeout) as excinfo:
            command('cisco-chassis', '10.0.0.1', 'IF-MIB::ifTable', timeout='1')
        assert 'Timeout' in str(excinfo.value)


def test_snmptable_return_structure():
    """
    snmptable return data should be a list of dicts containing info about 
    each row in the table
    """
    iftable = commands.snmptable('cisco-switch', SNMP_SRV_ADDR, IFTABLE_OID,
                                 SNMP_SRV_PORT, sortkey='ifIndex')
    assert type(iftable) is list
    assert type(iftable[0]) is dict
    assert type(iftable[0]['ifDescr']) is str
    assert iftable[0]['ifDescr'] == 'Vlan1'


def test_snmptable_wrong_oid():
    """
    The "Unknown Object Identifier" error produced by net-snmp commands 
    contains useful information regarding the OID attempted. rather than try 
    to extract it with a regex and handle this issue with an SNMPError, 
    I figure it's probably better to just bubble up the error message 
    produced by the net-snmp command as a generic SNMPError
    """
    with pytest.raises(exceptions.SNMPError):
        commands.snmptable('cisco-chassis', SNMP_SRV_ADDR,
                           'WRONG-MIB::Bogus-Table', SNMP_SRV_PORT)


def test_snmptable_not_table():
    """
    the snmptable function should give us an SNMPError if it's given an OID 
    which is not a table.
    """
    with pytest.raises(exceptions.SNMPTableError) as excinfo:
        commands.snmptable('cisco-chassis', SNMP_SRV_ADDR, 'IF-MIB::ifEntry',
                           SNMP_SRV_PORT)
    assert 'could not identify IF-MIB::ifEntry as a table' in str(excinfo.value)


def test_snmpget_return_structure():
    """
    The snmpget function takes one OID, and should give us that OID's value 
    as a string
    """
    result = commands.snmpget('cisco-switch', SNMP_SRV_ADDR, SYSDESCR_OID,
                              SNMP_SRV_PORT)
    assert 'Cisco IOS Software' in result
    assert type(result) is str


def test_snmpget_no_such_instance():
    """
    If a given OID is not available on the target "No Such Instance" / "No Such 
    Object", the result should be a null value so we can truth-test it. ex.: 
    if result:
        # do stuff
    """
    result = commands.snmpget('cisco-switch', SNMP_SRV_ADDR,
                              'SNMPv2-MIB::sysName', SNMP_SRV_PORT)
    assert result is None


def test_snmpgetbulk_return_structure():
    """
    The snmpgetbulk function should give us a tuple for each OID we 
    give it. First element of the tuple should be the OID requested, 
    and the second element should be the value of that OID on the 
    target server. All returned tuples should be arranged in a list.
    """
    oids = ['IF-MIB::ifTable.1.1.1', 'IF-MIB::ifTable.1.2.1',
            'IF-MIB::ifTable.1.3.1']
    result = commands.snmpgetbulk('cisco-switch', SNMP_SRV_ADDR, oids,
                                  SNMP_SRV_PORT)
    assert type(result) is list
    assert len(result) == len(oids)
    assert type(result[0]) is tuple
    assert type(result[0][0]) is str
    assert type(result[0][1]) is str
    assert result[1][0] == '.1.3.6.1.2.1.2.2.1.2.1'
    assert result[1][1] == 'Vlan1'


def test_snmpgetbulk_return_contains_no_such_instance():
    """
    If one of the OIDs we request from a server isn't available, 
    that specific result should be a null value. all other results in the 
    list should still be valid results (OID values)
    """
    oids = ['IF-MIB::ifTable.1.1.1', 'IF-MIB::ifTable.1.2.1',
            'IF-MIB::ifTable.1.3']
    result = commands.snmpgetbulk('cisco-switch', SNMP_SRV_ADDR, oids,
                                  SNMP_SRV_PORT)
    assert type(result[1][1]) is str
    assert result[2][0] == '.1.3.6.1.2.1.2.2.1.3'
    assert result[2][1] is None


def test_snmpgetbulk_return_contains_multiline_output():
    """
    there is an unfortunate bug / oversight in the net-snmp commands where 
    newline characters within SNMP variables returned from a server are not 
    escaped before printing. 
    If you do an snmpget for 3 oids you'll get 3 lines of output printed :)
    But if one of those 3 variables contains, say, 2 new-line chars in it, 
    you'll get 5 lines of output :(
    our snmpgetbulk function should detect whether a given line of output is 
    an oid-value pair or a continuation of the value from the last pair and 
    act accordingly
    """
    oids = ['IF-MIB::ifTable.1.1.1', 'SNMPv2-MIB::sysDescr.0',
            'IF-MIB::ifTable.1.3']
    result = commands.snmpgetbulk('cisco-switch', SNMP_SRV_ADDR, oids,
                                  SNMP_SRV_PORT)
    assert len(result) is 3
    assert type(result[1]) is tuple
    assert '\n' in result[1][1]


@pytest.mark.slow
def test_snmpwalk_return_structure():
    """
    The snmpwalk function should give us a list of tuples, one for each OID 
    walked. Each touple should contain the OID walked and the value of that 
    OID on the server.
    """
    result = commands.snmpwalk('cisco-switch', SNMP_SRV_ADDR, 'IF-MIB::ifTable',
                               SNMP_SRV_PORT)
    assert type(result) is list
    assert type(result[0]) is tuple
    assert type(result[0][0]) is str and type(result[0][1]) is str
    assert result[0][0] == '.1.3.6.1.2.1.2.2.1.1.1'
    assert result[0][1] == '1'


def test_snmpwalk_return_contains_multiline_output():
    """
    there is an unfortunate bug / oversight in the net-snmp commands where 
    newline characters within SNMP variables returned from a server are not 
    escaped before printing. 
    If you do an snmpget for 3 oids you'll get 3 lines of output printed :)
    But if one of those 3 variables contains, say, 2 new-line chars in it, 
    you'll get 5 lines of output :(
    our snmpwalk function should detect whether a given line of output is 
    an oid-value pair or a continuation of the value from the last pair and 
    act accordingly
    """
    result = commands.snmpwalk('cisco-switch', SNMP_SRV_ADDR,
                               'SNMPv2-MIB::system', SNMP_SRV_PORT)
    assert type(result[0]) is tuple
    assert '\n' in result[0][1]
