class Calculadora:

    def __init__(self, batteryMax: int = 0):
        self.battery: float = 0
        self.batteryMax: int = batteryMax
        self.display: float = 0

    def __str__(self) -> str:
        return(f'display = {self.display:.2f}, battery = {self.battery}')
    
    def charge(self, increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def useBattery(self) -> bool:
        if self.battery == 0:
            print('fail: bateria insuficiente')
            return False
        self.battery -= 1
        return True

    def sum(self, a: int, b: int):
        if not self.useBattery():
            return
        self.display = a + b

    def div(self, a: int, b: int):
        if not self.useBattery():
            return
        if b == 0:
            print('fail: divisao por zero')
            return
        self.display = a / b


def main():
    calculadora = Calculadora()
    while True:
        line: str = input()
        print(f'${line}', end='\n')
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            baterryMax = int(args[1])
            calculadora = Calculadora(baterryMax)
        elif args [0] == 'show':
            print(calculadora)
        elif args[0] == 'charge':
            inc = int(args[1])
            calculadora.charge(inc)
        elif args[0] == 'sum':
            a = int(args[1])
            b = int(args[2])
            calculadora.sum(a, b)
        elif args[0] == 'div':
            a = int(args[1])
            b = int(args[2])
            calculadora.div(a, b)
        else:
            print('fail: comando invalido')

main()