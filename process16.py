import multiprocessing as mp
import random
import time

class Producer(mp.Process):
    def __init__(self,queue):
        mp.Process.__init__(self)
        self.queue=queue
    def run(self):
       while True:
          item=random.randint(0,256)
          self.queue.put(item)
          print(f"Process producer: item{item} appended to queue {self.name}")
          time.sleep(1)
          print(f"The size of the queue is {self.queue.qsize()}")


class Consumer(mp.Process):
   def __init__(self,queue):
      mp.Process.__init__(self)
      self.queue=queue
   def run(self):
      while True:
         if (self.queue.empty()):
            print("The queue is empty")
         else:
            time.sleep(2)
            item=self.queue.get()
            print(f"Process consumer:item {item} popped from by {self.name}")
            time.sleep(1)

if __name__=="__main__":
   queue=mp.Queue()
   producer=Producer(queue)
   consumer=Consumer(queue)
   producer.start()
   consumer.start()
   producer.join()
   consumer.join()




   

