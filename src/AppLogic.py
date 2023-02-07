"""
*** @author chrisGrando
*** Classe destinada para lógica global do aplicativo.
"""

from csv_data.CsvReader import CsvReader
from interpreter.Tape import Tape
from interpreter.Token import Token
import os

class AppLogic:
    # Construtor
    def __init__(self, args):
        self.args = args
        self.fullClassPath = os.path.realpath(os.path.dirname(__file__))

    # Obtém caminho absoluto do arquivo
    def getAbsPathFile(self, path):
        finalPath = None

        # Se o caminho já for absoluto, mantém como está
        if (os.path.isabs(path)):
            finalPath = path
        # Se o caminho for relativo, converte para absoluto
        else:
            finalPath = self.fullClassPath + "/" + path
        
        return finalPath

    # Executa o programa
    def run(self):
        # Checa se os parâmetros de linha de comando estão corretos
        if (len(self.args) != 3):
            print("Uso incorreto de parâmetros.\nSaindo...")
            exit(0)

        # Caminho para o arquivo da tabela de AFD
        tablePath = self.getAbsPathFile(self.args[1])

        # Caminho para o arquivo do script
        scriptPath = self.getAbsPathFile(self.args[2])

        # Lê o arquivo do Autômato Finito Determinístico
        cr = CsvReader()
        cr.read(tablePath)
        table = cr.getTableData()

        # Gera a fita de entrada
        tape = Tape(table)
        inputTape = tape.generateTape(scriptPath)

        # Gera a fita de tokens
        token = Token()
        tokenTape = token.replaceNumbersWithTokens(inputTape)

        # Exibe a fita de entrada
        print("*** FITA ***")
        print(inputTape)

        # Exibe a fita de tokens
        print("\n*** TOKENS ***")
        print(tokenTape)
