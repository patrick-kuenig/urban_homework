from time import sleep


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, password):
        if self.current_user is not None:
            print("Ты уже авторизован, сначала надо выйти.")
        else:
            for user in self.users:
                if user.nickname is not login:
                    continue
                elif user.nickname is login and hash(password) == user.password:
                    self.current_user = user
                    break

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
        else:
            print(f"Пользователь {nickname} уже существет.")

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for vid in args:
            if vid not in self.videos and isinstance(vid, Video):
                self.videos.append(vid)

    def get_videos(self, check_word):
        result = []
        for vid in self.videos:
            if check_word.lower() in vid.title.lower():
                result.append(vid.title)
        return result

    def watch_video(self, video_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео!")
        else:
            for vid in self.videos:
                if video_name == vid.title and self.current_user.age < 18 and vid.adult_mode is True:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    break
                elif video_name == vid.title and self.current_user.age >= 18 and vid.adult_mode is True:
                    for i in range(vid.duration):
                        vid.time_now += 1
                        print(i, end='..')
                        sleep(1)
                    print("Конец видео.")
                    break
                elif video_name == vid.title and vid.adult_mode is False:
                    for i in range(vid.duration):
                        vid.time_now += 1
                        print(i)
                        sleep(1)
                    print("Конец видео.")



class User:

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'User: {self.nickname}'


class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('vasya_pupkin', '1234')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
ur.watch_video('Для чего девушкам парень программист?')
