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

# reconstruct P46 from BASE40 + EXTRA6 in sequential orbit order used in archived checker
oldpol,oldED=make_ED(BASE40)
positive={s:(defect(oldED,s,mv),mv) for s,mv in EXTRA6.items()}
unseen=set(EXTRA6); orbits=[]
while unseen:
    s=min(unseen,key=repr); fs=flip(s)
    orbits.append((positive[s][0],s,fs))
    unseen.remove(s); unseen.remove(fs)
orbits.sort(reverse=True,key=lambda z:z[0])
P46=dict(BASE40)
for _,s,fs in orbits:
    P46[s]=EXTRA6[s]; P46[fs]=EXTRA6[fs]
pol46,ED46=make_ED(P46)
U46=ED46(ROOT)
assert U46==Fraction(1332472567939180367,36028797018963968)

EXTRA15_B85 = 'c-rk&K@P+q2>eQK*06k_|LUpPzpu5nHQCKpXi7l6XkrjyhC!Bbbm(3~*ygb9iw`Fk2cC6ly9MiuasBVV*l<gN9LNvXC2xTUQhtgNw#!cPKXVv?M;JMBX<9BwOj?MX3@cG~Vm({{>UWb8LwbWr?0mV#2P)xKGi#Y0mUdW_G8<dF<Rt%!2szt1C3!jOgodCS&Bhpdpa(sBrKcyrtX)yYF-i1LyKq&br@8j*m0lNaO+T(J^q>p3o*!5Byn=mHuK35bReG9)`~CpWE7>0'
EXTRA15 = decode(EXTRA15_B85)
assert len(EXTRA15) == 6
assert hashlib.sha256(repr(EXTRA15).encode()).hexdigest() == '189ddcb04c39e3392583bcdaa78d051803492ac2ec32f1362c95451199c4fd1c'

# B26: six exact clock-15 improvement witnesses, paired by global sign.
S15 = layer(pol46, 15)
assert len(S15) == 1524
assert set(EXTRA15) <= S15
assert all(mv in queries(s) for s, mv in EXTRA15.items())
for s, mv in EXTRA15.items():
    assert flip(s) in EXTRA15
    assert EXTRA15[flip(s)] == flip_move(mv)

starting_defects = {s: defect(ED46, s, mv) for s, mv in EXTRA15.items()}
assert sorted(starting_defects.values()) == sorted(
    [Fraction(942705,67108864)]*2
    + [Fraction(10110183,1073741824)]*2
    + [Fraction(1988161,536870912)]*2
)

# Sequentially install the three sign orbits in decreasing starting-defect order.
unseen = set(EXTRA15)
new_orbits = []
while unseen:
    s = min(unseen, key=repr)
    fs = flip(s)
    assert fs != s
    new_orbits.append((starting_defects[s], s, fs))
    unseen.remove(s); unseen.remove(fs)
new_orbits.sort(reverse=True, key=lambda z: z[0])

P = dict(P46)
pol, ED = pol46, ED46
stage_rows = []
expected = [
    (Fraction(942705,67108864), Fraction(1213261335,17592186044416), Fraction(1287,262144),
     Fraction(1332470083179966287,36028797018963968)),
    (Fraction(10110183,1073741824), Fraction(242310755961,4503599627370496), Fraction(23967,4194304),
     Fraction(1332468144693918599,36028797018963968)),
    (Fraction(1988161,536870912), Fraction(47650254687,2251799813685248), Fraction(23967,4194304),
     Fraction(1332467382289843607,36028797018963968)),
]
Uprev = U46
for j, (d0, s, fs) in enumerate(new_orbits):
    ds = defect(ED, s, EXTRA15[s])
    dfs = defect(ED, fs, EXTRA15[fs])
    assert ds == dfs == expected[j][0]
    assert ds > 0
    P[s] = EXTRA15[s]; P[fs] = EXTRA15[fs]
    pol, ED = make_ED(P)
    Unew = ED(ROOT)
    gain = Uprev - Unew
    H = gain / ds
    assert gain == expected[j][1]
    assert H == expected[j][2]
    assert Unew == expected[j][3]
    stage_rows.append((ds, H, gain, Unew))
    Uprev = Unew

U52 = Uprev
assert len(P) == 52
assert U52 == Fraction(1332467382289843607,36028797018963968)
assert U46-U52 == Fraction(648206167095,4503599627370496)
def table_sha(d):
    rows = sorted((repr(k), repr(v)) for k,v in d.items())
    return hashlib.sha256(repr(rows).encode()).hexdigest()
assert table_sha(P) == '943e520577cc0131c482841c8b9967c4da47a3fce43bc22c78fb7d4bb6c70e75'

# B11 exact dual-slack values implied by the known D1,D2,D3.
D1 = Fraction(5,2)
D2 = Fraction(393,64)
D3 = Fraction(15796051,1048576)
slack1 = D1 - Fraction(9,4)
slack2 = D2 - Fraction(81,16)
slack3 = D3 - Fraction(729,64)
assert slack1 == Fraction(1,4)
assert slack2 == Fraction(69,64)
assert slack3 == Fraction(3852115,1048576)

getcontext().prec = 90
dec = lambda f: Decimal(f.numerator)/Decimal(f.denominator)
ln3 = Decimal(3).ln()
sigma_upper = (Decimal(4)/Decimal(3)).ln()/ln3
sigma46 = Decimal(1) - (dec(U46).ln()/Decimal(4))/ln3
sigma52 = Decimal(1) - (dec(U52).ln()/Decimal(4))/ln3
W46 = sigma_upper - sigma46
W52 = sigma_upper - sigma52
growth52 = dec(U52) ** (Decimal(1)/Decimal(4))
assert sigma52 > sigma46 and W52 < W46

print('extra15_sha256', hashlib.sha256(repr(EXTRA15).encode()).hexdigest())
print('policy52_canonical_sha256', table_sha(P))
print('clock15_reached_state_count', len(S15))
print('certified_clock15_improving_states', len(EXTRA15))
print('certified_clock15_sign_orbits', len(new_orbits))
for j,(d,H,g,U) in enumerate(stage_rows,1):
    print('stage',j,'defect',d,'total_hit',H,'root_gain',g,'U4',U)
print('D1_dual_slack', slack1)
print('D2_dual_slack', slack2)
print('D3_dual_slack', slack3)
print('U46', U46)
print('U52', U52)
print('U4_gain', U46-U52)
print('growth52', growth52)
print('sigma_lower46', sigma46)
print('sigma_lower52', sigma52)
print('sigma_upper', sigma_upper)
print('W_sigma46', W46)
print('W_sigma52', W52)
print('width_contraction', W46-W52)
print('ALL_EXACT_CLOCK15_SPORADIC_PATCH_CHECKS_PASS')
