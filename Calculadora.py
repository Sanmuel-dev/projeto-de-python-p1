from tkinter import * #importa funcionalidades da biblioteca tkinter, para criar interfaces de usuário gráficas

main = Tk()
main.title("Calculadora")

operacao = "" 
valor_input = StringVar()
texto_display = Entry(main, font=("arial", 15, "bold"), textvariable=valor_input, bd=30, insertwidth=4, 
                     bg="powder blue", justify=RIGHT)  #Define como a janela e o input dentro dela irão aparecer
texto_display.grid(columnspan=4) #faz com que uma coluna ocupe o espaço de 4 colunas

# fila 1 (7 8 9 +)

botao_7 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="7") #define a aparência do botão
botao_7.grid(row=1, column=0) #define a localização do botão

botao_8 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="8")
botao_8.grid(row=1, column=1)

botao_9 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="9")
botao_9.grid(row=1, column=2)

botao_adicao = Button(main, padx=16, bd=8, fg="black",
                 font=("arial", 15, "bold"), text="+")
botao_adicao.grid(row=1, column=3)

# fila 2  (4 5 6 -)

botao_4 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="4")
botao_4.grid(row=2, column=0)

botao_5 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="5")
botao_5.grid(row=2, column=1)

botao_6 = Button(main, padx=16, bd=8, fg="black",
               font=("arial", 15, "bold"), text="6")
botao_6.grid(row=2, column=2)

botao_subtrair = Button(main, padx=16, bd=8, fg="black",
                 font=("arial", 15, "bold"), text="-")
botao_subtrair.grid(row=2, column=3)


main.mainloop()
