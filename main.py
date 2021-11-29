import tkinter as tk

import controller as controller

import Login


class MainGUI:
    def __init__(self,main):
        self.main = main

        self.bg = tk.PhotoImage(file="image/mainbg.gif")
        self.bg_label = tk.Label(image=self.bg)
        self.bg_label.place(x=0, y=0)

        # 로그인 버튼
        self.startPhoto = tk.PhotoImage(file="image/startbtn.png")
        self.b1 = tk.Button(self.main, image=self.startPhoto)
        self.b1.config(command=self.loginmove)
        self.b1.place(x=490, y=360, width=300, height=50)

        # 랭킹보기 버튼
        self.rankPhoto = tk.PhotoImage(file="image/rankbtn.png")
        self.b2 = tk.Button(self.main, text="랭킹보기", image=self.rankPhoto)
        self.b2.place(x=490, y=430, width=300, height=50)

    def loginmove(self):
        move = Login.LoginGUI(self.main)
    def play(self):
        self.main.mainloop()


if __name__ == '__main__':
    main = tk.Tk()
    main.title('피자스쿨')
    main.geometry(f'1280x720')
    main.resizable(width=False, height=False)
    main.canvas = tk.Canvas(main, bg='white', width=1280, height=720)

    GUI = MainGUI(main)
    GUI.play()