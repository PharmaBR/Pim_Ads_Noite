# README.md - Sistema de Gerenciamento Educacional

## Sobre o Projeto

Este é um sistema educacional desenvolvido em Python que permite o gerenciamento de alunos, cursos, módulos e avaliações. O projeto foi criado como parte da disciplina PIM (Projeto Integrado Multidisciplinar) do curso de Análise e Desenvolvimento de Sistemas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- classes.py - Implementação da classe básica de Usuário
- final_project.py - Sistema de estatísticas e gerenciamento de dados dos usuários
- data - Diretório que armazena os arquivos JSON com dados persistentes
- usuarios.json - Arquivo de armazenamento dos dados dos usuários

## Funcionalidades

- Cadastro e gerenciamento de usuários (alunos e professores)
- Estruturação de cursos e módulos
- Sistema de mensagens e notificações para alunos
- Acompanhamento de progresso nos cursos
- Análise estatística dos dados (idade média, moda, mediana)
- Armazenamento persistente em arquivos JSON

## Requisitos

- Python 3.7 ou superior
- Biblioteca padrão do Python (sem dependências externas)

## Como Executar

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/PIM-ADS-Noite.git
```

2. Navegue até o diretório do projeto:
```
cd PIM-ADS-Noite
```

3. Execute o arquivo principal:
```
python final_project.py
```

## Exemplo de Uso

```python
# Criando um usuário
from classes import Usuario

novo_aluno = Usuario("Maria Silva", "maria@email.com", "senha123", "aluno")
novo_aluno.saudacao_aluno()  # Exibe mensagem de boas-vindas
novo_aluno.exercicio_aluno("Python")  # Notifica sobre exercícios
```

## Estrutura de Dados

O sistema utiliza dataclasses para representar as entidades:

- `Usuario` - Armazena informações de alunos e professores
- `Estatistica` - Processa dados estatísticos dos usuários

## Contribuição

Para contribuir com o projeto:

1. Crie um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b minha-nova-feature`)
3. Faça commit das suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Envie para o branch (`git push origin minha-nova-feature`)
5. Abra um Pull Request

## Autores

- [Seu Nome] - Desenvolvedor principal
- [Nome dos Colaboradores] - Contribuições

## Licença

Este projeto está licenciado sob [inserir licença aqui] - veja o arquivo LICENSE para detalhes.
