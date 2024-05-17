#Loop para que o CPF seja de 9 digitos apenas
nome = input('Digite seu nome: ')
while True:
    cpf = input('Digite seu CPF (apenas 9 dígitos): ')
    if len(cpf) == 9 and cpf.isdigit():
        break 
    else:
        print("CPF inválido. Por favor, digite exatamente 9 dígitos numéricos.")

#Para saber qual o seu estado
def mapear_regiao(regiao):
    regioes = {
        1: 'DF, GO, MS, MT ou TO',
        2: 'AC, AM, AP, PA, RO ou RR',
        3: 'CE, MA ou PI',
        4: 'AL, PB, PE ou RN',
        5: 'SE ou BA',
        6: 'MG',
        7: 'ES ou RJ',
        8: 'SP',
        9: 'PR ou SC',
        0: 'RS'
    }
    return regioes.get(regiao, 'RS')


regiao = int(cpf[8])
mensagem_regiao = mapear_regiao(regiao)
print(f'Nasceu em {mensagem_regiao}')

#Descobrindo o penúltimo dígito do CPF
primeiro_valor = (cpf[0:9])
fatores = [10, 9, 8, 7, 6, 5, 4, 3, 2] 
soma_multiplicacao = 0

for i in range(len(primeiro_valor)): #i é números do cpf
    multiplicacao = int(primeiro_valor[i]) * fatores[i]
    soma_multiplicacao = soma_multiplicacao + multiplicacao
   

resto = soma_multiplicacao % 11
penultimo_digito = 11 - resto
if resto == 0 or resto == 1:
    penultimo_digito = 0
    print('O seu penúltimo digito é: 0')
else:
    print(f'O penúltimo digito do seu CPF é: {penultimo_digito} ')

#Descobrindo o último dígito do CPF
segundo_valor = cpf + str(penultimo_digito)
valores = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

soma_segunda_multiplicacao = 0

for j in range(len(segundo_valor)):
    segunda_multiplicacao = int(segundo_valor[j]) * valores[j]
    soma_segunda_multiplicacao = soma_segunda_multiplicacao + segunda_multiplicacao

resto2 = soma_segunda_multiplicacao % 11

ultimo_digito = 11 - resto2
if resto2 == 0 or resto2 == 1:
    ultimo_digito = 0
    print('O seu último digito é: 0')
else:
    print(f'O último digito do seu CPF é: {ultimo_digito}')

print('-'*50)

print(f'Olá {nome}, você se registrou {mensagem_regiao} e seu CPF completo é: {cpf}{penultimo_digito}{ultimo_digito} ')
