#!/usr/bin/env python3
from fractions import Fraction
from decimal import Decimal, getcontext
import math

getcontext().prec = 80

def log2_interval_fraction(x, terms=140):
    """Rigorous rational enclosure for log2(x), x>0.

    Normalize x=2^k*y with y in [1,2), then use
    ln y = 2 sum_{j>=0} z^(2j+1)/(2j+1), z=(y-1)/(y+1),
    with an explicit positive tail bound.
    Divide by a rational enclosure for ln 2 computed by the same series.
    """
    if x <= 0:
        raise ValueError("x must be positive")
    n, d = x.numerator, x.denominator
    k = n.bit_length() - d.bit_length()
    if k >= 0:
        y = x / (1 << k)
    else:
        y = x * (1 << (-k))
    while y < 1:
        k -= 1
        y *= 2
    while y >= 2:
        k += 1
        y /= 2

    def ln_interval(y):
        z = (y - 1) / (y + 1)
        zz = z * z
        term = z
        s = Fraction(0)
        for j in range(terms):
            s += term / (2*j + 1)
            term *= zz
        lo = 2*s
        tail = 2*term / ((2*terms + 1) * (1 - zz))
        hi = lo + tail
        return lo, hi

    ln_y_lo, ln_y_hi = ln_interval(y)
    ln2_lo, ln2_hi = ln_interval(Fraction(2,1))
    if k >= 0:
        num_lo = k*ln2_lo + ln_y_lo
        num_hi = k*ln2_hi + ln_y_hi
    else:
        num_lo = k*ln2_hi + ln_y_lo
        num_hi = k*ln2_lo + ln_y_hi
    return num_lo / ln2_hi, num_hi / ln2_lo

def entropy_term_interval(p):
    if p == 0:
        return Fraction(0), Fraction(0)
    llo, lhi = log2_interval_fraction(1/p)
    return p*llo, p*lhi

def sum_intervals(items):
    lo=Fraction(0); hi=Fraction(0)
    for a,b in items:
        lo += a; hi += b
    return lo, hi

def mul_nonneg_interval(c, I):
    assert c >= 0
    return c*I[0], c*I[1]

def sub_interval(A,B):
    return A[0]-B[1], A[1]-B[0]

def div_pos_interval(A, c):
    assert c > 0
    return A[0]/c, A[1]/c

def dec(q):
    return Decimal(q.numerator)/Decimal(q.denominator)

coeff_by_weight = [Fraction(11,16), Fraction(-3,16), Fraction(-1,16),
                   Fraction(1,16), Fraction(3,16)]
rho_by_weight = [c*c for c in coeff_by_weight]
mult = [1,4,6,4,1]
mu = sum(Fraction(mult[k])*rho_by_weight[k] for k in range(5))
assert mu == Fraction(11,16)

rho = []
for s in range(16):
    k = s.bit_count()
    rho.append(rho_by_weight[k])
assert sum(rho) == mu

d0 = sum(rho[s] for s in range(16) if s & 1)
assert d0 == Fraction(3,32)

L = sum_intervals([entropy_term_interval(x) for x in rho if x])
A0 = sum(x*x for x in rho)
assert A0 == Fraction(941,4096)
A1 = sum_intervals([mul_nonneg_interval(x*x, log2_interval_fraction(1/x)) for x in rho if x])

pairs = [(s, s^1) for s in range(16) if (s & 1)==0]
B = sum(rho[u]*rho[v] for u,v in pairs)
assert B == Fraction(141,8192)
B1 = sum_intervals([
    mul_nonneg_interval(rho[u]*rho[v], log2_interval_fraction(1/(rho[u]*rho[v])))
    for u,v in pairs if rho[u] and rho[v]
])

def edge_W_interval(a,b):
    mn=min(a,b)
    if mn==0:
        return Fraction(0), Fraction(0)
    ratio=(a+b)/(2*mn)
    lg=log2_interval_fraction(ratio)
    return mul_nonneg_interval(Fraction(1,2)*mn, lg)
Wloc=sum_intervals([edge_W_interval(rho[u],rho[v]) for u,v in pairs])

m=12
raw0 = 4*mu**(2*m)
p0 = (1-2*mu**m)**2
pe = 4*rho[1]*mu**(2*m-2)
assert pe == Fraction(9,64)*mu**(2*m-2)
assert p0 > pe and raw0 > pe

inf_i = 4*mu**(m-1)*d0
assert inf_i == Fraction(3,8)*mu**(m-1)
assert inf_i < Fraction(1,2)
J = 4*m*inf_i
assert J == Fraction(3*m,2)*mu**(m-1)

Hraw = (
    Fraction(-8)*mu**m + 4*m*mu**(m-1)*L[0],
    Fraction(-8)*mu**m + 4*m*mu**(m-1)*L[1],
)
raw0_ent = entropy_term_interval(raw0)
p0_ent = entropy_term_interval(p0)
H = (Hraw[0]-raw0_ent[1]+p0_ent[0],
     Hraw[1]-raw0_ent[0]+p0_ent[1])

Wcoord_raw = mul_nonneg_interval(4*mu**(m-1), Wloc)
corrW = sub_interval(edge_W_interval(p0,pe), edge_W_interval(raw0,pe))
Wcoord=(Wcoord_raw[0]+corrW[0], Wcoord_raw[1]+corrW[1])
W=(4*m*Wcoord[0],4*m*Wcoord[1])

C1raw=(
    Fraction(-32)*A0**m + 16*m*A0**(m-1)*A1[0],
    Fraction(-32)*A0**m + 16*m*A0**(m-1)*A1[1],
)
raw0_sq_ent=mul_nonneg_interval(raw0, entropy_term_interval(raw0))
p0_sq_ent=mul_nonneg_interval(p0, entropy_term_interval(p0))
C1=(C1raw[0]-raw0_sq_ent[1]+p0_sq_ent[0],
    C1raw[1]-raw0_sq_ent[0]+p0_sq_ent[1])

Qcoord_raw=(
    16*A0**(m-1)*(Fraction(-4)*B + B1[0]) +
      32*(m-1)*B*A0**(m-2)*A1[0],
    16*A0**(m-1)*(Fraction(-4)*B + B1[1]) +
      32*(m-1)*B*A0**(m-2)*A1[1],
)
def pair_log_interval(a,b):
    if a==0 or b==0:
        return Fraction(0),Fraction(0)
    return mul_nonneg_interval(a*b, log2_interval_fraction(1/(a*b)))
corrQ=sub_interval(pair_log_interval(p0,pe), pair_log_interval(raw0,pe))
Qcoord=(Qcoord_raw[0]+corrQ[0],Qcoord_raw[1]+corrQ[1])
Q=(4*m*Qcoord[0],4*m*Qcoord[1])

R1=(C1[0]+Q[0],C1[1]+Q[1])
T2=sub_interval(H,R1)

Hratio=div_pos_interval(H,J)
Wratio=div_pos_interval(W,J)
T2ratio=div_pos_interval(T2,J)

assert Wratio[0] > Fraction(3,4)
assert T2ratio[0] > 4

print("CHECK=PASS")
print("family=F_m=1-2*prod_{b=1}^m 1{|x^(b)|>=2}, m=12, n=48")
print("local_fourier_by_weight=11/16,-3/16,-1/16,1/16,3/16")
print("mu=", mu)
print("J_exact=", J)
print("H_interval=[", dec(H[0]), ",", dec(H[1]), "]")
print("H_over_J_interval=[", dec(Hratio[0]), ",", dec(Hratio[1]), "]")
print("W_over_J_interval=[", dec(Wratio[0]), ",", dec(Wratio[1]), "]")
print("T2_over_J_interval=[", dec(T2ratio[0]), ",", dec(T2ratio[1]), "]")
print("W_over_J_minus_3/4_lower=", dec(Wratio[0]-Fraction(3,4)))
print("T2_over_J_minus_4_lower=", dec(T2ratio[0]-4))
