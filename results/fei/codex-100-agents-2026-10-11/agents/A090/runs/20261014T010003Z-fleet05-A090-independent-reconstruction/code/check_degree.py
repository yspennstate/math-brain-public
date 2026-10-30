from pathlib import Path
from fractions import Fraction as F
from math import comb
import json,time,sys

start=time.perf_counter();checks=0
def check(x):
    global checks
    assert x
    checks+=1
def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for j,y in enumerate(b):
        if y:
            for i,x in enumerate(a):out[i+j]+=x*y
    return out

ws=[4] if '--pilot' in sys.argv else [4,5,6,7]
records=[]
for w in ws:
    m=2**w;n=m*w;p=F(1,m);beta=1-p
    # Exact squared Fourier polynomial of one Boolean factor 1-A_w.
    C=[comb(w,t) for t in range(w+1)];C[0]=(m-1)**2
    power=[1]
    for j in range(m-1):power=conv(power,C)
    allpower=conv(power,C)
    den=m*(m-1)
    nu=[F(x,den**m) for x in allpower]
    U=[comb(w-1,t) for t in range(w)]
    mupoly=conv(power,U)
    mu=[F(x,2**(w-1)*den**(m-1)) for x in mupoly]
    # Independent direct residual-pair polynomial, including the vacuum reset.
    R=[2*comb(w-1,t) for t in range(w)];R[0]=(m-1)**2+1
    rpoly=conv(power,R)
    row=[F(4*x,m**(2*m)) for x in rpoly]
    row[0]+=1-4*beta**m
    W=[4*beta**m*x for x in nu];W[0]=(1-2*beta**m)**2
    eps=2*p*beta**(m-1);I=2*w*beta**(m-1)
    check(sum(W)==1);check(sum(mu)==1);check(sum(row)==1);check(sum(nu)==1)
    check(I==n*eps);check(sum(F(t)*v for t,v in enumerate(W))==I)
    check(mu[0]==eps);check(row[0]>=F(1,16));check(eps<=p)
    check(beta**m>=F(1,4));check(beta**m<F(3,8));check(beta**(m-1)<=F(1,2))
    mean=sum(t*v for t,v in enumerate(mu));check(mean==F(2*w-1,2))
    tail=sum(mu[n//2+1:],F(0));check(tail<=F(2,m))
    zero=negativezero=0
    for t,(u,r) in enumerate(zip(mu,row)):
        check(r>0);check(u>0)
        check(u==F(t+1)*W[t+1]/I)
        check(r==(1-F(t,n))*W[t]+F(t+1,n)*W[t+1])
        check(r>=eps*u)
        if t==0:
            check(u<=r);negativezero+=1
        else:
            check(u<=(2*p/beta+2*beta*t)*nu[t])
            check(r>=4*beta**m*(1-F(t,n))*nu[t])
            if t<=n//2:check(u<=4*(t+1)*r)
        check(time.perf_counter()-start<60)
    records.append({'w':w,'m':m,'n':n,'residual_degrees':len(mu),
       'mean_derivative_degree':str(mean),'tail_mass_bound':str(F(2,m)),
       'all_pointwise_certificate_checks':'PASS'})
out={'status':'PASS','assertions':checks,'families':len(ws),'residual_degree_packets':sum(x['residual_degrees'] for x in records),
     'arithmetic':'integer polynomial convolution and Fraction; no numerical logarithm signs',
     'elapsed_seconds':time.perf_counter()-start,'records':records,
     'analytic_result':'D_degree<=3+log2(w+1/2); retained degree-only cost/I>=w-4-log2(w+1/2)'}
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(Path(__file__).resolve().parents[1]/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
