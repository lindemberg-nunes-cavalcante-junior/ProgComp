'''
10. (Valor: 15 pontos) Faça um programa que simule o jogo da forca. O programa terá uma constante 
chamada PALAVRA_CHAVE que armazenara a palavra a ser descoberta (o programador deverá atribuir 
uma string ao eu critério para essa constante). O programa deverá solicitar ao usuário as letras e à medida 
que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou não. O jogo deverá 
considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de ser enforcado.
'''

PALAVRA_CHAVE = 'Charles'
palavra = '_______'
erros = ''
acertos = ''

while True:
    print(palavra)
    resposta = input('Digite uma letra pra descobrir a palavra secreta:').lower()
    
    
    if resposta is not acertos:
        for i in range(len(PALAVRA_CHAVE)):
            if PALAVRA_CHAVE[i].lower() == resposta:
                palavra = palavra.replace(palavra[i], PALAVRA_CHAVE[i], 1)
                print(palavra)