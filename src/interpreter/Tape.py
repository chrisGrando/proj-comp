"""
*** @author chrisGrando
*** Classe destinada para a construção da fita de entrada.
"""

class Tape:
    # Construtor
    def __init__(self, dfaTable):
        self.dfaTable = dfaTable

    # Lê código fonte do arquivo
    def readCode(self, src):
        fullCode = None
        stringCode = ""

        # Abre o arquivo e armazena todas as linhas em array
        with open(src, mode = 'r') as file:
            fullCode = file.readlines()
            file.close()

        # Converte array em string
        for row in fullCode:
            stringCode += row + "\n"

        # Retorna código lido em string
        return stringCode
    
    # Encontra o número da linha que contém a primeira cédula
    def findLineId(self, table, content):
        result = -1

        # Vasculha todas as linhas
        for i in range(len(table)):
            cell = table[i][0]

            # Cédula confere com a descrição
            if (cell == content or cell == ("*" + content)):
                result = i
                break
        
        # Retorna a posição (-1 => não encontrado)
        return result

    # Obtém o valor do símbolo na tabela de AFD
    def findSymbolValue(self, symbol):
        header = self.dfaTable[0]
        positionOnHeader = None
        result = None

        # Procura pelo índice do símbolo na primeira linha da tabela
        for i in range(1, len(header)):
            if (header[i] == symbol):
                positionOnHeader = i
                break

        # Se o símbolo não for encontrado, retorna estado de erro
        if (positionOnHeader == None):
            result = 6
        # Mas se o símbolo for encontrado, retorna o seu valor no estado "0"
        else:
            linePosition = self.findLineId(self.dfaTable, "0")
            result = self.dfaTable[linePosition][positionOnHeader]

        # Retorna o ID do estado
        return result

    # Gera a fita de entrada
    def generateTape(self, inputFile):
        code = self.readCode(inputFile)
        tape = ""
        previous = None

        # Vasculha cada caractere do script
        for c in code:
            # É espaço em branco?
            if (c.isspace()):
                if (previous != " "):
                    tape += " "
            # É um caractere ASCII?
            elif (c.isascii()):
                tape += self.findSymbolValue(c)
            # Caractere inválido
            else:
                continue
            
            # Atualiza caractere anterior
            if(len(tape) > 0):
                position = len(tape) - 1
                previous = tape[position]
            else:
                previous = tape

        # Insere um "$" no final da fita
        if (previous.isspace()):
            tape += "$"
        else:
            tape += " $"

        # Retorna a nova fita gerada
        return tape
