# 🐾 Sistema de Gestão Veterinária

> **⚠️ MVP (Minimum Viable Product):** Este projeto encontra-se em sua versão inicial de validação. As funcionalidades essenciais estão implementadas, mas a interface, relatórios avançados e integrações externas serão desenvolvidas em iterações futuras.

---

## 🎯 Sobre o Projeto

Um sistema **desktop** completo para gerenciamento de dados clínicos e administrativos de uma clínica veterinária. Focado na integridade dos dados e em uma arquitetura de software limpa e desacoplada.

Este projeto resolve o problema de organização de dados em clínicas veterinárias, permitindo o controle total sobre o fluxo de atendimento — desde o cadastro do tutor até o registro histórico de consultas e condições médicas dos pacientes.

A aplicação foi construída separando rigidamente a **Regra de Negócio / Persistência** da **Interface de Usuário**, garantindo que o sistema seja robusto e fácil de escalar.

---

## ✨ Funcionalidades (MVP)

- **Gestão de Entidades:** CRUD completo para Tutores, Veterinários, Espécies e Raças
- **Prontuário Eletrônico:** Cadastro de Pacientes com histórico clínico detalhado
- **Controle de Consultas:** Agendamento e registro de observações médicas vinculadas a veterinários e pacientes
- **Mapeamento de Condições:** Registro de condições preexistentes e diagnósticos
- **Autenticação:** Sistema de login com hash bcrypt e níveis de acesso (Padrão, Veterinário, Admin)

---

## 🛠️ Tecnologias e Stack

| Camada | Tecnologia |
|---|---|
| Linguagem | Python 3.x |
| Interface Gráfica | **CustomTkinter** (moderna, com suporte a temas dark/light) |
| ORM | SQLAlchemy 2.x |
| Banco de Dados | SQLite (serverless, ideal para desktop) |
| Autenticação | bcrypt |
| Padrão de Projeto | Repository Pattern |

> **Por que CustomTkinter?** O CustomTkinter substitui o Tkinter padrão oferecendo widgets modernos com suporte nativo a tema escuro/claro, cantos arredondados e aparência contemporânea — sem dependências externas pesadas, mantendo a leveza ideal para aplicações desktop locais.

---

## 🏗️ Arquitetura do Sistema

O projeto segue uma arquitetura em camadas bem definida, onde cada nível tem responsabilidades claras e não se comunica diretamente com camadas não adjacentes.

```
┌─────────────────────────────────────────────────────────────┐
│                     CAMADA DE APRESENTAÇÃO                  │
│                    (CustomTkinter / GUI)                     │
│   Telas, Formulários, Janelas, Widgets, Navegação           │
└────────────────────────────┬────────────────────────────────┘
                             │ chama
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     CAMADA DE SERVIÇOS                      │
│                  (services/ — Regras de Negócio)            │
│   Autenticação (auth.py), Validações, Orquestração          │
└────────────────────────────┬────────────────────────────────┘
                             │ usa
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                     CAMADA DE DADOS                         │
│               (database/ — Repository Pattern)              │
│   CRUDs (cruds.py), Modelos ORM (models.py)                 │
└────────────────────────────┬────────────────────────────────┘
                             │ persiste em
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                       BANCO DE DADOS                        │
│                      SQLite (clinica.db)                    │
└─────────────────────────────────────────────────────────────┘
```

### Detalhamento das Camadas

**1. Camada de Apresentação (`ui/`)**
Responsável exclusivamente pela exibição e captura de dados do usuário. Construída com **CustomTkinter**, não contém nenhuma lógica de negócio — apenas chama os serviços e exibe os resultados.

**2. Camada de Serviços (`services/`)**
Onde vivem as regras de negócio. Recebe os dados da UI, valida, orquestra chamadas aos repositórios e retorna resultados tratados. Exemplo atual: `auth.py` para autenticação.

**3. Camada de Dados (`database/`)**
Implementa o **Repository Pattern** via classes CRUD. Cada entidade tem seu próprio repositório, isolando completamente o acesso ao banco. O `database.py` gerencia a engine SQLAlchemy e o contexto de sessão.

**4. Banco de Dados**
SQLite local (`clinica.db`). Leve, sem servidor, ideal para aplicações desktop. Foreign Keys são ativadas via PRAGMA para garantir integridade referencial.

---

## 🗄️ Modelagem do Banco de Dados

O banco é composto por **8 tabelas** inter-relacionadas, cobrindo todas as entidades do domínio veterinário:

```
USUÁRIOS E ACESSO
─────────────────
tabela_usuarios
  idUsuario (PK)
  nomeDoUsuario
  nomeDeUsuario   ← unique
  senhaUsuario    ← bcrypt hash
  nivelDeAcesso   ← enum: usuarioPadrao | veterinario | admin
        │
        │ 1:1
        ▼
tabela_veterinario
  idVeterinario (PK)
  idUsuario (FK) ← CASCADE DELETE
  CRM            ← unique
        │
        │ 1:N
        ▼
tabela_consultas ◄─────────────── tabela_paciente
  idConsulta (PK)                   idPaciente (PK)
  idPaciente (FK) ─ RESTRICT        nomePaciente
  idVeterinario (FK) ─ RESTRICT     peso / porte / sexo
  Data                              dataDeNascimento
  Observacoes                       Raca (FK) ─ RESTRICT
                                    Tutor (FK) ─ RESTRICT
                                         │              │
                                         │              │
                              tabela_raca         tabela_tutor
                               idRaca (PK)         idTutor (PK)
                               NomeRaca            NomeTutor
                               Especie (FK)        EnderecoTutor
                                    │              CidadeTutor
                                    │              Telefone
                           tabela_especie
                            idEspecie (PK)
                            NomeEspecie

CONDIÇÕES CLÍNICAS
──────────────────
tabela_de_registros_de_condicoes
  idCondicao (PK)
  NomeCondicao
  Descricao
        │
        │ N:N via
        ▼
tabela_de_registro_de_condicao_do_paciente
  idRegistro (PK)
  idPaciente (FK) ─ CASCADE DELETE
  idCondicao (FK) ─ RESTRICT
  Observacoes
```

### Políticas de Integridade Referencial

| Relacionamento | Política | Motivo |
|---|---|---|
| Usuário → Veterinário | `CASCADE DELETE` | Ao remover usuário, remove o perfil vet |
| Paciente → Condições | `CASCADE DELETE` | Registros do paciente são removidos junto |
| Raça → Paciente | `RESTRICT` | Não remove raça com pacientes vinculados |
| Tutor → Paciente | `RESTRICT` | Não remove tutor com pacientes vinculados |
| Veterinário → Consulta | `RESTRICT` | Histórico de consultas é preservado |
| Paciente → Consulta | `RESTRICT` | Consultas não são órfãs |

---

## 📁 Estrutura de Arquivos

```
sistema-veterinario/
│
├── main.py                  ← Ponto de entrada da aplicação
├── setup_database.py        ← Script de inicialização do banco
├── requirements.txt
│
├── database/
│   ├── __init__.py
│   ├── database.py          ← Engine, sessão, contexto get_db()
│   ├── models.py            ← Modelos ORM (SQLAlchemy)
│   └── cruds.py             ← Repositórios (Repository Pattern)
│
├── services/
│   └── auth.py              ← Serviço de autenticação (bcrypt)
│
└── ui/                      ← (a ser implementado — CustomTkinter)
    ├── app.py
    ├── views/
    └── components/
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# 1. Clone o repositório
git clone <url-do-repositorio>
cd sistema-veterinario

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate          # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Instale o CustomTkinter
pip install customtkinter

# 5. Inicialize o banco de dados
python setup_database.py

# 6. Execute a aplicação
python main.py
```

---

## 🔐 Níveis de Acesso

| Nível | Permissões |
|---|---|
| `usuarioPadrao` | Visualização de dados básicos |
| `veterinario` | CRUD de pacientes, consultas e condições |
| `admin` | Acesso total, incluindo gestão de usuários |

---

## 🗺️ Roadmap (Pós-MVP)

- [ ] Interface gráfica completa com CustomTkinter
- [ ] Tela de login com validação visual
- [ ] Dashboard com estatísticas da clínica
- [ ] Emissão de prontuários em PDF
- [ ] Sistema de agendamento com calendário
- [ ] Backup automático do banco de dados
- [ ] Relatórios gerenciais exportáveis

---

## 📝 Observações sobre o MVP

Este é um **Produto Mínimo Viável (MVP)**. O foco desta versão foi:

1. **Modelar corretamente o domínio** — todas as entidades e seus relacionamentos estão definidos
2. **Garantir a integridade dos dados** — FK constraints, hash de senhas, rollback em erros
3. **Estabelecer a arquitetura** — separação clara entre camadas para facilitar evolução
4. **Validar o backend** — toda a lógica de persistência está funcional e testável

A interface gráfica com **CustomTkinter** será desenvolvida na próxima iteração, aproveitando a base sólida construída neste MVP.
