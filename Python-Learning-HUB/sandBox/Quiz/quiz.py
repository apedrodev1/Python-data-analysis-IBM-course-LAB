print('Mensagem de boas vindas')
answerUser = input ('Deseja começar? (S/N)')

if answerUser != 'S':
    quit()

score = 0

print ('Comecando...')

print ('Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Actvision \n (D) EA \n')
answer_1 = input('Resposta: ')

if answer_1 == 'A': 
    print ('Parabéns!!! Você acertou!')
    score = score + 1
else:
    print ('Que pena! Você errou...')

print ('Qual o nome do protagonista em GTA SAn Andreas?\n (A) Carlos John \n (B) Carl Johnson \n (C) Cassius Joe  \n (D) Carlos Jay \n')
answer_2 = input('Resposta: ')
if answer_2 == 'B': 
    print ('Parabéns!!! Você acertou!')
    score = score + 1
else:
    print ('Que pena! Você errou...')

print(f'O Quiz acabou... Pontuação: {score}'/2)
       