import tkinter as tk

# import Dino_runGame.main
import main
import setting
from PySide2.QtWidgets import QMessageBox


class SignUpGUI:
    def __init__(self,signup):
        self.signup = signup
        self.user = {"num": '',"pw":'', "score": []}
        self.id = ''
        self.pw = ''
        self.file_path = "user.txt"


        #회원가입 배경
        self.signUpbg = tk.PhotoImage(file="signUpbg.gif")
        self.signUpLabel = tk.Label(self.signup, image=self.signUpbg)
        self.signUpLabel.place(x=0, y=0)

        #아이디 텍스트
        self.idText = tk.PhotoImage(file="idText.png")
        self.idLabel = tk.Label(self.signup,image=self.idText)
        self.idLabel.place(x=490, y=300, width=60, height=30)

        # 아이디 입력 받기
        self.getId = tk.Entry(self.signup)
        self.getId.place(x=490, y=330, width=300, height=50)

        # 비밀번호 텍스트
        self.pwText = tk.PhotoImage(file="pwText.png")
        self.pwLabel = tk.Label(self.signup, image=self.pwText)
        self.pwLabel.place(x=490, y=385, width=90, height=30)

        # 비밀번호 입력 받기
        self.getPw = tk.Entry(self.signup)
        self.getPw.place(x=490, y=420, width=300, height=50)

        # 회원가입 버튼
        self.signUpPhoto = tk.PhotoImage(file="signupbtn.png")
        self.signUpbtn = tk.Button(image=self.signUpPhoto, command=self.setUserMove)
        self.signUpbtn.place(x=490, y=490, width=300, height=50)


    def setUser(self):
        print('--회원가입--')
        self.id = str(self.getId.get())
        self.pw = str(self.getPw.get())

        if self.id == ' ' and self.id == '':
            print('아이디는 공백으로 설정할 수 없습니다.')
            self.setUser()

        if self.pw == ' ' and self.pw == '':
            print('비밀번호는 공백으로 설정할 수 없습니다.')
            self.setUser()

        self.doubleCheck()

    def save(self):
        self.user['id'] = self.id
        self.user['pw'] = self.pw
        test = {"num":self.id,"pw":self.pw, "score":[]}
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
                print('다른 아이디를 사용하세요.')
                self.setUser()
                break

            if data == '':
                self.save()
                break

    def setUserMove(self):
        self.setUser()

    def signUpEnd(self):
        #tk.messagebox.showinfo("알림창", "Sign up Success!!")
        print('회원가입 성공')
        move = LoginGUI(self.signup)



class LoginGUI:
    def __init__(self,login):
        self.login = login
        # self.getid = tk.StringVar
        # self.getpw = tk.StringVar
        self.id = ''
        self.pw = ''
        self.user = ''
        self.file_path = 'user.txt'


        #로그인 화면 이미지
        self.loginbg = tk.PhotoImage(file="Loginbg.gif")
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
        self.loginPhoto = tk.PhotoImage(file="loginbtn.png")
        self.loginbtn = tk.Button(image=self.loginPhoto,command=self.setIdMove)
        self.loginbtn.place(x=490, y=450, width=300, height=50)


        #회원가입 버튼
        self.signupPhoto = tk.PhotoImage(file="signupbtn.png")
        self.signupbtn = tk.Button(image=self.signupPhoto,command=self.signupmove)
        self.signupbtn.place(x=490, y=510, width=300, height=50)



    def setIdMove(self):
        self.setId()

    def signupmove(self):
        move = SignUpGUI(self.login)

    def setId(self):
        print('--로그인--')
        self.id = str(self.getId.get())
        self.pw = str(self.getPw.get())
        f = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f.readline()
            if self.id in data and self.pw in data:
                #tk.messagebox.showinfo("알림창", "Sign up Success!!")
                # move = Dino_runGame.main.main(self.login)
                print('로그인 성공')
                break

            if data == '':
                new = tk.Tk()
                new.mainloop()
                break