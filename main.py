import customtkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("light")

largura_janela = 700
altura_janela = 400

app = customtkinter.CTk()
app.title("Marcação para Barbearia")

# Define o tamanho inicial da janela
app.geometry(f"{largura_janela}x{altura_janela}")
# Impede a redimensionamento da janela
app.resizable(False, False)

mode = "dark"


def mudar_modo():
    global mode
    if mode == "dark":
        customtkinter.set_appearance_mode("light")
        mode = "light"
    else:
        customtkinter.set_appearance_mode("dark")
        mode = "dark"


# Email com a primeira ft
def send_email_with_image_nudread(image_path, recipient_email, nome):
    ima1 = image_path

    corpo_do_email = f"""
    <p>Aqui está uma nova marcação</p>
    <p>Nome: {nome}</p>
    <p>O corte vai ser:</p>
    <img src="cid:{ima1}" />
    """
    msg = MIMEMultipart()
    msg['Subject'] = "Marcação"
    msg['From'] = 'emaildapp'
    msg['To'] = recipient_email
    password = 'dtew okch hvhl whzw'
    msg.attach(MIMEText(corpo_do_email, 'html'))

    with open(ima1, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', f'<{ima1}>')
        msg.attach(img)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
    print('Email enviado')


def on_button_click_nudread():
    nome_value = nome.get()
    send_email_with_image_nudread("imagem1.jpg", "emaildobarbeiro", nome_value)


# Email com a 2º ft
def send_email_with_image_lowfade(image_path, recipient_email, nome):
    ima1 = image_path

    corpo_do_email = f"""
    <p>Aqui está uma nova marcação</p>
    <p>Nome: {nome}</p>
    <p>O corte vai ser:</p>
    <img src="cid:{ima1}" />
    """
    msg = MIMEMultipart()
    msg['Subject'] = "Marcação"
    msg['From'] = 'emaildapp'
    msg['To'] = recipient_email
    password = 'dtew okch hvhl whzw'
    msg.attach(MIMEText(corpo_do_email, 'html'))

    with open(ima1, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', f'<{ima1}>')
        msg.attach(img)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
    print('Email enviado')


# Email com a 3º ft
def send_email_with_image_afro(image_path, recipient_email, nome):
    ima1 = image_path

    corpo_do_email = f"""
    <p>Aqui está uma nova marcação</p>
    <p>Nome: {nome}</p>
    <p>O corte vai ser:</p>
    <img src="cid:{ima1}" />
    """
    msg = MIMEMultipart()
    msg['Subject'] = "Marcação"
    msg['From'] = 'emaildapp'
    msg['To'] = recipient_email
    password = 'dtew okch hvhl whzw'
    msg.attach(MIMEText(corpo_do_email, 'html'))

    with open(ima1, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-ID', f'<{ima1}>')
        msg.attach(img)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()
    print('Email enviado')


# Título da interface
frame2 = tk.Frame(app, highlightbackground="black",
                  highlightthickness=4,
                  width=1200,
                  height=100,
                  bd=4,
                  bg="blue")
frame2.place(x=0, y=100)
frame2.pack()

labeltitulo = customtkinter.CTkLabel(frame2, text="Marcação para Barbearia", fg_color="transparent",
                                     font=("Helvetica", 30, "bold"))
labeltitulo.pack()
labeltitulo.place(x=300, y=10)

# Fim do título da interface

# Label e Entry (Nome)
labelnome = customtkinter.CTkLabel(app, text="Digite seu nome:", fg_color="transparent",
                                   font=("Helvetica", 15, "bold"),
                                   height=50)
labelnome.pack()

nome = customtkinter.CTkEntry(app, placeholder_text=" ", width=250, height=10)
nome.pack()
nome.place(x=410, y=81)

# Label e Entry (Email)
labelemail = customtkinter.CTkLabel(app, text="Digite seu email:", fg_color="transparent",
                                    font=("Helvetica", 15, "bold"))
labelemail.pack()

email1 = customtkinter.CTkEntry(app, placeholder_text=" ", width=250, height=10)
email1.pack()
email1.place(x=410, y=120)

# Adicionando a 1º imagem a minha label
file = 'imagem1.jpg'
image = Image.open(file)
zoom = 1.8
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((140, 140)))
label = tk.Label(app, image=img)
label.image = img
label.pack(padx=10, pady=10)
label.place(relx=0.5, rely=0.5, anchor="center")

# Adicionando a 2º imagem a minha label
file = 'imagem2.jpg'
image = Image.open(file)
zoom = 1.8
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((140, 140)))
label = tk.Label(app, image=img)
label.image = img
label.pack(padx=10, pady=10)
label.place(relx=0.7, rely=0.5, anchor="center")

# Adicionando a 3º imagem a minha label
file = 'imagem3.jpeg'
image = Image.open(file)
zoom = 1.8
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((140, 140)))
label = tk.Label(app, image=img)
label.image = img
label.pack(padx=10, pady=10)
label.place(relx=0.9, rely=0.5, anchor="center")

# Botões para envio
button1 = customtkinter.CTkButton(app, text="Nudread", width=100, height=30, command=on_button_click_nudread)
button1.place(x=300, y=255)

button2 = customtkinter.CTkButton(app, text="Low-Fade", width=100, height=30,
                                   command=lambda: send_email_with_image_lowfade("imagem2.jpg",
                                                                                  "fdlfidelitoborges@gmail.com",
                                                                                  nome.get()))
button2.place(x=440, y=255)

button3 = customtkinter.CTkButton(app, text="Afro", width=100, height=30,
                                   command=lambda: send_email_with_image_afro("imagem3.jpeg",
                                                                             "fdlfidelitoborges@gmail.com",
                                                                             nome.get()))
button3.place(x=580, y=255)

button_mudar_modo = customtkinter.CTkButton(app, text="Modo", width=100, height=30, command=mudar_modo)
button_mudar_modo.place(x=440, y=350)

# Frame com foto da barbearia
frame1 = tk.Frame(app, highlightbackground="black", highlightthickness=4, width=400, height=800, bd=0, bg="white")
frame1.pack()
frame1.place(x=0, y=-80)
frame1.config(bg="white")
img = ImageTk.PhotoImage(Image.open("image.jpg"))
label = tk.Label(frame1, image=img, width=400, height=700, bg='white')
label.pack()
# Fim da frame

app.mainloop()
