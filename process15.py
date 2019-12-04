import multiprocessing as mp


class MyProcess(mp.Process):
     def run(self):
        print(f"Called the run method {self.name}")
        return

if __name__=="__main__":
   jobs=[]
   for i in range(5):
       p=MyProcess()
       jobs.append(p)
       p.start()
       p.join()
