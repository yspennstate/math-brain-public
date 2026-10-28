from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import runpy,json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
m=runpy.run_path(str(R/'code/census.py'),run_name='A074_helpers')
add,sub,scale,decode,encode=(m[k] for k in ('add','sub','scale','decode','encode'))
def ck(x):
 global checks
 checks+=1
 if not x:raise AssertionError(checks)
def ln(z):
 n=48;lo=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(n)),Q(0))
 return lo,lo+2*z**(2*n+1)/(Q(2*n+1)*(1-z*z))
LN2=ln(Q(1,3))
@lru_cache(None)
def logbound(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;y=Q(p,2**k);a,b=ln((y-1)/(y+1));c,d=LN2
 return Q(k)+a/d,Q(k)+b/c
def interval(f):
 lo=hi=Q(0)
 for p,c in f.items():
  a,b=logbound(p)
  if c<0:a,b=b,a
  lo+=c*a;hi+=c*b
 return lo,hi
keys=set();distinct={};equal=raw_equal=positive=zero=0;maxform={2:Q(-4),3:Q(3)}
coverage=json.loads((R/'out/main_COVERAGE.json').read_text(encoding='utf-8'))
multiplicities={tuple(v['counts']):v['multiplicity'] for v in coverage['profiles']}
ck(coverage['core_query_rows']==768);ck(sum(multiplicities.values())==768)
for k in range(16):
 rows=json.loads((R/f'out/main_CHUNK_{k:02}.json').read_text(encoding='utf-8'))
 ck(len(rows)==560)
 for row in rows:
  h=row['outer_mask'];p=tuple(row['profile']);key=(h,p)
  ck(16*k<=h<16*k+16);ck(key not in keys);keys.add(key);ck(sum(p)==4 and min(p)>=0)
  d=Q(row['influence']);f=decode(row['drift']);gap=decode(row['gap'])
  ck(gap==sub(scale(maxform,d),f))
  kk=tuple(sorted(gap.items()));distinct[kk]=gap
  if d:
   positive+=1
   if not gap:equal+=1;raw_equal+=3*multiplicities[p]
  else:zero+=1;ck(not f)
ck(len(keys)==8960);ck(positive==7200);ck(zero==1760);ck(equal>0)
for f in distinct.values():
 if f:ck(interval(f)[0]>0)
 else:ck(interval(f)==(0,0))
# Opposite arithmetic path: no prime-product comparison in this audit.
for d in (Q(0),Q(1,8),Q(3,8)):
 forged=add(scale(maxform,d),{2:Q(1)})
 ck(interval(sub(scale(maxform,d),forged))[1]<0)
# Literal source witness: direct character summation rather than bitset spectra.
source=Path('agents/A072/runs/20261027T083832Z-account04-A072-exact-walsh-engine')
source_witness=json.loads((source/'out/HALF_RATE_COUNTEREXAMPLE.json').read_text(encoding='utf-8'))
mask=16579836;t=tuple(-1 if mask>>x&1 else 1 for x in range(32))
w=tuple(sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(32))
ck(list(w)==source_witness['Walsh']);ck(sum(a*a for a in w)==1024)
def H_direct(t):
 N=len(t);w=[sum(v*(-1 if (x&s).bit_count()%2 else 1) for x,v in enumerate(t)) for s in range(N)]
 hist={}
 for a in w:hist[a*a]=hist.get(a*a,0)+1
 return m['entropy'](tuple(sorted(hist.items())),N)
H=H_direct(t);ck(H=={2:Q(6),3:Q(-27,16)})
g=tuple(-1 if 3>>x&1 else 1 for x in range(8));h=tuple(-1 if 7>>z&1 else 1 for z in range(8))
reconstructed=tuple(h[((x>>3)&1)+2*((x>>4)&1)+4*(g[x&7]<0)] for x in range(32))
ck(reconstructed==t)
def restrict(t,i,b):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(b<<i)] for x in range(len(t)//2))
children=[restrict(t,1,b) for b in (0,1)];Hg=H_direct(g);ck(Hg=={2:Q(2)})
Hgchildren=[H_direct(restrict(g,1,b)) for b in (0,1)];ck(Hgchildren==[{},{}])
q=Q(3,4);C=sub(H,scale(Hg,q));Cchildren=[sub(H_direct(v),scale(Hgchildren[b],q)) for b,v in enumerate(children)]
drift=sub(scale(add(*Cchildren),Q(1,2)),C);d=Q(sum(t[x]!=t[x^2] for x in range(32)),32)
ck(d==Q(3,8));ck(drift=={2:Q(-3,2),3:Q(9,8)});ck(scale(drift,1/d)==maxform)
ck(interval(sub(maxform,{2:Q(1,2)}))[0]>0);ck(9>8)
lo,hi=interval(maxform)
result={'status':'PASS','rows':len(keys),'positive_influence_rows':positive,'zero_influence_rows':zero,'equality_representatives':equal,'raw_equality_query_rows_all_selected_inputs':raw_equal,'distinct_gap_profiles':len(distinct),'checks':checks,'seconds':time.monotonic()-start,'maximum':encode(maxform),'maximum_bounds':[str(lo),str(hi)],'witness_truth_mask':mask,'witness_influence':str(d),'witness_drift':encode(drift),'altered_controls_rejected':3,'method':'direct literal character witness; all saved gap forms via directed rational positive-series logarithms, independent of census prime-power signs'}
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
