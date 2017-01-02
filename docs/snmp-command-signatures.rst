================================================
SNMP Commands Signatures (A.K.A. Command Inputs)
================================================

list
----
snmpconf_
snmpdf_
snmpinform_
snmpstatus_
snmptranslate_
snmpusm_
snmpbulkget_
snmpd_
snmpget_
snmpnetstat_
snmptable_
snmptrap_
snmpvacm_
snmpbulkwalk_
snmpdelta_
snmpgetnext_
snmpset_
snmptest_
snmptrapd_
snmpwalk_


snmpget
-------
USAGE: snmpget [OPTIONS] AGENT OID [OID]...

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
              f:  do not fix errors and retry the request


snmpconf
--------
USAGE: snmpconf [OPTIONS] [fileToCreate]

OPTIONS
       -f      Force overwriting existing files in the current directory without prompting the user if this is a desired thing to do.

       -i      When finished, install the files into the location where the global system commands expect to find them.

       -p      When  finished, install the files into the users home directory's .snmp subdirectory (where the applications will also search for configura-
               tion files).

       -I DIRECTORY
               When finished, install the files into the directory DIRECTORY.

       -a      Don't ask any questions.  Simply read in the various known configuration files and write them back out again.  This has the effect of "auto-
               commenting" the configuration files for you.  See the NEAT TRICKS section below.

       -rall|none
               Read in either all or none of the found configuration files.  Normally snmpconf prompts you for which files you wish to read in.  Reading in
               these configuration files will merge these files with the results of the questions that it asks of you.

       -R FILE,...
               Read in a specific list of configuration files.

       -g GROUPNAME
               Groups of configuration entries can be created that can be used to walk a user through a series of questions to create an initial configura-
               tion file.  There are no menus to navigate, just a list of questions.  Run:

                      snmpconf -g basic_setup

               for a good example.

       -G      List all the known groups.

       -c CONFIGDIR
               snmpconf  uses  a directory of configuration information to learn about the files and questions that it should be asking.  This option tells
               snmpconf to use a different location for configuring itself.

       -q      Run slightly more quietly.  Since this is an interactive program, I don't recommend this option since it only removes information  from  the
               output that is designed to help you.

       -d      Turn on lots of debugging output.

       -D      Add even more debugging output in the form of Perl variable dumps.


snmpdf
------
Usage: snmpdf [-Cu] [OPTIONS] AGENT

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'

snmpdf options:
              -Cu	Use UCD-SNMP dskTable to do the calculations.
                [Normally the HOST-RESOURCES-MIB is consulted first.]

snmpinform
----------
USAGE: snmpinform [OPTIONS] AGENT TRAP-PARAMETERS

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviour:
              i:  send an INFORM instead of a TRAP

  -v 1 TRAP-PARAMETERS:
     enterprise-oid agent trap-type specific-type uptime [OID TYPE VALUE]...
  or
  -v 2 TRAP-PARAMETERS:
     uptime trapoid [OID TYPE VALUE] ...


snmpstatus
----------
USAGE: snmpstatus [OPTIONS] AGENT

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
              f:  do not fix errors and retry the request

snmptranslate
-------------
USAGE: snmptranslate [OPTIONS] OID [OID]...

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h			display this help message
  -V			display package version number
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
  -w WIDTH		set width of tree and detail output
  -T TRANSOPTS		Set various options controlling report produced:
              B:  print all matching objects for a regex search
              d:  print full details of the given OID
              p:  print tree format symbol table
              a:  print ASCII format symbol table
              l:  enable labeled OID report
              o:  enable OID report
              s:  enable dotted symbolic report
              z:  enable MIB child OID report
              t:  enable alternate format symbolic suffix report
  -P MIBOPTS		Toggle various defaults controlling mib parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'

snmpusm
-------
Usage: snmpusm [OPTIONS] AGENT COMMAND

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'

snmpusm commands:
  [options]               create     USER [CLONEFROM-USER]
  [options]               delete     USER
  [options]               activate   USER
  [options]               deactivate USER
  [options] [-Cw]         cloneFrom  USER CLONEFROM-USER
  [options] [-Ca] [-Cx]   changekey  [USER]
  [options] [-Ca] [-Cx]   passwd     OLD-PASSPHRASE NEW-PASSPHRASE [USER]
  [options] (-Ca|-Cx) -Ck passwd     OLD-KEY-OR-PASS NEW-KEY-OR-PASS [USER]

snmpusm options:
    -CE ENGINE-ID	Set usmUserEngineID (e.g. 800000020109840301).
    -Cp STRING	Set usmUserPublic value to STRING.
    -Cw		Create the user with createAndWait.
            (it won't be active until you active it)
    -Cx		Change the privacy key.
    -Ca		Change the authentication key.
    -Ck		Allows to use localized key (must start with 0x)
            instead of passphrase.

snmpbulkget
-----------
USAGE: snmpbulkget [OPTIONS] AGENT OID [OID]...

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
              n<NUM>:  set non-repeaters to <NUM>
              r<NUM>:  set max-repeaters to <NUM>

snmpbulkwalk
------------
USAGE: snmpbulkwalk [OPTIONS] AGENT [OID]

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
              c:       do not check returned OIDs are increasing
              i:       include given OIDs in the search range
              n<NUM>:  set non-repeaters to <NUM>
              p:       print the number of variables found
              r<NUM>:  set max-repeaters to <NUM>


snmpd
-----
USAGE: snmpd [OPTIONS] [LISTENING ADDRESSES]

OPTIONS
       -a      Log the source addresses of incoming requests.

       -A      Append to the log file rather than truncating it.

       -c FILE Read FILE as a configuration file (or a comma-separated list of
               configuration  files).   Note  that  the  loaded file will only
               understand snmpd.conf tokens, unless the configuration type  is
               specified  in the file as described in the snmp_config man page
               under SWITCHING CONFIGURATION TYPES IN MID-FILE.

       -C      Do not read any configuration files except the ones  optionally
               specified by the -c option.  Note that this behaviour also cov-
               ers the persistent configuration files.   This  may  result  in
               dynamically-assigned  values  being  reset  following  an agent
               restart,  unless  the  relevant  persistent  config  files  are
               explicitly loaded using the -c option.

       -d      Dump (in hexadecimal) the sent and received SNMP packets.

       -D[TOKEN[,...]]
               Turn  on  debugging output for the given TOKEN(s).  Without any
               tokens specified, it defaults to printing all the tokens (which
               is equivalent to the keyword "ALL").  You might want to try ALL
               for extremely verbose output.  Note: You can not  put  a  space
               between the -D flag and the listed TOKENs.

       -f      Do not fork() from the calling shell.

       -g GID  Change  to  the  numerical group ID GID after opening listening
               sockets.

       -h, --help
               Display a brief usage message and then exit.

       -H      Display a list of configuration file directives  understood  by
               the agent and then exit.

       -I [-]INITLIST
               Specifies  which  modules should (or should not) be initialized
               when the agent starts up.  If the comma-separated  INITLIST  is
               preceded  with a '-', it is the list of modules that should not
               be started.  Otherwise this is the list  of  the  only  modules
               that should be started.

               To get a list of compiled modules, run the agent with the argu-
               ments -Dmib_init -H (assuming debugging support has  been  com-
               piled in).

       -L[efos]
               Specify where logging output should be directed (standard error
               or output, to a file or via syslog).  See  LOGGING  OPTIONS  in
               snmpcmd(5) for details.

       -m MIBLIST
               Specifies  a  colon  separated  list of MIB modules to load for
               this application.   This  overrides  the  environment  variable
               MIBS.  See snmpcmd(1) for details.

       -M DIRLIST
               Specifies  a  colon separated list of directories to search for
               MIBs.  This overrides the environment  variable  MIBDIRS.   See
               snmpcmd(1) for details.

       -n NAME Set an alternative application name (which will affect the con-
               figuration files loaded).   By  default  this  will  be  snmpd,
               regardless of the name of the actual binary.

       -p FILE Save the process ID of the daemon in FILE.

       -q      Print simpler output for easier automated parsing.

       -r      Do not require root access to run the daemon.  Specifically, do
               not exit if files only accessible to root  (such  as  /dev/kmem
               etc.) cannot be opened.

       -u UID  Change  to  the user ID UID (which can be given in numerical or
               textual form) after opening listening sockets.

       -U      Instructs the agent to not remove its  pid  file  (see  the  -p
               option)  on  shutdown. Overrides the leave_pidfile token in the
               snmpd.conf file, see snmpd.conf(5).

       -v, --version
               Print version information for the agent and then exit.

       -V      Symbolically dump SNMP transactions.

       -x ADDRESS
               Listens for AgentX connections on the specified address  rather
               than  the  default  AGENTX_SOCKET.  The address can either be a
               Unix domain socket path, or the address of a network interface.
               The  format  is  the  same as the format of listening addresses
               described below.

       -X      Run as an AgentX subagent rather than as an SNMP master  agent.

       --name="value"
               Allows   to   specify  any  token  ("name")  supported  in  the
               snmpd.conf file and sets its value to  "value".  Overrides  the
               corresponding  token  in the snmpd.conf file. See snmpd.conf(5)
               for the full list of tokens.

snmpnetstat
-----------
       snmpnetstat [COMMON OPTIONS] [-Ca] [-Cn] AGENT
       snmpnetstat [COMMON OPTIONS] [-Ci] [-Co] [-Cr] [-Cn] [-Cs] AGENT
       snmpnetstat [COMMON OPTIONS] [-Ci] [-Cn] [-CI interface] AGENT [interval]
       snmpnetstat [COMMON OPTIONS] [-Ca] [-Cn] [-Cs] [-Cp protocol] AGENT

COMMON OPTIONS
        Please see snmpcmd(1) for a list of possible values for common options
       as well as their descriptions.

       -Ca  With  the default display, show the state of all sockets; normally
       sockets used by server processes are not shown.

       -Ci Show the state of all of the network  interfaces.   The   interface
       display  provides  a  table  of cumulative statistics regarding packets
       transferred, errors, and collisions.  The   network  addresses  of  the
       interface  and  the  maximum  transmission unit (``mtu'') are also dis-
       played.

       -Co Show an abbreviated interface status, giving  octets  in  place  of
       packets.   This  is  useful  when enquiring virtual interfaces (such as
       Frame-Relay circuits) on a router.

       -CI interface Show information only about this interface; used with  an
       interval as described below.

       -Cn  Show network addresses as numbers (normally snmpnetstat interprets
       addresses and attempts to display them symbolically).  This option  may
       be used with any of the display formats.

       -Cp  protocol  Show  statistics about protocol, which is either a well-
       known name for a protocol or an alias for it.  Some protocol names  and
       aliases  are  listed in the file /etc/protocols.  A null response typi-
       cally means that there are no interesting numbers to report.  The  pro-
       gram  will complain if protocol is unknown or if there is no statistics
       routine for it.

       -Cs Show per-protocol statistics.  When used with the -Cr option,  show
       routing statistics instead.

       -Cr Show the routing tables.  When -Cs is also present, show per-proto-
       col routing statistics instead of the routing tables.

       -CR repeaters  For  GETBULK  requests,  repeaters  specifies  the  max-
       repeaters value to use.

snmptable
---------
USAGE: snmptable [OPTIONS] AGENT TABLE-OID

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviours:
              b:       brief field names
              B:       do not use GETBULK requests
              c<NUM>:  print table in columns of <NUM> chars width
              f<STR>:  print table delimitied with <STR>
              h:       print only the column headers
              H:       print no column headers
              i:       print index values
              l:       left justify output
              r<NUM>:  for GETBULK: set max-repeaters to <NUM>
                       for GETNEXT: retrieve <NUM> entries at a time
              w<NUM>:  print table in parts of <NUM> chars width


snmptrap
--------
USAGE: snmptrap [OPTIONS] AGENT TRAP-PARAMETERS

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'
  -C APPOPTS		Set various application specific behaviour:
              i:  send an INFORM instead of a TRAP

  -v 1 TRAP-PARAMETERS:
     enterprise-oid agent trap-type specific-type uptime [OID TYPE VALUE]...
  or
  -v 2 TRAP-PARAMETERS:
     uptime trapoid [OID TYPE VALUE] ...


snmpvacm
--------
Usage: snmpvacm [OPTIONS] AGENT COMMAND

  Version:  5.6.2.1
  Web:      http://www.net-snmp.org/
  Email:    net-snmp-coders@lists.sourceforge.net

OPTIONS:
  -h, --help		display this help message
  -H			display configuration file directives understood
  -v 1|2c|3		specifies SNMP version to use
  -V, --version		display package version number
SNMP Version 1 or 2c specific
  -c COMMUNITY		set the community string
SNMP Version 3 specific
  -a PROTOCOL		set authentication protocol (MD5|SHA)
  -A PASSPHRASE		set authentication protocol pass phrase
  -e ENGINE-ID		set security engine ID (e.g. 800000020109840301)
  -E ENGINE-ID		set context engine ID (e.g. 800000020109840301)
  -l LEVEL		set security level (noAuthNoPriv|authNoPriv|authPriv)
  -n CONTEXT		set context name (e.g. bridge1)
  -u USER-NAME		set security name (e.g. bert)
  -x PROTOCOL		set privacy protocol (DES|AES)
  -X PASSPHRASE		set privacy protocol pass phrase
  -Z BOOTS,TIME		set destination engine boots/time
General communication options
  -r RETRIES		set the number of retries
  -t TIMEOUT		set the request timeout (in seconds)
Debugging
  -d			dump input/output packets in hexadecimal
  -D[TOKEN[,...]]	turn on debugging output for the specified TOKENs
               (ALL gives extremely verbose debugging output)
General options
  -m MIB[:...]		load given list of MIBs (ALL loads everything)
  -M DIR[:...]		look in given list of directories for MIBs
    (default: /Users/alex/.snmp/mibs:/usr/share/snmp/mibs)
  -P MIBOPTS		Toggle various defaults controlling MIB parsing:
              u:  allow the use of underlines in MIB symbols
              c:  disallow the use of "--" to terminate comments
              d:  save the DESCRIPTIONs of the MIB objects
              e:  disable errors when MIB symbols conflict
              w:  enable warnings when MIB symbols conflict
              W:  enable detailed warnings when MIB symbols conflict
              R:  replace MIB symbols from latest module
  -O OUTOPTS		Toggle various defaults controlling output display:
              0:  print leading 0 for single-digit hex characters
              a:  print all strings in ascii format
              b:  do not break OID indexes down
              e:  print enums numerically
              E:  escape quotes in string indices
              f:  print full OIDs on output
              n:  print OIDs numerically
              q:  quick print for easier parsing
              Q:  quick print with equal-signs
              s:  print only last symbolic element of OID
              S:  print MIB module-id plus last element
              t:  print timeticks unparsed as numeric integers
              T:  print human-readable text along with hex strings
              u:  print OIDs using UCD-style prefix suppression
              U:  don't print units
              v:  print values only (not OID = value)
              x:  print all strings in hex format
              X:  extended index format
  -I INOPTS		Toggle various defaults controlling input parsing:
              b:  do best/regex matching to find a MIB node
              h:  don't apply DISPLAY-HINTs
              r:  do not check values for range/type legality
              R:  do random access to OID labels
              u:  top-level OIDs must have '.' prefix (UCD-style)
              s SUFFIX:  Append all textual OIDs with SUFFIX before parsing
              S PREFIX:  Prepend all textual OIDs with PREFIX before parsing
  -L LOGOPTS		Toggle various defaults controlling logging:
              e:           log to standard error
              o:           log to standard output
              n:           don't log at all
              f file:      log to the specified file
              s facility:  log to syslog (via the specified facility)

              (variants)
              [EON] pri:   log to standard error, output or /dev/null for level 'pri' and above
              [EON] p1-p2: log to standard error, output or /dev/null for levels 'p1' to 'p2'
              [FS] pri token:    log to file/syslog for level 'pri' and above
              [FS] p1-p2 token:  log to file/syslog for levels 'p1' to 'p2'

snmpvacm commands:
        createAccess     GROUPNAME [CONTEXTPREFIX] SECURITYMODEL SECURITYLEVEL CONTEXTMATCH READVIEWNAME WRITEVIEWNAME NOTIFYVIEWNAME
        deleteAccess     GROUPNAME [CONTEXTPREFIX] SECURITYMODEL SECURITYLEVEL
        createSec2Group  MODEL SECURITYNAME  GROUPNAME
        deleteSec2Group  MODEL SECURITYNAME
  [-Ce] createView       NAME SUBTREE [MASK]
        deleteView       NAME SUBTREE
        createAuth       GROUPNAME [CONTEXTPREFIX] SECURITYMODEL SECURITYLEVEL AUTHTYPE CONTEXTMATCH VIEWNAME
        deleteAuth       GROUPNAME [CONTEXTPREFIX] SECURITYMODEL SECURITYLEVEL AUTHTYPE


