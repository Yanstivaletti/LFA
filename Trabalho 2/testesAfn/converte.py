def converte(file):
    ref_quintupla = open(file,"r")      #lemos o arquivo com o AFND
    quintupla = []                      #criamos o vetor para guardar o AFND

    for linha in ref_quintupla:          #guardamos o AFND no vetor
        linha = linha.replace('\n', '')
        quintupla.append(linha)       

    if(len(quintupla) < 5 or len(quintupla) > 5):
        print('Erro! Falta algum(uns) elementos em sua quintupla')  #se faltar algum item do AFD o programa avisará
        return 0
    else :
        
        print('\nArquivo Compilado')
        print('\nLinguagem:')
        print('1 - Conjunto de estados')
        print('2 - Alfabeto')
        print('3 - Estados de transição')
        print('4 - Estado inicial')
        print('5 - Conjunto de estados finais\n')
        for elementos in quintupla:                                 #chegagem do arquivo, mostrando todos os
            print(elementos)                                        #requisitos do AFD

        estadoInicial = quintupla[3]                                #usamos as variaveis estadoInicial e est de Transiçao
        quintupla[2] = quintupla[2].split()                               # para facilitar o entendimento do codigo
        quintupla[4] = quintupla[4].split(',')
        quintupla[1] = quintupla[1].split(',')
        quintupla[0] = quintupla[0].split(',')

        estDeTransicao = []
        estadosFinais = []
        alfabeto = []
        estadosAFND = []

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
        for c in quintupla[0]:
            c = c.replace('[', '')
            c = c.replace(']', '')
            estadosAFND.append(c)
                
        estadoInicialAFD = estadoInicial         #Para traduzirmos o AFND para AFD precisamos criar 
        estadosFinaisAFD = []                   #novos escopos para os estados finais, todos os estados e os estados de transiçao
        alfabetoAFD = alfabeto
        estDeTransicaoAFD = []
        estadosAFD = []
        
        final = 0                               #Criamos um indicador para tratarmos estados finais
        percorrimentoEst = []                   #Usaremos a variavel para percorrer os estados existentes e os que foram criados durante o processo do AFD
        percorrimentoEst.append([estadoInicialAFD]) #O primeiro estado a percorrermos será o Inicial
        novoEstadoAFD = ""                      #A variavel recebe um estado AFD novo
        conjEstAFND = []                        #A variavel recebe um conjunto de estados que devemos percorrer para criar o AFD
        novoEstDeTransicao = []                 #A variavel para alocar um novo estado de transição
        estadoAtual = ''  
                                                #A variavel para localizar e alocar o estado em que estamos em um estado de transição
        for elem in percorrimentoEst:           #percorremos todos os conjuntos de estados do AFND 
            for simbolo in alfabetoAFD:           #e percorremos também o alfabeto para comparação de simbolos em suas transições
                estadoAtual = ''                    #setamos para vazio para continuar o fluxo do for
                for estados in elem:               #percorremos os elementos dos conjuntos de estados do AFND
                    estadoAtual += estados                            #adicionamos os estados atuais na lista para em seguida adicionarmos na transição
                    for transicao in estDeTransicao:                  #percorremos as transições do AFND para criamos os estados e transições novas no AFD
                        if (estados == transicao[1] and simbolo == transicao[0] and transicao[2] not in conjEstAFND): #Se o estado analisado for equivalente ao estado atual e o simbolo for o mesmo criamos um novo estado a partir disto
                            novoEstadoAFD = novoEstadoAFD + transicao[2]   #cria-se o novo estado
                            conjEstAFND.append(transicao[2])          #adicionamos a transição aos conjuntos de estados do AFND
                        if (estados in estadosFinais):                #aqui tratamos caso o estado seja final, pois sabendo disso o adicionaremos aos finais
                            final = 1
                if (novoEstadoAFD not in estadosAFD):   #Caso o novo estado criado nao exista já, o adicionamos nos estados de AFD
                     estadosAFD.append(novoEstadoAFD)
                if (conjEstAFND not in percorrimentoEst):  #Adicionamos ao percorrimento do percorrimentoEst para tratarmos os futuros novos estados criados
                     percorrimentoEst.append(conjEstAFND)
                if (final == 1): 
                     estadosFinaisAFD.append(novoEstadoAFD)  #cria-se o estado final
                novoEstDeTransicao.append(simbolo)   #cria-se o novo estado de transição
                novoEstDeTransicao.append(estadoAtual)
                novoEstDeTransicao.append(novoEstadoAFD)
                if (novoEstDeTransicao not in estDeTransicaoAFD and len(novoEstDeTransicao) != 0):
                     estDeTransicaoAFD.append(novoEstDeTransicao)  #alocamos o novo estado nos estados do AFD
                novoEstDeTransicao = []                         #setamos todas as variaveis para zero/vazio novamente, para que ele possa continuar o fluxo do for
                final = 0
                novoEstadoAFD = ""              
                conjEstAFND = []
        
        estadosAFD = str(estadosAFD)
        estadosAFD = estadosAFD.replace(', ', ',')
        estadosAFD = estadosAFD.replace("'", '')

        alfabeto = str(alfabeto)
        alfabeto = alfabeto.replace(', ', ',')
        alfabeto = alfabeto.replace("'", '')

        estDeTransicaoAFD = str(estDeTransicaoAFD)
        estDeTransicaoAFD = estDeTransicaoAFD.replace('],', ']')
        estDeTransicaoAFD = estDeTransicaoAFD.replace('[[', '[')
        estDeTransicaoAFD = estDeTransicaoAFD.replace(']]', ']')
        estDeTransicaoAFD = estDeTransicaoAFD.replace(', ', ',')
        estDeTransicaoAFD = estDeTransicaoAFD.replace("'", '')
        
        estadosFinais = str(estadosFinais)
        estadosFinais = estadosFinais.replace(', ', ',')
        estadosFinais = estadosFinais.replace("'", '') 

        print("\n\n\nAFD resultante:")
        print(f"\nEstados: {estadosAFD}")
        #time.sleep(1.5)
        print(f"Alfabeto: {alfabeto}")
        #time.sleep(1.5)
        print(f"Estados de Transição: {estDeTransicaoAFD}")
        #time.sleep(1.5)
        print(f"Estado Inicial: {estadoInicial}")
        #time.sleep(1.5)
        print(f"Estados Finais: {estadosFinaisAFD}")
        #time.sleep(1.5)

        arquivo = open('arq.txt', 'w')
        arquivo.write(estadosAFD+'\n')
        arquivo.write(alfabeto+'\n')
        arquivo.write(estDeTransicaoAFD+'\n')
        arquivo.write(estadoInicial+'\n')
        arquivo.write(estadosFinais+'\n')
        arquivo.close()


converte('teste')