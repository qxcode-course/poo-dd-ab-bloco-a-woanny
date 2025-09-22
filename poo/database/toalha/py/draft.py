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
        return 0 # pra dizer quando nenhuma das opções for válida

def main():
    toalha = Towel('', '') 
    while True:
        print('$', end='')
        line: str = input()
        args: list[str] = line.split('')
