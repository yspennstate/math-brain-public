import sys,json,time
from pathlib import Path
from fractions import Fraction as Q
sys.dont_write_bytecode=True
import arithmetic as M
import rows as T
R=Path(__file__).resolve().parents[1]
spec={'helper_version':'direct-character-pair-replay-v1','family':'one actual five-bit Boolean fixture, one explicit nonBoolean four-bit real relaxation','domain':'fixed fixtures only','case_count':2,'symmetry':'none','arithmetic':'direct character sums/Fraction/formal prime-log and exact integer powers','memory_estimate_MB':30,'max_runtime_seconds':55}
(R/'out/INDEPENDENT_SPEC.json').write_text(json.dumps(spec,indent=2)+'\n')
start=time.perf_counter();checks=0
def ck(x):
    global checks
    checks+=1;assert x,checks
def direct(v):
    return {s:Q(sum(c*(-1 if (s&x).bit_count()%2 else 1) for x,c in enumerate(v)),len(v)) for s in range(len(v))}
def H(v):return M.H({s:c*c for s,c in direct(v).items() if c})
c=[6,1,2,1];v=tuple(-1 if x>>2<c[x&3] else 1 for x in range(32));a=direct(v)
ck(a=={s:M.fwht(v).get(s,Q(0)) for s in range(32)})
def child(i,b):return tuple(v[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(16))
h=H(v);hi=M.add(*[(Q(1,2),H(child(0,b))) for b in (0,1)]);hj=M.add(*[(Q(1,2),H(child(1,b))) for b in (0,1)])
hab=M.add(*[(Q(1,4),H(tuple(v[(y<<2)|b] for y in range(8)))) for b in range(4)])
omega=M.add((1,hi),(1,hj),(-1,h),(-1,hab))
ck(omega==((2,Q(1,2)),(3,Q(9,32)),(5,Q(-25,32))))
I=sum(c*c*((s&3).bit_count()) for s,c in a.items());ck(I==Q(5,8))
edgeI=Q(sum(v[x]!=v[x^(1<<i)] for x in range(32) for i in (0,1)),32);ck(edgeI==I)
ck(2**29*3**18<5**25);ck(2**56*3**9>5**25);ck(8>3)
# All four relaxed outside rows; their signs physically permute outcomes.
base=(3,-3,-2,-2);om,d=T.row(base)
for t in range(4):
    row=tuple(x*(-1 if (s&t).bit_count()%2 else 1) for s,x in enumerate(base))
    ck(T.row(row)==(om,d))
    for x in range(4):
        # Direct inverse outside transform leaves y=s only.
        for y in range(4):
            numerator=sum(row_s*(-1 if ((s&x).bit_count()+(tt&y).bit_count())%2 else 1) for s in range(4) for tt in range(4) for row_s in [base[s]*(-1 if (s&tt).bit_count()%2 else 1)])
            ck(numerator==4*base[y]*(-1 if (x&y).bit_count()%2 else 1))
    ck(sum(Q(4*z*z,26) for z in base)/4==1)
ck(all(Q(4*z*z,26)!=1 for z in base))
ck(T.interval(M.add((1,om),(1,((2,2*d),))))[1]<0)
out={'status':'PASS','checks':checks,'seconds':time.perf_counter()-start,'representations':'direct characters; physical edges; integer-power strict signs; exact relaxed inverse transform','nonBoolean_scope_guard':True}
(R/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
