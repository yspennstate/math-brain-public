"""Positive strict irreducible bridge profiles and scalar baseline mass."""
import math
from collections import Counter
def profiles(cutoff):
    out=[];counts=[0]*(cutoff+2)
    def visit(word,height,maximum):
        if len(word)==cutoff:return
        for step in (1,-1):
            new=height+step
            if new<=0:continue
            full=word+(step,);record=new>maximum
            if record and all(counts[k]>=2 for k in range(1,new)):
                out.append((full,new))
            counts[new]+=1;visit(full,new,max(maximum,new));counts[new]-=1
    visit((),0,0)
    return sorted(out,key=lambda item:(len(item[0]),item[0]))
def scalar_total_float(d,a,z):
    b=d/a;c=math.sqrt(1-4*b*b);rp=(1+c)/2;rm=(1-c)/2
    q=rm/rp;y=b*z/rp
    assert y>1 and y*q<1
    value=sum(y*q**k/(1-y*q**k) for k in range(40))*c
    return value/(1+value)
def scalar_short_float(words,d,a,z):
    return sum((d/a)**len(word)*z**height for word,height in words)
