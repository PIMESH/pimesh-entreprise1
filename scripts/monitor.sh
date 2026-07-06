#!/bin/bash
cd ~/pimesh_enterprise
if [ -f "data/enterprise.pid" ]; then
    PID=$(cat data/enterprise.pid)
    if ps -p $PID > /dev/null; then
        echo "✅ Enterprise: Active (PID: $PID)"
    else
        echo "❌ Enterprise: Inactive"
    fi
else
    echo "❌ Aucun PID trouve"
fi
echo ""
echo "📊 Logs recents:"
tail -5 logs/enterprise.log
