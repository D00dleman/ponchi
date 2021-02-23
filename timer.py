"""
Самое тупое, что можно придумать...
Таймер
"""
__author__ = 'dm'

from time import time


class Timer:
    """
    Думаю, что и так всем все понятно
    """

    def __init__(self, second_for):
        self.pref_time = time()
        self.second_for = second_for

    def timer(self):
        """
        Возращает время, которое прошло с момента обнуления
        """
        return time() - self.pref_time

    def time_out_test(self):
        """
        Тест на обнуление
        """
        return self.timer() > self.second_for

    def reset(self):
        """
        Обнуление таймера
        """
        self.pref_time = time()

    def time_out(self):
        """
        Обнуление таймера, если время вышло
        """
        if self.time_out_test():
            self.reset()
            return True
        else:
            return False
