#!/usr/bin/env python3
# ============================================================
# PIMESH ENTERPRISE - ORCHESTRATEUR
# Coordination de tous les services
# ============================================================

import sys
import time
import asyncio
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from core.config.config import CONFIG
from services.payments.payments import PaymentService
from services.contracts.contracts import ContractService
from services.dao.dao import DAOService
from services.identity.identity import IdentityService
from services.dex.dex import DEXService

class PiMeshEnterprise:
    def __init__(self):
        self.name = CONFIG["name"]
        self.version = CONFIG["version"]
        self.services = {
            "payments": PaymentService(),
            "contracts": ContractService(),
            "dao": DAOService(),
            "identity": IdentityService(),
            "dex": DEXService()
        }
        self.stats = {
            "start_time": datetime.now().isoformat(),
            "uptime": 0,
            "transactions": 0,
            "contracts": 0,
            "dao_proposals": 0,
            "users": 0
        }
        self.running = False

    def start(self):
        print(f"🏢 {self.name} - Version {self.version}")
        print(f"🌐 Réseau : {CONFIG['network']}")
        print("📦 Services disponibles :")
        for name in self.services.keys():
            print(f"   - {name}")
        print("✅ Entreprise opérationnelle")
        self.running = True
        self._main_loop()

    def _main_loop(self):
        while self.running:
            self.stats["uptime"] += 10
            self._process_services()
            time.sleep(10)

    def _process_services(self):
        # Vérifier les paiements
        balance = self.services["payments"].get_balance()
        self.stats["transactions"] += 1
        
        # Mise à jour des stats
        if self.stats["uptime"] % 60 == 0:
            print(f"\n📊 Entreprise - Uptime : {self.stats['uptime']//60}m")
            print(f"💰 Solde : {balance:.2f} Pi")
            print(f"📦 Transactions : {self.stats['transactions']}")

    def stop(self):
        self.running = False
        print("🛑 Entreprise arrêtée")

if __name__ == "__main__":
    enterprise = PiMeshEnterprise()
    try:
        enterprise.start()
    except KeyboardInterrupt:
        enterprise.stop()
