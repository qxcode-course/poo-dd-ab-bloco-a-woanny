class Roupa:
    def __init__(self):
        self.__tamanho: str = ''

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, valor: str): #apenas aceita os valores válidos de tamanho
        tamanhos = ['PP', 'P', 'M', 'G', 'GG', 'XG']

        if valor in tamanhos:
            self.__tamanho = valor
        else:
            print('fail: Valor inválido, tente PP, P, M, G, GG ou XG')

    def __str__(self):
        if self.__tamanho == '':
            return 'size: ()'
        else:
            return f'size: ({self.__tamanho})'

def main():
    roupa = Roupa()

    while True:

        line: str = input()
        print(f'${line}', end='\n')
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(roupa)
        elif args[0] == 'size':
            valor = args[1]
            roupa.setTamanho(valor)

main()