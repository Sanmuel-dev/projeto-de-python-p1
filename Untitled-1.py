num_1 = float(input("digite um numero: "))
num_2 = float(input("digite um numero: "))
operacao = input("Qual a operação desejada?: (soma, mutiplicação, subtração, divisão: ")

if operacao == "soma":
    soma = num_1 + num_2
    print ("A soma das variaveis é: ", soma)

elif operacao == "mutiplicação":
    mutiplicacao = num_1 * num_2
    print ("A mutiplição das variaveis é: ", mutiplicacao)

elif operacao == "subtração":
    subtracao = num_1 - num_2
    print ("A subtração das variaveis é: ", subtracao)

elif operacao == "divisão":
    if num_1 == 0 or num_2 == 0:
        print ("Erro: não é possível dividir por 0")
    else:
        divisao = num_1 / num_2
        print ("A divisão das variaveis é: ", divisao)

else:
    print ("escolha uma operação existente.")

print ("fim do programa")