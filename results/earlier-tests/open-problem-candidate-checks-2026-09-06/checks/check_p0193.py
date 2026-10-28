"""Exact rational checks for the compact multiplicative initial law (P0193).

For the two-atom initial law with atoms 1/10 and 10 (half mass each) and minus-cosine parameter c in {0, 1/10, 1/2,
9/10, 1}, this checks at r in {1/1000, 1/10, 1, 10, 1000} that the averaged kernel z/(1 + z^2 + 2cz), z = r xi, crosses the level 1/10
four times (signs -,+,-,+,-), the closed form 5r(a+b)/(ab), the quartic identity (1 - 10 I) ab = 100 r^2 Q(r + 1/r),
the symmetry r -> 1/r, and the signs of Q at 2 and 101/10. Two deliberately wrong variants are rejected: the kernel
sum without the half masses, and the law collapsed to a single atom at 1.
Finite cases check the formulas; the argument for every c in [0, 1] is in
analyses/P0193_compact_multiplicative_log_unimodality.md.
"""
from fractions import Fraction as F
import json


def kernel(r,xi,c):
 z=r*xi
 return z/(1+z*z+2*c*z)
def integral(r,c):return (kernel(r,F(1,10),c)+kernel(r,F(10),c))/2
def q(y,c):return y*y+(F(101,5)*c-F(101,2))*y+F(9801,100)+4*c*c-20*c
def horner(r,c):
 coeff=[F(100),2020*c-5050,10001+400*c*c-2000*c,2020*c-5050,F(100)]
 ans=F(0)
 for a in coeff:ans=ans*r+a
 return ans


def main():
 cs=[F(0),F(1,10),F(1,2),F(9,10),F(1)]
 rs=[F(1,1000),F(1,10),F(1),F(10),F(1000)]
 rows=[];identities=0;bad_mass_rejected=0;collapsed_rejected=0
 for c in cs:
  signs=[-1 if integral(r,c)<F(1,10) else 1 for r in rs]
  assert signs==[-1,1,-1,1,-1]
  assert q(F(2),c)==F(101,100)+F(102,5)*c+4*c*c>0
  assert q(F(101,10),c)==-F(31003,100)+F(9201,50)*c+4*c*c<0
  for r in rs:
   a=r*r+20*c*r+100;b=100*r*r+20*c*r+1
   assert integral(r,c)==5*r*(a+b)/(a*b)
   assert (1-10*integral(r,c))*a*b==horner(r,c)
   assert horner(r,c)==100*r*r*q(r+1/r,c)
   assert integral(r,c)==integral(1/r,c)
   identities+=1
   wrong=kernel(r,F(1,10),c)+kernel(r,F(10),c)
   assert (1-10*wrong)*a*b!=horner(r,c)
   bad_mass_rejected+=1
  collapsed=[-1 if kernel(r,F(1),c)<F(1,10) else 1 for r in rs]
  assert collapsed!=[-1,1,-1,1,-1]
  collapsed_rejected+=1
  rows.append({'minus_cos_R':str(c),'four_crossing_signs':signs,'Q_at_2':str(q(F(2),c)),'Q_at_101_over_10':str(q(F(101,10),c))})
 assert F(10,101)<F(1,10)<F(1,8)
 assert q(F(101,10),F(1))==-F(12201,100)
 assert kernel(F(1,1000),F(1,10),F(0))/2+kernel(F(1,1000),F(10),F(0))/2<F(1,10)
 print(json.dumps({'exact_identity_cases':identities,'omitted_half_mass_controls_rejected':bad_mass_rejected,
  'collapsed_atom_controls_rejected':collapsed_rejected,'cases':rows},indent=2))


if __name__=='__main__':main()
