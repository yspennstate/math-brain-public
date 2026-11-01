"""Exact checks for the unweighted Abelian reset construction (P0276).

On small cases (d = 2..5, m = 2 and 4) this enumerates the Cayley graph of (Z_2)^d x Z_m with the basis-times-nonzero
and nonzero-cube generators, checks connectivity, the projected generator identity (cube walk at rate alpha plus
uniform reset at rate beta), every character eigenvalue against the closed form, and the smallest spectral gap. It
also checks the conditional auxiliary total-variation bound by finite convolutions and the cube chi-square formula
(1+r^2)^d - 1 by direct product masses, and rejects deliberately wrong reset-rate and bias-power formulas.
Finite cases check the formulas; the asymptotic argument is in analyses/P0276_unweighted_abelian_cutoff.md.
"""
from fractions import Fraction as F
from collections import Counter
import itertools, json


def main():
 roots=[(1,0),(0,1),(-1,0),(0,-1)]
 cases=[];characters=0;projected_entries=0;bad_rates=0;conditional_cases=0;chi_cases=0
 for d,m in itertools.product(range(2,6),[2,4]):
  N=2**d;S={(1<<i,k) for i in range(d) for k in range(1,m)}|{(x,0) for x in range(1,N)}
  D=len(S);assert D==d*(m-1)+N-1 and (0,0) not in S
  assert all((x,(-k)%m) in S for x,k in S)
  # Actual graph breadth-first traversal verifies connectivity independently.
  seen={(0,0)};queue=[(0,0)]
  for x,k in queue:
   for y,l in S:
    z=(x^y,(k+l)%m)
    if z not in seen:seen.add(z);queue.append(z)
  assert len(seen)==N*m
  alpha=F(d*(m-1),D);beta=F(N,D);theta=F(N-1,D)
  counts=Counter(x for x,k in S)
  for x in range(N):
   for y in range(N):
    actual=F(counts[x^y],D)-(x==y)
    cube=F(1,d) if (x^y).bit_count()==1 else (-1 if x==y else 0)
    assert actual==alpha*cube+beta*(F(1,N)-(x==y))
    projected_entries+=1
  assert F(counts[1],D)!=alpha*F(1,d)+theta*F(1,N);bad_rates+=1
  gaps=[]
  for A,l in itertools.product(range(N),range(m)):
   re=im=0
   for x,k in S:
    sign=(-1)**((A&x).bit_count());rr,ii=roots[((4//m)*l*k)%4]
    re+=sign*rr;im+=sign*ii
   assert im==0
   a=A.bit_count();expected=((d-2*a)*((m-1) if l==0 else -1)+(N-1 if A==0 else -1))
   assert re==expected;characters+=1
   if A or l:gaps.append(F(D-re,D))
  sector_min=min(F(2*(m-1)+N,D),F(d*m,D),F(D-d+1,D))
  assert min(gaps)==sector_min
  cases.append({'d':d,'m':m,'vertices':N*m,'degree':D,'gap':str(min(gaps))})
 # Direct finite convolutions bound the conditional auxiliary error, without
 # assuming independent coordinates before conditioning on the event count.
 for m in [2,3,4,7]:
  law=[F(i==0) for i in range(m)]
  for n in range(1,5):
   law=[sum(law[(j-k)%m] for k in range(1,m))/F(m-1) for j in range(m)]
   tv=sum(abs(p-F(1,m)) for p in law)/2
   assert tv<=F(1,m)
   if n==1:assert tv==F(1,m)
   conditional_cases+=1
 # Enumerate Bernoulli product masses to verify the cube chi-square formula.
 for d,r in itertools.product(range(2,7),[F(1,3),F(2,3)]):
  masses=[((1+r)/2)**(d-x.bit_count())*((1-r)/2)**x.bit_count() for x in range(2**d)]
  actual=sum((p-F(1,2**d))**2/F(1,2**d) for p in masses)
  assert actual==(1+r*r)**d-1
  assert actual!=(1+r)**d-1
  chi_cases+=1

 print(json.dumps({'graph_cases':cases,'characters_checked':characters,'projected_generator_entries_checked':projected_entries,
  'conditional_convolutions_checked':conditional_cases,'cube_chi_square_cases':chi_cases,
  'wrong_reset_rate_controls_rejected':bad_rates,'wrong_bias_power_controls_rejected':chi_cases},indent=2))


if __name__=='__main__':main()
