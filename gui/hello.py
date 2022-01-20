"""
# Etapas padrão do tkinter (cria a tela basica, a casca)

# importação da lib tkinter
from tkinter import *

# Classe que é a tela
class Tela:
    # Receber a master root do TK
    def __init__(self, master=None):
        # Criação de um container
        self.container1 = Frame(master)
        # Registro do container1
        self.container1.pack()
        # Criar um widget e add ao container1
        self.msg = Label(self.container1, text="Bem-vinda!")
        # Registro do widget
        self.msg.pack ()
         # Criar um widget e add ao container1
        self.msg2 = Label(self.container1, text="Informe seus dados")
        # Registro do widget
        self.msg2.pack ()
# Criando um objeto do tipo TK()
root = Tk()
# Passando o root para minha classe
Tela(root)
# Event Loop: verifica constantemente se outro evento foi acionado 
root.mainloop() # exibe a GUI

"""

# Etapas padrão do tkinter (cria a tela basica, a casca)

# importação da lib tkinter
from tkinter import *

# Classe que é a tela
class Tela:
    # Receber a master root do TK
    def __init__(self, master=None):
        # Criação de um container
        self.container1 = Frame(master)
        # Registro do container1
        self.container1.pack()
        # Criar um widget e add ao container1
        self.msg = Label(self.container1, text="Bem-vinda!")
        # Registro do widget
        self.msg.pack ()
         # Criar um widget e add ao container1
        self.msg2 = Label(self.container1, text="Informe seus dados")
        # Registro do widget
        self.msg2.pack ()
# Criando um objeto do tipo TK()
root = Tk()
# Passando o root para minha classe
Tela(root)
# Event Loop: verifica constantemente se outro evento foi acionado 
root.mainloop() # exibe a GUI
