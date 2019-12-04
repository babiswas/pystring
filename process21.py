import multiprocessing as mp

def worker(dictionary,key,item):
    dictionary[key]=item

if __name__=="__main__":
   mgr=mp.Manager()
   dictionary=mgr.dict()
   jobs=[mp.Process(target=worker,args=(dictionary,i,i*2)) for i in range(20)]
   for j in jobs:
      j.start()
   for j in jobs:
      j.join()
   print("Results:",dictionary)
