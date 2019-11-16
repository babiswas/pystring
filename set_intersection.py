from collections import Counter

def rem_char(str1,str2):
    d=Counter(str1)
    e=Counter(str2)
    k1=d.keys()
    k2=e.keys()
    s1=set(k1)
    common_key=len(s1.intersection(k2))
    if common_key==0:
        return len(k1)+len(k2)
    else:
        return max(len(k1),len(k2))-common_key


if __name__=="__main__":
   print(rem_char("bcadeh","hea"))
   


