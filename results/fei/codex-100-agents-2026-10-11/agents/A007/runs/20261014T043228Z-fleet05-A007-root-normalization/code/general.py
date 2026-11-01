import itertools as it, json, math, time
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); assertions=0; intersections=0; roots=0
def check(v):
    global assertions
    assertions+=1
    assert v
    if time.perf_counter()-start>60: raise RuntimeError('frozen 60 second limit')
def compositions(s,k,positive):
    for values in it.product(range(1 if positive else 0,s+1),repeat=k):
        if sum(values)==s: yield values

for s in range(1,6):
    for k in range(1,s+1):
        for sizes in compositions(s,k,True):
            for kappas in it.product(*(range(sl,s+1) for sl in sizes)):
                for u in range(1,4):
                    # exp(s*K_ln)=product bracket^s_l, exact rational.
                    product=math.prod((Q(s,kap)**s / Q(s+u,kap+u)**(s+u))**sl for sl,kap in zip(sizes,kappas))
                    check(product>=1)
                    if all(kap==s for kap in kappas): check(product==1)
                    intersections+=1

for c in range(1,5):
    for widths in it.product(range(1,7),repeat=c):
        pi=tuple(Q(1,2**w) for w in widths); prod=math.prod(pi)
        for u in range(1,4):
            m=math.prod(range(u,u+c-1))
            for ua in compositions(u,c,False):
                ma=(1,) if c==1 else tuple(a*math.prod(range(u+1,u+c-1)) for a in ua)
                check(sum(ma)==m)
                check(sum(cnt*rarity/prod for cnt,rarity in zip(ma,pi))>=m*min(pi)/prod)
                check(min(pi)/prod==2**(sum(widths)-max(widths)))
                roots+=1

result={'status':'PASS','helper_version':'A007-root-intersection-budget-v1','assertions':assertions,
        'intersection_records':intersections,'root_records':roots,'elapsed_seconds':time.perf_counter()-start,
        'arithmetic':'exact rational products and integer/fraction root rarity credits',
        'unproved':'influence payment of complete signed arbitrary-support budget'}
(ROOT/'out'/'GENERAL_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
