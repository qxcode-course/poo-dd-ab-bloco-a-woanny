class Carro:
    def __init__(self):
            
        self.passa: int = 0
        self.km: int = 0
        self.gas: int = 0

    def __str__(self) -> str:
        return f'pass:{self.passa}, gas:{self.gas}, km:{self.km}'
    
    def passMax (self, increment: int):
        self.passa += increment

        if self.passa > 2:
            print('fail: limite de pessoas atingido')
            self.passa = 2

    def gasMax (self):
        if self.gas > 100:
            self.gas = 100


def main():
    carro = Carro()
    while True:
        line: str = input()
        print(f'${line}', end='\n')
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'enter':

        elif args[0] == 'leave':

        elif args[0] == 'fuel':

        elif args[0] == 'drive':

        else:
            print('fail: comando invalido')



main()