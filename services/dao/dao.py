#!/usr/bin/env python3
# ============================================================
# SERVICE DAO - Gouvernance Décentralisée
# Propositions | Votes | Trésorerie
# ============================================================

import time
import json
from datetime import datetime
from core.config.config import CONFIG

class DAOService:
    def __init__(self):
        self.proposals = []
        self.votes = []
        self.treasury = 0.0

    def create_proposal(self, title, description, options, proposer):
        proposal = {
            "id": f"prop_{int(time.time())}",
            "title": title,
            "description": description,
            "options": options,
            "proposer": proposer,
            "votes": {opt: 0 for opt in options},
            "status": "active",
            "created_at": datetime.now().isoformat()
        }
        self.proposals.append(proposal)
        return proposal

    def vote(self, proposal_id, voter, option):
        for prop in self.proposals:
            if prop["id"] == proposal_id and prop["status"] == "active":
                if option in prop["votes"]:
                    prop["votes"][option] += 1
                    self.votes.append({
                        "proposal": proposal_id,
                        "voter": voter,
                        "option": option,
                        "timestamp": datetime.now().isoformat()
                    })
                    return {"success": True}
        return {"success": False, "error": "Invalid proposal"}

    def get_treasury(self):
        # Récupère le solde du wallet
        return CONFIG["pi"]["wallet"]
