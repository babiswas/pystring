import multiprocessing as mp
import time

def foo():
  print("Starting Function")
  time.sleep(0.1)
  print("Finished Function")

if __name__=="__main__":
   p=mp.Process(target=foo)
   print(f"Process before execution{p},{p.is_alive()}")
   p.start()
   print(f"Process before execution{p},{p.is_alive()}")
   p.terminate()
   print(f"Process before execution{p},{p.is_alive()}")
   p.join()

   