import random

class conselho:
    def __init__(self):
        self.resposta = [
            'É melhor orar!',
            'Vai ler a Bíblia, vai!',
            'Nem sempre sua vontade é a do Senhor!',
            'Espera no Senhor!'
        ]

    def iniciar(self):
        input('Faça sua pergunta: ')
        print(random.choice(self.resposta))

pergunta = conselho()
pergunta.iniciar()