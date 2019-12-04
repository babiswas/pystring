import multiprocessing as mp

def function_square(data):
   result=data*data
   return result

if __name__=="__main__":
  inputs=list(range(0,100))
  pool=mp.Pool(processes=4)
  pool_output=pool.map(function_square,inputs)
  pool.close()
  pool.join()
  print('Pool :',pool_output)

  