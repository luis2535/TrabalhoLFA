from black import out


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

def primeiro_conjunto(V,T,P,S):
    D0 = []
    verificador = [S]
    status = 1
    for i in P:
        if(i[0] == S):
            D0.append([i[0],i[1],[0,0]])
    for i in D0:
        if(i[1][0] in V):         
            if(i[1][0] in verificador):
                continue
            else:
                verificador.append(i[1][0])
                for j in P:
                    if(j[0] == i[1][0]):
                        D0.append([j[0],j[1],[0,0]])
    return D0

def imprimir_conjunto(conjunto):
    
    for i in conjunto:
        juntaProducao = ''.join(i[1])
        producao = juntaProducao[:i[2][0]] + '.' + juntaProducao[i[2][0]:] + '/' + str(i[2][1])
        print(f"{i[0]} -> {producao}")

def outros_conjuntos(palavra, V, T, P, S, D0):
    tamanho_palavra = len(palavra)
    
    D = [[0,D0]]
    for r in range(1, tamanho_palavra + 1):
        letra_palavra = palavra[r-1]
        producoes = []
        verificador = []
        
        for i in D[r-1][1]:
            if(i[2][0] < len(i[1])):
                if(i[1][i[2][0]] == letra_palavra):
                    producoes.append([i[0], i[1], [i[2][0] + 1, i[2][1]]])
        for j in producoes:
            if (j[2][0] == len(j[1])):
                for i in D[j[2][1]][1]:
                    if(i[1][i[2][0]] == j[0]):
                        producoes.append([i[0], i[1], [i[2][0]+1, i[2][1]]])
            else:
                if(j[1][j[2][0]] in V):
                    verificador.append(j[1][j[2][0]])
                    for i in D[r-1][1]:
                        if(j[1][j[2][0]] == i[0]):
                            producoes.append([i[0], i[1], [0,r]])
        D.append([r, producoes])
        print(1)
    print('==========D1==========')
    imprimir_conjunto(D[1][1])
    print('======================')
    print('==========D2==========')
    imprimir_conjunto(D[2][1])
    print('======================')
    print('==========D3==========')
    imprimir_conjunto(D[3][1])
    print('======================')
                            


        


   
V, T, P, S = abrir_arquivo()
print(f'Variaveis : {V}')
print(f'Terminais : {T}')
print(f'Producoes : {P}')
print(f'Estado Inicial: {S}')
D0 = primeiro_conjunto(V,T,P,S)
# print(D0)
# palavra = input("Digite a palavra a ser analisada:")
palavra = 'x+x'
print('==========D0==========')
imprimir_conjunto(D0)
print('======================')
outros_conjuntos(palavra, V,T,P,S,D0)

# manipulações com o P
# print(len(P[0][1])) # tamanho da lista associada a E
# print(P[0][1][1]) # acessar elemento da lista associada a E