class Chinela:
    def __init__(self):
        self.__tam: int = 0

    def getTamanho(self, value: int):
        return self.__tam

    def setTamanho(self, value: int):
        if value < 20 or value > 50 and valor % 2 != 0:
            print('Erro: não exite gente com pé desse tamanho.')
            return self
        self.__tam = value
        return self
    
def main():

    chinela = Chinela()

    while chinela.getTamanho == 0:
        print('Digite o tamanho da sua chinela')
        resposta = input()


print('Parabéns, você comprou uma chinela tamanho ', chinela.getTamanho())
main()