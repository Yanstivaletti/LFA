def vazia_para_estfinal(file):

    arquivo = open(file, "r")
    sextupla = []

    for linha in arquivo:
        linha = linha.replace('\n', '')
        sextupla.append(linha)

    if(len(sextupla) < 7 or len(sextupla) > 7):
        print('Erro! Falta algum(uns) elementos em sua sextupla')  #se faltar algum item do APD o programa avisará
        return 0

    
    estadoInicial = sextupla[4]
    sextupla[0] = sextupla[0].split(',')
    sextupla[3] = sextupla[3].split()
    sextupla[1] = sextupla[1].split(',')
    sextupla[2] = sextupla[2].split(',')
    estadoInicial_pilha = sextupla[5]

    transicao = []
    alfabeto_pilha = []
    alfabeto = []
    estadosFinais = []
    estados = []

    for c in sextupla[0]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        estados.append(c)
    for c in sextupla[3]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        c = c.split(',')
        transicao.append(c)
    for c in sextupla[1]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        alfabeto.append(c)
    for c in sextupla[2]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        alfabeto_pilha.append(c)

    novo_estFinal = 'EF' #Cria-se um novo estado Final (Estado Final)
    for estado in estados: #Para cada estado do automato, adicionamos uma transição vazia para o novo estado criado
        novo_estTransicao = [estado,'E',estadoInicial_pilha,novo_estFinal,estadoInicial_pilha]
        transicao.append(novo_estTransicao)  #Adicionamos uma transição vazia para cada vez que a pilha esteja vazia, chegarmos em tal estado

    estados.append(novo_estFinal) #adicionamos o novo estado gerado aos estados conhecidos
    estadosFinais.append(novo_estFinal)

    estados = str(estados)
    estados = estados.replace(', ', ',')
    estados = estados.replace("'", '')

    alfabeto = str(alfabeto)
    alfabeto = alfabeto.replace(', ', ',')
    alfabeto = alfabeto.replace("'", '')

    alfabeto_pilha = str(alfabeto_pilha)
    alfabeto_pilha = alfabeto_pilha.replace(', ', ',')
    alfabeto_pilha = alfabeto_pilha.replace("'", '')

    transicao = str(transicao)
    transicao = transicao.replace('],', ']')
    transicao = transicao.replace('[[', '[')
    transicao = transicao.replace(']]', ']')
    transicao = transicao.replace(', ', ',')
    transicao = transicao.replace("'", '')

    estadosFinais = str(estadosFinais)
    estadosFinais = estadosFinais.replace(', ', ',')
    estadosFinais = estadosFinais.replace("'", '')

    arquivo = open('APD_EstadoFinal.txt', 'w')
    arquivo.write(estados+'\n')
    arquivo.write(alfabeto+'\n')
    arquivo.write(alfabeto_pilha+'\n')
    arquivo.write(transicao+'\n')
    arquivo.write(estadoInicial+'\n')
    arquivo.write(estadoInicial_pilha+'\n')
    arquivo.write(estadosFinais)
    arquivo.close()

    return 1


def estfinal_para_vazia(file):

    arquivo = open(file, "r")
    setupla = []

    for linha in arquivo:
        linha = linha.replace('\n', '')
        setupla.append(linha)

    if(len(setupla) < 7 or len(setupla) > 7):
        print('Erro! Falta algum(uns) elementos em sua setupla')  #se faltar algum item do APD o programa avisará
        return 0

    estadoInicial = setupla[4]
    setupla[0] = setupla[0].split(',')
    setupla[3] = setupla[3].split()
    setupla[6] = setupla[6].split(',')
    setupla[1] = setupla[1].split(',')
    setupla[2] = setupla[2].split(',')
    estadoInicial_pilha = setupla[5]

    transicao = []
    alfabeto_pilha = []
    alfabeto = []
    estadosFinais = []
    estados = []

    for c in setupla[0]:
        c = c.replace('[', '')
        c = c.replace(']', '')
        estados.append(c)
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

    novo_estInicial = 'EIC' #Cria-se um novo estado inicial (Estado Inicial Convertido)
    novoSimbolo_Pilha = 'NSP' #Cria-se um novo simbolo para a pilha

    #adicionar uma transicao de p0 pro estado inicial do automato existente, com X0 no topo da pilha, e empilhando Z0
    transicao.append([novo_estInicial,'E',novoSimbolo_Pilha,estadoInicial,estadoInicial_pilha])

    novo_estFinal = 'EFC' #Cria-se um novo estado Final (Estado Final Convertido)
    for estado in estadosFinais: #percorremos todos os estado juntos dos simbolos da pilha para gerarmos todas 
        for simbolo in alfabeto_pilha: #as transições que levam ao EFC
            novo_estTransicao = [estado,'E',simbolo,novo_estFinal,'E']
            transicao.append(novo_estTransicao) #adicionamos as transições

    for simbolo in alfabeto_pilha:
        estadoFinal = [novo_estFinal,'E',simbolo,novo_estFinal,'E'] #criamos as transições para esvaziar a pilha
        transicao.append(estadoFinal)                               # assim que chegamos em EFC

    estados.append(novo_estInicial)
    estados.append(novo_estFinal)
    alfabeto_pilha.append(novoSimbolo_Pilha)

    estadoInicial =  novo_estInicial
    estadosFinais = []
    estadosFinais.append(novo_estFinal)

    estados = str(estados)
    estados = estados.replace(', ', ',')
    estados = estados.replace("'", '')

    alfabeto = str(alfabeto)
    alfabeto = alfabeto.replace(', ', ',')
    alfabeto = alfabeto.replace("'", '')

    alfabeto_pilha = str(alfabeto_pilha)
    alfabeto_pilha = alfabeto_pilha.replace(', ', ',')
    alfabeto_pilha = alfabeto_pilha.replace("'", '')

    transicao = str(transicao)
    transicao = transicao.replace('],', ']')
    transicao = transicao.replace('[[', '[')
    transicao = transicao.replace(']]', ']')
    transicao = transicao.replace(', ', ',')
    transicao = transicao.replace("'", '')

    estadosFinais = str(estadosFinais)
    estadosFinais = estadosFinais.replace(', ', ',')
    estadosFinais = estadosFinais.replace("'", '')

    arquivo = open('APD_PilhaVazia.txt', 'w')
    arquivo.write(estados+'\n')
    arquivo.write(alfabeto+'\n')
    arquivo.write(alfabeto_pilha+'\n')
    arquivo.write(transicao+'\n')
    arquivo.write(estadoInicial+'\n')
    arquivo.write(estadoInicial_pilha+'\n')
    arquivo.write(estadosFinais)
    arquivo.close()

    return 1


#estfinal_para_vazia('teste.txt')
vazia_para_estfinal('APD_PilhaVazia.txt')