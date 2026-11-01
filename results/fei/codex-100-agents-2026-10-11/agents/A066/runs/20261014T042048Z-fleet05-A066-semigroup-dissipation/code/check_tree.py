from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache
import json,sys,time
run=Path(__file__).resolve().parents[1]
source=run/'code/check_quotient.py'
ns={'__file__':str(source)}
exec(compile(source.read_text().split('cases=rows=0')[0],str(source),'exec'),ns)
test,logadd,combine,bound,walsh=[ns[x] for x in ['test','logadd','combine','bound','physical_spectrum']]
mode=sys.argv[1]; started=time.perf_counter()
def child(q,i,y):
    return tuple(q[(x&((1<<i)-1))|((x>>i)<<(i+1))|(y<<i)] for x in range(len(q)//2))
@lru_cache(None)
def influence(q):
    return sum(Q(sum(q[x]!=q[x^(1<<i)] for x in range(len(q))),len(q)) for i in range((len(q)-1).bit_length()))
@lru_cache(None)
def loss(q,d,i):
    coeff=walsh(q); delta=Q(1,1<<d); t=Q(1,1<<(d//2)); alpha=1-coeff[0]; beta=coeff[1<<i]
    if not beta: return {}
    R=1+delta*(coeff[0]**2+beta**2-1); result={}
    for sigma in [-1,1]:
        c=1-2*alpha*sigma*t+delta*(alpha**2+beta**2)
        logadd(result,R/c,delta*beta**2*(1+sigma*t)/2)
    return result
@lru_cache(None)
def prefix(q,d,order):
    delta=Q(1,1<<d); core=Q(d,2)+d*delta*(1-Q(sum(q),len(q)))
    if not order: return {},influence(q),core+delta*influence(q),Q(0)
    i=order[0]; next_order=tuple(j-(j>i) for j in order[1:])
    paid=loss(q,d,i); leafIq=leafI=removed=Q(0)
    pivot=Q(sum(q[x]!=q[x^(1<<i)] for x in range(len(q))),len(q))
    for y in [0,1]:
        P,Iq,I,rem=prefix(child(q,i,y),d,next_order)
        paid=combine((paid,1),(P,Q(1,2))); leafIq+=Iq/2; leafI+=I/2; removed+=rem/2
    removed+=pivot
    test(influence(q)-leafIq==removed)
    test(core+delta*influence(q)-leafI==delta*removed)
    test(bound(paid)[1]<=Q(256,9)*delta*delta*removed)
    return paid,leafIq,leafI,removed
count=0
for d in ([4] if mode=='pilot' else [4,6]):
    for r in ([1,2] if mode=='pilot' else [1,2,3]):
        for mask in range(1<<(1<<r)):
            q=tuple(1 if mask>>x&1 else -1 for x in range(1<<r))
            for order in permutations(range(r)):
                for depth in range(1,r+1):
                    prefix(q,d,order[:depth]); count+=1
test(count==(68 if mode=='pilot' else 9352))
out={'mode':mode,'prefix_cases':count,'assertions':ns['ns']['assertions'],'elapsed_seconds':time.perf_counter()-started,
     'bound':'cumulative discarded KL <=(256/9)*delta*removed physical influence, control-only queries',
     'terminal':'Exact average full leaf influence and unrevealed Boolean gate retained; terminal entropy not declared paid',
     'arithmetic':'Exact Fraction and prime-log identities; rational log enclosure only for paid bound'}
(run/'out'/('TREE_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
