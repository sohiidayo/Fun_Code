#�������
import threading  
from queue import Queue  
import time
class Task:  
    def __init__(self, task_id):  
        self.task_id = task_id  
  
    def execute(self):  
        print(f"��ʼִ������ {self.task_id}")  
        # ���������Ӻ�ʱ�����������������������ֻ�Ǵ�ӡ  
        
        time.sleep(2)


        print(f"���� {self.task_id} ���")  
  
# �����߳���  
class Worker(threading.Thread):  
    def __init__(self, task_queue):  
        threading.Thread.__init__(self)  
        self.task_queue = task_queue  
        self.daemon = True  
        self.start()  
  
    def run(self):  
        while True:  
            task = self.task_queue.get()  
            if task is None:  # �����е�None��ʾ�߳�Ӧ���˳�  
                self.task_queue.task_done()  
                break  
            task.execute()  
            self.task_queue.task_done()  
  
def main():  
    task_queue = Queue()  
  
    # ���������������߳�  
    for _ in range(5):  # �������Ǵ���5�������߳�  
        Worker(task_queue)  
  
    try:  
        while True:  
            task_id = input("����������ID������q�˳���: ")  
            if task_id.lower() == 'q':  
                break  
            task = Task(task_id)  
            task_queue.put(task)  
            print(f"���� {task_id} �Ѽ������")  
  
    except (KeyboardInterrupt, EOFError):  
        print("�û��жϣ������˳���")  
  
    # ����������None��֪ͨ�����߳��˳�  
    for _ in range(5):  
        task_queue.put(None)  
  
    # �ȴ������������  
    task_queue.join()  
  
    print("������������ɣ������˳���")  
  
if __name__ == "__main__":  
    main()