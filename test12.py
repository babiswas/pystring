import multiprocessing as mp
from cla import A

def calc_square(numbers,q):
    for n in numbers:
       q.put(n)

if __name__=="__main__":
   a1=A(12)
   a2=A(3)
   a3=A(4)
   numbers=[a1,a2,a3]
   q=mp.Queue()
   p=mp.Process(target=calc_square,args=(numbers,q))
   p.start()
   p.join()
   while q.empty() is False:
       print(q.get())