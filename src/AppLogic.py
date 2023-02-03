"""
*** @author chrisGrando
*** Classe destinada para lógica global do aplicativo.
"""

class AppLogic:
    # Construtor
    def __init__(self, args):
        self.args = args

    # Executa o programa
    def run(self):
        print(self.args[0])
