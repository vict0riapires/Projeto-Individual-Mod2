candidato1 = [8,9,5,10]
candidato2 = [7,6,7,8]
candidato3 = [8,5,6,7]
candidato4 =[9,10,10,8]
candidato5 = [7,8,9,7]
candidatos = [candidato1,candidato2,candidato3,candidato5]
notaCandidatoIdeal =  []
candidatosAptos = []
dicionario = {'cand1' : 'MARIO LOPES\n20 ANOS\nTELEFONE: (21)97658-3543\nE-MAIL: mariolopesrj@gmail.com\n','cand2' : 'JOÃO PEDRO\n28 ANOS\nTELEFONE: (21)97468-7353\nE-MAIL: jpdasilva@hotmail.com\n','cand3' : 'ANA BEATRIZ\n23 ANOS\nTELEFONE: (21)98265-3765\nE-MAIL: anab00@gmail.com\n','cand4' : 'MARIA LUIZA\n20 ANOS\nTELEFONE: (21)8746-4356\nE-MAIL: marialuiza02@yahoo.com\n','cand5' : 'EDUARDA FERNANDES\n25 ANOS\nTELEFONE: (21)99652-0010\nE-MAIL: dudafrj@yahoo.com\n'}
def candidatoIdeal():
    eX = int(input("\nEscolha o conceito da entrevista: "))
    tX = int(input("Escolha o conceito do teste teórico: "))
    pX = int(input("Escolha o conceito das habilidades práticas: "))
    sX = int(input("Escreva o conceito da avaliação de Soft Skills: "))
    notaCandidatoIdeal.append(eX)
    notaCandidatoIdeal.append(tX)
    notaCandidatoIdeal.append(pX)
    notaCandidatoIdeal.append(sX)
    print(f"\nVocê está buscando um candidato com as notas:\n\neX: {notaCandidatoIdeal[0]}\ntX: {notaCandidatoIdeal[1]}\npX: {notaCandidatoIdeal[2]}\nsX: {notaCandidatoIdeal[3]}\nou maior.")
def buscandoCandidato():
    for i in candidatos:
        if (i >= notaCandidatoIdeal):
            candidatosAptos.append(i)

def candidatoFinal():
    candidatoIdeal()
    buscandoCandidato()
    print("\n\nCANDIDATOS\n\n")
    if candidato1 in candidatosAptos:
        print(dicionario['cand1'])
    if candidato2 in candidatosAptos:
        print(dicionario['cand2'])
    if candidato3 in candidatosAptos:
        print(dicionario['cand3'])
    if candidato4 in candidatosAptos:
        print(dicionario['cand4'])
    if candidato5 in candidatosAptos:
        print(dicionario['cand5'])
    if (candidato1 not in candidatosAptos) and (candidato2 not in candidatosAptos) and (candidato3 not in candidatosAptos) and (candidato4 not in candidatosAptos) and (candidato5 not in candidatosAptos):
        print("\nInfelizmente, não há nenhum candidato apto para a vaga.\n")

candidatoFinal()

loop = input('\nDeseja tentar novamente?\n')
while loop == 'SIM':
    notaCandidatoIdeal =  []
    candidatosAptos = []
    candidatoFinal()
    loop = input('\nDeseja tentar novamente?\n')
else:
    print('\nObrigada por utilizar o nosso sistema!')

