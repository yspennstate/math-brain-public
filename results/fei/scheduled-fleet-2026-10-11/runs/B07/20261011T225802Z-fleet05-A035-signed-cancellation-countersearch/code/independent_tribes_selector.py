from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1];start=time.perf_counter()
# Independent logarithm implementation, directly on rational probabilities.
def ln(q):
 exponent=0
 while q<1:q*=2;exponent-=1
 while q>=2:q/=2;exponent+=1
 def unit(q):
  z=(q-1)/(q+1);terms=32
  partial=sum((z**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))*2
  return partial,partial+2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
 lo,hi=unit(q);two=unit(Q(2))
 if exponent>=0:return lo+exponent*two[0],hi+exponent*two[1]
 return lo+exponent*two[1],hi+exponent*two[0]
ln2=ln(Q(2))
def negative_log2(p):
 a,b=ln(p)
 # ln(p)<=0; interval division reverses the denominator endpoints.
 return -b/ln2[1],-a/ln2[0]
def spectrum(w,m):
 q=Q(1,2**w);r=1-q;atoms=[((1-2*r**m)**2,1)]
 atoms += [(4*q**(2*t)*r**(2*(m-t)),comb(m,t)*(2**w-1)**t) for t in range(1,m+1)]
 assert sum(p*c for p,c in atoms)==1
 Hlo=Hhi=Q(0)
 for p,c in atoms:
  if p:
   lo,hi=negative_log2(p);Hlo+=p*c*lo;Hhi+=p*c*hi
 I=2*w*m*q*r**(m-1)
 return atoms,(Hlo,Hhi),I
atoms,H,I=spectrum(2,8);t=32
F_I=1+t*I/2;gap=[t*h/2 for h in H];margin=[h-4*F_I for h in gap]
assert I==Q(2187,2048) and margin[0]>Q(1)
seed_interval=[Q(4623,1000),Q(4624,1000)]
assert seed_interval[0]<H[0]<=H[1]<seed_interval[1]
a,b,j=spectrum(2,3);assert a==[(Q(25,1024),1),(Q(81,1024),9),(Q(9,1024),27),(Q(1,1024),27)] and j==Q(27,16)
assert 3**32<2**53
Hinf=negative_log2(max(p for p,c in a));assert Hinf[0]>2*j
def grid(pair):
 scale=10**12
 return [str(Q(pair[0].numerator*scale//pair[0].denominator,scale)),str(Q(-((-pair[1].numerator*scale)//pair[1].denominator),scale))]
out=dict(helper_version='A035-independent-tribes-selector-v1',runtime_seconds=time.perf_counter()-start,
 seed=dict(w=2,m=8,I=str(I),H_interval=grid(H),atoms=[[str(p),c] for p,c in atoms]),
 gap4_counterexample=dict(dimension=514,copies=t,definition='g=y*product of 32 independent width-2/eight-tribe seeds; F=1 if z=+1, g if z=-1',I=str(F_I),Hinf='2',gap_interval=grid(gap),gap_minus_4I_interval=grid(margin)),
 FMEI2_counterexample=dict(w=2,m=3,I=str(j),Hinf_interval=grid(Hinf),integer_certificate={'left':str(3**32),'right':str(2**53),'inequality':'left<right'}),
 independent_seed_entropy_enclosure=[str(x) for x in seed_interval],
 limitations='Refutes constants 4 and 2 of two precise helpers; neither all-constant helper nor FEI is refuted. Independent code by same author, not independent reviewer acceptance.')
(ROOT/'out'/'independent_tribes_selector.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
