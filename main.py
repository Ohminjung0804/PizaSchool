import tkinter as tk


class PizaSchoolGUI:
    def __init__(self):
        self.init_GUI()
    def init_GUI(self):
        self.CANVAS_vertical = 720 #세로
        self.CANVAS_horizontal = 1280 #가로

        self.root = tk.Tk()
        self.root.title('피자스쿨')
        self.root.geometry(f'{self.CANVAS_horizontal}x{self.CANVAS_vertical}')
        self.root.resizable(width=False, height=False)
        self.canvas = tk.Canvas(self.root, bg='white', width=self.CANVAS_horizontal, height=self.CANVAS_vertical)
        bg = tk.PhotoImage(file="main.gif")
        bg_label = tk.Label(image = bg)
        bg_label.place(x = 0, y = 0)


        # 로그인 버튼
        startPhoto = tk.PhotoImage(file="startbtn.png")
        self.b1 = tk.Button(self.root, text="로그인",image = startPhoto)
       
        self.b1.place(x=490, y=360, width = 300, height = 50)
        # self.b1.pack()

        # 회원가입 버튼
        rankPhoto = tk.PhotoImage(file="rankbtn.png")
        self.b2 = tk.Button(self.root, text="회원가입", image = rankPhoto)
        self.b2.place(x=490, y=430, width = 300, height = 50)


        self.root.mainloop()


if __name__ == '__main__':
    GUI = PizaSchoolGUI()