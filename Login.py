import json


class SignUp:
    def __init__(self):
        self.id = ''
        self.user = {'id':'','score':''}
        self.file_path = "user.Json"


    def setUser(self):
        print('--회원가입--')

        self.id = input('아이디를 입력하세요.')
        if self.id == ' ':
            print('아이디는 공백으로 설정할 수 없습니다.')
            self.setUser()


    def save(self):
        self.user['id'] = self.id
        with open(self.file_path, 'a', encoding='utf-8') as f:
            json.dump(self.user,f,indent='4',ensure_ascii=False)


            f.close()


    # def doubleCheck(self):
    #     with open(self.file_path, 'r') as f:
    #         self.user = json.load(f)
    #
    #     if  self.id in self.user['id'] :
    #         print('다른 아이디를 사용하세요.')
    #         self.setUser()


class Login:
    def __init__(self):
        self.id = ''
        self.user = ''
        self.file_path = 'user.Json'

    def setId(self):
        self.id = input('아이디를 입력하세요.')
        with open(self.file_path,'r',encoding='utf-8') as f:
            self.user = json.load(f)
        if self.id in self.user:
            print("로그인 성공")
        else:
            self.setId()

if __name__ == '__main__':
    signup = SignUp()
    login = Login()

    signup.setUser()
    # signup.doubleCheck()
    signup.save()

    login.setId()


