import re
class AnaPython:
    @staticmethod
    def countDef(codigo: str) -> int:
        patron = "def.+:"
        result = re.findall(patron,codigo)
        return len(result)
    

if __name__ == "__main__":
    ejemplo  = """
def roberto():
    pass
def pedro()
    pass
def truepedro():
    pass

Carlos():
    pass
"""
    print(AnaPython.countDef(ejemplo))