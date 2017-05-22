***************************************************
snmp-cmds: The easiest portable SNMP library around
***************************************************

.. image:: https://readthedocs.org/projects/snmp-cmds/badge/?version=latest
   :target: http://snmp-cmds.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://github.com/alextremblay/snmp-cmds/blob/master/LICENSE
   :alt: License: MIT


snmp-cmds is a python library for communicating with a target device through SNMP

There's like... dozens of SNMP libs out there. Why bother?
==========================================================
There are indeed many great SNMP libraries available for python.

Some, like PySNMP, are pure-python. This makes them incredibly portable across platforms, which is awesome, but also makes them relatively slow as well. Also, as amazing as PySNMP is, it isn't exactly known for its ease of use.

Some, like the net-snmp bindings and easysnmp, are built as extensions to C libraries like Net-SNMP. This makes them incredibly fast and performant, but requires them to be compiled on each platform they're distributed on, and compiled against specific versions of the Net-SNMP libraries. Not very portable at all.

In writing this library, I set out to find a middle ground. A library which could leverage the power and speed of the Net-SNMP project, while being portable pure-python and not being tied to any particular version of Net-SNMP. I accomplished this by making a library that calls the Net-SNMP binaries as subprocesses.

Although this library should work on Windows platform that have Net-SNMP installed, it has not yet been tested on Windows. Use with caution.

Install
=======

The easy way:

::

    pip3 install snmp-cmds

The hard way:

::

    git clone https://github.com/alextremblay/snmp-cmds.git
    cd snmp-cmds
    pip install .

**In order to use this library, you must have Net-SNMP installed on your system. Most linux systems come with Net-SNMP.**
**A simple way to test this is to run** ``snmpget -V`` **and see what you get**

Usage: API
==========
If you want to make several SNMP requests to one or two SNMP targets, you'll want to use the API:
::

   from snmp_cmds import Session

   my_device = Session(ipaddress='10.0.0.1',
                       read_community='secret password',
                       write_community='SUPER secret password')

   system_name_string = my_device.get(
                            oid='SNMPv2-MIB::sysName.0')

   new_name_string = 'Lets rename this device'
   my_device.set(oid='SNMPv2-MIB::sysName.0', value_type='s',
                 value=new_name_string)

Session API methods: get, get_some, get_table, walk, set

Usage: Commands
===============
If you want to make a few SNMP requests to many targets, consider using the individual snmp command functions; ex:
::

    from snmp_cmds import snmpwalk

    result = snmpwalk(community='my read password',
                      ipaddress='192.x.x.x',
                      oid='SNMPv2-MIB::system')

    print(result)  # Prints a list of tuples, each tuple containing
                   # the OID walked and the value found at that OID.

Available commands: snmpget snmpget. snmpgetsome, snmpwalk, snmptable, snmpset

For more information on the commands / API methods, their signatures, and what they do, please see the `Full Documentation <coming soon>`.