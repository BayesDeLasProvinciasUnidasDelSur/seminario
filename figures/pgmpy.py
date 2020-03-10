d = [0.15, 0.85]
p = [0.70, 0.30]
r = [[ [0.30, 0.70], [0.02, 0.20] ],
     [ [0.40, 0.25], [0.08, 0.30] ],
     [ [0.30, 0.05], [0.90, 0.50] ]]

c = [[0.95, 0.20],
     [0.05, 0,80]]

a = [[0.99, 0.40, 0.10],
     [0.01, 0.60, 0.90]]


def Pr(k):
    res = 0
    for i in range(len(d)):
        for j in range(len(p)):
            res += d[i]*p[j]*r[k][i][j]
    return res

def Pr_p0(k):
    res = 0
    for i in range(len(d)):
        res += d[i]*p[0]*r[k][i][0]
    return res

Pr_p0(1)/p[0]

def Pa(m):
    res = 0
    for k in range(len(r)):
        res += a[m][k]*Pr(k)
    return res
        
Pa(1)

"""
import numpy as np        
m = {}
m['d']=np.array(d)
m['p']=np.array(p)
m['r']=np.array(r)
m['c']=np.array(c)
m['a']=np.array(a)
"""