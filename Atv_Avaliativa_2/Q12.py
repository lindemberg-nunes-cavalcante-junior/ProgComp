'''
12. (Valor: 25 pontos) A cifra de Vigenère é um método de criptografia por substituição, onde cada letra da 
mensagem original é substituída por outra letra de acordo com uma chave pré-definida. Essa chave é 
repetida ao longo da mensagem até que tenha o mesmo tamanho da mensagem (veja a definição 
detalhada em https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re).
Implemente um programa que realize a criptografia e descriptografia de mensagens usando a cifra de 
Vigenère.
Para implementar essa cifra, seu programa deverá:
a) Receber uma mensagem e uma chave como entrada.
b) Realizar a criptografia da mensagem usando a cifra de Vigenère.
c) Realizar a descriptografia da mensagem criptografada usando a mesma chave.
d) Imprimir a mensagem criptografada e descriptografada.
Lembre-se de que sua implementação deve lidar corretamente com letras maiúsculas e minúsculas, e 
deve considerar apenas as letras do alfabeto (ignorando espaços, pontuação, etc).
'''

palavra = input('Digite sua palavra:')
chave = input('Digite a chave:')

alfabeto = 'abcdefghijklmnopqrstuvwxyz' # alfabeto utilizado pra percorre cada coluna 
linha = ''

criptografada = ''
i = 0

while len(chave) != len(palavra): # deixando do memso tamanho da palavra que vai ser criptada
    chave = chave + chave[i]
    i += 1

for i in range(len(palavra)): # Cifra de Viginére
    contador = alfabeto.find(chave[i].lower()) # colunas formadas a partir do embaralhamento do alfabeto de acordo com a Cifra
    linha = alfabeto[contador:len(alfabeto)]
    linha += alfabeto[0:contador]

    coluna = alfabeto.find(palavra[i].lower()) 
    criptografada += linha[coluna] # pegando a letra correspondente a posição dela na tabela de Viginére
print(f'Sua palavra é {palavra}e sua forma criptografada é {criptografada}')


    


        


