class Towel:
    def __init__(self, color: str, size: str):
        
        self.color: str = color
        self.size: str = size # P M G
        self.wetness: int = 0 # max umidade: P -> 10 M -> 20 G -> 30

    def dry (self, amount: int): #quantidade de umidade recebido

        self.wetness += amount # deveria aumentar a umidade
        
        if self.wetness > self.getMaxWetness():
            print('Toalha encharcada.')
            self.wetness = self.getMaxWetness()

    def wringOut (self): # torce a toalha
        self.wetness = 0

    def getMaxWetness(self): # umidade máxima por tamanho
        if self.size == 'P':
            return 10
        elif self.size == 'M':
            return 20
        elif self.size == 'G':
            return 30
        else:
            return 0 # pra dizer quando nenhuma das opções for válida

def main():
    toalha = Towel('', '') 
    while True:
        print('$', end='\n')
        line: str = input()
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'criar':
            color = args[1]
            size = args [2]
            toalha = Towel(color, size)
        elif args[0] == 'mostrar':
            print(toalha)
        elif args[0] == 'enxugar':
            amount = int(args[1])
            toalha.dry(amount)
        elif args[0] == 'seca':
            print('sim' if toalha.wetness else 'nao') 
        else:
            print('fail: comando desconhecido.')
main()