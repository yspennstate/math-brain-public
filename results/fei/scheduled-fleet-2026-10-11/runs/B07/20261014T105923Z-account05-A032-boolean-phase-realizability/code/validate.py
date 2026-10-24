import json, time, hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'out'
OUT.mkdir(exist_ok=True)
t0 = time.perf_counter()

def walsh(v):
    return [sum(h * (-1 if (x&s).bit_count()%2 else 1) for x,h in enumerate(v)) for s in range(len(v))]

def product_parameters(v):
    W=walsh(v); d=(len(v)-1).bit_length(); sq=[x*x for x in W]; T=sum(sq)
    marg=[sum(q for s,q in enumerate(sq) if s>>i&1) for i in range(d)]
    assert all(q*T**(d-1)==__import__('math').prod(marg[i] if s>>i&1 else T-marg[i] for i in range(d)) for s,q in enumerate(sq))
    N=sum(0<a<T and 2*a!=T for a in marg)
    m=sum(2*a==T for a in marg)
    k=sum(x*x for x in v)
    fixed=sum(a==T for a in marg)
    active=N+m
    reduced_k=F(k,2**(d-active)); assert reduced_k.denominator==1
    odd=reduced_k.numerator
    while odd%2==0: odd//=2
    assert odd>=5**N
    assert 5**N<=2**active
    assert N==0 or 10*m>13*N
    return W,N,m,k, marg,T,fixed

checks={
    '5^10>2^23':5**10>2**23,
    '2^12*19^5>100^5':2**12*19**5>100**5,
    '119^50<2^13*100^50':119**50<2**13*100**50,
    '2^28>48^5':2**28>48**5,
    '49^25<2*48^25':49**25<2*48**25,
    '5^4>2*4^4':5**4>2*4**4,
}
assert all(checks.values())
source=ROOT.parent/'20261011T234647Z-account05-A032-boolean-phase-realizability/out/mixed_slices_m4.json'
catalogue=json.loads(source.read_text())['records']
assert len(catalogue)==45088
counts=Counter(); heightone=0
for row in catalogue:
    v=row['truth_h']
    if max(map(abs,v))>1: continue
    W,N,m,k,_,_,_=product_parameters(v)
    assert k==row['norm_integer']
    heightone+=1; counts[(N,m)]+=1

fixtures=[('nonflat_A079', [1,-1,1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],2),
          ('two_bit_point_defect',[-1,1,1,1],0)]
results=[]
for name,v,z in fixtures:
    d=(len(v)-1).bit_length(); P=len(v); W=walsh(v)
    edges=[sum(v[x]!=v[x^(1<<i)] for x in range(P)) for i in range(d)]
    I=F(sum(edges),P); IY=F(sum(edges[i] for i in range(d) if i!=z),P)
    assert I==sum((F(w*w*s.bit_count(),P*P) for s,w in enumerate(W)),F(0))
    branches=[]
    for b in (0,1):
        u=[]
        for y in range(P//2):
            x=(y&((1<<z)-1))|((y>>z)<<(z+1))
            u.append((v[x]+(-1)**b*v[x|(1<<z)])//2)
        U,N,m,k,marg,T,fixed=product_parameters(u)
        w=F(k,P//2); a=sum((F(x,T) for x in marg),F(0))
        assert N==0 # certificate fixtures happen to have only fair branches
        # H=m and R=m exactly for these fixtures; generic proof is analytic.
        assert F(m)<=F(12,5)*a
        assert F(2*m)<=F(28,5)*a
        branches.append(dict(truth=u,Walsh=U,N=N,m=m,mass=str(w),a=str(a),entropy_bits=m))
    assert all(branches[0]['truth'][i]*branches[1]['truth'][i]==0 for i in range(P//2))
    assert all(branches[0]['truth'][i]**2+branches[1]['truth'][i]**2==1 for i in range(P//2))
    assert sum(F(b['mass']) for b in branches)==1
    assert IY==sum((F(b['mass'])*F(b['a']) for b in branches),F(0))
    H=1+sum((F(b['mass'])*b['m'] for b in branches),F(0))
    Hcond=H-1
    assert H<=F(28,5)*IY and Hcond<=F(12,5)*IY
    results.append(dict(name=name,truth=v,frequency_bit=z,Walsh=W,influence=str(I),data_influence=str(IY),entropy_bits=str(H),conditional_entropy_bits=str(Hcond),branches=branches))
(OUT/'truth_tables.json').write_text(json.dumps(results,indent=2)+'\n')
summary=dict(status='PASS',arithmetic='integers and Fraction only',constant_checks=checks,
             catalogue_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),records_inspected=len(catalogue),
             actual_ternary_rows=heightone,heightone_counts={f'N={n},m={m}':v for (n,m),v in sorted(counts.items())},
             fixture_count=len(results),seconds=time.perf_counter()-t0,
             scope='Stored finite catalogue revalidated for new height-one inequalities; completeness not newly established; no actual nonfair height-one example asserted')
(OUT/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
