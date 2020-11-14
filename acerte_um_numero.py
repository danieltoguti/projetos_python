import random
import PySimpleGUI as sg

class AcerteNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def iniciar(self):

        layout = [
            [sg.Text('Sua tentativa: ', size=(20,0))],
            [sg.Input(size=(18,0),key='ValorTentativa')],
            [sg.Button('Tentar')],
            [sg.Output(size=(30,10))]
        ]

        self.janela = sg.Window('Acerte o Número!', layout=layout)
        self.gerarNumeroAleatorio()

        try:
            while True:
                self.PedirValorAleatorio()
            
                if self.evento == 'Tentar':
                    self.valor_do_chute = self.valores['ValorTentativa']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Valor está acima, digite um valor menor!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Valor está baixo, digite um valor maior')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabéns Você ganhou!')
                            break
        except :
            print("Digite um número inteiro!")
            self.iniciar()

    def PedirValorAleatorio(self):
        self.evento, self.valores = self.janela.Read()

    def gerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

tente = AcerteNumero()
tente.iniciar()
