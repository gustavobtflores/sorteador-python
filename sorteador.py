integrantesArq = open("integrantes.txt")
integrantes = integrantesArq.readlines()
integrantesList = []
gruposSorteados = []
grupoAtual = 0
numeroGrupos = 0
grupo = 1

def sortear(lista):
  import random
  sorteado = random.choice(lista)
  lista.remove(sorteado)
  return sorteado

for integrante in integrantes:
  integrantesList.append(integrante.strip())
  numeroGrupos = int(len(integrantesList) / 5)

for i in range(0, numeroGrupos):
  gruposSorteados.append([])

while len(integrantesList) >= 1:
  if(grupoAtual == numeroGrupos):
    grupoAtual = 0

  gruposSorteados[grupoAtual].append(sortear(integrantesList))
  grupoAtual += 1

for integrante in gruposSorteados:
  print(f'GRUPO {grupo}', end="\n\n")
  for i in integrante:
    print(i)
  grupo += 1
  print('\n')


