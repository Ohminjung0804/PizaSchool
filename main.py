import tkinter as tk
import tkinter.messagebox as msgbox
from DataClass import userData
# import Dino_runGame.main
from PySide2.QtWidgets import QMessageBox
import controller as controller

import rank


class MainGUI:
    def __init__(self,main):
        self.main = main

        self.bg = tk.PhotoImage(file="image/mainbg.gif")
        self.bg_label = tk.Label(image=self.bg)
        self.bg_label.place(x=0, y=0)

        # 시작 버튼
        self.startPhoto = tk.PhotoImage(file="image/startbtn.png")
        self.b1 = tk.Button(self.main, image=self.startPhoto)
        self.b1.config(command=self.loginmove)
        self.b1.place(x=490, y=380, width=300, height=50)

    def loginmove(self):
        move = LoginGUI(self.main)
    def play(self):
        self.main.mainloop()

class SignUpGUI:
    def __init__(self,signup):
        self.signup = signup
        self.user = {"num": '',"pw":'', "score": ''}
        self.id = ''
        self.pw = ''
        self.file_path = "user.txt"


        #회원가입 배경
        self.signUpbg = tk.PhotoImage(file="image/signUpbg.gif")
        self.signUpLabel = tk.Label(self.signup, image=self.signUpbg)
        self.signUpLabel.place(x=0, y=0)

        #아이디 텍스트
        self.idText = tk.PhotoImage(file="image/idText.png")
        self.idLabel = tk.Label(self.signup,image=self.idText)
        self.idLabel.place(x=490, y=300, width=60, height=30)

        # 아이디 입력 받기
        self.getId = tk.Entry(self.signup)
        self.getId.place(x=490, y=330, width=300, height=50)

        # 비밀번호 텍스트
        self.pwText = tk.PhotoImage(file="image/pwText.png")
        self.pwLabel = tk.Label(self.signup, image=self.pwText)
        self.pwLabel.place(x=490, y=385, width=90, height=30)

        # 비밀번호 입력 받기
        self.getPw = tk.Entry(self.signup)
        self.getPw.place(x=490, y=420, width=300, height=50)

        # 회원가입 버튼
        self.signUpPhoto = tk.PhotoImage(file="image/signupbtn.png")
        self.signUpbtn = tk.Button(image=self.signUpPhoto, command=self.setUserMove)
        self.signUpbtn.place(x=490, y=490, width=300, height=50)


    def setUser(self):
        print('--회원가입--')
        self.id = str(self.getId.get())
        self.pw = str(self.getPw.get())

        self.doubleCheck()

    def save(self):
        self.user['id'] = self.id
        self.user['pw'] = self.pw
        test = {"num":self.id,"pw":self.pw, "score":'0'}
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(str(test))
            f.write('\n')
            f.close()
        self.signUpEnd()

    def doubleCheck(self):
        f = open('user.txt','r',encoding='utf-8')
        while True:
            data = f.readline()
            print(data)
            if self.id in data:
                msgbox.showinfo("알림","다른 아이디를 사용하세요.")
                print('다른 아이디를 사용하세요.')
                break

            if data == '':
                self.save()
                break

    def setUserMove(self):
        self.setUser()

    def signUpEnd(self):
        msgbox.showinfo("알림", "회원가입 성공")
        print('회원가입 성공')
        move = LoginGUI(self.signup)

class LoginGUI:
    def __init__(self,login):
        self.login = login
        self.id = ''
        self.pw = ''
        self.user = ''
        self.file_path = 'user.txt'
        self.draw_gui()

    def draw_gui(self):
        #로그인 화면 이미지
        self.loginbg = tk.PhotoImage(file="image/Loginbg.gif")
        self.loginLabel = tk.Label(self.login,image=self.loginbg)
        self.loginLabel.place(x=0, y=0)

        #아이디 입력 받기
        self.getId = tk.Entry(self.login)
        self.getId.insert(0,"아이디 입력")
        self.getId.place(x=490, y=330, width=300, height=50)

        #비밀번호 입력 받기
        self.getPw = tk.Entry(self.login,show='*')
        self.getPw.insert(0, "비밀번호")
        self.getPw.place(x=490, y=390, width=300, height=50)

        #로그인 버튼
        self.loginPhoto = tk.PhotoImage(file="image/loginbtn.png")
        self.loginbtn = tk.Button(image=self.loginPhoto,command=self.setIdmove)
        self.loginbtn.place(x=490, y=450, width=300, height=50)

        #회원가입 버튼
        self.signupPhoto = tk.PhotoImage(file="image/signupbtn.png")
        self.signupbtn = tk.Button(image=self.signupPhoto,command=self.signupmove)
        self.signupbtn.place(x=490, y=510, width=300, height=50)

    def setIdmove(self):
        self.setId()

    def signupmove(self):
        move = SignUpGUI(self.login)

    def readymove(self):
        move = Ready(self.login)

    def trunid(self):
        return self.id

    def setId(self):
        print('--로그인--')
        self.id = str(self.getId.get())
        self.pw = str(self.getPw.get())
        f = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f.readline()
            if self.id in data and self.pw in data:
                msgbox.showinfo("알림", "로그인 성공")
                print('로그인 성공')

                name = userData()
                name.set_now_user(self.id)
                print('현재 사용자 넘김')
                self.readymove()
                break

            if data == '':
                msgbox.showinfo("알림","아이디나 비밀번호를 올바르게 입력해주세요.")
                break

class Ready:
    def __init__(self, ready):
        print('레디 프레임으로 넘어감')
        self.ready = ready

        #준비 배경
        self.readybg = tk.PhotoImage(file="image/readybg.gif")
        self.readyLabel = tk.Label(self.ready, image=self.readybg)
        self.readyLabel.config(image=self.readybg)
        self.readyLabel.place(x=0, y=0)

        #게임 시작 버튼
        self.startPhoto = tk.PhotoImage(file="image/star.png")
        self.startbtn = tk.Button(self.ready, image=self.startPhoto, command=self.startmove)
        self.startbtn.place(x=490, y=320, width=300, height=50)

        #랭킹 버튼
        self.rankPhoto = tk.PhotoImage(file="image/rankbtn.png")
        self.rankbtn = tk.Button(self.ready, image=self.rankPhoto, command=self.rankmove)
        self.rankbtn.place(x=490, y=380, width=300, height=50)

        #로그아웃 버튼
        self.logoutPhoto = tk.PhotoImage(file="image/logout.png")
        self.logoutbtn = tk.Button(self.ready, image=self.logoutPhoto,command=self.logoutmove)
        self.logoutbtn.place(x=490, y=440, width=300, height=50)

    def logoutmove(self):
        move = MainGUI(self.ready)
    def rankmove(self):
        # d = rank.Rank()
        # d.changeScore()
        move = rank.ShowRank(self.ready)

    def startmove(self):
        from Dino_runGame.main import main as dino_main
        move =dino_main()

if __name__ == '__main__':
    main = tk.Tk()
    main.title('피자스쿨')
    main.geometry(f'1280x720')
    main.resizable(width=False, height=False)
    main.canvas = tk.Canvas(main, bg='white', width=1280, height=720)

    GUI = MainGUI(main)
    GUI.play()

