import ollama

def run_decision_model():
    response = ollama.systemone(
        model='nimble',
        state='Hello World',
        questions={
            'says_hello': {
                'type': 'noul',
                'instructions': 'Does the state text contain a greeting?',
                'criteria': {
                    'true': 'The state text contains a greeting.',
                    'false': 'The state text does not contain a greeting.',
                },
            },
        },
    )
    print(response.answers['says_hello'].noul)

if __name__ == "__main__":
    run_decision_model()