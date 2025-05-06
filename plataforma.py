from dataclasses import dataclass, field
from typing import List
import json
import uuid
import statistics


#1.1 




#USUARIO
@dataclass
class Usuario:
    nome: str
    email: str
    senha: str
    tipo_usuario: str
    id_usuario: str

    def saudacao_aluno(self):
        print(f"Olá, {self.nome}! Seja bem-vindo(a) à nossa escola!")

    def exercicio_aluno(self, modulo):
        print(f"Olá, {self.nome}! Você tem um exercício de {modulo} para fazer.")


#CURSO
@dataclass
class Curso:
    nome: str
    descricao: str
    carga_horaria: int
    id_curso: str
    professor: str = None
    alunos: list[Usuario] = None



curso_introducao_informatica = Curso("Introdução à Informática", "Curso básico de informática", 40, "1")
curso_pensamento_logico = Curso("Pensamento Lógico", "Curso de raciocínio lógico", 30, "2")
curso_programacao_python = Curso("Programação em Python", "Curso de programação em Python", 60, "3")
curso_engenharia_dados = Curso("Engenharia de Dados", "Curso de engenharia de dados", 80, "4")

print(curso_introducao_informatica)
print(curso_pensamento_logico)


#MODULO
@dataclass
class Modulo:
    nome: str
    descricao: str
    carga_horaria: int
    id_modulo: str
    curso: Curso = None

modulo_introducao_informatica = Modulo("Introdução à Informática", "Módulo básico de informática", 10, "1")
modulo_pensamento_logico = Modulo("Pensamento Lógico", "Módulo de raciocínio lógico", 10, "2")
modulo_programacao_python = Modulo("Programação em Python", "Módulo de programação em Python", 20, "3")
modulo_engenharia_dados = Modulo("Engenharia de Dados", "Módulo de engenharia de dados", 30, "4")


#AVALIAÇÃO
#Verifica se o aluno aprendeu o conteúdo
@dataclass
class Avaliacao:
    nome: str
    descricao: str
    peso: float
    nota_maxima: float
    id_avaliacao: str
    modulo: Modulo = None
    aluno: Usuario = None

#CERTIFICADO
#certificado de conclusão do curso
@dataclass
class Certificado:
    nome: str
    descricao: str
    carga_horaria: int
    id_certificado: str
    aluno: Usuario = None
    curso: Curso = None

