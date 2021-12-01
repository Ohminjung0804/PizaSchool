class userData:
    USER = ''
    def __init__(self):
        pass

    def set_now_user(self, id):
        userData.USER = id
        # print(f'현재 사용자 {self.USER}')

    def get_now_user(self):
        return userData.USER

    def get_user_info(self):
        f = open('user.txt', 'r', encoding='utf-8')
        while True:
            data = f.readline()
            if data == '':
                break
            data = eval(data)
            # print(data['num'])

            if data['num'] == userData.USER:
                return data

class userScore:
    SCORE = ''
    def __init__(self):
        pass
    def set_now_score(self, score):

        userScore.SCORE = str(score)
        # print(f'현재 사용자 {self.USER}')

    def get_now_score(self):
        return userScore.SCORE

if __name__ == '__main__':
    k = userData()
    k.get_user_info()