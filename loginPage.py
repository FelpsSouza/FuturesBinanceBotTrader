from tkinter import *


root = Tk()


class loginPage():
    def __init__(self):
        self.root = root
        self.background()
        self.frames()
        self.labels()
        self.inputs()
        self.buttons()
        self.root.mainloop()

    def background(self):
        self.root.title("Trader Bot - Login")
        self.root.configure(background="#ffc104")
        self.root.resizable(False, False)
        self.root.attributes("-fullscreen", False)
        self.root.maxsize = "1024x768"
        self.root.geometry(self.root.maxsize)

    def frames(self):
        self.mainFrame = Frame(self.root, bd=4, bg="#23FF00")
        self.mainFrame.place(relx=0.3, rely=0.23, relwidth=0.4, relheight=0.4)

    def labels(self):
        self.icon = Label(text="ICON")
        self.icon.place(relx=0.45, rely=0.14, relwidth=0.11, relheight=0.05)

        self.loginLabel = Label(
            self.mainFrame, text="Login", background="#23FF01")
        self.loginLabel.place(relx=0.15, rely=0, relwidth=0.1, relheight=0.1)

        self.passwordLabel = Label(
            self.mainFrame, text="Senha", background="#23FF01")
        self.passwordLabel.place(relx=0.15, rely=0.22,
                                 relwidth=0.1, relheight=0.1)

    def inputs(self):
        self.loginInput = Entry(self.mainFrame, font="Arial", width=15)
        self.loginInput.place(relx=0.15, rely=0.1,
                              relwidth=0.7, relheight=0.08)

        self.passwordInput = Entry(self.mainFrame,show="*", font="Arial", width=15)
        self.passwordInput.place(relx=0.15, rely=0.31,
                                 relwidth=0.7, relheight=0.08)

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
