
import logging
from typing import Dict, Any, Callable

# Configure logging for better visibility
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Orchestrator:
    """ Orchestrates multi-model Generative AI workflows. """

    def __init__(self):
        self.models: Dict[str, Any] = {}
        logging.info("Orchestrator initialized.")

    def add_model(self, name: str, model_instance: Any):
        """ Adds a generative AI model to the orchestrator. """
        if not isinstance(name, str) or not name:
            raise ValueError("Model name must be a non-empty string.")
        if not model_instance:
            raise ValueError("Model instance cannot be None.")
        self.models[name] = model_instance
        logging.info(f"Model '{name}' added to orchestrator.")

    def run(self, model_name: str, *args, **kwargs) -> Any:
        """ Runs a specific model with given inputs. """
        if model_name not in self.models:
            logging.error(f"Model '{model_name}' not found.")
            raise ValueError(f"Model '{model_name}' not found.")
        
        model = self.models[model_name]
        logging.info(f"Running model '{model_name}' with args: {args}, kwargs: {kwargs}")
        try:
            result = model(*args, **kwargs)
            logging.info(f"Model '{model_name}' executed successfully.")
            return result
        except Exception as e:
            logging.error(f"Error running model '{model_name}'": {e}")
            raise

    def define_workflow(self, name: str, workflow_func: Callable):
        """ Defines and registers a custom workflow. """
        if not isinstance(name, str) or not name:
            raise ValueError("Workflow name must be a non-empty string.")
        if not callable(workflow_func):
            raise ValueError("Workflow function must be callable.")
        setattr(self, name, workflow_func)
        logging.info(f"Workflow '{name}' defined.")

    def get_model(self, name: str) -> Any:
        """ Retrieves a model by its name. """
        return self.models.get(name)

    def list_models(self) -> list[str]:
        """ Lists all registered model names. """
        return list(self.models.keys())

# Example usage (for demonstration, not part of the library itself)
if __name__ == "__main__":
    from transformers import pipeline
    # Mock models for demonstration
    class MockTextGenerator:
        def __call__(self, prompt, **kwargs):
            return f"Generated text for: {prompt}"

    class MockImageGenerator:
        def __call__(self, text_input, **kwargs):
            return f"Generated image for: {text_input}"

    orchestrator = Orchestrator()
    orchestrator.add_model("mock_text_gen", MockTextGenerator())
    orchestrator.add_model("mock_image_gen", MockImageGenerator())

    def simple_creative_workflow(prompt):
        text = orchestrator.run("mock_text_gen", prompt)
        image = orchestrator.run("mock_image_gen", text)
        return text, image

    orchestrator.define_workflow("creative_flow", simple_creative_workflow)

    text_output, image_output = orchestrator.creative_flow("A serene landscape")
    print(f"
Final Text Output: {text_output}")
    print(f"Final Image Output: {image_output}")

    # Example with actual Hugging Face pipelines (requires transformers and torch installed)
    # try:
    #     real_text_generator = pipeline("text-generation", model="gpt2")
    #     orchestrator.add_model("real_text_gen", real_text_generator)
    #     real_text = orchestrator.run("real_text_gen", "Hello, my name is")
    #     print(f"
Real Text Generation: {real_text}")
    # except Exception as e:
    #     print(f"Could not load real text generator: {e}")
