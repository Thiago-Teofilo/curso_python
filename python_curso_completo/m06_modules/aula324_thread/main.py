from time import sleep
from threading import Thread

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

# t1 = MeuThread('Thread 1', 5)
# t1.start()

# t2 = MeuThread('Thread 2', 3)
# t2.start()

# t3 = MeuThread('Thread 3', 8)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)

def my_thread(text, time):
    sleep(time)
    print(text)

t1 = Thread(target=my_thread, args=('Thread 1', 3))
t1.start()

t2 = Thread(target=my_thread, args=('Thread 2', 3))
t2.start()

t3 = Thread(target=my_thread, args=('Thread 2', 5))
t3.start()

for i in range(10):
    print(i)
    sleep(1)