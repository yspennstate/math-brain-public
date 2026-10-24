from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import prod,lcm,comb
import json,hashlib,time,sys
ROOT=Path(__file__).resolve().parents[1]
VERSION='A073-exact-refund-review/1'
START=time.perf_counter();CHECKS=0

def ck(ok,detail=''):
    global CHECKS
    CHECKS+=1
    if not ok:raise AssertionError((CHECKS,detail))
    if time.perf_counter()-START>55:raise RuntimeError('Frozen 55-second job cap exceeded')

def serial(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [serial(v) for v in x]
    return x

def save(name,value):
    (ROOT/'out').mkdir(exist_ok=True)
    (ROOT/'out'/name).write_text(json.dumps(serial(value),indent=2)+'\n',encoding='utf-8')

@lru_cache(None)
def factor(n):
    if n<1:raise ValueError('Positive factor input required')
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p=3 if p==2 else p+2
    if n>1:out[n]=out.get(n,0)+1
    return out

def combine(*terms):
    out={}
    for weight,form in terms:
        for prime,c in form.items():out[prime]=out.get(prime,F(0))+weight*c
    return {p:F(c) for p,c in out.items() if c}

def lg(q,weight=F(1)):
    q=F(q);weight=F(weight)
    if q<=0:raise ValueError('Positive log argument required')
    return combine((weight,factor(q.numerator)),(-weight,factor(q.denominator)))

def product_sign(form):
    if not form:return {'sign':0,'denominator':1,'exponents':{},'bit_budget':0}
    L=lcm(*(c.denominator for c in form.values()))
    exps={p:int(c*L) for p,c in form.items()}
    estimate=sum(abs(e)*p.bit_length() for p,e in exps.items())
    ck(estimate<=1000000,'product budget')
    U=prod(p**e for p,e in exps.items() if e>0)
    V=prod(p**(-e) for p,e in exps.items() if e<0)
    return {'sign':(U>V)-(U<V),'denominator':L,'exponents':exps,'bit_budget':estimate,
       'U_hex':format(U,'x'),'V_hex':format(V,'x')}

@lru_cache(None)
def reduced_ln(t,N=40):
    t=F(t);ck(1<=t<=2,'log range')
    y=(t-1)/(t+1)
    lower=2*sum((y**(2*j+1)/F(2*j+1) for j in range(N)),F(0))
    tail=2*y**(2*N+1)/(F(2*N+1)*(1-y*y))
    return lower,lower+tail

@lru_cache(None)
def log_bounds(x,N=40):
    x=F(x);ck(x>0);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    if x==1:return F(k),F(k)
    a,b=reduced_ln(x,N);c,d=reduced_ln(F(2),N)
    return k+a/d,k+b/c

def bounds(form,N=40):
    lo=hi=F(0)
    for p,coef in form.items():
        a,b=log_bounds(F(p),N)
        if coef<0:a,b=b,a
        lo+=coef*a;hi+=coef*b
    return lo,hi

def decimal_interval(interval,digits=30):
    a,b=interval;scale=10**digits;a*=scale;b*=scale
    low=a.numerator//a.denominator
    high=-((-b.numerator)//b.denominator)
    def string(i):return ('-' if i<0 else '')+str(abs(i)//scale)+'.'+str(abs(i)%scale).zfill(digits)
    return {'lower':string(low),'upper':string(high),'lower_rational':F(low,scale),
      'upper_rational':F(high,scale),'digits':digits,'width':F(high-low,scale)}

def spectrum(table,direct=False):
    N=len(table);n=N.bit_length()-1
    ck(N==1<<n and all(x in (-1,1) for x in table))
    W=list(table);step=1
    while step<N:
        for start in range(0,N,step*2):
            for j in range(start,start+step):W[j],W[j+step]=W[j]+W[j+step],W[j]-W[j+step]
        step*=2
    ck(sum(w*w for w in W)==N*N,'Parseval')
    inverse=W[:];step=1
    while step<N:
        for start in range(0,N,step*2):
            for j in range(start,start+step):inverse[j],inverse[j+step]=inverse[j]+inverse[j+step],inverse[j]-inverse[j+step]
        step*=2
    ck(inverse==[N*x for x in table],'signed inverse')
    if direct:
        ck(W==[sum(table[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)],'direct characters')
    p={s:F(w*w,N*N) for s,w in enumerate(W) if w}
    e=[]
    for i in range(n):
        physical=F(sum(table[x]!=table[x^(1<<i)] for x in range(N)),N)
        ck(physical==sum(m for s,m in p.items() if s>>i&1),'physical influence')
        e.append(physical)
    return p,e,W

def edge_forms(p,n,e,save_joint=False):
    I=sum(e,F(0));M={};ID={};tail={};levels={};rows=[];joint_P={};joint_Q={}
    for i in range(n):
        bit=1<<i;r={}
        for s,mass in p.items():r[s&~bit]=r.get(s&~bit,F(0))+mass
        ck(sum(r.values())==1,'complete residual normalizer')
        rowM={};rowD={};mu={}
        for t,r_mass in r.items():
            upper=p.get(t|bit,F(0))
            if e[i]:
                joint_Q[i,t]=e[i]*r_mass/I
                if upper:
                    mu[t]=upper/e[i];joint_P[i,t]=upper/I
                    rowD=combine((1,rowD),(1,lg(mu[t]/r_mass,mu[t])))
            if upper:
                term=lg(r_mass/upper,upper);rowM=combine((1,rowM),(1,term))
                level=t.bit_count();levels[level]=combine((1,levels.get(level,{})),(1,term))
                if t.bit_count()>=2:tail=combine((1,tail),(1,term))
        if e[i]:
            ck(sum(mu.values())==1,'derivative normalizer')
            ck(rowM==combine((1,lg(1/e[i],e[i])),(-e[i],rowD)),'row rarity refund')
        else:ck(rowM==rowD=={})
        M=combine((1,M),(1,rowM));ID=combine((1,ID),(e[i],rowD))
        rows.append({'i':i,'M':rowM,'D':rowD,'mu':mu,'r':r})
    if I:
        ck(sum(joint_P.values())==sum(joint_Q.values())==1,'joint normalizers')
        direct={}
        for key,Pmass in joint_P.items():
            ck(joint_Q[key]>0,'finite KL support')
            direct=combine((1,direct),(1,lg(Pmass/joint_Q[key],I*Pmass)))
        ck(direct==ID,'joint KL direct versus conditional')
        for i in range(n):
            ck(sum(v for (j,t),v in joint_P.items() if j==i)==e[i]/I,'P coordinate marginal')
            ck(sum(v for (j,t),v in joint_Q.items() if j==i)==e[i]/I,'Q coordinate marginal')
        rarity=combine(*[(1,lg(1/x,x)) for x in e if x])
        ck(M==combine((1,rarity),(-1,ID)),'joint refund')
    else:ck(M==ID=={} and not joint_P and not joint_Q)
    result={'I':I,'M':M,'ID':ID,'rows':rows,'tail':tail,'levels':levels}
    if save_joint:result['joint']={'P':[[i,t,v] for (i,t),v in joint_P.items()],
                               'Q':[[i,t,v] for (i,t),v in joint_Q.items()]}
    return result

