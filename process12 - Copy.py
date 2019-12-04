import multiprocessing as mp
import time

def foo():
  name=mp.current_process().name
  print(f"Starting {name}")
  time.sleep(3)
  print(f"Exiting {name}")

if __name__=="__main__":
   process_name=mp.Process(name='foo_process',target=foo)
   process_name.daemon=True
   process_default_name=mp.Process(target=foo)
   process_name.start()
   process_default_name.start()
   process_name.join()
   process_default_name.join()

   
   
   
