from setuptools import setup, find_packages
from sys import platform

def get_requirements():
    requires = []
    if platform == 'win32':
        requires += ['pbs']
    else:
        requires += ['sh']
    return requires

setup(
    name='snmp-cmds',
    version='0.1',
    description='A python library for issuing SNMP commands',
    long_description='''This package is a wrapper around the Net-SNMP command line utilities''',
    url='https://github.com/alextremblay/snmp-cmds',
    author='Alex Tremblay',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',

        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=['snmp_cmds'],
    install_requires=get_requirements(),
    entry_points=None
)
