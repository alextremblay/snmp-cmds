"""
For these tests, we will use a local snmpsim instance loaded up with snmprec 
files for a cisco chassis, a cisco switch, a nortel stack, and a nortel switch
"""
import pytest

from snmp_cmds import Session

SNMP_SRV_ADDR = '127.0.0.1'
SNMP_SRV_PORT = '10000'
IFTABLE_OID = '.1.3.6.1.2.1.2.2'
SYSDESCR_OID = '.1.3.6.1.2.1.1.1.0'
SYSNAME_OID = '.1.3.6.1.2.1.1.5.0'
SYSLOCATION_OID = '.1.3.6.1.2.1.1.6.0'
SYSTEM_OID = '.1.3.6.1.2.1.1'

@pytest.fixture()
def valid_snmp_server() -> Session:
    session = Session(ipaddress=SNMP_SRV_ADDR, port=SNMP_SRV_PORT)
    return session


@pytest.fixture()
def non_existant_server() -> Session:
    session = Session(ipaddress='123.231.123.231', timeout=1)
    return session


def test_api_get(valid_snmp_server: Session):
    """
    Make sure the API's get method completes without errors
    """
    result = valid_snmp_server.get(SYSDESCR_OID)
    assert type(result) is str


def test_api_get_bulk(valid_snmp_server: Session):
    """
    Make sure the API's get_bulk method completes without errors
    """
    result = valid_snmp_server.get_bulk(
        oids=[SYSDESCR_OID, SYSLOCATION_OID, SYSNAME_OID]
    )
    assert type(result) is list
    assert type(result[0]) is tuple
    assert type(result[0][0]) is str
    assert type(result[0][1]) is str


def test_api_get_table(valid_snmp_server: Session):
    """
    Make sure the API's get_table method completes without errors
    """
    result = valid_snmp_server.get_table(oid=IFTABLE_OID, sortkey='ifIndex')
    assert type(result) is list
    assert type(result[0]) is dict
    assert type(result[0]['ifIndex']) is str


def test_api_walk(valid_snmp_server: Session):
    """
    Make sure the API's walk method completes without errors
    """
    result = valid_snmp_server.walk(oid=IFTABLE_OID)
    assert type(result) is list
    assert type(result[0]) is tuple
    assert type(result[0][0]) is str
    assert type(result[0][1]) is str


def test_api_set(valid_snmp_server: Session):
    """
    Make sure the API's set method completes without errors
    """
    result = valid_snmp_server.set(oid=SYSNAME_OID, value_type='s',
                                   value='Test String')
    assert type(result) is str