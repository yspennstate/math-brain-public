from fractions import Fraction
from functools import lru_cache
from collections import Counter
from decimal import Decimal, getcontext
import ast, zlib, base64, sys
sys.setrecursionlimit(1000000)

CURRENT_B85 = "c-rmTL2d#u429vVunQ>U0^EyL)w{P0Vn<bV=nRhiu|R0Vh{$jJ=h+S)$M09`?R;q0``hV!I6glAaN&04x9|MZP0L+7{Z`Tio-Vf)K2y01Vjh*36+Y2)h+!U)A1V()tO#tmoDbN8$OV8MK9!XK6&$u5rGUdG@)iy|S`d{06&yBqSioTuc?*Z#0h_~SzA`xM4%mRLB?8!csB9{l57>6)Er5NsEdw@{^{|O-=%^*4hs}HeHjyi}L=?+^1@;m$%BF?%kiJfa*osrQ>Otkiz+NIo*o2VgvAE|Q0~hphix1$yX*#6oD*(2&W(9CeWy9NbZg|zs8uMw>ORjLdF7R&QcwGsV9j_}OvQzH`j+6KU3t)?3B4FPu6G54)een*}v?g8z>i(i>JFJ9aZwk!$pt!qg24?F(*qdS4d{7*qI8*cY%}!A>cP6K(p_9Zl8a{=0jrwZyI!L|7$pC5ClLC-(Ej}O(W0cq>0ZFyFsx_%LBOpJ&0Q|)XJp"
GROUPS_B85 = "c-rk;(Qd*p4E&Y8L1iqh+Z+GYC)9sm)e0sivBfD#&hfoa2~kpfv9Zq=-=>f2a66w*a=HxbWnM4$mvMdPpEt&=o3^|5C7(Ve32RBk2h`u6(gJJcJ>YnKn6N5p`-(~5p9OD+Nd1_tfqSWOErPa#)(ExD1W1N>5vgYeLMKQ`^g!qZD74^bF<e%Bu!ev99quG+G$X6VA0yqxE+1KDI<N(On_#{x`_x9ooiO_}W}igLN%l#goMfLw>eb&AgCBj0!H>LS1d>F_JCe>K@5r(@ZrySKHSIbJ%xrL0+5aqu{|<@-%G``ePo=Ydj52VxYR04@YuExrvsDAe=%z|H#m`EY%P>t(DoMekPz=JnOpIn9#dv8$5D|0Hot3B)oJxhZ;!z@oGNIdGrqz9i=-3M9(sm#q9kPbP2LxaZ4;w{dqUPJxG$v@xP9OnyExfc<5RPRk7+a5wnr~MN3fji-eKtA=-P1ub>05e(c=j1?`%rG<<PbJhp_JJ86<TBJe&|xbS|4kV9#n9_2{@4Q8BWG2ESag~j+~fNWoQIXpyOwpaA;EO-NSGQioo+2%CDWFM6NEVJ@-+tht`tg7wOc7x9nWE5IC?Cjer6?v)DffpsZn>?a!WX+x?G5BL>_4(7jsZu6oTGupG>P7^zA#T{)Ql=&6pN;Ec=i4SRU_9s"
CURRENT = ast.literal_eval(zlib.decompress(base64.b85decode(CURRENT_B85)).decode())
GROUPS = ast.literal_eval(zlib.decompress(base64.b85decode(GROUPS_B85)).decode())
assert len(CURRENT) == 20
assert {d: len(GROUPS[d]) for d in GROUPS} == {10:8, 11:4, 12:4, 13:4}

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
                sp=list(st); sm=list(st); sp[i]=1; sm[i]=0
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
            h=1.0+(R(tp)+R(tm))/2
            if best is None or h<best[0]-1e-12:best=(h,tp,tm)
    return best[1],best[2]
ROOT=full(4)

def make_ED(patches):
    def pol(t):return patches[t] if t in patches else base_policy(t)
    @lru_cache(None)
    def ED(t):
        if t in ('+','-'):return Fraction(0),Fraction(0)
        a,b=pol(t); Ea,Da=ED(a); Eb,Db=ED(b)
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

def flip(t):
    if t=='+':return '-'
    if t=='-':return '+'
    if t=='u':return 'u'
    return norm(tuple(flip(c) for c in t))
def flip_move(mv):
    a,b=mv
    return flip(b),flip(a)

EXPECTED={
    0: Fraction(1332517664326644559,36028797018963968),
    10: Fraction(1332501816044412239,36028797018963968),
    11: Fraction(1332497576336439119,36028797018963968),
    12: Fraction(1332495381349676879,36028797018963968),
    13: Fraction(1332477360033879887,36028797018963968),
}
patch=dict(CURRENT)
pol,ED=make_ED(patch)
assert ED(ROOT)[0]==EXPECTED[0]
print('U_before',ED(ROOT)[0],float(ED(ROOT)[0]))

for d in (10,11,12,13):
    oldpol,oldED=make_ED(patch)
    states=layer(oldpol,d)
    adds=GROUPS[d]
    assert set(adds)<=states
    assert all(mv in queries(s) for s,mv in adds.items())
    assert all(flip(s) in adds and adds[flip(s)]==flip_move(mv) for s,mv in adds.items())
    defects=[]; derivs=[]
    for s,mv in adds.items():
        E0,K0=oldED(s); a,b=mv; Ea,Ka=oldED(a); Eb,Kb=oldED(b)
        defects.append(E0-(Fraction(1)+(Ea+Eb)/2))
        derivs.append(K0-((Ea-Eb)+(Ka+Kb)/2))
    assert all(x>0 for x in defects)
    assert Counter(derivs)==Counter([-x for x in derivs])
    before=oldED(ROOT)[0]
    newpatch=dict(patch); newpatch.update(adds)
    newpol,newED=make_ED(newpatch)
    after=newED(ROOT)[0]
    assert after==EXPECTED[d]

    @lru_cache(None)
    def G(s):
        if s in ('+','-'):return Fraction(0)
        a,b=newpol(s)
        delta=oldED(s)[0]-(Fraction(1)+(oldED(a)[0]+oldED(b)[0])/2)
        return delta+(G(a)+G(b))/2
    assert G(ROOT)==before-after
    print('stage',d,'states',len(states),'patches',len(adds),'orbits',len(adds)//2)
    print('  defects',Counter(defects))
    print('  derivative_pairs',Counter(derivs))
    print('  U',before,'->',after,'gain',before-after)
    print('  performance_difference',G(ROOT))
    patch=newpatch

assert len(patch)==40
U=make_ED(patch)[1](ROOT)[0]
assert U==EXPECTED[13]
OLD=EXPECTED[0]
print('total_patches',len(patch),'new_patches',len(patch)-len(CURRENT))
print('U_after',U,float(U))
print('exact_U_gain',OLD-U,float(OLD-U))

getcontext().prec=80
D=Decimal; ln3=D(3).ln(); dec=lambda f:D(f.numerator)/D(f.denominator)
siglo=D(1)-(dec(U).ln()/D(4))/ln3
sighi=(D(4)/D(3)).ln()/ln3
W=sighi-siglo
oldlo=D('0.1783937532290626654407820192070906898593985836476')
oldW=D('0.0834657539138522087582722094784310187397726966161')
assert siglo>oldlo and W<oldW
print('stationary_4block_growth',dec(U)**(D(1)/D(4)))
print('sigma_lower',siglo)
print('sigma_upper',sighi)
print('W_sigma',W)
print('sigma_gain',siglo-oldlo)
print('width_contraction',oldW-W)
print('ALL_EXACT_STRONGER_POLICY_PERFORMANCE_CHECKS_PASS')
