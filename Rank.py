from Login import LoginGUI as login


class Rank:
    def __init__(self):
        self.time = input('시간')
        self.user = dict()
        self.current = login().id

    def setTime(self):
        f = open('user.txt', 'r', encoding='utf-8')
        while True:
            self.user = f.readline()
            if self.current == self.user['num']:
                if int(self.user['score']) < int(self.time):
                    self.user['score'] = self.time

            if self.user == '':
                break
        # print(self.user['score'])

    def maxTime(self):
        self.all = list()
        self.u = dict()
        self.gold = ''
        self.silver = ''
        self. bronze = ''
        f = open('user.txt', 'r', encoding='utf-8')
        self.u = f.readline()
        self.all.append(self.u)
        for i in len(self.all):
            onedict = self.all[i]
            onedict['score']

    def show(self):
        pass