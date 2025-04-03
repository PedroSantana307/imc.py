# interface.py

import tkinter as tk
from tkinter import messagebox
from imcc import calcularimc, classificarimc  


def calcular():
    try:
        peso = float(entry_peso.get())  
        altura = float(entry_altura.get())  
        
        if peso <= 0 or altura <= 0:
            messagebox.showerror("Erro", "Peso e altura devem ser valores positivos.")
            return
        
        imc = calcularimc(peso, altura)  
        classificacao = classificarimc(imc) 
        
       
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")


janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("920x350")


janela.config(bg="black")


label_peso = tk.Label(janela, text="Peso (kg):", fg="white", bg="black")
label_peso.pack(pady=10)

entry_peso = tk.Entry(janela)
entry_peso.pack(pady=5)

label_altura = tk.Label(janela, text="Altura (m):", fg="white", bg="black")
label_altura.pack(pady=10)

entry_altura = tk.Entry(janela)
entry_altura.pack(pady=5)


botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular, bg="red", fg="white")
botao_calcular.pack(pady=20)


label_resultado = tk.Label(janela, text="", font=("Arial", 12), fg="white", bg="black")
label_resultado.pack(pady=10)


janela.mainloop()
