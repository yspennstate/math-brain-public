#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
from itertools import product
import math

getcontext().prec = 70
D = Decimal
LN2 = D(2).ln()

def h2d(x):
    x = D(x)
    if x == 0 or x == 1:
        return D(0)
    return -(x*x.ln() + (1-x)*(1-x).ln())/LN2

def solve_c(r):
    r = [D(x.numerator)/D(x.denominator) if isinstance(x, Fraction) else D(x) for x in r]
    mu = sum(r)
    if mu == 1:
        return D(1)
    def f(c):
        z = D(1)
        for x in r:
            z *= (1-c*x)
        return 1-c-z
    lo, hi = D('1e-50'), D(1)
    for _ in range(260):
        mid = (lo+hi)/2
        if f(mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

def q_from_r(r):
    c = solve_c(r)
    n = len(r)
    if sum(r) == 1:
        q = {1<<i: D(x.numerator)/D(x.denominator) for i,x in enumerate(r) if x}
        return q,c
    rd = [D(x.numerator)/D(x.denominator) if isinstance(x,Fraction) else D(x) for x in r]
    t = [c*x for x in rd]
    q = {}
    for mask in range(1,1<<n):
        z = D(1)
        for i,x in enumerate(t):
            z *= x if ((mask>>i)&1) else (1-x)
        q[mask] = z/c
    return q,c

def entropy_dec(dist):
    ans=D(0)
    for x in dist.values():
        if x:
            ans -= x*x.ln()/LN2
    return ans

def twoflip_P(k):
    q = Fraction(1, 2**(k-2))
    out = {1:(1-q)**2}
    for mask in range(1<<k):
        exactly_one = bool(mask&1) ^ bool(mask&2)
        if exactly_one and mask != 1:
            out[mask]=q*q
    assert sum(out.values()) == 1
    return out

def marginals(P,n):
    return [sum(v for m,v in P.items() if (m>>i)&1) for i in range(n)]

def influence(P):
    return sum(Fraction(m.bit_count())*v for m,v in P.items())

def min_half_signed_gap(weights):
    N=len(weights)
    total=sum(weights,D(0))
    best=abs(total)
    for bits in range(1<<N):
        s=D(0)
        for j,w in enumerate(weights):
            if (bits>>j)&1:
                s += w
        val=abs(total-2*s)
        if val < best:
            best=val
    return best

def uniform_quadratic_gap(Q,n,U):
    seen=set()
    weights=[]
    for S in range(1<<n):
        if S in seen: continue
        T=S^U
        seen.add(S); seen.add(T)
        weights.append((Q.get(S,D(0))*Q.get(T,D(0))).sqrt())
    return 2*min_half_signed_gap(weights)

def full_active_d(r,c):
    td=[c*(D(x.numerator)/D(x.denominator)) for x in r]
    z=D(1)/c
    for t in td:
        z *= (t*(1-t)).sqrt()
    return z

def walsh4_boolean_check():
    W=[0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0]
    vals=[]
    for x in range(16):
        num=sum(W[s]*((-1)**((s&x).bit_count())) for s in range(16))
        assert num % 16 == 0
        vals.append(num//16)
    assert set(vals) <= {-1,1} and len(set(vals))==2
    P={s:Fraction(a*a,256) for s,a in enumerate(W) if a}
    assert sum(P.values())==1 and P.get(0,Fraction(0))==0
    r=marginals(P,4)
    assert r == [Fraction(1,4),Fraction(1,4),Fraction(1,4),Fraction(3,4)]
    Q,c=q_from_r(r)
    Pd={m:D(v.numerator)/D(v.denominator) for m,v in P.items()}
    K=entropy_dec(Q)-entropy_dec(Pd)
    gaps=[(uniform_quadratic_gap(Q,4,U),U) for U in range(1,16)]
    g,U=max(gaps,key=lambda z:z[0])
    lower=g*g/(D(4)*LN2)
    d=full_active_d(r,c)
    assert abs(g-2*d) < D('1e-55')
    assert lower < K
    return vals,r,c,K,g,U,lower

def twoflip_checks():
    rows=[]
    for k in range(3,9):
        P=twoflip_P(k)
        q=Fraction(1,2**(k-2))
        r=marginals(P,k)
        assert r == [1-q]+[q]*(k-1)
        I=influence(P)
        assert I-1 == (k-2)*q
        c=solve_c(r)
        assert c > D('0.5') and c < 1
        Q,_=q_from_r(r)
        Pd={m:D(v.numerator)/D(v.denominator) for m,v in P.items()}
        K=entropy_dec(Q)-entropy_dec(Pd)
        d=full_active_d(r,c)
        full_lb=d*d/LN2
        qd=D(q.numerator)/D(q.denominator)
        assert d <= qd**(D(k-1)/D(2)) + D('1e-55')
        assert full_lb < K
        row=[k,q,I-1,c,K,d,full_lb]
        if k<=5:
            gaps=[(uniform_quadratic_gap(Q,k,U),U) for U in range(1,1<<k)]
            g,U=max(gaps,key=lambda z:z[0])
            max_lb=g*g/(D(4)*LN2)
            assert max_lb < K
            row += [g,U,max_lb]
        rows.append(row)
    return rows

def biased_basis_coeffs_majority3():
    probs=[Fraction(3,8),Fraction(2,5),Fraction(1,3)]
    n=3
    pd=[D(p.numerator)/D(p.denominator) for p in probs]
    a=[]
    for S in range(1<<n):
        z=D(0)
        for x in range(1<<n):
            pr=D(1); phi=D(1); ones=0
            for i,p in enumerate(pd):
                bit=(x>>i)&1
                if bit: ones += 1
                pr *= p if bit else (1-p)
                if (S>>i)&1:
                    phi *= ((D(bit)-p)/(p*(1-p)).sqrt())
            f=D(1) if ones>=2 else D(-1)
            z += pr*f*phi
        a.append(z)
    assert abs(sum(x*x for x in a)-1) < D('1e-55')
    mean=a[0]
    v=1-mean*mean
    P={S:a[S]*a[S]/v for S in range(1,1<<n)}
    r=[sum(P[S] for S in P if (S>>i)&1) for i in range(n)]
    Q,c=q_from_r(r)
    K=entropy_dec(Q)-entropy_dec(P)
    kapp=[(1-2*p)/(p*(1-p)).sqrt() for p in pd]
    def local(si,ti,ui,i):
        if ui==0:
            return D(1) if si==ti else D(0)
        if si==0 and ti==0: return D(0)
        if si!=ti: return D(1)
        return kapp[i]
    def FU(vec,U):
        ans=D(0)
        for S in range(1<<n):
            for T in range(1<<n):
                cf=D(1)
                for i in range(n):
                    cf *= local((S>>i)&1,(T>>i)&1,(U>>i)&1,i)
                    if cf==0: break
                ans += vec[S]*vec[T]*cf
        return ans
    for U in range(1,1<<n):
        assert abs(FU(a,U)) < D('1e-50')
    best_lb=D(0); bestU=None; bestg=None
    supp=list(range(1,1<<n))
    for U in range(1,1<<n):
        g=None
        for bits in range(1<<len(supp)):
            b=[D(0)]*(1<<n); b[0]=mean
            for j,S in enumerate(supp):
                sign=D(1) if ((bits>>j)&1) else D(-1)
                b[S]=sign*(v*Q[S]).sqrt()
            val=abs(FU(b,U))
            if g is None or val<g:g=val
        L=D(1)
        for i,p in enumerate(pd):
            if (U>>i)&1:
                L *= (max(p,1-p)/min(p,1-p)).sqrt()
        lb=g*g/(D(4)*v*L*L*LN2)
        assert lb < K
        if lb>best_lb:
            best_lb,bestU,bestg=lb,U,g
    return probs,mean,v,r,c,K,bestg,bestU,best_lb

vals,r4,c4,K4,g4,U4,lb4 = walsh4_boolean_check()
rows=twoflip_checks()
off=biased_basis_coeffs_majority3()

print('PASS')
print('four_bit_inverse_truth_values', ''.join('1' if x==1 else '0' for x in vals))
print('four_bit_r', [str(x) for x in r4])
print('four_bit_c', c4)
print('four_bit_K_occ', K4)
print('four_bit_max_quadratic_gap', g4, 'U', U4)
print('four_bit_KL_lower', lb4)
for row in rows:
    print('twoflip', *row)
print('biased_majority3_probs', [str(x) for x in off[0]])
print('biased_majority3_mean', off[1])
print('biased_majority3_v', off[2])
print('biased_majority3_r', off[3])
print('biased_majority3_c', off[4])
print('biased_majority3_K_occ', off[5])
print('biased_majority3_best_gap', off[6], 'U', off[7])
print('biased_majority3_KL_lower', off[8])
