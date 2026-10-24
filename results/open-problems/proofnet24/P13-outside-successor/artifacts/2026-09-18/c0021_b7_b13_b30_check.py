from fractions import Fraction
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import ast,zlib,base64

def dec(s): return ast.literal_eval(zlib.decompress(base64.b85decode(s)).decode())
OLD=dec('c-rloOAdoD3`DQOE}-BG^j@s0-n}IiJF2RmMAppf0#&Gp$b+9J#=XvuPpM^{%Jw`g>ogzVU!2&_y!*|cE^1c|x|iqzm&?AwGnFer)KR&u@I=!fhB_i2DhEMy1U9*>2kby(17N35Wwrng4x5T%;II+7hr`YmM79794jXr9;II+7hr_M_8;6bgQgGN6U;}JgA^>}Y%DffT12$E;2e3EFGQdV<df14}OGjEF^sq5s02`5=S|V(gKLvIR8Oq8+I!Iq8Lny@(t~yXz7}zah2rCF_JQnVGVBnHIZutS6I8B2z{RP03R#gD!R5ra`#|?i~S#v&Z^pYLM>k?NB#_KFpX1vZoWTxH?#!2`C3&19ZBEY`g0kI9`9s')
N7=dec('c-pJh&`{S_*HHjcr9cWsXaYqD2xyX}39JiZC5kF-8rVgN1L<NHc@EUHf(Id80|jE^XiSk1Q;1+2fb69^n!U)1G>AT3`p23sx+>k#SR=7e)ExwQZ8X+MEFkF~X%HJnBZ`zlu@(TC6AJk')
N8=dec('c-pJh&`{S_*HHjcr9cWsXaYqD2xyX}39JiZCC%-k#DTi#s&og912wJSK{(K{rac;KM8_If+hB+^-O)%RI?^EebVsuq;aDpjYz5?KtPQEcU^J@@-2!p|sx{pqSFM$fwjf6vBSWzTsXH2Jqb<l0H3l%+f*gtt9L;J&vDvR#3jkFi8gT')
P10=dec('c-rlmO%4Jf3`VcwZiZkl;JsWK?=CXYXyOm8FrAvWfn*YB;n9zlInDEwr~R&U$I{)JRK9%qkW7P?QF66d+urlrom%!`xGkH5>2UWDQZGp5?U1U&0QCmcb{vG%6DdLbh$+NxXh<P`#;ZF+%~c4i#isdJ$;<+fat$w0+5+06D2h{fWy)ct5JD<QISi;M<uIh8l*5n;QVs)(%rD~A{R1`mYaujNS*x6XGQ!Vqgn&|tqUJU+Ek+PdpA52{tl|hj(??L%VJd`ajI31icgyr-r`-X_b`xMFSy3(~6SGcY+zNJJYy-1{0G}^^r7k@')
assert (len(OLD),len(N7),len(N8),len(P10))==(14,2,4,8)

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
    if t=='+':return Fraction(1)
    if t=='-':return Fraction(0)
    if t=='u':return Fraction(1,2)
    a,b,c=(q(x) for x in t)
    return a*b+a*c+b*c-2*a*b*c
@lru_cache(None)
def lottery(ws,qs):
    @lru_cache(None)
    def g(st):
        if sum(x==1 for x in st)>=2 or sum(x==0 for x in st)>=2:return Fraction(0)
        best=None
        for i in range(3):
            if st[i] is None:
                sp=list(st);sm=list(st);sp[i]=1;sm[i]=0
                v=ws[i]+qs[i]*g(tuple(sp))+(1-qs[i])*g(tuple(sm))
                best=v if best is None or v<best else best
        return best
    init=tuple(None if 0<qs[i]<1 else int(qs[i]>Fraction(1,2)) for i in range(3))
    return g(init)
@lru_cache(None)
def R(t):
    if t in ('+','-'):return Fraction(0)
    return lottery(tuple(V(c) for c in t),tuple(q(c) for c in t))
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
            h=Fraction(1)+(R(tp)+R(tm))/2
            if best is None or h<best[0]:best=(h,tp,tm)
    return best[1],best[2]
ROOT=full(4)
U8=Fraction(1332517664326644559,36028797018963968)
U10=Fraction(1332501816044412239,36028797018963968)

def make_E(patches):
    def pol(t):return patches[t] if t in patches else base_policy(t)
    @lru_cache(None)
    def E(t):
        if t in ('+','-'):return Fraction(0)
        a,b=pol(t)
        return Fraction(1)+(E(a)+E(b))/2
    return pol,E

def layer(pol,d):
    S={ROOT}
    for _ in range(d):
        T=set()
        for s in S:
            if s not in ('+','-'):T.update(pol(s))
        S=T
    return S

def defect(E,s,mv):
    a,b=mv
    return E(s)-(Fraction(1)+(E(a)+E(b))/2)
def flip(t):
    if t=='+':return '-'
    if t=='-':return '+'
    if t=='u':return 'u'
    return norm(tuple(flip(c) for c in t))
def flip_move(mv):
    a,b=mv;return flip(b),flip(a)
def info_gap_sq(mv):return (q(mv[0])-q(mv[1]))**2

P8=dict(OLD);P8.update(N7);P8.update(N8)
pol8,E8=make_E(P8)
assert E8(ROOT)==U8
L10=layer(pol8,10)
assert set(P10)<=L10
G=[]
for s,mv in P10.items():
    assert mv in queries(s)
    g=defect(E8,s,mv);assert g>0;G.append(g)
assert Counter(G)==Counter({
    Fraction(298677,4294967296):2,
    Fraction(352919261,34359738368):2,
    Fraction(78965,16777216):2,
    Fraction(2679195,268435456):2,
})
# Global sign quotient: the eight new states are four two-state orbits, actions conjugate.
seen=set();orbits=[]
for s,mv in P10.items():
    if s in seen:continue
    fs=flip(s);assert fs in P10 and P10[fs]==flip_move(mv)
    seen|={s,fs};orbits.append((s,fs))
assert len(orbits)==4 and seen==set(P10)
# Immediate posterior-variance heuristic is insufficient: at least one strict Bellman
# improvement ties the incumbent in one-step posterior gap squared.
assert any(info_gap_sq(P10[s])==info_gap_sq(pol8(s)) for s in P10)
# It is sometimes directionally useful too.
assert any(info_gap_sq(P10[s])>info_gap_sq(pol8(s)) for s in P10)

PNEW=dict(P8);PNEW.update(P10)
poln,En=make_E(PNEW)
assert En(ROOT)==U10
assert U10<U8
getcontext().prec=70
D=Decimal;decf=lambda f:D(f.numerator)/D(f.denominator);ln3=D(3).ln()
siglo=D(1)-(decf(U10).ln()/D(4))/ln3
sighi=(D(4)/D(3)).ln()/ln3
W=sighi-siglo
oldW=D('0.083465753913852208758272209478431018739772696616')
assert W<oldW
print('old_U',U8,float(U8))
print('new_depth4_policy_U',U10,float(U10))
print('exact_gain',U8-U10,float(U8-U10))
print('new_patch_count',len(P10),'sign_orbits',len(orbits))
print('defect_multiset',Counter(G))
print('information_ties',sum(info_gap_sq(P10[s])==info_gap_sq(pol8(s)) for s in P10))
print('information_strict_improvements',sum(info_gap_sq(P10[s])>info_gap_sq(pol8(s)) for s in P10))
print('growth_upper',decf(U10)**(D(1)/D(4)))
print('sigma_lower',siglo)
print('sigma_upper',sighi)
print('W_sigma',W)
print('width_contraction',oldW-W)
print('ALL_EXACT_B7_B13_B30_CHECKS_PASS')
