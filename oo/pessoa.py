class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
        
    def cumprimentar(self):
        return f"Ola meu nome eh {self.nome}"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def atributos_classe(cls):
        return cls, cls.olhos

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f"Opa, baum? {cumprimentar_da_classe}"

class Mutante(Pessoa):
    olhos = 3


if __name__ == "__main__":
    Cassiano = Homem(nome="Cassiano", idade="26")
    Lucinda = Pessoa(Cassiano, nome="Lucinda")
    Ketlin = Mutante(nome="Ketlin", idade="22")
    print(Lucinda.cumprimentar())
    print(Cassiano.cumprimentar())
    for filho in Lucinda.filhos:
        print(filho.nome)
    Cassiano.dinamico = "possui"
    del Cassiano.filhos
    print(Cassiano.__dict__)
    print(Cassiano.metodo_estatico())
    print(Pessoa.atributos_classe())
    print(isinstance(Cassiano, Homem))
    print(Ketlin.olhos)