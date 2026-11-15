"""Independent Walsh evaluation, census audit, and saved summaries."""
import csv, json, math
from pathlib import Path
import numpy as np

def wht(f):
 a=np.asarray(f,dtype=np.int64).copy();N=a.size
 for h in (1<<i for i in range(N.bit_length()-1)):
  z=a.reshape(-1,2,h);left=z[:,0,:].copy();right=z[:,1,:].copy()
  z[:,0,:]=left+right;z[:,1,:]=left-right
 return a

def phi(p,q):
 p=np.asarray(p,dtype=float);q=np.asarray(q,dtype=float);s=p+q
 z=np.zeros_like(s)
 for v in (p,q):
  m=v>0;z[m]-=v[m]*np.log2(v[m]/s[m])
 return z

def evaluate(f,validate=True):
 f=np.asarray(f,dtype=np.int64);N=f.size;n=N.bit_length()-1;a=wht(f);mu=(a.astype(float)/N)**2
 assert int(a@a)==N*N
 inf=[];er=[];w2=[];idx=np.arange(N);wt=np.zeros(N,dtype=np.uint8)
 for i in range(n):wt+=(idx>>i&1).astype(np.uint8)
 for i in range(n):
  p=mu.reshape(-1,2,1<<i)[:,0,:].ravel();q=mu.reshape(-1,2,1<<i)[:,1,:].ravel()
  delta=float(q.sum());inf.append(delta);er.append(float(phi(p,q).sum()));w2.append(float(mu[((idx>>i)&1==1)&(wt==2)].sum()))
  if validate:
   z=f.reshape(-1,2,1<<i);assert np.all(z[:,0,:]<=z[:,1,:]);assert abs(delta-np.mean(z[:,0,:]!=z[:,1,:]))<1e-12
   assert abs(delta-abs(a[1<<i]/N))<1e-12
 H=float(-(mu[mu>0]*np.log2(mu[mu>0])).sum());I=sum(inf)
 return dict(n=n,H=H,I=I,sumE=sum(er),minratio=min((e/d for e,d in zip(er,inf) if d),default=0),HI=H/I if I else 0,EI=sum(er)/I if I else 0,inf=inf,erasure=er,w2=w2,mean=float(a[0]/N))

def table_from_hex(s,n):
 v=int(s,16);return np.array([1 if v>>x&1 else -1 for x in range(1<<n)],dtype=np.int64)
def minterms(f):
 n=len(f).bit_length()-1;out=[]
 for x in np.flatnonzero(np.asarray(f)>0):
  x=int(x)
  if all(f[x^(1<<i)]<0 for i in range(n) if x>>i&1):out.append(x)
 return out

def audit():
 summary={};maxerror=0;counts=[];checks=0
 for n in range(1,7):
  rows=list(csv.DictReader(open(f'census_n{n}.csv')));N=1<<n
  # Direct character matrix, independent of the butterfly implementation.
  chars=np.array([[(-1)**((s&x).bit_count()) for x in range(N)] for s in range(N)],dtype=np.int64)
  for r in rows:
   f=table_from_hex(r['truth_hex'],n);a=chars@f;assert np.array_equal(a,wht(f));s=evaluate(f)
   assert minterms(f)==[int(t) for t in r['minterms'].split('|')] if s['I'] else True
   for key in ['H','I','sumE','minratio']:
    maxerror=max(maxerror,abs(s[key]-float(r[key])));assert abs(s[key]-float(r[key]))<2e-12
   for key in ['inf','erasure','w2']:
    if s['I']:assert np.max(np.abs(np.array(s[key])-np.array([float(x) for x in r[key].split('|')])))<2e-12
   if s['I']:
    assert sum(d*d for d in s['inf'])<=1+1e-12
    assert s['sumE']<=s['H']+1e-12
   checks+=1
  nonconstant=[r for r in rows if float(r['I'])>0]
  for r in nonconstant:
   r['HI']=float(r['H'])/float(r['I']);r['EI']=float(r['sumE'])/float(r['I'])
  summary[n]={key:max(nonconstant,key=lambda r:float(r[key])) for key in ['minratio','HI','EI','rule_maxInf','rule_minInf','rule_shortest','rule_minW2','rule_maxW2','rule_term_clause']}
  counts.append(dict(n=n,classes=len(rows),labelled=sum(int(r['orbit']) for r in rows)))
 json.dump(summary,open('census_summary.json','w'),indent=2)
 result=dict(checks=checks,maxerror=maxerror,counts=counts,method='direct integer character matrix versus integer butterfly; direct edge counts; minterm reconstruction; Parseval; Han; monotone singleton identity; sum squares influences')
 json.dump(result,open('audit.json','w'),indent=2);print(json.dumps(result,indent=2))
 with open('RESULTS.md','a') as out:
  out.write('\n## Exhaustive monotone census, independently audited\n\nCommands: `clang++ -O3 -std=c++17 census.cpp -o census; nice -n 10 ./census > census.log`; `OPENBLAS_NUM_THREADS=1 nice -n 10 python3 analysis.py > audit.log`. Integer Walsh coefficients are exact; logarithms use double precision. Constants and irrelevant coordinates are excluded from ratios. Counts include constants and unused variables.\n\n| n | labelled functions | permutation classes | max min E/Inf | max H/I | max sum E/I |\n|---|---:|---:|---:|---:|---:|\n')
  for c in counts:
   n=c['n'];r=summary[n];out.write(f"| {n} | {c['labelled']} | {c['classes']} | {float(r['minratio']['minratio']):.12f} | {r['HI']['HI']:.12f} | {r['EI']['EI']:.12f} |\n")
  out.write('\nEvery class and its orbit size, truth-table hex, integer-mask DNF, influence, erasure, and coordinate-rule outcomes are saved in `census_n*.csv`. The audit recomputed all representatives by direct character matrices and by butterfly transforms.\n\nAt n=6, the good-coordinate maximizer is `MAJ3(AND(x1,x2), AND(x3,x4), AND(x5,x6))` up to permutation or monotone duality. Its saved mask terms are 15, 54, 57 (complementary to three disjoint pairs), and all coordinate influences equal 0.1875. H/I is maximized by AND6 (and its dual), while sum E/I has a different maximizer. See `census_summary.json` for complete witnesses.\n\nCoordinate-rule ties are resolved adversarially. The term/clause rule chooses the best spectral ratio within the intersection of the union of shortest minterms and the union of shortest zero-certificates; it is a restricted spectral oracle, not a rule from simple combinatorial data alone.\n\n| rule | worst selected E/Inf on six-variable census | DNF term masks of witness |\n|---|---:|---|\n')
  for k,v in summary[6].items():
   if k.startswith('rule'):out.write(f"| {k} | {float(v[k]):.12f} | {v['minterms']} |\n")
  out.write('\nThe proposed score Inf_i² / mu({i}) is identically one on relevant monotone coordinates; its worst tied outcome is the smallest-influence-rule maximum, because E_i/Inf_i <= h2(Inf_i)/Inf_i does not force this equality, so this last identification still requires a direct all-coordinate maximum check. Private singleton mass divided by influence is exactly influence.\n')
if __name__=='__main__':audit()
