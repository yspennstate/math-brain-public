import json,time
from fractions import Fraction as Q
import check as h
START=time.perf_counter();COUNT=0
def ck(b):
    global COUNT
    COUNT+=1;assert b;assert time.perf_counter()-START<60
records=[]
for t in [4,5,6]:
    # Core is the first t bits, then shared c, private u, private V(t).
    n=2*t+2;coreN=1<<t;controlN=1<<(t+2)
    core=[-1 if x==0 else 1 for x in range(coreN)]
    ctrl=[-1 if not(z&1) and not(z&~3) else 1 for z in range(controlN)]
    v=[core[x]*ctrl[z] for z in range(controlN) for x in range(coreN)]
    a=h.fwht(v);den=len(v)**2;IZ=h.physical(v,range(t,n));IX=h.physical(v,range(t))
    alpha=Q(sum(a[x+(s<<t)]**2 for s in range(1,controlN) for x in range(coreN)),den)
    # Full positive reference on all nonempty controller subsets, including canceled-u labels.
    R=1;U=2;V=((1<<t)-1)<<2;cells={}
    for s in range(1,controlN):cells.setdefault((bool(s&U),bool(s&V)),[]).append(s)
    ck(len(cells)==4)
    tail_cost={}
    for cell in cells.values():
        mass=Q(sum(a[x+(s<<t)]**2 for s in cell for x in range(coreN)),den)
        tail_cost=h.combine((tail_cost,Q(1)),(h.ns['factors'](4*len(cell)),mass))
    binary=h.combine((h.ns['factors'](alpha.denominator),Q(1)),(h.ns['factors'](alpha.numerator),-alpha),(h.ns['factors'](alpha.denominator-alpha.numerator),-(1-alpha)))
    coreH=h.entropy(h.fwht(core));wholeCE=h.combine((coreH,Q(1)),(binary,Q(1)),(tail_cost,Q(1)))
    actualH=h.entropy(a);ck(h.interval(h.combine((wholeCE,Q(1)),(actualH,Q(-1))))[0]>=0)
    ck(h.interval(wholeCE)[1]<=Q(9)*(IZ+IX))
    ck(IZ==(t+1)*Q(1,1<<t));ck(IX==2*t*Q(1,1<<t))
    records.append({'t':t,'I_Z':str(IZ),'I_X':str(IX),'whole_reference_cost_upper':str(h.interval(wholeCE)[1]),'bound_9I':str(9*(IZ+IX)),'control_alpha':str(alpha),'actual_H_upper':str(h.interval(actualH)[1])})
out={'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'final_reference_exposed_fixtures':records}
(h.ROOT/'out/GUARDS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
