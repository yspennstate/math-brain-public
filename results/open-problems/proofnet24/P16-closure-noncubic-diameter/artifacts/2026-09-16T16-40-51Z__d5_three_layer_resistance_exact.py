#!/usr/bin/env python3
from fractions import Fraction

D=5
S_MAX=14
TARGET=Fraction(16,3)
CANDIDATE=Fraction(4,1)

best=None
mins=[]
feasible=0
shorter=0

# Three cyclic layers, positive sizes s_i, positive inter-layer edge counts e_i.
# Necessary conditions for a simple D-regular realization:
#  * e_i <= s_i s_{i+1} and <= D min(s_i,s_{i+1});
#  * internal degree-sum I_i=D s_i-e_{i-1}-e_i is even and lies in [0,s_i(s_i-1)].
# These are deliberately only necessary conditions, so minimizing over them is a relaxation.
# The electrical/homogenized coefficient is C=M/R with M=sum s_i, R=sum 1/e_i.
for s0 in range(1,S_MAX+1):
  for s1 in range(1,S_MAX+1):
    for s2 in range(1,S_MAX+1):
      ss=(s0,s1,s2)
      M=sum(ss)
      caps=(min(s0*s1,D*s0,D*s1),
            min(s1*s2,D*s1,D*s2),
            min(s2*s0,D*s2,D*s0))
      for e0 in range(1,caps[0]+1):
        for e1 in range(1,caps[1]+1):
          I1=D*s1-e0-e1
          if I1<0 or I1>s1*(s1-1) or I1%2: continue
          for e2 in range(1,caps[2]+1):
            I0=D*s0-e2-e0
            I2=D*s2-e1-e2
            if I0<0 or I0>s0*(s0-1) or I0%2: continue
            if I2<0 or I2>s2*(s2-1) or I2%2: continue
            feasible += 1
            if M<=6: continue
            shorter += 1
            R=Fraction(1,e0)+Fraction(1,e1)+Fraction(1,e2)
            C=Fraction(M,1)/R
            rec=(C,ss,(e0,e1,e2),(I0,I1,I2))
            if best is None or C<best[0]:
              best=rec
              mins=[rec]
            elif C==best[0]:
              mins.append(rec)

assert best is not None
assert best[0]==TARGET, best
# If some layer size is >=15 then M>=17, while R<=3 since every e_i>=1,
# hence C=M/R>=17/3>16/3. Thus S_MAX=14 plus this tail bound is exhaustive.
assert Fraction(17,3)>TARGET
# Candidate maximum-diameter cell profile (1,1,4), e=(1,4,4): C=4.
M0=6; R0=Fraction(1,1)+Fraction(1,4)+Fraction(1,4)
assert Fraction(M0,1)/R0==CANDIDATE

canon=set()
for _,ss,es,ints in mins:
  canon.add((ss,es,ints))

print('D',D)
print('SEARCH_LAYER_SIZES',f'1..{S_MAX}')
print('FEASIBLE_RELAXED_PROFILES',feasible)
print('STRICTLY_SHORTER_MASS_PROFILES',shorter)
print('TAIL_BOUND_IF_ANY_LAYER_GE_15','C>=17/3>16/3')
print('MAX_DIAMETER_REFERENCE_PROFILE','s=(1,1,4) e=(1,4,4) C=4')
print('MIN_STRICTLY_SHORTER_C',f'{best[0].numerator}/{best[0].denominator}')
print('ONE_MINIMIZER_S',best[1])
print('ONE_MINIMIZER_E',best[2])
print('ONE_MINIMIZER_INTERNAL_DEGREE_SUMS',best[3])
print('NUMBER_OF_EQUALITY_RECORDS',len(mins))
print('EQUALITY_RECORDS')
for rec in sorted(canon):
  print(rec)
print('CLAIM P16-D5-3LAYER-RESISTANCE-RELAXATION-01 PASS')
print('ALL_EXACT_CHECKS_PASSED')
