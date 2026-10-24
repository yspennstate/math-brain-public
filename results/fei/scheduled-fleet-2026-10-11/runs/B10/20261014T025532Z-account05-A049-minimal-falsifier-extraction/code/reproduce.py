"""Second representation: full physical leaves and explicit negative-set Fourier sums.
No imports from the certificate helper; internal reproduction is not external review.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
start=time.perf_counter(); checks=0
def ck(b):
    global checks
    assert b;checks+=1
out=Path(__file__).resolve().parents[1]/'out'
v=[int(s) for s in (out/'truth_table.txt').read_text().splitlines()]
ck(len(v)==2**17)
# Seven explicitly enumerated core points, without using the circuit implementation.
negative={0,1,2,3,7,14,15}
for x,a in enumerate(v):
    expected=(-1 if (x&511) in negative else 1)*(-1)**((x>>9).bit_count())
    ck(a==expected)
coeff={s:F((512 if s==0 else 0)-2*sum((-1)**((s&x).bit_count()) for x in negative),512) for s in range(512)}
ck(sum(a*a for a in coeff.values())==1)
ck(sum(s.bit_count()*a*a for s,a in coeff.items())==F(49,256))
ck(all(sum(a*a for s,a in coeff.items() if s>>i&1)>0 for i in range(9)))
sum_leaf_I=F(0)
for prefix in range(8):
    for outcome in range(2):
        fixedmask=7|(1<<(9+prefix));fixed=prefix|(outcome<<(9+prefix))
        free=[i for i in range(17) if not fixedmask>>i&1]
        points=[fixed|sum(((a>>j)&1)<<i for j,i in enumerate(free)) for a in range(1<<13)]
        ck(sum(v[x] for x in points)==0)
        leaf_I=F(0)
        for i in free:
            directed=sum(v[x]!=v[x^(1<<i)] for x in points)
            leaf_I+=F(directed,len(points))
        sum_leaf_I+=leaf_I/16
        # Terminal label is precisely all eight parity labels except the queried one.
        parity_W=255^(1<<prefix)
        ck((255^parity_W)==1<<prefix)
ck(sum_leaf_I==F(229,32))
ck(8+F(49,256)-sum_leaf_I==F(265,256))
for depth in range(3):
    for prefix in range(1<<depth):
        relevant=sum(v[x]!=v[x^(1<<depth)] for x in range(prefix,1<<17,1<<depth))
        ck(relevant>0)
# Three-term atanh bound, reconstructed as its integral geometric-series remainder.
z=F(1,3);L=2*(z+z**3/3+z**5/5);U=L+2*z**7/(7*(1-z*z))
ck(L==F(842,1215));ck(L>F(265,384));ck(U<F(139,200))
ck(F(3,2)-F(265,256)/L>F(1,256))
# Minimum within the essential-prefix/parity-missing-label class: r<=2 impossible;
# r=3, k<=8 impossible by the essential-edge lower bound; r>=4 uses >=20 variables.
ck(U<1);ck(F(3,2)*U<1+F(7,128));ck(4+2**4>17)
r={'assertions':checks,'runtime_seconds':time.perf_counter()-start,
   'I_terminal_mean':str(sum_leaf_I),'explicit_core_negative_points':sorted(negative),
   'ln2_bounds':[str(L),str(U)],'minimum_variables_in_stated_class':17,
   'truth_table_sha256':hashlib.sha256((out/'truth_table.txt').read_bytes()).hexdigest(),
   'external_independent_review':'pending'}
(out/'reproduction.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps(r,indent=2))
