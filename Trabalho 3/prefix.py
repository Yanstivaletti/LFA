def normalizeExp(str1, opcodes):
    sai = ""
    for elem in str1:
        if elem in opcodes or elem == '(' or elem == ')':
            sai = sai + elem
        elif sai != "":
            aux = sai[-1]
            if aux in opcodes or aux == '(' or aux == ')':
                sai = sai + elem
            else:
                sai = sai + '.'
                sai = sai + elem
        else:
            sai = sai+elem
    return sai



def resolveOp(pilha,elem,opcodes,popped):
    if popped == '(' or ')': 
        pilha.append(popped) 
        pilha.append(elem) 
    elif opcodes.index(elem) >= opcodes.index(popped): 
        pilha.append(popped) 
        pilha.append(elem) 

def resolveLessOp(pilha,elem,opcodes,output):
    if pilha: 
        for op in pilha:
            if op != '(' and op != ')' and opcodes.index(elem) < opcodes.index(op):
                popped = pilha.pop() 
                output.append(popped) 
            else:
                popped = pilha.pop() 
                resolveOp(pilha,elem,opcodes,popped)
                break
    if not pilha:
        pilha.append(elem)

def convert(ex):
    opcodes = ['+','.','*']

    lista = normalizeExp(ex[::-1],opcodes)

    saida = [] #output stack
    pilha = [] #op stack

    for elem in lista: 
        if elem in opcodes: 
            if pilha: 
                popped = pilha.pop() 
                if popped in opcodes and opcodes.index(elem) < opcodes.index(popped): 
                    saida.append(popped)
                    resolveLessOp(pilha,elem,opcodes,popped) 
                else:
                    resolveOp(pilha,elem,opcodes,popped) 
            else:
                pilha.append(elem) 
        elif elem == ')': 
           pilha.append(elem) 
        elif elem == '(':
            popped = pilha.pop() 
            saida.append(popped)
            while popped != ')':
                popped = pilha.pop()
               saida.append(popped)
            saida.pop()
        else: 
            saida.append(elem)

    while pilha: 
        elem = pilha.pop()
        saida.append(elem)

    saida.reverse() 
    str1 = "".join(str(x) for x in saida)
    return str1   

