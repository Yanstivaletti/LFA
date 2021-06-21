# Criaremos um automato de pilha onde a entrada do automato será a setupla:
# 0 -> Q, o conjunto Finito de Estados
# 1 -> E, o conjunto de simbolos de entrada
# 2 -> T, o alfabeto da pilha 
# 3 -> F, as Funções de transição do automato, dado na forma F(q,a,X), onde q é
#      é um estado em Q, a é um simbolo de entrada em E, ou uma transição vazia e X é um simbolo da pilha,
#      ou seja, um elemento em T. E a saida dessa transição é o conjunto de pares (p,y), sendo p um novo estado em Q,
#      e y é a string de símbolos da pilha que substitui X no topo. Então representaremos F por uma matriz na forma:
#       [q0,a0,X0,p0,y0]
#       [q1,a1,X1,p1,y1]
#       [q2,a2,X2,p2,y2]...
#       [qn,an,Xn,pn,yn]
# 4 -> q0, é o estado inicial da pilha
# 5 -> Z0, é o simbolo de inicio da pilha
# 6 -> F, é o conjunto de estados de aceitação ou estados finais do automato.



from converte import vazia_para_estfinal
import traceback
import sys

class Pilha:
    def __init__(self):
        self.itens = []

    def éVazia(self):
        return self.itens == []

    def empilha(self,valor):
        self.itens.append(valor)

    def desempilha(self):
        return self.itens.pop()
    
    def topo(self):
        return self.itens[len(self.itens)-1]
    
    def tamanho(self):
        return len(self.itens)

    def ImprimePilha(Pilha):
        "Pilha Impressa: "
        while not Pilha.éVazia():
            print(Pilha.desempilha())


def automato_apd(file):

    arquivo = open(file, "r")
    setupla = []

    for linha in arquivo:
        linha = linha.replace('\n', '')
        setupla.append(linha)

    if(len(setupla) < 7 or len(setupla) > 7):
        print('Erro! Falta algum(uns) elementos em sua setupla')  #se faltar algum item do APD o programa avisará
        return 0
    else:
        print('\nArquivo Compilado')
        print('\nLinguagem:')
        print('1 - Conjunto de estados')
        print('2 - Alfabeto')
        print('3 - Alfabeto da pilha')
        print('4 - Funções de transição')
        print('5 - Estado inicial')
        print('6 - Símbolo de início da pilha')
        print('7 - Conjunto de estados finais\n')
        for elementos in setupla:                                 #chegagem do arquivo, mostrando todos os
            print(elementos)                                        #requisitos do APD

    estadoInicial = setupla[4]
    setupla[3] = setupla[3].split()
    setupla[6] = setupla[6].split(',')
    setupla[1] = setupla[1].split(',')
    setupla[2] = setupla[2].split(',')
    estadoInicial_pilha = setupla[5]

    transicao = []
    alfabeto_pilha = []
    alfabeto = []
    estadosFinais = []

    for c in setupla[3]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        c = c.split(',')
        transicao.append(c)
    for c in setupla[6]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        estadosFinais.append(c)
    for c in setupla[1]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        alfabeto.append(c)
    for c in setupla[2]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        alfabeto_pilha.append(c)


    cadeia = str(input('\nDigite a cadeia que será lida: '))
    cadeiacount = 0                                            #Usaremos cadeiacount pra saber quantos simbolos do alfabeto existem na cadeia
    for simbolo in alfabeto:
        cadeiacount = cadeiacount + cadeia.count(simbolo)
    if(cadeiacount != len(cadeia)):                             #Caso a quantidade de simbolos lidos não for igual ao tamanho da cadeia, então temos simbolos
        print('Erro! A cadeia possui algum(uns) simbolos que não fazem parte do alfabeto!') # não pertencentes ao alfabeto
        return 0
    if(len(cadeia) == 0 and estadoInicial == estadosFinais[0]):                 #Caso o estado Inicial esteja em um dos estados Finais
        print('A cadeia inserida é vazia e chega a um estado final!\n')
        print('CADEIA ACEITA!\n')
    if(len(cadeia) == 0 and estadoInicial != estadosFinais[0]): 
        print('A cadeia inserida é vazia mas não chega a um estado final!\n')
        print('CADEIA REJEITADA!\n')
    
    else:
        estadoAtual = []
        estadoAtual.append(estadoInicial) #iniciamos o automato com o estado inicial 
        estProximos = []            #criaremos um vetor para guardar todas as possiveis transições do automato
        pilha = Pilha()             #Criamos e instanciamos a pilha com o estadoInicial da Pilha (Z0) 
        if(pilha.éVazia() == True): 
            print('Iniciando Pilha do automato...')
            pilha.empilha(estadoInicial_pilha)
        
        for simbolo in cadeia:                  #Percorremos o simbolo da cadeia
            print("simbolo da cadeia: ",simbolo)    
            for estado in estadoAtual:
                print("Estado analisado: ",estado)    
                for funcao in transicao:             #Percorremos os estados atuais 
                    if (estado == funcao[0]) and (simbolo == funcao[1] or funcao[1] == 'E') and (pilha.topo() == funcao[2] or pilha.topo() == estadoInicial_pilha):
                        print(funcao)
                        print(pilha.topo())
                        
                       #Caso encontremos um estado que cumpra os requisitos, iniciaremos as futuras transições
                       # e alteraremos (ou não) a pilha 
                        estProximos.append(funcao[3])  #Os proximos estados são alocados no vetor 
                        novoTopo = funcao[4]           #O novo topo da pilha será armazenado em 'novoTopo'
                        estados_pilha = list(novoTopo)  #transformamos a string em uma lista para obtermos o elementos inseridos

                        if funcao[4] != 'E': #Trata o caso em que não é uma operação de desempilhamento
                            topo = pilha.desempilha()  
                            pilha.empilha(topo)
                            pilha.empilha(estados_pilha[0]) #O index 0 pega o elemento que será empilhado junto com a pilha
                        else:
                            if pilha.topo() == estadoInicial:   #Caso a pilha esteja vazia, não é possivel desempiplhar
                                continue
                            else:
                                pilha.desempilha() #desempilha da pilha
                                

                estProximos = list(dict.fromkeys(estProximos))                    #E Retiramos repetições de estados ja encontrados
                print(estProximos)
            estadoAtual = estProximos       #Os estados encontrados serão analisados em seguida                                 #Agora os estados atuais serão os estados encontrados anteriormente nos estados de transição
            estProximos = []                #Esvazia a lista para encontramos os proximos estados
        final = 0
        for estado in estadosFinais:
            if estadoAtual == estado: #Se dentro dos estados Atuais há um final, então a cadeia será aceita
                final = 1
                print('CADEIA ACEITA! Estado: ',estadoAtual)
                break
        if not pilha.éVazia():
            topo = pilha.topo()
            if topo == estadoInicial: #Se apenas há Z0 na pilha, entao aceitamos por pilha vazia
                final = 1
                print('CADEIA ACEITA! Pilha Vazia')
        if final == 0:      #Se a cadeia não cumpre nenhuma das requisições, então não é aceita
            print("cadeia rejeitada")


automato_apd('teste.txt')