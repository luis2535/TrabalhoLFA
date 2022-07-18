def abrirArquivo():
    arq = open('gramatica.txt', 'r')
    linhas = arq.readlines()
    linha1 = linhas[0]
    comecoLinha1 = linha1.find('(')
    linha1 = linha1[comecoLinha1 + 1:].replace(' ', '').split(';')
    linha2 = linhas[1]
    comecoLinha2 = linha2.find('{')
    linha2 = linha2[comecoLinha2 + 1:len(linha2)-1].replace(' ','').split(';')
    variaveis = []
    for i in linha1[0]:
        if(ord(i) >= 65 and ord(i)<=90):
            variaveis.append(i)
    terminais = []
    inicioTerminal = linha1[1].find('{') + 1
    for i in linha1[1][inicioTerminal:]:
        if(i != ','):
            terminais.append(i)
    terminais.pop(len(terminais)-1)
    estadoInicial = []
    for i in linha1[3]:
        if(ord(i) >= 65 and ord(i) <= 90):
            estadoInicial.append(i)
            break
    producoes = {}
    for i in range(len(variaveis)):
        inicioProducoes = linha2[i].find('>')
        produtos = linha2[i][inicioProducoes + 1:].split('|')
        producoes[variaveis[i]] = produtos
    
    return variaveis, terminais, estadoInicial, producoes

def primeiroConjunto(producoes, variaveis):
    arrayProducoes = {}
    for i in variaveis:
        novaProducao = []
        for j in range(len(producoes[i])):
            novaProducao.append('.'+producoes[i][j]+'/0')
        arrayProducoes[i] = novaProducao
    return arrayProducoes




variaveis, terminais, estadoInicial, producoes = abrirArquivo()
print(f'Variaveis {variaveis}')
print(f'Terminais: {terminais}')
print(f'Estado Inicial: {estadoInicial}')
print(f'Producoes: {producoes}')

conjunto = primeiroConjunto(producoes, variaveis)

print(conjunto)
# print(producoes)