from tkinter import * #importa funcionalidades da biblioteca tkinter, para criar interfaces de usuário gráficas

def BotaoFuncional(numero): 
    global operacao
    operacao = operacao + str(numero)
    valor_input.set(operacao) # adiciona a função de mostrar os valores na tela

def BotaoDeLimpeza():
    global operacao
    operacao = ""
    valor_input.set(operacao) # adiciona função de  apagar os valores ao botão de limpeza C

def BotaoDeIgualdade():
    global operacao
    try:
        resultado = str(eval(operacao))
        valor_input.set(resultado)
    except (ZeroDivisionError):
        valor_input.set(0)
    except (SyntaxError):
        valor_input.set("Erro, limpe o Display")
        operacao = "" # adicona função de efetuar os calculos ao botao de igualdade =


main = Tk()
main.title("Calculadora")

operacao = "" 
valor_input = StringVar()
texto_display = Entry(main, font=("arial", 15, "bold"), textvariable=valor_input, bd=30, insertwidth=4, 
                     bg="powder blue", justify=RIGHT)  #Define como a janela e o input dentro dela irão aparecer
texto_display.grid(columnspan=4) #faz com que uma coluna ocupe o espaço de 4 colunas

# fila 1 (7 8 9 +)

botao_7 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="7",command=lambda: BotaoFuncional(7)) #define a aparência do botão e adiciona funcionalidade
botao_7.grid(row=1, column=0) #define a localização do botão

botao_8 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="8",command=lambda: BotaoFuncional(8))
botao_8.grid(row=1, column=1)

botao_9 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="9",command=lambda: BotaoFuncional(9))
botao_9.grid(row=1, column=2)

botao_adicao = Button(main, padx=16, bd=8, fg="black", bg="yellow",
                 font=("arial", 15, "bold"), text="+",command=lambda: BotaoFuncional("+"))
botao_adicao.grid(row=1, column=3)

# fila 2  (4 5 6 -)

botao_4 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="4",command=lambda: BotaoFuncional(4))
botao_4.grid(row=2, column=0)

botao_5 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="5",command=lambda: BotaoFuncional(5))
botao_5.grid(row=2, column=1)

botao_6 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="6",command=lambda: BotaoFuncional(6))
botao_6.grid(row=2, column=2)

botao_subtrair = Button(main, padx=16, bd=8, fg="black", bg="yellow",
                 font=("arial", 15, "bold"), text="-",command=lambda: BotaoFuncional("-"))
botao_subtrair.grid(row=2, column=3)

# Fila 3 (1 2 3 *)

botao_1 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="1",command=lambda: BotaoFuncional(1))
botao_1.grid(row=3, column=0)

botao_2 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="2",command=lambda: BotaoFuncional(2))
botao_2.grid(row=3, column=1)

botao_3 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="3",command=lambda: BotaoFuncional(3))
botao_3.grid(row=3, column=2)

botao_multiplicar = Button(main, padx=16, bd=8, fg="black", bg="yellow",
               font=("arial", 15, "bold"), text="×",command=lambda: BotaoFuncional("*"))
botao_multiplicar.grid(row=3, column=3)

# Fila 4 (0 C = /)

botao_0 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="0",command=lambda: BotaoFuncional(0))
botao_0.grid(row=4, column=0)

botao_limpar = Button(main, padx=16, bd=8, fg="black", bg="cyan",
               font=("arial", 15, "bold"), text="C",command=BotaoDeLimpeza)
botao_limpar.grid(row=4, column=1)

botao_igual = Button(main, padx=16, bd=8, fg="black", bg="cyan",
               font=("arial", 15, "bold"), text="=",command=BotaoDeIgualdade)
botao_igual.grid(row=4, column=2)

botao_dividir = Button(main, padx=16, bd=8, fg="black", bg="yellow",
               font=("arial", 15, "bold"), text="÷",command=lambda: BotaoFuncional("/"))
botao_dividir.grid(row=4, column=3)

main.mainloop()