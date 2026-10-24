from fractions import Fraction
from functools import lru_cache
from decimal import Decimal, getcontext
import ast, zlib, base64, hashlib

BASE40_B85 = 'c-rlq%}&EW41`~$w{5ib3-De&A>JLDs<$Gv8`c@y9|wdgD$<>JG9Lf%dHwlnz1=SD{`|JxF4x!3zr65x<*(oQr#J2Ia{60IFL3*KT;V&EJBOGD<^2lZU}~IU9*|!s8;4ktu!-e-gl&LafUxC5nG~Rc!sdxmKw$&&3Wcq9h@=1&6gKLxfWijk6$-mU*eGnoR|bXMA#4a6O9aC9K$)s&KEmdyyn?XrJeDDBP{zXsWQvYhB6!${F9;iuD_J5W%cF$79~sD|C21pk=?vjfoI+I_C?_WD{low^AxWdLP|uDBCwjZ-6R>cY8ew{bfO)iLC16ct<>fkRc<RZjdAH#uS7@&jep=98R{~|)>k5EO*L#6>5(ZcxY|bzdVLvky4kea-aRzEw69);^A2e)-NmA^M1T!8fx}!$HY>o(fqZk&C6b(|0Wd5G46ftunDMbvOB&w0(le}ugSBtA4@fw2>B*mT-1WByv6C}kLQtXlh32L#jH9`#qxfrz$Y669s`wUVY)p%-Q2GHb5QF(ZVR5~J3y*d#_0ZOjneBj`w_+ga((fTKhXioJecCt9}5zU3M4VYm)%P3n>@G03}6Qxl+2vCrpC{h$@h$+Yq-?5}gLJJRe7QQ2CFZ}~Es97t}s$+{?XVT#XqzF(87Zy)_7=t*~7ZwlP0-&kCuy|^28emUO$-AC;GSHHjdqKtOg8-4?bbCso1CCRQZF*+NK!T8c1({>)fX-OTy!spfB%xo}xxj#<eVzjm%BaN-HLD3)tci8w0s}6G@bu}GQHvdFMM0xCAeL%m-dXbYA&i0yUegImTTR^NYRz6BLQ1&5XS6Oa+GN4j8_AX#w&5&plW_`1w&b`hieTzoUvbKzNrQKWg%C7;Crs7pG>?(0m+l-75=L}_pX4Hk`9H0xtIy023KUeB2dqRwRC@*Pe>DTK*zGS}rB$w{dv1JX4gX=JoHn?!hX3d!M^SLLuWwE6`P='
EXTRA6_B85 = 'c-rlmO%4Jf427@a4kp+OcrRAQyPKII+62c?u(itDupmSE`RL2*aE&pfa6a)i<h@zej?6pOo*3xuH}#-x)Qiw9b0y(i+o0UHz-nKlFjwCKm&@Y_)k&53xra`glMXvJn=~TfmH=u8^*njrep-Y^1TT9RJhBu#OH$IDGP&peuaaR(mH2=&B6w<gBA^dCM<VBePNjwrHZO1l6#rJtxX;!j((dEot&d97@6!=roS`grlP-jGfp7jTXQoXjfsWsj6GhF4OT(|~nI971p*=n%l=uWV?ZS4u15q};wg'

def decode(s):
    return ast.literal_eval(zlib.decompress(base64.b85decode(s)).decode())
BASE40=decode(BASE40_B85); EXTRA6=decode(EXTRA6_B85)
assert len(BASE40)==40 and len(EXTRA6)==6
assert hashlib.sha256(repr(BASE40).encode()).hexdigest()=='57124f0c264baea225bd8f798d33613597b11b9722e60a4173652e81abd2a4bc'
assert hashlib.sha256(repr(EXTRA6).encode()).hexdigest()=='1bfa88bba17a43119adb3db6e0e45ce3ab28a8910d1d36360341d7d9d1674876'

def norm(ch):
    p=sum(c=='+' for c in ch); m=sum(c=='-' for c in ch)
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
@lru_cache(None)
def q_frac(t):
    if t=='+':return Fraction(1)
    if t=='-':return Fraction(0)
    if t=='u':return Fraction(1,2)
    a,b,c=(q_frac(x) for x in t)
    return a*b+a*c+b*c-2*a*b*c
@lru_cache(None)
def lottery_frac(ws,qs):
    @lru_cache(None)
    def g(st):
        if sum(x==1 for x in st)>=2 or sum(x==0 for x in st)>=2:return Fraction(0)
        best=None
        for i in range(3):
            if st[i] is None:
                sp=list(st); sm=list(st); sp[i]=1; sm[i]=0
                h=ws[i]+qs[i]*g(tuple(sp))+(1-qs[i])*g(tuple(sm))
                if best is None or h<best:best=h
        return best
    init=tuple(None if 0<qs[i]<1 else int(qs[i]>Fraction(1,2)) for i in range(3))
    return g(init)
@lru_cache(None)
def R_frac(t):
    if t in ('+','-'):return Fraction(0)
    return lottery_frac(tuple(V(c) for c in t),tuple(q_frac(c) for c in t))
@lru_cache(None)
def child_opt_moves(c):
    if c=='u':return (('+','-'),)
    xs=[(Fraction(1)+(V(a)+V(b))/2,a,b) for a,b in queries(c)]
    z=min(v for v,a,b in xs)
    return tuple((a,b) for v,a,b in xs if v==z)
@lru_cache(None)
def base_policy(t):
    best=None
    for i,c in enumerate(t):
        if c in ('+','-'):continue
        if i and t[i]==t[i-1]:continue
        for cp,cm in child_opt_moves(c):
            tp=norm(t[:i]+(cp,)+t[i+1:]); tm=norm(t[:i]+(cm,)+t[i+1:])
            h=Fraction(1)+R_frac(tp)/2+R_frac(tm)/2
            if best is None or h<best[0]:best=(h,tp,tm)
    return best[1],best[2]
def flip(t):
    if t=='+':return '-'
    if t=='-':return '+'
    if t=='u':return 'u'
    return norm(tuple(flip(c) for c in t))
def flip_move(mv):
    a,b=mv
    return flip(b),flip(a)
def make_ED(patches):
    def pol(t):return patches[t] if t in patches else base_policy(t)
    @lru_cache(None)
    def ED(t):
        if t in ('+','-'):return Fraction(0)
        a,b=pol(t)
        return Fraction(1)+(ED(a)+ED(b))/2
    return pol,ED
def full(k):return 'u' if k==0 else norm((full(k-1),)*3)
ROOT=full(4)
def defect(ED,s,mv):
    return ED(s)-(Fraction(1)+(ED(mv[0])+ED(mv[1]))/2)
def layer(pol,d):
    S={ROOT}
    for _ in range(d):
        T=set()
        for s in S:
            if s not in ('+','-'):T.update(pol(s))
        S=T
    return S

# The six new actions form three legal global-sign orbits.
assert all(mv in queries(s) for s,mv in EXTRA6.items())
for s,mv in EXTRA6.items():
    assert flip(s) in EXTRA6 and EXTRA6[flip(s)]==flip_move(mv)
assert not(set(BASE40)&set(EXTRA6))

oldpol,oldED=make_ED(BASE40)
OLD_U=oldED(ROOT)
assert OLD_U==Fraction(1332477360033879887,36028797018963968)

# B28: restrict attention to a finite set of actually reached clock-14 states.
# No exhaustiveness claim is made: the certificate checks only the six stored
# candidate states, all of which are reachable and have strict positive defect.
S14=layer(oldpol,14)
assert len(S14)==1021
assert set(EXTRA6) <= S14
positive={}
for s,mv in EXTRA6.items():
    d=defect(oldED,s,mv)
    assert d>0
    positive[s]=(d,mv)
assert sorted([d for d,mv in positive.values()])==sorted([
    Fraction(346565,33554432)]*2+
    [Fraction(25155,4194304)]*2+
    [Fraction(16875,33554432)]*2)

# Make the three sign orbits and sort by decreasing defect.
unseen=set(EXTRA6); orbits=[]
while unseen:
    s=min(unseen,key=repr); fs=flip(s)
    orbits.append((positive[s][0],s,fs))
    unseen.remove(s); unseen.remove(fs)
orbits.sort(reverse=True,key=lambda z:z[0])
assert [z[0] for z in orbits]==[
    Fraction(346565,33554432),
    Fraction(25155,4194304),
    Fraction(16875,33554432)]

# Stage 1, largest defect.
d1,s1,fs1=orbits[0]
P42=dict(BASE40); P42[s1]=EXTRA6[s1]; P42[fs1]=EXTRA6[fs1]
pol42,ED42=make_ED(P42); U42=ED42(ROOT); G1=OLD_U-U42
assert U42==Fraction(1332474770810722127,36028797018963968)
assert G1==Fraction(19754205,274877906944)
H1=G1/d1; assert H1==Fraction(57,8192)

# B10 obstruction: the exact buy-out surrogate prefers the old action at s1,
# while true continuation value strictly prefers the new interleaving action.
base_mv=oldpol(s1); new_mv=EXTRA6[s1]
R_base=Fraction(1)+(R_frac(base_mv[0])+R_frac(base_mv[1]))/2
R_new=Fraction(1)+(R_frac(new_mv[0])+R_frac(new_mv[1]))/2
T_base=Fraction(1)+(oldED(base_mv[0])+oldED(base_mv[1]))/2
T_new=Fraction(1)+(oldED(new_mv[0])+oldED(new_mv[1]))/2
assert R_new-R_base==Fraction(126785,134217728)>0
assert T_base-T_new==d1>0

# Stage 2, medium defect.
d3,s3,fs3=orbits[1]
assert defect(ED42,s3,EXTRA6[s3])==d3
assert defect(ED42,fs3,EXTRA6[fs3])==d3
P44=dict(P42); P44[s3]=EXTRA6[s3]; P44[fs3]=EXTRA6[fs3]
pol44,ED44=make_ED(P44); U44=ED44(ROOT); G3=U42-U44
assert U44==Fraction(1332472797486700367,36028797018963968)
assert G3==Fraction(30110535,549755813888)
H3=G3/d3; assert H3==Fraction(1197,131072)

# Stage 3, smallest positive orbit.
d2,s2,fs2=orbits[2]
assert defect(ED44,s2,EXTRA6[s2])==d2
assert defect(ED44,fs2,EXTRA6[fs2])==d2
P46=dict(P44); P46[s2]=EXTRA6[s2]; P46[fs2]=EXTRA6[fs2]
pol46,ED46=make_ED(P46); NEW_U=ED46(ROOT); G2=U44-NEW_U
assert NEW_U==Fraction(1332472567939180367,36028797018963968)
assert G2==Fraction(56041875,8796093022208)
H2=G2/d2; assert H2==Fraction(3321,262144)
TOTAL_GAIN=OLD_U-NEW_U
assert TOTAL_GAIN==Fraction(1169944995,8796093022208)

# All three orbit representatives really occur at clock 14 under the old
# policy. H1,H3,H2 are total-hit masses when canonicalization permits the same
# type at more than one raw query clock.
for _,s,fs in orbits:
    assert s in S14 and fs in S14

# Frozen source metric.
getcontext().prec=90
dec=lambda f:Decimal(f.numerator)/Decimal(f.denominator)
ln3=Decimal(3).ln()
sigma_upper=(Decimal(4)/Decimal(3)).ln()/ln3
sigma_old=Decimal(1)-(dec(OLD_U).ln()/Decimal(4))/ln3
sigma_new=Decimal(1)-(dec(NEW_U).ln()/Decimal(4))/ln3
W_old=sigma_upper-sigma_old; W_new=sigma_upper-sigma_new
assert sigma_new>sigma_old and W_new<W_old

print('base40_sha256',hashlib.sha256(repr(BASE40).encode()).hexdigest())
print('extra6_sha256',hashlib.sha256(repr(EXTRA6).encode()).hexdigest())
print('clock14_state_count',len(S14))
print('clock14_certified_improving_states',len(positive))
print('clock14_certified_improving_sign_orbits',len(orbits))
print('orbit1_defect',d1,'total_hit',H1,'root_gain',G1)
print('orbit2_defect',d3,'total_hit',H3,'root_gain',G3)
print('orbit3_defect',d2,'total_hit',H2,'root_gain',G2)
print('B10_R_base',R_base)
print('B10_R_new',R_new)
print('B10_surrogate_penalty',R_new-R_base)
print('B10_true_base',T_base)
print('B10_true_new',T_new)
print('B10_true_advantage',T_base-T_new)
print('old_U4',OLD_U)
print('new_U4',NEW_U)
print('total_U4_gain',TOTAL_GAIN)
print('new_patch_count',len(P46))
print('stationary_4block_growth_upper',dec(NEW_U)**(Decimal(1)/Decimal(4)))
print('sigma_lower_old',sigma_old)
print('sigma_lower_new',sigma_new)
print('sigma_upper',sigma_upper)
print('W_sigma_old',W_old)
print('W_sigma_new',W_new)
print('width_contraction',W_old-W_new)
print('ALL_EXACT_CLOCK14_TYPICAL_PATCH_CHECKS_PASS')
