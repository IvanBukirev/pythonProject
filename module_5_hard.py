from time import sleep


class User:
    '''
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    '''

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.h_password = hash(password)
        self.age = age

    def __str__(self):
        return f'Текущий пользователь - {self.nickname}'




class Video:
    '''
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    '''


    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    '''Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
       Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    '''

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None



    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.h_password:
                self.current_user = user
                print(f'{nickname} вход выполнен')
                return True
        return False


    def register(self, nickname, password, age):
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует!')
                return
        user = User(nickname, password, age)
        self.users.append(user)
        print(f'Новый пользователь {nickname}  зарегистрирован.')
        self.log_in(nickname, password)




    def log_out(self):
        self.current_user = None
        print('Выход выполнен.')

    def add(self, *args):
        for video in args:
            if video.title in self.videos:
                print(f'Видео с названием: "{video.title}" уже существует.')
            else:
                self.videos.append(video)
                print(f'Видео "{video.title}" успешно загружено.')

    def get_videos(self, word):
        word = word.upper()
        result = []
        for video in self.videos:
            if word in video.title.upper():
                result.append(video.title)
        return result

    def find_video(self, title):
        for video in self.videos:
            if title in video.title:
                return video
        return None

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        video = self.find_video(title)
        if video is None:
            print(f'Видео {title} не найдено')
            return
        if video.adult_mode and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            return

        for time in range(video.duration):
            print(f'ведётся просмотр {time + 1} секунды')
            sleep(1)
            video.time_now += 1
        print('Конец видео:)')
        video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


# выход из аккаунта
ur.log_out()
ur.log_in('vasya_pupkin', 'lolkekcheburek')
print(ur.current_user)

v3=Video('Укус Питона',5)
# Добавление видео
ur.add(v3)
ur.register('programmer', 'qwertyu25', 35)
ur.watch_video('Укус Питона')
print(ur.current_user)