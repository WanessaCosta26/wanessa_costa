import random
from time import sleep
print('''\033[4;35mVamos jogar Jokenpô!!!
\033[35m[1] PEDRA
[2] PAPEL
[3] TESOURA\033[m''')
option = int(input('\033[34mQual sua opção ? \033[m'))
print('\033[33mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!\033[m')
sleep(0.5)
variaveis = 'PEDRA', 'PAPEL', 'TESOURA'
pc = random.choice(variaveis)
print(f'\033[36mPC escolheu {pc}!!!\033[m')
if option == 1 and pc == 'PEDRA':
    print('\033[31mEMPATE!!! Tente novamente\033[m')
elif option == 1 and pc == 'PAPEL':
    print('\033[32mPapel cobre a pedra , PC GANHOU!!!\033[m')
elif option == 1 and pc == 'TESOURA':
    print('\033[32mPedra quebra tesoura , VOCÊ GANHOU!!!\033[m')
elif option == 2 and pc == 'PAPEL':
    print('\033[31mEMPATE!!! Tente novamente\033[m')
elif option == 2 and pc == 'PEDRA':
    print('\033[32mPapel cobre a pedra , VOCÊ GANHOU!!!\033[m')
elif option == 2 and pc == 'TESOURA':
    print('\033[32mTesoura corta o papel , PC GANHOU!!!\033[m')
elif option == 3 and pc == 'TESOURA':
    print('\033[31mEMPATE!!! Tente novamente\033[m')
elif option == 3 and pc == 'PEDRA':
    print('\033[32mPedra quebra a tesoura , PC GANHOU!!!\033[m')
elif option == 3 and pc == 'PAPEL':
    print('\033[32mTesoura corta o papel , VOCÊ GANHOU!!!\033[m')
else :
    print('\033[31mSua opção é inválida.\033[m')
