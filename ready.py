import tkinter as tk


class Ready:
    def __init__(self, ready):
        print('넘어감')
        self.ready = ready

        #준비 배경
        self.readybg = tk.PhotoImage(file="image/readybg.gif")
        self.readyLabel = tk.Label(self.ready, image=self.readybg)
        self.readyLabel.config(image=self.readybg)
        self.readyLabel.place(x=0, y=0)

        #게임 시작 버튼
        self.startPhoto = tk.PhotoImage(file="image/start.png")
        self.start = tk.Button(self.ready, image=self.startPhoto)
        self.start.place(x=490, y=360, width=300, height=50)






