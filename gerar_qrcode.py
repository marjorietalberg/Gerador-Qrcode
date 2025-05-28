import qrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


# 🔥 Função para gerar QR Code
def gerar_qrcode():
    link = entrada.get()
    if not link:
        messagebox.showerror("🚫 Erro", "Por favor, insira um link!")
        return

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4  # Mais borda para não cortar
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")  # Fundo branco
    img = img.resize((300, 300))

    img.save("temp_qrcode.png")
    exibir_imagem(img)

    caminho_arquivo = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Salvar QR Code como..."
    )
    if caminho_arquivo:
        img.save(caminho_arquivo)
        messagebox.showinfo("✅ Sucesso", f"QR Code salvo em:\n{caminho_arquivo}")


# ✨ Exibir imagem no app
def exibir_imagem(img):
    img_tk = ImageTk.PhotoImage(img)
    imagem_label.configure(image=img_tk)
    imagem_label.image = img_tk


# 🎨 Setup Janela
janela = tk.Tk()
janela.title("🚀 Gerador de QR Code - Marjorie")
janela.configure(bg="#121212")
janela.geometry("500x650")
janela.resizable(False, False)

# 💎 Estilo - Card
card = tk.Frame(janela, bg="#1a1a1a", bd=0, relief="flat")
card.place(relx=0.5, rely=0.5, anchor="center", width=440, height=560)

# 🔥 Título
titulo = tk.Label(card, text="🔗 Gerador de QR Code",
                   bg="#1a1a1a", fg="#f72585",
                   font=("Arial", 20, "bold"))
titulo.pack(pady=(30, 5))

subtitulo = tk.Label(card, text="Cole o link abaixo 👇",
                      bg="#1a1a1a", fg="#e0e0e0",
                      font=("Arial", 13))
subtitulo.pack()

# 🔗 Entrada
entrada = tk.Entry(card, width=35, font=("Arial", 13), border=0,
                    relief="flat", highlightthickness=2,
                    highlightbackground="#00f5d4", highlightcolor="#00f5d4",
                    bg="#303030", fg="white", insertbackground="white")
entrada.pack(pady=15)

# 🔥 Botão
botao = tk.Button(card, text="✨ Gerar QR Code", command=gerar_qrcode,
                   bg="#7209b7", fg="white", activebackground="#560bad",
                   activeforeground="white",
                   font=("Arial", 12, "bold"), relief="flat",
                   padx=15, pady=8, cursor="hand2")
botao.pack(pady=10)

# 🖼️ Imagem QR (Corrigido maior)
imagem_label = tk.Label(card, bg="#1a1a1a", width=300, height=300)
imagem_label.pack(pady=20)

# 🖤 Créditos
creditos = tk.Label(card, text="By Marjorie 💖",
                      bg="#1a1a1a", fg="#888888",
                      font=("Arial", 10))
creditos.pack(side="bottom", pady=15)


# 🚀 Executa
janela.mainloop()
