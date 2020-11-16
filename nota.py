
class MediaFinal:
    def acss(self):
        acs = []
        nome = input('Digite o nome da disciplina: ')
        self.notaAc1 = acs.append(float(input('Digite sua nota ac1: ')))
        self.notaAc2 = acs.append(float(input('Digite sua nota ac2: ')))
        self.notaAc3 = acs.append(float(input('Digite sua nota ac3: ')))
        self.notaAc4 = acs.append(float(input('Digite sua nota ac4: ')))
        self.notaAc5 = acs.append(float(input('Digite sua nota ac5: ')))

        acs.sort()
        acs.pop(0)
        mediaAcs = sum(acs) / 4
        ponderadaAcs = mediaAcs / 2     

        print(f' Sua média das acs da disciplina {nome} é: {mediaAcs}')
        print(f' Sua média ponderada das acs da disciplina {nome} é: {ponderadaAcs}')       

        self.prova = float(input('Digite sua nota da prova: '))
        notaFinal = ponderadaAcs + (self.prova / 2)
            
        print(f'Sua nota final da disciplina {nome} é: {notaFinal} ')

        if notaFinal >= 6:
            print('Parabéns você foi aprovado(a)!!')
        else:
            print('Infelizmente você foi reprovado!')


iniciar = MediaFinal()
iniciar.acss()  