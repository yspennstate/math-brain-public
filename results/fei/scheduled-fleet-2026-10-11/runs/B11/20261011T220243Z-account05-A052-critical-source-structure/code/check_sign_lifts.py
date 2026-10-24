import json,time
from fractions import Fraction as Q
import check_structure as m
start=time.monotonic(); out=[]
for d,c in ((4,3),(5,4)):
    n=d+c; N=1<<n
    v=[-1 if (x&((1<<d)-1)).bit_count()<=1 or x==((1<<d)-1) else 1 for x in range(N)]
    g=m.restricted(v,3,3)
    m.check(sum(x==-1 for x in g)==1)
    p=m.pspec(v); q=m.pspec(g); H=m.entropy(p); h=m.entropy(q); I=m.energy(p); i=m.energy(q)
    m.check(m.fwht(v)==m.direct(v)); m.check(m.fwht(g)==m.direct(g))
    m.check(I==m.edges(v)); m.check(i==m.edges(g))
    gap=m.add(m.scale(h,I),m.scale(H,i),-1)
    m.check(m.nonnegative(gap))
    l,u=m.interval(gap); a,b=m.ln_bound(2)
    lo=l/(I*i*b); hi=u/(I*i*a)
    # Conservative positive rational bit-ratio margin.
    m.check(lo>Q(1,2))
    out.append({'n':n,'fixed_data_bits':'first two = 1','descendant':'one-point sign defect on n-2 coordinates',
                'source_I':str(I),'descendant_I':str(i),'ratio_gap_bits_interval':[str(lo),str(hi)],
                'certified_gap_lower_bound':'1/2'})
result={'status':'PASS','assertions':m.COUNT,'runtime_seconds':time.monotonic()-start,'cases':out}
(m.ROOT/'out'/'SIGN_REPLAY_OUTPUT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
