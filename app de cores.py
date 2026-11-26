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

# Controles deslizantes RGB no frame esquerdo
# Cria o rótulo da cor vermelha (RED).
l_red = Label(
    frame_esquerda,
    text="RED",
    width=7,
    bg=cor_fundo,
    fg="red",
    anchor="nw",
    font=("Arial", 14, "bold"),
)
# Posiciona o rótulo na primeira linha, coluna 0.
l_red.grid(row=0, column=0)
# Cria o controle deslizante vermelho, com valores de 0 a 255.
s_red = Scale(
    frame_esquerda,
    from_=0,
    to=255,
    length=150,
    bg=cor_fundo,
    fg="red",
    orient=HORIZONTAL,
)
# Posiciona o controle vermelho ao lado do rótulo.
s_red.grid(row=0, column=1)

# Cria o rótulo da cor verde (GREEN).
l_green = Label(
    frame_esquerda,
    text="GREEN",
    width=7,
    bg=cor_fundo,
    fg="green",
    anchor="nw",
    font=("Arial", 14, "bold"),
)
# Posiciona o rótulo na segunda linha, coluna 0.
l_green.grid(row=1, column=0)
# Cria o controle deslizante verde, com valores de 0 a 255.
s_green = Scale(
    frame_esquerda,
    from_=0,
    to=255,
    length=150,
    bg=cor_fundo,
    fg="green",
    orient=HORIZONTAL,
)
# Posiciona o controle verde ao lado do rótulo.
s_green.grid(row=1, column=1)

# Cria o rótulo da cor azul (BLUE).
l_blue = Label(
    frame_esquerda,
    text="BLUE",
    width=7,
    bg=cor_fundo,
    fg="blue",
    anchor="nw",
    font=("Arial", 14, "bold"),
)
# Posiciona o rótulo na terceira linha, coluna 0.
l_blue.grid(row=2, column=0)
# Cria o controle deslizante azul, com valores de 0 a 255.
s_blue = Scale(
    frame_esquerda,
    from_=0,
    to=255,
    length=150,
    bg=cor_fundo,
    fg="blue",
    orient=HORIZONTAL,
)
# Posiciona o controle azul ao lado do rótulo.
s_blue.grid(row=2, column=1)

# Cria o rótulo do código hexadecimal no frame inferior.
l_rgb = Label(
    frame_baixo,
    text="CÓDIGO HEX :",
    bg=cor_fundo,
    font=("Verdana", 14, "bold"),
)
# Posiciona o rótulo na primeira coluna do frame inferior.
l_rgb.grid(row=0, column=0, padx=5)

# Cria o campo de texto que exibe o código hexadecimal, com texto centralizado.
e_cor = Entry(frame_baixo, width=10, font=("Ivy", 10, "bold"), justify=CENTER)
# Posiciona o campo ao lado do rótulo.
e_cor.grid(row=0, column=1, padx=5)

# Cria o texto com o nome do aplicativo no frame inferior.
l_app_nome = Label(
    frame_baixo,
    text="ESCOLHA SUA COR!",
    bg=cor_fundo,
    font=("Verdana", 15, "bold"),
)
# Posiciona o nome na quarta coluna do frame inferior.
l_app_nome.grid(row=0, column=3, padx=40)

# Mantendo a janela aberta e aguardando as ações do usuário
janela.mainloop()