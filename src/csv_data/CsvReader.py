"""
*** @author chrisGrando
*** Classe destinada para leitura de arquivo CSV (planilhas).
"""

import csv

class CsvReader:
    # Construtor
    def __init__(self):
        self.contents = []

    # Abre e lê o arquivo CSV
    def read(self, file):
        with open(file, mode = 'r') as csvFile:
            # Lê o arquivo
            csvTable = csv.reader(csvFile, delimiter = ',')

            # Armazena conteúdo do arquivo em array
            for row in csvTable:
                self.contents.append(row)
            
            # Fecha o arquivo
            csvFile.close

    # Retorna o conteúdo do arquivo lido
    def getTableData(self):
        return self.contents
