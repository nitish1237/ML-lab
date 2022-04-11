import numpy as np
import pandas as pd
data=pd.read_csv("data.csv")
print(data,"\n")

d=np.array(data)[:,:-1]
print("\n The attributes are: ",d)
target=np.array(data)[:,-1]
print("\n Target is ",target)


def finds(c,t):
    for i,val in enumerate(t):
        if val=="yes":
            s=c[i].copy()
            break
            
    for i,val in enumerate(c):
        if t[i]=="yes":
            for x in range(len(s)):
                if val[x]!=s[x]:
                    s[x]='?'
                else:
                    pass
    return s

print("final hypothesis",finds(d,target))
