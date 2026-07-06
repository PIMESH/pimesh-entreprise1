# ============================================================
# PIMESH ENTERPRISE - CONFIGURATION CENTRALE
# ============================================================

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

for d in [DATA_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

CONFIG = {
    "name": "PiMesh Enterprise",
    "version": "1.0",
    "company": "PiMesh",
    "network": "Pi Network",
    
    "pi": {
        "wallet": "GB4QOLEVD3FBPWXTHXBSOMED7DVSVTAPN5CSM4WPZS4NUUIFHMDVNKIR",
        "seed": "soda despair noise camp mouse spring canyon wool walnut reunion river vault alcohol damp parrot weather melody laugh ship garage sword frog cabin wave",
        "api_key": "7ng1ukccnvqko3rf9htp36bo90vmyipw4yjy6y2cwz8vpgc5c48c0ymwskeycu5f",
        "client_auth": "jx5tZMds24fiQh-G4JyGyE1tuQOLLNVBKQQ43rGLyrA",
        "mainnet_url": "https://api.mainnet.minepi.com"
    },
    
    "services": {
        "payments": True,
        "contracts": True,
        "dao": True,
        "identity": True,
        "staking": True,
        "dex": True,
        "nft": True,
        "bridge": True
    },
    
    "conversion": {
        "rate": 0.5,
        "interval": 3600,
        "min_pi": 100,
        "eth_private_key": "5a72dc7a6a3a2d56b6e1fbdb5f4e11393190da2303df376a78277a3de2197b80"
    },
    
    "gcv": 314159,
    "apr": 5.2
}
