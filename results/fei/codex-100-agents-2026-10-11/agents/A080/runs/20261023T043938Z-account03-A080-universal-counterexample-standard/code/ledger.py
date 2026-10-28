"""Read exact spectra, validate full Bellman envelope and carried accounts."""
import certify as E
from certify import *
from functools import lru_cache
import importlib.util
START=time.perf_counter()
def load(n):return json.loads((R/'out'/n).read_text(encoding='utf-8'))
def repl(ts,j,t):return ts[:j]+(t,)+ts[j+1:]
E.setup()
D={}
for i in range(12):
 for z in load(f'BLOCK_{i:02d}_STATES.json'):
  ts=tuple(z['state']);ck(ts not in D);D[ts]=z
ck(len(D)==20736);root=(ROOT,)*4
@lru_cache(None)
def hull(ts,allowed):
 s=D[ts]['S'];lo=max(0,-s[1]);hi=max(0,-s[0])
 for j in allowed:
  for coord,a,b in ACT[ts[j]]:
   z=mean(hull(repl(ts,j,a),allowed),hull(repl(ts,j,b),allowed));lo=max(lo,z[0]);hi=max(hi,z[1])
 return lo,hi
allaxes=(0,1,2,3);rroot=hull(root,allaxes);A=(-D[root]['S'][1],-D[root]['S'][0]);rootm=[]
for j in allaxes:
 for coord,a,b in ACT[ROOT]:
  avg=mean(hull(repl(root,j,a),allaxes),hull(repl(root,j,b),allaxes));margin=A[0]-avg[1];ck(margin>0);rootm.append({'core_original':j+2,'coordinate':coord,'margin_lower_grid':margin})
rows=0;negative_control=None
for ts,z in D.items():
 v=hull(ts,allaxes);ck(v[0]<=v[1]);ck(v[1]>=max(0,-z['S'][0]))
 for j in allaxes:
  for coord,a,b in ACT[ts[j]]:
   c0,c1=repl(ts,j,a),repl(ts,j,b);u,w=hull(c0,allaxes),hull(c1,allaxes);ck(2*v[1]>=u[1]+w[1])
   d=F(z['I'])-(F(D[c0]['I'])+F(D[c1]['I']))/2;ck(d>=0);rows+=1
   stopupper=max(0,-z['S'][0]);kidstoplower=(max(0,-D[c0]['S'][1])+max(0,-D[c1]['S'][1]))//2
   if kidstoplower>stopupper and (negative_control is None or kidstoplower-stopupper>negative_control['extra_lower_grid']):
    negative_control={'state':ts,'types':[T[x] for x in ts],'core_original':j+2,'coordinate':coord,'children':[c0,c1],'parent_S':z['S'],'child_S':[D[c0]['S'],D[c1]['S']],'extra_lower_grid':kidstoplower-stopupper,'physical_influence':str(d),'scope':'Greedy reset to current negative slack cannot pay this actual full-child row; not a FEI disproof.'}
for i in range(12):
 save(f'ENVELOPE_{i:02d}.json',[{'state':list(ts),'rho_upper_grid':hull(ts,allaxes)[1],'exact_hull_interval_grid':hull(ts,allaxes)} for ts in D if ts[0]==i])
ck(negative_control is not None);save('GREEDY_RESET_CONTROL.json',negative_control)
# Minimum carried source credit under the actual pair-envelope rule.
prefix=[];both=[];allm=[];pairsummary=[]
for pair in combinations(range(4),2):
 states=[tuple(a if j==pair[0] else b if j==pair[1] else ROOT for j in allaxes) for a,b in product(range(12),repeat=2)]
 states.sort(key=lambda ts:sum(T[x][1] for x in ts),reverse=True);credit={root:A};paths={root:[]}
 for ts in states:
  ck(ts in credit);ac=credit[ts];required=hull(ts,allaxes)
  if ts!=root:
   margin=ac[0]-required[1];ck(margin>0);allm.append(margin)
   rec={'pair_original':[j+2 for j in pair],'state':ts,'credit_min_interval_grid':ac,'full_required_interval_grid':required,'margin_lower_grid':margin,'path':paths[ts]};prefix.append(rec)
   if all(ts[j]!=ROOT for j in pair):both.append(rec)
  for j in pair:
   for coord,a,b in ACT[ts[j]]:
    kids=[repl(ts,j,a),repl(ts,j,b)];m=mean(*(hull(k,pair) for k in kids))
    for ans,k in enumerate(kids):
     proposed=plus(hull(k,pair),sub(ac,m))
     if k not in credit:credit[k]=proposed;paths[k]=paths[ts]+[(j+2,coord,ans)]
     else:
      old=credit[k];credit[k]=(min(old[0],proposed[0]),min(old[1],proposed[1]))
      if proposed[0]<old[0]:paths[k]=paths[ts]+[(j+2,coord,ans)]
 pairsummary.append({'pair_original':[j+2 for j in pair],'states':len(states),'root_interval':hull(root,pair),'min_nonroot_margin_grid':min(x['margin_lower_grid'] for x in prefix if x['pair_original']==[j+2 for j in pair])})
save('CARRIED_PREFIXES.json',prefix)
# Independently review unchanged source spectra, hulls and actual saved rows.
source=Path('agents/A084/runs/20261023T035136Z-account03-A084-continuum-parameters')
src=json.loads((source/'out/JOINT_CASES.json').read_text(encoding='utf-8'));sourcecomparisons=0
def prime(p):return plus(*(scale(E.log(F(int(k))),F(v)) for k,v in p.items()))
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def padd(*ps):
 z={}
 for p in ps:
  for k,v in p.items():z[k]=z.get(k,F(0))+v
 return {k:v for k,v in z.items() if v}
def pmul(p,c):return {k:v*c for k,v in p.items() if v*c}
def unpack(p):return {int(k):F(v) for k,v in p.items() if F(v)}
@lru_cache(None)
def factor(n):
 ck(n>0);d={};p=2
 while p*p<=n:
  while n%p==0:d[p]=d.get(p,0)+1;n//=p
  p=3 if p==2 else p+2
 if n>1:d[n]=d.get(n,0)+1
 return d
def plog(x):
 ck(x>0);return padd({k:F(v) for k,v in factor(x.numerator).items()},{k:F(-v) for k,v in factor(x.denominator).items()})
def pell(x):return pmul(plog(x),-x) if x else {}
def pcmp(a,b):
 q=padd(a,pmul(b,-1))
 if not q:return 0
 v=prime(q)
 if v[0]>0:return 1
 if v[1]<0:return -1
 raise ArithmeticError('Unresolved exact prime-log comparison')
COREH=[padd(*(pell(a*a) for a in walsh(truth(t)))) for t in T]
@lru_cache(None)
def pspectrum(ts):
 cs=[E.C[x] for x in ts];mus=[c['mu'] for c in cs];vs=[c['var'] for c in cs];hs={};qs=[F(0)]*4
 for B in range(16):
  v=F(0)
  for U in range(16):
   if U&B!=B:continue
   a=W[U]
   for j in range(4):
    if (U^B)>>j&1:a*=mus[j]
   v+=a
  p=v*v
  for j in range(4):
   if B>>j&1:p*=vs[j]
  if p:
   lp=pmul(plog(abs(v)),2)
   for j in range(4):
    if B>>j&1:lp=padd(lp,plog(vs[j]));qs[j]+=p/vs[j]
   hs=padd(hs,pmul(lp,-p))
 for j in range(4):hs=padd(hs,pmul(padd(COREH[ts[j]],pmul(padd(pell(vs[j]),pell(1-vs[j])),-1)),qs[j]))
 return padd({2:4*F(D[ts]['I'])},pmul(hs,-1))
for item in src:
 pair=tuple(j-2 for j in item['pair_original'])
 PR={}
 for z in item['states_certificate']:
  st=[ROOT]*4
  for j,t in zip(pair,z['truths']):st[j]=[truth(t0) for t0 in T].index(tuple(t))
  PR[tuple(st)]=unpack(z['R'])
 for z in item['states_certificate']:
  ts=[ROOT]*4
  for j,t in zip(pair,z['truths']):ts[j]=[truth(t0) for t0 in T].index(tuple(t))
  ts=tuple(ts);ck(unpack(z['S'])==pspectrum(ts));ck(overlap(prime(z['S']),D[ts]['S']));ck(overlap(prime(z['R']),hull(ts,pair)))
  opts=[{},pmul(pspectrum(ts),-1)]
  for j in pair:
   for coord,a,b in ACT[ts[j]]:opts.append(pmul(padd(PR[repl(ts,j,a)],PR[repl(ts,j,b)]),F(1,2)))
  ck(all(pcmp(PR[ts],q)>=0 for q in opts));ck(any(PR[ts]==q for q in opts));sourcecomparisons+=1
 for row in item['rows']:
  ts=[ROOT]*4
  for j,t in zip(pair,row['state']):ts[j]=[truth(t0) for t0 in T].index(tuple(t))
  ts=tuple(ts);j=pair[row['side']];coord=row['coordinate'];raw=truth(T[ts[j]])
  kids=[repl(ts,j,[truth(t0) for t0 in T].index(canon(child(raw,coord,b)))) for b in range(2)]
  rr=hull(ts,pair);m=mean(*(hull(k,pair) for k in kids));ck(unpack(row['parent_required_credit'])==PR[ts]);ck(overlap(prime(row['parent_required_credit']),rr))
  pm=pmul(padd(*(PR[k] for k in kids)),F(1,2));spare=padd(PR[ts],pmul(pm,-1))
  for b,k in enumerate(kids):
   ac=plus(hull(k,pair),sub(rr,m));dc=plus(D[k]['S'],ac)
   pa=padd(PR[k],spare);ck(unpack(row['child_credit'][b])==pa);ck(unpack(row['child_debit'][b])==padd(pspectrum(k),pa))
   ck(overlap(prime(row['child_credit'][b]),ac));ck(overlap(prime(row['child_debit'][b]),dc))
  ck(row['new_outside_flow']=='0');sourcecomparisons+=1
save('REVIEW.json',{'verdict':'HOLDS_AT_SUBSTATEMENT_SCOPE','source':str(source),'scope':'All432 full S/R states and2520 actual two-core allocation rows, independently reconstructed; generic finite Bellman and label transport rederived. Earlier original source-prefix ancestry and donor reach bookings are not independently reviewed.','source_comparisons':sourcecomparisons,'source_spectrum_hull_implementation_executed':False})
# Separate 12-bit full truth table boundary, including physical edges.
ts=tuple(T.index(('A',3)) if j<2 else T.index(('L',3)) for j in range(4));tabs=[truth(T[x]) for x in ts]
flat=tuple(K[sum((tabs[j][(x>>(3*j))&7]<0)<<j for j in allaxes)] for x in range(4096));w=walsh(flat)
ck(sum(a*a for a in w)==1);wi=walsh(w);ck(all(4096*wi[x]==flat[x] for x in range(4096)))
I=F(0)
for j in range(12):
 d=F(sum(flat[x]!=flat[x^(1<<j)] for x in range(4096)),4096);ck(d==sum(a*a for s,a in enumerate(w) if s>>j&1));I+=d
ck(I==F(D[ts]['I']));hh=entropy([x*x for x in w]);ck(overlap(hh,D[ts]['H']))
save('FLAT12.json',{'state':ts,'table_sha256':hashlib.sha256(bytes(x+1 for x in flat)).hexdigest(),'dimension':12,'I':str(I),'H_grid':hh,'walsh_parseval_inverse_edges':'PASS'})
# Arithmetic adversary: independent prior Fraction-series path.
p=R.parent/'20261022T234750Z-account03-A080-universal-counterexample-standard/code/exact.py';spec=importlib.util.spec_from_file_location('prior_exact',p);prior=importlib.util.module_from_spec(spec);spec.loader.exec_module(prior)
mass=[F(i,64) for i in range(1,65)]+[F(1,1<<k) for k in [1,16,64,128,256]]+[1-F(1,1<<k) for k in [16,64,128]]
for x in mass:
 q=E.ell(x);piv=prior.ell(x);ck(max(F(q[0],G),piv[0])<=min(F(q[1],G),piv[1]))
ck(sum(truth(('A',1))[x]**2!=1 for x in range(2))==0);ck(E.C[T.index(('A',1))]['I']==1)
ck(time.perf_counter()-START<120)
result={'verdict':'PASS','complete_boolean_profiles':len(D),'canonical_query_rows':rows,'root_credit_grid':A,'root_stop_dominance_margin_lower_grid':min(x['margin_lower_grid'] for x in rootm),'root_rows':rootm,'carried_nonroot_prefixes':len(prefix),'carried_both_cores_touched':len(both),'all_nonroot_margin_lower_grid':min(allm),'both_touched_margin_lower_grid':min(x['margin_lower_grid'] for x in both),'pairs':pairsummary,'review_source_comparisons':sourcecomparisons,'independent_log_controls':len(mass),'assertions':E.CHECKS,'seconds':time.perf_counter()-START,'new_credit':'ZERO','full_fei':'OPEN'}
save('LEDGER_VALIDATION.json',result);print(json.dumps(result),flush=True)
