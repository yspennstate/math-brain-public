from fractions import Fraction
from itertools import product

def bits(x,l):
    return tuple((x>>(l-1-i))&1 for i in range(l))

def enc(t):
    x=0
    for b in t: x=(x<<1)|b
    return x

def comp_state(s,l):
    a,b=s; m=(1<<l)-1
    return (m^a,m^b)

def swap_state(s,l):
    a,b=s; return (b,a)

def rev(x,l):
    r=0
    for i in range(l): r=(r<<1)|((x>>i)&1)
    return r

def rev_state(s,l):
    a,b=s; return (rev(a,l),rev(b,l))

def transform_value(h,l,g):
    m=1<<l
    out=[Fraction(0)]*(m*m)
    for a in range(m):
      for b in range(m):
        s=(a,b)
        if g=='C': t=comp_state(s,l)
        elif g=='S': t=swap_state(s,l)
        elif g=='R': t=rev_state(s,l)
        else: t=s
        out[a*m+b]=h[t[0]*m+t[1]]
    return out

def T(h,l):
    m=1<<l; mask=m-1
    out=[Fraction(0)]*(m*m)
    for a in range(m):
      ha=(a>>(l-1))&1; ta=(a<<1)&mask
      for b in range(m):
        hb=(b>>(l-1))&1; tb=(b<<1)&mask
        def H(x,y): return h[x*m+y]
        if ha==hb:
          out[a*m+b]=Fraction(1)+Fraction(sum(H(ta|u,tb|v) for u in (0,1) for v in (0,1)),4)
        else:
          qa=Fraction(H(ta,b)+H(ta|1,b),2)
          qb=Fraction(H(a,tb)+H(a,tb|1),2)
          out[a*m+b]=max(qa,qb)
    return out

def orbit_count_enum(l):
    m=1<<l
    seen=set(); cnt=0
    for a in range(m):
      for b in range(m):
        s=(a,b)
        if s in seen: continue
        orb={s,comp_state(s,l),swap_state(s,l),comp_state(swap_state(s,l),l)}
        seen.update(orb);cnt+=1
    return cnt

def orbit_formula(l):
    return (2**(2*l)+2**l+2**l)//4

# Exact Burnside/orbit verification.
for l in range(1,9):
    e=orbit_count_enum(l); f=orbit_formula(l)
    assert e==f,(l,e,f)
    print(f"ell={l} orbit_count={e} formula_pass=1")

n22=orbit_formula(22)
assert n22==4398048608256
print(f"ell=22 exact_Klein4_orbit_count={n22}")
print(f"ell=22 complement_only_count={2**43}")

# Exact threshold corresponding to retained deterministic lower endpoint.
L=Fraction(99083249,125000000)
r0=L/(2-L)
assert 2*r0/(1+r0)==L
print(f"L={L.numerator}/{L.denominator}")
print(f"r0={r0.numerator}/{r0.denominator}")
print(f"r0_decimal={float(r0):.15f}")
print("EXACT_BOUND_CONVERSION_THRESHOLD_PASS")

# Exhaust all {0,1}-valued potentials on S_2 (2^16 functions) and verify
# complement/swap equivariance exactly. This is a self-check of the algebraic theorem.
l=2;m=1<<l;N=m*m
for mask in range(1<<N):
    h=[Fraction((mask>>i)&1) for i in range(N)]
    Th=T(h,l)
    for g in ('C','S'):
        lhs=T(transform_value(h,l,g),l)
        rhs=transform_value(Th,l,g)
        if lhs!=rhs:
            raise AssertionError(("equivariance",g,mask))
print("EXHAUSTIVE_BINARY_POTENTIAL_EQUIVARIANCE_ELL2_PASS")

# Reversal is NOT an equivariance of the one-sided lookahead operator.
h=[Fraction(0)]*N
h[0]=Fraction(1) # indicator of (00,00)
lhs=T(transform_value(h,l,'R'),l)
rhs=transform_value(T(h,l),l,'R')
st=(0,1) # (00,01)
idx=st[0]*m+st[1]
assert lhs[idx]==1 and rhs[idx]==Fraction(1,2)
print("REVERSAL_COUNTEREXAMPLE_ELL2 state=(00,01) T(Rh)=1 R(Th)=1/2")
print("EXACT_REVERSAL_NONEQUIVARIANCE_PASS")
print("ALL_EXACT_CHECKS_PASS")
