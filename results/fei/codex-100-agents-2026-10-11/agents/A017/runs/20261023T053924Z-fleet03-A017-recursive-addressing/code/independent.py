"""Separate direct character-sum and positive-integer erasure reproduction."""
import hashlib,json,time,sys
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[1];O=R/'out'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,v):(O/n).write_bytes((json.dumps(v,indent=2)+'\n').encode('utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def direct(t):return [sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(len(t))]
def entropy_product(groups):
    P=Q=1
    for group in groups:
        total=sum(group)
        if total:P*=total**total
        for v in group:
            if v:Q*=v**v
    return P,Q
def edge(t,j):return F(sum(t[x]!=t[x^(1<<j)] for x in range(len(t))),len(t))
def factor(z):
    d={};p=2
    while p*p<=z:
        while z%p==0:d[p]=d.get(p,0)+1;z//=p
        p+=1
    if z>1:d[z]=d.get(z,0)+1
    return d
def B(t,j):
    a=direct(t);d={}
    assert sum(x*x for x in a)==len(t)**2
    for s in range(len(a)):
        if s&(1<<j):continue
        u,v=a[s]**2,a[s^(1<<j)]**2
        for z,c in ((u+v,u+v),(u,-u),(v,-v)):
            if z:
                for p,e in factor(z).items():d[p]=d.get(p,0)+c*e
    return {p:F(c,len(t)**2) for p,c in d.items() if c}
def H(t):
    a=direct(t);d={2:F(2*(len(t).bit_length()-1))}
    for v in a:
        if v:
            for p,e in factor(abs(v)).items():d[p]=d.get(p,F(0))-F(2*v*v*e,len(t)**2)
    return {p:c for p,c in d.items() if c}
if '--freeze' in sys.argv:
    if (O/'independent_spec.json').exists() and read(O/'independent_spec.json')['helper_sha256']!=sha(Path(__file__)):
        (O/'independent_spec_v1_before_activation_addition.json').write_bytes((O/'independent_spec.json').read_bytes())
    write('independent_spec.json',dict(helper_version='A017-direct-interacting-reproduction-v2',helper_sha256=sha(Path(__file__)),
      actual_Boolean_family='all256 half-cube edit masks of q=x0*x1+x2*x3, plus saved actual 10-bit witness and its child',
      parameter_domain='n4 inside mask0..255, no outside edits; one n10 fixture and its n9 actual child; all16 two-bit h in tagged-half activation',case_count=273,
      symmetry='none',arithmetic='direct XOR/popcount character sums, integer entropy products, exact rational edge counts and prime exponents',
      memory_estimate_MB=40,max_runtime_seconds=60))
    print('FROZEN independent273 fixtures, including16 exact activation identities')
else:
    spec=read(O/'independent_spec.json');assert sha(Path(__file__))==spec['helper_sha256']
    start=time.monotonic();checks=0
    for mask in range(256):
        t=[]
        for x in range(16):
            q=(((x>>0)&1)*((x>>1)&1))^(((x>>2)&1)*((x>>3)&1))
            k=(x&1)|((x>>2)<<1)
            t.append((1-2*q)*(-1 if (x&2 and (mask>>k)&1) else 1))
        a=direct(t)
        assert sum(v*v for v in a)==256
        I=edge(t,2)+edge(t,3)
        assert edge(t,2)>=F(1,4) and edge(t,3)>=F(1,4)
        groups=[[a[s|(z<<2)]**2 for z in range(4)] for s in range(4)]
        P,Q=entropy_product(groups)
        bound=4*I*256;assert bound.denominator==1
        assert P<=Q*(1<<int(bound));checks+=4
    witness=read(O/'bad_intermediate_query.json')['truth_table']
    parent_spectrum=direct(witness);assert sum(v*v for v in parent_spectrum)==1024**2;checks+=1
    child=[witness[x] for x in range(1024) if not(x&256)]
    source=R.parent/'20261021T213328Z-fleet03-A017-recursive-addressing/out/boolean_counterexample.json'
    h=read(source)['truth_table'];bh=B(h,0);bc=B(child,0)
    assert bc=={p:v/2 for p,v in bh.items()};checks+=1
    assert edge(child,0)==F(1,16) and edge(witness,8)==F(1,4) and edge(witness,0)==F(5,16);checks+=1
    assert bh=={2:F(-704,256),5:F(120,256),17:F(136,256)};checks+=1
    assert 17**136*5**120>2**832;checks+=1
    for mask in range(16):
        h2=[1-2*((mask>>x)&1) for x in range(4)]
        activated=[1 if not(x&4) else (1-2*((x>>3)&1))*h2[x&3] for x in range(16)]
        expected={p:v/2 for p,v in H(h2).items()};expected[2]=expected.get(2,F(0))+2
        assert H(activated)=={p:v for p,v in expected.items() if v}
        assert sum(edge(activated,j) for j in range(4))==1+sum(edge(h2,j) for j in range(2))/2
        checks+=2
    result=dict(status='PASS',parents=273,exhaustive_four_bit_parents=256,activation_identities=16,assertions=checks,
      direct_character_sum_domains=[16,64,512,1024],elapsed_seconds=time.monotonic()-start,
      scope='Independent computational representation by A017, not external-agent proof review.')
    assert result['elapsed_seconds']<spec['max_runtime_seconds']
    write('independent_certificate.json',result);print(json.dumps(result))
