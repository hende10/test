class Aluno:
    def __init__(self, nome, sexo, idade, matricula):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.matricula = matricula

if __name__ == '__main__':
    aluno1 = Aluno("Hendeson", "M", "16", "123456")
    print(f'Matrícula: {aluno1.matricula} \nNome: {aluno1.nome} \nSexo: {aluno1.sexo} \nIdade: {aluno1.idade}')
