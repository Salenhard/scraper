import module
from threading import Thread

__author__ = "Гурбатов Владислав"
n = int(input("Введите кол-во страниц: "))
for i in range(n):
    # содание потоков чтобы не ждать ответа от каждой страницы по отдельности
    Thread(target = module.parser, args=(i + 1,)).start()