import time

#Criação de um AFD 
#Para criarmos um algoritmo de um AFD precisamos primeiro definir os estados:
#0 - Estados = ['q0','q1',...,'qn']
#1 - Alfabeto = ['a1','a2',...,'an']
#Os Estados de Transição que serão representados pela Matriz de Estados:
#2- [['a1','q0','q1']
#    ['a2','q1','q2'] 
#    ['a2','q1','q2']... 
#    ['an','qn','qn']]
# 
#3 - Estado inicial = 'q0'
#4 - Estados Finais = ['q1','q2',...,'qn']  

#Portanto o algoritmo receberá esses 5 estados, junto com uma cadeia de caracteres (pertencentes ao alfabeto) e retornará
#se ACEITA ou REJEITA a cadeia.


def AFD(file):
    ref_quintupla = open(file,"r")      #lemos o arquivo com o AFD
    quintupla = []                      #criamos o vetor para guardar o AFD

    for linha in ref_quintupla:          #guardamos o AFD no vetor
        linha = linha.replace('\n', '')
        quintupla.append(linha)

    if(len(quintupla) < 5 or len(quintupla) > 5):
        print('Erro! Falta algum(uns) elementos em sua quintupla')  #se faltar algum item do AFD o programa avisará
        return 0
    else:
        
        print('\nArquivo Compilado')
        print('\nLinguagem:')
        print('1 - Conjunto de estados')
        print('2 - Alfabeto')
        print('3 - Estados de transição')
        print('4 - Estado inicial')
        print('5 - Conjunto de estados finais\n')
        for elementos in quintupla:                                 #chegagem do arquivo, mostrando todos os
            print(elementos)                                        #requisitos do AFD


        estadoInicial = quintupla[3]                                      #usamos as variaveis estadoInicial e est de Transiçao
        quintupla[2] = quintupla[2].split()                               # para facilitar o entendimento do codigo
        quintupla[4] = quintupla[4].split(',')
        quintupla[1] = quintupla[1].split(',')

        estDeTransicao = []
        estadosFinais = []
        alfabeto = []

        for c in quintupla[2]:
            c = c.replace('[', '')
            c = c.replace(']', '')
            c = c.split(',')
            estDeTransicao.append(c)
        for c in quintupla[4]:
            c = c.replace('[', '')
            c = c.replace(']', '')
            estadosFinais.append(c)
        for c in quintupla[1]:
            c = c.replace('[', '')
            c = c.replace(']', '')
            alfabeto.append(c)

        cadeia = str(input('\nDigite a cadeia que será lida: '))
        print()
        cadeiacount = 0                                            #Usaremos cadeiacount pra saber quantos simbolos do alfabeto existem na cadeia
        for simbolo in alfabeto:
            cadeiacount = cadeiacount + cadeia.count(simbolo)
        if(cadeiacount != len(cadeia)):                             #Caso a quantidade de simbolos lidos não for igual ao tamanho da cadeia, então temos simbolos
            print('Erro! A cadeia possui algum(uns) simbolos que não fazem parte do alfabeto!') # não pertencentes ao alfabeto
            return 0
        if(len(cadeia) == 0 and estadoInicial == estadosFinais[0]):
            print('A cadeia inserida é vazia e chega a um estado final!\n')
            print('CADEIA ACEITA!\n')
        if(len(cadeia) == 0 and estadoInicial != estadosFinais[0]):
            print('A cadeia inserida é vazia mas não chega a um estado final!\n')
            print('CADEIA REJEITADA!\n')
        else :
            estadoAtual = estadoInicial
            for elemento in cadeia:

                time.sleep(1)
                print('Elemento lido: ' +elemento)          #Mostra o elemento que vamos analisar
                print('Posição Atual: '+estadoAtual)        #Mostra a posição atual na cadeia
        
                for estados in estDeTransicao:              #For para avaliarmos qual estado iremos escolher
                    if(estados[0] == elemento and estados[1] == estadoAtual):     #estados [0] é o elemento lido 
                                                                                #e estados[1] é o estado em que estamos
                        estadoAtual = estados[2]            #se ambos forem verdadeiros então selecionaremos estados[2]
                        time.sleep(2)
                        print('Estado selecionado: ' + str(estados))
                        time.sleep(1)
                        print(f'Estado atual: {estadoAtual}\n')              
                                                        
                        break
            
            time.sleep(1.3)
            print('TODA A CADEIA FOI LIDA!')

            print('Resultado:')
            time.sleep(0.7)

            if estadoAtual in estadosFinais:
                print('quintupla:\n')
                for elementos in quintupla:
                    print(elementos)
                print('\n')
                print('cadeia inserida:\n')
                print(cadeia)
                print('CADEIA ACEITA!')
                return ''

            print('quintupla:\n')
            for elementos in quintupla:
                print(elementos)
            print('\n')
            print('cadeia inserida:\n')
            print(cadeia)
            print('REJEITADA!')
            return ''

arquivo = input('Digite o caminho do arquivo: ')
print(AFD(arquivo))
