import threading

def thread_job():
    print('this is an added Thread, number is %s'% threading.current_thread()) # 显示正在运行的thread的名字


def main():
    added_thread = threading.Thread(target=thread_job) # 添加线程
    added_thread.start() # 执行线程
    print(threading.active_count()) # 计算有多少已激活的线程
    print(threading.enumerate()) # 查看激活的是哪些线程
    print(threading.current_thread())  #  运行程序是的主线程

if __name__=='__main__':
    main()
