class Towel:
    def __init__(self, color, size, wetness):
        
        self.color = color
        self.size = size # P M G
        self.wetness: int = 0 # max umidade: P -> 10 M -> 20 G -> 30

toalha = Towel ("azul", "M", 40)
print(toalha.color)
print(toalha.size)
print(toalha.wetness)