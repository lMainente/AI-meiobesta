from flask import Flask
from reconhecimento_fala import ouvir_microfone
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    fala = ouvir_microfone()
    if fala:
        if "bom dia" in fala.lower():
            return responder_cumprimento("bom dia")
        elif "boa tarde" in fala.lower():
            return responder_cumprimento("boa tarde")
        elif "boa noite" in fala.lower():
            return responder_cumprimento("boa noite")
        elif "que horas são" in fala.lower():
            return responder_horas()

    return responder_cumprimento("olá")

def responder_cumprimento(cumprimento):
    return cumprimento.capitalize() + "!"

def responder_horas():
    hora_atual = datetime.now().strftime("%H:%M:%S")
    return f"Agora são {hora_atual}."

if __name__ == '__main__':
    app.run(debug=True)
