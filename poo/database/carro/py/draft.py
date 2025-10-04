class Carro:
    def __init__(self):
            
        self.passa: int = 0
        self.passMax: int = 2
        self.gas: int = 0
        self.gasMax: int = 100
        self.km: int = 0

    def __str__(self) -> str:
        return f'pass: {self.passa}, gas: {self.gas}, km: {self.km}'

    def enter(self):
        if self.passa < self.passMax:
            self.passa += 1
        else:
            print('fail: limite de pessoas atingido')

    def leave(self):
        if self.passa > 0:
            self.passa -= 1
        else:
            print('fail: nao ha ninguem no carro')

    def fuel(self, litros: int):
        self.gas += litros
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, dist: int,):
        if self.passa == 0:
            print('fail: nao ha ninguem no carro')
        elif self.gas == 0:
            print('fail: tanque vazio')
        elif self.gas >= dist:
            self.gas -= dist
            self.km += dist
        else:
            print(f'fail: tanque vazio apos andar {self.gas} km')
            self.km += self.gas
            self.gas = 0


def main():
    carro = Carro()
    while True:
        line: str = input()
        print(f'${line}', end='\n')
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'show':
            print(carro)
        elif args[0] == 'enter':
            carro.enter()
        elif args[0] == 'leave':
            carro.leave()
        elif args[0] == 'fuel':
            litros = int(args[1])
            carro.fuel(litros)
        elif args[0] == 'drive':
            dist = int(args[1])
            carro.drive(dist)
        else:
            print('fail: comando invalido')



main()