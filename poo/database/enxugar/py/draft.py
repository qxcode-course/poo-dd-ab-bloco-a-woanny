class Towel:
    def __init__(self, color: str, size: str):
        
        self.color: str = color
        self.size: str = size # P M G
        self.wetness: int = 0 # max umidade: P -> 10 M -> 20 G -> 30

    def dry (self, amount: int): #quantidade de umidade recebido
        self.wetness += amount # deveria aumentar a umidade
        if self.wetness >= self.getMaxWetness():
            print('toalha encharcada')
            self.wetness = self.getMaxWetness()

    def getMaxWetness(self): # umidade máxima por tamanho
        if self.size == 'P':
            return 10
        if self.size == 'M':
            return 20
        if self.size == 'G':
            return 30
        return 0 # pra dizer quando nenhuma das opções for válida

    def wringOut (self): # torce a toalha
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def __str__(self):
        return f'Cor: {self.color}, Tamanho: {self.size}, Umidade: {self.wetness}'

def main():
    toalha = Towel('', '') 
    while True:
        line: str = input()
        print(f'${line}', end='\n')
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
            print('sim' if toalha.isDry() else 'nao') 
        elif args[0] =='torcer':
            toalha.wringOut()
        else:
            print('fail: comando desconhecido.')
main()