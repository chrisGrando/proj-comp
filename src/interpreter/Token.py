"""
*** @author chrisGrando
*** Classe destinada para a substituição dos números da fita
*** de entrada pelos seus respectivos tokens.
"""

class Token:
    # Construtor
    def __init__(self):
        self.tokenList = [
            " ",
            "+",
            "*",
            "(",
            ")",
            "id",
            "X",
            "$"
        ]

    # Substitui os números pelos tokens
    def replaceNumbersWithTokens(self, tape):
        newTape = ""

        # Vasculha todos os caracteres da fita
        for c in tape:
            if (c == "$"):
                newTape += self.tokenList[7]
                break
            elif (c.isspace()):
                newTape += self.tokenList[0]
            elif (c == "1"):
                newTape += self.tokenList[1]
            elif (c == "2"):
                newTape += self.tokenList[2]
            elif (c == "3"):
                newTape += self.tokenList[3]
            elif (c == "4"):
                newTape += self.tokenList[4]
            elif (c == "5"):
                newTape += self.tokenList[5]
            else:
                newTape += self.tokenList[6]
        
        # Retorna a nova fita com os tokens
        return newTape
