# Sistema de Gerenciamento de Notas (CRUD)

Este projeto consiste em uma aplicação desktop desenvolvida em **Python** utilizando o framework **Tkinter** para a interface gráfica e o **SQLite** para persistência de dados. O sistema foi criado como parte do trabalho prático da disciplina de *Desenvolvimento Rápido de Aplicações em Python (RAD)*.

## 📋 Funcionalidades
O sistema permite realizar as quatro operações básicas (CRUD) para o gerenciamento de alunos:
- **Create (Adicionar):** Cadastro de alunos com Nome, Matrícula e 4 notas bimestrais.
- **Read (Listar):** Visualização automática de todos os registros em uma tabela (Treeview).
- **Update (Atualizar):** Edição dos dados de alunos já cadastrados.
- **Delete (Excluir):** Remoção de registros do banco de dados.
- **Cálculo Automático:** O sistema calcula a média final das 4 notas do aluno de forma automática.
- **Tratamento de Erros:** O sistema valida entradas para garantir que apenas valores numéricos (0 a 10) sejam aceitos nas notas.

## 🛠 Tecnologias Utilizadas
- **Linguagem:** Python 3
- **Interface Gráfica:** Tkinter (`ttk`)
- **Banco de Dados:** SQLite
- **Gerenciamento de Código:** Git e GitHub

## 🚀 Como Executar

1. **Pré-requisitos:**
   Certifique-se de ter o Python instalado em sua máquina.

2. **Clonando o repositório:**
   ```bash
   git clone [https://github.com/maurocollin/sistema-notas-crud.git](https://github.com/maurocollin/sistema-notas-crud.git)
   cd sistema-notas-crud
