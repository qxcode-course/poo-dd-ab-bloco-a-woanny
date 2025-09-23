class Animal:
    def __init__(self, species: str, sound: str):

        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

    def ageBy (self, increment: int):

        self.age += increment

        if self.age > 4:
            print()
            self.age = 4

    def makeSound (self):

        if self.age == 0:
            print('---')
        elif self.age == 4:
            print('RIP')
        else:
            print(self.sound)

def main():
    animal = Animal('', '')
    while True:
        print('$', end='')
        line: str = input()
        args: list[str] = line.split('')

        if args[0] == 'end':
            break
        elif args[0] == 'init':
            species = args[1]
            sound = args[2]
            animal = Animal(species, sound)
        elif args [0] == 'show':
            print()
        elif args[0] == 'noise':
            print(animal.makeSound)
        elif args[0] == 'grow':
            print(animal.ageBy)
        

main()