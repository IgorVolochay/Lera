'''
Name: Lera
Version: v0.2

Description:    Новая версия. Добавлена нейронная сеть, 
                обученная на датасете "TlkPersonaChatRus"
                (https://toloka.ai/ru/datasets).
                Общение реализуется в режиме реального
                времени, с помощью нейронной сети.

To-Do list (https://github.com/IgorVolochay/Lera/projects/1):
                (+) - Взаимодействие пользователя и
                      программы
                ( ) - Нейронная сеть для общения:
                    ( ) - Приготовление данных для обучения
                    ( ) - Токенизация
                    ( ) - Векторизация
                    ( ) - Конструирование нейронной сети
                    ( ) - Функция обучения
                    ( ) - Функция сохранения весовФункция сохранения
                          весов
                    ( ) - Обучение...
                ### Опциональное: ###
'''

class User_Interface():
    '''
    СВЯЗУЮЩИЙ КЛАСС! 
    Класс пользовательского интерфейса. 
    Ввод/вывод информации, Служебные команды
    '''

    def __init__(self):
        print("* Start session...")
        print("Lera: Приветик! Мы можем сразу же перейти к разговору! Если ты захочешь остановить разговор, то просто напиши \"выход\" или \"стоп\". Обещаю, я не сильно обижусь)")

        self.input_command()

    def input_command(self):
        while True:
            input_text = input("User: ")

            if input_text in ["exit", "выход", "stop", "стоп",
                              "пока", "bye", ]:
                break
            else:
                # Передача текста на обработку Нейронной Сети
                print(Neural_Network().input_data(input_text))

class Sentence_Conversion():
    '''
    Класс преобразования предложения. 
    Токенизация, Векторизация
    '''
    pass

class Neural_Network():
    '''
    Класс Нейронной Сети. 
    Генерация ответа, Обучение, Сохранение(загрузка) весов
    '''
    def __init__(self):
        pass

    def input_data(self, text):
        return text


if __name__ == "__main__":
    User_Interface()