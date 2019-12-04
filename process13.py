import multiprocessing as mp
import time

def foo():
  name=mp.current_process().name
  print(f"Starting {name}")
  time.sleep(3)
  print(f"Exiting {name}")

if __name__=="__main__":
  background_process=mp.Process(name="Background_process",target=foo)
  background_process.daemon=True
  No_background_process=mp.Process(name="No_background_process",target=foo)
  No_background_process.daemon=False
  background_process.start()
  No_background_process.start()
  background_process.join()
  No_background_process.join()


  
