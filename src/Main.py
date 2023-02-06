"""
*** @author chrisGrando
*** Classe destinada somente à inicialização básica.
*** (Lógica do software fica armazenada em AppLogic)
"""

from AppLogic import AppLogic
import sys

class Main:
    # Função principal
    @staticmethod
    def main():
        app = AppLogic(sys.argv)
        app.run()

# Chama a função "main" ao iniciar
if __name__ == "__main__":
    Main.main()
