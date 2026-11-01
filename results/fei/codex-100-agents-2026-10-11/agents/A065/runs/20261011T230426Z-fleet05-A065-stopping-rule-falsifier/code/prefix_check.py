import check as c
from fractions import Fraction as F
from pathlib import Path
import json,time
start=time.monotonic(); rows=[]; coded=[]
for a in (1,2,3):
    N=1<<a; hlo=hhi=0; influence=F(0)
    for data in range(1<<N):
        t=bytes((data>>j)&1 for j in range(N))
        h,inf=c.stats(t); hlo+=h[0];hhi+=h[1]
        influence+=F(2*sum(inf),N)
    eH=(hlo//(1<<N),(hhi+(1<<N)-1)//(1<<N))
    c.check(eH[1]<=a*c.SCALE)
    c.check(influence/(1<<N)==F(a,2))
    t,groups=c.addressing(a)
    c.check(c.stats(t)[0]==(2*a*c.SCALE,2*a*c.SCALE))
    c.check(F(2*sum(c.stats(t)[1]),len(t))==1+F(a,2))
    data_budget=F(2*sum(c.stats(t)[1][a:]),len(t))
    c.check(data_budget==1)
    rows.append({'a':a,'terminal_assignments':1<<N,'E_H_scaled':eH,'E_I_exact':str(F(a,2)),'queried_data_budget_exact':str(data_budget),'expected_prefix_D_scaled':(2*a*c.SCALE-eH[1],2*a*c.SCALE-eH[0]),'unpaid_C4_scaled':(2*a*c.SCALE-eH[1]-4*c.SCALE,2*a*c.SCALE-eH[0]-4*c.SCALE)})
    c.stats.cache_clear();c.children.cache_clear()
for a in (1,2):
    N=1<<a; n=2*a+N
    t=bytes((v>>(2*a+((v&((1<<a)-1))^((v>>a)&((1<<a)-1)))))&1 for v in range(1<<n))
    h,inf=c.stats(t)
    c.check(h==(2*a*c.SCALE,2*a*c.SCALE))
    c.check(F(2*sum(inf),len(t))==1+a)
    for z in range(1<<a):
        child=bytes(t[x | (z<<a) | (y<<(2*a))] for y in range(1<<N) for x in range(1<<a))
        ch,ci=c.stats(child)
        c.check(ch==h)
        c.check(F(2*sum(ci),len(child))==1+F(a,2))
    coded.append({'a':a,'dimension':n,'H_exact':2*a,'I_exact':1+a,'mask_queried_budget_exact':str(F(a,2)),'all_mask_children_H_exact':2*a,'all_mask_children_I_exact':str(1+F(a,2)),'mask_prefix_D_exact':0})
out={'scale':str(c.SCALE),'prefix_cases':rows,'coded_plateaux':coded,'assertions':c.ASSERTIONS,'elapsed_seconds':time.monotonic()-start}
c.check(out['elapsed_seconds']<60)
(c.ROOT/'out'/'PREFIX_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
