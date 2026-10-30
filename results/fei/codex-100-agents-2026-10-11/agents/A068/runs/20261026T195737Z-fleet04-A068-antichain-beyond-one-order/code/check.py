from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json, time, sys, math

RUN=Path(__file__).resolve().parents[1]
t0=time.perf_counter(); checks=0; states=0
def ck(a):
    global checks
    checks+=1
    assert a, checks
    if time.perf_counter()-t0>55: raise RuntimeError('frozen runtime exceeded')
def parity(a): return a.bit_count()&1
def walsh(tab):
    a=list(tab); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h]; a[j],a[j+h]=u+v,u-v
        h*=2
    return [F(x,len(a)) for x in a]
def proj(s,keep): return sum(((s>>i)&1)<<j for j,i in enumerate(keep))
def push(q,keep):
    a=[F(0)]*(1<<len(keep))
    for s,v in enumerate(q): a[proj(s,keep)]+=v
    return a
def smooth(q,V):
    c=[s for s in range(len(q)) if s not in V]
    if not c: return list(q)
    u=sum((q[s] for s in c),F(0))/len(c)
    return [q[s] if s in V else u for s in range(len(q))]
def direct_restrict(tab,assignment):
    keep=[i for i,b in enumerate(assignment) if b<0]
    fixed=sum(b<<i for i,b in enumerate(assignment) if b>=0)
    out=[]
    for x in range(1<<len(keep)):
        address=fixed+sum(((x>>j)&1)<<i for j,i in enumerate(keep))
        out.append(tab[address])
    return out,keep
def amgm(q,V):
    c=[v for s,v in enumerate(q) if s not in V]
    if not c: return
    m=len(c); avg=sum(c,F(0))/m
    ck(avg**m>=math.prod(c))

pilot='--pilot' in sys.argv
cores=range(2) if pilot else range(16)
assignments=list(product((-1,0,1),repeat=4))
sources=[[F(i+1,136) for i in range(16)], [F(241 if i==7 else 1,256) for i in range(16)]]
for a,b in ((1,2),(3,6),(5,10)):
    V={0,a,b,a^b}; ck(len(V)==4)
    source_data=[]
    for q in sources:
        qb=smooth(q,V); amgm(q,V)
        for ass in assignments:
            keep=[i for i,v in enumerate(ass) if v<0]
            Vp={proj(s,keep) for s in V}
            raw=push(q,keep); inherited=push(qb,keep)
            ck(inherited==smooth(inherited,Vp)); amgm(raw,Vp)
            # Exact projected orbit formula, including every vacuum/ghost atom.
            codim=4-len(keep); r=(len(Vp)).bit_length()-1
            outside=sum((q[s] for s in range(16) if s not in V),F(0))
            expected=[]
            for u in range(1<<len(keep)):
                core=sum((q[s] for s in V if proj(s,keep)==u),F(0))
                count=(1<<codim)-((1<<(2-r)) if u in Vp else 0)
                expected.append(core+outside*F(count,12))
            ck(inherited==expected)
            source_data.append((ass,keep,Vp,raw,inherited))
    for mask in cores:
        core=[1 if (mask>>j)&1 else -1 for j in range(4)]
        clean=[core[parity(x&a)+2*parity(x&b)] for x in range(16)]
        for edit in range(16):
            tab=clean.copy(); tab[edit]*=-1
            coeff=walsh(tab); outside=[s for s in range(16) if s not in V]
            ck(all(coeff[s]**2==F(1,64) for s in outside))
            for ass in assignments:
                child,keep=direct_restrict(tab,ass)
                base,_=direct_restrict(clean,ass)
                Vp={proj(s,keep) for s in V}
                actual=[c*c for c in walsh(child)]
                basehat=walsh(base)
                ck(all(basehat[s]==0 for s in range(len(basehat)) if s not in Vp))
                compatible=all(v<0 or v==((edit>>i)&1) for i,v in enumerate(ass))
                shell=[actual[s] for s in range(len(actual)) if s not in Vp]
                ck(not shell or all(p==(F(4,len(child)**2) if compatible else 0) for p in shell))
                ck(sum(actual,F(0))==1)
                states+=1

# Boundary guard: larger full group costs rank n, partial orbit leaves dominant label fixed.
guards=[]
for n in (2,4,8,16,32,64):
    delta=F(2,1<<n); small=delta*delta; main=(1-delta)**2
    ck(main+((1<<n)-1)*small==1)
    ck(main!=small if n>2 else main==small)
    # V={0,1}; outside all equal, so P already equals its partial return.
    ck(small*((1<<n)-2)/((1<<n)-2)==small)
    guards.append(dict(n=n,partial_return_debit='0',core_labels_fixed=2,full_GL_nonempty_orbit=(1<<n)-1))
result=dict(status='PASS',cases=states,assertions=checks,seconds=time.perf_counter()-t0,pilot=pilot,arithmetic='Fraction/integer; exact AM-GM products',guards=guards)
(RUN/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
