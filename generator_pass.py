import tkinter as tk
import pyperclip
import random

alfabeto_minusculo = [chr(i) for i in range(97, 123)]
alfabeto_maiusculo = [chr(i) for i in range(65, 91)]
numeros = list(range(1, 11))
caracteres_especiais = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
alfabeto_completo = alfabeto_maiusculo + alfabeto_minusculo

def processar_numero():
    try:
        numero = int(entrada.get())
        senha = []
        for i in range(0, numero+1):
            x = random.choice(alfabeto_completo + numeros + caracteres_especiais)
            senha.append(str(x))

        senha = ",".join(senha).replace(",", "")

        return resultado_label.config(text=f"{senha}")
        # Faça o que você desejar com o número aqui
        
    except ValueError:
        resultado_label.config(text="Erro: Digite um número inteiro válido!")


def copiar_senha():
    senha = resultado_label.cget("text")
    if senha:
        pyperclip.copy(senha)

# Criação da janela principal
janela = tk.Tk()
janela.title("Interface para Número Inteiro")

# Criação dos elementos da interface
instrucao_label = tk.Label(janela, text="Digite quantidade de caracteres para sua senha: ")
instrucao_label.pack()

entrada = tk.Entry(janela)
entrada.pack()

botao = tk.Button(janela, text="Processar", command=processar_numero)
botao.pack()

copiar_botao = tk.Button(janela, text="Copiar", command=copiar_senha)
copiar_botao.pack()

resultado_label = tk.Label(janela, text="")
resultado_label.pack()

# Loop principal da interface
janela.mainloop()
