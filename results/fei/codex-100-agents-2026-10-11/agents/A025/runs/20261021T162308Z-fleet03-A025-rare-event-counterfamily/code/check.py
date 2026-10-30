"""A025 continuation certificate v1. No external writes; exact rational arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache
import json, time, hashlib

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
OUT.mkdir(exist_ok=True)
PI=(Q(1,2),Q(1,4),Q(1,4))
checks=0
def check(x):
    global checks
    checks+=1
    assert x, checks
def save(name,obj):
    (OUT/name).write_text(json.dumps(obj,indent=2,default=str)+'\n',encoding='utf-8',newline='')

def ln2_bounds():
    z=Q(1,3); v=z; s=Q(0)
    for j in range(40): s+=2*v/(2*j+1); v/=9
    return s,s+2*v/(81*(1-z*z))
L2=ln2_bounds()
@lru_cache(None)
def log2_bounds(x):
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    z=(x-1)/(x+1); v=z; s=Q(0)
    for j in range(40): s+=2*v/(2*j+1); v*=z*z
    tail=2*v/(81*(1-z*z))
    return k+s/L2[1],k+(s+tail)/L2[0]
def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,q): return a[0]*q,a[1]*q
def sub(a,b): return a[0]-b[1],a[1]-b[0]
def fwht(f):
    a=list(f); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h): u,v=a[i],a[i+h]; a[i]=u+v; a[i+h]=u-v
        h*=2
    return a
def entropy(f):
    n=len(f); ans=(Q(0),Q(0))
    for v,c in Counter(abs(x) for x in fwht(f)).items():
        if v:
            p=Q(v*v,n*n); lo,hi=log2_bounds(1/p)
            ans=add(ans,(c*p*lo,c*p*hi))
    return ans
def infs(f):
    return [Q(sum(f[j]!=f[j^(1<<i)] for j in range(len(f))),len(f)) for i in range(len(f).bit_length()-1)]
def influence(f): return sum(infs(f),Q(0))
def restrict(f,i,b):
    return [v for j,v in enumerate(f) if (j>>i)&1==b]
def bank(cores):
    return sum((2*PI[j]*PI[k]*influence([u*v for u,v in zip(cores[j],cores[k])]) for j in range(3) for k in range(j+1,3)),Q(0))
def terminal(cores):
    it=sum((p*influence(g) for p,g in zip(PI,cores)),Q(0))
    ht=(Q(0),Q(0))
    for p,g in zip(PI,cores): ht=add(ht,scale(entropy(g),p))
    return it,ht,(8*it-ht[1],8*it-ht[0])
def actual(cores):
    n=len(cores[0]); f=[]
    for b in range(2):
        for a in range(2):
            label=0 if a else (1 if b else 2)
            f.extend(cores[label])
    return f
def erasure(f,i):
    a=fwht(f); N=len(f); ans=(Q(0),Q(0))
    for s in range(N):
        if (s>>i)&1: continue
        p=Q(a[s]**2,N*N); q=Q(a[s|(1<<i)]**2,N*N)
        if p and q:
            ans=add(ans,scale(log2_bounds((p+q)/p),p))
            ans=add(ans,scale(log2_bounds((p+q)/q),q))
    return ans

def build(m,t):
    # Bit order: y[0:m], x, z, activation[0:t], then A,B.
    cores=[[],[],[]]; mask=(1<<m)-1
    for j in range(1<<(m+2+t)):
        y=j&mask; x=(j>>m)&1; z=1-2*((j>>(m+1))&1)
        b=1-2*(sum(((y>>i)&1)*((y>>(i+1))&1) for i in range(0,m,2))%2)
        active=(j>>(m+2))==0
        for k in range(3):
            v=z*b*(-1 if k and x==0 and y==k-1 else 1)
            cores[k].append(v if active else 1)
    return cores

def run():
    start=time.perf_counter(); rows=[]
    # Direct physical reconstruction, without importing A021 or old A025 helpers.
    for m in (4,6,8):
        for t in (0,1):
            delta=Q(1,2**m); p=Q(1,2**t); cores=build(m,t)
            f=actual(cores); xchildren=[[restrict(g,m,b) for g in cores] for b in (0,1)]
            c0,c1=xchildren; f0=actual(c0)
            ychildren=[[restrict(g,0,b) for g in c0] for b in (0,1)]
            itx,htx,sx=terminal(c0); ity,hty,sy=(Q(0),(Q(0),Q(0)),(Q(0),Q(0)))
            ty=[terminal(c) for c in ychildren]
            for cs,tr in zip(ychildren,ty):
                ff=actual(cs); ic=sum(infs(ff)[-2:])
                cb=sub(entropy(ff),tr[1])
                check(ic==2*p*delta)
                check(cb[1]<bank(cs)+6*ic)
            ity=sum((v[0]/2 for v in ty),Q(0)); hty=scale(add(ty[0][1],ty[1][1]),Q(1,2))
            d=infs(f0)[0]; D=sub(entropy(f0),scale(add(entropy(actual(ychildren[0])),entropy(actual(ychildren[1]))),Q(1,2)))
            check(d==p*(Q(1,2)+delta)); check(D[1]<5*d)
            check(bank(c0)-sum((bank(c)/2 for c in ychildren),Q(0))==p*delta)
            check(ity==p*(Q(m+1,2)+(m-2)*delta+t))
            # Whole physical leaf partition: x=1, (x=0,y0=0), (x=0,y0=1).
            it1,ht1,s1=terminal(c1)
            S=add(scale(s1,Q(1,2)),scale(add(ty[0][2],ty[1][2]),Q(1,4)))
            R=sum((bank(c)*w for c,w in [(c1,Q(1,2)),(ychildren[0],Q(1,4)),(ychildren[1],Q(1,4))]),Q(0))
            check(S[0]>=p*(3*m+1+4*t))
            oldR=p*(3*m-1+3*t)*delta/4
            check(R==p*(3*m-3+3*t)*delta/4)
            check(oldR<=delta*S[0]/4)
            Dx=sub(entropy(f),scale(add(entropy(f0),entropy(actual(c1))),Q(1,2)))
            U=max(Q(0),Dx[1]-10*p*delta/2)
            check(U<=delta*S[0]/6)
            check(R+U<=5*delta*S[0]/12)
            # Full tree telescope with all leaves and full terminals.
            itnew=it1/2+ity/2
            check(10*influence(f)-entropy(f)[1]>=2*itnew+(1-5*delta/12)*S[0])
            # The next partner coordinate y1 now occupies bit0, all original labels retained.
            reb=actual(ychildren[0]); dr=infs(reb)[0]; Br=erasure(reb,0)
            check(dr==p*delta)
            check(Br[0]>p*delta*(Q(3,2)+Q(m,4)))
            rcs=[[restrict(g,0,b) for g in ychildren[0]] for b in (0,1)]
            check(bank(ychildren[0])-sum((bank(c)/2 for c in rcs),Q(0))==Q(3,2)*dr)
            rows.append({'m':m,'activation_width':t,'second_query_influence':str(d),'second_decrement_interval':list(map(str,D)), 'remaining_bank':str(R),'terminal_surplus_lower':str(S[0]),'first_query_debit_upper':str(U),'rebound_B_interval':list(map(str,Br)),'rebound_d':str(dr)})
            save('DIRECT.json',{'status':'RUNNING','rows':rows,'assertions':checks})
    scalar=[]
    for m in range(4,102,2):
        for t in (0,m,3*m+1):
            delta=Q(1,2**m); p=Q(1,2**t)
            S=p*(3*m+1+4*t); Rold=p*(3*m-1+3*t)*delta/4; U=p*m*delta/2
            Rnew=Rold-p*delta/2
            check(Rold<=delta*S/4); check(U<=delta*S/6); check(Rnew>=0)
            check(5*delta/12<=Q(5,192)); check(Rnew+U<=5*delta*S/12)
            scalar.append({'m':m,'t':t,'S_lower':str(S),'old_bank':str(Rold),'new_bank':str(Rnew),'U_bound':str(U)})
    save('SCALAR.json',{'status':'PASS','cases':len(scalar),'rows':scalar})
    save('DIRECT.json',{'status':'PASS','cases':len(rows),'rows':rows,'assertions':checks,'seconds':time.perf_counter()-start,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    print(json.dumps({'status':'PASS','direct_cases':len(rows),'scalar_cases':len(scalar),'assertions':checks,'seconds':time.perf_counter()-start}))

if __name__=='__main__': run()
