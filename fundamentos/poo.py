class Usuario:

    # Constructor
    def __init__(self, nome, cpf, idade, nivel, dinheiro):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.nivel = nivel
        self.dinheiro = dinheiro

    def updateDinheiro(self, dinheiro):
        self.dinheiro = dinheiro

aron = Usuario("Aron Felippe Kerkoven", "070.802.749-07", 24, 1, 4000)
rebeca = Usuario("Rebeca Cristina Kerkhoven", "070.802.759-69", 27, 2, 16000)

print(aron.nome)
print(rebeca.idade)