# 🐾 Projeto VetClinic - Gerenciamento de Clínica Veterinária

Este é o repositório central para o nosso projeto de sistema de gerenciamento de clínica veterinária. Este README serve como nosso guia interno para garantir que todos estejamos alinhados.

**Importante:** Este é um **aplicativo desktop (offline)**. Ele não usa e não precisa de um servidor web (como o Django). Nossa arquitetura é focada em rodar localmente na máquina do usuário.

## 👥 Equipe

* [Lavinia Butinholi] - (@LaviniaButinholiBasilio)
* [Nícolas Barbosa] - (@Nicolas-Granato)
* [Pedro Gomes] - (@MonkeyNails)

---

## 🚀 Stack de Tecnologias

Para manter a consistência, esta é a nossa stack oficial. Todo o desenvolvimento deve usar estas ferramentas:

* **Linguagem:** Python
* **Interface Gráfica (GUI):** PySimpleGUI
* **Banco de Dados Local:** SQLite (um arquivo `clinica.db`)
* **ORM (Acesso ao Banco):** **SQLAlchemy** (para evitar escrever SQL na mão)
* **Controle de Versão:** Git & GitHub
* **Empacotamento (Futuro):** PyInstaller (para criar o `.exe`)

---

## 🛠️ Como Rodar o Projeto Localmente (Setup)

Siga estes passos **exatamente** para configurar o ambiente de desenvolvimento.

### 1. Clonar o Repositório

git clone [https://github.com/Nicolas-Granato/Projeto-ACS.git]
cd [https://github.com/Nicolas-Granato/Projeto-ACS.git]

### 2. Criar e Ativar o Ambiente Virtual (venv)

É obrigatório usar um ambiente virtual para este projeto.

Bash

Cria o ambiente
-> python -m venv venv

Ativa o ambiente
-> .\venv\Scripts\activate
Você saberá que funcionou pois verá (venv) no início do seu terminal.

### 3. Instalar as Dependências

Temos um arquivo que lista tudo que o projeto precisa.
-> (venv) pip install -r requirements.txt
(Nota: Lembrem-se de atualizar o requirements.txt sempre que instalarem um novo pacote! Use: 
-> (venv) pip freeze > requirements.txt)

### 4. Criar o Banco de Dados (Primeira vez)

Nós não damos commit do arquivo do banco (clinica.db). Nós damos commit do código que cria o banco.
Rode este script (que devemos criar) para que o SQLAlchemy crie as tabelas:
-> (venv) python database/database_setup.py
(Este comando só precisa ser rodado uma vez, ou quando mudarmos os models)
