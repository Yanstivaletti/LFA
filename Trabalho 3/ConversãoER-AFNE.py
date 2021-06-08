class Noh:

    def __init__(self, info):       #as primeiras funções são para a criação de uma arvore binária para alocarmos os 

        self.direita = None         #simbolos da expressão regular __init__ cria o nó de uma arvore e a inserção dos mesmos
        self.esquerda = None        #é dado pela função insere
        self.info = info


#observação: a arvore criada não será balanceada, ou seja, temos uma arvore binária desbalanceada para a esquerda, então teremos maior 
# enfase nos operadores da esquerda 

    def insere(self,info):  
        if self.info:
            if info == '*': #como o fechamento é um simbolo unario, alocamos o valor da direita com um termo vazio
                if self.esquerda is None:
                    self.esquerda = Noh(info) 
                    self.esquerda.direita = Noh('') #cria-se o nó vazio na direita
                    return
                else: 
                    self.esquerda.insere(info)  #caso o nó ja tenha nós na direita e esquerda, o codigo prossegue até achar o 
                    return                      #nó na esquerda vazio
            if self.esquerda is None:
                self.esquerda = Noh(info)
                return
            if self.direita is None:
                self.direita = Noh(info)
                return
            else:
                self.esquerda.insere(info)
        else:
            if info == '*':         #tratamos o operador "*" no final da função caso ele seja o primeiro item a 
                self.info = info    #ser inserido dentro da arvore
                self.direita = Noh('')
                return
            else:
                self.info = info
    
    def PrintaArvore(self):             #função que nos ajuda a reconhecer os nós da arvore
        if self.esquerda:
            self.esquerda.PrintaArvore()
        if self.direita:
            self.direita.PrintaArvore()
        print(self.info)
       

    
alfabeto = []
estados = []
estDeTransicao = []

#a função ExpressionTree realizará toda a conversão da Expressão Regular para um automato
#observações:
# - a computação da função é dada de forma recursiva, dado que é a opção menos complexa para unirmos transições e estados 
# - Iniciamos a expressão com os parametros da quintupla, para que assim o preenchimento seja realizado de forma automatica
# - Tratamos a transição vazia usando o simbolo 'E' para ajudar no entendimento da construção da quintupla
# - Usaremos contadores: contInicial e contFinal para gerar novos estados iniciais e finais respectivamente

def ExpressionTree(raiz, estados=[], alfabeto=[], estDeTransicao=[], contInicial = 1, contFinal = 1): #Onde sera criado o AFNE
    estadoInicial = ''                  #iniciamos a função com os estados Final e Inicial vazios, e tratamos 
    estadoFinal = ''                    #'q0' como o estado inicial global, ou seja, ele que será o referencial para o inicio do automato
    estadoInicialGlobal = 'q0'
    

    if estadoInicialGlobal not in estados:      #Caso um dos estados iniciais gerados pelo automato não foi reconhecido ele será tratado no if
        estados.append(estadoInicialGlobal)     # e adicionado a lista de estados globais

    if raiz.info is None:                       #Tratamento para caso a arvore seja vazia
        estDeTransicao.append(['E',estadoInicialGlobal,estadoInicialGlobal])
        return raiz.info,estados,alfabeto,estDeTransicao,estadoInicialGlobal,estadoInicialGlobal,contInicial, contFinal

    if raiz.info == 'E':                        #Este if cobre o caso de uma linguagem vazia, ou seja, L(R) = {E}, criando um estado incial e final
        estadoInicial = 'q0'+str(contInicial)   # e os conectando por uma transição vazia.
        if contInicial == 1:
            estDeTransicao.append(['E', estadoInicialGlobal, estadoInicial])
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
        if contInicial == 1:
            estDeTransicao.append(['E', estadoInicialGlobal, estadoInicial])
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
        estadoInicial = 'q0'+str(contInicial)               #Para o operador '+' temos a criação de um estado inicial que se conecta aos estados 
        estadoFinal = 'qf'+str(contFinal)                   # da esquerda e da direita (a,b) por meio de uma transição vazia e logo depois duas transições 
        contInicial += 1                                    # que conectam os estados da esquerda e da direita a um estado final(c,d)
        contFinal += 1
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
        contInicial += 1                                #outro do esquerdo ao final, e por ultimo, outro estado de transição que realiza transições vazias no estado
        contFinal += 1                                  #que se encontra no nó esquerdo, são essas todas as regras para termos um automato gerado pelo fechamento.
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



#arvore teste
root = Noh('+')
root.insere('.')
root.insere('a')
root.insere('+')
root.insere('b')
root.insere('*')
root.insere('b')
root.insere('a')
''' Teste
root = Noh('+')
root.insere('.')
root.insere('0')
root.insere('*')
root.insere('1')
root.insere('1')'''
'''Teste 2
root = Noh('*')
root.insere('.')
root.insere('*')
root.insere('1')
root.insere('+')
root.insere('.')
root.insere('0')
root.insere('1')
root.insere('0')
'''
'''Teste 3
root = Noh('*')
root.insere('.')
root.insere('.')
root.insere('0')
root.insere('*')
root.insere('1')
root.insere('.')
root.insere('*')
root.insere('1')
root.insere('.')
root.insere('0')
root.insere('0')

'''
'''Teste 4
root = Noh('.')
root.insere('.')
root.insere('0')
root.insere('*')
root.insere('0')
root.insere('+')
root.insere('1')
root.insere('0')
'''
'''Teste 5
root = Noh('.')
root.insere('.')
root.insere('1')
root.insere('+')
root.insere('0')
root.insere('0')
root.insere('1')
'''
'''Teste 6
root = Noh('*')
root.insere('.')
root.insere('0')
root.insere('1')
'''

#root.PrintaArvore()
#root.info = None
root2 = Noh('E')
print('\n\n')
automato = ExpressionTree(root, estados, alfabeto, estDeTransicao)
print('\n\n')

print(automato)

geraArquivo(automato)