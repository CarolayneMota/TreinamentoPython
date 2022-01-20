# importação da lib tkinter
from tkinter import *

# Classe que é a tela
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 5
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["pady"] = 5
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["pady"] = 5
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="CALCULADORA")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
        
        self.lbl_num1 = Label(self.primeiroContainer, text="Número 1: ")
        self.lbl_num1["font"] = ("Arial", "10", "bold")
        self.lbl_num1.pack()
        
        self.lbl_num2 = Label(self.segundoContainer, text="Número 2: ")
        self.lbl_num2["font"] = ("Arial", "10", "bold")
        self.lbl_num2.pack()
        
        # Entry é o mesmo q input
        self.nome = Entry(self.primeiroContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.btn_soma = Button(self.terceiroContainer)
        self.btn_soma["text"] = "Calcular"
        self.btn_soma["font"] = ("Calibri", "8")
        self.btn_soma["width"] = 12
        self.btn_soma["command"] = self.soma
        self.btn_soma.pack()

        self.lbl_resultado = Label(self.quartoContainer, text="")
        self.lbl_resultado["font"] = ("Arial", "10", "bold")
        self.lbl_resultado.pack()


    
    def soma(self):
        num1 = float(self.lbl_num1.get())
        num2 = float(self.lbl_num2.get())
        soma = num1 + num2
        self.lbl_resultado["text"] = f"{num1} + {num2} == {soma}"
        


# Criando um objeto do tipo TK()
root = Tk()
# Passando o root para minha classe
Application(root)
# Event Loop: verifica constantemente se outro evento foi acionado 
root.mainloop() # exibe a GUI