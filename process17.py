import multiprocessing as mp

def create_items(pipe):
    output_pipe=pipe
    for item in range(10):
       output_pipe.send(item)
    out_pipe.close()

def multiply_items(pipe_1,pipe_2):
      close,input_pipe=pipe_1
      close.close()
      output_pipe,_=pipe2
      try:
        while True:
           item=input_pipe.recv()
           output_pipe.send(item*item)
        except EOFError:
           output_pipe.close()

if __name__=="__main__":
   pipe_1=mp.Pipe(True)
   p1=mp.Process(target=create_items,args(pipe_1,))
   p1.start()
   pipe_2=mp.Pipe(True)
   p2=mp.Process(target=multiply_items,args(pipe_2,))
   p2.start()

