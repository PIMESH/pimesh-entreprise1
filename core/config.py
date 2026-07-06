#!/usr/bin/env python3
import os, json
from pathlib import Path
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
for d in [DATA_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)
CONFIG = {
    "version": "100.0.0",
    "name": "PiMesh Enterprise Ultimate",
    "pi_network": {
        "api_key": "t1vcstnh6topz03qvhstojjeci9i4wukmbmdry2blhpt71uw1desahhy9v15rzwl",
        "wallet": "GB4QOLEVD3FBPWXTHXBSOMED7DVSVTAPN5CSM4WPZS4NUUIFHMDVNKIR",
        "mainnet_url": "https://api.mainnet.minepi.com"
    },
    "agents": {"total": 650000, "active": 645000, "performance": 99.7},
    "economy": {"gcv": 31415900, "apr": 52.0, "credit_price": 0.0001}
}
def get_config(key=None):
    if key is None:
        return CONFIG.copy()
    keys = key.split('.')
    value = CONFIG
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None
    return value
