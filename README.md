
# Gen AI Orchestrator

A robust framework for orchestrating multi-model Generative AI workflows with built-in evaluation and monitoring.

## Features
- **Multi-Model Support**: Integrate and manage various generative AI models (LLMs, image generation, etc.).
- **Workflow Orchestration**: Define and execute complex AI workflows with ease.
- **Evaluation & Monitoring**: Tools for assessing model performance and tracking usage.
- **Scalable Deployment**: Designed for scalable deployment in cloud environments.

## Installation

```bash
pip install gen-ai-orchestrator
```

## Usage

```python
from gen_ai_orchestrator import Orchestrator
from transformers import pipeline

# Initialize models
text_generator = pipeline("text-generation", model="gpt2")
image_generator = pipeline("text-to-image", model="stabilityai/stable-diffusion-v2")

orchestrator = Orchestrator()
orchestrator.add_model("text_gen", text_generator)
orchestrator.add_model("image_gen", image_generator)

# Define a simple workflow
def creative_workflow(prompt):
    text = orchestrator.run("text_gen", prompt)
    image = orchestrator.run("image_gen", text)
    return text, image

# Execute workflow
prompt = "A futuristic city at sunset"
text_output, image_output = creative_workflow(prompt)
print(f"Generated Text: {text_output}")
# image_output.save("generated_image.png")
```

## Contributing

Contributions are welcome! Please see `CONTRIBUTING.md` for details.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
