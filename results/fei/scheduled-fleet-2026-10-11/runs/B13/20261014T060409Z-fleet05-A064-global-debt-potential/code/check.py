from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,hashlib,time,sys
R=Path(__file__).resolve().parents[1]; START=time.perf_counter(); COUNT=0
PILOT='--pilot' in sys.argv; CAP=58 if PILOT else 595
START_MASK=int(next((arg.split('=')[1] for arg in sys.argv if arg.startswith('--start-mask=')),'0'))
STOP_MASK=int(next((arg.split('=')[1] for arg in sys.argv if arg.startswith('--stop-mask=')),'256'))
GRID=2**44
def ck(b,s):
 global COUNT
 COUNT+=1
 if not b: raise AssertionError((COUNT,s))
def iv(x): return (F(x),F(x))
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[1],-a[0])
def sub(a,b): return add(a,neg(b))
def scale(a,s): return (a[0]*s,a[1]*s) if s>=0 else (a[1]*s,a[0]*s)
def mul(a,b):
 q=[a[i]*b[j] for i in (0,1) for j in (0,1)];return min(q),max(q)
def div(a,b):
 assert b[0]>0
 return mul(a,(1/b[1],1/b[0]))
def total(a):
 z=iv(0)
 for t in a:z=add(z,t)
 return z
@lru_cache(None)
def lnf(x):
 z=(x-1)/(x+1); z2=z*z; t=z; a=F(0)
 for j in range(24):a+=2*t/F(2*j+1);t*=z2
 return a,a+2*t/(49*(1-z2))
LN2=lnf(F(2))
@lru_cache(None)
def logpoint(x):
 assert x>0
 k=x.numerator.bit_length()-x.denominator.bit_length()
 while x<F(2)**k:k-=1
 while x>=F(2)**(k+1):k+=1
 y=x/F(2)**k; lo,hi=lnf(y)
 return F(k)+lo/LN2[1],F(k)+hi/LN2[0]
def log(a):
 assert a[0]>0
 # Enlarge to a dyadic grid BEFORE series evaluation; avoid huge bisection denominators.
 low=F((a[0]*GRID).__floor__(),GRID); high=F((a[1]*GRID).__ceil__(),GRID)
 assert low>0
 return logpoint(low)[0],logpoint(high)[1]
def entropy_prob(a):
 if a[1]==0:return iv(0)
 assert a[0]>0
 return neg(mul(a,log(a)))
def H(p):return total(entropy_prob(iv(x)) for x in p if x)
def KL(p,q):return total(scale(sub(log(iv(x)),log(y)),x) for x,y in zip(p,q) if x)
def fw(v):
 a=list(v);s=1
 while s<len(a):
  for j in range(0,len(a),2*s):
   for k in range(j,j+s):x,y=a[k],a[k+s];a[k],a[k+s]=x+y,x-y
  s*=2
 return a
def law(v):return tuple(F(a*a,len(v)**2) for a in fw(v))
def marg(p):
 return tuple(sum((x for j,x in enumerate(p) if (j>>i)&1),F(0)) for i in range(len(p).bit_length()-1))
def productlaw(ds):
 return tuple(__import__('functools').reduce(lambda x,y:x*y,(d if (s>>i)&1 else 1-d for i,d in enumerate(ds)),F(1)) for s in range(2**len(ds)))
def child(v,i,b):return tuple(v[x] for x in range(len(v)) if (x>>i)&1==b)
def profile(v):
 p=law(v); ds=marg(p); m=F(sum(v),len(v)); coreH=H(p)
 n=len(v).bit_length()-1
 ed=tuple(F(sum(v[x]!=v[x^(1<<i)] for x in range(len(v))),len(v)) for i in range(n))
 ck(ds==ed,'independent edge versus Walsh influences')
 return p,ds,coreH,m
def TC(p):
 ds=marg(p)
 return sub(H(productlaw(ds)),H(p))
def cond_entropy(p,keepmask):
 n=len(p).bit_length()-1; grouped={}
 for s,x in enumerate(p):grouped[s&keepmask]=grouped.get(s&keepmask,F(0))+x
 return sub(H(p),H(tuple(grouped.values())))
def erase(p,i):
 return tuple(p[t]+p[t|(1<<i)] for t in range(len(p)) if not (t>>i)&1)
def kernel_transition(v,i,q):
 p=law(v); q_e=[]; p_e=[]; kernels=[]
 children=[child(v,i,b) for b in (0,1)]; ps=[law(c) for c in children]
 for t in range(len(p)):
  if not (t>>i)&1:
   p_e.append(p[t]+p[t|(1<<i)]);q_e.append(add(q[t],q[t|(1<<i)]))
 for j,x in enumerate(p_e):kernels.append([ps[b][j]/(2*x) if x else F(1,2) for b in (0,1)])
 reach=[total(scale(z,k[b]) for z,k in zip(q_e,kernels)) for b in (0,1)]
 ck(reach[0][0]>0 and reach[1][0]>0,'reference branch supported')
 qs=[[div(scale(z,k[b]),reach[b]) for z,k in zip(q_e,kernels)] for b in (0,1)]
 O=scale(neg(log(scale(mul(reach[0],reach[1]),4))),F(1,2))
 E=sub(KL(p,q),KL(tuple(p_e),q_e))
 terminalKL=scale(add(KL(ps[0],qs[0]),KL(ps[1],qs[1])),F(1,2))
 residual=sub(KL(p,q),add(E,add(O,terminalKL)))
 ck(residual[0]<=0<=residual[1],'analytic common-kernel KL chain numerical enclosure')
 refonly=total(z for x,z in zip(p_e,q_e) if not x)
 return children,ps,qs,O,E,refonly
def occupancy(p):
 ds=marg(p); z=1-p[0]; rr=[d/z for d in ds]
 def poly(c):
  t=F(1)
  for r in rr:t*=1-c*r
  return 1-c-t
 lo=F(1,2)
 for _ in range(16):
  if poly(lo)>0:break
  lo/=2
 else:raise ArithmeticError('no positive frozen initial bracket')
 hi=F(1);ck(poly(hi)<0,'positive occupancy root upper sign')
 for _ in range(36):
  mid=(lo+hi)/2
  value=poly(mid)
  if value==0:lo=hi=mid;break
  if value>0:lo=mid
  else:hi=mid
 ck((lo==hi and poly(lo)==0) or (poly(lo)>0 and poly(hi)<0),'positive root exact endpoint signs or exact rational root')
 c=(lo,hi); theta=[scale(c,r) for r in rr]; out=[]
 for s in range(len(p)):
  if not s:out.append(iv(p[0]));continue
  term=iv(z)
  for i,t in enumerate(theta):term=mul(term,t if (s>>i)&1 else sub(iv(1),t))
  out.append(div(term,c))
 # Source matched-marginal max entropy is proved analytically; interval enclosure checks it.
 norm=total(out);ck(norm[0]<=1<=norm[1],'completed occupancy normalized')
 for i,d in enumerate(ds):
  t=total(x for s,x in enumerate(out) if (s>>i)&1);ck(t[0]<=d<=t[1],'completed original marginals')
 return out,c
def compose(core):
 return tuple(-1 if not (z&1) and (z&2) else core[t] if (z&1) and (z&4) else 1 for t in range(len(core)) for z in range(8))
def plus(a):return max(F(0),a[1])
def interval_json(a):return [str(a[0]),str(a[1])]
def outgrid(a):
 g=10**12;return [str(F((a[0]*g).__floor__(),g)),str(F((a[1]*g).__ceil__(),g))]
masks=[0,255,1,254,7,248,15,240] if PILOT else list(range(START_MASK,STOP_MASK))
records=[]; maxcharge=F(0); minremaining=None; refonlycount=0; rawcases=0
for mask in masks:
 v=tuple(1 if (mask>>j)&1 else -1 for j in range(8)); full=compose(v); p,ds,h,m=profile(full)
 Q,c=occupancy(p); A=KL(p,Q)
 ac,ap,aq,Oa,Ea,za=kernel_transition(full,1,Q)
 tcs=[TC(x) for x in ap]
 Da=sub(add(Oa,scale(add(*tcs),F(1,2))),A)
 slack=[]
 for f in ac:
  pp,dd,hh,mm=profile(f);slack.append(sub(iv(4*sum(dd,F(0))),hh))
 meanS=scale(add(*slack),F(1,2));ck(meanS[0]>0,'actual certified mean child surplus')
 ck(all(s[0]>=0 for s in slack),'both actual child surplus certificates including constant zero')
 first=plus(Da)
 for i in range(3):
  spends=[]; terminalh=[]; afterS=[]; rowmass=[]; conditionals=[]
  # a is erased, so remaining physical data positions start at2.
  for b in (0,1):
   f=ac[b]; prodq=[iv(x) for x in productlaw(marg(ap[b]))]
   fc,pc,qc,Oo,Ee,Z=kernel_transition(f,i+2,prodq)
   meanTC=scale(add(TC(pc[0]),TC(pc[1])),F(1,2))
   Di=sub(add(Oo,meanTC),tcs[b]);spends.append(plus(Di));rowmass.append(Z)
   # Bayes-to-product mismatch includes every retained data row, including source-zero rows.
   sigma=sub(meanTC,scale(add(KL(pc[0],qc[0]),KL(pc[1],qc[1])),F(1,2)))
   ident=sub(Di,sub(sigma,Ee));ck(ident[0]<=0<=ident[1],'signed conversion sigma-E including outcome normalization')
   for ff,pp,qq in zip(fc,pc,qc):
    ppp,ddd,hhh,mmm=profile(ff);terminalh.append(hhh);afterS.append(sub(iv(4*sum(ddd,F(0))),hhh))
    # Retained core-frequency versus control-frequency conditional reference KL.
    keep=3; groupsP={}; groupsQ={}
    for s,x in enumerate(pp):groupsP[s&keep]=groupsP.get(s&keep,F(0))+x;groupsQ[s&keep]=add(groupsQ.get(s&keep,iv(0)),qq[s])
    KLquot=KL(tuple(groupsP[k] for k in sorted(groupsP)),tuple(groupsQ[k] for k in sorted(groupsP)))
    cond=sub(KL(pp,qq),KLquot);conditionals.append(cond)
   if Z[1]>0:refonlycount+=1
  spend=first+sum(spends,F(0))/2
  remaining=sub(meanS,iv(spend))
  # Frozen half-budget target, with both complete terminal laws retained.
  halfmargin=sub(scale(meanS,F(1,2)),iv(spend))
  ck(halfmargin[0]>0,'two conversions use less than half SAME original mean S4')
  meanleafS=scale(total(afterS),F(1,4))
  ck(meanleafS[0]>=0,'all actual terminal S4 retained')
  rec={'core_mask':mask,'data_coordinate':i,'root_c':outgrid(c),'initial_conversion_debit':outgrid(Da),'mean_child_S4':outgrid(meanS),'total_positive_withdrawal_upper':str(F((spend*10**12).__ceil__(),10**12)),'half_budget_margin':outgrid(halfmargin),'remaining_same_child_budget':outgrid(remaining),'reference_only_mass':list(map(outgrid,rowmass)),'mean_terminal_H':outgrid(scale(total(terminalh),F(1,4))),'mean_terminal_S4':outgrid(meanleafS),'conditional_reference_KL':list(map(outgrid,conditionals))}
  records.append(rec); maxcharge=max(maxcharge,spend);minremaining=remaining[0] if minremaining is None else min(minremaining,remaining[0]);rawcases+=1
 if time.perf_counter()-START>CAP:raise TimeoutError('Frozen run ceiling')
 (R/'out/CHECKPOINT.json').write_text(json.dumps({'status':'IN_PROGRESS','core_masks_finished':len(records)//3,'query_cases':rawcases,'assertions':COUNT,'elapsed_seconds':time.perf_counter()-START},indent=2)+'\n')
 logpoint.cache_clear();lnf.cache_clear()
result={'status':'PASS','pilot':PILOT,'actual_core_masks':len(masks),'query_cases':rawcases,'exact_assertions':COUNT,'reference_only_data_nodes':refonlycount,'max_total_positive_withdrawal_upper':str(F((maxcharge*10**12).__ceil__(),10**12)),'minimum_remaining_same_child_budget_lower':str(F((minremaining*10**12).__floor__(),10**12)),'runtime_seconds':time.perf_counter()-START,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'maximum_dimension':6,'records':records}
(R/'out'/('PILOT.json' if PILOT else 'VALIDATION_SUFFIX.json' if START_MASK else 'VALIDATION_PREFIX_REPLAY.json' if STOP_MASK<256 else 'VALIDATION.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))

if START_MASK and STOP_MASK==256:
 prefix=json.loads((R/'out/PREFIX_CERTIFICATE.json').read_text())
 assert prefix['actual_core_masks']==START_MASK
 merged={k:v for k,v in result.items() if k!='records'}
 merged.update({'actual_core_masks':256,'query_cases':768,'exact_assertions':prefix['exact_assertions']+COUNT,'runtime_seconds':prefix['runtime_checkpoint_seconds']+result['runtime_seconds'],'reference_only_data_nodes':'Prefix total unrecorded; suffix observed '+str(refonlycount),'split_receipts':['PREFIX_CERTIFICATE.json','VALIDATION_SUFFIX.json'],'prefix_helper_sha256':prefix['helper_sha256'],'prefix_individual_margin_records':'not persisted at runtime stop; byte-pinned exact assertion receipt retained','suffix_first_mask':START_MASK})
 (R/'out/VALIDATION.json').write_text(json.dumps(merged,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'merged_status':'PASS','actual_core_masks':256,'query_cases':768,'exact_assertions':merged['exact_assertions']},indent=2))
