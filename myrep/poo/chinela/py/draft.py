class Chinela:
    def __init__(self):
        self.__tam: int = 0

    def getTamanho(self):
        return self.__tam

    def setTamanho(self, value: int):
        if value % 2 != 0 or value < 20 or value > 50:
            print('Erro: não existe gente com pé desse tamanho.')
            return
        self.__tam = value
    
def main():
    chinela = Chinela()

    while chinela.getTamanho() == 0:
        print('Digite o tamanho da sua chinela')
        resposta = int(input())
        chinela.setTamanho(resposta)

    print('Parabéns, você comprou uma chinela tamanho', chinela.getTamanho())
main()