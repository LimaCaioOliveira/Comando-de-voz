import speech_recognition as sr
import os

#Função para ouvir o microfone

#habilitando o microfone
microfone = sr.Recognizer()


#usando o microfone
with sr.Microphone() as source:
    #para reduzir o ruído
    microfone.adjust_for_ambient_noise(source)
    #retorno para o usuário dizer algo
    print("Diga o comando: ")
    #armazena o que foi dito
    audio = microfone.listen(source)

    try:
        frase = microfone.recognize_google(audio,language='pt-br')

        if "navegador" in frase:
            os.system("start Chrome.exe")

        elif "planilha" in frase:
            os.system("start Excel.exe")

        elif "Lol" in frase:
            os.system("start LeagueClient.exe")

        elif "texto" in frase:
            os.system("start Word.exe")

        elif "Estúdio code" in frase:
            os.system("start VSCode.exe")

    except sr.UnknownValueError:
        print("Comando não reconhecido!")
    

