# Importa os componentes do Tkinter para criar a interface gráfica
from tkinter import *
# Importa o módulo responsável por exibir caixas de mensagens
import tkinter.messagebox

# Definindo as cores utilizadas no aplicativo
cor_tela = "#FFFFFF"  # Branco
cor_fundo = "#DBDCF7"  # Azul claro
cor2 = "#030303"  # Preto

# Criando a janela principal do aplicativo
janela = Tk()
# Definindo o título da janela
janela.title("APP DE CORES")
# Definindo a largura e a altura da janela em pixels
janela.geometry("620x310")
# Configurando a cor de fundo da janela
janela.configure(bg=cor_fundo)

# Criando a tela de visualização da cor, definindo seu tamanho e borda
tela = Label(janela, bg=cor_tela, width=38, height=9, bd=2, relief=SOLID)
# Posicionando a tela e definindo seus espaçamentos
tela.grid(row=1, column=1, padx=(60, 10), pady=10)
# Criando o frame que agrupa os controles deslizantes RGB
frame_esquerda = Frame(janela, bg=cor_fundo)
# Posicionando o frame no lado esquerdo da janela
frame_esquerda.grid(row=1, column=0, padx=20, pady=5)
# Criando o frame inferior para o código hexadecimal, botão e título
frame_baixo = Frame(janela, bg=cor_fundo)
# Posicionando o frame inferior para ocupar duas colunas
frame_baixo.grid(row=2, column=0, columnspan=2, pady=15)

# Mantendo a janela aberta e aguardando as ações do usuário
janela.mainloop()
