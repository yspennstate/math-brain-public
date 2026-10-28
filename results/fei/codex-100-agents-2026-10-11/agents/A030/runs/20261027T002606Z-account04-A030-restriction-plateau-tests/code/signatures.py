from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib,json,time,sys
start=time.perf_counter();checks=0;count=0
def test(x):
    global checks
    checks+=1
    assert x,checks
    assert time.perf_counter()-start<55
def fw(table):
    out=list(table);s=1
    while s<len(out):
        for b in range(0,len(out),2*s):
            for j in range(b,b+s):
                a,c=out[j],out[j+s];out[j],out[j+s]=a+c,a-c
        s*=2
    return [Q(a,len(out)) for a in out]
domain=[(1,2,1)] if '--pilot' in sys.argv else [(1,2,1),(1,3,2),(2,2,1),(1,4,3)]
rows=[]
for k,L,d in domain:
    n=2*k*L+1;N=1<<n;gs=[[],[]]
    for x in range(N//2):
        block=[((x>>(j*L))&((1<<L)-1)).bit_count()%2 for j in range(2*k)]
        for s in (0,1):gs[s].append((-1)**sum((block[2*j]^s)*block[2*j+1] for j in range(k)))
    table=gs[0]+gs[1]
    a,b=map(fw,gs)
    root=fw(table);ref=[(x*x+y*y)/4 for x,y in zip(a,b)]*2
    # Selector first is highest-coordinate pair deletion, independently of primary's low-bit channel.
    for s in (0,1):
        inherited=[]
        for t in range(N//2):
            u,v=root[t],root[t+N//2];norm=u*u+v*v
            mass=(ref[t]+ref[t+N//2])*((u+(-1)**s*v)**2/(2*norm) if norm else Q(1,2))
            inherited.append(2*mass)
        test(inherited==[z*z for z in (a if s==0 else b)])
    before=count
    for q in range(d+1):
        for chosen in combinations(range(n),q):
            live=[i for i in range(n) if i not in chosen]
            for assignment in range(1<<q):
                base=sum(((assignment>>j)&1)<<i for j,i in enumerate(chosen))
                restricted=[table[base+sum(((z>>j)&1)<<i for j,i in enumerate(live))] for z in range(1<<len(live))]
                p=[z*z for z in fw(restricted)]
                test(sum(p)==1)
                test(sum(z>0 for z in p)==4**k)
                test(all(z==Q(1,4**k) for z in p if z))
                influences=[sum(z for t,z in enumerate(p) if (t>>j)&1) for j in range(len(live))]
                test(all(v==Q(1,2) for v in influences))
                test(sum(influences)==L*k+Q(1,2)-Q(q,2))
                count+=1
    rows.append({'k':k,'L':L,'d':d,'restrictions':count-before,'selector_first_inherited_reference_exact':True})
out={'status':'PASS','domain':rows,'restrictions':count,'exact_predicates':checks,'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
dest=Path(__file__).resolve().parents[1]/'out'/('SIGNATURE_PILOT.json' if '--pilot' in sys.argv else 'SIGNATURES.json')
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
