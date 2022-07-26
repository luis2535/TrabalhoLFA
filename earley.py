# Função para receber arquivo txt e captar dados
def abrir_arquivo():
    with open("entrada.txt") as file:
        linhas=[]
        for line in file:
            linhas.append(line)
        # V
        V=[]
        for i in range(3,len(linhas[0])-2):
            if(linhas[0][i] != ','):
                V.append(linhas[0][i])
        # T
        T=[]
        for i in range(3,len(linhas[1])-2):
            if(linhas[1][i] != ','):
                T.append(linhas[1][i])
        # P
        P=[]
        txt = linhas[2][3:-1]
        ps = txt.split(";")
        P = []
        iteracoes = 0
        for i in ps:
            if(iteracoes == len(ps)-1):
                nova = i[6:-3] # para remover um ']' excedente na ultima produão
            else:
                nova=i[6:-2]
            novo_nova = nova.replace("'","").split(",")
            P.append((i[2], novo_nova))
            iteracoes = iteracoes + 1
        # S
        S=linhas[3][2]

    return V,T,P,S
# Função para construção de primeiro conjunto de produções
def primeiro_conjunto(V,P,S):
    D0 = []
    verificador = [S] # Array para verificar se alguma produção ja foi adicionada
    for i in P:
        if(i[0] == S):
            D0.append([i[0],i[1],[0,0]]) # Adiciona a D0 produções de S, ultimo array representa a posição do ponto e em que produção foi adicionada
    for i in D0: 
        if(i[1][0] in V): # Verifica se o valor da posição do ponto é uma variavel         
            if(i[1][0] in verificador): # Verifica se esta no array verificador
                continue
            else:
                verificador.append(i[1][0])
                for j in P:
                    if(j[0] == i[1][0]):
                        D0.append([j[0],j[1],[0,0]])# Adiciona a produção D0
    return D0

# Função para imprimir os conjuntos gerados no seu devido formato
def imprimir_conjunto(conjunto):
    
    for i in conjunto:
        juntaProducao = ''.join(i[1]) # Junta os chars do array em uma str
        producao = juntaProducao[:i[2][0]] + '.' + juntaProducao[i[2][0]:] + '/' + str(i[2][1]) # Adiciona o ponto na posicao correta e em que conjunto foi gerada
        print(f"{i[0]} -> {producao}")

# Função para construção dos demais conjuntos de produção
def outros_conjuntos(palavra, V, D0):
    tamanho_palavra = len(palavra)
    
    D = [[0,D0]] # Todas as produções ficarão salvas em D
    for r in range(1, tamanho_palavra + 1):
        letra_palavra = palavra[r-1] # Letra a ser analisada
        producoes = []
        verificador = [] # Array para verificar se alguma produção ja foi adicionada
        for i in D[r-1][1]: # Verifica produção anterior
            if(i[2][0] < len(i[1])): # Verificação para não acessar index indisponivel
                if(letra_palavra == i[1][i[2][0]]):
                    producoes.append([i[0],i[1],[i[2][0] + 1, i[2][1]]]) # Adiciona se o ponto está na posição do terminal correto
        if producoes != []:
            for i in producoes: # Percorre o array se ele não for nulo
                if(len(i[1]) == i[2][0]): # Verifica se alguma produção chegou ao final
                    for j in D[i[2][1]][1]: # Verifica que conjunto originou essa produção
                            if(j[1][j[2][0]] == i[0]):
                                producoes.append([j[0],j[1],[j[2][0]+1,j[2][1]]]) # Adiciona produção que gerou passando o ponto para direita
                else:
                    if(i[1][i[2][0]] in V): #Verifica se a posição do ponto que a produção está é uma Variavel
                        if(i[1][i[2][0]] in verificador):
                            continue
                        else:
                            verificador.append(i[1][i[2][0]])
                            for j in D0:
                                if(j[0] == i[1][i[2][0]]):
                                    producoes.append([j[0],j[1],[0, r]]) # Adiciona essa produção adicionando o ponto na posição zero e em que conjunto foi gerada
        D.append([r,producoes])
    return D

# Função para identificar se a palavra pertence a gramática com base nos conjuntos
def verifica_palavra(D, palavra, S):
    tamanho_palavra = len(palavra)
    producoes_iniciais = []
    status = 0
    for i in D[0][1]:
        if(i[0] == S):
            producoes_iniciais.append([i[0],i[1],[len(i[1]),0]]) #adiciona ao array producoes_inicias com um ponto na ultima posição
    for i in producoes_iniciais:
        if(i in D[tamanho_palavra][1]): #verifica se no ultimo conjunto existe uma das produções iniciais com um ponto na ultima posição
            juntaProducao = ''.join(i[1])
            producao = juntaProducao[:i[2][0]] + '.' + juntaProducao[i[2][0]:] + '/' + str(i[2][1]) 
            print(f'Palavra verificada com sucesso pois {i[0]} -> {producao} pertence a D{tamanho_palavra}')
            status = 1 #caso palavra tenha sido identificada
    if status == 0: # caso palavra não tenha sido identificada
        print('Palavra nao pertence a gramatica')




        


   
V, T, P, S = abrir_arquivo()
print(f'Variaveis : {V}')
print(f'Terminais : {T}')
print(f'Producoes : {P}')
print(f'Estado Inicial: {S}')
D0 = primeiro_conjunto(V,P,S)
# print(D0)
palavra = input("Digite a palavra a ser analisada:")


print('==========D0==========')
imprimir_conjunto(D0)
print('======================')
D = outros_conjuntos(palavra, V,D0)
for i in range(1, len(palavra)+1):
    print(f'==========D{i}==========')
    imprimir_conjunto(D[i][1])
    print('======================')
status = verifica_palavra(D, palavra, S)
# manipulações com o P
# print(len(P[0][1])) # tamanho da lista associada a E
# print(P[0][1][1]) # acessar elemento da lista associada a E