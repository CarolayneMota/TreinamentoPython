"""

"""
# importação da lib tkinter
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack ()

        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair" 
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5 # largura do botão
        self.sair["command"] = self.widget1.quit # toda vez q clicar acontecer algo 
        self.sair.pack ()

        self.cadastrar = Button(self.widget1)
        self.cadastrar["text"] = "Cadastrar" 
        self.cadastrar["font"] = ("Calibri", "10")
        self.cadastrar["width"] = 10 # largura do botão
        self.cadastrar["command"] = self.cadastrar # toda vez q clicar acontecer algo 
        self.cadastrar.pack ()

        self.resultado = Label(self.widget1, text="")
        self.resultado["font"] = ("Verdana", "10", "italic", "bold")
        self.resultado.pack ()

    
    def cadastrar(self):
        self.resultado['text'] = "Cadastro realizado"


root = Tk()
Application(root)
root.mainloop()