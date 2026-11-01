"""One actual exterior exposure, old debit, and full two-query terminals."""
from fractions import Fraction as Q
import json,time
import density as d
import exact as c

start=time.perf_counter();rows=[]
for m in [4,6,8,10,12]:
 N=1<<m;p=Q(1,N)
 b=[(-1)**sum(((x>>j)&1)*((x>>(j+1))&1) for j in range(0,m,2)) for x in range(N)]
 g=b.copy();g[0]=-1
 rare=b+g;literal=[1]*N+[-1]*N;root=literal+rare
 dx=Q(sum(a!=bb for a,bb in zip(literal,rare)),2*N)
 d.check(dx==(1-p)/2);d.check((1+p)/2>=Q(1,2))
 Hroot,Hrare,Hb,Hg=map(d.H,[root,rare,b,g])
 old=c.add(Hroot,c.neg(c.times(Hrare,Q(1,2))))
 d.check(old[1]<c.times(c.ln(Q(2)),Q(2))[0])
 tax=c.times(c.ln(1/p),p/2)
 remaining=c.add(c.times(c.ln(Q(2)),6*dx),c.neg(old),c.neg(tax))
 target=c.times(c.ln(Q(2)),Q(7,30)*dx)
 d.check(remaining[0]>target[1])
 Dz=c.add(Hrare,c.neg(c.times(c.add(Hb,Hg),Q(1,2))))
 full=c.add(Hroot,c.neg(c.times(c.add(Hb,Hg),Q(1,4))))
 d.close(full,c.add(old,c.times(Dz,Q(1,2))))
 rhs=c.times(c.ln(Q(2)),6*dx+10*p)
 d.check(full[1]<rhs[0])
 rows.append({'m':m,'root_density':str((1+p)/2),'rare_child_density':str(p),'source_query_influence':str(dx),'original_fine_R':0,'old_actual_decrement':c.serial(old),'weighted_descendant_density_tax':c.serial(tax),'source_bank':str(6*dx),'remaining_after_old_debit_and_tax':c.serial(remaining),'strict_remaining_lower':str(Q(7,30)*dx),'actual_final_terminal_entropy':c.serial(c.times(c.add(Hb,Hg),Q(1,4)))})
elapsed=time.perf_counter()-start;d.check(elapsed<55)
(d.ROOT/'out/CHECK_bridge.json').write_text(json.dumps({'status':'PASS','assertions':d.CHECKS,'seconds':elapsed,'rows':rows,'bank_never_renewed':True,'both_actual_terminals_retained':True},indent=2),encoding='utf-8')
print(json.dumps({'mode':'bridge','status':'PASS','assertions':d.CHECKS,'seconds':elapsed,'remaining_ratios':[r['remaining_after_old_debit_and_tax']['display'] for r in rows]}))
