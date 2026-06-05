import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# ==========================================
# 1. BANCO DE DADOS
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
# 2. INTERFACE GRAFICA E LOGICA 
# ===============================
class AppCadastroNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Notas - CRUD - Mauro Collin")
        self.root.geometry("800x550")
        self.id_selecionado = None
        self.matricula_original = None # Guarda a matrícula original para validação

        # --- FRAME DE ENTRADA ---
        frame_form = ttk.LabelFrame(root, text=" Dados do Aluno ", padding=10)
        frame_form.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Nome
        ttk.Label(frame_form, text="Nome:").grid(row=0, column=0, sticky="w")
        self.txt_nome = ttk.Entry(frame_form, width=40)
        self.txt_nome.grid(row=0, column=1, columnspan=2, pady=5, sticky="w")
        
        # Matrícula
        ttk.Label(frame_form, text="Matrícula:").grid(row=1, column=0, sticky="w")
        self.txt_matricula = ttk.Entry(frame_form, width=15)
        self.txt_matricula.grid(row=1, column=1, pady=5, sticky="w")
        
        # 1º Bimestre
        ttk.Label(frame_form, text="1º Bimestre:").grid(row=2, column=0, sticky="w")
        self.txt_n1 = ttk.Entry(frame_form, width=15)
        self.txt_n1.grid(row=2, column=1, pady=2, sticky="w") 
        
        # 2º Bimestre
        ttk.Label(frame_form, text="2º Bimestre:").grid(row=3, column=0, sticky="w")
        self.txt_n2 = ttk.Entry(frame_form, width=15)
        self.txt_n2.grid(row=3, column=1, pady=2, sticky="w") 
        
        # 3º Bimestre
        ttk.Label(frame_form, text="3º Bimestre:").grid(row=4, column=0, sticky="w")
        self.txt_n3 = ttk.Entry(frame_form, width=15)
        self.txt_n3.grid(row=4, column=1, pady=2, sticky="w") 
        
        # 4º Bimestre
        ttk.Label(frame_form, text="4º Bimestre:").grid(row=5, column=0, sticky="w")
        self.txt_n4 = ttk.Entry(frame_form, width=15)
        self.txt_n4.grid(row=5, column=1, pady=2, sticky="w") 

        # --- BOTÕES ---
        frame_btn = ttk.Frame(root)
        frame_btn.grid(row=1, column=0, pady=10)
        ttk.Button(frame_btn, text="Adicionar", command=self.inserir).grid(row=0, column=0, padx=5)
        ttk.Button(frame_btn, text="Atualizar", command=self.atualizar).grid(row=0, column=1, padx=5)
        ttk.Button(frame_btn, text="Excluir", command=self.excluir).grid(row=0, column=2, padx=5)
        ttk.Button(frame_btn, text="Limpar", command=self.limpar_campos).grid(row=0, column=3, padx=5)

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

        # Definindo larguras das colunas
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
        try:
            notas = []
            for i in range(1, 5):
                valor_campo = getattr(self, f'txt_n{i}').get().strip()
                if valor_campo == "":
                    notas.append(None)
                else:
                    nota_float = float(valor_campo)
                    if nota_float < 0 or nota_float > 10:
                        raise ValueError
                    notas.append(nota_float)
            
            notas_preenchidas = [n for n in notas if n is not None]
            if notas_preenchidas:
                media = round(sum(notas_preenchidas) / len(notas_preenchidas), 2)
            else:
                media = None
                
            return notas, media
        except ValueError:
            messagebox.showerror("Erro", "Insira notas válidas (0 a 10)!")
            return False, False

    def inserir(self):
        if not self.txt_nome.get().strip() or not self.txt_matricula.get().strip():
            messagebox.showerror("Erro", "Nome e Matrícula são campos obrigatórios!")
            return

        notas, media = self.processar_notas()
        if notas is False: return
        
        try:
            conn = sqlite3.connect("notas.db")
            conn.execute("INSERT INTO alunos (nome, matricula, n1, n2, n3, n4, media) VALUES (?,?,?,?,?,?,?)",
                         (self.txt_nome.get().strip(), self.txt_matricula.get().strip(), *notas, media))
            conn.commit()
            conn.close()
            self.limpar_campos()
            self.listar()
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", "Matrícula já existe.")

    def listar(self):
        for i in self.tabela.get_children():
            self.tabela.delete(i)
        conn = sqlite3.connect("notas.db")
        for row in conn.execute("SELECT * FROM alunos"):
            lista_row = list(row)
            for idx in range(3, 7):
                if lista_row[idx] is None:
                    lista_row[idx] = ""
            if row[7] is not None:
                lista_row[7] = f"{row[7]:.2f}"
            else:
                lista_row[7] = ""
            self.tabela.insert("", "end", values=lista_row)
        conn.close()

    def carregar_selecionado(self, event):
        sel = self.tabela.selection()
        if not sel: return

        val = self.tabela.item(sel[0], "values")
        self.id_selecionado = val[0]
        self.matricula_original = val[2] # Armazena a matrícula que veio do banco

        self.txt_nome.delete(0, 'end')
        self.txt_nome.insert(0, val[1])
        
        # Modifica o estado para 'normal' temporariamente para poder preencher o campo
        self.txt_matricula.config(state="normal")
        self.txt_matricula.delete(0, 'end')
        self.txt_matricula.insert(0, val[2])
        # Desativa o campo para o usuário não conseguir digitar alterações por cima
        self.txt_matricula.config(state="readonly")
        
        for i in range(1, 5):
            campo = getattr(self, f'txt_n{i}')
            campo.delete(0, 'end')
            campo.insert(0, val[2 + i])

    def atualizar(self):
        if not self.id_selecionado: return
        
        # Validação de Segurança: Garante que a matrícula do campo (mesmo bloqueado) bate com a original
        matricula_atual = self.txt_matricula.get().strip()
        if matricula_atual != self.matricula_original:
            messagebox.showerror("Erro", "A matrícula não pode ser modificada!")
            return

        if not self.txt_nome.get().strip():
            messagebox.showerror("Erro", "O campo Nome é obrigatório!")
            return

        notas, media = self.processar_notas()
        if notas is False: return
        
        conn = sqlite3.connect("notas.db")
        # Mantém a query atualizando a matrícula com o valor original seguro
        conn.execute("UPDATE alunos SET nome=?, matricula=?, n1=?, n2=?, n3=?, n4=?, media=? WHERE id=?",
                     (self.txt_nome.get().strip(), self.matricula_original, *notas, media, self.id_selecionado))
        conn.commit()
        conn.close()
        self.limpar_campos()
        self.listar()
        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
        
    def excluir(self):
        if not self.id_selecionado: return
        conn = sqlite3.connect("notas.db")
        conn.execute("DELETE FROM alunos WHERE id=?", (self.id_selecionado,))
        conn.commit(); conn.close(); self.listar()
        self.limpar_campos()
        messagebox.showinfo("Sucesso", "Dados excluídos com sucesso!")

    def limpar_campos(self):
        self.txt_nome.delete(0, 'end')
        
        # Garante que o campo volte ao estado normal ao limpar para permitir novas inserções
        self.txt_matricula.config(state="normal")
        self.txt_matricula.delete(0, 'end')
        
        for i in range(1, 5):
            getattr(self, f'txt_n{i}').delete(0, 'end')
        self.id_selecionado = None
        self.matricula_original = None

if __name__ == "__main__":
    inicializar_banco()
    root = tk.Tk()
    AppCadastroNotas(root)
    root.mainloop()
