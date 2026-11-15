"""Compressed exact formulas: no truth table allocation at large dimension."""
import json,math,resource,os,time
from pathlib import Path
import mpmath as mp
mp.mp.dps=180
Q=[mp.mpf(str(x)) for x in [1,.5,.25,.1,.05,.01,0]]
def bits(x):return -mp.log(x,2)
def finish(name,n,I,H,A,v,mom,**kw):
    L=[A if q==0 else bits(mom(q))/q for q in Q]
    return dict(name=name,n=n,I=float(I),H_bits=float(H),A_bits=float(A),Var=float(v),
                WC=float(mom(mp.mpf(1))),Lq_bits={str(float(q)):float(x) for q,x in zip(Q,L)},
                ratios={str(float(q)):float(x/I) for q,x in zip(Q,L)},**kw)
def and_row(n):
    p=mp.power(2,-n);m0=(1-2*p)**2;v=1-m0;I=2*n*p
    H=(0 if m0==0 else m0*bits(m0))+v*(2*n-2)
    A=(n-2)*v+I
    def mom(q):return m0+4*p*p*(4*p)**q*((1+mp.power(2,-q))**n-1)
    out=finish('AND',n,I,H,A,v,mom)
    out['L_over_I_squared']=float(bits(mom(1))/(I*I));return out
def address_row(k):
    def mom(q):return (mp.power(2,-q)*(1+mp.power(2,-q))/2)**k
    return finish('address_MUX',k+(1<<k),1+mp.mpf(k)/2,2*k,mp.mpf(3)*k/2,1,mom,address_bits=k)
def bent_row(n):
    return finish('bent',n,mp.mpf(n)/2,n,mp.mpf(n)/2,1-mp.power(2,-n),lambda q:((1+mp.power(2,-q))/2)**n)
def tribes_row(w,t=None):
    p=mp.power(2,-w);d=1-p
    if t is None:t=int(mp.nint(mp.log(mp.mpf('.5'))/mp.log(d)))
    z=d**t;m0=(2*z-1)**2;v=1-m0;K1=4*z*t*p;I=K1*w/(2*d)
    H=(0 if m0==0 else m0*bits(m0))-2*v+(2*w+2*mp.log(d,2))*K1-2*t*mp.log(d,2)*v
    A=-2*v+(w+w/(2*d)+mp.log(d,2))*K1-t*mp.log(d,2)*v
    def mom(q):
        b=d**(2+q);c=p**(2+q)*((1+mp.power(2,-q))**w-1)
        return m0+mp.power(4,1+q)*b**t*mp.expm1(t*mp.log1p(c/b))
    return finish('tribes',w*t,I,H,A,v,mom,width=w,tribes=t)
def majority_row(n):
    m=(n-1)//2;c1=mp.mpf(math.comb(2*m,m))/mp.power(2,2*m)
    mu=[mp.mpf(0)]*(n+1)
    for k in range(m+1):mu[2*k+1]=(c1*math.comb(m,k)/math.comb(2*m,2*k))**2
    W=[math.comb(n,s)*mu[s] for s in range(n+1)]
    up=[sum(math.comb(n-s,j-s)*mu[j] for j in range(s,n+1)) for s in range(n+1)]
    H=sum(W[s]*bits(mu[s]) for s in range(n+1) if mu[s]);A=sum(W[s]*bits(up[s]) for s in range(n+1) if mu[s])
    return finish('majority',n,n*c1,H,A,1,lambda q:sum(W[s]*up[s]**q for s in range(n+1)))
if __name__=='__main__':
    start=time.time();rows=[]
    for n in list(range(2,19))+[32,64,128,256]:rows.append(and_row(n))
    for k in [1,2,3,4,8,16,32,64,128]:rows.append(address_row(k))
    for n in [2,4,8,16,64,256]:rows.append(bent_row(n))
    for w in [2,3,4,6,8,12,16,32,64,128]:rows.append(tribes_row(w))
    for w,t in [(2,2),(2,3),(3,4),(3,5),(3,6),(4,4)]:rows.append(tribes_row(w,t))
    for n in [3,5,7,9,17,31,63,127,255]:rows.append(majority_row(n))
    Path('analytic_families.json').write_text(json.dumps(rows,indent=2))
    evidence=dict(wall_seconds=time.time()-start,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),precision_decimal_digits=mp.mp.dps,rows=len(rows))
    Path('analytic_resources.json').write_text(json.dumps(evidence,indent=2));print(json.dumps(evidence))
