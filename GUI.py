import tkinter


class PizaSchoolGUI:
    def __init__(self):
        self.init_GUI()
    def init_GUI(self):
        self.CANVAS_vertical = 600 #세로
        self.CANVAS_horizontal = 1000 #가로

        self.root = tkinter.Tk()
        self.root.title('피자스쿨')
        self.root.geometry(f'{self.CANVAS_horizontal}x{self.CANVAS_vertical}')
        self.root.resizable(width=False, height=False)
        self.canvas = tkinter.Canvas(self.root, bg='white', width=self.CANVAS_horizontal, height=self.CANVAS_vertical)
        self.canvas.pack()
        self.root.mainloop()


if __name__ == '__main__':
    GUI = PizaSchoolGUI()