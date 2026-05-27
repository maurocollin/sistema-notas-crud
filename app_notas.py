import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# 1. CAMADA DE PERSISTÊNCIA (BANCO DE DADOS)
# ==========================================
def inicializar_banco():
    conexao = sqlite3.connect("notas.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            matricula TEXT NOT NULL UNIQUE,
            n1 REAL, n2 REAL, n3 REAL, n4 REAL,
            media REAL
        )
    """)
    conexao.commit()
    conexao.close()

# ===============================
# 2. CAMADA DE INTERFACE E LÓGICA 
# ===============================
class AppCadastroNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Notas - CRUD - GRUPO 4")
        self.root.geometry("800x550")
        self.id_selecionado = None

        # --- FRAME DE ENTRADA ---
        frame_form = ttk.LabelFrame(root, text=" Dados do Aluno ", padding=10)
        frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Nome
        ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
        self.txt_nome = ttk.Entry(frame_form, width=40)
        self.txt_nome.grid(row=0, column=1, columnspan=3, pady=5)
        # Matrícula
        ttk.Label(frame_form, text="Matrícula:").grid(row=1, column=0, sticky="w")
        self.txt_matricula = ttk.Entry(frame_form, width=15)
        self.txt_matricula.grid(row=1, column=1, sticky="w", pady=5)
        # 1º Bimestre
        ttk.Label(frame_form, text="1º Bimestre:").grid(row=2, column=0, sticky="w")
        self.txt_n1 = ttk.Entry(frame_form, width=15)
        self.txt_n1.grid(row=2, column=1, padx=5)
        # 2º Bimestre
        ttk.Label(frame_form, text="2º Bimestre:").grid(row=2, column=2, sticky="w")
        self.txt_n2 = ttk.Entry(frame_form, width=15)
        self.txt_n2.grid(row=2, column=3, padx=5)
        # 3º Bimestre
        ttk.Label(frame_form, text="3º Bimestre:").grid(row=2, column=4, sticky="w")
        self.txt_n3 = ttk.Entry(frame_form, width=15)
        self.txt_n3.grid(row=2, column=5, padx=5)
        # 4º Bimestre
        ttk.Label(frame_form, text="4º Bimestre:").grid(row=2, column=6, sticky="w")
        self.txt_n4 = ttk.Entry(frame_form, width=15)
        self.txt_n4.grid(row=2, column=7, padx=5)

        # --- BOTÕES ---
        frame_btn = ttk.Frame(root)
        frame_btn.grid(row=1, column=0, pady=10)
        ttk.Button(frame_btn, text="Adicionar", command=self.inserir).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btn, text="Atualizar", command=self.atualizar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_btn, text="Excluir", command=self.excluir).grid(row=0, column=2, padx=5)
        ttk.Button(frame_btn, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)

        # --- TREEVIEW ---
        # self.tabela = ttk.Treeview(root, columns=("id", "nome", "mat", "n1", "n2", "n3", "n4", "media"), show="headings")
        # for col in ("id", "nome", "mat", "n1", "n2", "n3", "n4", "media"):
        #     self.tabela.heading(col, text=col.upper())
        #     self.tabela.column(col, width=60 if col != "nome" else 200)
        # self.tabela.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        # Definindo cabeçalhos individualmente
        # --- TREEVIEW ---
        colunas = ("id", "nome", "mat", "n1", "n2", "n3", "n4", "media")
        self.tabela = ttk.Treeview(root, columns=colunas, show="headings")
        self.tabela.heading("id", text="ID")
        self.tabela.heading("nome", text="NOME")
        self.tabela.heading("mat", text="MATRÍCULA")
        self.tabela.heading("n1", text="1º BIM")
        self.tabela.heading("n2", text="2º BIM")
        self.tabela.heading("n3", text="3º BIM")
        self.tabela.heading("n4", text="4º BIM")
        self.tabela.heading("media", text="MÉDIA")

        # Definindo larguras individualmente
        self.tabela.column("id", width=30)
        self.tabela.column("nome", width=200)
        self.tabela.column("mat", width=80)
        self.tabela.column("n1", width=60)
        self.tabela.column("n2", width=60)
        self.tabela.column("n3", width=60)
        self.tabela.column("n4", width=60)
        self.tabela.column("media", width=60)

        self.tabela.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        self.tabela.bind("<<TreeviewSelect>>", self.carregar_selecionado)

        root.columnconfigure(0, weight=1)
        self.listar()

    def processar_notas(self):
        """Valida e calcula a média das 4 notas."""
        try:
            notas = [float(getattr(self, f'txt_n{i}').get()) for i in range(1, 5)]
            if any(n < 0 or n > 10 for n in notas):
                raise ValueError
            return notas, sum(notas)/4
        except ValueError:
            messagebox.showerror("Erro", "Insira notas válidas (0 a 10)!")
            return None, None

    def inserir(self):
        notas, media = self.processar_notas()
        if not notas: return
        
        try:
            conn = sqlite3.connect("notas.db")
            conn.execute("INSERT INTO alunos (nome, matricula, n1, n2, n3, n4, media) VALUES (?,?,?,?,?,?,?)",
                         (self.txt_nome.get(), self.txt_matricula.get(), *notas, media))
            conn.commit()
            conn.close()
            self.limpar_campos()
            self.listar()
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Matrícula já existe.")

    def listar(self):
        for i in self.tabela.get_children(): self.tabela.delete(i)
        conn = sqlite3.connect("notas.db")
        for row in conn.execute("SELECT * FROM alunos"):
            self.tabela.insert("", "end", values=row)
        conn.close()

    # def carregar_selecionado(self, event):
    #     sel = self.tabela.selection()
    #     if not sel: return
    #     val = self.tabela.item(sel[0], "values")
    #     self.id_selecionado = val[0]
    #     self.txt_nome.delete(0, 'end'); self.txt_nome.insert(0, val[1])
    #     self.txt_matricula.delete(0, 'end'); self.txt_matricula.insert(0, val[2])
    #     for i in range(4): getattr(self, f'txt_n{i+1}').delete(0, 'end'); getattr(self, f'txt_n{i+1}').insert(0, val[i+3])
    def carregar_selecionado(self, event):
        sel = self.tabela.selection()
        if not sel: return
        
        # Extrai os valores da linha clicada
        val = self.tabela.item(sel[0], "values")
        self.id_selecionado = val[0]
        
        # Limpa e preenche cada campo manualmente
        self.txt_nome.delete(0, 'end')
        self.txt_nome.insert(0, val[1])
        
        self.txt_matricula.delete(0, 'end')
        self.txt_matricula.insert(0, val[2])
        
        self.txt_n1.delete(0, 'end')
        self.txt_n1.insert(0, val[3])
        
        self.txt_n2.delete(0, 'end')
        self.txt_n2.insert(0, val[4])
        
        self.txt_n3.delete(0, 'end')
        self.txt_n3.insert(0, val[5])
        
        self.txt_n4.delete(0, 'end')
        self.txt_n4.insert(0, val[6])

    def atualizar(self):
        if not self.id_selecionado: return
        notas, media = self.processar_notas()
        if not notas: return
        conn = sqlite3.connect("notas.db")
        conn.execute("UPDATE alunos SET nome=?, matricula=?, n1=?, n2=?, n3=?, n4=?, media=? WHERE id=?",
                     (self.txt_nome.get(), self.txt_matricula.get(), *notas, media, self.id_selecionado))
        conn.commit(); conn.close(); self.listar()

    def excluir(self):
        if not self.id_selecionado: return
        conn = sqlite3.connect("notas.db")
        conn.execute("DELETE FROM alunos WHERE id=?", (self.id_selecionado,))
        conn.commit(); conn.close(); self.listar()

    def limpar_campos(self):
        self.txt_nome.delete(0, 'end')
        self.txt_matricula.delete(0, 'end')
        for i in range(1, 5):
            getattr(self, f'txt_n{i}').delete(0, 'end')
        self.id_selecionado = None

if __name__ == "__main__":
    inicializar_banco()
    root = tk.Tk()
    AppCadastroNotas(root)
    root.mainloop()