"""
*** @author chrisGrando
*** Classe destinada para lógica global do aplicativo.
"""

from csv_data.CsvReader import CsvReader
from interpreter.Tape import Tape
import os

class AppLogic:
    # Construtor
    def __init__(self, args):
        self.args = args
        self.fullClassPath = os.path.realpath(os.path.dirname(__file__))

    # Executa o programa
    def run(self):
        # Lê o arquivo do Autômato Finito Determinístico
        cr = CsvReader()
        cr.read(self.fullClassPath + "/data/afd.csv")
        table = cr.getTableData()

        # Gera a fita de entrada
        tape = Tape(table)
        inputTape = tape.generateTape(self.fullClassPath + "/data/script.cdc")

        # Depurar...
        self.debugMyApp(
            table,
            tape.readCode(self.fullClassPath + "/data/script.cdc"),
            inputTape
        )

    # Função para testes
    def debugMyApp(self, table, code, tape):
        # Parâmetros de linha de comando
        print("*** PARÂMETROS ***")
        print(self.args)

        # Tabela de AFD
        print("\n*** AFD ***")
        for row in table:
            print(row)

        # Código fonte
        print("\n*** SCRIPT ***")
        print(code, end='')

        # Fita de entrada
        print("*** FITA ***")
        print(tape)
