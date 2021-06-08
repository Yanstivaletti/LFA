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
        quintupla[linha] = linha        

    if(len(quintupla) < 5 or len(quintupla) > 5):
        print('Erro! Falta algum(uns) elementos em sua quintupla')  #se faltar algum item do AFD o programa avisará
        return 0
    else :
        
        print('Arquivo Compilado\n')
        for elementos in quintupla:                                 #chegagem do arquivo, mostrando todos os
            print(elementos)                                        #requisitos do AFD
            print('\n')

        estadoInicial = quintupla[3]                                #usamos as variaveis estadoInicial e est de Transiçao
        estDeTransicao = quintupla[2]                               # para facilitar o entendimento do codigo
        estadosFinais = quintupla [4]
        alfabeto = quintupla[1]

        cadeia = input('Digite a cadeia que será lida: ')
        cadeiacount = 0                                             #Usaremos cadeiacount pra saber quantos simbolos do alfabeto existem na cadeia
        for simbolo in alfabeto:
            cadeiacount = cadeiacount + cadeia.count(simbolo)
        if(cadeiacount != len(cadeia)):                             #Caso a quantidade de simbolos lidos não for igual ao tamanho da cadeia, então temos simbolos
            print('Erro! A cadeia possui algum(uns) simbolos que não fazem parte do alfabeto!') # não pertencentes ao alfabeto
            return 0;
        else : 

            estadoAtual = estadoInicial
            for elemento in cadeia:
                print('Posição Atual: '+estadoAtual)        #Mostra a posição atual na cadeia
                print('Elemento lido: ' +elemento)          #Mostra o elemento que vamos analisar
                for estados in estDeTransicao:              #For para avaliarmos qual estado iremos escolher
                    if(estados[0] == elemento and estados[1] == estadoAtual):     #estados [0] é o elemento lido 
                                                                                #e estados[1] é o estado em que estamos
                        estadoAtual = estados[2]                                  #se ambos forem verdadeiros então selecionaremos estados[2]
                        print('Estado selecionado: ' + estados)                  
                                                        
                        break
            for estado in estadosFinais:                                           #agora descobriremos se a cadeia atingiu algum dos estados finais
                if (estado == estadoAtual):
                    print('ACEITA!')                       #se sim a cadeia sera aceita, caso ao contrario sera rejeitada
                    return 1;
            print('REJEITADA!')
            return 0;




