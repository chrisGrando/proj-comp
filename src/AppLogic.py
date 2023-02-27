"""
*** @author chrisGrando
*** Classe destinada para lógica global do aplicativo.
"""

from csv_data.CsvReader import CsvReader
from interpreter.SLR import SLR
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
        # Inicializa leitor de planilhas CSV
        cr = CsvReader()

        # Checa se os parâmetros de linha de comando estão corretos
        if (len(self.args) != 4):
            print("Uso incorreto de parâmetros.\nSaindo...")
            exit(0)

        # Caminho para o arquivo da tabela de AFD
        dfaTablePath = self.getAbsPathFile(self.args[1])

        # Caminho para o arquivo do script
        scriptPath = self.getAbsPathFile(self.args[2])

        # Caminho para o arquivo da tabela de SLR
        slrTablePath = self.getAbsPathFile(self.args[3])

        # Lê o arquivo do Autômato Finito Determinístico (AFD)
        cr.read(dfaTablePath)
        dfaTable = cr.getTableData()

        # Gera a fita de entrada
        tape = Tape(dfaTable)
        inputTape = tape.generateTape(scriptPath)

        # Exibe a fita de entrada
        print("*** FITA ***")
        print(inputTape)

        # Gera a fita de tokens
        token = Token()
        tokenTape = token.replaceNumbersWithTokens(inputTape)

        # Exibe a fita de tokens
        print("\n*** TOKENS ***")
        print(tokenTape)

        # Lê o arquivo do Reconhecimento Sintático (SLR)
        cr.read(slrTablePath)
        slrTable = cr.getTableData()

        # Executa o Reconhecimento Sintático (SLR)
        print("\n*** SLR ***")
        slr = SLR(tokenTape, slrTable)
        slr.runSyntaxRecognition()
