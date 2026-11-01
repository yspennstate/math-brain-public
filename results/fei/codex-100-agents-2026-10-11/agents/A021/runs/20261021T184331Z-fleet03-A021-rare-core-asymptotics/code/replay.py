"""No production/A025 helper imports. Direct DFT and physical products."""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1]; checks=0
def ck(p):
    global checks
    checks+=1
    assert p,checks
def log(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    y=x/F(2)**k
    if y<1: k-=1; y*=2
    def ln(y):
        z=(y-1)/(y+1); term=z; s=F(0)
        for j in range(48): s+=2*term/(2*j+1); term*=z*z
        return s,s+2*term/(97*(1-z*z))
    a,b=ln(y); c,d=ln(F(2))
    return k+a/d,k+b/c
def ent(f):
    N=len(f); freq=Counter(abs(sum(v*(-1 if (j&s).bit_count()%2 else 1) for j,v in enumerate(f))) for s in range(N))
    lo=hi=F(0)
    for a,count in freq.items():
        if a:
            p=F(a*a,N*N); l,u=log(1/p); lo+=count*p*l; hi+=count*p*u
    return lo,hi
def influences(f):
    return [F(sum(f[j]!=f[j^(1<<i)] for j in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)]
def influence(f): return sum(influences(f),F(0))
def fixed(f,i,b): return [v for j,v in enumerate(f) if j>>i&1==b]
pi=(F(1,2),F(1,4),F(1,4))
def bank(gs):
    return sum((2*pi[i]*pi[j]*influence([u*v for u,v in zip(gs[i],gs[j])]) for i in range(3) for j in range(i)),F(0))
def actual(gs): return gs[2]+gs[0]+gs[1]+gs[0]
def run():
    start=time.perf_counter(); results=[]
    for t in (0,1):
        gs=[[],[],[]]
        for a in range(2**t):
          for z in (1,-1):
           for x in (0,1):
            for y in range(16):
             b=(-1)**(((y&1)*((y>>1)&1))+(((y>>2)&1)*((y>>3)&1)))
             for label in range(3):
              edited=label>0 and x==0 and y==label-1
              gs[label].append(1 if a else z*b*(-1 if edited else 1))
        x0=[fixed(g,4,0) for g in gs]; x1=[fixed(g,4,1) for g in gs]
        ychildren=[[fixed(g,0,a) for g in x0] for a in (0,1)]
        pairchildren=[[[fixed(g,0,b) for g in cs] for b in (0,1)] for cs in ychildren]
        leaves=[(F(1,2),x1)]+[(F(1,8),cs) for pair in pairchildren for cs in pair]
        p=F(1,2**t); delta=F(1,16)
        for a in (0,1):
            ck(influences(actual(ychildren[a]))[0]==p*(delta if a==0 else 1-delta))
            ck(bank(ychildren[a])-sum((bank(c)/2 for c in pairchildren[a]),F(0))==3*p*delta/2)
        It=sum((w*q*influence(g) for w,cs in leaves for q,g in zip(pi,cs)),F(0))
        ht=[F(0),F(0)]
        for w,cs in leaves:
          for q,g in zip(pi,cs):
            h=ent(g); ht[0]+=w*q*h[0]; ht[1]+=w*q*h[1]
        S=8*It-ht[1]; rb=sum((w*bank(cs) for w,cs in leaves),F(0))
        ck(It==p*(F(5,2)+delta+t)); ck(rb==p*(6+3*t)*delta/4)
        ck(S>p*(14+4*t))
        f=actual(gs); H=ent(f)
        ck(10*influence(f)-H[1]>=2*It+(1-delta/2)*S)
        results.append({'t':t,'It':str(It),'R3':str(rb),'S3_lower':str(S)})
    obj={'status':'PASS','cases':2,'assertions':checks,'seconds':time.perf_counter()-start,'rows':results}
    (R/'out/REPLAY.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='')
    print(json.dumps({k:v for k,v in obj.items() if k!='rows'}))
if __name__=='__main__': run()
