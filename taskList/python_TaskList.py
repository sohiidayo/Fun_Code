#任务队列
import threading  
from queue import Queue  
import time
class Task:  
    def __init__(self, task_id):  
        self.task_id = task_id  
  
    def execute(self):  
        print(f"开始执行任务 {self.task_id}")  
        # 这里可以添加耗时操作，但在这个例子里我们只是打印  
        
        time.sleep(2)


        print(f"任务 {self.task_id} 完成")  
  
# 工作线程类  
class Worker(threading.Thread):  
    def __init__(self, task_queue):  
        threading.Thread.__init__(self)  
        self.task_queue = task_queue  
        self.daemon = True  
        self.start()  
  
    def run(self):  
        while True:  
            task = self.task_queue.get()  
            if task is None:  # 队列中的None表示线程应该退出  
                self.task_queue.task_done()  
                break  
            task.execute()  
            self.task_queue.task_done()  
  
def main():  
    task_queue = Queue()  
  
    # 创建并启动工作线程  
    for _ in range(5):  # 假设我们创建5个工作线程  
        Worker(task_queue)  
  
    try:  
        while True:  
            task_id = input("请输入任务ID（输入q退出）: ")  
            if task_id.lower() == 'q':  
                break  
            task = Task(task_id)  
            task_queue.put(task)  
            print(f"任务 {task_id} 已加入队列")  
  
    except (KeyboardInterrupt, EOFError):  
        print("用户中断，程序将退出。")  
  
    # 向队列中添加None以通知工作线程退出  
    for _ in range(5):  
        task_queue.put(None)  
  
    # 等待所有任务完成  
    task_queue.join()  
  
    print("所有任务都已完成，程序将退出。")  
  
if __name__ == "__main__":  
    main()