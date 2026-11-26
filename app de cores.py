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
# Mantendo a janela aberta e aguardando as ações do usuário
janela.mainloop()
