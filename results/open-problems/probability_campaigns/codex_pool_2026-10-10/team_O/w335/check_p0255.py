from fractions import Fraction as F
import itertools
import json
import math
import pathlib
import random
import time
from bundle_tools import emit, entry, edge_to_problem, edge_to_attempt

root=pathlib.Path(__file__).resolve().parent
start=time.perf_counter()

def distances(n,edges):
    d=[[0 if i==j else float('inf') for j in range(n)] for i in range(n)]
    for i,j,w in edges:
        d[i][j]=d[j][i]=w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

def lengths(d):
    values=[]
    for start_vertex in range(len(d)):
        remaining=set(range(len(d)))-{start_vertex}
        current=start_vertex
        total=0
        while remaining:
            target=min(remaining,key=lambda v:(d[current][v],v))
            total+=d[current][target]
            remaining.remove(target)
            current=target
        values.append(int(total))
    return values

one_leaf_cases=[]
for weight in (1,2,17,1000000):
    one_leaf_values=lengths(distances(2,[(0,1,weight)]))
    assert one_leaf_values==[weight,weight]
    one_leaf_cases.append({'weight':weight,'lengths':one_leaf_values,'cv':0})
star_cases=0
for m in range(2,6):
    for weights in itertools.product(range(1,5),repeat=m):
        values=lengths(distances(m+1,[(0,i+1,w) for i,w in enumerate(weights)]))
        S=sum(weights)
        largest=sorted(weights,reverse=True)[:2]
        expected=[2*S-largest[0]]+[2*S-weights[r]-max(weights[j] for j in range(m) if j!=r) for r in range(m)]
        assert values==expected
        mean=F(sum(values),len(values))
        variance=sum((F(value)-mean)**2 for value in values)/len(values)
        assert variance<=mean**2/F(24)
        star_cases+=1
attain_mean=F(2)*F(3,5)+F(3)*F(2,5)
attain_var=F(3,5)*(2-attain_mean)**2+F(2,5)*(3-attain_mean)**2
assert attain_var/attain_mean**2==F(1,24)
rng=random.Random(3350255)
best={'cv':-1}
for case in range(200):
    n=5+case%6
    edges=[(i,rng.randrange(i),rng.randint(1,100)) for i in range(1,n)]
    present={tuple(sorted((i,j))) for i,j,_ in edges}
    for i in range(n):
        for j in range(i+1,n):
            if (i,j) not in present and rng.random()<0.3:
                edges.append((i,j,rng.randint(1,100)))
    values=lengths(distances(n,edges))
    mean=sum(values)/n
    cv=math.sqrt(sum((value-mean)**2 for value in values)/n)/mean
    if cv>best['cv']:
        best={'case':case,'n':n,'cv':cv,'edges':edges,'lengths':values}
measurement={'command':'python -X utf8 check_p0255.py','exhaustive_star_vectors':star_cases,'one_leaf_boundary_cases':one_leaf_cases,'sharp_arbitrary_start_cv_squared':'1/24','star_absolute_cv_bound':1/(2*math.sqrt(6)),'seeded_general_graph_cases':200,'general_graph_maximum_found':best,'elapsed_seconds':round(time.perf_counter()-start,6),'result':'PASS; general graph search is numerical evidence only'}
(root/'p0255_measurement.json').write_text(json.dumps(measurement,indent=2),encoding='utf-8')
statement='For a finite star with at least one leaf and positive edge lengths, and a nearest-unvisited walk that stops after all vertices are visited, every random start distribution satisfies sd(L)/E L<=1/(2*sqrt(6)). For at least two leaves, write S for the sum of all edge lengths and w_1>=w_2 for the largest two. All lengths lie in [2S-w_1-w_2,2S-w_1], whose endpoint ratio is at most 3/2. A one-leaf star has constant positive length and coefficient zero. The constant is sharp over arbitrary start distributions; the uniform-start case is included but no optimality claim for that subclass is made. This does not prove an absolute bound for arbitrary graphs.'
proof=(root/'P0255_proof.md').read_text(encoding='utf-8').split('Consider a star',1)[1].split('\n\nThe earlier attempt',1)[0]
new=entry('p0255-weighted-star-cv','probability.random-graphs','weighted-star-nearest-unvisited-walk-coefficient-of-variation-bound','lemma','An absolute variation bound for weighted-star NUV walks',statement,'Consider a star'+proof,['Positive weighted star with at least one leaf','Walk stops on visiting the final new vertex','Arbitrary random starting vertex'])
relations=[edge_to_problem('P0255',new['key'],'This does not prove an absolute bound for arbitrary graphs'),edge_to_attempt('P0255',new['key'],'endpoint ratio is at most 3/2','a rigorous O(sqrt(log n)) coefficient-of-variation bound follows','specializes')]
emit(5,'P0255',[new],relations,'P0255_proof.md','p0255_measurement.json')
print(json.dumps(measurement),flush=True)
