class Camisa:
    def __init__(self):
        self.__tamanho: str = ''

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: str): #apenas aceita os valores válidos de tamanho
        tamanhos = ['PP', 'P', 'M', 'G', 'GG', 'XG']

        if valor in tamanhos:
            self.__tamanho = valor
        else:
            print("Não tem camisa desse tamanho! Os tamanhos são: PP, P, M, G, GG, XG.")

def main():
    camisa = Camisa()

    while camisa.getTamanho() == '':
        print('Informe seu tamanho de camisa.')
        tamanho = input()
        camisa.setTamanho(tamanho)

    print('Parabéns, você comprou uma camisa tamanho', camisa.getTamanho())

main()