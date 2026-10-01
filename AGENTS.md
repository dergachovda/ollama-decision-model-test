# Project Agents

This document describes the agents involved in the `ollama-decision-model-test` project, their roles, and their responsibilities.

## Project Overview
The project is designed to test and implement a decision model using Ollama's system capabilities (specifically `systemone`).

## Core Agents

### Main Orchestrator (`main.py`)
- **Role**: Entry point and coordinator.
- **Responsibilities**:
    - Initializes the application environment.
    - Orchestrates the execution of the decision model.
    - Handles high-level error reporting and logging.

### Decision Model Agent (`ollama-decision-model.py`)
- **Role**: Domain logic provider.
- **Responsibilities**:
    - Defines the state and the questions for the decision model.
    - Interfaces with the `ollama` library.
    - Processes and returns the decision results (e.g., `noul` answers).

## Workflow
1. `main.py` triggers the `run_decision_model()` function.
2. `ollama-decision-model.py` sends a `systemone` request to the Ollama server.
3. The Ollama model evaluates the `state` against the provided `questions` and `criteria`.
4. The result is parsed and printed to the console.
