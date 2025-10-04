class Calculadora:

    def __init__(self):
        self.baterry: int = 0
        self.baterryMax: int = 0
        self.display: int = 0

    def __str__(self) -> str:
        return(f'display = {self.display:.2f}, battery = {self.battery}')
    
    def charce(self):


def main():
    calculadora = Calculadora()
    while True:
        line: str = input()
        print(f'S{line}', end='\n')
        args: list[str] = line.split(' ')

        if args[0] == 'end':
            break
        elif args [0] == 'show':
        elif args[0] == 'init':
        elif args[0] == 'charge':
        elif