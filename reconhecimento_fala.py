import speech_recognition as sr

def ouvir_microfone():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Diga algo!")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language='pt-BR')
        return texto
    except sr.UnknownValueError:
        print("Não foi possível entender a fala.")
    except sr.RequestError as e:
        print(f"Erro ao acessar o serviço de reconhecimento de fala: {e}")
