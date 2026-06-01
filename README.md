# 📊 Sistema de Gerenciamento de Notas (CRUD)

> ### 🏫 Entrega de Projeto Universitário
> * **Curso:** Análise e Desenvolvimento de Sistemas (ADS) 
> * **Aluno:** Mauro Henrique Collin Ferreira
> * **Matrícula:** 202403689601
> * **Disciplina:** Desenvolvimento Rápido de Aplicações em Python (RAD)
> * **Professor:** Ralfh V Ansuattigui

---

Este projeto consiste em uma aplicação desktop completa com uma interface gráfica nativa voltada para a gestão escolar. O sistema implementa o padrão **CRUD** (Create, Read, Update, Delete), possibilitando o controle de alunos, suas respectivas notas e o cálculo automatizado de médias acadêmicas.

---

## Análise Técnica: SQLite vs PostgreSQL
Conforme os requisitos da atividade, optou-se pela utilização do **SQLite** por ser embutido, portátil e mais leve.

### Ganhos:
* **Portabilidade:** A base de dados é um ficheiro único (`notas.db`), permitindo a execução imediata sem a necessidade de configurar um servidor externo como o PostgreSQL.
* **Agilidade no Desenvolvimento:** Ideal para prototipagem rápida e aplicações de pequeno porte.

### Perdas:
* **Escalabilidade:** O SQLite não suporta múltiplos acessos simultâneos de escrita tão eficientemente quanto o PostgreSQL.
* **Segurança:** Ausência de um sistema robusto de gestão de utilizadores e permissões a nível de motor de base de dados.


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
* **Gerenciamento de Código:** Git e GitHub

---

## 🚀 Como executar o Projeto

1. **Clonando o repositório:**

   ```bash
   git clone https://github.com/maurocollin/sistema-notas-crud.git
   cd sistema-notas-crud
   ```

2. **Criar o Ambiente Virtual:**

* **No Windows (PowerShell / Prompt de Comando):**

   ```bash
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  .venv\Scripts\activate.bat
   ```
* **No Linux / macOS:**

   ```bash
  python3 -m venv .venv
  source .venv/bin/activate
   ```

3. **Finalmente execute o programa:**

```bash
  python3 app_notas.py
```

---

## ⚙️ Arquitetura e Diferenciais do Projeto (Destaque para a Avaliação)

* **Persistência de Dados Robusta:** O banco de dados SQLite garante a integridade dos dados, mantendo todas as notas salvas com segurança mesmo após fechar o aplicativo.
* **Interface Responsiva e Alinhada:** Uso inteligente de gerenciadores de layout (`grid`, `columnspan` e `sticky`) para corrigir o alinhamento das entradas de texto, aproximando os campos das notas bimestrais aos seus respectivos rótulos e otimizando o espaço da tela.
* **Componente Orientado a Eventos:** Uso de *bindings* (`<<TreeviewSelect>>`) para detectar cliques do mouse na tabela e carregar os dados dinamicamente nos campos de texto, elevando a experiência do usuário (UX).
