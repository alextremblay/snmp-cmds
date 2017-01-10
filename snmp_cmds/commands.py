# Internal module imports
import re
# Internal module imports
from .helpers import snmp_command, SNMPResult


# This compiled Regex will allow us to split the string we receive from any of the net-snmp shell commands into usable
# chunks
result_splitter = re.compile(r'::| = |(?<=[A-Z]{2}): ')


def snmpget(
        agent, oid, version='2c', v2_community_string='public', v3_auth_protocol=None, v3_auth_passphrase=None,
        v3_security_engine_id=None, v3_context_engine_id=None, v3_security_level=None, v3_context_name=None,
        v3_user_name=None, v3_privacy_protocol=None, v3_privacy_passphrase=None, v3_dest_engine_boots_time=None):
    options = []
    options.extend(['-v', version])
    if v2_community_string and version == '2c':
        options.extend(['-c', v2_community_string])
    if v3_auth_protocol and version == '3':
        options.extend(['-a', v3_auth_protocol])
    if v3_auth_passphrase and version == '3':
        options.extend(['-A', v3_auth_passphrase])
    if v3_security_engine_id and version == '3':
        options.extend(['-e', v3_security_engine_id])
    if v3_context_engine_id and version == '3':
        options.extend(['-E', v3_context_engine_id])
    if v3_security_level and version == '3':
        options.extend(['-l', v3_security_level])
    if v3_context_name and version == '3':
        options.extend(['-n', v3_context_name])
    if v3_user_name and version == '3':
        options.extend(['-u', v3_user_name])
    if v3_privacy_protocol and version == '3':
        options.extend(['-x', v3_privacy_protocol])
    if v3_privacy_passphrase and version == '3':
        options.extend(['-X', v3_privacy_passphrase])
    if v3_dest_engine_boots_time and version == '3':
        options.extend(['-Z', v3_dest_engine_boots_time])

    result = snmp_command('snmpget', agent, oid, *options)

    result = result_splitter.split(str(result))
    if 'No Such' in result[2]:
        return SNMPResult(mib=result[0], oid=result[1], type='NoSuchInstance', value=None)
    for index in range(len(result)):
        result[index] = result[index].strip('\n')
    if len(result) == 4:
        return SNMPResult(*result)
    else:
        raise Exception('snmp command returned an unexpected number of results. expected 4 results, got:' + result)


def snmpwalk(
        agent, oid, version='2c', v2_community_string='public', v3_auth_protocol=None, v3_auth_passphrase=None,
        v3_security_engine_id=None, v3_context_engine_id=None, v3_security_level=None, v3_context_name=None,
        v3_user_name=None, v3_privacy_protocol=None, v3_privacy_passphrase=None, v3_dest_engine_boots_time=None):
    '''
    a generator which yields an SNMPResult object for each oid found while walking

    :param agent:
    :param oid:
    :param version:
    :param v2_community_string:
    :param v3_auth_protocol:
    :param v3_auth_passphrase:
    :param v3_security_engine_id:
    :param v3_context_engine_id:
    :param v3_security_level:
    :param v3_context_name:
    :param v3_user_name:
    :param v3_privacy_protocol:
    :param v3_privacy_passphrase:
    :param v3_dest_engine_boots_time:
    :return:
    '''
    options = []
    options.extend(['-v', version])
    if v2_community_string and version == '2c':
        options.extend(['-c', v2_community_string])
    if v3_auth_protocol and version == '3':
        options.extend(['-a', v3_auth_protocol])
    if v3_auth_passphrase and version == '3':
        options.extend(['-A', v3_auth_passphrase])
    if v3_security_engine_id and version == '3':
        options.extend(['-e', v3_security_engine_id])
    if v3_context_engine_id and version == '3':
        options.extend(['-E', v3_context_engine_id])
    if v3_security_level and version == '3':
        options.extend(['-l', v3_security_level])
    if v3_context_name and version == '3':
        options.extend(['-n', v3_context_name])
    if v3_user_name and version == '3':
        options.extend(['-u', v3_user_name])
    if v3_privacy_protocol and version == '3':
        options.extend(['-x', v3_privacy_protocol])
    if v3_privacy_passphrase and version == '3':
        options.extend(['-X', v3_privacy_passphrase])
    if v3_dest_engine_boots_time and version == '3':
        options.extend(['-Z', v3_dest_engine_boots_time])

    result = snmp_command('snmpwalk', agent, oid, *options)
    result = str(result).splitlines()
    for item in result:
        item = result_splitter.split(str(item))
        if 'No Such' in item[2]:
            yield SNMPResult(mib=item[0], oid=item[1], type='NoSuchInstance', value=None)
        for index in range(len(item)):
            item[index] = item[index].strip('\n')
        if len(item) == 4:
            yield SNMPResult(*item)
        else:
            raise Exception('snmp command returned an unexpected number of results. expected 4 results, got:' + result)