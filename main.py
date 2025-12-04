import ollama

# Le nom exact du modèle tel qu'il apparaît dans 'ollama list'
model_name = "gemma3:270m" 

try:
    response = ollama.chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': 'Pourquoi le ciel est-il bleu ? Réponds en une phrase.',
        },
    ])
    
    # Affichage de la réponse
    print(response['message']['content'])

except ollama.ResponseError as e:
    print(f"Erreur : Le modèle '{model_name}' est introuvable. Vérifiez le nom avec 'ollama list'.")