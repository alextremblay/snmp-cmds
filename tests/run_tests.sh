#!/usr/bin/env bash
snmpsimd.py --agent-udpv4-endpoint=127.0.0.1:10000 --data-dir=tests > /dev/null &
SNMPSIM_PID=$!
pytest
PYTEST_STATUS=$?
kill $SNMPSIM_PID
exit $PYTEST_STATUS