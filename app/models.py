from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from typing import List
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LLMInference:
    """Singleton class to manage LLM loading and inference, ensuring model is loaded once."""
    _instance = None

    def __new__(cls, model_name: str):
        if cls._instance is None:
            cls._instance = super(LLMInference, cls).__new__(cls)
            # Load model and tokenizer once during initialization
            logger.info(f"Loading model: {model_name}")
            cls._instance.tokenizer = AutoTokenizer.from_pretrained(model_name)
            cls._instance.model = AutoModelForSequenceClassification.from_pretrained(model_name)
            cls._instance.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            cls._instance.model.to(cls._instance.device)
            cls._instance.model.eval()  # Set to evaluation mode for inference
        return cls._instance

    def predict(self, text: str, max_length: int) -> List[float]:
        """Perform inference on input text and return logits."""
        try:
            # Tokenize input
            inputs = self.tokenizer(
                text,
                max_length=max_length,
                truncation=True,
                padding=True,
                return_tensors="pt"
            ).to(self.device)

            # Inference with no gradient computation for efficiency
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits.softmax(dim=-1).cpu().numpy()[0].tolist()
            return logits
        except Exception as e:
            logger.error(f"Inference error: {str(e)}")
            raise


# Global instance for reuse across requests
llm = LLMInference(model_name="distilbert-base-uncased")  # Replace with your fine-tuned model