"""
For these tests, we will use a local snmpsim instance loaded up with snmprec 
files for a cisco chassis, a cisco switch, a nortel stack, and a nortel switch
"""
import pytest

from snmp_cmds import snmpwalk, snmpget, snmpgetsome, snmptable, snmpset
from snmp_cmds import SNMPError, SNMPTimeout, SNMPInvalidAddress, \
    SNMPTableError, SNMPWriteError

SNMP_SRV_ADDR = '127.0.0.1'
SNMP_SRV_PORT = '10000'
IFTABLE_OID = '.1.3.6.1.2.1.2.2'
SYSDESCR_OID = '.1.3.6.1.2.1.1.1.0'

snmp_commands = [
    snmpget,
    snmpwalk,
    snmptable,
]


def test_snmp_invalid_address():
    """
    all snmp commands should implement the check_invalid_address function
    """
    for command in snmp_commands:
        with pytest.raises(SNMPInvalidAddress) as excinfo:
            command(oid='some-irelevant-oid', community='public',
                    ipaddress='invalid-hostname', )
        assert 'does not appear to be a valid' in str(excinfo.value)
    with pytest.raises(SNMPInvalidAddress) as excinfo:
        snmpgetsome(oids=['some-irelevant-oid'], community='public',
                    ipaddress='invalid-hostname', )
    assert 'does not appear to be a valid' in str(excinfo.value)


@pytest.mark.slow
def test_snmp_timeout():
    """
    all snmp commands should implement the check_timeout function
    """
    for command in snmp_commands:
        with pytest.raises(SNMPTimeout) as excinfo:
            command(ipaddress='10.0.0.1', oid='IF-MIB::ifTable', timeout='1')
        assert 'Timeout' in str(excinfo.value)

    with pytest.raises(SNMPTimeout) as excinfo:
        snmpgetsome(ipaddress='10.0.0.1', oids=['IF-MIB::ifTable'], timeout='1')
    assert 'Timeout' in str(excinfo.value)

    with pytest.raises(SNMPTimeout) as excinfo:
        snmpset(community='public', ipaddress='10.0.0.1',
                oid='IF-MIB::ifTable', value_type='s',
                value='random string', timeout='1')
    assert 'Timeout' in str(excinfo.value)


def test_snmptable_return_structure():
    """
    snmptable return data should be a list of dicts containing info about 
    each row in the table
    """
    iftable = snmptable(community='public', ipaddress=SNMP_SRV_ADDR,
                        oid=IFTABLE_OID, port=SNMP_SRV_PORT, sortkey='ifIndex')
    assert isinstance(iftable, list)
    assert isinstance(iftable[0], dict)
    assert isinstance(iftable[0]['ifDescr'], str)
    assert iftable[1]['ifDescr'] == 'eth0'


def test_snmptable_wrong_oid():
    """
    The "Unknown Object Identifier" error produced by net-snmp commands 
    contains useful information regarding the OID attempted. rather than try 
    to extract it with a regex and handle this issue with an SNMPError, 
    I figure it's probably better to just bubble up the error message 
    produced by the net-snmp command as a generic SNMPError
    """
    with pytest.raises(SNMPError):
        snmptable(community='public', ipaddress=SNMP_SRV_ADDR,
                  oid='WRONG-MIB::Bogus-Table', port=SNMP_SRV_PORT)


def test_snmptable_not_table():
    """
    the snmptable function should give us an SNMPError if it's given an OID 
    which is not a table.
    """
    with pytest.raises(SNMPTableError) as excinfo:
        snmptable(community='public', ipaddress=SNMP_SRV_ADDR,
                  oid='IF-MIB::ifEntry', port=SNMP_SRV_PORT)
    assert 'could not identify IF-MIB::ifEntry as a table' in str(excinfo.value)


def test_snmpget_return_structure():
    """
    The snmpget function takes one OID, and should give us that OID's value 
    as a string
    """
    result = snmpget(community='public', ipaddress=SNMP_SRV_ADDR,
                     oid=SYSDESCR_OID, port=SNMP_SRV_PORT)
    assert 'Linux' in result
    assert isinstance(result, str)


def test_snmpget_no_such_instance():
    """
    If a given OID is not available on the target "No Such Instance" / "No Such 
    Object", the result should be a null value so we can truth-test it. ex.: 
    if result:
        # do stuff
    """
    result = snmpget(community='public', ipaddress=SNMP_SRV_ADDR,
                     oid='SNMPv2-MIB::sysName', port=SNMP_SRV_PORT)
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
    result = snmpgetsome(community='public', ipaddress=SNMP_SRV_ADDR,
                         oids=oids, port=SNMP_SRV_PORT)
    assert isinstance(result, list)
    assert len(result) == len(oids)
    assert isinstance(result[0], tuple)
    assert isinstance(result[0][0], str)
    assert isinstance(result[0][1], str)
    assert result[1][0] == '.1.3.6.1.2.1.2.2.1.2.1'
    assert result[1][1] == 'lo'


def test_snmpgetbulk_return_contains_no_such_instance():
    """
    If one of the OIDs we request from a server isn't available, 
    that specific result should be a null value. all other results in the 
    list should still be valid results (OID values)
    """
    oids = ['IF-MIB::ifTable.1.1.1', 'IF-MIB::ifTable.1.2.1',
            'IF-MIB::ifTable.1.3']
    result = snmpgetsome(community='public', ipaddress=SNMP_SRV_ADDR,
                         oids=oids, port=SNMP_SRV_PORT)
    assert isinstance(result[1][1], str)
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
    result = snmpgetsome(community='multiline-test', ipaddress=SNMP_SRV_ADDR,
                         oids=oids, port=SNMP_SRV_PORT)
    assert len(result) is 3
    assert isinstance(result[1], tuple)
    assert '\n' in result[1][1]


@pytest.mark.slow
def test_snmpwalk_return_structure():
    """
    The snmpwalk function should give us a list of tuples, one for each OID 
    walked. Each touple should contain the OID walked and the value of that 
    OID on the server.
    """
    result = snmpwalk(community='public', ipaddress=SNMP_SRV_ADDR,
                      oid='IF-MIB::ifTable', port=SNMP_SRV_PORT)
    assert isinstance(result, list)
    assert isinstance(result[0], tuple)
    assert isinstance(result[0][0], str) and isinstance(result[0][1], str)
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
    result = snmpwalk(community='multiline-test', ipaddress=SNMP_SRV_ADDR,
                      oid='SNMPv2-MIB::system', port=SNMP_SRV_PORT)
    assert isinstance(result[0], tuple)
    assert '\n' in result[0][1]


def test_snmpset_return_structure():
    """
    On success, snmpset should return a string detailing the OID that was 
    updated, and the value that was set
    """
    result = snmpset(ipaddress=SNMP_SRV_ADDR, community='public',
                     oid='SNMPv2-MIB::sysName.0', value_type='s',
                     value='Test Description', port=SNMP_SRV_PORT)
    assert 'Test Description' in result


def test_snmpset_unwritable_field():
    """
    When an attempt is made to write to a field the target device doesn't 
    support writing to, net-snmp's snmpget command produces a "No Such 
    Instance" error. Our function should replicate this
    """
    with pytest.raises(SNMPWriteError) as excinfo:
        snmpset(ipaddress=SNMP_SRV_ADDR, oid='SNMPv2-MIB::sysDescr.0',
                community='public', value_type='s',
                value='Test Description', port=SNMP_SRV_PORT)
    assert 'No Such Instance' in str(excinfo.value)


def test_snmpset_non_existant_type():
    """
    There are a specific set of type codes which net-snmp's snmpset command 
    will accept. Our function should raise an SNMPWriteError if none of those 
    are specified
    """
    with pytest.raises(SNMPWriteError) as excinfo:
        snmpset(ipaddress=SNMP_SRV_ADDR, community='public',
                oid='SNMPv2-MIB::sysName.0', value_type='z',
                value='Test Description', port=SNMP_SRV_PORT)
    assert str(excinfo.value) == 'The type value you specified does not ' \
                                 'match one of the accepted type codes.\n' \
                                 'Valid type codes are one of ' \
                                 '(i|u|t|a|o|s|x|d|b)'


def test_snmpset_wrong_type():
    """
    When an attempt is made to set a variable of one type (an integer, 
    for example) with a value of another type (say, a string), our function 
    should raise an SNMPWriteError to let us know this is not OK.
    """
    with pytest.raises(SNMPWriteError) as excinfo:
        snmpset(ipaddress=SNMP_SRV_ADDR, oid='SNMPv2-MIB::sysName.0',
                value_type='a', value='255.255.255.255', port=SNMP_SRV_PORT)
    assert 'Bad variable type' in str(excinfo.value)


def test_snmpset_value_out_of_range_error():
    """
    If an attempt is made to write a value to an OID which is larger than the 
    max allowable size for that OID, an SNMPWriteError should be raised to let 
    us know 
    """
    with pytest.raises(SNMPWriteError) as excinfo:
        snmpset(ipaddress=SNMP_SRV_ADDR, oid='SNMPv2-MIB::sysName.0',
                value_type='s', value='Thiiiiiiiiiiiiiiiiiiiiiiiiiiiiis '
                'sssssttttttttrrrriiiiiiiiiiiiiiinnnnnnnnnnnnng is '
                'wwwwwwaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaayyyyyyyyyy '
                'tttoooooooooooooooooooooooooooooooooooooooooooooo '
                'lllooooooooooooooooooooooonnnnnnnnnnnnnnnnnnnggggg'
                ' !!!!!!!!!!!!!!!!!!!!!!!!!!!!', port=SNMP_SRV_PORT)
    assert 'Value out of range' in str(excinfo.value)
