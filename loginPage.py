from tkinter import *


root = Tk()


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
        self.root.configure(background="#ffc104")
        self.root.resizable(False, False)
        self.root.attributes("-fullscreen", False)
        self.root.maxsize = "320x480"
        self.root.geometry(self.root.maxsize)

    def frames(self):
        self.mainFrame = Frame(self.root, bd=4, bg="#23FF00")
        self.mainFrame.place(relx=0.3, rely=0.23, relwidth=0.4, relheight=0.4)

    def labels(self):
        # BOT TRADER LABEL
        self.icon = Label(text="Bot Trader",font=('Impact', 14))
        self.icon.place(relx=0.15, rely=0.14, relwidth=0.35, relheight=0.05)

        # LOGIN LABEL
        self.loginLabel = Label(
            text="Login", background="#23FF01")
        self.loginLabel.place(relx=0.15, rely=0.25, relwidth=0.1, relheight=0.05)

        # PASSWORD LABEL
        self.passwordLabel = Label(
            text="Senha", background="#23FF01")
        self.passwordLabel.place(relx=0.15, rely=0.43,relwidth=0.1, relheight=0.05)

    def inputs(self):
        # LOGIN INPUT
        self.loginInput = Entry(font=('Verdana', 10), width=15)
        self.loginInput.place(relx=0.15, rely=0.31,
                              relwidth=0.7, relheight=0.05)

        # PASSWORD INPUT
        self.passwordInput = Entry(
            show="*", font=('Verdana', 10), width=15)
        self.passwordInput.place(relx=0.15, rely=0.49,
                                 relwidth=0.7, relheight=0.05)

    def buttons(self):
        ...
        # remeberLogin = "Lembrar login"
        # val = ""
        # v = self.root.IntVar()
        # v.set(1)

        # self.radioButton = Radiobutton(
        #            self.root,
        #            text=remeberLogin,
        #            padx = 20,
        #            variable=v,
        #         #    command=ShowChoice,
        #            value=val)

        # self.radioButton.place(self.mainFrame, relx=0.9, rely=0.9)


loginPage()
