#!/usr/bin/env bash
snmpsimd.py --agent-udpv4-endpoint=127.0.0.1:10000 --data-dir=tests &
SNMPSIM_PID=$!
pytest
kill $SNMPSIM_PID