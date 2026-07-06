#!/usr/bin/env python3
# ============================================================
# SERVICE DEX - Échange Décentralisé
# Pools de liquidité | Swap | Ordres
# ============================================================

import random
import time
from datetime import datetime

class DEXService:
    def __init__(self):
        self.pools = {}
        self.orders = []

    def create_pool(self, token_a, token_b, amount_a, amount_b):
        pool_id = f"pool_{int(time.time())}"
        self.pools[pool_id] = {
            "id": pool_id,
            "token_a": token_a,
            "token_b": token_b,
            "reserve_a": amount_a,
            "reserve_b": amount_b,
            "created_at": datetime.now().isoformat()
        }
        return pool_id

    def swap(self, pool_id, token_in, amount_in):
        pool = self.pools.get(pool_id)
        if not pool:
            return {"error": "Pool not found"}
        # Calcul du taux (simulation)
        rate = pool["reserve_b"] / pool["reserve_a"]
        amount_out = amount_in * rate * 0.997  # 0.3% de frais
        return {
            "success": True,
            "amount_in": amount_in,
            "amount_out": amount_out,
            "rate": rate
        }

    def add_liquidity(self, pool_id, amount_a, amount_b):
        pool = self.pools.get(pool_id)
        if not pool:
            return {"error": "Pool not found"}
        pool["reserve_a"] += amount_a
        pool["reserve_b"] += amount_b
        return {"success": True}
