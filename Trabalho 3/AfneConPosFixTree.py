class Noh:

    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None

def isOperator(c):
    if (c == '+' or c == '*' or c == '.'):
        return True
    else:
        return False

def inorder(t):
    if t is not None:
        inorder(t.esquerda)
        print(t.info)
        inorder(t.direita)

def constructTree(postfix):
    stack = []
    for char in postfix:
        if not isOperator(char):
            t = Noh(char)
            stack.append(t)
        else:
            t = Noh(char)
            t1 = stack.pop()    
            t2 = stack.pop() if stack else None
            t.direita = t1
            t.esquerda = t2

            stack.append(t)

    t = stack.pop()

    return t

def PrintaArvore(self):             #função que nos ajuda a reconhecer os nós da arvore
    if self.direita:
        PrintaArvore(self.direita)
    if self.esquerda:
        PrintaArvore(self.esquerda)
    print(self.info)



def ExpressionTree(raiz, estados=[], alfabeto=[], estDeTransicao=[], contInicial = 1, contFinal = 1): #Onde sera criado o AFNE
    estadoInicial = ''                  #iniciamos a função com os estados Final e Inicial vazios, e tratamos 
    estadoFinal = ''                    #'q0' como o estado inicial global, ou seja, ele que será o referencial para o inicio do automato    

    if raiz.info is None:                       #Tratamento para caso a arvore seja vazia
        estadoInicial = 'q0'+str(contInicial)
        contInicial += 1
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        estDeTransicao.append(['E',estadoInicial,estadoInicial])
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,[],contInicial, contFinal

    if raiz.info == 'E':                        #Este if cobre o caso de uma linguagem vazia, ou seja, L(R) = {E}, criando um estado incial e final
        estadoInicial = 'q0'+str(contInicial)   # e os conectando por uma transição vazia.
        contInicial += 1
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        estDeTransicao.append([raiz.info, estadoInicial, estadoInicial])
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoInicial,contInicial,contFinal

    if raiz.info == '': #If para tratarmos o caso especial de ser um nó de fechamento 
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoFinal,contInicial, contFinal
  
    # Neste trecho de código tratamos os nós folhas da arvore, criando as primeiras transições e estados para seguirmos com o código
    if raiz.esquerda is None and raiz.direita is None:
              
        estadoInicial = 'q0'+str(contInicial)
        estadoFinal = 'qf'+str(contFinal)
        contInicial += 1
        contFinal += 1
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        if estadoFinal not in estados:
            estados.append(estadoFinal)
        estDeTransicao.append([raiz.info, estadoInicial, estadoFinal])
        if raiz.info not in alfabeto and raiz.info != 'E': #If para tratarmos a inserção de um simbolo
            alfabeto.append(raiz.info)                     #não visto antes ao alfabeto
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoFinal,contInicial, contFinal

#as duas linhas de codigo, esquerda e direita, são onde as recursoes dentro do código acontecem, adicionamos prints para retratar melhor 
#as recursões dentro do código

    esquerda = ExpressionTree(raiz.esquerda, estados, alfabeto, estDeTransicao, contInicial, contFinal)
    contInicial = esquerda[6]
    contFinal = esquerda[7]
    print(esquerda)
 
    direita = ExpressionTree(raiz.direita, estados, alfabeto, estDeTransicao, contInicial, contFinal)
    contInicial = direita[6]
    contFinal = direita[7]
    print(direita)
    
#as seguintes linhas de código tratam os operadores de uma expressão regular, utilizando os conceitos de conversão estudados em aula:

    if raiz.info == '+':
        estadoInicial = esquerda[4]              #Para o operador '+' temos a criação de um estado inicial que se conecta aos estados 
        estadoFinal = direita[5]                   # da esquerda e da direita (a,b) por meio de uma transição vazia e logo depois duas transições 
                                                            # que conectam os estados da esquerda e da direita a um estado final(c,d)
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        if estadoFinal not in estados:
            estados.append(estadoFinal)
        estDeTransicao.append(['E', estadoInicial, esquerda[4]]) #a
        estDeTransicao.append(['E', estadoInicial, direita[4]]) #b
        estDeTransicao.append(['E', esquerda[5], estadoFinal]) #c
        estDeTransicao.append(['E', direita[5], estadoFinal]) #d
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoFinal,contInicial, contFinal

       
      
    elif raiz.info == '.':                               #Para o operador '.' temos a criação de um estado de transição que conecta o estado
        estadoInicial = esquerda[4]                      #da direita com o da esquerda com uma transição vazia
        estadoFinal = direita[5]
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        if estadoFinal not in estados:
            estados.append(estadoFinal)
        estDeTransicao.append(['E', esquerda[5], direita[4]])
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoFinal,contInicial, contFinal
        
      
    elif raiz.info == '*':
        estadoInicial = 'q0'+str(contInicial)           #Para o operador '*' temos a criação de um estado Inicial que se conecta ao Final por meio de uma 
        estadoFinal = 'qf'+str(contFinal)               #transição vazia, outro estado de transição que referencia o lado esquerdo da arvore ao estado inicial,
        contFinal += 1                                  #outro do esquerdo ao final, e por ultimo, outro estado de transição que realiza transições vazias no estado
        contInicial += 1                                #que se encontra no nó esquerdo, são essas todas as regras para termos um automato gerado pelo fechamento.
        if estadoInicial not in estados:
            estados.append(estadoInicial)
        if estadoFinal not in estados:
            estados.append(estadoFinal)
        estDeTransicao = esquerda[3]
        estDeTransicao.append(['E', estadoInicial, estadoFinal])
        estDeTransicao.append(['E', estadoInicial, esquerda[4]])
        estDeTransicao.append(['E', esquerda[5], esquerda[4]])
        estDeTransicao.append(['E', esquerda[5], estadoFinal])
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicial,estadoFinal,contInicial, contFinal


def geraArquivo(automato):              #Logo após a formação da quintupla geramos o arquivo que guarda todos os elementos da quintupla
    estados = str(automato[1])          #esses elementos serão usados no AFNE para sabermos se a cadeia é aceitada ou rejeitada
    alfabeto = str(automato[2])
    estDeTransicao = str(automato[3])
    estadoInicial = automato[1][0]
    estadoFinal = str([automato[5]])

    arquivo = open('AFNE.txt', 'a')

    estados = estados.replace("'", "")
    estados = estados.replace(' ', '')
    alfabeto = alfabeto.replace("'", "")
    alfabeto = alfabeto.replace(' ', '')
    estDeTransicao = estDeTransicao.replace('[[', '[')
    estDeTransicao = estDeTransicao.replace(']]', ']')
    estDeTransicao = estDeTransicao.replace('], ', '] ')
    estDeTransicao = estDeTransicao.replace("'", '')
    estDeTransicao = estDeTransicao.replace(', ', ',')
    estadoFinal = estadoFinal.replace("'", '')

    arquivo.write(estados+'\n')
    arquivo.write(alfabeto+'\n')
    arquivo.write(estDeTransicao+'\n')
    arquivo.write(estadoInicial+'\n')
    arquivo.write(estadoFinal)

alfabeto = []
estados = []
estDeTransicao = []


postfix = '00.01+*.'

r = constructTree(postfix)

PrintaArvore(r)

automato = ExpressionTree(r, estados, alfabeto, estDeTransicao)
print('\n\n')

print(automato)

geraArquivo(automato)