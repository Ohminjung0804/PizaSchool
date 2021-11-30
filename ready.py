import tkinter as tk
import main



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
        from Dino_runGame.main import main as dino_main
        self.startPhoto = tk.PhotoImage(file="image/star.png")
        self.startbtn = tk.Button(self.ready, image=self.startPhoto, command=dino_main)
        self.startbtn.place(x=490, y=360, width=300, height=50)

        #로그아웃 버튼
        self.logoutPhoto = tk.PhotoImage(file="image/logout.png")
        self.logoutbtn = tk.Button(self.ready, image=self.logoutPhoto,command=self.logoutmove)
        self.logoutbtn.place(x=490, y=420, width=300, height=50)

    def logoutmove(self):
        move = main.MainGUI(self.ready)

    # def startmove(self):
    #     move =game.main()






