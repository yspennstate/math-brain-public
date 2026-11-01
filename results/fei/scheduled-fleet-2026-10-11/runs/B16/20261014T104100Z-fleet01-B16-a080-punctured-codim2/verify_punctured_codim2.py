#!/usr/bin/env python3
"""Exact/numerical certificate for the punctured codimension-two family.

The finite truth-table checks use integer Walsh transforms.  Logarithmic
quantities are evaluated at 100 decimal digits only after exact squared
masses and upper-set masses are constructed.
"""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext

getcontext().prec = 100
LN2 = D(2).ln()


def values(n):
    # Coordinate sign is +1 when its bit is zero.  The negative set is the
    # codimension-two subcube x1=x2=+1 with the all-plus point punctured.
    return [(-1 if (x & 3) == 0 and x != 0 else 1) for x in range(1 << n)]


def walsh_int(v):
    a = list(v)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def masses(v):
    N = len(v)
    return [F(z*z, N*N) for z in walsh_int(v)]


def mlog2(x):
    return (D(x.numerator)/D(x.denominator)).ln()/LN2


def HU_from_masses(p):
    N = len(p)
    n = N.bit_length()-1
    H = D(0)
    U = D(0)
    for s,ps in enumerate(p):
        if not ps:
            continue
        H -= (D(ps.numerator)/D(ps.denominator))*mlog2(ps)
        pi = sum((p[t] for t in range(N) if (t & s) == s), F(0))
        U += (D(ps.numerator)/D(ps.denominator))*mlog2(pi/ps)
    I = sum((s.bit_count()*p[s] for s in range(N)), F(0))
    return H,U,I


def restrict(v,n,i,bit):
    out=[]
    for x in range(1 << (n-1)):
        lo=x & ((1 << i)-1)
        hi=x >> i
        old=lo | (bit << i) | (hi << (i+1))
        out.append(v[old])
    return out


def direct_G(v,n):
    _,U,_ = HU_from_masses(masses(v))
    child = D(0)
    for i in range(n):
        for bit in (0,1):
            child += HU_from_masses(masses(restrict(v,n,i,bit)))[1]/2
    return n*U-child


def L(x):
    return D(0) if x == 0 else x*(D(1)/x).ln()/LN2


def formulas(n):
    e = D(2)**(1-n)
    r = e*e
    qp = (D('0.5')+e)**2
    qm = (D('0.5')-e)**2
    H = L(qp)+3*L(qm)+(D(2)**n-4)*L(r)
    U = (L(qp)+L(qm)+qm*(D(1)/(1-2*e)).ln()/LN2
         + n*e-(4*n-4)*r)
    I = 1+(n-4)*e
    M1 = D('0.5')-2*e+n*r
    W2 = D('0.25')-e+D(n*(n-1))/2*r
    Q = I-M1-W2

    N=n-1
    ee=2*e
    V = L(ee*ee)+D('0.5')*L((1-ee)**2)+N*ee-(2*N-1)*ee*ee
    if n == 3:
        # The n-1 family still has the same formula; no singular terms occur.
        pass
    ep=2*e
    if N == 2:
        # Puncturing the only point in the codimension-two subcube leaves
        # the constant function.
        Up=D(0)
    else:
        qpp=(D('0.5')+ep)**2
        qmp=(D('0.5')-ep)**2
        Up=(L(qpp)+L(qmp)+qmp*(D(1)/(1-2*ep)).ln()/LN2
            + N*ep-(4*N-4)*ep*ep)
    G=n*U-V-(n-2)*(1+Up)/2
    return H,U,I,G,Q


def coefficient(n,s):
    e=F(1,1 << (n-1))
    if s == 0:
        return F(1,2)+e
    if s & ~3 == 0:
        return -F(1,2)+e
    return e


def certify_tensor_prime(n):
    full=(1 << n)-1
    Y=full & ~3
    for A in range(1,full):
        B=full ^ A
        # Select one variable from each side giving a nonzero Fourier 2x2 minor.
        YA=A & Y
        YB=B & Y
        if YA and YB:
            i=(YA & -YA)
            j=(YB & -YB)
        elif YA:
            i=(YA & -YA)
            j=(B & -B)
        else:
            i=(A & -A)
            j=(YB & -YB)
        det=coefficient(n,0)*coefficient(n,i|j)-coefficient(n,i)*coefficient(n,j)
        assert det != 0, (n,A,i,j)


def fmt(x):
    return format(x,'.18E')


def main():
    assertions=0
    max_H=max_U=max_I=max_G=D(0)
    for n in range(3,10):
        v=values(n)
        p=masses(v)
        e=F(1,1 << (n-1))
        for s,z in enumerate(walsh_int(v)):
            got=F(z,1 << n)
            want=(F(1,2)+e if s==0 else (-F(1,2)+e if (s & ~3)==0 else e))
            assert got == want
            assertions += 1
        H,U,I=HU_from_masses(p)
        G=direct_G(v,n)
        Hf,Uf,If,Gf,Qf=formulas(n)
        max_H=max(max_H,abs(H-Hf)); max_U=max(max_U,abs(U-Uf))
        max_I=max(max_I,abs(D(I.numerator)/D(I.denominator)-If))
        max_G=max(max_G,abs(G-Gf))
        assert max_H < D('1e-85') and max_U < D('1e-85')
        assert max_I < D('1e-85') and max_G < D('1e-85')
        certify_tensor_prime(n)
        assertions += (1 << n)-2

    c=D(1)/LN2
    rows=[]
    for n in (3,4,6,8,12,20,40,80):
        H,U,I,G,Q=formulas(n)
        R=G-4*I-D('0.75')*U
        rows.append((n,H/I,U/I,G/I,Q/I,R))

    # The remainders after the displayed first-order asymptotics vanish at
    # the asserted scales.  This is a diagnostic; the proof is analytic.
    asym=[]
    for n in (12,20,40,80):
        e=D(2)**(1-n)
        H,U,I,G,Q=formulas(n)
        asym.append((n,
            (H-(2+(4*n-8+2*c)*e))/(n*e*e),
            (U-(1+(n+c/2)*e))/(n*e*e),
            (G-(2+(n-c)*e))/(n*n*e*e)))

    print('claim=B16-A080-PUNCTURED-CODIM2-v1')
    print('family=codimension-two negative subcube with all-plus point punctured')
    print('direct_truth_table_dimensions=3..9')
    print('walsh_arithmetic=exact integers and Fractions')
    print('log_precision_decimal_digits=100')
    print('max_H_formula_error='+format(max_H,'.5E'))
    print('max_U_formula_error='+format(max_U,'.5E'))
    print('max_I_formula_error='+format(max_I,'.5E'))
    print('max_G_formula_error='+format(max_G,'.5E'))
    print('tensor_partition_checks=all nontrivial partitions for n=3..9')
    print('assertions='+str(assertions))
    print('n H/I U/I G/I Q/I G-4I-3U/4')
    for row in rows:
        print(row[0],*(fmt(x) for x in row[1:]))
    print('scaled_asymptotic_remainders n H U G')
    for row in asym:
        print(row[0],*(fmt(x) for x in row[1:]))
    print('limits=H/I->2,U/I->1,G/I->2,Q/I->1/4,residual->-11/4')
    print('seed=None')
    print('status=PASS')


if __name__ == '__main__':
    main()
