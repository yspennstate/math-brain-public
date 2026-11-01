"""Zero-phase-energy guard with EVERY extra physical influence billed."""
from pathlib import Path
from fractions import Fraction as F
import json,time,sys
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(b):
    global checks
    checks+=1;assert b,checks;assert time.perf_counter()-t0<45
def fw(v):
    v=list(v);l=1
    while l<len(v):
        for a in range(0,len(v),2*l):
            for j in range(a,a+l):
                x,y=v[j],v[j+l];v[j]=x+y;v[j+l]=x-y
        l*=2
    return [F(x,len(v)) for x in v]
def influence(v):
    return sum(F(sum(v[s]!=v[s^(1<<j)] for s in range(len(v))),len(v)) for j in range(len(v).bit_length()-1))
pilot='pilot' in sys.argv
ns=range(3,6) if pilot else range(3,11)
for n in ns:
    N=2**n;delta=F(2,N)
    h=[-1 if s==0 else (1 if s%2==0 else -1) for s in range(N)]
    ph=[v*v for v in fw(h)]
    # t,x,z are all relevant and retained in original physical influence.
    f=[(-1)**((s&7).bit_count()%2)*h[s>>3] for s in range(8*N)]
    pf=[v*v for v in fw(f)]
    ck(pf==[ph[s>>3] if s&7==7 else 0 for s in range(8*N)])
    J=1+(n-2)*delta;ck(influence(f)==J+3)
    ck(sum(f)==0)
    for t in [0,1]:
        child=[f[t+2*s] for s in range(4*N)];w=fw(child)
        ck(sum(child)==0);ck(w[1]==0)
        ck(all(w[2*j]*w[2*j+1]==0 for j in range(2*N)))
        ck(influence(child)==J+2)
        for x in [0,1]:
            terminal=[child[x+2*s] for s in range(2*N)];wp=fw(terminal)
            ck(sum(terminal)==0);ck(influence(terminal)==J+1)
            ck([v*v for v in wp]==[ph[s>>1] if s&1 else 0 for s in range(2*N)])
for K in range(1,9 if pilot else 257):
    n=4*K+8;delta=F(1,2**(n-1));J=1+(n-2)*delta
    Hb=(4*n-1)*delta;Cfloor=n-1-F(1,64)
    ck(K*(J-1)<=F(1,64));ck((n-1)*delta**2<F(1,64));ck(Hb<F(1,4))
    # Source delta_txz tensor Ph, actual A=K(J+3), old tau1/4.
    ck(K*(J+1)-Hb-F(1,4)>K+F(1,2))
    ck(Cfloor-K*(J+2)>=K+F(223,32))
    ck(Cfloor-K*(J+1)+F(1,4)>=2*K+F(231,32))
    ck(K*(J+3)-2*K-F(1,4)==K*(J+1)-F(1,4))
out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-t0,'physical_n':list(ns),'symbolic_K_count':8 if pilot else 256,'family':'F=t*x*z*h_n; original K pays all3 private physical influences; no external core source','proof_scope':'zero singleton and all paired products at BOTH queried signs; full terminals retain z and Ph; n>=4K+8 gives conversion deficit BEFORE x > K+231/32','arithmetic':'integer Walsh, exact Fraction, rational proven-log bounds'}
(R/'out'/('BALANCED_PILOT.json' if pilot else 'BALANCED_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
