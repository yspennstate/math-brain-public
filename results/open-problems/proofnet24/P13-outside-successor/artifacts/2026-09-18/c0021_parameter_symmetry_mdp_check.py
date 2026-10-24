from fractions import Fraction
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import ast,zlib,base64,time

OLD=ast.literal_eval(zlib.decompress(base64.b85decode('c-rloOAdoD3`DQOE}-BG^j@s0-n}IiJF2RmMAppf0#&Gp$b+9J#=XvuPpM^{%Jw`g>ogzVU!2&_y!*|cE^1c|x|iqzm&?AwGnFer)KR&u@I=!fhB_i2DhEMy1U9*>2kby(17N35Wwrng4x5T%;II+7hr`YmM79794jXr9;II+7hr_M_8;6bgQgGN6U;}JgA^>}Y%DffT12$E;2e3EFGQdV<df14}OGjEF^sq5s02`5=S|V(gKLvIR8Oq8+I!Iq8Lny@(t~yXz7}zah2rCF_JQnVGVBnHIZutS6I8B2z{RP03R#gD!R5ra`#|?i~S#v&Z^pYLM>k?NB#_KFpX1vZoWTxH?#!2`C3&19ZBEY`g0kI9`9s')).decode())
N7=ast.literal_eval(zlib.decompress(base64.b85decode('c-pJh&`{S_*HHjcr9cWsXaYqD2xyX}39JiZC5kF-8rVgN1L<NHc@EUHf(Id80|jE^XiSk1Q;1+2fb69^n!U)1G>AT3`p23sx+>k#SR=7e)ExwQZ8X+MEFkF~X%HJnBZ`zlu@(TC6AJk')).decode())
N8=ast.literal_eval(zlib.decompress(base64.b85decode('c-pJh&`{S_*HHjcr9cWsXaYqD2xyX}39JiZCC%-k#DTi#s&og912wJSK{(K{rac;KM8_If+hB+^-O)%RI?@I#)^vwltd))ykfV8RBLxf7y@D3^1y6|0>$S*2gU9E!dh75h4XR0MWOV>@Ps)NQW-jL#dTUqKa{_d^;Odo8T')).decode())
assert len(OLD)==14 and len(N7)==2 and len(N8)==4 and set(N7).isdisjoint(N8)

def norm(ch):
    p=sum(c=='+' for c in ch);m=sum(c=='-' for c in ch)
    if p>=2:return '+'
    if m>=2:return '-'
    return tuple(sorted(ch,key=repr))
@lru_cache(None)
def queries(t):
    if t=='u':return (('+','-'),)
    if t in ('+','-'):return ()
    out=set()
    for i,c in enumerate(t):
        if i and t[i]==t[i-1]:continue
        for cp,cm in queries(c):
            out.add((norm(t[:i]+(cp,)+t[i+1:]),norm(t[:i]+(cm,)+t[i+1:])))
    return tuple(sorted(out,key=repr))
@lru_cache(None)
def V(t):
    if t in ('+','-'):return Fraction(0)
    return min(Fraction(1)+(V(a)+V(b))/2 for a,b in queries(t))
def full(k):return 'u' if k==0 else norm((full(k-1),)*3)
@lru_cache(None)
def q(t):
    if t=='+':return 1.0
    if t=='-':return 0.0
    if t=='u':return 0.5
    a,b,c=(q(x) for x in t)
    return a*b+a*c+b*c-2*a*b*c
@lru_cache(None)
def lottery(ws,qs):
    @lru_cache(None)
    def g(st):
        if sum(x==1 for x in st)>=2 or sum(x==0 for x in st)>=2:return 0.0
        best=float('inf')
        for i in range(3):
            if st[i] is None:
                sp=list(st);sm=list(st);sp[i]=1;sm[i]=0
                best=min(best,ws[i]+qs[i]*g(tuple(sp))+(1-qs[i])*g(tuple(sm)))
        return best
    init=tuple(None if 0<qs[i]<1 else int(qs[i]>.5) for i in range(3))
    return g(init)
@lru_cache(None)
def R(t):
    if t in ('+','-'):return 0.0
    return lottery(tuple(float(V(c)) for c in t),tuple(q(c) for c in t))
@lru_cache(None)
def child_opt_moves(c):
    if c=='u':return (('+','-'),)
    xs=[(Fraction(1)+(V(a)+V(b))/2,a,b) for a,b in queries(c)]
    m=min(z for z,a,b in xs)
    return tuple((a,b) for z,a,b in xs if z==m)
@lru_cache(None)
def base_policy(t):
    best=None
    for i,c in enumerate(t):
        if c in ('+','-'):continue
        if i and t[i]==t[i-1]:continue
        for cp,cm in child_opt_moves(c):
            tp=norm(t[:i]+(cp,)+t[i+1:]);tm=norm(t[:i]+(cm,)+t[i+1:])
            h=1.0+(R(tp)+R(tm))/2
            if best is None or h<best[0]-1e-12:best=(h,tp,tm)
    return best[1],best[2]
ROOT=full(4)
OLD_U=Fraction(1332788674231672015,36028797018963968)
MID_U=Fraction(1332632382813415759,36028797018963968)
NEW_U=Fraction(1332517664326644559,36028797018963968)

def make_ED(patches):
    def pol(t):return patches[t] if t in patches else base_policy(t)
    @lru_cache(None)
    def ED(t):
        if t in ('+','-'):return Fraction(0),Fraction(0)
        a,b=pol(t);Ea,Da=ED(a);Eb,Db=ED(b)
        return Fraction(1)+(Ea+Eb)/2,(Ea-Eb)+(Da+Db)/2
    return pol,ED
def layer(pol,d):
    S={ROOT}
    for _ in range(d):
        T=set()
        for s in S:
            if s not in ('+','-'):T.update(pol(s))
        S=T
    return S
def defect(ED,s,mv):
    E,D=ED(s);a,b=mv;Ea,Da=ED(a);Eb,Db=ED(b)
    return E-(Fraction(1)+(Ea+Eb)/2), D-((Ea-Eb)+(Da+Db)/2)
def flip(t):
    if t=='+':return '-'
    if t=='-':return '+'
    if t=='u':return 'u'
    return norm(tuple(flip(c) for c in t))
def flip_move(mv):
    a,b=mv
    return flip(b),flip(a)

start=time.time()
pol0,ED0=make_ED(OLD)
assert ED0(ROOT)[0]==OLD_U
L7=layer(pol0,7)
assert set(N7)<=L7
g7=[];d7=[]
for s,mv in N7.items():
    assert mv in queries(s)
    g,d=defect(ED0,s,mv);assert g>0
    g7.append(g);d7.append(d)
assert Counter(g7)==Counter({Fraction(18224279181,1099511627776):2})
assert Counter(d7)==Counter({Fraction(3142409184233,4398046511104):1,-Fraction(3142409184233,4398046511104):1})
P7=dict(OLD);P7.update(N7)
pol7,ED7=make_ED(P7)
assert ED7(ROOT)[0]==MID_U
L8=layer(pol7,8)
assert set(N8)<=L8
g8=[];d8=[]
for s,mv in N8.items():
    assert mv in queries(s)
    g,d=defect(ED7,s,mv);assert g>0
    g8.append(g);d8.append(d)
assert Counter(g8)==Counter({Fraction(2514971655,137438953472):2,Fraction(91533515,17179869184):2})
assert Counter(d8)==Counter({Fraction(3268295917,8589934592):1,-Fraction(3268295917,8589934592):1,Fraction(9062117167,68719476736):1,-Fraction(9062117167,68719476736):1})
P8=dict(P7);P8.update(N8)
pol8,ED8=make_ED(P8)
assert ED8(ROOT)[0]==NEW_U

ALLNEW=dict(N7);ALLNEW.update(N8)
seen=set();orbits=[]
for s,mv in ALLNEW.items():
    if s in seen:continue
    fs=flip(s);assert fs in ALLNEW and ALLNEW[fs]==flip_move(mv)
    o={s,fs};assert len(o)==2;seen|=o;orbits.append(o)
assert len(orbits)==3 and seen==set(ALLNEW)

print('old_U',OLD_U,float(OLD_U))
print('depth7_states',len(L7),'new_patches',len(N7),'defects',Counter(g7))
print('depth7_bias_derivatives',Counter(d7))
print('mid_U',MID_U,float(MID_U))
print('depth8_states',len(L8),'new_patches',len(N8),'defects',Counter(g8))
print('depth8_bias_derivatives',Counter(d8))
print('new_U',NEW_U,float(NEW_U))
print('global_sign_orbits',len(orbits),'sizes',[len(o) for o in orbits])
print('total_exact_gain',OLD_U-NEW_U,float(OLD_U-NEW_U))

getcontext().prec=70
D=Decimal;ln3=D(3).ln();dec=lambda f:D(f.numerator)/D(f.denominator)
siglo=D(1)-(dec(NEW_U).ln()/D(4))/ln3
sighi=(D(4)/D(3)).ln()/ln3
W=sighi-siglo
oldlo=D('0.178347476400834359946482097379537497368908069843')
oldW=D('0.083512030742080514252572131305984211230263210420')
assert siglo>oldlo and W<oldW
print('stationary_4block_growth',dec(NEW_U)**(D(1)/D(4)))
print('sigma_lower',siglo)
print('sigma_upper',sighi)
print('W_sigma',W)
print('sigma_gain',siglo-oldlo)
print('width_contraction',oldW-W)
print('runtime_seconds',round(time.time()-start,3))
print('ALL_EXACT_PARAMETER_SYMMETRY_MDP_CHECKS_PASS')
