from pathlib import Path
from collections import defaultdict
from math import comb
from fractions import Fraction as F
import json, sympy as S,time
from joint_boundary import exact_joint,admissible,orbit,score

# Independent exhaustive graph enumeration for R=1 (8 random rim edges).
marks=[(-1,0),(0,1),(1,0),(0,-1)];vs=[(x,y) for x in [-1,0,1] for y in [-1,0,1] if (x,y)!=(0,0)];idx={v:i for i,v in enumerate(vs)}
ed=[(idx[(x,y)],idx[(x+dx,y+dy)]) for x,y in vs for dx,dy in [(1,0),(0,1)] if (x+dx,y+dy) in idx];assert len(ed)==8
brute={}
for mask in range(256):
 rt=list(range(8))
 def find(i):
  while rt[i]!=i:i=rt[i]
  return i
 for j,(a,b) in enumerate(ed):
  if mask>>j&1:rt[find(a)]=find(b)
 d={};tokens=tuple(2*d.setdefault(find(idx[v]),len(d))+1 for v in marks)
 row=brute.setdefault(tokens,[0]*9);row[mask.bit_count()]+=1
r1=json.loads(Path('joint_R1.json').read_text());assert brute=={tuple(st['tokens']):st['weight'] for st in r1['states']}

# Reverse edge-order radius-two polynomial distribution (all 80 final states).
r2=json.loads(Path('joint_R2.json').read_text());rv=exact_joint(2,poly=True,reverse=True)
assert {tuple(s['tokens']):s['weight'] for s in rv['states']}=={tuple(s['tokens']):s['weight'] for s in r2['states']}

# Independently enumerate D4 and the restored star, producing degree-four
# UNNORMALIZED Bernstein coefficients of the averaged signed functional.
allparts=[]
def gen(a):
 if len(a)==4:allparts.append(tuple(a));return
 for z in range(max(a,default=-1)+2):gen(a+[z])
gen([]);allparts=[a for a in allparts if orbit(a)!='cross']
def canonical(a):
 d={};return tuple(d.setdefault(v,len(d)) for v in a)
symmetries=[tuple((rot+sgn*i)%4 for i in range(4)) for rot in range(4) for sgn in [-1,1]]
star={}
for part in allparts:
 coeff=[F(0)]*5
 for perm in symmetries:
  a=canonical(tuple(part[perm[i]] for i in range(4)))
  for mask in range(16):
   root=list(range(5))
   def find(i):
    while root[i]!=i:i=root[i]
    return i
   for i in range(4):
    for j in range(i):
     if a[i]==a[j]:root[find(i)]=find(j)
    if mask>>i&1:root[find(i)]=find(4)
   d=int(find(0)==find(4))-int(find(0)==find(2));coeff[mask.bit_count()]+=F(d,8)
 star[part]=coeff
 for p in [F(1,7),F(1,2),F(6,7)]:assert sum(c*p**k*(1-p)**(4-k) for k,c in enumerate(coeff))==score(part,p)

# Independent integer convolution: min each UNNORMALIZED star coefficient
# over the allowed coarsenings, then convolve with interior open-edge counts.
DD=[F(0)]*41
for st in r2['states']:
 tok=st['tokens'];part=tuple(v>>1 for v in tok);hit=tuple(v&1 for v in tok);poss=admissible(part,hit)
 low=[min(star[a][j] for a in poss) for j in range(5)]
 for i,c in enumerate(st['weight']):
  for j,v in enumerate(low):DD[i+j]+=4*c*v
assert all(v.denominator==1 for v in DD);DD=list(map(int,DD));saved=json.loads(Path('joint_signed_integer_certificate.json').read_text());assert DD==saved['counts']
assert DD[0]==0 and DD[35:]==[0]*6
assert all(DD[k]>=4*comb(33,k-1) for k in range(1,35))
# Thus 4L >= 4 p q^6 (p+q)^33 =4p q^6.

# Sanity: the signed functional at R=1 can fail, proving the bound is not
# a hidden assumption that every exterior automatically helps.
assert F(r1['evaluation']['lower'])==F(-1,16)
report={'R1_exhaustive_configurations':256,'R1_all_partition_and_hit_counts':'PASS','R2_reverse_order_80_state_polynomial_counts':'PASS','D4_8_by_16_direct_star_enumeration':'PASS','independent_integer_convolution':'PASS','all_34_reduced_coefficients_ge_4_binomial_33':'PASS','radius_one_lower_bound':str(F(-1,16))}
Path('joint_verification.json').write_text(json.dumps(report,indent=2),encoding='utf8');print(report)
