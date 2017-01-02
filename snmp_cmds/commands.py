# Internal module imports
# Internal module imports
from .helpers import snmp_command


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

    return snmp_command('snmpget', agent, oid, *options)
