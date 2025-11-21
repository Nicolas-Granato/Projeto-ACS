🐾 Sistema de Gestão Veterinária
Um sistema desktop completo para o gerenciamento de dados clínicos e administrativos de uma clínica veterinária. Focado na integridade dos dados e em uma arquitetura de software limpa e desacoplada.

🎯 Sobre o Projeto
Este projeto resolve o problema de organização de dados em clínicas veterinárias, permitindo o controle total sobre o fluxo de atendimento, desde o cadastro do tutor até o registro histórico de consultas e condições médicas dos pacientes.

A aplicação foi construída separando rigidamente a Regra de Negócio/Persistência da Interface de Usuário, garantindo que o sistema seja robusto e fácil de escalar.

✨ Funcionalidades
Gestão de Entidades: CRUD completo para Tutores, Veterinários, Espécies e Raças.

Prontuário Eletrônico: Cadastro de Pacientes com histórico clínico detalhado.

Controle de Consultas: Agendamento e registro de observações médicas vinculadas a veterinários e pacientes.

Mapeamento de Condições: Registro de condições preexistentes e diagnósticos.

🛠️ Tecnologias e Arquitetura
O projeto foi desenvolvido em Python utilizando o padrão Repository Pattern para a camada de dados.

Linguagem: Python 3.x

ORM: SQLAlchemy (Gerenciamento de sessões e modelos relacionais)

Banco de Dados: SQLite (Leve e serverless, ideal para aplicações desktop locais)

Interface (GUI): Tkinter (Nativo)
