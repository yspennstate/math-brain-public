import itertools,json,math,time
from fractions import Fraction as R
from pathlib import Path
base=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0; traces=0
def test(x):
    global checks
    assert x
    checks+=1
rows=[]
for a in range(1,4):
 for b in range(a,4):
    edges=list(itertools.product(range(a),range(a,a+b)))
    lam=R(1,b); odds=lam/4; rootp=odds/(1+odds)
    none=(1-rootp)**len(edges); conditioning=1-none
    normalizer=(1+odds)**len(edges)-1
    N=2**(a+b)
    values=[2*int(any(x>>i&1 for i in range(a)) and any(x>>j&1 for j in range(a,a+b)))-1 for x in range(N)]
    physical=sum(R(sum(values[x]!=values[x^(1<<j)] for x in range(N)),N) for j in range(a+b))
    spectral_degree=R(0); qsum=R(0)
    for A in range(1,N):
        left=[i for i in range(a) if A>>i&1]; right=[j for j in range(a,a+b) if A>>j&1]
        walsh=sum(values[x]*(-1 if (A&x).bit_count()%2 else 1) for x in range(N))
        spectral_degree+=R(walsh**2,N**2)*A.bit_count()
        event=R(0)
        if not left or not right:
            active=left or right
            opposite=range(a,a+b) if left else range(a)
            for partners in itertools.product(opposite,repeat=len(active)):
                labels=[(i,j) if left else (j,i) for i,j in zip(active,partners)]
                test(len(set(labels))==len(active))
                # Full present/absent Bernoulli factors, conditional on nonempty roots.
                probability=rootp**len(labels)*(1-rootp)**(len(edges)-len(labels))/conditioning
                for _ in labels:
                    probability*=R(1,2)*R(1,2)*R(1,2) # size1, specified singleton, zero children
                event+=probability; traces+=1
            expected=(R(1,32)**len(left) if left else R(a,32*b)**len(right))/normalizer
        else:
            pivot=(left[0],right[0]); owners=[pivot]
            children=[(i,right[0]) for i in left[1:]]+[(left[0],j) for j in right[1:]]
            owners+=children
            test(len(owners)==len(set(owners)))
            test(all(e in edges for e in owners))
            # Every child has exactly its own selected singleton and one root endpoint.
            for e in children:
                test(len(set(e)&set(pivot))==1)
            c=len(children)
            probability=rootp*(1-rootp)**(len(edges)-1)/conditioning
            probability*=R(1,6) # size2 and its unique subset
            probability*=R(1,(c+1)*(c+2))*R(1,c+1) # count and fixed two-slot multiset
            for _ in children:
                probability*=lam*R(1,2)*R(1,2)*R(1,2)
            event=probability; traces+=1
            k=len(left)+len(right)
            expected=lam**(k-1)/R(24*8**(k-2)*(k-1)**2*k)/normalizer
        test(event==expected)
        qsum+=event
    test(qsum<=1)
    test(spectral_degree==physical)
    rows.append({'a':a,'b':b,'I':str(physical),'queue_subprobability':str(qsum)})
result={'helper_version':'A009-leafless-independent-replay-v1','functions':len(rows),'checks':checks,'distinct_explicit_traces':traces,'elapsed_seconds':time.perf_counter()-start,'all_passed':True,'cases':rows}
base.joinpath('out','VERIFY.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
