#!/bin/bash
cd ~/pimesh_enterprise
if [ -f "data/enterprise.pid" ]; then
    kill $(cat data/enterprise.pid) 2>/dev/null
    rm -f data/enterprise.pid
    echo "✅ Enterprise arretee"
else
    echo "❌ Aucun PID trouve"
fi
