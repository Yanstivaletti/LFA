import time

def AFND(file):
    ref_quintupla = open(file,"r")      #lemos o arquivo com o AFN
    quintupla = []                      #criamos o vetor para guardar o AFN

    for linha in ref_quintupla:          #guardamos o AFN no vetor
        linha = linha.replace('\n', '')
        quintupla.append(linha)

    if(len(quintupla) < 5 or len(quintupla) > 5):
        print('Erro! Falta algum(uns) elementos em sua quintupla')  #se faltar algum item do AFN o programa avisará
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
            print(elementos)                                        #requisitos do AFN


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
            estAtual = []     #vetor para guardar os estados nos quais estamos no momento
            estProximos = []  #vetor para guardar os estados que o AFN vai percorrer ao analisar o elemento da cadeia
            
            estAtual.append(estadoInicial) #O estado atual é incializado com o estado inicial
            for elemento in cadeia:
              time.sleep(0.9)
              print('\nElemento da cadeia analisado: ',elemento) #printa o elemento analisado
              for estados in estAtual:                         
                print('Estado atual: ',estados)            #printa todos os estados que vamos analisar
                print("Transições:")
                time.sleep(0.5)
                for transicao in estDeTransicao:
                  if(transicao[1] == estados and elemento == transicao[0]): #Se o estado de transição for correspondente nós:
                    estProximos.append(transicao[2])      #Adicionaremos o estado aos proximos estados que iremos percorrer em seguida
                    time.sleep(0.4)
                    #print(f'Estado selecionado: {transicao[2]}')
                    print(transicao)

                estProximos = list(dict.fromkeys(estProximos))                    #E Retiramos repetições de estados ja encontrados
              estAtual = estProximos                                              #Agora os estados atuais serão os estados encontrados anteriormente nos estados de transição
              estProximos = []                                                    #Setamos o vetor para adicionarmos os novos estados que serão encontrados

            time.sleep(1.3)
            print('\nTODA A CADEIA FOI LIDA!\n')
            time.sleep(1.7)

            print('quintupla:')
            print(f'Estados: {quintupla[0]}')
            time.sleep(0.4)
            print(f'Alfabeto: {alfabeto}')
            time.sleep(0.4)
            print(f'Estados de transição: {estDeTransicao}')
            time.sleep(0.4)
            print(f'Estado inicial: {estadoInicial}')
            time.sleep(0.4)
            print(f'Estados finais: {estadosFinais}\n')
            time.sleep(0.4)

            for est in estAtual:
              for final in estadosFinais:      #Procura se a cadeia atingiu algum dos estados finais, se sim a cadeia é aceita
                if(est == final):
                  print('CADEIA ACEITA!')
                  return ''
            print('CADEIA REJEITADA!')          
      

AFND('testesAfn/afnd-termina-com-ab.txt')

