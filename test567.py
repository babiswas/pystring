from itertools import groupby

def remov_dup(str1):
    str2=[]
    for key,val in groupby(str1):
      str2.append(key)
    return ''.join(str2)

if __name__=="__main__":
   print(remov_dup('aaaaabbbbbb'))

       