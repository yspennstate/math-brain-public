"""Certify monotone census rankings with outward-rounded logarithms and integer sums.

Every Phi/eta interval is rounded outward onto a common 10^-40 grid.
All subsequent additions, influence divisions, minima and ranking comparisons
use Python integers/Fraction. No binary64 number participates in a verdict.
"""
import csv,json,collections,time,os,resource
from fractions import Fraction
import mpmath as mp
from analysis import wht,table_from_hex
mp.iv.dps=70;S=10**40;start=time.time()
def gridfloor(t):
 sign,man,exponent,_=t;num=(-man if sign else man)*S
 return num<<exponent if exponent>=0 else num//(1<<(-exponent))
def bounds(v):
 lo,hi=v._mpi_
 # ceil(x)=-floor(-x), with the exact binary endpoint tuple.
 sign,man,exponent,bc=hi
 neg=(1-sign,man,exponent,bc)
 return gridfloor(lo),-gridfloor(neg)
def out(f):return format(float(f),'.17g')
results=[]
for n in range(1,7):
 N=1<<n;ln2=mp.iv.log(2);eta=[];tab={}
 for v in range(0,N+1,2):
  p=mp.iv.mpf(v*v)/(N*N)
  eta.append(bounds(p*mp.iv.log(1/p)/ln2) if v else (0,0))
  for w in range(v,N+1,2):
   q=mp.iv.mpf(w*w)/(N*N)
   val=(p*mp.iv.log((p+q)/p)/ln2 if v else mp.iv.mpf(0))+(q*mp.iv.log((p+q)/q)/ln2 if w else mp.iv.mpf(0))
   tab[(v,w)]=bounds(val)
 records=[]
 for r in csv.DictReader(open(f'census_n{n}.csv')):
  if not float(r['I']):continue
  a=list(map(int,wht(table_from_hex(r['truth_hex'],n))));hh=[0,0];ec=[0,0];ds=[];ers=[];coordfp=[];totalpairs=collections.Counter()
  for v in a:
   lo,hi=eta[abs(v)//2];hh[0]+=lo;hh[1]+=hi
  for i in range(n):
   d=sum(a[t]*a[t] for t in range(N) if t>>i&1);ds.append(d);ee=[0,0];pairs=collections.Counter()
   for t in range(N):
    if t>>i&1:continue
    v,w=sorted((abs(a[t]),abs(a[t|(1<<i)])));lo,hi=tab[v,w];ee[0]+=lo;ee[1]+=hi;pairs[(v,w)]+=1
   ec[0]+=ee[0];ec[1]+=ee[1];totalpairs.update(pairs)
   if d:
    ers.append((Fraction(ee[0]*N*N,S*d),Fraction(ee[1]*N*N,S*d)))
    coordfp.append((d,tuple(sorted(pairs.items()))))
  I=sum(ds)
  intervals={'minratio':(min(e[0] for e in ers),min(e[1] for e in ers)),'HI':(Fraction(hh[0]*N*N,S*I),Fraction(hh[1]*N*N,S*I)),'EI':(Fraction(ec[0]*N*N,S*I),Fraction(ec[1]*N*N,S*I))}
  fingerprints={'minratio':tuple(sorted(coordfp)),'HI':(I,tuple(sorted(collections.Counter(map(abs,a)).items()))),'EI':(I,tuple(sorted(totalpairs.items())))}
  records.append((r['truth_hex'],intervals,fingerprints))
 fields={}
 for field in ['minratio','HI','EI']:
  top=max(x[1][field][0] for x in records);possible=[x for x in records if x[1][field][1]>=top]
  # All surviving ties have exactly the same dyadic formulas for each objective.
  assert len({x[2][field] for x in possible})==1,(n,field,'unresolved')
  other=[x[1][field][1] for x in records if x[1][field][1]<top]
  lower=min(x[1][field][0] for x in possible);upper=max(x[1][field][1] for x in possible)
  assert lower<=upper
  fields[field]=dict(extremizers=[x[0] for x in possible],lower_exact=str(lower),upper_exact=str(upper),interval_width_exact=str(upper-lower),nonmax_gap_lower_exact=str(lower-max(other)) if other else None,lower_display=out(lower),upper_display=out(upper))
 results.append(dict(n=n,nonconstant_classes=len(records),fields=fields));print('certified',n,{k:v['extremizers'] for k,v in fields.items()},flush=True)
json.dump(dict(method=__doc__,iv_dps=70,grid_scale=str(S),results=results,elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1),open('interval_census.json','w'),indent=2)
