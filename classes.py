from dataclasses import dataclass


@dataclass
class Usuario:
    nome: str
    email: str
    senha: str
    tipo_usuario: str

    def saudacao_aluno(self):
        print(f"Olá, {self.nome}! Seja bem-vindo(a) à nossa escola!")

    def exercicio_aluno(self, modulo):
        print(f"Olá, {self.nome}! Você tem um exercício de {modulo} para fazer.")


aluno_breno = Usuario("Breno Abreu", "brenoabreu@brenoabreu.com", "123456", "aluno")
aluno_deisson = Usuario("Deisson", "deisson@deisson.com.br", "123456", "aluno")

