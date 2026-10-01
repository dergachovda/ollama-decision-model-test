# Ollama Decision Model Test

This project is designed to test and implement a decision model using Ollama's system capabilities, specifically the `systemone` feature.

## Project Overview

The goal of this project is to evaluate how an Ollama model can process a given `state` against a set of `questions` and `criteria` to produce structured decision results (e.g., `noul` answers).

## Project Structure

- `main.py`: The main entry point and orchestrator that triggers the decision model.
- `ollama-decision-model.py`: Contains the domain logic, defines the state and questions, and interfaces with the `ollama` library.
- `AGENTS.md`: Detailed description of the agent roles and responsibilities within the project.

## Getting Started

### Prerequisites

- Python 3.10+
- Ollama installed and running locally
- A model compatible with `systemone` (e.g., `nimble`) pulled in Ollama

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ollama-decision-model-test
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```
   *(Note: Ensure the `ollama` Python library is installed)*

### Running the Model

Execute the main orchestrator:
```bash
uv run main.py
```

### Running Tests

To run the project tests:
```bash
uv run pytest
```

## Workflow

1. `main.py` calls the `run_decision_model()` function.
2. `ollama-decision-model.py` sends a `systemone` request to the Ollama server with a specific `state`, `questions`, and `criteria`.
3. The Ollama model evaluates the state and returns the results.
4. The result is parsed and printed to the console.
