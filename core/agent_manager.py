from abc import ABC, abstractmethod
from core.logging import logger

class BaseAgent(ABC):
    def __init__(self, name, client):
        self.name = name
        self.client = client
        logger.info(f"Agent {name} initialized")

    @abstractmethod
    def execute(self, task, **kwargs):
        pass
