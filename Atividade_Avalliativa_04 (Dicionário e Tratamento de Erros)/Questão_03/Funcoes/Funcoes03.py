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

def SalvarC(Cartelas:dict):
    print(len(Cartelas))
    if not isinstance(Cartelas, dict) or len(Cartelas)<1:
        raise Exception('ERROR: Dicionário inválido, pequeno demais ou não existe')
    dirarquivos = os.path.abspath(__file__)
    dirarquivos = os.path.dirname(dirarquivos)
