"""A062-check-v1: exact finite identities; no numerical logarithms."""
from fractions import Fraction as Q
from collections import defaultdict
from pathlib import Path
import json, time

START = time.perf_counter()
RUN = Path(__file__).resolve().parents[1]
counts = defaultdict(int)

def check(a, b, category):
    assert a == b, (category, a, b)
    counts[category] += 1

def add(a, b, scale=Q(1)):
    c = dict(a)
    for p, v in b.items():
        c[p] = c.get(p, Q(0)) + scale*v
        if c[p] == 0:
            del c[p]
    return c

def factors(n):
    p = 2
    while p*p <= n:
        while n % p == 0:
            yield p
            n //= p
        p += 1
    if n > 1:
        yield n

def entropy(law):
    c = {}
    for w in law:
        if not w:
            continue
        for p in factors(w.numerator):
            c[p] = c.get(p, Q(0))-w
        for p in factors(w.denominator):
            c[p] = c.get(p, Q(0))+w
    return {p:v for p,v in c.items() if v}

def scale(a, s):
    return {p:v*s for p,v in a.items() if v*s}

def spectrum(f):
    a = list(f)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                u,v = a[j], a[j+h]
                a[j],a[j+h] = u+v,u-v
        h *= 2
    return [Q(x, len(a)) for x in a]

def data(f):
    a = spectrum(f)
    law = [v*v for v in a]
    check(sum(law), Q(1), 'parseval')
    n = len(f).bit_length()-1
    inf = [sum(law[s] for s in range(len(f)) if s & (1 << i)) for i in range(n)]
    direct = [Q(sum(f[x] != f[x ^ (1 << i)] for x in range(len(f))), len(f)) for i in range(n)]
    check(inf, direct, 'boundary_vs_fourier')
    return law, inf, sum(inf), entropy(law)

def restrict(f, block, assignment):
    n = len(f).bit_length()-1
    rest = [i for i in range(n) if i not in block]
    out = []
    for y in range(1 << len(rest)):
        x = sum(((y >> j) & 1) << i for j,i in enumerate(rest))
        x |= sum(((assignment >> j) & 1) << i for j,i in enumerate(block))
        out.append(f[x])
    return tuple(out)

def local(f, block):
    law, inf, infl, ent = data(f)
    n = len(inf)
    rest = [i for i in range(n) if i not in block]
    marginal = [Q(0)]*(1 << len(rest))
    for s,p in enumerate(law):
        t = sum(((s >> i) & 1) << j for j,i in enumerate(rest))
        marginal[t] += p
    children = [restrict(f,block,z) for z in range(1 << len(block))]
    weight = Q(1,len(children))
    child = [data(g) for g in children]
    avg_law = [sum(weight*d[0][t] for d in child) for t in range(len(marginal))]
    check(avg_law, marginal, 'physical_marginal')
    cost = sum(inf[i] for i in block)
    check(infl, cost+sum(weight*d[2] for d in child), 'local_influence')
    avg_h = {}
    for d in child:
        avg_h = add(avg_h,d[3],weight)
    erasure = add(ent,entropy(marginal),Q(-1))
    js = add(entropy(marginal),avg_h,Q(-1))
    delta = add(ent,avg_h,Q(-1))
    check(delta,add(erasure,js),'local_entropy')
    return children,cost,delta,erasure,js

def tree(f, policy, depth=0, history=()):
    law,inf,infl,ent = data(f)
    n = len(inf)
    if n == 0 or infl == 0 or (policy == 2 and depth >= 1 and history[-1] == 0) or (policy == 3 and depth >= 2):
        return Q(0),infl,{},ent,{},{}
    if policy == 4:
        # Independent stop coin, followed by a fair random coordinate choice.
        actions = [((),Q(1,3))]+[((i,),Q(2,3*n)) for i in range(n)]
    elif policy == 3:
        actions = [(tuple(range(min(2,n))),Q(1))]
    else:
        eligible = [i for i in range(n) if inf[i] > 0]
        i = min(eligible,key=lambda i: (-inf[i],i) if policy != 1 else (inf[i],i))
        actions = [((i,),Q(1))]
    spent,terminalI,drop,terminalH,eras,js = Q(0),Q(0),{},{},{},{}
    for block,pa in actions:
        if not block:
            terminalI += pa*infl
            terminalH = add(terminalH,ent,pa)
            continue
        children,cost,delta,b,j = local(f,block)
        spent += pa*cost
        drop = add(drop,delta,pa)
        eras = add(eras,b,pa)
        js = add(js,j,pa)
        for z,g in enumerate(children):
            ps = pa/len(children)
            s,ti,dh,th,bb,jj = tree(g,policy,depth+1,history+(z,))
            spent += ps*s
            terminalI += ps*ti
            drop = add(drop,dh,ps)
            terminalH = add(terminalH,th,ps)
            eras = add(eras,bb,ps)
            js = add(js,jj,ps)
    check(infl,spent+terminalI,'tree_influence')
    check(ent,add(drop,terminalH),'tree_entropy')
    check(drop,add(eras,js),'tree_erasure_js')
    return spent,terminalI,drop,terminalH,eras,js

tables = 0
for n in range(4):
    for mask in range(1 << (1 << n)):
        f = tuple(1 if mask & (1 << x) else -1 for x in range(1 << n))
        tables += 1
        for bits in range(1,1 << n):
            local(f,tuple(i for i in range(n) if bits & (1 << i)))
        results = [tree(f,p) for p in range(5)]
        mixture = [Q(1,2),Q(1,4),Q(1,8),Q(1,8)]
        _,_,infl,ent = data(f)
        check(infl,sum(w*(r[0]+r[1]) for w,r in zip(mixture,results)), 'random_policy_influence')
        hh = {}
        for w,r in zip(mixture,results):
            hh = add(hh,add(r[2],r[3]),w)
        check(ent,hh,'random_policy_entropy')
        assert time.perf_counter()-START < 60, 'pilot runtime exceeded'

# Actual Boolean branch where residual influence exceeds root influence.
f = tuple(1 if not (x&1) else (1 if ((x>>1).bit_count()%2)==0 else -1) for x in range(8))
rootI = data(f)[2]
children = [restrict(f,(0,),z) for z in range(2)]
childI = [data(g)[2] for g in children]
check(rootI,Q(3,2),'pathwise_counterexample_root')
check(childI,[Q(0),Q(2)],'pathwise_counterexample_children')

def serialize(q):
    return str(q)
result = {'helper_version':'A062-check-v1','truth_tables':tables,'dimensions':[0,1,2,3],
          'adaptive_policies':5,'assertions':sum(counts.values()),'counts':dict(counts),
          'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer FWHT + Fraction + formal prime logarithms',
          'failures':0,'pathwise_influence_witness':{'table':f,'rootI':str(rootI),'childI':list(map(str,childI))}}
(RUN/'out'/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
