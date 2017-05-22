from setuptools import setup

setup(
    name='snmp-cmds',
    version='0.1',
    description='A python library for issuing SNMP commands',
    long_description='''This package is a wrapper around the Net-SNMP command 
        line utilities''',
    url='https://github.com/alextremblay/snmp-cmds',
    author='Alex Tremblay',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',

        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',

        'License :: OSI Approved :: MIT License',

        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=['snmp_cmds'],
    extras_require={
        'test': ['pytest', 'snmpsim']
    },
    entry_points=None
)
