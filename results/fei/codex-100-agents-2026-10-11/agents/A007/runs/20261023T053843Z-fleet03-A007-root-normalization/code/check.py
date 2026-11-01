from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import prod
import argparse, hashlib, json, time

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser(); ap.add_argument('--pilot',action='store_true'); args=ap.parse_args()
start=time.monotonic(); assertions=0
counts={'truth_tables':0,'signed_faces':0,'reference_vectors':0,'output_component_cases':0,
        'enumerated_root_sets':0,'heterogeneous_orbits':0,'physical_spectral_coefficients':0}
def ck(b):
    global assertions
    assert b
    assertions+=1
    assert time.monotonic()-start<55

def components(A,gates):
    parts=[{i} for i in A]
    for gate in gates:
        touched=[part for part in parts if part & gate]
        if touched:
            merged=set().union(*touched)
            parts=[part for part in parts if not part & merged]+[merged]
    return sorted(parts,key=lambda s:min(s))

def prior_audit(n,gates,activities,packing_check=True):
    N=len(gates); denominator=prod(1+x for x in activities)-1
    roots=[]
    for mask in range(1,1<<N):
        roots.append((mask,prod(activities[e] for e in range(N) if mask>>e&1)/denominator))
    ck(sum(q for _,q in roots)==1)
    counts['enumerated_root_sets']+=len(roots)
    counts['reference_vectors']+=1
    pi=max(F(1,2**len(g)) for g in gates)
    for amask in range(1,1<<n):
        A={i for i in range(n) if amask>>i&1}
        parts=components(A,gates)
        masks=[]; local=[]; sums=[]
        for part in parts:
            group=[e for e,g in enumerate(gates) if g & part]
            masks.append(sum(1<<e for e in group))
            local.append(prod(1+activities[e] for e in group)-1)
            sums.append(sum(activities[e] for e in group))
        allowed=0
        for mask in masks:allowed|=mask
        # Independent root-set enumeration versus component product factorization.
        exact=sum(q for m,q in roots if not m & ~allowed and all(m & c for c in masks))
        factored=prod(local)/denominator
        ck(exact==factored and 0<exact<=1)
        # Every permitted attachment through A stays in the same component.
        owner={e:c for c,mask in enumerate(masks) for e in range(N) if mask>>e&1}
        for e,g in enumerate(gates):
            for i in A & g:
                for h,gate in enumerate(gates):
                    if i in gate:ck(owner[e]==owner[h])
        if packing_check and all(len(g & A)<=1 for g in gates):
            ck(len(parts)==len(A))
            ck(all(0<s<=pi for s in sums))
            k=len(parts)
            bound=pi**(k-1)/(k*(1-pi)**k)
            ck(exact<=bound)
            ck(prod(sums)/sum(sums)<=pi**(k-1)/k)
        counts['output_component_cases']+=1

def prime_faces(truth,n):
    implicants=set()
    for signs in product([-1,0,1],repeat=n):
        if not any(signs):continue
        points=[z for z in range(1<<n) if all(not s or bool(z>>i&1)==(s==1) for i,s in enumerate(signs))]
        if all(truth[z] for z in points):implicants.add(signs)
        counts['signed_faces']+=1
    return {s for s in implicants if all(tuple(0 if i==j else a for i,a in enumerate(s)) not in implicants
                                        for j,a in enumerate(s) if a)}

small=[(2,2)] if args.pilot else [(2,2),(3,2),(2,3)]
for r,w in small:
    n=r*w; epsilon=F(1,2**w); p=1-epsilon; P=p**r
    gates=[set(j*w+a[j] for j in range(r)) for a in product(range(w),repeat=r)]
    truth=[all(any(z>>(j*w+i)&1 for i in range(w)) for j in range(r)) for z in range(1<<n)]
    vals=[2*int(b)-1 for b in truth]
    influences=[F(sum(truth[z]!=truth[z^(1<<i)] for z in range(1<<n)),1<<n) for i in range(n)]
    ck(sum(influences)==2*r*w*epsilon*p**(r-1))
    walsh=vals[:]
    h=1
    while h<len(walsh):
        for base in range(0,len(walsh),2*h):
            for i in range(base,base+h):
                a,b=walsh[i],walsh[i+h]; walsh[i],walsh[i+h]=a+b,a-b
        h*=2
    coeff=[F(x,1<<n) for x in walsh]
    ck(sum(x*x for x in coeff)==1)
    ck(sum(s.bit_count()*x*x for s,x in enumerate(coeff))==sum(influences))
    for mask,c in enumerate(coeff):
        mu=prod(p if not any(mask>>(j*w+i)&1 for i in range(w)) else epsilon**2/p for j in range(r))
        if mask:ck(c*c==4*P*mu)
        else:ck(c==2*P-1 and mu==P)
        blocks={i//w for i in range(n) if mask>>i&1}
        if len(blocks)==1:ck(c*c==4*epsilon**2*p**(2*r-2))
    counts['physical_spectral_coefficients']+=len(coeff)
    actual=prime_faces(truth,n)
    expected={tuple(1 if i in g else 0 for i in range(n)) for g in gates}
    ck(actual==expected)
    negative=prime_faces([not x for x in truth],n)
    expected_negative={tuple(-1 if i//w==j else 0 for i in range(n)) for j in range(r)}
    ck(negative==expected_negative)
    # Complementary polarity joins all coordinates of a one-block target.
    neg_supports=[{i for i,a in enumerate(s) if a} for s in negative]
    ck(len(components(set(range(w)),neg_supports))==1)
    for mode in range(3):
        raw=[F(1) if mode!=1 else F(1+(7*e)%5) for e in range(len(gates))]
        maxrow=max(sum(raw[e] for e,g in enumerate(gates) if i in g) for i in range(n))
        weights=[x/maxrow/(4 if mode==2 else 1) for x in raw]
        ck(all(sum(weights[e] for e,g in enumerate(gates) if i in g)<=1 for i in range(n)))
        prior_audit(n,gates,[x/2**r for x in weights])
    counts['truth_tables']+=1

if not args.pilot:
    # Genuinely non-prime but actual conjunction-gate table for a five-bit OR.
    gates=[{0,1},{1,2},{3},{2,4}]
    raw=[F(1),F(2),F(3),F(4)]
    scale=max(sum(raw[e] for e,g in enumerate(gates) if i in g) for i in range(5))
    prior_audit(5,gates,[a/scale/2**len(g) for a,g in zip(raw,gates)],packing_check=False)

orbits=[]
for w in ([4] if args.pilot else range(4,9)):
    r=2**w; pi=F(1,2**r)
    for t in ([0,r//2,r] if args.pilot else range(r+1)):
        # All width patterns up to permuting whole clauses; no lambda optimization is assumed.
        P=(1-F(1,r))**(r-t)*(1-F(1,2*r))**t
        blocks=[(r-t,w,F(1,r)),(t,w+1,F(1,2*r))]
        I=F(0); lower=F(0); entropy_upper=F(1)
        for multiplicity,width,epsilon in blocks:
            if not multiplicity:continue
            p=1-epsilon; outside=P/p
            Ij=2*multiplicity*width*epsilon*outside
            I+=Ij
            lower+=Ij*outside*(r*(1-2*p/width)-3*pi)
            entropy_upper+=4*P*multiplicity*epsilon*(2*width+F(3,2))
            ck(outside>F(1,3))
            ck(r*(1-2*p/width)-3*pi>0)
        ck(F(1,4)<P<F(2,3))
        ck(4*P*(1-P)>F(3,4))
        ck(I>F(w,4)>=1)
        ck(lower>F(r,7)*I)
        ck(entropy_upper<6*I)
        counts['heterogeneous_orbits']+=1
        if t in {0,r//2,r}:
            orbits.append({'w':w,'r':r,'wide_blocks':t,'I':str(I),
                           'cost_ratio_lower':str(lower/I),'entropy_ratio_upper':str(entropy_upper/I)})

# Exact guards: omitted root conditioning changes the mass; a nonprime whole-support gate merges components.
x=[F(1,16),F(1,16)]
D=prod(1+a for a in x)-1
ck((x[0]/D)>x[0])
ck(len(components({0,1},[{0,2},{1,2}]))==2)
ck(len(components({0,1},[{0,2},{1,2},{0,1,2}]))==1)
result={'status':'PASS','pilot':args.pilot,'assertions':assertions,'counts':counts,
        'seconds':time.monotonic()-start,'parameter_samples':orbits,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic':'integer Walsh, exact Fraction; analytic logs bounded rationally; no tolerance'}
(ROOT/'out').mkdir(exist_ok=True)
(ROOT/'out'/('pilot.json' if args.pilot else 'checks.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='parameter_samples'}))
