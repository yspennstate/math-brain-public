"""Exact rational certificates for worker 027's four-site sector obstruction.

Only the displayed logarithmic decimal values are approximate. Matrix algebra,
all output atoms, and the strict signs use integers/Fractions. Standard library.
"""
from collections import Counter
from decimal import Decimal, localcontext
from fractions import Fraction as F
from itertools import combinations, permutations
import json

# Gaussian integers, represented by (real, imaginary).
Z=(0,0)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a): return (a[0],-a[1])
def norm(a): return a[0]**2+a[1]**2
def determinant(A):
    n=len(A)
    ans=Z
    for p in permutations(range(n)):
        inversions=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=(-1 if inversions%2 else 1,0)
        for i in range(n):term=mul(term,A[i][p[i]])
        ans=add(ans,term)
    return ans

C=[[(0,0),(1,0),(1,0),(1,0)],
   [(1,0),(0,0),(0,-1),(0,1)],
   [(1,0),(0,1),(0,0),(0,-1)],
   [(1,0),(0,-1),(0,1),(0,0)]]

for i in range(4):
    for j in range(4):
        assert C[i][j]==conj(C[j][i])
        value=Z
        for k in range(4):value=add(value,mul(C[i][k],C[k][j]))
        assert value==((3,0) if i==j else Z)
        if i!=j:assert norm(C[i][j])==1

# Thus P=(I+C/sqrt(3))/2 and Q=I-P are rank-two projections.
# P_ii=1/2 and |P_ij|^2=1/12, so every rank-two atom is 1/6.
assert F(1,4)-F(1,12)==F(1,6)

atoms={}
sector={}
sites=set(range(4))
for size_s in range(5):
    for S in combinations(range(4),size_s):
        Sc=sorted(sites-set(S))
        for T in combinations(range(4),4-size_s):
            minor=[[C[i][j] for j in Sc] for i in T]
            p=F(norm(determinant(minor)),16*3**len(T))
            atoms[(S,T)]=p
            if set(T)==sites-set(S):sector[(S,T)]=p

assert sum(atoms.values())==1
expected={F(0):8,F(1,16):2,F(1,48):24,F(1,144):30,F(1,36):6}
assert Counter(atoms.values())==Counter(expected)
assert sum(sector.values())==F(1,6)
conditional=Counter(p/F(1,6) for p in sector.values())
assert conditional==Counter({F(0):8,F(3,8):2,F(1,24):6})

# Global gap = (5/3) log 2 - (3/4) log 3 > 0.
assert 2**20>3**9
# Conditional gap = log(4/(3 sqrt(3))) < 0.
assert 4**2<3**3

with localcontext() as ctx:
    ctx.prec=60
    log2,log3=Decimal(2).ln(),Decimal(3).ln()
    global_gap=Decimal(5)/3*log2-Decimal(3)/4*log3
    conditional_gap=2*log2-Decimal(3)/2*log3
    print(json.dumps({
        'matrix_identity':'C = C*, C^2 = 3 I',
        'input_atom_distribution':{'1/6':6},
        'output_atom_distribution':{str(k):v for k,v in sorted(expected.items())},
        'global_gap_exact':'(5/3) log 2 - (3/4) log 3',
        'global_gap_decimal':str(global_gap),
        'global_gap_integer_sign_certificate':{'2^20':2**20,'3^9':3**9},
        'all_sites_single_probability':'1/6',
        'conditional_input_atom_distribution':{'1/6':6},
        'conditional_output_atom_distribution':{str(k):v for k,v in sorted(conditional.items())},
        'conditional_gap_exact':'2 log 2 - (3/2) log 3',
        'conditional_gap_decimal':str(conditional_gap),
        'conditional_gap_integer_sign_certificate':{'4^2':4**2,'3^3':3**3},
    },indent=2))
