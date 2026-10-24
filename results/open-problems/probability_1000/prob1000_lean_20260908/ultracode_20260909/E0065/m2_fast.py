import numpy as np
def analyse(a,mb,c):
    A=a-mb+c; B=mb-2*c; C=c
    r=np.roots([A,B-1,C]); r=[x.real for x in r if abs(x.imag)<1e-10 and -1e-9<=x.real<=1+1e-9]
    p=r[0]; fpr=2*A*p+B
    f=np.poly1d([A,B,C]); g=f(f)-np.poly1d([1,0]); h=f-np.poly1d([1,0])
    q,_=np.polydiv(g,h)
    two=[x.real for x in np.roots(q) if abs(x.imag)<1e-9 and -1e-9<=x.real<=1+1e-9]
    return p,fpr,len(two)>0
def exists(al,conv,crit,nb=801):
    for b in np.linspace(al,1-al,nb):
        mb=2*b if conv==1 else b
        for (a,c) in [(al,1-al),(1-al,al)]:
            p,fpr,two=analyse(a,mb,c)
            if (abs(fpr)>=1 if crit=='L' else two): return True
    return False
for conv in (1,2):
    for crit in ('L','G'):
        lo,hi=0.01,0.5
        for _ in range(40):
            mid=(lo+hi)/2
            if exists(mid,conv,crit): lo=mid
            else: hi=mid
        print("conv",conv,"crit",crit,"sup alpha (a,c at extremes):",lo)
print("(3-sqrt7)/2 =",(3-7**0.5)/2,"  (3-sqrt7)/4 =",(3-7**0.5)/4)
