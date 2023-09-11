import tkinter as tk

class Interface:
    def __init__(self):
        self.servicos_label = []
        self.produtos_selecionados = []


        self.window = tk.Tk()
        self.window.title("Loja de Autopeças")
        self.window.geometry("400x400")

        # Label para o nome
        tk.Label(self.window, text="Nome:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.window)
        self.nome_entry.grid(row=0, column=1)

        # Label para o telefone
        tk.Label(self.window, text="Telefone:").grid(row=1, column=0)
        self.telefone_entry = tk.Entry(self.window)
        self.telefone_entry.grid(row=1, column=1)

        # Label para o endereço
        tk.Label(self.window, text="Endereço:").grid(row=2, column=0)
        self.endereco_entry = tk.Entry(self.window)
        self.endereco_entry.grid(row=2, column=1)

        # Label para os produtos
        tk.Label(self.window, text="Produtos:").grid(row=3, column=0)

        # Botões para seleção de produtos
        tk.Button(self.window, text="Troca de Pneu (R$50.00)", command=lambda: self.selecionar_produto(1)).grid(row=4, column=0)
        tk.Button(self.window, text="Troca de Suspensão (R$120.00)", command=lambda: self.selecionar_produto(2)).grid(row=5, column=0)
        tk.Button(self.window, text="Troca de Óleo (R$60.00)", command=lambda: self.selecionar_produto(3)).grid(row=6, column=0)

        # Botão para finalizar a compra
        tk.Button(self.window, text="Finalizar Compra", command=self.finalizar_compra).grid(row=7, column=0)

        self.window.mainloop()

    def selecionar_produto(self, produto):
        self.produtos_selecionados.append(produto)
        self.atualizar_resumo_servicos()

    def finalizar_compra(self):
        # Obter o nome, telefone e endereço do cliente
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        endereco = self.endereco_entry.get()

        # Calcular o valor total da compra
        valor_total = self.calcular_valor_total(self.produtos_selecionados)

        # Exibir a comanda
        comanda = "-------- COMANDA --------\n"
        comanda += "Nome: {}\n".format(nome)
        comanda += "Telefone: {}\n".format(telefone)
        comanda += "Endereço: {}\n".format(endereco)
        comanda += "Serviços Selecionados:\n"
        for produto in self.produtos_selecionados:
            if produto == 1:
                comanda += "- Troca de Pneu (R$50.00)\n"
            elif produto == 2:
                comanda += "- Troca de Suspensão (R$120.00)\n"
            elif produto == 3:
                comanda += "- Troca de Óleo (R$60.00)\n"
        comanda += "Valor Total: R${:.2f}".format(valor_total)
        print(comanda)


    def calcular_valor_total(self, produtos):
            valor_total = 0
            for produto in produtos:
                if produto == 1:
                    valor_total += 50
                elif produto == 2:
                    valor_total += 120
                elif produto == 3:
                    valor_total += 60
            return valor_total

    def atualizar_resumo_servicos(self):
        servicos = ""
        for produto in self.produtos_selecionados:
            if produto == 1:
                servicos += "Troca de Pneu (R$50.00)\n"
            elif produto == 2:
                servicos += "Troca de Suspensão (R$120.00)\n"
            elif produto == 3:
                servicos += "Troca de Óleo (R$60.00)\n"
        # Label para o resumo de serviços selecionados
        tk.Label(self.window, text="Serviços Selecionados:").grid(row=7, column=0)
        self.servicos_label = tk.Label(self.window, text="")
        self.servicos_label.grid(row=8, column=0)
        self.servicos_label.config(text=servicos)


    def atualizar_comanda(self):
            nome = self.nome_entry.get()
            telefone = self.telefone_entry.get()
            endereco = self.endereco_entry.get()
            servicos = ""
            valor_total = self.calcular_valor_total(self.produtos_selecionados)

            for produto in self.produtos_selecionados:
                if produto == 1:
                    servicos += "Troca de Pneu (R$50.00)\n"
                elif produto == 2:
                    servicos += "Troca de Suspensão (R$120.00)\n"
                elif produto == 3:
                    servicos += "Troca de Óleo (R$60.00)\n"

            self.comanda = "-------- COMANDA --------\n"
            self.comanda += "Nome: {}\n".format(nome)
            self.comanda += "Telefone: {}\n".format(telefone)
            self.comanda += "Endereço: {}\n".format(endereco)
            self.comanda += "Serviços Selecionados:\n{}\n".format(servicos)
            self.comanda += "Valor Total: R${:.2f}\n".format(valor_total)
            self.comanda_label.config(text=self.comanda)
            # Label para a comanda
            self.comanda_label = tk.Label(self.window, text="")
            self.comanda_label.grid(row=10, column=0)

        # Exibir a comanda em uma nova janela
            comanda_window = tk.Toplevel()
            comanda_window.title("Comanda")
            comanda_window.geometry("400x400")

            tk.Label(comanda_window, text= 'comanda').pack()


    def calcular_valor_total(self, produtos):
        valor_total = 0
        for produto in produtos:
            if produto == 1:
                valor_total += 50.00
            elif produto == 2:
                valor_total += 120.00
            elif produto == 3:
                valor_total += 60.00
        return valor_total
        self.comanda += "Valor Total: R${:.2f}".format(valor_total)
        print(self.comanda)
    def atualizar_resumo_servicos(self):
        # Remover o resumo de serviços atual
        for widget in self.window.grid_slaves():
            if int(widget.grid_info()["row"]) == 8:
                widget.destroy()

        # Adicionar o novo resumo de serviços
        resumo = "Serviços Selecionados:\n"
        for produto in self.produtos_selecionados:
            if produto == 1:
                resumo += "- Troca de Pneu (R$50.00)\n"
            elif produto == 2:
                resumo += "- Troca de Suspensão (R$120.00)\n"
            elif produto == 3:
                resumo += "- Troca de Óleo (R$60.00)\n"
        tk.Label(self.window, text=resumo).grid(row=8, column=0)




Interface()


