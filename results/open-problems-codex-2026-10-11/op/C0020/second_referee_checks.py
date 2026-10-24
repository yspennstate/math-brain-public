from fractions import Fraction as Q
from pathlib import Path
import json
R=Path(__file__).resolve().parent

# Verify the claimed corridor formula on all completions of the explicit 4x3 state.
known=425;unknown=4095^known;required=3158
coords=[(x,y) for y in range(3) for x in range(4)]
adj=[[j for j in range(12) if
 (coords[j][0]-coords[i][0],coords[j][1]-coords[i][1]) in
 [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]] for i in range(12)]
def cross(m):
    seen=set();stack=[i for i in [0,4,8] if m&(1<<i)]
    while stack:
        i=stack.pop()
        if i in seen:continue
        seen.add(i)
        if i in [3,7,11]:return True
        stack.extend(j for j in adj[i] if m&(1<<j) and j not in seen)
    return False
s=unknown;checked=positive=0
while True:
    assert cross(s)==(s&required==required)
    checked+=1;positive+=cross(s)
    if not s:break
    s=(s-1)&unknown
assert checked==128 and positive==2 and required.bit_count()==6

# Exhaustively evaluate forced depth-first greedy paths for small tribes examples.
rows=[]
for k,m in [(2,4),(3,4),(4,2)]:
    n=k*m;total=0
    for word in range(1<<n):
        depth=0;success=False
        for block in range(m):
            for j in range(k):
                depth+=1
                if not (word>>(k*block+j))&1:break
            else:
                success=True
                break
        total+=depth
        assert success==any(all((word>>(k*b+j))&1 for j in range(k)) for b in range(m))
    q=Q(1,2**k);r=(1-q)**m
    formula=2*(1-q)*(1-r)/q
    assert Q(total,1<<n)==formula
    rows.append({'k':k,'m':m,'inputs':1<<n,'exact_greedy_cost':str(formula)})
family=[]
for k in range(1,11):
    m=2**k;q=Q(1,m);r=(1-q)**m
    v=r*(1-r);I=2*k*(1-q)**(m-1);H=I*I/(4*v)
    c=2*(1-q)*(1-r)/q
    assert Q(1,4)<=r<Q(1,2) and v>=Q(3,16)
    assert H<=Q(16,3)*k*k and c>=m*r
    family.append({'k':k,'m':m,'C_greedy_over_H_float_for_display_only':float(c/H)})
result={'corridor_completions':checked,'corridor_positive_inputs':positive,
 'required_AND_sites':[i for i in range(12) if required&(1<<i)],
 'irrelevant_unknown_sites':[i for i in range(12) if (unknown^required)&(1<<i)],
 'exact_small_tribes_checks':rows,'symbolic_family_checks':family}
(R/'second_referee_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result))
