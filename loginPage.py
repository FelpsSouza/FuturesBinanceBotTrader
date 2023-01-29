from tkinter import *
import webbrowser

root = Tk()


def callback(url):
    webbrowser.open_new(url)


class loginPage():
    def __init__(self):
        self.root = root
        self.background()
        # self.frames()
        self.labels()
        self.inputs()
        self.buttons()
        self.root.mainloop()

    def background(self):
        self.root.title("Trader Bot - Login")
        self.root.configure(background="#FFC104")
        self.root.resizable(False, False)
        self.root.attributes("-fullscreen", False)
        self.root.maxsize = "320x480"
        self.root.geometry(self.root.maxsize)

    def frames(self):
        self.mainFrame = Frame(self.root, bd=4, background="#23FF00")
        self.mainFrame.place(relx=0.3, rely=0.23, relwidth=0.4, relheight=0.4)

    def labels(self):
        # BOT TRADER LABEL
        self.icon = Label(text="Bot Trader", font=('Impact', 14))
        self.icon.place(relx=0.15, rely=0.14, relwidth=0.35, relheight=0.05)

        # LOGIN LABEL
        self.loginLabel = Label(text="Login", background="#23FF01")
        self.loginLabel.place(relx=0.15, rely=0.25)

        # PASSWORD LABEL
        self.passwordLabel = Label(text="Senha", background="#23FF01")
        self.passwordLabel.place(relx=0.15, rely=0.43)

        # FORGOT PASSWORD LABEL LINK
        self.forgotPassLinkLabel = Label(text="Esqueçeu a senha?", background="#23FF01", foreground="blue", cursor="hand2")
        self.forgotPassLinkLabel.bind("<Button-1>", lambda e: callback("https://accounts.binance.com/pt-BR/login"))

        self.forgotPassLinkLabel.pack()
        self.forgotPassLinkLabel.place(relx=0.55, rely=0.55)

        # NOT REGISTER LABEL1
        self.notRegisteredLabel1 = Label(text="NÃO É CADASTRADO?", background="#FFC104")
        self.notRegisteredLabel1.place(relx=0.28, rely=0.77)

        # NOT REGISTER LABEL2
        self.notRegisteredLabel2 = Label(text="CRIE UMA CONTA", background="#FFC104", underline=True, cursor="hand2")
        self.notRegisteredLabel2.bind("<Button-1>", lambda e: callback("https://accounts.binance.com/pt-BR/register"))
        self.notRegisteredLabel2.place(relx=0.32, rely=0.805)

        # NOT REGISTER LABEL3
        self.notRegisteredLabel3 = Label(text="AGORA MESMO", background="#FFC104")
        self.notRegisteredLabel3.place(relx=0.335, rely=0.84)

    def inputs(self):
        # LOGIN INPUT
        self.loginInput = Entry(font=("Verdana", 10), width=15)

        self.loginInput.place(relx=0.15, rely=0.31,relwidth=0.7, relheight=0.05)

        # PASSWORD INPUT
        self.passwordInput = Entry(show="*", font=("Verdana", 10), width=15)
        self.passwordInput.place(relx=0.15, rely=0.49,relwidth=0.7, relheight=0.05)

    def buttons(self):
        # REMEMBER LOGIN CHECKBOX
        self.remeberLoginCheckBox = Checkbutton(text="Lembrar login", onvalue=1, offvalue=0, background="#FFC104")
        self.remeberLoginCheckBox.place(relx=0.15, rely=0.55)

        # LOGIN BUTTON
        self.loginButton = Button(text="Login",font=("Verdana", 12))
        # self.loginButton.bind(
        #     "<Button-1>", lambda e: callback("https://accounts.binance.com/pt-BR/register"))

        self.loginButton.place(relx=0.35, rely=0.65, relwidth=0.25, relheight=0.1)


loginPage()
