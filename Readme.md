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

```bash
git clone [https://github.com/Nicolas-Granato/Projeto-ACS.git]
cd [https://github.com/Nicolas-Granato/Projeto-ACS.git]
