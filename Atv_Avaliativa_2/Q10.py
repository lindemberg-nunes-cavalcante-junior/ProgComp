'''
10. (Valor: 15 pontos) Faça um programa que simule o jogo da forca. O programa terá uma constante 
chamada PALAVRA_CHAVE que armazenara a palavra a ser descoberta (o programador deverá atribuir 
uma string ao eu critério para essa constante). O programa deverá solicitar ao usuário as letras e à medida 
que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou não. O jogo deverá 
considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de ser enforcado.

(Não consegui completamente)
'''

PALAVRA_CHAVE = 'Lucas'
aux = PALAVRA_CHAVE.lower()

erros = 0
acertos = 0
acertados = ''
errados = ''

while True:
    print(f'Essas são as letras certas: {acertados}')
    print(f'Essas são as letras erradas: {errados}')
    resposta = input('Digite uma letra pra descobrir a palavra secreta:').lower()
    
    
    if aux.find(resposta):
        acertos += 1
        print('Você acertou uma palavra, continue até descobri.')
        acertados += resposta
    else:
        print('você errou uma letra, continue tentando.')
        errados += resposta
        erros += 1
        '''elif acertados.find(resposta):
            print('essa letra já foi, tente outra')'''

    if acertos == len(PALAVRA_CHAVE):
        print(f'Você ganhou, a palavra era {PALAVRA_CHAVE}') 
        break
    elif erros == 6:
        print('Desculpe, mas você perdeu')
        break

    