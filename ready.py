# import tkinter as tk
# import main
# import rank
#
#
# class Ready:
#     def __init__(self, ready):
#         print('넘어감')
#         self.ready = ready
#
#         #준비 배경
#         self.readybg = tk.PhotoImage(file="image/readybg.gif")
#         self.readyLabel = tk.Label(self.ready, image=self.readybg)
#         self.readyLabel.config(image=self.readybg)
#         self.readyLabel.place(x=0, y=0)
#
#         #게임 시작 버튼
#         self.startPhoto = tk.PhotoImage(file="image/star.png")
#         self.startbtn = tk.Button(self.ready, image=self.startPhoto, command=self.startmove)
#         self.startbtn.place(x=490, y=320, width=300, height=50)
#
#         #랭킹 버튼
#         self.rankPhoto = tk.PhotoImage(file="image/rankbtn.png")
#         self.rankbtn = tk.Button(self.ready, image=self.rankPhoto, command=self.rankmove)
#         self.rankbtn.place(x=490, y=380, width=300, height=50)
#
#         #로그아웃 버튼
#         self.logoutPhoto = tk.PhotoImage(file="image/logout.png")
#         self.logoutbtn = tk.Button(self.ready, image=self.logoutPhoto,command=self.logoutmove)
#         self.logoutbtn.place(x=490, y=440, width=300, height=50)
#
#     def logoutmove(self):
#         move = main.MainGUI(self.ready)
#     def rankmove(self):
#         move = rank.ShowRank(self.ready)
#
#     def startmove(self):
#         from Dino_runGame.main import main as dino_main
#         move =dino_main()
#
#
#
#
#
#
