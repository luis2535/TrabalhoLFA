d0 = [1,2,3]

for i in d0:
    if(i == 1):
        d0.append(4)
    print(i)



#    for r in range(1, tamanho_palavra + 1):
#         letra_palavra = palavra[r-1]
#         producoes = []
#         verificador = []
        
        
#         for i in D[r-1][1]:
#             if(i[2][0] < len(i[1])):
#                 if(i[1][i[2][0]] == letra_palavra):
#                     producoes.append([i[0], i[1], [i[2][0] + 1, i[2][1]]])
#         for j in producoes:
#             if (j[2][0] == len(j[1])):
#                 for i in D[j[2][1]][1]:
#                     if(i[1][i[2][0]] == j[0]):
#                         producoes.append([i[0], i[1], [i[2][0]+1, i[2][1]]])
#             else:
#                 if(j[1][j[2][0]] in V):
#                     verificador.append(j[1][j[2][0]])
#                     for i in D[r-1][1]:
#                         if(j[1][j[2][0]] == i[0]):
#                             producoes.append([i[0], i[1], [0,r]])
#         D.append([r, producoes])