from fractions import Fraction
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import ast, sys, time

sys.setrecursionlimit(1000000)

import zlib, base64
PATCH_B85 = "c-rloOAdoD3`DQOE}-BG^j@s0-n}IiJF2RmMAppf0#&Gp$b+9J#=XvuPpM^{%Jw`g>ogzVU!2&_y!*|cE^1c|x|iqzm&?AwGnFer)KR&u@I=!fhB_i2DhEMy1U9*>2kby(17N35Wwrng4x5T%;II+7hr`YmM79794jXr9;II+7hr_M_8;6bgQgGN6U;}JgA^>}Y%DffT12$E;2e3EFGQdV<df14}OGjEF^sq5s02`5=S|V(gKLvIR8Oq8+I!Iq8Lny@(t~yXz7}zah2rCF_JQnVGVBnHIZutS6I8B2z{RP03R#gD!R5ra`#|?i~S#v&Z^pYLM>k?NB#_KFpX1vZoWTxH?#!2`C3&19ZBEY`g0kI9`9s"
PATCHES = ast.literal_eval(zlib.decompress(base64.b85decode(PATCH_B85)).decode())
assert isinstance(PATCHES, dict) and len(PATCHES) == 14


def norm(children):
    p = sum(1 for c in children if c == '+')
    m = sum(1 for c in children if c == '-')
    if p >= 2: return '+'
    if m >= 2: return '-'
    return tuple(sorted(children, key=repr))

@lru_cache(maxsize=None)
def queries(t):
    if t == 'u': return (('+','-'),)
    if t in ('+','-'): return ()
    out=set()
    for i,c in enumerate(t):
        if i>0 and t[i]==t[i-1]: continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]), norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out,key=repr))

@lru_cache(maxsize=None)
def V(t):
    if t in ('+','-'): return Fraction(0)
    return min(Fraction(1)+(V(a)+V(b))/2 for a,b in queries(t))

def full(k):
    return 'u' if k==0 else norm((full(k-1),)*3)

@lru_cache(maxsize=None)
def q(t):
    if t=='+': return 1.0
    if t=='-': return 0.0
    if t=='u': return 0.5
    a,b,c=(q(x) for x in t)
    return a*b*c+a*b*(1-c)+a*(1-b)*c+(1-a)*b*c

@lru_cache(maxsize=None)
def lottery(ws,qs):
    @lru_cache(maxsize=None)
    def g(state):
        p=sum(1 for s in state if s==1); m=sum(1 for s in state if s==0)
        if p>=2 or m>=2: return 0.0
        best=float('inf')
        for i in range(3):
            if state[i] is None:
                sp=list(state); sp[i]=1
                sm=list(state); sm[i]=0
                z=ws[i]+qs[i]*g(tuple(sp))+(1-qs[i])*g(tuple(sm))
                if z<best: best=z
        return best
    init=tuple(None if 0<qs[i]<1 else int(qs[i]>0.5) for i in range(3))
    return g(init)

@lru_cache(maxsize=None)
def R(t):
    if t in ('+','-'): return 0.0
    return lottery(tuple(float(V(c)) for c in t), tuple(q(c) for c in t))

@lru_cache(maxsize=None)
def child_opt_moves(c):
    if c=='u': return (('+','-'),)
    opts=[(Fraction(1)+(V(a)+V(b))/2,a,b) for a,b in queries(c)]
    m=min(x[0] for x in opts)
    return tuple((a,b) for z,a,b in opts if z==m)

@lru_cache(maxsize=None)
def base_policy(t):
    best=None
    for i,c in enumerate(t):
        if c in ('+','-'): continue
        if i>0 and t[i]==t[i-1]: continue
        for cp,cm in child_opt_moves(c):
            tp=norm(t[:i]+(cp,)+t[i+1:]); tm=norm(t[:i]+(cm,)+t[i+1:])
            h=1.0+(R(tp)+R(tm))/2.0
            if best is None or h<best[0]-1e-12:
                best=(h,tp,tm)
    return best[1],best[2]

ROOT=full(4)
OLD_U4=Fraction(20871140813662641,562949953421312)
U1=Fraction(83382761998226581,2251799813685248)
U3=Fraction(83309742205455645,2251799813685248)
U4=Fraction(1332929426337871847,36028797018963968)
UF=Fraction(1332788674231672015,36028797018963968)

def make_pol_E(patches):
    def pol(t):
        return patches[t] if t in patches else base_policy(t)
    @lru_cache(maxsize=None)
    def E(t):
        if t in ('+','-'): return Fraction(0)
        a,b=pol(t)
        return Fraction(1)+(E(a)+E(b))/2
    return pol,E

def layer(pol,d):
    s={ROOT}
    for _ in range(d):
        n=set()
        for x in s:
            if x not in ('+','-'):
                a,b=pol(x); n|={a,b}
        s=n
    return s

def stage(oldpatch, d):
    oldpol, oldE=make_pol_E(oldpatch)
    states=layer(oldpol,d)
    add={s:PATCHES[s] for s in states if s in PATCHES and s not in oldpatch}
    residuals=[]
    for s,mv in add.items():
        assert mv in queries(s), 'patched move must be a legal leaf query orbit'
        a,b=mv
        qv=Fraction(1)+(oldE(a)+oldE(b))/2
        r=oldE(s)-qv
        assert r>0, 'each override must be a strict exact Bellman improvement'
        residuals.append(r)
    newpatch=dict(oldpatch); newpatch.update(add)
    newpol,newE=make_pol_E(newpatch)
    return states,add,Counter(residuals),newpatch,newpol,newE

def is_d1(x):
    if x in ('+','-'): return True
    return isinstance(x,tuple) and len(x)==3 and all(y in ('u','+','-') for y in x)

def depth2_nodes(t):
    out=[]
    if isinstance(t,tuple) and len(t)==3 and all(is_d1(c) for c in t): out.append(t)
    elif isinstance(t,tuple):
        for c in t: out.extend(depth2_nodes(c))
    return out

start=time.time()
pol0,E0=make_pol_E({})
assert E0(ROOT)==OLD_U4
print('baseline_U4',E0(ROOT),float(E0(ROOT)))

patch={}
s1,a1,r1,patch,p1,E1=stage(patch,1)
assert (len(s1),len(a1),E1(ROOT))==(2,2,U1)
assert r1==Counter({Fraction(101801256423983,2251799813685248):2})
print('stage_d1',len(s1),len(a1),r1,'U4',E1(ROOT),float(E1(ROOT)))

# Correct geometry of the first override.
pp=norm(('+','u','u')); geom=False
for s,mv in a1.items():
    for succ in mv:
        if any(sum(c==pp for c in node)==2 for node in depth2_nodes(succ)):
            geom=True
assert geom
print('first_override_geometry PASS different bottom MAJ3 gate, same depth2 block')

# No patch in the table lies at depth 2; this records the failed B3 subcase.
s2=layer(p1,2)
assert not any(s in PATCHES for s in s2)
print('stage_d2',len(s2),'patched 0')

s3,a3,r3,patch,p3,E3=stage(patch,3)
assert (len(s3),len(a3),E3(ROOT))==(6,6,U3)
assert r3==Counter({Fraction(4987919693479,70368744177664):2,
                    Fraction(16456306516981,562949953421312):2,
                    Fraction(101911094571,281474976710656):2})
print('stage_d3',len(s3),len(a3),r3,'U4',E3(ROOT),float(E3(ROOT)))

s4,a4,r4,patch,p4,E4=stage(patch,4)
assert (len(s4),len(a4),E4(ROOT))==(6,2,U4)
assert r4==Counter({Fraction(26448949418473,4503599627370496):2})
print('stage_d4',len(s4),len(a4),r4,'U4',E4(ROOT),float(E4(ROOT)))

s5,a5,r5,patch,p5,EF=stage(patch,5)
assert (len(s5),len(a5),EF(ROOT))==(12,4,UF)
assert r5==Counter({Fraction(7520884513,274877906944):2,
                    Fraction(730413930785,140737488355328):2})
assert patch==PATCHES
print('stage_d5',len(s5),len(a5),r5,'U4',EF(ROOT),float(EF(ROOT)))
print('patch_states',len(PATCHES),'= 7 global-sign orbits')
print('gain_vs_previous',U1-UF,float(U1-UF))
print('gain_vs_baseline',OLD_U4-UF,float(OLD_U4-UF))

getcontext().prec=60
D=Decimal; ln3=D(3).ln()
def df(x): return D(x.numerator)/D(x.denominator)
su=(D(4)/D(3)).ln()/ln3
sl=D(1)-(df(UF).ln()/D(4))/ln3
w=su-sl
oldsl=D('0.1781195648046619356672102637439')
oldw=D('0.08373994233825293853184396494162')
assert sl>oldsl and w<oldw
print('stationary_4block_growth',df(UF)**(D(1)/D(4)))
print('sigma_lower',sl)
print('sigma_upper',su)
print('W_sigma',w)
print('sigma_gain',sl-oldsl)
print('width_contraction',oldw-w)
print('runtime_seconds',round(time.time()-start,3))
print('ALL_EXACT_POLICY_CHECKS_PASS')
