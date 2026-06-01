# 📊 Sistema de Gerenciamento de Notas (CRUD)

> ### 🏫 Entrega de Projeto Universitário
> * **Aluno:** Mauro Henrique Collin Ferreira
> * **Matrícula:** [Inserir seu número de matrícula aqui]
> * **Disciplina:** Desenvolvimento Rápido de Aplicações em Python (RAD)
> * **Professor:** [Inserir nome do professor aqui]
> * **Grupo:** GRUPO 4

---

Este projeto consiste em uma aplicação desktop completa com uma interface gráfica nativa voltada para a gestão escolar. O sistema implementa o padrão **CRUD** (Create, Read, Update, Delete), possibilitando o controle de alunos, suas respectivas notas e o cálculo automatizado de médias acadêmicas.

---

## 📋 Funcionalidades do Aplicativo

O sistema opera de forma reativa e centraliza todas as operações essenciais em uma única tela de fácil navegação:

* **Adicionar (Create):** Permite registrar um novo aluno inserindo Nome, Matrícula (chave única) e as quatro notas bimestrais.
* **Listar (Read):** Exibe de forma instantânea todos os alunos cadastrados em uma tabela organizada (`Treeview`).
* **Atualizar (Update):** Ao selecionar qualquer aluno na tabela com um clique, seus dados preenchem o formulário automaticamente para que alterações sejam salvas no banco de dados.
* **Excluir (Delete):** Remove de forma definitiva o registro do aluno selecionado do banco de dados.
* **Cálculo Automático da Média:** O sistema elimina a necessidade de cálculo manual, processando a média aritmética das quatro notas no exato momento do cadastro ou edição.
* **Tratamento de Exceções e Validação:** Possui regras de negócio para impedir notas menores que `0` ou maiores que `10`, além de barrar duplicidade no número de matrícula.

---

## 🛠 Tecnologias Utilizadas

Para garantir leveza, estabilidade e compatibilidade imediata em qualquer computador (sem necessidade de baixar pacotes visuais externos), o ecossistema do projeto foi construído utilizando:

* **Python 3:** Linguagem de programação principal.
* **Tkinter (`ttk`):** Biblioteca nativa do Python para criação de componentes visuais modernos e limpos.
* **SQLite3:** Banco de dados relacional embutido de altíssima performance, que dispensa configurações complexas ou servidores externos.

---

## 🚀 Como Executar o Projeto Localmente

Como o projeto utiliza apenas as ferramentas nativas do próprio Python, o processo para rodar a aplicação é extremamente simples e direto:

### 1. Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina. Você pode verificar digitando no seu terminal ou prompt de comando:
```bash
python --version

---

## ⚙️ Arquitetura e Diferenciais do Projeto (Destaque para a Avaliação)

Persistência de Dados Robusta: O banco de dados SQLite garante a integridade dos dados, mantendo todas as notas salvas com segurança mesmo após fechar o aplicativo.

Interface Responsiva e Alinhada: Uso inteligente de gerenciadores de layout (grid, columnspan e sticky) para corrigir o alinhamento das entradas de texto, aproximando os campos das notas bimestrais aos seus respectivos rótulos e otimizando o espaço da tela.

Componente Orientado a Eventos: Uso de bindings (<<TreeviewSelect>>) para detectar cliques do mouse na tabela e carregar os dados dinamicamente nos campos de texto, elevando a experiência do usuário (UX).














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
   git clone https://github.com/maurocollin/sistema-notas-crud.git
   cd sistema-notas-crud
