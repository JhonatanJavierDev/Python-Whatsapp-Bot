from twilio.rest import Client
from flask import Flask, request
import requests

app = Flask(__name__)

account_sid = 'tu_account_sid'
auth_token = 'tu_auth_token'
client = Client(account_sid, auth_token)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = get_response(incoming_msg)
    msg = client.messages.create(
        body=resp,
        from_='whatsapp:+14155238886',
        to=request.values.get('From')
    )
    return '', 200

def get_response(msg):
    responses = {
        'hola': 'Hola! ¿Cómo estás?',
        'qué tal': 'Muy bien, gracias. ¿Y tú?',
        'dónde estás': 'Estoy en línea, ¿y tú?',
        'qué haces': 'Estoy aquí para ayudarte, ¿en qué puedo ayudarte?',
        'quién eres': 'Soy un bot creado para ayudarte',
        'cómo estás': 'Estoy bien, gracias por preguntar',
        'adiós': 'Hasta luego, ¡que tengas un buen día!',
        'cuál es tu nombre': 'Mi nombre es Botsito',
        'en qué puedo ayudarte': 'Puedo responder tus preguntas o ayudarte en lo que necesites',
        'gracias': 'De nada, ¡estoy aquí para ayudarte siempre!'
    }
    return responses.get(msg, 'Lo siento, no te entiendo. Por favor, intenta de nuevo.')

if __name__ == '__main__':
    app.run()
