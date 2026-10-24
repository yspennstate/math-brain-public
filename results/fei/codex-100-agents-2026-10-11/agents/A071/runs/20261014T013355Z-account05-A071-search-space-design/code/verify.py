import hashlib,json,time
from fractions import Fraction as Q
from pathlib import Path
import search as s
start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
def decode_interval(x):return tuple(map(Q,x))
def overlap(x,y):return max(x[0],y[0])<=min(x[1],y[1])
# Place oversized completed records in the explicitly permitted big directory.
big_manifest=[]
for p in list((s.ROOT/'out').glob('*.json')):
 if p.stat().st_size>=20_000_000:
  dest=s.ROOT/'out/big'/p.name;dest.parent.mkdir(exist_ok=True)
  ck(p.resolve().is_relative_to(s.ROOT.resolve()) and dest.resolve().is_relative_to(s.ROOT.resolve()))
  p.rename(dest)
  big_manifest.append({'path':str(dest.relative_to(s.ROOT)),'bytes':dest.stat().st_size,
   'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'regenerate':'python -X utf8 code/search.py'})
s.save('big_manifest.json',big_manifest)
results=s.ROOT/'out/results.json'
if not results.exists():results=s.ROOT/'out/big/results.json'
a=json.loads(results.read_text(encoding='utf-8'));g=a['core'];p=Q(g['p']);v=4*p*(1-p)
source=Path('~/brain_workers/FEI100_20261011/agents/A080/runs/20261014T005622Z-account05-A080-universal-counterexample-standard/out/VALIDATION.json')
b=json.loads(source.read_text(encoding='utf-8'))
for own,external in zip(a['core_trace'],b['records'][:4]):
 z=external['state']
 for k in ('p','d','t','I'):ck(Q(own[k])==Q(z[k]))
 ck(own['n']==z['n'])
 for k in ('H','B'):ck(overlap(decode_interval(own[k]),decode_interval(z[k])))
ck(len(a['core_trace'])==4)
cover=sorted(x for row in a['orbits'] for x in row['members']);ck(cover==list(range(64)))
ck(len(a['orbits'])==10)
uc=[Q(x,64) for x in s.fwht([s.h(x) for x in range(64)])]
out=[]
for case in a['cases']:
 mask=case['mask'];ps=[1-p if mask>>j&1 else p for j in range(6)]
 means=[1-2*x for x in ps];products=[Q(1)]*64
 for T in range(64):
  for j in range(6):
   if T>>j&1:products[T]*=means[j]
 # New coefficient formula: hat_mu(h)(T)=sqrt(v)^|T| sum_(U superset T) hat_uniform(h)(U)*prod_(U\T) m_j.
 sq=[]
 for T in range(64):
  c=sum(uc[U]*products[U^T] for U in range(64) if U&T==T)
  sq.append(c*c*v**T.bit_count())
 _,checksq=s.transform(ps);ck(sq==checksq);ck(sum(sq)==1)
 witness=min(range(6),key=lambda j:Q(case['rows'][j]['E'][1]))
 for j,row in enumerate(case['rows']):
  q=sum(sq[U] for U in range(64) if U>>j&1)/v;ck(q==Q(row['q']))
  inputs=[[sq[U],Q(g['t'])*sq[U|(1<<j)]/v] for U in range(64) if not U>>j&1]
  ck(inputs==[[Q(x),Q(y)] for x,y in row['packets']])
  if mask!=1 and j!=witness:continue
  M=(Q(0),Q(0))
  for U in range(64):
   if not U>>j&1:
    M=s.add(M,s.phi(sq[U],Q(g['t'])*sq[U|(1<<j)]/v))
  R=s.sub(M,s.mul(s.phi(means[j]**2,Q(g['t'])),q))
  ck(R==decode_interval(row['reserve']))
  E=s.mul(s.add(s.mul(decode_interval(g['B']),q),R),1/(q*Q(g['d'])))
  ck(E==decode_interval(row['E']))
 ratios=[decode_interval(r['E']) for r in case['rows']]
 Emin=(min(r[0] for r in ratios),min(r[1] for r in ratios));ck(Emin==decode_interval(case['E_min']))
 qsum=sum(Q(r['q']) for r in case['rows']);ck(qsum==Q(case['sum_q']))
 Cp=decode_interval(case['C_p'])
 # Full terminal entropy is retained and exactly checked algebraically; outer entropy
 # is independently re-enclosed on the best case only, since it is not an erasure-sign premise.
 if mask==1:ck(s.sub(s.entropy(sq),s.mul(s.entropy([v,1-v]),qsum))==Cp)
 ck(s.add(s.mul(decode_interval(g['H']),qsum),Cp)==decode_interval(case['H']))
 ck(Q(case['I'])==qsum*Q(g['I']))
 # Record whichever frozen threshold assertion is actually supported.
 out.append({'mask':mask,'orbit_size':len(next(o['members'] for o in a['orbits'] if o['representative']==mask)),
   'E_bounds':list(map(str,Emin)),'display':list(map(float,Emin)),
   'fails_K':Emin[1]<Q(669,200),'coordinate_E_display':[float(x[0]) for x in ratios],
   'coordinate_q': [r['q'] for r in case['rows']],
   'H_over_I':case['H_over_I'],'C_p':case['C_p']})
 s.save('verification_partial.json',out)
 if time.perf_counter()-start>600:raise RuntimeError('frozen verification cap')
best=(max(Q(r['E_bounds'][0]) for r in out),max(Q(r['E_bounds'][1]) for r in out))
ck(best==decode_interval(a['best_E_enclosure']))
core_E=s.mul(decode_interval(g['B']),1/Q(g['d']))
separator=Q(33483,10000)
separates=best[1]<separator<core_E[0]
one=next(r for r in out if r['mask']==1)
ck(Q(one['E_bounds'][0])>max(Q(r['E_bounds'][1]) for r in out if r['mask']!=1))
one_case=next(r for r in a['cases'] if r['mask']==1)
one_p=Q(one_case['output_p']);one_min=min(one_p,1-one_p)
ck(Q(one['E_bounds'][0])>Q(669,200))
ck(one_min>Q(1,16))
# Exact one-complement bias map, counted directly on the actual gate truth table.
hist=[sum(1 for x in s.NEG if (x^1).bit_count()==k) for k in range(7)]
ck(hist==[1,2,5,2,0,0,0])
coeff=[0]*7
for k,count in enumerate(hist):
 for j in range(7-k):coeff[k+j]+=count*__import__('math').comb(6-k,j)*(-1)**j
sigma=[-c for c in coeff];sigma[0]+=1
ck(sigma==[0,4,-10,18,-19,10,-2])
ck(sum(Q(c)*p**k for k,c in enumerate(sigma))==one_min)
ck(4-Q(10,16)-Q(19,16**3)-Q(2,16**5)>3)
ck(Q(18,16)+Q(10,16**3)<10)
s.save('bias_map.json',{'negative_distance_histogram_about_unit_vertex':hist,
 'minority_polynomial_in_ascending_powers':sigma,'domain':'0<p<=1/16',
 'proved_bounds':'3p<sigma(p)<4p<=1/4',
 'actual_core_p':g['p'],'one_flip_output_minority':str(one_min),
 'caution':'Bias escape only; no all-depth signed-erasure or terminal payment'})
summary={'assertions':checks,'runtime_seconds':time.perf_counter()-start,'core_E':list(map(str,s.mul(decode_interval(g['B']),1/Q(g['d'])))),
 'core_bits':g['n'],'all64_fail_K':all(r['fails_K'] for r in out),'K':'669/200','orbits':out,
 'best_E_bounds':list(map(str,best)),'best_E_display':list(map(float,best)),
 'A080_core_states_independently_matched':4,'coefficient_reconstruction':'uniform Walsh reexpansion matched64 coefficients on all10 orbits exactly',
 'all64_fail_monotone_E':best[1]<core_E[0],
 'separator_K':str(separator),'all64_fail_separator_K_but_core_passes':separates,
 'one_flip_rescues_A080_K':True,'one_flip_escapes_rare_band':True,
 'full_FEI':'OPEN'}
s.save('verification.json',summary)
print(json.dumps({k:v for k,v in summary.items() if k!='orbits'},indent=2))
