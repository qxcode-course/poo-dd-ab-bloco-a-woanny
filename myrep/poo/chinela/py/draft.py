class Chinela:
    def __init__(self):
        self.__tam: int = 0

    def getTamanho(self, value: int):
        


    def setTamanho(self, value: int):
        #talvez um if aqui pra saber se é par, ver depois de continua 2 if ou elif
        if value % 2 == 0:
            return self.__tam
        if value < 20 or value > 50:
            print('Erro: não exite gente com pé desse tamanho.')
            return self
        self.__tam = value
        return self
    
chinela = Chinela()

while chinela.getTamanho == 0:
    print('Digite o tamanho da sua chinela')
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print('Parabéns, você comprou uma chinela tamanho ', chinela.getTamanho())