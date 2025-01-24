from multiprocessing import Process, Queue, Pool
import os

# 简单的多进程
# def worker(target_name):
#   print(f'{target_name} is running in {os.getpid()}')

# if __name__ == '__main__':
#   print(f'{os.getpid()} is running')
#   # 创建进程
#   process = Process(target=worker, args=('Task1',))
#   process1 = Process(target=worker, args=('Task2',))
#   # 启动进程
#   process.start()
#   process1.start()
#   # 等待进程完成
#   process.join()
#   process1.join()
#   print(f'{os.getpid()} is finished')


# 进程池
# def worker(x):
#   print(f'{os.getpid()} is running Process')
#   return x * x

# if __name__ == '__main__':
#   with Pool(processes=4) as pool:
#     result = pool.map(worker, range(5))
#     print(result)
#   print(f'{os.getpid()} is finished Main')
  

# 进程间的通信
def producer(queue):
  for i in range(5):
    queue.put(i)
    print(f'{os.getpid()} is producing {i}')

def consumer(queue):
  while not queue.empty():
    item = queue.get()
    print(f'{os.getpid()} is consuming {item}')

if __name__ == '__main__':
  queue = Queue()
  producer_process = Process(target=producer, args=(queue,))
  consumer_process = Process(target=consumer, args=(queue,))
  producer_process.start()
  consumer_process.start()
  producer_process.join()
  consumer_process.join()
  print(f'{os.getpid()} is finished Main')
