#!/usr/bin/env python3
# ============================================================
# SERVICE IDENTITÉ - KYC & Vérification
# Preuve d'humanité | Vérification Pi
# ============================================================

import hashlib
from datetime import datetime

class IdentityService:
    def __init__(self):
        self.users = {}
        self.verifications = []

    def verify_user(self, pi_username, wallet_address):
        user_id = hashlib.sha256(f"{pi_username}{wallet_address}".encode()).hexdigest()[:16]
        user = {
            "id": user_id,
            "username": pi_username,
            "wallet": wallet_address,
            "verified": True,
            "verified_at": datetime.now().isoformat()
        }
        self.users[user_id] = user
        self.verifications.append(user)
        return user

    def get_user(self, user_id):
        return self.users.get(user_id)

    def is_human(self, user_id):
        user = self.users.get(user_id)
        return user is not None and user.get("verified", False)
