import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.resizable(False, False)
        
        self.jogador_atual = "X"
        self.placar_x = 0
        self.placar_o = 0
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.criar_widgets()

    def criar_widgets(self):
        self.label_status = tk.Label(
            self.root, 
            text=f"Vez do jogador: {self.jogador_atual}", 
            font=("Arial", 14, "bold"), 
            pady=10
        )
        self.label_status.pack()
        self.frame_tabuleiro = tk.Frame(self.root)
        self.frame_tabuleiro.pack()

        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                botao = tk.Button(
                    self.frame_tabuleiro,
                    text="",
                    font=("Arial", 24, "bold"),
                    width=5,
                    height=2,
                    command=lambda row=r, col=c: self.ao_clicar(row, col)
                )
                botao.grid(row=r, column=c, padx=3, pady=3)
                self.botoes[r][c] = botao

        self.botao_reiniciar = tk.Button(
            self.root,
            text="Reiniciar Jogo",
            font=("Arial", 11),
            command=self.reiniciar_jogo,
            pady=5
        )
        self.botao_reiniciar.pack(pady=10)

    def ao_clicar(self, row, col):
        if self.tabuleiro[row][col] == "" and not self.verificar_fim_de_jogo():
            self.tabuleiro[row][col] = self.jogador_atual
            self.botoes[row][col].config(
                text=self.jogador_atual, 
                fg="blue" if self.jogador_atual == "X" else "red"
            )
            
            if self.verificar_vitoria(self.jogador_atual):
                messagebox.showinfo("Fim de Jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.reiniciar_jogo()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
                self.label_status.config(text=f"Vez do jogador: {self.jogador_atual}")

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if all(self.tabuleiro[i][j] == jogador for j in range(3)):
                return True
            if all(self.tabuleiro[j][i] == jogador for j in range(3)):
                return True
                
        # Verifica diagonais
        if all(self.tabuleiro[i][i] == jogador for i in range(3)):
            return True
        if all(self.tabuleiro[i][2 - i] == jogador for i in range(3)):
            return True
            
        return False

    def verificar_empate(self):
        return all(self.tabuleiro[r][c] != "" for r in range(3) for c in range(3))

    def verificar_fim_de_jogo(self):
        return self.verificar_vitoria("X") or self.verificar_vitoria("O") or self.verificar_empate()

    def reiniciar_jogo(self):
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.label_status.config(text=f"Vez do jogador: {self.jogador_atual}")
        for r in range(3):
            for c in range(3):
                self.botoes[r][c].config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaVelha(root)
    root.mainloop()