from pathlib import Path
import json
from dataclasses import dataclass, asdict, field
from typing import List
import statistics

# Diretório de dados (usando uma pasta local no projeto)
DATA_DIR = Path(__file__).parent / "data"
# Ou use uma pasta na home do usuário:
# DATA_DIR = Path.home() / "Documents" / "pim_ads_console"
DATA_DIR.mkdir(exist_ok=True, parents=True)  # Cria diretórios pai se necessário

# Caminhos para arquivos
USERS_FILE = DATA_DIR / "usuarios.json"

# Definições de dataclasses
@dataclass
class Usuario:
    id: str
    nome: str
    idade: int
    email: str
    senha: str
    cursos_concluidos: List[str] = field(default_factory=list)

@dataclass
class Estatistica:
    usuarios: List[Usuario]

    def idade_media(self):
        return statistics.mean([u.idade for u in self.usuarios])

    def idade_moda(self):
        return statistics.mode([u.idade for u in self.usuarios])

    def idade_mediana(self):
        return statistics.median([u.idade for u in self.usuarios])

# Funções utilitárias
def salvar_usuarios(lista_usuarios: List[Usuario]):
    with USERS_FILE.open("w", encoding="utf-8") as f:
        json.dump([asdict(u) for u in lista_usuarios], f, indent=2)

def carregar_usuarios() -> List[Usuario]:
    if not USERS_FILE.exists():
        return []
    with USERS_FILE.open("r", encoding="utf-8") as f:
        dados = json.load(f)
    return [Usuario(**u) for u in dados]

# Criando usuários fictícios
usuarios_demo = [
    Usuario(id="1", nome="Ana", idade=18, email="ana@email.com", senha="1234"),
    Usuario(id="2", nome="João", idade=20, email="joao@email.com", senha="abcd"),
    Usuario(id="3", nome="Clara", idade=18, email="clara@email.com", senha="4321")
]

# Salvando e gerando estatísticas
salvar_usuarios(usuarios_demo)
estat = Estatistica(usuarios_demo)

# Print the statistics
resultado = {
    "media": estat.idade_media(),
    "moda": estat.idade_moda(),
    "mediana": estat.idade_mediana(),
    "arquivo": str(USERS_FILE)
}

print("Estatísticas de idade:")
print(f"Média: {resultado['media']}")
print(f"Moda: {resultado['moda']}")
print(f"Mediana: {resultado['mediana']}")
print(f"Arquivo salvo em: {resultado['arquivo']}")
