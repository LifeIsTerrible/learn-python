import threading;
import time;
import queue;
from concurrent.futures import ThreadPoolExecutor

# def print_numbers():
#   for i in range(5):
#     print(f"Number: {i}")
#     time.sleep(1)

# def print_letters():
#   for letter in ['A', 'B', 'C', 'D', 'E']:
#     print(f"Letter: {letter}")
#     time.sleep(1)
    
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # 启动线程
# thread1.start()
# thread2.start()

# # 等待线程完成
# thread1.join()
# thread2.join()

# # 打印线程完成，主线程会被阻塞，直到线程完成
# print("Threads have finished execution.")

# def cpu_task():
#   print(f'{threading.current_thread().name} is running')
#   time.sleep(1)
#   print(f'{threading.current_thread().name} is finished')
  
# threads = [threading.Thread(target=cpu_task) for _ in range(5)]

# for thread in threads:
#   thread.start()

# for thread in threads:
#   thread.join()

# print(f'{threading.current_thread().name} is finished')


# 多线程的锁
# lock = threading.Lock()

# def task():
#   # 获取锁
#   lock.acquire()
#   print(f'{threading.current_thread().name} is running')
#   time.sleep(1)
#   print(f'{threading.current_thread().name} is finished')
#   # 释放锁
#   lock.release()
  
# threads = [threading.Thread(target=task) for _ in range(5)]

# for thread in threads:
#   thread.start()

# for thread in threads:
#   thread.join()

# print(f'{threading.current_thread().name} is finished')

# 线程间的通信
def producer(q):
    for i in range(5):
        item = f"item-{i}"
        print(f"Producing {item}")
        q.put(item)
        time.sleep(1)

def consumer(q):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consuming {item}")
        q.task_done()

q = queue.Queue()
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

producer_thread.join()
q.put(None)  # Signal the consumer to exit
consumer_thread.join()


# 线程池
def task(n):
    print(f"Task {n} is running")
    time.sleep(1)
    return f"Task {n} is finished"

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for future in futures:
        print(future.result())
