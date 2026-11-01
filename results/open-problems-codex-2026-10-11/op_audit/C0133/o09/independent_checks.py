from pathlib import Path
from itertools import product
from fractions import Fraction as F
import json, math
out={}
steps=((1,0),(-1,0),(0,1),(0,-1))
cover=0; front_checks=0; count_checks=0
for dirs in product(range(4),repeat=9):
 path=[(0,0)]
 for k in dirs:
  dx,dy=steps[k]; x,y=path[-1]; path.append((x+dx,y+dy))
 h=[x for x,y in path]
 first={}
 for t,v in enumerate(h): first.setdefault(v,t)
 maxh=max(h)
 for m in range(maxh+1):
  tm=first[m]
  assert all(h[t]<m for t in range(tm)); front_checks+=1
  for L in range(1,maxh-m+1):
   upper=first[m+L]
   visits=[t for t in range(tm,upper) if h[t]==m]
   s=visits[-1]; c=s-tm
   if L>c:
    assert all(h[t]>m for t in range(s+1,upper+1))
    assert all(h[t]<m+L for t in range(tm,s+1))
    assert (path[s][0]-path[tm][0])==0
    cover+=1
 for L in range(1,maxh+1):
  for M in range(maxh-L+1):
   sizes=[]; diam=[]; gaps=[]
   for m in range(M+1):
    tm=first[m]; tu=first[m+L]; vv=[t for t in range(tm,tu) if h[t]==m]
    sizes.append(len(vv)); diam.append(vv[-1]-tm); gaps.append(tu-tm)
   assert sum(sizes)<=first[M+L]
   assert sum(diam)<=sum(gaps)<=L*first[M+L]
   count_checks+=1
out['path_checks']={'planar_paths':4**9,'cover_cases':cover,'fresh_front_checks':front_checks,'deterministic_count_cases':count_checks}
# Exact one-dimensional three-level continuation in a two-type IID field.
# pi = (0,1,0); every stack here is constant, retaining maximal index correlation.
ps=[F(1,10),F(4,5)]
ef=F(0); ewf=F(0); ew=F(0)
for p0,p1,p2 in product(ps,repeat=3):
 w=p0*(1-p1)
 f=p0*p1*p2/(1-p1*(1-p2))
 ef+=f/F(8); ewf+=w*f/F(8); ew+=w/F(8)
 assert 0<=w*f<=f
assert ewf<=ef
out['likelihood']={'unweighted':str(ef),'joint':str(ewf),'prefix':str(ew),'posterior':str(ewf/ew),'posterior_exceeds_fresh':ewf/ew>ef}
# Independent exact checks of earlier finite formulas.
q=F(1,4); a=F(1,8)
out['three_step_probabilities']={'opposite':str(q**3-q*a*a),'fair':str(q**3),'persistent':str(q**3+q*a*a)}
assert (q**3-q*a*a,q**3,q**3+q*a*a)==(F(3,256),F(4,256),F(5,256))
for L in range(2,61):
 u=[F(i,L) for i in range(L+1)]
 assert all(2*u[i]-u[i-1]-u[i+1]==0 for i in range(1,L))
out['harmonic_profiles']='exact identity for every L=2,...,60'
for x in [F(k,20) for k in range(101)]:
 assert float(x*x/2)-math.log(math.cosh(float(x)))>=-1e-14
out['mgf_check']='log(cosh(x)) <= x^2/2 at 101 points on [0,5]; general inequality checked analytically'
Path('independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
