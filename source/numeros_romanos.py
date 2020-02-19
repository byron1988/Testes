class ConverteNumeroRomano:
    
    def __init__(self):
        self.digito_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        

    def converte_para_decimal(self, numero_romano):
        val = 0
        for char in numero_romano:
            val += self.digito_map[char]
        return val
        