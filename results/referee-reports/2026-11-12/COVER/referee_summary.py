"""Small exact second checks and report evidence, using only referee modules."""
import json
import math
import resource
import signal
import time
from fractions import Fraction as F
from pathlib import Path
from referee_cones import add, mul, prod, scale, U
from referee_exact import inspect, augmented_blocks, alternating, chain, stationary

signal.alarm(280)
start=time.monotonic()
a,b,c=({U[i]:1} for i in range(3))
tau=add(mul(a,b),mul(a,c),mul(b,c))
q=[add(a,b),add(a,c),add(b,c)]
Bs=[prod([q[i],q[j],add(q[i],q[j],scale(w,2))])
    for i,j,w in [(0,1,a),(0,2,b),(1,2,c)]]
Q=add(scale(add(prod([a,a,a]),prod([b,b,b]),prod([c,c,c])),4),
      scale(add(*(prod([v,v,u]) for i,v in enumerate([a,b,c])
                  for j,u in enumerate([a,b,c]) if i!=j)),-1),scale(prod([a,b,c]),-6))
assert add(*Bs,scale(mul(add(*q),tau),-4))==Q
S=add(prod([a,a,a]),prod([b,b,b]),prod([c,c,c]),scale(prod([a,b,c]),3),
      scale(add(*(prod([v,v,u]) for i,v in enumerate([a,b,c])
                  for j,u in enumerate([a,b,c]) if i!=j)),-1))
assert add(S,scale(add(prod([a,a,a]),prod([b,b,b]),prod([c,c,c]),
                       scale(prod([a,b,c]),-3)),3))==Q

exact=json.loads(Path('referee_exact_results.json').read_text())
cones=json.loads(Path('referee_cones_results.json').read_text())
numeric=json.loads(Path('referee_numeric_results.json').read_text())
out={'three_state_polynomial_identity':True,'three_state_Schur_split':True,
     'holding_example':{},'named_no_holding':{},'rounded_numerical_endpoints':[],
     'minimum_interior_coefficient':min(min(r['interior']) for r in cones['cones']),
     'boundary_coefficients':sorted({v for r in cones['cones'] for v in r['boundary'].values()}),
     'five_state_ordering_orbits':math.factorial(10)//math.factorial(5)}
for k in ['3:K3','3:path3','4:K4','4:path4','4:star4','4:cycle4','4:K4_minus_edge']:
    out['named_no_holding'][k]=exact['named'][k]['results'][0]
rows=exact['named']['3:holding_decrease']['results']
out['holding_example']={'before':rows[0]['stationary'],'after':rows[1]['stationary'],
                        'before_float':float(F(rows[0]['stationary'])),
                        'after_float':float(F(rows[1]['stationary'])),
                        'difference':str(F(rows[1]['stationary'])-F(rows[0]['stationary']))}
# Re-evaluate numerical endpoints as exact rational conductances; no floating point
# inequality is trusted in these endpoint checks.
for group in ['K4_support_no_holding','K4_support_with_holding']:
    for k in [0,10,20,30]:
        run=numeric['groups'][group]['runs'][k]
        w=[F(round(v*10**9),10**9) for v in run['weights']]
        h=[F(round(v*10**9),10**9) for v in run['holding']]
        result=inspect(4,w,[h],full=True)[0]
        out['rounded_numerical_endpoints'].append(dict(group=group,run=k,
                 weights=list(map(str,w)),value=result['stationary'],
                 defect=str(F(result['stationary'])-F(11,2))))
# The general formula itself extends to n=5, including holding.
five=[]
for w,h in [([1]*10,[0]*5),([1]*10,[0,1,0,2,0]),
             ([1,0,0,0,1,0,0,1,0,1],[0]*5)]:
    P,q,m,L=chain(5,list(map(F,w)),list(map(F,h)))
    cc=[r[0] for r in augmented_blocks(P)]
    E=stationary(m,cc)
    assert E==alternating(5,L,m)
    N=augmented_blocks(P,True)
    K=[[N[i][j]/m[j] for j in range(5)] for i in range(5)]
    assert all(K[i][j]==K[j][i] and K[i][j]>=0 for i in range(5) for j in range(5))
    five.append(dict(weights=w,holding=h,stationary=str(E)))
out['five_state_formula_examples']=five
out['seconds']=time.monotonic()-start
out['max_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
Path('referee_summary_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
