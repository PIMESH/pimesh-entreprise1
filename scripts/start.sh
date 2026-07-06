#!/bin/bash
cd ~/pimesh_enterprise
mkdir -p logs data
nohup python3 main.py > logs/enterprise.log 2>&1 &
echo $! > data/enterprise.pid
echo "✅ Enterprise demarree (PID: $(cat data/enterprise.pid))"
