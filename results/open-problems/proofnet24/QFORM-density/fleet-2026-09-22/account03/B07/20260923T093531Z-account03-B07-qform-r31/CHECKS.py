from fractions import Fraction
import math, random

# Algebraic regression checks only; the proofs are in REPORT.md.
def split_product(r,c,mask):
    U=sum(r[j]*r[j] for j in range(len(r)) if (mask>>j)&1)
    V=sum(c[j]*c[j] for j in range(len(c)) if not((mask>>j)&1))
    return U*V

def wedge2(r,c):
    R2=sum(x*x for x in r); C2=sum(x*x for x in c)
    dot=sum(x*y for x,y in zip(r,c))
    return R2*C2-dot*dot

def cut_wedge(r,c,mask):
    ans=0
    m=len(r)
    for j in range(m):
        for k in range(j+1,m):
            if ((mask>>j)&1) != ((mask>>k)&1):
                ans += (r[j]*c[k]-r[k]*c[j])**2
    return ans

rng=random.Random(3107)
cases=0
for m in range(2,9):
    for _ in range(30):
        r=[rng.randint(-3,3) for _ in range(m)]
        c=[rng.randint(-3,3) for _ in range(m)]
        if not any(r) or not any(c):
            continue
        R2=sum(x*x for x in r); C2=sum(x*x for x in c)
        diag=sum((r[j]*c[j])**2 for j in range(m))
        average=Fraction(R2*C2-diag,4)
        best=max(split_product(r,c,mask) for mask in range(1<<m))
        assert Fraction(best,1) >= average
        W2=wedge2(r,c)
        bestcut=max(cut_wedge(r,c,mask) for mask in range(1<<m))
        assert 2*bestcut >= W2
        cases += 1

m=80
u=[1/math.sqrt(m)]*m
z=[(1 if j%2==0 else -1)/math.sqrt(m) for j in range(m)]
eps=0.05
raw=[u[j]+eps*z[j] for j in range(m)]
norm=math.sqrt(sum(x*x for x in raw))
v=[x/norm for x in raw]
dot=sum(u[j]*v[j] for j in range(m))
W=math.sqrt(max(0.0,1-dot*dot))
dist=math.sqrt(sum((u[j]-v[j])**2 for j in range(m)))
assert W < 1/9
assert dist < 1/8
assert max(abs(x) for x in u) <= 1/8

remaining=set(range(m)); banks=[]
for _ in range(4):
    B=[]; mass=0.0
    for j in sorted(list(remaining)):
        B.append(j); remaining.remove(j); mass += u[j]*u[j]
        if mass >= 1/16:
            break
    banks.append(B)
for B in banks:
    un=math.sqrt(sum(u[j]*u[j] for j in B))
    vn=math.sqrt(sum(v[j]*v[j] for j in B))
    assert un >= 1/4
    assert vn > 1/8

h=(2*math.sqrt(2)-1)/1572864
alpha=math.sqrt(63)/16
print(f'exact_small_vector_cases={cases}')
print(f'disjoint_innovation_factor_sq={63/256:.15f}')
print(f'disjoint_innovation_factor={alpha:.15f}')
print(f'partner_h={h:.18e}')
print(f'partner_bank_norm_lower={alpha*h:.18e}')
print(f'partner_transverse_minor_mass_lower={h**4/162:.18e}')
print(f'aligned_test_wedge_ratio={W:.15f}')
print(f'aligned_test_distance={dist:.15f}')
print('STATUS=PASS')
