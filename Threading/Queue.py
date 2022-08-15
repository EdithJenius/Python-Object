import threading
import time
from queue import Queue 
"""多线程运算没有返回值，所以要把结果放在长的队列中，
对每一个线程的队列在主线程拿出"""

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2 # 列表计算
    q.put(l) # 一般是return l，线程不能用return

def multithreading():
    q = Queue() # 在q中放入返回值
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4): # 定义4个线程
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get()) # 从q中按顺序拿出一个
    print(results)

if __name__=='__main__':
    multithreading()
