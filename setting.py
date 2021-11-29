import tkinter as tk


class Setting:
    def __init__(self, setC):
        print('넘어감')
        self.setC = setC

        #세팅 배경
        self.setCbg = tk.PhotoImage(file="Loginbg.gif")
        self.setCLabel = tk.Label(self.setC, image=self.setCbg)
        self.setCLabel.config(image=self.setCbg)
        self.setCLabel.place(x=0, y=0)






