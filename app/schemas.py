from dataclasses import dataclass
from typing import List

@dataclass
class PredictionRequest:
    """Input structure for API requests."""
    text: str

@dataclass
class PredictionResponse:
    """Output structure for API responses."""
    probabilities: List[float]