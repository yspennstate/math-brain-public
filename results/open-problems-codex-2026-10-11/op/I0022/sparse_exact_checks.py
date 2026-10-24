"""Exact integer checks of a sparse-weight condensation construction.

The allocation/cycle-lemma partition function is checked against an independent
ordered-tree recursion for small n. No floating-point partition functions.
"""
from fractions import Fraction
from math import comb
import pathlib, json, time
ROOT=pathlib.Path(__file__).parent
START=time.monotonic()

def weights(M):
 w={0:1,1:1}
 k=3
 while k<=M:
  w[k]=1<<(k**3)
  k*=3
 return w

def partition(n):
 # Z_n = (1/n)[z^(n-1)] Phi(z)^n.
 M=n-1; w=weights(M); p=[0]*n; p[0]=1
 for _ in range(n):
  q=[0]*n
  for i,c in enumerate(p):
   if c:
    for d,v in w.items():
     if i+d<n: q[i+d]+=c*v
  p=q
 assert p[M]%n==0
 return p[M]//n

def tree_recursion(N):
 # T(z)=z Phi(T(z)): coefficient-by-coefficient independent computation.
 z=[0]*(N+1); w=weights(N-1)
 for n in range(1,N+1):
  coeff=0
  for d,v in w.items():
   if d>n-1: continue
   p=[0]*n; p[0]=1
   for _ in range(d):
    q=[0]*n
    for i,c in enumerate(p):
     if c:
      for j in range(1,n-i):
       q[i+j]+=c*z[j]
    p=q
   coeff+=v*p[n-1]
  z[n]=coeff
 return z

small=tree_recursion(13)
for n in range(1,14): assert small[n]==partition(n)

rows=[]
for k in [3,9,27]:
 for q in [1,2]:
  n=q*k+1; Z=partition(n)
  target_count=1 if q==1 else k
  target=target_count*(1<<(q*k**3))
  assert 0<target<=Z
  bad=Fraction(Z-target,Z)
  gap=8*k**3//9
  exponent=2*q*k-gap
  bound=Fraction(1<<exponent) if exponent>=0 else Fraction(1,1<<(-exponent))
  assert bad<=bound
  # Check the degree energy upper bound for all feasible degree multisets.
  w=weights(q*k); degrees=sorted(d for d in w if d>0)
  max_bad=-1; patterns=0
  def visit(i,budget,count_hubs,energy):
   if i==len(degrees):
    if budget==0: yield count_hubs,energy
    return
   d=degrees[i]
   for count in range(budget//d+1):
    yield from visit(i+1,budget-count*d,count_hubs+(count if d==k else 0),
                     energy+(count*d**3 if d>=3 else 0))
  for hubs,energy in visit(0,q*k,0,0):
   patterns+=1
   if hubs<q:
    max_bad=max(max_bad,energy)
    assert energy<=q*k**3-gap
  # Distance distribution for exact target graph with uniform iid vertices.
  if q==1:
   pair={0:Fraction(1,n),1:Fraction(2*k,n*n),2:Fraction(k*(k-1),n*n)}
  else:
   # centers 0,1; k-1 leaves on first, k on second
   A=k-1; B=k
   pair={0:Fraction(1,n),1:Fraction(2*(n-1),n*n),
         2:Fraction(A*(A-1)+B*(B-1)+2*(A+B),n*n),
         3:Fraction(2*A*B,n*n)}
  assert sum(pair.values())==1
  rows.append({'k':k,'q':q,'n':n,'degree_patterns':patterns,
               'maximum_bad_energy':max_bad,'proved_energy_bound':q*k**3-gap,
               'partition_bit_length':Z.bit_length(),
               'bad_probability_approx':float(bad),
               'bad_probability_positive':bad>0,
               'bad_probability_numerator_bits':bad.numerator.bit_length(),
               'bad_probability_denominator_bits':bad.denominator.bit_length(),
               'bad_probability_bound_base2_exponent':exponent,
               'target_pair_distance_law':{str(d):str(p) for d,p in pair.items()}})
results={'independent_partition_checks':13,'rows':rows,
         'elapsed_seconds':round(time.monotonic()-START,3)}
(ROOT/'sparse_exact_checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
