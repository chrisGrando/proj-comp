"""
*** @author chrisGrando
*** Classe destinada para lógica global do aplicativo.
"""

from csv_data.CsvReader import CsvReader
import os

class AppLogic:
    # Construtor
    def __init__(self, args):
        self.args = args
        self.fullClassPath = os.path.realpath(os.path.dirname(__file__))

    # Executa o programa
    def run(self):
        #Lê o arquivo do Autômato Finito Determinístico
        cr = CsvReader()
        cr.read(self.fullClassPath + "/data/afd.csv")
        table = cr.getTableData()

        for row in table:
            print(row)
