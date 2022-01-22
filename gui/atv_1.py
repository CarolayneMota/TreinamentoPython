from tkinter import *

# Classe que é a tela
class Tela:
    
    def __init__(self, master=None):
        self.container1 = Frame(master)
        self.container1["pady"] = 5
        self.container1.pack()

        self.titulo = Label(self.container1, text="LOGIN DO SISTEMA")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2["padx"] = 10
        self.container2.pack()

        self.nomeLabel = Label(self.container2,text="Usuário: ")
        self.nomeLabel["font"] = ("Arial", "10", "bold")
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.container2)
        self.nome["width"] = 30
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome.pack(side=LEFT)

        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3["padx"] = 10
        self.container3.pack()

        self.senhaLabel = Label(self.container3, text="Senha: ")
        self.senhaLabel["font"] = ("Arial", "10", "bold")
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.container3)
        self.senha["width"] = 30
        self.senha["font"] = ("Arial", "10", "bold")
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.widget1 = Frame(master)
        self.widget1.pack()

        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"  #nome no botão
        self.sair["font"] = ("Arial", "10", "bold")
        self.sair["width"] = 5 # largura do botão
        self.sair["command"] = self.widget1.quit # Quando clicar vai sair 
        self.sair.pack(side=LEFT) # para deixar o botão da senha ao lado do botão do login

        self.container4 = Frame(master)
        self.container4["pady"] = 5
        self.container4.pack()
        
        self.autenticar = Button(self.widget1)
        self.autenticar["text"] = "Login" #nome no botão
        self.autenticar["font"] = ("Arial", "10", "bold")
        self.autenticar["width"] = 5 # largura do botão
        self.autenticar["command"] = self.verificaSenha # Chama a função para verificar se a senha é igual ao login
        self.autenticar.pack(side=LEFT) # para deixar o botão da senha ao lado do botão do login

        # para aparecer a mensagem se o usuario é bem vindo ou inválido
        self.mensagem = Label(self.container4, text="")
        self.mensagem["font"] = ("Arial", "10", "bold")
        self.mensagem.pack()

    
    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario != senha :
            self.mensagem["text"] = "Bem-vind@ ao sistema!"
        else:
            self.mensagem["text"] = "Usuário inválido"

        




# Criando um objeto do tipo TK()
root = Tk()
# Passando o root para minha classe
Tela(root)
# Event Loop: verifica constantemente se outro evento foi acionado 
root.mainloop() # exibe a GUI