import tkinter as tk
import os
from tkinter import messagebox

class Interface:

    def __init__(self):
        self.produtos = {
            1: {"nome": "Troca de Pneu", "preco": 50.00},
            2: {"nome": "Troca de Suspensão", "preco": 120.00},
            3: {"nome": "Troca de Óleo", "preco": 60.00}
        }

        self.produtos_selecionados = []

        self.window = tk.Tk()
        self.window.title("Loja de Autopeças")
        self.window.geometry("800x800")
        self.window.configure(bg="white")

        self.fonte_grande = ("Calibri", 20)
        self.fonte_pequena = ("Calibri", 14)

        # Labels e entradas para nome, telefone e endereço
        self.nome_label, self.nome_entry = self.criar_campo_cliente("Nome:")
        self.telefone_label, self.telefone_entry = self.criar_campo_cliente("Telefone:")
        self.endereco_label, self.endereco_entry = self.criar_campo_cliente("Endereço:")

        # Label para os produtos
        tk.Label(self.window, text="Produtos:", font=self.fonte_grande, bg="white", fg="Black").pack()

        # Botões para seleção de produtos
        for produto_id, produto_info in self.produtos.items():
            botao = tk.Button(self.window, text=f"{produto_info['nome']} (R${produto_info['preco']:.2f})", command=lambda id=produto_id: self.toggle_produto(id), font=self.fonte_pequena, fg="red",bg="yellow")
            botao.pack()

        # Lista de produtos selecionados
        self.lista_produtos = tk.Listbox(self.window, selectmode=tk.MULTIPLE, font=self.fonte_pequena)
        self.lista_produtos.pack()

        # Botão para remover produtos selecionados
        tk.Button(self.window, text="Remover Produto(s)", command=self.remover_produto, font=self.fonte_pequena, fg="red").pack()

        # Botão para finalizar a compra
        tk.Button(self.window, text="Finalizar Compra", command=self.finalizar_compra, font=self.fonte_grande, fg="red").pack()

        # Adicionando o texto no canto direito
        created_by_label = tk.Label(self.window, text="Created by Cainã Reis", font=self.fonte_pequena, fg="black", bg="white")
        created_by_label.place(relx=1.0, rely=0, anchor='ne')



    def criar_campo_cliente(self, label_text):
        label = tk.Label(self.window, text=label_text, font=self.fonte_grande, bg="white", fg="red")
        label.pack()
        entry = tk.Entry(self.window)
        entry.pack()
        return label, entry

    def toggle_produto(self, produto_id):
        if produto_id in self.produtos_selecionados:
            self.produtos_selecionados.remove(produto_id)
        else:
            self.produtos_selecionados.append(produto_id)
        self.atualizar_lista_produtos()

    def remover_produto(self):
        selecionados = self.lista_produtos.curselection()
        produtos_para_remover = []

        for index in selecionados:
            produto_index = int(index)
            produto_id = self.produtos_selecionados[produto_index]
            produtos_para_remover.append(produto_id)

        for produto_id in produtos_para_remover:
            self.produtos_selecionados.remove(produto_id)

        self.atualizar_lista_produtos()

    def atualizar_lista_produtos(self):
        self.lista_produtos.delete(0, tk.END)
        for produto_id in self.produtos_selecionados:
            produto_info = self.produtos[produto_id]
            self.lista_produtos.insert(tk.END, f"{produto_info['nome']} (R${produto_info['preco']:.2f})")

    def finalizar_compra(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()

        valor_total = self.calcular_valor_total(self.produtos_selecionados)

        comanda = "-------- COMANDA --------\n"
        comanda += f"Nome: {nome}\n"
        comanda += f"Telefone: {telefone}\n"
        comanda += f"Endereço: {endereco}\n"
        comanda += "Serviços Selecionados:\n"
        for produto_id in self.produtos_selecionados:
            produto_info = self.produtos[produto_id]
            comanda += f"- {produto_info['nome']} (R${produto_info['preco']:.2f})\n"
        comanda += f"Valor Total: R${valor_total:.2f}"

        # Encontre um nome de arquivo único com numeração incremental
        caminho_base = os.path.join('C:\\Users\\Cainã\\Desktop\\Comandas', nome)
        caminho_comanda = self.encontrar_nome_unico(caminho_base, ".txt")

        # Salvar comanda em um arquivo de texto
        with open(caminho_comanda, 'w') as arquivo:
            arquivo.write(comanda)

        # Exibir janela de mensagem "Comanda Salva"
        messagebox.showinfo("Comanda Salva", "A comanda foi salva com sucesso!")

        print(f"Comanda gerada como {caminho_comanda}")

    def encontrar_nome_unico(self, caminho_base, extensao):
        contador = 1
        while True:
            caminho = f"{caminho_base}_{contador}{extensao}"
            if not os.path.exists(caminho):
                return caminho
            contador += 1

    def calcular_valor_total(self, produtos_selecionados):
        valor_total = 0
        for produto_id in produtos_selecionados:
            valor_total += self.produtos[produto_id]["preco"]
        return valor_total

if __name__ == "__main__":
    Interface().window.mainloop()
