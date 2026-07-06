#!/usr/bin/env python3
import time, random, logging
from datetime import datetime
from core.config import CONFIG

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self):
        self.running = False
        self.cycle_count = 0
        self.actions = 0
        self.errors = 0
        self.start_time = None
        self.agents_total = CONFIG.get('agents', {}).get('total', 6500)
        self.agents_active = CONFIG.get('agents', {}).get('active', 6450)

    def initialize(self):
        logger.info("Orchestrator initialise")
        return True

    def start(self):
        self.running = True
        self.start_time = datetime.now()
        logger.info("Orchestrator demarre")

    def stop(self):
        self.running = False
        logger.info("Orchestrator arrete")

    def execute_cycle(self):
        self.cycle_count += 1
        self.actions += 1
        variation = random.randint(-5, 5)
        self.agents_active = max(6400, min(self.agents_total, self.agents_active + variation))
        revenue = round(random.uniform(0.01, 0.5), 2)
        return {
            'success': True,
            'revenue': revenue,
            'users': random.randint(1, 10),
            'agents_active': self.agents_active
        }

    def get_status(self):
        return {
            'running': self.running,
            'cycle_count': self.cycle_count,
            'actions': self.actions,
            'errors': self.errors,
            'agents_active': self.agents_active,
            'agents_total': self.agents_total
        }
