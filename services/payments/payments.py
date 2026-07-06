#!/usr/bin/env python3
# ============================================================
# SERVICE PAIEMENTS - Pi Network
# U2A (User-to-App) | P2P (Peer-to-Peer)
# ============================================================

import requests
from core.config.config import CONFIG

class PaymentService:
    def __init__(self):
        self.api_key = CONFIG["pi"]["api_key"]
        self.wallet = CONFIG["pi"]["wallet"]
        self.mainnet_url = CONFIG["pi"]["mainnet_url"]

    def approve_payment(self, payment_id):
        url = f"{self.mainnet_url}/v2/payments/{payment_id}/approve"
        headers = {"Authorization": f"Key {self.api_key}"}
        response = requests.post(url, headers=headers)
        return response.json()

    def complete_payment(self, payment_id, txid):
        url = f"{self.mainnet_url}/v2/payments/{payment_id}/complete"
        headers = {"Authorization": f"Key {self.api_key}"}
        payload = {"txid": txid}
        response = requests.post(url, headers=headers, json=payload)
        return response.json()

    def get_balance(self, address=None):
        if not address:
            address = self.wallet
        url = f"{self.mainnet_url}/accounts/{address}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for b in data.get("balances", []):
                if b.get("asset_type") == "native":
                    return float(b.get("balance", 0))
        return 0
