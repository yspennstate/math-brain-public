from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import itertools,math,json,time
R=Path(__file__).resolve().parents[1];start=time.monotonic();assertions=0
def ck(x):
    global assertions
    assertions+=1;assert x
    if time.monotonic()-start>300:raise TimeoutError('Independent fixed-domain budget')
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def direct_spectrum(values):
    N=len(values)
    return [F(sum(y*(-1 if (A&x).bit_count()%2 else 1) for x,y in enumerate(values))**2,N*N) for A in range(N)]
def direct_mass(n,edges,A):
    E={frozenset(e) for e in edges};V=[i for i in range(n) if A>>i&1];lam=F(1,n-1);total=F(0)
    def perfect(vertices):
        if not vertices:yield [];return
        u=vertices[0]
        for v in vertices[1:]:
            if frozenset((u,v)) in E:
                for M in perfect([x for x in vertices if x not in (u,v)]):yield [(u,v)]+M
    # Independent-unmatched-set parameterization, not the main matching recursion.
    for Ubits in range(1<<len(V)):
        U=[x for j,x in enumerate(V) if Ubits>>j&1]
        if any(frozenset((u,v)) in E for u,v in itertools.combinations(U,2)):continue
        root=[x for x in V if x not in U]
        if len(root)%2:continue
        for M in perfect(root):
            endpoints=[x for e in M for x in e];choices=[]
            for u in U:
                choices.append([(x,lam/(8 if x in endpoints else 32)) for x in range(n) if frozenset((u,x)) in E])
            for chosen in itertools.product(*choices):
                term=(lam/24)**len(M);counts={x:0 for x in endpoints}
                for x,w in chosen:
                    term*=w
                    if x in counts:counts[x]+=1
                for u,v in M:
                    a,b=counts[u],counts[v]
                    term*=F(math.factorial(a)*math.factorial(b),(a+b+1)**2*(a+b+2))
                total+=term
    return total

src=read(R/'out/check.json');rows=[x for x in src['rows'] if x['density_hypothesis']];sets=0
for row in rows:
    n=row['n'];edges=row['edges'];em=[sum(1<<v for v in e) for e in edges]
    values=[1-2*int(not any(x&e==e for e in em)) for x in range(1<<n)]
    p=direct_spectrum(values);v=1-p[0];I=sum((A.bit_count()*z for A,z in enumerate(p)),F(0))
    ck(v==F(row['v']));ck(I==F(row['I']));ck(sum(p)==1)
    masses=[direct_mass(n,edges,A) for A in range(1,1<<n)];Z=sum(masses)
    ck(Z==F(row['Z_F']));q=[z/Z for z in masses]
    ck(q==[F(z) for z in row['complete_original_q']]);sets+=len(masses)
    # Verify the exact downset boundary directly by cube-edge counting.
    boundary=sum(values[x]!=values[x^(1<<i)] for x in range(1<<n) for i in range(n))//2
    ck(I==F(boundary,1<<(n-1)))
out={'method':'independent unmatched-set/perfect-matching partition; direct character spectrum; direct cube boundary','graphs':len(rows),'nonempty_sets':sets,'assertions':assertions,'elapsed_seconds':time.monotonic()-start}
(R/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
