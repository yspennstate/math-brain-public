#!/usr/bin/env python3
from fractions import Fraction
from collections import Counter

W=10
FULL=(1<<W)-1
SCALE=10**15
V,C,O=0,1,2

# Dynamic protected patch: four width-10 rows plus four lateral guards.
cells=[(x,y) for x in range(W) for y in range(4)] + [(-1,1),(W,1),(-1,2),(W,2)]
cells=list(dict.fromkeys(cells))
idx={u:i for i,u in enumerate(cells)}
cellset=set(cells)
N=len(cells)

def nbrs(u):
    x,y=u
    return [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

edges=[]
for u in cells:
    x,y=u
    for dx,dy in ((1,0),(0,1)):
        v=(x+dx,y+dy)
        if v in cellset:
            edges.append((u,v))

# Clean manifold state corresponding to consumed first-rail subset A.
def clean_state(mask):
    s={u:C for u in cells}
    for x in range(W):
        s[(x,0)]=V
        s[(x,1)]=V
        s[(x,2)]=V if ((mask>>x)&1) else C
        s[(x,3)]=C
    for u in ((-1,1),(W,1),(-1,2),(W,2)):
        s[u]=V
    return s

def recognize_clean(s):
    if any(s[u]==O for u in cells): return None
    for x in range(W):
        if s[(x,0)]!=V or s[(x,1)]!=V or s[(x,3)]!=C:
            return None
    for u in ((-1,1),(W,1),(-1,2),(W,2)):
        if s[u]!=V: return None
    m=0
    for x in range(W):
        if s[(x,2)]==V: m |= 1<<x
        elif s[(x,2)]!=C: return None
    return m

# Exact one-event enumeration under fixed all-CO exterior.
def enumerate_one(mask):
    s0=clean_state(mask)
    out=Counter()
    # CO adsorption clocks at rate 1/2 on every dynamic vacancy.
    for u in cells:
        if s0[u]!=V: continue
        os=[z for z in nbrs(u) if z in cellset and s0[z]==O]
        assert not os
        s=s0.copy(); s[u]=C
        m=recognize_clean(s)
        out[("clean",m) if m is not None else ("fatal",None)] += Fraction(1,2)
    # O2 clocks at rate 1/4 on every internal vacant-vacant edge.
    for u,v in edges:
        if s0[u]!=V or s0[v]!=V: continue
        placed=s0.copy(); placed[u]=O; placed[v]=O
        choices=[]
        for a in (u,v):
            cs=[]
            for z in nbrs(a):
                if z in cellset:
                    if placed[z]==C: cs.append(z)
                else:
                    # fixed all-CO exterior; distinct outside neighbors are distinct reaction choices
                    cs.append(("ext",z))
            if not cs: cs=[("stay",a)]
            choices.append(cs)
        w=Fraction(1,4*len(choices[0])*len(choices[1]))
        for ca in choices[0]:
            for cb in choices[1]:
                s=placed.copy()
                for a,ch in ((u,ca),(v,cb)):
                    if isinstance(ch,tuple) and ch and ch[0]=="stay":
                        continue
                    s[a]=V
                    if not (isinstance(ch,tuple) and ch and ch[0]=="ext"):
                        s[ch]=V
                m=recognize_clean(s)
                out[("clean",m) if m is not None else ("fatal",None)] += w
    return out

# Build exact clean-manifold kernel directly from the full one-event rules.
kernels=[]
for m in range(1<<W):
    enum=enumerate_one(m)
    # independent total-rate check from vacancies and vacant-vacant edges
    s=clean_state(m)
    nv=sum(1 for u in cells if s[u]==V)
    ne=sum(1 for u,v in edges if s[u]==V and s[v]==V)
    expected=Fraction(nv,2)+Fraction(ne,4)
    if sum(enum.values(),Fraction(0,1)) != expected:
        raise SystemExit(f"total rate mismatch at mask {m}")
    retry=enum.pop(("clean",m),Fraction(0,1))
    fatal=enum.pop(("fatal",None),Fraction(0,1))
    trans={k[1]:v for k,v in enum.items() if k[0]=="clean" and v}
    import math
    den_lcm=1
    for q in [fatal,*trans.values()]: den_lcm=math.lcm(den_lcm,q.denominator)
    fint=int(fatal*den_lcm)
    tint={n:int(q*den_lcm) for n,q in trans.items()}
    if fint<=0: raise SystemExit(f"no fatal rate at nonterminal clean mask {m}")
    kernels.append((tint,fint,retry,expected))
print("one_step_states_checked=1024")
print("PASS exact full-event enumeration and total-rate checks for all clean-manifold states")

# Initial-state rate decomposition.
enum0=enumerate_one(0)
r0=enum0.get(("clean",0),Fraction(0,1))
f0=enum0.get(("fatal",None),Fraction(0,1))
p0=sum(v for (kind,n),v in enum0.items() if kind=="clean" and n not in (0,None))
print("initial_retry_rate=",r0)
print("initial_progress_rate=",p0)
print("initial_fatal_rate=",f0)
print("initial_total_rate=",sum(enum0.values(),Fraction(0,1)))

# Monotone fixed-grid lower/upper solve of clean success-before-fatal probability.
lo=[0]*(1<<W); up=[SCALE]*(1<<W)
lo[FULL]=up[FULL]=SCALE
iters=0
for it in range(10000):
    nlo=lo.copy(); nup=up.copy(); maxgap=0
    for m in range(FULL):
        tw,fatal,retry,totalrate=kernels[m]
        den=fatal+sum(tw.values())  # literal clean self-loop RETRY cancels
        assert den>0 and fatal>0
        sl=sum(w*lo[n] for n,w in tw.items())
        su=sum(w*up[n] for n,w in tw.items())
        lv=sl//den
        uv=(su+den-1)//den
        if lv < lo[m] or uv > up[m] or lv>uv:
            raise SystemExit("monotone enclosure invariant failed")
        nlo[m]=lv; nup[m]=uv
        maxgap=max(maxgap,uv-lv)
    lo,up=nlo,nup; iters=it+1
    if maxgap<=2: break
else:
    raise SystemExit("interval iteration did not converge")

L,U=lo[0],up[0]
print("iterations=",iters)
print("scale=",SCALE)
print("clean_success_lower_scaled=",L)
print("clean_success_upper_scaled=",U)
print("clean_success_interval=[%.15g, %.15g]"%(L/SCALE,U/SCALE))
assert U*6000000 < SCALE
assert (6000001)*U < SCALE  # p/(1-p) < 1/6,000,000
assert 64*U < 63*SCALE
print("CERTIFIED clean_success < 1/6000000")
print("CERTIFIED clean_success/(1-clean_success) < 1/6000000")
print("FAILURE_OF_ROUTE: pure-vacancy fuel-subset restart class misses required success/fatal ratio 63 by >3.7e8 factor")
print("PASS")
