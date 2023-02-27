"""
*** @author chrisGrando
*** Classe destinada para realizar o reconhecimento sintático
*** a partir da fita de entrada.
"""

class SLR:
    # Construtor
    def __init__(self, tape, slrTable):
        self.tape = tape
        self.slrTable = slrTable
        self.codeStack = ["0"]
        self.reductionCode = [
            ["E", "E", "+", "T"],
            ["E", "T", None, None],
            ["T", "T", "*", "F"],
            ["T", "F", None, None],
            ["F", "(", "E", ")"],
            ["F", "id", None, None]
        ]

    # Obtém o próximo elemento da fita
    def getNextElement(self):
        # Checa se a fita NÃO está vazia
        if (self.tape and not self.tape.isspace()):
            # Divide a fita em um vetor
            tapeArray = self.tape.split()

            # Pega o primeiro elemento do vetor
            element = tapeArray.pop(0)

            # Remove o elemento obtido da fita (se não for um $)
            if (element != "$"):
                self.tape = self.tape.replace(element, '', 1)

            # Se o primeiro caractere da nova fita for um espaço, então o remova da fita
            if (len(self.tape) > 0):
                if (self.tape[0].isspace()):
                    self.tape = self.tape.replace(self.tape[0], '', 1)

            # Retorna o elemento obtido
            return element
        # Fita está vazia
        else:
            return None
    
    # Obtém o número da coluna que contém o rótulo especificado
    def getLabelPosition(self, label):
        header = self.slrTable[0]
        position = -1

        # Vasculha todas as colunas do cabeçalho
        for i in range(len(header)):
            if (header[i] == label):
                position = i
                break

        # Retorna a posição da coluna ou "-1" caso não encontrada
        return position

    # Converte código da operação para número inteiro
    def opToInt(self, op):
        aux = op.replace('s', '')
        aux = aux.replace('r', '')
        value = int(aux)
        return value
    
    # Obtém posição na tabela do estado de "Aceita"
    def getAcceptPosition(self):
        # Coluna
        colID = self.getLabelPosition("$")

        # Linha
        rowID = -1
        for i in range(len(self.slrTable)):
            row = self.slrTable[i]
            if (row[colID] == "acc"):
                rowID = i
                break

        # Retorna o número da linha
        return rowID

    # Operação de empilhamento
    def stackUp(self, token, state, stack):
        # Converte ID do estado para inteiro
        intState = self.opToInt(state)

        # Cria nova pilha e adiciona o token e o estado nela
        newStack = stack.copy()
        newStack.append(token)
        newStack.append(str(intState))
        
        # Retorna nova pilha
        return newStack

    # Operação de redução
    def reduction(self, code, stack):
        # Converte ID do código para linha da lista "reductionCode"
        intOpCode = self.opToInt(code) - 1
        opCode = self.reductionCode[intOpCode][0]
        
        # Cria nova pilha
        newStack = stack.copy()

        # Remove os dois últimos itens da pilha 
        lastItem = len(newStack) - 1
        newStack.pop(lastItem)
        lastItem = len(newStack) - 1
        newStack.pop(lastItem)

        # Pega o ID da linha do topo da pilha
        lastItem = len(newStack) - 1
        rowID = int(newStack[lastItem]) + 1

        # Pega o ID da coluna
        colID = self.getLabelPosition(opCode)

        # Obtém o estado encontrado na cédula
        state = self.slrTable[rowID][colID]

        # Se novo estado for "–", então elimina itens da pilha
        # até ela esvaziar ou encontrar estado de "Aceita"
        if (state == "–"):
            id = str(self.getAcceptPosition() - 1)

            while (len(newStack) > 0):
                lastItem = len(newStack) - 1

                # Para ao encontrar ID da linha do "Aceita"
                if (newStack[lastItem] == id):
                    break

                # Remove último elemento
                newStack.pop(lastItem)

            # Acrescenta elemento nulo se a pilha esvaziou totalmente
            if (len(newStack) == 0):
                newStack.append(None)
        # Novo estado é válido
        else:
            # Insere novo token e novo estado na pilha
            newStack.append(opCode)
            newStack.append(state)

        # Retorna nova pilha
        return newStack

    # Atualiza progresso na tela
    def updateProgress(self, codeStack, tape, ap):
        print()
        print("PILHA ==>", codeStack)
        print("FITA ===>", tape)
        print("AÇÃO ===>", ap)

    # Executa o reconhecimento sintático da fita
    def runSyntaxRecognition(self):
        print("PILHA ==>", self.codeStack)
        print("FITA ===>", self.tape)
        print("AÇÃO ===> ['0', None]")

        # Controladores
        next = self.getNextElement()
        ap = [self.codeStack[0], next]
        accept = False
        reject = False

        # Atualiza progresso na tela
        self.updateProgress(self.codeStack, self.tape, ap)
        
        # Roda até encontrar a situação de "Aceita" ou "Rejeita"
        while (not accept and not reject):
            # Permite ou não seguir para o próximo elemento da fita
            updateTape = False

            # Situação de "Rejeita"
            if (ap[0] == None and ap[1] == "$"):
                reject = True
                continue

            # Obtém item da tabela de SLR
            rowID = int(ap[0]) + 1
            colID = self.getLabelPosition(ap[1])
            currentItem = None
            # Checa se a posição na tabela de SLR é valida
            if (colID > 0 and (rowID > 0 and rowID < len(self.slrTable))):
                currentItem = self.slrTable[rowID][colID]

            # Operação de empilhamento
            if (("s" in currentItem) or currentItem.isdigit()):
                self.codeStack = self.stackUp(ap[1], currentItem, self.codeStack)
                updateTape = True
            # Operação de redução
            elif ("r" in currentItem):
                self.codeStack = self.reduction(currentItem, self.codeStack)
            # Situação de "Aceita"
            elif (currentItem == "acc"):
                accept = True
                print()
                continue
            # Condição de erro
            else:
                ap[0] = None
                ap[1] = "$"
                print()
                continue

            # Atualiza controladores
            if (updateTape):
                next = self.getNextElement()
            last = len(self.codeStack) - 1
            ap = [self.codeStack[last], next]

            # Atualiza progresso na tela
            self.updateProgress(self.codeStack, self.tape, ap)

        # Resultado do reconhecimento sintático
        if (accept):
            print("* Resultado: ACEITA")

        if (reject):
            print("* Resultado: REJEITA")
