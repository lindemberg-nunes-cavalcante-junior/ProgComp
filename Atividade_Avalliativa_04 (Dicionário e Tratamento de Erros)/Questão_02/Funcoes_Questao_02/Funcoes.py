def Esquema(Lista:list,jogadores:dict):
    Zagueiros = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Zagueiro']
    Laterais = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Lateral']
    Meias = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Meia']
    Atacantes = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Atacante']
    Tecnicos = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Técnico']
    Goleiros = [jogadores[i][i] for i in jogadores.keys() if jogadores[i][i]['Posicao'] == 'Goleiro']
    tecnico = [i for i in Tecnicos if i['Pontuacao'] == max(x['Pontuacao'] for x in Tecnicos)][0]
    goleiro = [i for i in Goleiros if i['Pontuacao'] == max(x['Pontuacao'] for x in Goleiros)][0]

    if Lista[0] == '4':
        Zagueiro = []
        for  _ in range(1,3):
            x = [i for i in Zagueiros if i['Pontuacao'] == max(x['Pontuacao'] for x in Zagueiros)]
            if x[0] not in Zagueiro:
                Zagueiro.append(x[0])
                Zagueiros.remove(x[0])
        Lateral = []
        for  _ in range(1,3):
            x = [i for i in Laterais if i['Pontuacao'] == max(x['Pontuacao'] for x in Laterais)]
            if x[0] not in Lateral:
                Lateral.append(x[0])
                Laterais.remove(x[0])
    elif Lista[0] == '5':
        Zagueiro = []
        for  _ in range(1,4):
            x = [i for i in Zagueiros if i['Pontuacao'] == max(x['Pontuacao'] for x in Zagueiros)]
            if x[0] not in Zagueiro:
                Zagueiro.append(x[0])
                Zagueiros.remove(x[0])
        Lateral = []
        for  _ in range(1,3):
            x = [i for i in Laterais if i['Pontuacao'] == max(x['Pontuacao'] for x in Laterais)]
            if x[0] not in Lateral:
                Lateral.append(x[0])
                Laterais.remove(x[0])
    else:
        Zagueiro = []
        for  _ in range(1,4):
            x = [i for i in Zagueiros if i['Pontuacao'] == max(x['Pontuacao'] for x in Zagueiros)]
            if x[0] not in Zagueiro:
                Zagueiro.append(x[0])
                Zagueiros.remove(x[0])
        Lateral = 0

    Meia = []
    for  _ in range(1,int(Lista[1])):
        x = [i for i in Meias if i['Pontuacao'] == max(x['Pontuacao'] for x in Meias)]
        if x[0] not in Meia:
            Meia.append(x[0])
            Meias.remove(x[0])
    Atacante = []
    for  _ in range(1,int(Lista[2])):
        x = [i for i in Atacantes if i['Pontuacao'] == max(x['Pontuacao'] for x in Atacantes)]
        if x[0] not in Atacante:
            Atacante.append(x[0])
            Atacantes.remove(x[0])
    esquema = {'Esquema':{'Tecnico': tecnico, 'Goleiro': goleiro,'Zagueiros':Zagueiro, 'Laterais': Lateral, 'Meias':Meia, 'Atacantes':Atacante}}

    return esquema