import multiprocessing as mp
import test

if __name__=="__main__":
   jobs=[]
   for i in range(0,5):
      p=mp.Process(target=test.function,args=(i,))
      jobs.append(p)
      p.start()
      p.join()
