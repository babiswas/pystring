import multiprocessing as mp
from multiprocessing import Barrier,Lock,Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer,serializer):
    name=mp.current_process().name
    synchronizer.wait()
    now=time()
    with serializer:
      print(f"Process {name} and {datetime.fromtimestamp(now)}")


def test_without_barrier(synchronizer,serializer):
    name=mp.current_process().name
    synchronizer.wait()
    now=time()
    with serializer:
      print(f"Process {name} and {datetime.fromtimestamp(now)}")

if __name__=="__main__":
   synchronizer=Barrier(2)
   serializer=Lock()
   Process(name="P1-Test with barrier",target=test_with_barrier,args=(synchronizer,serializer)).start()
   Process(name="P2-Test with barrier",target=test_with_barrier,args=(synchronizer,serializer)).start()
   Process(name="P3-Test without barrier",target=test_without_barrier,args=(synchronizer,serializer)).start()
   Process(name="P4-Test without barrier",target=test_without_barrier,args=(synchronizer,serializer)).start()
   
