import random
import PySimpleGUI as sg


class SimuladorDeDado:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Vamos jogar? '
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]

    
    def iniciar(self):
        self.janela = sg.Window('Simulador de dado', size= (150,150), layout=self.layout)
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.gerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digitar sim ou não')
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def gerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.iniciar()