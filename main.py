from ollama_decision_model import run_decision_model

def main():
    """
    Entry point for the ollama-decision-model-test project.
    """
    print("Starting Ollama Decision Model...")
    try:
        run_decision_model()
    except Exception as e:
        print(f"An error occurred while running the decision model: {e}")

if __name__ == "__main__":
    main()
