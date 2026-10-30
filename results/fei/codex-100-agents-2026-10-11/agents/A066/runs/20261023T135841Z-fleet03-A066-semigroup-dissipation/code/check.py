"""Exact stage11 certificate, self-contained, no floating sign decisions."""
from pathlib import Path
from fractions import Fraction as F
import json,time,hashlib,sys
R=Path(__file__).resolve().parents[1]
checks=0
start=time.perf_counter()
def ck(x):
    global checks
    checks+=1
    assert x, checks
    assert time.perf_counter()-start<45
def fw(v):
    v=list(v);j=1
    while j<len(v):
        for k in range(0,len(v),2*j):
            for i in range(k,k+j):
                a,b=v[i],v[i+j];v[i],v[i+j]=a+b,a-b
        j*=2
    return [F(a,len(v)) for a in v]
def truth(n):
    return [-1 if s==0 else (1 if not s&1 else -1) for s in range(1<<n)]
def inf(v,n):
    return [F(sum(v[s]!=v[s^(1<<i)] for s in range(1<<n)),1<<n) for i in range(n)]
def logs(terms):
    d={}
    for c,q in terms:
        q=F(q)
        for v,sgn in [(q.numerator,1),(q.denominator,-1)]:
            prime=2
            while prime*prime<=v:
                e=0
                while v%prime==0:v//=prime;e+=1
                if e:d[prime]=d.get(prime,F(0))+sgn*c*e
                prime+=1
            if v>1:d[v]=d.get(v,F(0))+sgn*c
    return {q:c for q,c in d.items() if c}
def add(*ds):return logs((c,q) for d in ds for q,c in d.items())
def neg(d):return {q:-c for q,c in d.items()}
def ce(p,q):return logs((-v,q[i]) for i,v in enumerate(p) if v)
def entropy(p):return ce(p,p)
def direct_majority():
    n=5;v=[1 if s.bit_count()<3 else -1 for s in range(32)]
    w=[]
    for a in range(32):
        w.append(F(sum(v[s]*(-1 if (s&a).bit_count()%2 else 1) for s in range(32)),32))
    ck(sorted(x*x for x in w if x)==[F(1,64)]*10+[F(9,64)]*6)
    ck(sum(a.bit_count()*w[a]**2 for a in range(32))==F(15,8))
    for k in range(4,33):
        eps=F(1,2**(3*k));ck(30*eps<F(1,2))
        ck(F(23*k,8)-F(165*k+9,64)-F(1,4)==F(19*k-25,64))
        ck(F(19*k-25,64)>0)
        ck(F(15*k,8)-F(165*k,64)-F(1,4)<0)
        ck(F(15*k,8)-5-F(1,4)>=F(9,4))
    return 29
def main():
    pilot='pilot' in sys.argv
    ns=range(3,6) if pilot else range(3,11)
    rows=[]
    for n in ns:
        N=1<<n;delta=F(2,N);a=(1-delta)**2;b=delta**2
        v=truth(n);w=fw(v);p=[x*x for x in w]
        ck(w==[1-delta if j==1 else -delta for j in range(N)])
        ck(sum(p)==1);ck(all(p));ck(all(x>0 for x in inf(v,n)))
        J=sum(inf(v,n));ck(J==1+(n-2)*delta)
        ck(J==sum(j.bit_count()*p[j] for j in range(N)))
        qbar=[b]+[(1-b)/(N-1)]*(N-1)
        ck(sum(qbar)==1);ck(qbar[0]==p[0])
        H=entropy(p);C=ce(p,qbar);Delta=add(C,neg(H))
        # Direct conditional-KL expression equals exact original source invoice.
        phi=logs((p[j],p[j]*(N-1)/(1-b)) for j in range(1,N))
        # Expand ratios, instead of comparing inequivalent log atom spellings.
        phiex=logs([(p[j],p[j]) for j in range(1,N)]+[(1-b,F(N-1)),(-(1-b),1-b)])
        ck(Delta==phiex)
        ck(phi==phiex)
        # Private t,x root spectra from physical truth tables; every branch.
        root=[((-1 if s&1 else 1)*(-1 if s&2 else 1)*v[s>>2]) for s in range(4*N)]
        wr=fw(root);pr=[x*x for x in wr]
        ck(pr==[p[j>>2] if j&3==3 else 0 for j in range(4*N)])
        ck(sum(inf(root,n+2))==J+2)
        for t in [0,1]:
            child=[root[t+2*s] for s in range(2*N)];wc=fw(child)
            ck(all(wc[2*j]==0 for j in range(N)))
            ck(all(wc[2*j]*wc[2*j+1]==0 for j in range(N)))
            ck(wc[1]**2==b) # nonzero singleton: edited dictator is biased
            ck(entropy([x*x for x in wc])==H)
            for x in [0,1]:
                term=[child[x+2*s] for s in range(N)];pt=[z*z for z in fw(term)]
                ck(pt==p);ck(ce(pt,p)==H);ck(ce(pt,qbar)==C)
                ck(pt[0]==b) # child mean is nonzero, heat boundary retained
        if n>=8:
            ck((4*n-1)*delta<=F(31,128));ck(J<=F(67,64));ck(b<=F(1,16384))
        rows.append({'n':n,'I':str(J),'vacuum':str(b),'all_relevant':True,'full_support':True})
    # Symbolic exact rational certificates; no large truth tables built.
    for k in range(1,9 if pilot else 257):
        n=2*k+8;delta=F(1,2**(n-1));J=1+(n-2)*delta
        Hb=(4*n-1)*delta;Cb=F(63,64)*(n-1)
        ck(Hb<F(1,4));ck(J<F(17,16));ck(k*J-Hb-F(1,4)>F(1,2))
        ck(Cb-k*J>0);ck(Cb-F(17*k,16)==F(58*k+441,64))
        ck(k*(n-2)*delta<=F(1,64))
        ck((n-1)*delta**2<F(1,64))
        ck((n-1)-F(1,64)-k*(J+1)>=F(223,32))
        # Fixed original owner and both complete-terminal conservation equations.
        A=k*(J+2);ck(A-2*k-F(1,4)==k*J-F(1,4))
        ck(k*J-Cb-F(1,4)<0)
    reviewed=direct_majority()
    out={'status':'PASS','assertions':checks,'seconds':time.perf_counter()-start,'arithmetic':'integer FWHT, Fraction, formal rational-log identities; rational analytic bounds for signs','physical_n':list(ns),'symbolic_K_count':8 if pilot else 256,'A068_Maj5_K_cases':reviewed,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    name='PILOT.json' if pilot else 'CHECK.json'
    (R/'out'/name).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:out[k] for k in ['status','assertions','seconds','physical_n','symbolic_K_count']}))
if __name__=='__main__':main()
