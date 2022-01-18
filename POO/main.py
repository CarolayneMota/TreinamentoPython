"""
Classe: entidade/projeto/planta/entidade/blueprint que gera os objetos
Objeto: gerado pela classe. Tem atributos e métodos.
Atributos:característica do objeto (cor, altura, nome,cpf, rg)
Método:ações que pode ser realizadas pelo objeto(andar(), comer())

class Animal:
    # Atributos com valores padrão
    nome = "Animal"
    idade = 0

objeto_gato = Animal()
objeto_gato.nome = "Gato"
objeto_gato.idade = 5

objeto_dog = Animal()
objeto_dog.nome = "Cachorro"
objeto_dog.idade = 10
class Animal:
    
    def __init__(self, nome="Animal", idade=0):
        # Atributos com valores padrão
        self.nome = nome
        self.idade = idade
    def __str__(self): #para imprimir automaticamente
        return f"Animal com nome {self.nome} e idade {self.idade}"

# objeto_gato = Animal("Gato", 5)
# objeto_dog = Animal("Cachorro", 10)

nome = input("Digite o nome do animal: ")
idade = input("Digite a idade do animal: ")
objeto_animal = Animal(nome, idade)
#print(f'Animal com nome {objeto_animal.nome} e idade {objeto_animal.idade}')
print(objeto_animal)

1 - 
class Pessoa():
    def __init__(self, cpf, nome, idade, cidade, genero):
        self.cpf = cpf
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.genero = genero


    def __str__(self):
        return f'CPF: {self.cpf}, nome: {self.nome}, idade: {self.idade}, cidade: {self.idade}, genero: {self.genero}'
    

    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}')
    

    def estudar(self, materia):
        print(f'{self.nome} está estudanto {materia}')
    

    def dormir(self):
        print(f'{self.nome} está dormindo')
    

    def jogar(self):
        print(f'{self.nome} está jogando')


pessoa = Pessoa(123,'Carol', 20, 'Gameleira', 'F')
pessoa.comer('Pizza')
pessoa.estudar('Python')
pessoa.dormir()
pessoa.jogar()
print(pessoa)


Executaveu: https://pypi.org/project/auto-py-to-exe/ 
"""
