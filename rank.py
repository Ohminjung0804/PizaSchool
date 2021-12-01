from operator import itemgetter

import tkinter as tk

# from Login import LoginGUI as login
import Login
import ready


class Rank:
    def __init__(self,rank):
        self.rank = rank
        from Login import LoginGUI as id
        self.current = '오민정'
        self.oriScore = int()

        # 랭크 배경
        self.rankbg = tk.PhotoImage(file="image/rankbg.gif")
        self.rankLabel = tk.Label(self.rank, image=self.rankbg)
        self.rankLabel.config(image=self.rankbg)
        self.rankLabel.place(x=0, y=0)

        # 뒤로가기기 버튼
        self.backPhoto = tk.PhotoImage(file="image/backbtn.png")
        self.backLabel = tk.Button(self.rank, image=self.backPhoto, command=self.backmove)
        self.backLabel.place(x=490, y=540, width=300, height=50)

    def setScore(self):
        f = open('user.txt', 'r', encoding='utf-8')
        from Dino_runGame import main as dg
        self.newscore =dg.Scoreboard.trunScore()
        while True:
            self.user = eval(f.readline())

            if self.user['num'] == self.current:
                print(self.user)
                self.changeScore()
                break
            if not self.user:
                break

    #신기록이면 기록 바꿔주기
    def changeScore(self):
        # oriScore변수에 원래 있던 점수 넣기
        if self.user['num'] == self.current:
            self.oriScore = self.user['score']
            print(self.oriScore)

        # 더 큰 점수를 다시 self.user변수에 넣기
        if self.oriScore < self.newscore:
            self.user['score'] = str(self.newscore)
            print(self.user)

        #txt파일 정보 전부 리스트에 넣기
        self.search = []
        f2 = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f2.readline()

            if not data:break
            self.search.append(eval(data))

        #리스트에서 정보 바꿔줌
        for i,item in enumerate(self.search):
            if item['num'] == self.user['num']:
                self.search[i] = self.user
                print(self.search)

        #점수기준 내림차순
        self.search = sorted(self.search, key=(lambda x: x['score']), reverse=True)
        print(self.search)

        #파일 전체 지우기
        with open("user.txt", 'r+') as delf:
            delf.truncate(0)
        delf.close()

        #파일에 바뀐 내용 넣기
        with open('user.txt', 'w+', encoding='utf-8') as addf:
            for i in self.search:
                addf.write(str(i)+'\n')
        addf.close()

    #Top3 보여주기
    # def show(self,rank):
    #     # for i in range(3):
    #     #     self.info = self.search[i]
    #     #     self.name = self.info['num']
    #     #     self.score = self.info['score']
    #     #     print(f'{i+1} \t {self.name} - {self.score}')

class ShowRank():
    def __init__(self,rank):
        self.rank = rank
        # 랭크 배경
        self.rankbg = tk.PhotoImage(file="image/rankbg.gif")
        self.rankLabel = tk.Label(self.rank, image=self.rankbg)
        self.rankLabel.config(image=self.rankbg)
        self.rankLabel.place(x=0, y=0)

        # 뒤로가기기 버튼
        self.backPhoto = tk.PhotoImage(file="image/backbtn.png")
        self.backLabel = tk.Button(self.rank, image=self.backPhoto, command=self.backmove)
        self.backLabel.place(x=490, y=540, width=300, height=50)

        self.search = []
        f2 = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f2.readline()

            if not data: break
            self.search.append(eval(data))

        # 첫번째 이름,점수 라벨
        self.info = self.search[0]
        self.name = self.info['num']
        self.score = self.info['score']
        self.firstName = tk.Label(rank, text="사용자 이름1")
        self.firstName.config(text=self.name)
        self.firstName.place(x=530, y=280, width=100, height=50)
        self.firstScore = tk.Label(rank, text=self.score)
        self.firstScore.place(x=660, y=280, width=100, height=50)

        # 두번째 이름,점수 라벨
        self.info = self.search[1]
        self.name = self.info['num']
        self.score = self.info['score']
        self.secondName = tk.Label(rank, text=self.name)
        self.secondName.place(x=530, y=350, width=100, height=50)
        self.secondScore = tk.Label(rank, text=self.score)
        self.secondScore.place(x=660, y=350, width=100, height=50)

        # 세번째 이름,점수 라벨
        self.info = self.search[2]
        self.name = self.info['num']
        self.score = self.info['score']
        self.thirdName = tk.Label(rank, text=self.name)
        self.thirdName.place(x=530, y=435, width=100, height=50)
        self.thirdScore = tk.Label(rank, text=self.score)
        self.thirdScore.place(x=660, y=435, width=100, height=50)
    def backmove(self):
        move = ready.Ready(self.rank)


if __name__ == '__main__':
    rank = Rank()
    rank.setScore()
