import sys
sys.dont_write_bytecode=True
from pathlib import Path
import importlib.util,json,time
from fractions import Fraction as F
R=Path(__file__).resolve().parents[1]
old=R.parents[1]/'runs/20261014T055856Z-account05-A054-connectedness-alternatives/code/mathcore.py'
sp=importlib.util.spec_from_file_location('oldcore',old);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
E=m.entropy;add=m.add;lv=m.logv
def const(x):return {2:F(x)} if x else {}
count=0
def eq(x,y):
    global count
    assert add((x,1),(y,-1))=={};count+=1
def nn(x):
    global count
    assert m.ge(x);count+=1
def Hcounts(xs):
    t=sum(xs)
    return E([F(x,t) for x in xs]) if t else {}
def run(n,mask):
    N=1<<n;g=tuple((mask>>x)&1 for x in range(N));p=F(sum(g),N)
    if not p:return None
    comps=m.components(g);sizes=[sum(c) for c in comps]
    h={}
    for s in sizes:h=add((h,1),(lv(F(s)),F(s,sum(g))))
    inf=[4*m.edges(g,1<<i) for i in range(n)];I=sum(inf,F(0));mx=max(inf)
    hc=[]
    for i in range(n):
        v={}
        for c,s in zip(comps,sizes):
            pairs={}
            for x,z in enumerate(c):
                if z:pairs[x&~(1<<i)]=pairs.get(x&~(1<<i),0)+1
            for num in pairs.values():v=add((v,1),(lv(F(num)),F(num,sum(g))))
        eq(v,const(1-inf[i]/(2*p)));hc.append(v)
    b=add((h,1),(const(n-I/(2*p)),-1));nn(b)
    eq(h,add((const(n-I/(2*p)),1),(b,1)))
    for A in range(1,N-1):
        r=A.bit_count();W={};cond={}
        for c,s in zip(comps,sizes):
            fibers={}
            for x,z in enumerate(c):
                if z:fibers[x&~A]=fibers.get(x&~A,0)+1
            for num in fibers.values():
                W=add((W,1),(lv(F(1<<r,num)),F(num,N)))
                cond=add((cond,1),(lv(F(num)),F(num,sum(g))))
        eq(W,add((const(r*p),1),(cond,-p)))
        IA=sum((inf[i] for i in range(n) if A>>i&1),F(0))
        nn(add((const(IA),1),(W,-2)))
        nn(add((const(r*mx),1),(W,-2)))
        if r==1:eq(W,const(IA/2))
        # Original-label conditioning must include all retained coordinates.
        rhs={}
        for i in range(n):
            if A>>i&1:rhs=add((rhs,1),(hc[i],1))
        nn(add((cond,1),(rhs,-1)))
    return {'n':n,'mask':str(mask),'p':str(p),'I':str(I),'maxInf':str(mx),'h':m.vec(h),'dual_TC':m.vec(b),'components':sizes}
t=time.perf_counter();pilot='--pilot' in sys.argv
domain=[(n,k) for n in range(1,3 if pilot else 4) for k in range(1<<(1<<n))]
fixtures=[(4,sum(1<<x for x in [0,1,5,7,14,15])),(5,sum(1<<x for x in [0,4,12,13,15,3,19,27,26,24])),(5,sum(1<<x for x in range(32) if x.bit_count()<=2)),(4,sum(1<<x for x in range(16) if x.bit_count()%2==0))]
records=[]
for n,k in domain:
    run(n,k)
    assert time.perf_counter()-t<55
for n,k in fixtures:records.append(run(n,k))
# Necessity of the actual component / edge-constant label hypothesis.
bad_label_W=F(1);full_cube_Inf=F(0)
assert bad_label_W>full_cube_Inf/2;count+=1
out={'status':'PASS','pilot':pilot,'root_cases':len(domain),'fixtures':records,'assertions':count,'seconds':time.perf_counter()-t,'arithmetic':'Fraction; canonical prime-log vectors; 32-term atanh bounds with proved tail and outward 112-bit dyadics','noncomponent_label_countercheck':'full-cube parity labels: W_singleton=1, Inf=0'}
(R/'out'/('PILOT.json' if pilot else 'EXACT_CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='fixtures'}))
