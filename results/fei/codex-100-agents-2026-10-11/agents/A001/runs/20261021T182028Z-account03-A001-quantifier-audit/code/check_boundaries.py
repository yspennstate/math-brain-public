from helpers import *
import helpers
from itertools import product
start=time.perf_counter();cases=0
for n in range(3):
    family=list(product((-1,1),repeat=1<<n))
    for b in family:
        for c in family:
            ck(time.perf_counter()-start<55)
            delta=F(sum(x!=y for x,y in zip(b,c)),len(b))
            G=selector(b,c);v=encoded(b,c)
            ck(entropy(spectrum(v))==add((1,entropy(spectrum(G))),(1,const(2*delta))))
            T=add((F(1,2),entropy(spectrum(b))),(F(1,2),entropy(spectrum(c))))
            JS=add((1,entropy(spectrum(G))),(-1,T),(-1,erase(G,0)))
            slack=add((1,const(3*delta)),(-1,JS))
            ck(not slack or interval(slack)[0]>0)
            cases+=1
b=[1 if y&7==0 else -1 for y in range(64)];c=b[:];c[0]=-1
v=encoded(b,c);N=len(v)
# A direct character sum reconstructs every coefficient independently of FWHT.
direct=[sum(v[x]*(-1 if (x&s).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
ck(direct==fw(v))
for j in range(9):
    ck(F(sum(direct[s]**2 for s in range(N) if s&(1<<j)),N*N)==inf(v,j))
# Dropping balance: h=+1, b=+1, c=y. Dropping freshness: h=y on the same data bit.
G=selector([1,1],[1,-1]);predicted=entropy(spectrum(G))
ck(predicted==const(2));ck(entropy(spectrum([1,1]))=={})
ck(entropy(spectrum([1,-1]))=={})
out={'status':'PASS','cases':cases,'direct_root_coefficients':N,'assertions':helpers.count,'seconds':time.perf_counter()-start,'balance_counterexample':{'b':[1,1],'c':[1,-1],'h':[1,1],'actual_H':'0','claimed_formula_H':'2'},'freshness_counterexample':{'b':[1,1],'c':[1,-1],'h_on_same_data_bit':[1,-1],'actual_H':'0','claimed_formula_H':'2'},'scope':'exact formula and rational JS upper bound checked; does not prove all-dimensional scalar JS theorem'}
(RUN/'out/BOUNDARIES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
