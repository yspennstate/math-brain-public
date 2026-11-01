from pathlib import Path
import json,time,sys,itertools
run=Path(__file__).resolve().parents[1]
helper=run.parent/'20261014T015800Z-fleet05-A062-influence-compensator/code/check_transfer.py'
e={'__file__':str(helper)}
exec(compile(helper.read_text().split("pilot='--pilot'")[0],str(helper),'exec'),e)
F=e['F']; tree=e['tree']; measure=e['measure']; point=e['point']; plus=e['plus']; minus=e['minus']; mul=e['mul']; fmt=e['fmt']; equal=e['equal']; leq=e['leq']
pilot='--pilot' in sys.argv
start=time.perf_counter()
def child(v,i,s): return tuple(v[x] for x in range(len(v)) if (x>>i)&1==s)
def mean(v): return F(sum(v),len(v))
def mismatch(u,v): return F(sum(a!=b for a,b in zip(u,v)),len(u))
def overlap(a,b,k): leq(max(a[0],b[0]),min(a[1],b[1]),k)
u=tuple(-1 if x==0 else 1 for x in range(8))
v=tuple(-1 if x in (0,2) else 1 for x in range(8))
pairs=[('unequal_shared',u,v),('constant_endpoint',u,(1,)*8),('same',u,u),('opposite',u,tuple(-a for a in u)),('independent',tuple(-1 if x&3==0 else 1 for x in range(8)),tuple(1 if x&4 else -1 for x in range(8)))]
seeds=[tuple(1 if mask>>x&1 else -1 for x in range(4)) for mask in range(16)]
if not pilot: seeds += [tuple(-1 if x==0 else 1 for x in range(1<<m)) for m in (3,4)]
roots=strict=boundary=0; rows=[]
for name,u,v in pairs[:1] if pilot else pairs:
 t=mismatch(u,v)
 M=tuple(u[x>>1] if x&1 else v[x>>1] for x in range(16))
 _,HM,IM=measure(M)
 for C in (4,) if pilot else (4,6):
  QM,_,_=tree(M,(1,2,3,0),C)
  for a in seeds:
   m=len(a).bit_length()-1; _,Ha,Ia=measure(a); Qa,_,_=tree(a,tuple(range(m)),C)
   f=tuple(u[x>>(m+1)] if (1 if x>>m&1 else -1)*a[x&((1<<m)-1)]==1 else v[x>>(m+1)] for x in range(1<<(m+4)))
   _,Hf,If=measure(f)
   overlap(Hf,plus(HM,mul(Ha,t)),'entropy_sector_identity_overlap')
   equal(If[:m],[t*d for d in Ia],'actual_seed_influence')
   equal(If[m],t,'actual_tag_influence')
   equal(If[m+1:],[F(du+dv,2) for du,dv in zip(measure(u)[2],measure(v)[2])],'actual_shared_data_influence')
   for j in range(3):
    uc=[child(u,j,s) for s in (0,1)]; vc=[child(v,j,s) for s in (0,1)]
    tc=[mismatch(uc[s],vc[s]) for s in (0,1)]
    equal(t,sum(tc)/2,'actual_disagreement_harmonic')
    df=minus(Hf,mul(plus(measure(child(f,m+1+j,0))[1],measure(child(f,m+1+j,1))[1]),F(1,2)))
    dm=minus(HM,mul(plus(measure(child(M,1+j,0))[1],measure(child(M,1+j,1))[1]),F(1,2)))
    overlap(df,dm,'actual_data_decrement_overlap')
   bound=plus(mul(Qa,t),QM)
   for seedslots in itertools.combinations(range(m+3),m):
    slots=set(seedslots); si=di=0; order=[]
    for j in range(m+3):
     if j in slots: order.append(si); si+=1
     else: order.append(m+1+di); di+=1
    order.append(m)
    q,_,_=tree(f,tuple(order),C)
    if q[1]<=bound[0]: strict+=1; leq(q[1],bound[0],'strict_reserve_certificate')
    else:
     overlap(q,bound,'boundary_compatible_only'); boundary+=1
    roots+=1
   rows.append({'pair':name,'seed':list(a),'C':C,'t':str(t),'Qa':fmt(Qa),'QM':fmt(QM),'bound':fmt(bound)})
   # Clear mixed recursion state between roots: bounded memory, no lost certificates.
   tree.cache_clear(); measure.cache_clear()
# Exact actual versus counterfeit conditional coefficients, independent of log signs.
u,v=pairs[0][1:]; t=mismatch(u,v)
tc=[mismatch(child(u,0,s),child(v,0,s)) for s in (0,1)]
proxy=(1-mean(u)*mean(v))/2
pc=[(1-mean(child(u,0,s))*mean(child(v,0,s)))/2 for s in (0,1)]
equal(t,F(1,8),'fixture_t'); equal(tc,[F(1,4),F(0)],'fixture_children_t')
equal(proxy,F(5,16),'fixture_proxy'); equal(proxy-sum(pc)/2,F(1,16),'fake_release')
a=tuple(-1 if x==0 else 1 for x in range(8))
_,Ha,Ia=measure(a)
ell=minus(minus(Ha,mul(plus(measure(child(a,0,0))[1],measure(child(a,0,1))[1]),F(1,2))),point(4*Ia[0]))
leq(F(1,8),ell[0],'tensor_seed_positive_local_debt')
elapsed=time.perf_counter()-start
assert elapsed<60,elapsed
out={'pilot':pilot,'roots':roots,'strict_interval_dominance':strict,'boundary_compatible_not_interval_proof':boundary,'analytic_bound_source':'DERIVATION.md section2','assertions':sum(e['env']['counts'].values()),'counts':dict(e['env']['counts']),'runtime_seconds':elapsed,'failures':0,'ell':fmt(ell),'fixture':{'t':str(t),'child_t':[str(x) for x in tc],'proxy':str(proxy),'false_release':str(proxy-sum(pc)/2)},'rows':rows}
(run/'out'/('PILOT.json' if pilot else 'EXACT_SHARED.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
