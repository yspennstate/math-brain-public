#!/usr/bin/env python3
from functools import lru_cache
from fractions import Fraction
from itertools import combinations
import hashlib

# Q_m is a two-flank perturbation of the account03/B19 P_m corridor.
# Core labels: e=0,d=1,x=2,y=3,u=4.
# Residual chain: r_j=4+j (1<=j<=m).
# Low flank ell=5+m; high flank h=6+m.
def closure(n, edges):
    R=[[False]*n for _ in range(n)]
    for a,b in edges:
        R[a][b]=True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j]=True
    assert not any(R[i][i] for i in range(n))
    return R

def build(m):
    assert m>=1
    ell=5+m
    h=6+m
    n=7+m
    edges=[(0,2),(0,3),(1,3),(1,4),(2,4)]
    rs=list(range(5,5+m))
    edges += [(0,rs[0])] + list(zip(rs,rs[1:])) + [(rs[-1],4)]
    edges += [(ell,1),(ell,2)]
    edges += [(1,h),(2,h),(3,h)]
    return closure(n,edges),ell,h

def pred_masks(R):
    out=[]
    for j in range(len(R)):
        mask=0
        for i in range(len(R)):
            if R[i][j]:
                mask |= 1<<i
        out.append(mask)
    return out

def count_le(R):
    n=len(R); pred=pred_masks(R); full=(1<<n)-1
    @lru_cache(None)
    def f(mask):
        if mask==full:
            return 1
        total=0
        for v in range(n):
            if not (mask>>v)&1 and pred[v]&~mask==0:
                total += f(mask | (1<<v))
        return total
    return f(0)

def pair_count(R,a,b,E=None):
    if E is None:
        E=count_le(R)
    if R[a][b]:
        return E
    if R[b][a]:
        return 0
    edges=[(i,j) for i in range(len(R)) for j in range(len(R)) if R[i][j]]
    return count_le(closure(len(R),edges+[(a,b)]))

def covers(R,a,b):
    return R[a][b] and not any(k not in (a,b) and R[a][k] and R[k][b] for k in range(len(R)))

def relation(R,a,b):
    if R[a][b]: return -1
    if R[b][a]: return 1
    return 0

def distinguishers(R,v,w):
    return {z for z in range(len(R)) if z not in (v,w) and relation(R,z,v)!=relation(R,z,w)}

def formulas(m):
    E=(m+1)*(3*m**4+72*m**3+623*m**2+2182*m+2520)//120
    A=(m+1)*(m+2)*(m+5)*(m+8)*(m+9)//120
    B=(m+1)*(m+3)*(m+5)//3
    H=(m+1)*(m+3)*(m+4)*(m*m+17*m+90)//120
    return E,A,B,H

def labels(v,m):
    if v==0:return 'e'
    if v==1:return 'd'
    if v==2:return 'x'
    if v==3:return 'y'
    if v==4:return 'u'
    if 5<=v<5+m:return f'r{v-4:02d}'
    if v==5+m:return 'ell'
    if v==6+m:return 'h'
    raise ValueError(v)

def is_chain(R,M):
    return all(R[a][b] or R[b][a] for a,b in combinations(M,2))

def autonomous_sets(R):
    n=len(R); out=[]
    for mask in range(1,1<<n):
        k=mask.bit_count()
        if k<=1 or k==n: continue
        M=[i for i in range(n) if (mask>>i)&1]
        ok=True
        for z in range(n):
            if (mask>>z)&1: continue
            if len({relation(R,z,v) for v in M})!=1:
                ok=False; break
        if ok: out.append(tuple(M))
    return out

def structural_checks(m):
    R,ell,h=build(m)
    Pred=lambda v:{z for z in range(len(R)) if R[z][v]}
    Succ=lambda v:{z for z in range(len(R)) if R[v][z]}
    assert Pred(3)==Pred(2)|{1}
    assert Succ(2)==Succ(3)|{4}
    assert Pred(2)==Pred(1)|{0}
    assert Succ(1)==Succ(2)|{3}
    assert not R[1][2] and not R[2][1]
    assert not R[1][5] and not R[5][1]
    assert not R[2][5] and not R[5][2]
    assert covers(R,1,3)
    ext=(distinguishers(R,1,2)-{3}) | (distinguishers(R,3,2)-{1})
    assert ext=={0,4}
    return R,ell,h

def formula_check(m):
    R,ell,h=structural_checks(m)
    E=count_le(R); Ef,A,B,H=formulas(m)
    assert E==Ef
    assert pair_count(R,3,2,E)==A
    assert pair_count(R,2,1,E)==A
    assert pair_count(R,1,0,E)==B
    assert pair_count(R,4,3,E)==B
    assert pair_count(R,1,2,E)==E-A
    assert H==E-2*A
    assert 3*H>E and 3*A<E
    assert 3*H-E == 2*(E-3*A)
    assert Fraction(B,H)==Fraction(40*(m+5),(m+4)*(m*m+17*m+90))
    return R,E,A,B,H

# The counts are degree <=5 order polynomials because only five fixed
# outside vertices are inserted against one variable chain. Twelve exact
# values therefore overdetermine the displayed degree <=5 formulas.
for m in range(1,13):
    formula_check(m)
print('FORMULA_REGRESSION_m1_to_m12 PASS')

R12,E12,A12,B12,H12=formula_check(12)
autos=autonomous_sets(R12)
nonchain=[M for M in autos if not is_chain(R12,M)]
assert not nonchain
assert len(autos)==66
print('M12_AUTONOMY proper_nontrivial=66 nonchain=0 all_chain=True')

m=60
R,E,A,B,H=formula_check(m)
actual=[]; balanced=[]
for a,b in combinations(range(len(R)),2):
    if R[a][b] or R[b][a]: continue
    c=pair_count(R,a,b,E); p=Fraction(c,E)
    actual.append((a,b,c,p))
    if Fraction(1,3)<=p<=Fraction(2,3):
        balanced.append((a,b,p))
assert len(actual)==306
assert len(balanced)==52
pair_table='\n'.join(f'{labels(a,m)},{labels(b,m)},{c},{E},{p}' for a,b,c,p in actual)+'\n'
balanced_table='\n'.join(f'{labels(a,m)},{labels(b,m)},{p}' for a,b,p in balanced)+'\n'

print(f'TARGET_m {m}')
print(f'E {E}')
print(f'central_A {A} prob={Fraction(A,E)}')
print(f'heavy_H {H} prob={Fraction(H,E)}')
print(f'each_witness_B {B} prob={Fraction(B,E)}')
print(f'B_over_H {Fraction(B,H)} combined_count_over_H={Fraction(2*B,H)}')
print(f'heavy_surplus 3H-E={3*H-E}')
print(f'central_deficit E-3A={E-3*A}')
print(f'surplus_twice_deficit {3*H-E==2*(E-3*A)}')
print('heavy_edge d<y pivot=x external_distinguishers=e,u')
print(f'incomparable_pairs {len(actual)} balanced_pairs {len(balanced)}')
print('all_incomparable_pair_table_sha256',hashlib.sha256(pair_table.encode()).hexdigest())
print('balanced_pair_table_sha256',hashlib.sha256(balanced_table.encode()).hexdigest())
print('first_pair_rows',[f'{labels(a,m)},{labels(b,m)},{c},{E},{p}' for a,b,c,p in actual[:5]])
print('last_pair_rows',[f'{labels(a,m)},{labels(b,m)},{c},{E},{p}' for a,b,c,p in actual[-5:]])
print('ASYMPTOTIC witness/heavy = 40(m+5)/((m+4)(m^2+17m+90)) -> 0')
print('POS3_TWO_FLANK_VANISHING_WITNESS_PASS')
