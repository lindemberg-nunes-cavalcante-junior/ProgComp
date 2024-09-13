import random,os

def Cartelas(quantia: int):
    if not isinstance(quantia,int):
        raise Exception('Informe um valor inteiro..')
    elif quantia <= 0:
        raise Exception('Informe um valor que seja maior que 0...')
    dictCartelas = {}
    while quantia > 0:
        serial = str(random.randint(0, 100000))
        serial = (6-len(serial))*'0' + serial
        if serial not in dictCartelas:
            cartela = {'CART_'+serial:{
                'B':sorted(random.sample(range(1,15),5)),
                'I':sorted(random.sample(range(1,15),5)),
                'N':sorted(random.sample(range(1,15),5)),
                'G':sorted(random.sample(range(1,15),5)),
                'O':sorted(random.sample(range(1,15),5))}}
            duplicada = 0
            for x in dictCartelas:
                if dictCartelas[x] == cartela:
                    duplicada += 1
            if duplicada < 1:
                dictCartelas.update(cartela)
                quantia -= 1
    return(True,dictCartelas)

def SalvarC(Cartelas: dict):
    if not isinstance(Cartelas, dict) or len(Cartelas)<1:
        raise Exception('Não é um dicionário ou o dicionário é pequeno demais...')
    dirArquivos = os.path.abspath(__file__)
    dirArquivos = os.path.dirname(dirArquivos)
    Salvarcartelas = open(dirArquivos + '\\cartelas.txt','w', encoding='utf-8')
    for x in Cartelas:
        Salvarcartelas.write(f"{x};B;{Cartelas[x]['B']};I;{Cartelas[x]['I']};N;{Cartelas[x]['N']};G;{Cartelas[x]['G']};O;{Cartelas[x]['O']};\n")
    return(True,"Arquivo salvo com sucesso!")

def Ler():
    dirname = os.path.abspath(__file__)
    dirname = os.path.dirname(dirname)
    try:
        CartelasL = open(dirname + '\\cartelas.txt','r',encoding='utf-8')
    except ValueError:
        raise Exception(False,'Arquivo Inexistente...')
    dict = {}
    while True:
        linha = CartelasL.readline()
        if linha[-1:] ==' \n': linha = linha[:-1]
        if not linha: break
        cartela = linha.replace('[','').replace(']','')
        cartela = cartela.split(';')
        for i in range(2,11,2):
            cartela[i] = cartela[i].split(',')
        cartela = {cartela[0]:{cartela[1]:cartela[2],
        cartela[3]:cartela[4],
        cartela[5]:cartela[6],
        cartela[7]:cartela[8],
        cartela[9]:cartela[10]
        }}
        dict.update(cartela)
    return(True,dict)

def Imprimir(ID:str):
    cartelas = Ler()[1]
    if not isinstance(cartelas,dict):
        raise Exception('\ERROR: Cartelas não existe...')
    if not isinstance(ID,str):
        raise Exception('\ERROR: cartela não encontrada, valor inválido')
    
    if len(ID)>6:
        if 'CART_' in ID and ID in cartelas:
            return(True,cartelas[ID])
    elif len(ID)<=6:
        ID = 'CART_' + (6 - len(ID))*'0' + ID
        if ID in cartelas:
            ID = ID
            return(True,cartelas[ID])
    return(False,'ID inválido...')
