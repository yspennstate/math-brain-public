"""Exact finite audit of the stationary uniqueness improvement in PROOF.md."""
import os
import resource
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS,0) >= 15
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from itertools import product, permutations, combinations
from math import comb, factorial
from pathlib import Path
import json

def g(k):
    return (0,0,1,2,2)[k]

def C0(e):
    return (2-4*e)*(1-e**3/2)

def C(e):
    a = Q(1,2)-e
    return C0(e)-Q(17,630)*e**4*a**4

def polynomial(e):
    # Independently expanded 630*(C(e)-1).
    return (630-2520*e-630*e**3+1260*e**4
            -Q(17,16)*e**4+Q(17,2)*e**5
            -Q(51,2)*e**6+34*e**7-17*e**8)

def record(q):
    with localcontext() as ctx:
        ctx.prec=45
        return {'exact':str(q),'decimal':str(Decimal(q.numerator)/Decimal(q.denominator))}

pairs=0
slack_by_M={i:set() for i in range(5)}
for states in product(((0,0),(0,1),(1,1)),repeat=4):
    lo=[p[0] for p in states]
    hi=[p[1] for p in states]
    D=[h-l for l,h in zip(lo,hi)]
    M=sum(D)
    B=sum(D[i] for i in range(4) if any(
        all(lo[j]==hi[j]==b for j in range(4) if j!=i) for b in (0,1)))
    triples=sum(all(D[j] for j in t) for t in combinations(range(4),3))
    gap=M-B-(g(sum(hi))-g(sum(lo)))
    assert gap>=Q(1,2)*triples
    slack_by_M[M].add(gap)
    pairs+=1
assert pairs==81

# Independent reconstruction of p(k) at four rational parameters.
rule_checks=0
for bits in product((0,1),repeat=4):
    majority_probability=Q(sum(sum(bits[j] for j in t)>=2
        for t in combinations(range(4),3)),4)
    for e in (Q(0),Q(1,10),Q(24807685,10**8),Q(1,2)):
        assert e+(1-2*e)*majority_probability == e+(Q(1,2)-e)*g(sum(bits))
        rule_checks+=1

# Two fixed diagonal neighbors give one common 0 and one common 1.
# The source is a disagreement; the remaining axial input is arbitrary.
transmission_checks=0
for l,u in ((0,0),(0,1),(1,1)):
    increment=g(2+u)-g(1+l)
    assert increment>=1
    transmission_checks+=1

# Helper sites 0,1,2,3; receiver 4+j needs helpers j,j+1 first.
edges=[(j,4+j) for j in range(3)]+[(j+1,4+j) for j in range(3)]
extensions=0
for order in permutations(range(7)):
    ranks={v:i for i,v in enumerate(order)}
    extensions+=all(ranks[h]<ranks[r] for h,r in edges)
assert extensions==272

# Independent subset dynamic program counting legal prefixes.
ways=[0]*128
ways[0]=1
for mask in range(128):
    for v in range(7):
        if not (mask>>v)&1 and all((mask>>h)&1 for h,r in edges if r==v):
            ways[mask|(1<<v)]+=ways[mask]
assert ways[-1]==extensions

# Independent inclusion-exclusion for exact descents {2,4,6}.
ie=0
terms=[]
for mask in range(8):
    cuts=[0]+[2*(i+1) for i in range(3) if (mask>>i)&1]+[7]
    composition=[b-a for a,b in zip(cuts,cuts[1:])]
    number=factorial(7)
    for size in composition:
        number//=factorial(size)
    term=(-1)**(3-mask.bit_count())*number
    terms.append(term)
    ie+=term
assert ie==extensions
clock_order=Q(extensions,factorial(7))
clock_integral=sum(Q((-1)**j*comb(7,j),j+1) for j in range(8))
assert clock_integral==Q(1,8)
clock_constant=clock_order*clock_integral
assert clock_constant==Q(17,2520)
assert clock_constant==Q(extensions,factorial(8))
broadcast=2*clock_constant
assert broadcast==Q(17,1260)
correction=2*broadcast
assert correction==Q(17,630)

# Check diagonal geometry for each choice of the omitted receiver.
diagonals=[(1,1),(1,-1),(-1,-1),(-1,1)]
receivers=[(0,1),(1,0),(0,-1),(-1,0)]
geometry_checks=0
for omitted in receivers:
    chosen=[v for v in receivers if v!=omitted]
    for pattern in ((0,1,0,1),(1,0,1,0)):
        for x,y in chosen:
            near=[pattern[i] for i,(u,v) in enumerate(diagonals) if abs(x-u)+abs(y-v)==1]
            assert sorted(near)==[0,1]
            geometry_checks+=1

old_lo=Q(558619565237287,2251799813685248)
old_hi=Q(69827445654661,281474976710656)
assert C0(old_lo)>1>C0(old_hi)
assert C(old_lo)<1
lo,hi=Q(0),Q(1,4)
for _ in range(70):
    mid=(lo+hi)/2
    assert polynomial(mid)==630*(C(mid)-1)
    if C(mid)>1:
        lo=mid
    else:
        hi=mid
assert C(lo)>1>C(hi)
grid_lo=Q(24807681,10**8)
grid_hi=Q(24807683,10**8)
assert C(grid_lo)>1>C(grid_hi)
endpoint=Q(24807685,10**8)
assert hi<grid_hi<endpoint<old_lo
assert C(endpoint)<1<C0(endpoint)
for e in (Q(0),Q(1,4),Q(1,2),endpoint,lo,hi):
    assert polynomial(e)==630*(C(e)-1)

result={
    'status':'all assertions passed',
    'ordered_pairs':pairs,
    'local_slack_by_M':{k:sorted(v) for k,v in slack_by_M.items()},
    'update_rule_checks':rule_checks,
    'transmission_cases':transmission_checks,
    'geometry_checks':geometry_checks,
    'linear_extensions_permutations':extensions,
    'linear_extensions_dynamic_program':ways[-1],
    'linear_extensions_inclusion_exclusion':ie,
    'inclusion_exclusion_terms':terms,
    'clock_order_probability':record(clock_order),
    'age_integral':record(clock_integral),
    'clock_constant':record(clock_constant),
    'broadcast_coefficient_before_e4_a3':record(broadcast),
    'contraction_correction_coefficient_before_e4_a4':record(correction),
    'new_root_lower':record(lo),
    'new_root_upper':record(hi),
    'new_root_width':record(hi-lo),
    'old_minus_new_root_lower_bound':record(old_lo-hi),
    'old_minus_new_root_upper_bound':record(old_hi-lo),
    'new_rational_endpoint':record(endpoint),
    'new_contraction_at_endpoint':record(C(endpoint)),
    'old_contraction_at_endpoint':record(C0(endpoint)),
    'nice':os.getpriority(os.PRIO_PROCESS,0),
    'OMP_NUM_THREADS':os.environ['OMP_NUM_THREADS'],
    'cpu_time_limit_seconds':30,
    'peak_rss_bytes_macos':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
}
output=json.dumps(result,sort_keys=True,indent=2)+'\n'
Path(__file__).with_name('audit_output.json').write_text(output)
print(output,end='')
