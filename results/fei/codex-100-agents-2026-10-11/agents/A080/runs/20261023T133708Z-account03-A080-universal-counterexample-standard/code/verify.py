"""Different frame: validate feasible duals + attaining physical trees, no DP."""
import functools
import itertools
import json
import math
import time
from fractions import Fraction
from pathlib import Path

root=Path(__file__).resolve().parents[1]
started=time.monotonic()
count=0

def require(ok, label):
    global count
    count+=1
    if not ok:
        raise AssertionError(label)
    if time.monotonic()-started>55:
        raise RuntimeError('Frozen verifier cap')

def combine(*forms):
    result={}
    for f in forms:
        for p,c in f:
            result[p]=result.get(p,Fraction(0))+c
    return tuple(sorted((p,c) for p,c in result.items() if c))

def times(a,q):
    return tuple((p,c*q) for p,c in a if c*q)

def rational(x):
    return ((2,Fraction(x)),) if x else ()

def difference(a,b):
    return combine(a,times(b,-1))

@functools.lru_cache(None)
def nonnegative(a):
    multiple=math.lcm(*(c.denominator for _,c in a)) if a else 1
    lhs=rhs=1
    for p,c in a:
        exponent=c.numerator*(multiple//c.denominator)
        if exponent>0:
            lhs*=pow(p,exponent)
        else:
            rhs*=pow(p,-exponent)
    return lhs>=rhs

def log_integer(v):
    result=[]
    k=2
    while k<=v:
        exponent=0
        while v%k==0:
            exponent+=1
            v//=k
        if exponent:
            result.append((k,Fraction(exponent)))
        k+=1
    return tuple(result)

@functools.lru_cache(None)
def observable(table):
    N=len(table)
    n=N.bit_length()-1
    H=()
    # Direct Fourier definition, independent of producer's butterfly transform.
    spectrum=[sum(table[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
    require(sum(v*v for v in spectrum)==N*N,'direct Parseval')
    for v in spectrum:
        if v:
            probability=Fraction(v*v,N*N)
            logarithm=difference(log_integer(probability.numerator),log_integer(probability.denominator))
            H=combine(H,times(logarithm,-probability))
    # Each unoriented physical edge is visited once.
    I=sum((Fraction(sum(table[x]!=table[x+(1<<i)] for x in range(N) if not x&(1<<i)),N//2) for i in range(n)),Fraction(0))
    return H,I

def section(table, coordinate, bit):
    return tuple(value for x,value in enumerate(table) if (x//(2**coordinate))%2==bit)

def tensor(f,g):
    return tuple(f[x]*g[y] for y in range(len(g)) for x in range(len(f)))

def load_form(raw):
    return tuple((p,Fraction(c)) for p,c in raw)

def walk(tree, table, K, reach=Fraction(1)):
    H,I=observable(table)
    if tree.get('stop'):
        d=difference(H,rational(K*I))
        require(nonnegative(d),'attaining tree has nonnegative terminal signed deficit')
        return [(reach,table,d)]
    i=tree['query']
    require(0<=i<len(table).bit_length()-1,'query is a remaining physical coordinate')
    require(len(tree['children'])==2,'both full outcomes')
    result=[]
    for b in (0,1):
        result.extend(walk(tree['children'][b],section(table,i,b),K,reach/2))
    return result

def main():
    certificate=json.loads((root/'out'/'main_certificates.json').read_text(encoding='utf-8'))
    duals={(tuple(row['f']),Fraction(row['K'])):load_form(row['value']) for row in certificate['dual']}
    rates=tuple(map(Fraction,('0','1/2','1','3/2','2','4')))
    tables=[f for n in range(3) for f in itertools.product((-1,1),repeat=2**n)]
    require(len(duals)==132,'complete factor dual domain')
    for (f,K),u in duals.items():
        H,I=observable(f)
        require(nonnegative(u),'nonnegative dual')
        require(nonnegative(difference(u,difference(H,rational(K*I)))),'dual majorizes signed obstacle')
        for i in range(len(f).bit_length()-1):
            mean=times(combine(duals[(section(f,i,0),K)],duals[(section(f,i,1),K)]),Fraction(1,2))
            require(nonnegative(difference(u,mean)),'every dual physical-query inequality')
    
    lifted_states=0
    for f,g in itertools.product(tables,repeat=2):
        H,I=observable(tensor(f,g))
        for K in rates:
            u=combine(duals[(f,K)],duals[(g,K)])
            require(nonnegative(u),'lifted dual nonnegative')
            require(nonnegative(difference(u,difference(H,rational(K*I)))),'lifted dual majorizes ACTUAL product deficit')
            for which,t in enumerate((f,g)):
                for i in range(len(t).bit_length()-1):
                    us=[]
                    for b in (0,1):
                        args=[f,g]
                        args[which]=section(t,i,b)
                        us.append(combine(duals[(args[0],K)],duals[(args[1],K)]))
                    require(nonnegative(difference(u,times(combine(*us),Fraction(1,2)))),'lifted dual every physical query')
            lifted_states+=1
    
    leaves={}
    for row in certificate['policies']:
        f,K=tuple(row['f']),Fraction(row['K'])
        terminal=walk(row['tree'],f,K)
        require(sum((p for p,_,_ in terminal),Fraction(0))==1,'policy total reach')
        value=combine(*(times(d,p) for p,_,d in terminal))
        require(value==duals[(f,K)]==load_form(row['value']),'primal attains independently feasible dual')
        leaves[(f,K)]=terminal
    
    for row in certificate['tensor']:
        f,g,K=tuple(row['f']),tuple(row['g']),Fraction(row['K'])
        payoff=()
        for p,a,_ in leaves[(f,K)]:
            for q,b,_ in leaves[(g,K)]:
                H,I=observable(tensor(a,b))
                d=difference(H,rational(K*I))
                require(nonnegative(d),'actual joint terminal signed deficit')
                payoff=combine(payoff,times(d,p*q))
        upper=combine(duals[(f,K)],duals[(g,K)])
        require(payoff==upper==load_form(row['hull']),'actual policy attains lifted feasible dual')
    
    summary={'status':'PASS','method':'Direct characters; feasible primal/dual trees; no Bellman recurrence or producer import','factor_dual_rows':len(duals),'lifted_dual_states':lifted_states,'physical_policy_trees':len(leaves),'tensor_root_receipts':len(certificate['tensor']),'exact_predicates':count,'direct_character_tables':observable.cache_info().currsize,'elapsed_seconds':time.monotonic()-started,'scope':'Separate author implementation; external independent-agent review pending'}
    (root/'out'/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary),flush=True)

if __name__ == "__main__":
    main()
