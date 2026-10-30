import json,time
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
t0=time.perf_counter()
def walsh(v):
    return [sum(h*(-1 if (s&x).bit_count()%2 else 1) for x,h in enumerate(v)) for s in range(len(v))]
def product(v):
    W=walsh(v); d=(len(v)-1).bit_length(); sq=[a*a for a in W]; T=sum(sq)
    marg=[sum(q for s,q in enumerate(sq) if s>>i&1) for i in range(d)]
    checks=[q*T**(d-1)==__import__('math').prod(marg[i] if s>>i&1 else T-marg[i] for i in range(d)) for s,q in enumerate(sq)]
    return all(checks),W,sum(0<a<T and 2*a!=T for a in marg),marg,T
rows=json.loads((ROOT.parent/'20261011T234647Z-fleet05-A032-boolean-phase-realizability/out/mixed_slices_m4.json').read_text())['records']
examined=0
for row in rows:
    examined+=1; h=row['truth_h']
    if max(map(abs,h))>1: continue
    yes,W,N,marg,T=product(h)
    assert yes
    if N: break
else: raise AssertionError('No nonfair row')
j=[int(x==0) for x in h]
yes2,V,N2,marg2,T2=product(j)
assert not yes2
w0=F(sum(x*x for x in h),len(h)); w1=F(sum(x*x for x in j),len(h))
assert w0==F(5,8) and w1==F(3,8)
g=[h[y]+j[y] for y in range(16)]+[h[y]-j[y] for y in range(16)]
assert set(g)<= {-1,1}
G=walsh(g)
assert G[:16]==[2*a for a in W] and G[16:]==[2*a for a in V]
edges=[sum(g[x]!=g[x^(1<<i)] for x in range(32)) for i in range(5)]
I=F(sum(edges),32)
assert I==sum((F(a*a*s.bit_count(),1024) for s,a in enumerate(G)),F(0))
certificate=dict(truth=g,Walsh=G,z_bit=4,influence=str(I),product_branch=dict(truth=h,Walsh=W,mass=str(w0),N=N),
    nonproduct_branch=dict(truth=j,Walsh=V,mass=str(w1)),
    impossibility='A ternary product branch of mass3/8 is impossible in every dimension: its reduced numerator3 is not1 modulo4; every signing of that requested product-mass law is rejected')
(ROOT/'out/ternary_obstruction.json').write_text(json.dumps(certificate,indent=2)+'\n')
values={F(r,2**a) for a in range(1,13) for r in range(1,2**a,2) if r%4==1}
assert len(values)==2048
pairs=[str(w) for w in values if 1-w in values]
assert pairs==['1/2']
result=dict(status='PASS',dyadic_domain='a=1..12',masses_checked=len(values),complement_admissions=pairs,
            catalogue_records_examined=examined,actual_truth_count=len(g),seconds=time.perf_counter()-t0,
            scope='Finite congruence audit supports the independent all-dimensional modular proof; no entropy evaluated approximately')
(ROOT/'out/mass_congruence.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
