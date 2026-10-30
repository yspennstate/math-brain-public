"""Independent exact reconstruction; no floating point arithmetic in assertions."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
VERSION='A021-arbitrary-controller-face-v1'

def walsh(a):
    a=list(a); h=1
    while h<len(a):
        for k in range(0,len(a),2*h):
            for j in range(k,k+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return [Q(x,len(a)) for x in a]

def influence(a):
    n=(len(a)-1).bit_length()
    return sum(Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(n))

def erasure(a,b):
    """Exact formal linear combination of h2(rational) atoms."""
    ans={}
    for x,y in zip(walsh(a),walsh(b)):
        mass=(x*x+y*y)/2
        if not mass:continue
        r=(x+y)**2/(2*(x*x+y*y));r=min(r,1-r)
        if not r:continue
        ans[r]=ans.get(r,Q(0))+mass
    return ans

def multiply_ledger(ledger,p):
    return {r:v*p for r,v in ledger.items() if v*p}

def activate(a,g):return [1+aa*(gg-1) for aa in a for gg in g]

def union_table(sets,n):
    return [int(any((x&s)==s for s in sets)) for x in range(1<<n)]

def union_ie(sets):
    p=j=Q(0)
    for mask in range(1,1<<len(sets)):
        u=0
        for e,s in enumerate(sets):
            if mask>>e&1:u|=s
        c=(-1)**(mask.bit_count()+1)*Q(1,1<<u.bit_count())
        p+=c;j+=u.bit_count()*c
    return p,j

def restrict(a,j,b):
    n=(len(a)-1).bit_length()
    return [a[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(1<<(n-1))]

def boundary(a):return influence([1-2*x for x in a])/2

def run():
    start=time.perf_counter(); pairs=0;atoms=0
    balanced=[g for g in product((-1,1),repeat=4) if sum(g)==0]
    examples=[]
    for bits in range(256):
        a=[bits>>x&1 for x in range(8)]
        p=Q(sum(a),8);j=boundary(a)
        for gp in balanced:
            for gm in balanced:
                fp,fm=activate(a,gp),activate(a,gm)
                d=Q(sum(x!=y for x,y in zip(gp,gm)),4)
                coreproduct=[x*y for x,y in zip(gp,gm)]
                fproduct=[x*y for x,y in zip(fp,fm)]
                original=erasure(gp,gm);actual=erasure(fp,fm)
                assert actual==multiply_ledger(original,p)
                assert Q(sum(x!=y for x,y in zip(fp,fm)),len(fp))==p*d
                assert influence(fproduct)/2==p*influence(coreproduct)/2+d*j
                pairs+=1;atoms+=len(actual)
    unions=0;max_overcount=Q(0);max_example=None
    for sets in combinations_with_replacement(range(1,16),3):
        a=union_table(sets,4);p,j=union_ie(sets)
        assert p==Q(sum(a),16);assert j==boundary(a)
        naive=sum(Q(s.bit_count(),1<<s.bit_count()) for s in sets)
        if j and naive/j>max_overcount:
            max_overcount=naive/j;max_example=sets
        unions+=1
    recursions=0
    for bits in range(256):
        a=[bits>>x&1 for x in range(8)]
        for coord in range(3):
            plus,minus=restrict(a,coord,1),restrict(a,coord,0)
            cost=Q(sum(x!=y for x,y in zip(plus,minus)),2*len(plus))
            assert boundary(a)==cost+(boundary(plus)+boundary(minus))/2
            recursions+=1
    # Exact adaptive control/selector scheduling with m=4, delta=1/16.
    # Each state keeps a controller table, number of selectors left, and
    # selector parity. Policy can depend on previous fair selector values.
    delta=Q(1,16);m=4;t=3
    policies={
        'selectors_first':lambda a,left,parity: 'S' if left else 'C',
        'controls_first':lambda a,left,parity: 'C' if len(a)>1 else 'S',
        'adaptive':lambda a,left,parity: 'S' if left and (parity or len(a)==1) else 'C',
        'alternating':lambda a,left,parity: 'S' if left and ((len(a)-1).bit_length()+left)%2 else 'C',
    }
    def walk(a,left,parity,policy):
        if not sum(a) or (left==0 and len(a)==1):return (Q(0),)*4
        action=policy(a,left,parity)
        if not left:action='C'
        if len(a)==1:action='S'
        if action=='S':
            children=[walk(a,left-1,parity^b,policy) for b in (0,1)]
            p=Q(sum(a),len(a));j=boundary(a)
            increment=(delta*(m*p+j),j,p,Q(0))
        else:
            children=[walk(restrict(a,0,b),left,parity,policy) for b in (0,1)]
            increment=(Q(0),Q(0),Q(0),boundary(a)-sum(boundary(restrict(a,0,b)) for b in (0,1))/2)
        return tuple(inc+(children[0][k]+children[1][k])/2 for k,inc in enumerate(increment))
    policy_cases=[]
    for sets in ((1,2,4),(3,5,6),(3,6,12),(3,3,3)):
        a=union_table(sets,4);p=Q(sum(a),16);j=boundary(a)
        for name,policy in policies.items():
            charge,exposure,pmass,spent=walk(a,t,0,policy)
            assert pmass==t*p
            assert charge==delta*(m*t*p+exposure)
            assert spent==j
            if name=='selectors_first':assert exposure==t*j
            if name=='controls_first':assert exposure==0
            policy_cases.append({'events':sets,'policy':name,'density':str(p),'boundary':str(j),'exposure':str(exposure),'selector_charge':str(charge),'spent_controller_budget':str(spent)})
    out={'status':'PASS','helper_version':VERSION,'balanced_child_pairs':pairs,'formal_entropy_atoms_checked':atoms,'three_event_unions':unions,'boundary_recursions':recursions,'adaptive_policy_cases':len(policy_cases),'maximum_naive_union_boundary_overcount_in_frozen_domain':str(max_overcount),'max_example':max_example,'arithmetic':'integers, Fraction, formal h2(rational) coefficients; no logarithm approximation','seconds':time.perf_counter()-start}
    (ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'out'/'policy_certificates.json').write_text(json.dumps(policy_cases,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':run()
