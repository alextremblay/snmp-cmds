from snmp_cmds.helpers import snmp_command
from snmp_cmds.commands import snmpget
from snmp_cmds.api import Session
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
import pytest


@pytest.fixture()
def conf():
    config = ConfigParser()
    config.read(['variables.cfg', 'tests/variables.cfg'])
    return config


@pytest.fixture()
def oid():
    oids = {
        'sysName': '.1.3.6.1.2.1.1.5.0',
        'sysDescr': '.1.3.6.1.2.1.1.1.0',
        'ifNumber': '.1.3.6.1.2.1.2.1.0',
        'ifTable': '.1.3.6.1.2.1.2.2.1',
        'ifIndex': '.1.3.6.1.2.1.2.2.1.1',
        'ifDescr': '.1.3.6.1.2.1.2.2.1.2',
        'ifType': '.1.3.6.1.2.1.2.2.1.3',
        'ifPhysAddress': '.1.3.6.1.2.1.2.2.1.6',
        'ifXTable': '.1.3.6.1.2.1.31.1.1.1',
        'ifName': '.1.3.6.1.2.1.31.1.1.1.1',
        'ifAlias': '.1.3.6.1.2.1.31.1.1.1.18',
        'dot1qVlanStaticName': '.1.3.6.1.2.1.17.7.1.4.3.1.1',
        'cisco': {
            'nativeVlan':
            '.1.3.6.1.4.1.9.9.68.1.2.2.1.2',  # VlanMembership_vmVlan
            # from CISCO-VLAN-MEMBERSHIP-MIB
            'vlanTable': ''
        },
        'nortel': {
            'nativeVlan':
            '.1.3.6.1.4.1.2272.1.3.3.1.7',  # rcVlanPortDefaultVlanId
            # from RC-VLAN-MIB
            'vlanTable': ''
        },
    }
    return oids


def test_basic(conf, oid):
    cstring = conf.get('auth', 'comm string')
    nortel1 = conf.get('test variables', 'nortel 1 ip')
    cisco1 = conf.get('test variables', 'cisco 1 ip')
    print snmp_command('snmpget', nortel1, oid['sysDescr'], '-v', '2c', '-c',
                       cstring)
    print snmp_command('snmpget', nortel1, oid['ifNumber'], '-v', '2c', '-c',
                       cstring)
    print snmp_command('snmpget', nortel1, oid['ifIndex'], '-v', '2c', '-c',
                       cstring)
    print snmp_command('snmpget', cisco1, oid['sysDescr'], '-v', '2c', '-c',
                       cstring)
    print snmp_command('snmpget', cisco1, oid['ifNumber'], '-v', '2c', '-c',
                       cstring)
    print snmp_command('snmpget', cisco1, oid['ifIndex'], '-v', '2c', '-c',
                       cstring)


def test_snmpget(conf, oid):
    comm_str = conf.get('auth', 'comm string')
    ip_list = [
        conf.get('test variables', 'cisco 1 ip'),
        conf.get('test variables', 'nortel 1 ip')
    ]
    for ip in ip_list:
        print snmpget(ip, oid['sysDescr'], v2_community_string=comm_str)
        print snmpget(ip, oid['sysName'], v2_community_string=comm_str)
        print snmpget(ip, oid['ifNumber'], v2_community_string=comm_str)
        print snmpget(ip, oid['ifIndex'] + '.1', v2_community_string=comm_str)
        print snmpget(ip, oid['ifDescr'] + '.1', v2_community_string=comm_str)
        print snmpget(ip, oid['ifType'] + '.1', v2_community_string=comm_str)


def test_api(conf, oid):
    ip = conf.get('test variables', 'cisco 1 ip')
    community_string = conf.get('auth', 'comm string')
    print 'Session Test'
    print Session(
        hostname=ip, community=community_string,
        version=2).get(oid['sysName']).value
