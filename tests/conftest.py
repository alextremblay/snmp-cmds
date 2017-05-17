"""
We're using snmpsim to simulate various target devices for our tests. 
Before we do anything, we should probably make sure it's actually running
"""
import pytest

from subprocess import run, PIPE

SNMP_TEST_SRV_HOST = '127.0.0.1:10000'
SNMP_TEST_SRV_COMM_STR = 'cisco-switch'
IFTABLE_OID = '.1.3.6.1.2.1.2.2'
SYSDESCR_OID = '.1.3.6.1.2.1.1.1.0'


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    """
    We're using snmpsim to simulate various target devices for our tests. 
    Before we do anything, we should probably make sure it's actually running
    """
    test = run(['snmpget', '-v', '2c', '-c', SNMP_TEST_SRV_COMM_STR,
         SNMP_TEST_SRV_HOST, SYSDESCR_OID], stdout=PIPE, stderr=PIPE)
    if test.returncode is not 0:
        raise Exception("the SNMP test server is either not running, or not "
                        "configured properly.")