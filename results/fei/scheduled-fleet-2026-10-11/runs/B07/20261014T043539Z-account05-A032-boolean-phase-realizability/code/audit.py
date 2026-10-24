import json,time,math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def factor(n):
    result={};p=2
    while p*p<=n:
        while n%p==0:result[p]=result.get(p,0)+1;n//=p
        p+=1
    if n>1:result[n]=result.get(n,0)+1
    return result
FACTORS={n:factor(n) for n in range(1,257)}
def addlog(counter,n,a):
    for p,e in FACTORS[n].items():counter[p]+=a*e
def entropy(weights):
    out=Counter({2:2048})
    for t in weights:
        if t:addlog(out,t,-t)
    return out
def logsig(s):return tuple(sorted((p,a) for p,a in s.items() if a))
def log_interval(p):
    if p==2:return F(1),F(1)
    def ln(x):
        k=0;x=F(x)
        while x>=2:x/=2;k+=1
        def series(z):
            t=(z-1)/(z+1);v=2*sum((t**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
            return v,v+2*t**65/(65*(1-t*t))
        a,b=series(x);c,d=series(F(2));return a+k*c,b+k*d
    a,b=ln(p);c,d=ln(2);return a/d,b/c
def bound(sig):
    lo=hi=F(0)
    for p,a in sig:
        c,d=log_interval(p);lo+=a*(c if a>0 else d);hi+=a*(d if a>0 else c)
    return lo,hi
def verify(name,signatures):
    out=[]
    for sig in sorted(signatures):
        if not sig:out.append({'signature':[],'verdict':'EXACT_ZERO'});continue
        lo,hi=bound(sig);assert lo>0,(name,sig,lo)
        out.append({'signature':[[p,str(v)] for p,v in sig],'verdict':'POSITIVE','lower_bound':str(lo)})
    return {'name':name,'objectives':len(out),'exact_zero':sum(r['verdict']=='EXACT_ZERO' for r in out),'certificates':out}
def main():
    start=time.monotonic();chars=[[(-1 if (s&x).bit_count()%2 else 1) for x in range(16)] for s in range(16)]
    ledger=set();conditional=set();joint=set();arbitraryjoint=set();admitted=0;maxN=0;controls={}
    for code in range(32768):
        truth=[1]+[(-1 if code>>(x-1)&1 else 1) for x in range(1,16)]
        W=[sum(v*c for v,c in zip(truth,char)) for char in chars];a=[v*v for v in W]
        assert sum(a)==256
        Iaddr=sum((s&3).bit_count()*v for s,v in enumerate(a));Iy=sum((s>>2).bit_count()*v for s,v in enumerate(a))
        edges=[sum(truth[x]!=truth[x^(1<<j)] for x in range(16)) for j in range(4)]
        assert 16*sum(edges[:2])==Iaddr and 16*sum(edges[2:])==Iy
        masses=[sum(a[J+4*s] for s in range(4)) for J in range(4)]
        L=Counter({2:2*Iaddr-2048});product=True
        for J,z in enumerate(masses):
            if not z:continue
            weights=[a[J+4*s] for s in range(4)]
            addlog(L,sum(abs(W[J+4*s]) for s in range(4)),2*z)
            if weights[0]*weights[3]!=weights[1]*weights[2]:product=False;continue
            N=sum(t not in(0,z) and 2*t!=z for t in (weights[1]+weights[3],weights[2]+weights[3]))
            maxN=max(maxN,N)
            if N>1:product=False
        ledger.add(logsig(L))
        if not product:continue
        admitted+=1;H=entropy(a);Ha=entropy(masses);Hc=Counter(H)
        for p,v in Ha.items():Hc[p]-=v
        C=Counter({2:4*Iy,5:F(5*Iy,2),3:F(-9*Iy,2)})
        for p,v in Hc.items():C[p]-=v
        conditional.add(logsig(C))
        D=Counter({2:10*(Iaddr+Iy),3:-3*(Iaddr+Iy)})
        E=Counter({2:-6*(Iaddr+Iy),5:2*(Iaddr+Iy),13:2*(Iaddr+Iy)})
        for p,v in H.items():D[p]-=v;E[p]-=v
        joint.add(logsig(D));arbitraryjoint.add(logsig(E))
        if code==1:controls={'truth':truth,'Walsh':W,'physical_edges':edges,'masses_numerators':masses,'IY_numerator':Iy}
        if code%1000==0:assert time.monotonic()-start<60,'FROZEN_RUNTIME_LIMIT'
    assert admitted==5280 and maxN==1
    checks=[verify('universal address/Renyi ledger',ledger),verify('sharp conditional Kcond',conditional),verify('fixed-ratio joint Kjoint',joint),verify('arbitrary-ratio joint Kall',arbitraryjoint)]
    out={'status':'PASS','truth_tables_mod_global_sign':32768,'unreduced_truth_tables':65536,'admitted_tables_mod_global_sign':admitted,'max_row_N':maxN,'checks':checks,'seconds':time.monotonic()-start,'scope':'independent direct-character implementation; no author code imported'}
    (ROOT/'out/a079_audit.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items() if k!='checks'}));print(json.dumps([{'name':c['name'],'objectives':c['objectives'],'exact_zero':c['exact_zero']} for c in checks]))
if __name__=='__main__':main()
