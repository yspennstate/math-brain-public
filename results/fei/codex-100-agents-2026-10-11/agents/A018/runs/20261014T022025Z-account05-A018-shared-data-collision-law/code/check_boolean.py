from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time,sys,hashlib
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261012T010436Z-account05-A018-shared-data-collision-law/code/check_lead.py'
ns={'__file__':str(OLD),'__name__':'arithmetic_only'}
exec(compile(OLD.read_text(encoding='utf8').split("\nresult={'helper_version'")[0],str(OLD),'exec'),ns)
start=time.perf_counter();checks=0
def ck(x):
 global checks
 checks+=1;assert x;assert time.perf_counter()-start<60
def walsh(v):
 if len(v)==1:return v[:]
 half=len(v)//2;a=walsh(v[:half]);b=walsh(v[half:])
 return [x+y for x,y in zip(a,b)]+[x-y for x,y in zip(a,b)]
def entropy(w):
 L=len(w)
 return ns['ent']([Q(c*c,L*L) for c in w])
def influence(v,w):
 n=(len(v)-1).bit_length();L=len(v);I=Q(0)
 for bit in range(n):
  physical=Q(sum(v[i]!=v[i^(1<<bit)] for i in range(L)),L)
  spectral=Q(sum(c*c for s,c in enumerate(w) if s&(1<<bit)),L*L)
  ck(physical==spectral);I+=physical
 return I
def bits_interval(expr):
 lo,hi=ns['grid'](expr);l2,h2=ns['ln_grid'](2)
 return str(lo/h2),str(hi/l2)
rows=[]
for n1,n2 in ([(4,4)] if '--pilot' in sys.argv else [(a,b) for a in (4,5,6) for b in (4,5,6)]):
 modules=[]
 for n in (n1,n2):
  v=[-1]+[1]*((1<<(n+1))-1);w=walsh(v)
  ck(w==ns['fw'](v));ck(sum(c*c for c in w)==len(v)**2)
  ck(w[0]==len(v)-2 and all(c==-2 for c in w[1:]))
  I=influence(v,w);ck(I==Q(n+1,1<<n))
  modules.append((v,w,entropy(w),I))
 N=1+n1+n2;L=1<<N
 def value(i):
  z=i&1;y1=(i>>1)&((1<<n1)-1);y2=i>>(1+n1)
  return (-1 if z==0 and y1==0 else 1)*(-1 if z==0 and y2==0 else 1)
 v=[value(i) for i in range(L)];w=walsh(v);ck(w==ns['fw'](v));ck(sum(c*c for c in w)==L*L)
 I=influence(v,w);a=Q(1,1<<n1);b=Q(1,1<<n2)
 ck(I==(n1+1)*a+(n2+1)*b-2*a*b)
 ck(sum(v[i]!=v[i^1] for i in range(L))==L*(a+b-2*a*b))
 H=entropy(w);gap=ns['add']((1,H),(-1,modules[0][2]),(-1,modules[1][2]));lo,hi=ns['grid'](gap)
 # Independently reconstruct every actual parent coefficient from branch products.
 c1=walsh([-1]+[1]*((1<<n1)-1));c2=walsh([-1]+[1]*((1<<n2)-1))
 for s,c in enumerate(w):
  selector=s&1;t=(s>>1)&((1<<n1)-1);u=s>>(n1+1)
  expected=c1[t]*c2[u]+(-1 if selector else 1)*(1<<(n1+n2))*int(t==0 and u==0)
  ck(c==expected)
 row={'n1':n1,'n2':n2,'dimension':N,'delta1':str(a),'delta2':str(b),'I_parent':str(I),'I_module_sum':str(modules[0][3]+modules[1][3]),'gap_prime_log':{str(p):str(c) for p,c in gap.items()},'gap_natural_scaled_interval':[str(lo),str(hi)],'scale':str(ns['SCALE']),'gap_bits_interval':bits_interval(gap),'positive_gap':lo>0,'negative_gap':hi<0,'spectrum_histogram':{str(k):v for k,v in Counter(w).items()},'truth_sha256':hashlib.sha256(bytes(int(x<0) for x in v)).hexdigest()}
 rows.append(row)
 (ROOT/'out/BOOLEAN_PARTIAL.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf8')
 if lo>0 and not(ROOT/'out/FIRST_BOOLEAN_WITNESS.json').exists():
  (ROOT/'out/FIRST_BOOLEAN_WITNESS.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf8')
out={'status':'PASS','fixtures':rows,'checks':checks,'positive_gaps':sum(r['positive_gap'] for r in rows),'elapsed_seconds':time.perf_counter()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'arithmetic_helper_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),'claim':'Finite actual Boolean refutation of shared-bit entropy subadditivity if a positive gap is certified; not FEI disproof'}
(ROOT/'out'/('BOOLEAN_PILOT.json' if '--pilot' in sys.argv else 'BOOLEAN_CHECK.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','checks','positive_gaps','elapsed_seconds')}))
