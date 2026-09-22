"""Abstract base class for AI providers."""

from abc import ABC, abstractmethod
from typing import Optional


class BaseProvider(ABC):
    def __init__(self, model: Optional[str] = None, **kwargs):
        self.model = model
        self.kwargs = kwargs

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Generate a response from the AI."""
        pass

    @abstractmethod
    def list_models(self) -> list:
        """List available models."""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if provider is available."""
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(model={self.model})"
