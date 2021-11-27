
class SignUp:
    def __init__(self):
        self.user = {"num": '',"pw":'', "score": []}
        self.id = ''
        self.pw = ''
        self.file_path = "user.txt"


    def setUser(self):
        print('--회원가입--')

        self.id = input('아이디를 입력하세요.')
        if self.id == ' ' and self.id == '':
            print('아이디는 공백으로 설정할 수 없습니다.')
            self.setUser()

        self.pw = input('비밀번호를 입력하세요.')
        if self.pw == ' ' and self.pw == '':
            print('비밀번호는 공백으로 설정할 수 없습니다.')
            self.setUser()


    def save(self):
        self.user['id'] = self.id
        self.user['pw'] = self.pw
        test = {"num":self.id,"pw":self.pw, "score":[]}
        with open(self.file_path, 'a', encoding='utf-8') as f:
            f.write(str(test))
            f.write('\n')
            f.close()



    def doubleCheck(self):
        f = open('user.txt','r',encoding='utf-8')
        while True:
            data = f.readline()
            print(data)
            if self.id in data:
                print('다른 아이디를 사용하세요.')
                self.setUser()

            if data == '':
                break


class Login(SignUp):
    def __init__(self):
        self.id = ''
        self.pw = ''
        self.user = ''
        self.file_path = 'user.txt'

    def setId(self):
        print('--로그인--')
        self.id = input('아이디를 입력하세요.')
        self.pw = input('비밀번호를 입력하세요.')
        f = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f.readline()
            print(data)
            if self.id in data and self.pw in data:
                print('로그인 성공')
                break

            if data == '':
                print('다시 로그인 하세요.')
                break


if __name__ == '__main__':
    # signup = SignUp()
    login = Login()
    #
    # signup.setUser()
    # signup.doubleCheck()
    # signup.save()

    login.setId()


