from pathlib import Path
from fractions import Fraction as Q
import importlib.util
import time
import json

here=Path(__file__).resolve().parent
# Load only definitions, avoiding execution of the other script's job body.
namespace={}
source=(here/'check_restrictions.py').read_text(encoding='utf-8')
definitions=source.split("mode=sys.argv[1]")[0]
namespace['__file__']=str(here/'check_restrictions.py')
exec(compile(definitions,str(here/'check_restrictions.py'),'exec'),namespace)
walsh=namespace['walsh']; plus=namespace['plus']; add=namespace['add']; entropy=namespace['entropy']

start=time.perf_counter(); assertions=0; cases=0
def test(x):
    global assertions
    assert x; assertions+=1
    if time.perf_counter()-start>60: raise RuntimeError('Frozen limit exceeded')

def metrics(values,n):
    a=walsh(values); p=[v*v for v in a]
    test(sum(p)==1)
    B={}; R={}
    for i in range(n):
        for t in range(1<<n):
            if t>>i&1: continue
            u,v=p[t],p[t|(1<<i)]; q=u+v
            row=entropy([u,v]); add(row,q,q)
            B=plus((B,1),(row,1))
            if t: R=plus((R,1),(row,1))
    I=sum(s.bit_count()*v for s,v in enumerate(p))
    return B,R,I,p

def audit(base,n,m):
    global cases
    B,R,I,p=metrics(base,n)
    dim=m*n+1; size=1<<dim
    vals=[]
    for x in range(size):
        out=-1 if x>>(m*n)&1 else 1
        for j in range(m): out*=base[(x>>(j*n))&((1<<n)-1)]
        vals.append(out)
    BF,RF,IF,pF=metrics(vals,dim)
    test(plus((RF,1),(B,-m))=={})
    test(plus((BF,1),(RF,-1))=={})
    test(IF==m*I+1)
    test(all(v==0 for s,v in enumerate(pF) if not s>>(m*n)&1))
    cases+=1

for n in range(4):
    for mask in range(1<<(1<<n)):
        audit([1 if mask>>x&1 else -1 for x in range(1<<n)],n,1)
seeds=[([1],0),([1,-1],1),([-1,1,1,1],2),
       ([1 if 3-2*x.bit_count()>0 else -1 for x in range(8)],3),
       ([1 if not x>>(1+(x&1))&1 else -1 for x in range(8)],3)]
for values,n in seeds: audit(values,n,2)
result={'status':'PASS','cases':cases,'assertions':assertions,'runtime_seconds':time.perf_counter()-start,
        'identities':['R_nat(y*g^m)=m B_nat(g)','I(y*g^m)=m I(g)+1'],
        'arithmetic':'integer Walsh and Fraction formal logarithm identities',
        'scope':'Finite checks m=1,2; all-m and equal-optimal-constant conclusion are analytic.'}
out=here.parent/'out'; out.mkdir(exist_ok=True)
(out/'EMBEDDING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
