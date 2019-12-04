import multiprocessing as mp

def function(i):
   print(f"Called function will process {i}")
   return

if __name__=="__main__":
   jobs=[]
   for i in range(5):
     p=mp.Process(target=function,args=(i,))
     jobs.append(p)
     p.start()
     p.join()
