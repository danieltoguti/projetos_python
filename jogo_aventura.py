# Jogo de descisões onde eu terei que criar vários finais diferentes, baseados nas respostas
# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa
# Serão duas opções l1 e l2, sendo que l1 é o vencedor

class JogoAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou sul? (s/n) '
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo) '
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico) '
        self.finalHistoria1 =  'Você será um heroi na linha de frente!'
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar na batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'
    
    def iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            elif resposta1B == 'escudo':
                print(self.finalHistoria2)
            else:
                print('Resposta inválida!')
        
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria3)

jogador1 = JogoAventura()
jogador1.iniciar()