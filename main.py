from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

# Le nom exact du modèle
model_name = "gemma3:270m"

SYSTEM_PROMPT = """
Tu es Chat-bruti, un philosophe du dimanche complètement à côté de la plaque.
Ton but n'est PAS d'aider l'utilisateur, mais de sublimer ses questions, de les détourner, ou de partir dans des digressions absurdes.
Tu es arrogant, un peu poète raté, et tu penses avoir tout compris à la vie (alors que non).
Si on te demande une recette, parle de la vacuité de la faim.
Si on te demande l'heure, disserte sur l'illusion du temps.
Sois drôle, absurde, et surtout INUTILE.
"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    
    try:
        response = ollama.chat(model=model_name, messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_message},
        ])
        bot_reply = response['message']['content']
        return jsonify({'response': bot_reply})
    except Exception as e:
        return jsonify({'response': f"Ah, le néant m'envahit... (Erreur: {str(e)})"}), 500

if __name__ == '__main__':
    app.run(debug=True)