#!/usr/bin/env python3
from math import factorial
from fractions import Fraction

NMAX=32

def parts(n, maxp=None, pref=()):
    if n==0:
        yield pref; return
    if maxp is None or maxp>n: maxp=n
    for a in range(maxp,0,-1):
        yield from parts(n-a,a,pref+(a,))

def hookdim(lam):
    n=sum(lam); f=factorial(n); w=lam[0]; r=len(lam)
    col=[sum(1 for x in lam if x>c) for c in range(w)]
    hp=1
    for i,a in enumerate(lam):
        for c in range(a):
            hp *= (a-c)+(col[c]-i-1)
    assert f%hp==0
    return f//hp

def ellrow(n):
    e=[0]*(n+1); pc=0
    for lam in parts(n):
        d=hookdim(lam); e[lam[0]] += d*d; pc+=1
    assert sum(e)==factorial(n)
    return e,pc

rows={}; partcounts={}
for n in range(1,NMAX+2):
    rows[n],partcounts[n]=ellrow(n)

def alpha_row(n):
    e,e1=rows[n],rows[n+1]
    U=[0]*(n+1); U1=[0]*(n+2)
    for k in range(1,n+1): U[k]=U[k-1]+e[k]
    for k in range(1,n+2): U1[k]=U1[k-1]+e1[k]
    a={}
    for k in range(1,n+1):
        H=U1[k]-(n+1)*U[k-1]
        assert e[k] <= H <= n*e[k]
        a[k]=Fraction(H,(n+1)*e[k])
        Hprev=(U1[k-1]-(n+1)*U[k-2]) if k>=2 else 0
        assert e1[k]==H+(n+1)*e[k-1]-Hprev
    return a

monotone_checks=0; A_checks=0; universal_checks=0
universal_failures=[]; C_negative=0; B_negative=0; first_fail=None
for n in range(3,NMAX+1):
    e=rows[n]; a=alpha_row(n)
    for k in range(1,n):
        assert a[k] <= a[k+1]
        monotone_checks += 1
    for k in range(3,n):
        A=a[k]*a[k]-a[k-1]*a[k+1]
        B=2*a[k]*(1-a[k-1])-a[k-1]*(1-a[k])-a[k+1]*(1-a[k-2])
        C=(1-a[k-1])*(1-a[k-1])-(1-a[k-2])*(1-a[k])
        if A>=0: A_checks += 1
        if C<0: C_negative += 1
        if B<0: B_negative += 1
        ok=True
        if A<0 or C<0:
            ok=False
        elif A==0:
            if B<0: ok=False
        elif B<0 and B*B>4*A*C:
            ok=False
        universal_checks += 1
        if not ok:
            rec=(n,k,A,B,C); universal_failures.append(rec)
            if first_fail is None: first_fail=rec

assert first_fail is not None and first_fail[0:2]==(4,3)
n,k=4,3; a=alpha_row(n); e=rows[n]; e1=rows[n+1]
r=Fraction(e[k],e[k-1])
A=a[k]*a[k]-a[k-1]*a[k+1]
B=2*a[k]*(1-a[k-1])-a[k-1]*(1-a[k])-a[k+1]*(1-a[k-2])
C=(1-a[k-1])*(1-a[k-1])-(1-a[k-2])*(1-a[k])
P=A*r*r+B*r+C
assert P==Fraction(-16321,164775)
x=Fraction(e[k-1],factorial(n))
base=x*x*P
actual=Fraction(e1[k],factorial(n+1))**2-Fraction(e1[k-1],factorial(n+1))*Fraction(e1[k+1],factorial(n+1))
assert base==Fraction(-16321,561600)
assert actual==Fraction(613,2880)
assert actual>0 and actual-base==Fraction(8491,35100)
a0,a1,a2,a3=Fraction(0),Fraction(1,2),Fraction(2,3),Fraction(3,4)
AA=a2*a2-a1*a3
BB=2*a2*(1-a1)-a1*(1-a2)-a3*(1-a0)
CC=(1-a1)*(1-a1)-(1-a0)*(1-a2)
assert (AA,BB,CC)==(Fraction(5,72),Fraction(-1,4),Fraction(-1,12))
print('P0282 insertion-flux universal-preserver exact checker')
print(f'NMAX={NMAX} rows_rebuilt=1..{NMAX+1} total_partition_shapes={sum(partcounts.values())}')
print(f'alpha_adjacent_monotonicity_checks={monotone_checks} all_pass=True')
print(f'alpha_logconcavity_A_nonnegative_checks={A_checks}/{universal_checks}')
print(f'universal_preserver_local_checks={universal_checks} failures={len(universal_failures)} C_negative={C_negative} B_negative={B_negative}')
print('first_universal_preserver_failure=n4_k3')
print(f'alpha_n4={[str(a[i]) for i in range(1,5)]}')
print(f'row4_counts={e[1:]} ratio_r=p3/p2={r}')
print(f'P_4_3_at_actual_ratio={P}')
print(f'geometric_extremal_normalized_margin={base}')
print(f'actual_row5_normalized_margin_k3={actual}')
print(f'curvature_rescue_amount={actual-base}')
print(f'monotone_kernel_counterexample_coeffs=A:{AA},B:{BB},C:{CC}')
print('ALL_EXACT_CHECKS_PASS')
