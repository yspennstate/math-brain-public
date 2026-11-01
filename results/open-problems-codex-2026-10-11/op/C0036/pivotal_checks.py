"""Exact finite checks of the new pivotal expansion and zero-direction structure."""
import itertools,json,pathlib
import sympy as s
P=pathlib.Path(__file__).resolve().parent
n=4;t=s.Rational(1,3);z=s.Symbol('z',real=True)
q=[0,1+s.I,2,1-s.I]
H=s.Matrix(n,n,lambda i,j:q[(j-i)%n]);r=8
subsets=[[i for i in range(n) if mask>>i&1] for mask in range(1<<n)]
polys=[]
for ix in subsets:
 M=t*s.eye(len(ix))+z*H.extract(ix,ix)
 polys.append(s.Poly(s.expand(M.det()),z))
assert polys[-1].coeff_monomial(z)==0
assert polys[-1].coeff_monomial(z**2)==-s.Rational(n*r,2)*t**(n-2)
def mobius(f):
 c=list(f)
 for i in range(n):
  for mask in range(1<<n):
   if mask>>i&1:c[mask]-=c[mask^(1<<i)]
 return c
def b0(f,i,j):
 others=[a for a in range(n) if a not in [i,j]];v=0
 for pattern in range(1<<len(others)):
  mask=sum(1<<others[k] for k in range(len(others)) if pattern>>k&1)
  k=pattern.bit_count();v+=t**k*(1-t)**(len(others)-k)*(f[mask|(1<<i)]-f[mask])
 return v
def rotate(mask):return ((mask<<1)&15)|(mask>>3)
events=[];invariant=0;zero_examples=[];min_positive=None
for bit_table in range(1<<(1<<n)):
 f=[(bit_table>>mask)&1 for mask in range(1<<n)]
 if any(f[mask]>f[mask|(1<<i)] for mask in range(1<<n) for i in range(n)):continue
 c=mobius(f);minimal=[mask for mask in range(1<<n) if f[mask] and all(not f[mask^(1<<i)] for i in range(n) if mask>>i&1)]
 alpha=[sum(c[mask]*t**(mask.bit_count()-1) for mask in range(1<<n) if mask>>i&1) for i in range(n)]
 gamma={}
 for i in range(n):
  for j in range(i+1,n):
   gamma[i,j]=s.factor((b0(f,i,j)+b0(f,j,i))/(2*t))
   equivalent=all(bool(mask>>i&1)==bool(mask>>j&1) for mask in minimal)
   assert (gamma[i,j]==0)==equivalent
 direct=sum(c[mask]*polys[mask].coeff_monomial(z**2) for mask in range(1<<n))+s.Rational(r,2)/t*sum(alpha)
 predicted=sum(s.expand_complex(H[i,j]*s.conjugate(H[i,j]))*gamma[i,j] for i,j in gamma)
 assert s.simplify(direct-predicted)==0 and direct>=0
 if direct>0:min_positive=direct if min_positive is None else min(min_positive,direct)
 if all(f[rotate(mask)]==f[mask] for mask in range(1<<n)):
  invariant+=1
  classes=[];unassigned=set(range(n))
  while unassigned:
   i=min(unassigned);block={j for j in unassigned if all(bool(mask>>i&1)==bool(mask>>j&1) for mask in minimal)}
   classes.append(block);unassigned-=block
  assert len({len(block) for block in classes})==1
  labels={i:k for k,block in enumerate(classes) for i in block}
  A=s.Matrix(n,n,lambda i,j:H[i,j]/100 if labels[i]==labels[j] else 0)
  Q=(t+s.Rational(1,17))*s.eye(n)+A
  B=s.Matrix(n,n,lambda i,j:H[i,j] if labels[i]!=labels[j] else 0)
  m=len(classes[0]);ds=[s.factor(Q.extract(sorted(block),sorted(block)).det()) for block in classes]
  assert all(d==ds[0] for d in ds)
  # Full-block dependence makes c_S vanish unless S is a union of classes.
  for mask in range(1<<n):
   if c[mask]:assert all(not (set(subsets[mask])&block) or block<=set(subsets[mask]) for block in classes)
  lhs=sum(c[mask]*Q.extract(subsets[mask],subsets[mask]).det() for mask in range(1<<n))
  rhs=sum(c[mask]*ds[0]**(mask.bit_count()//m) for mask in range(1<<n) if c[mask])
  assert s.simplify(lhs-rhs)==0
  for ix in subsets:
   if ix:assert s.simplify((Q.extract(ix,ix).inv()*B.extract(ix,ix)).trace())==0
  if len(classes)>1 and any(len(block)>1 for block in classes):zero_examples.append({'accepted_masks':[mask for mask in range(16) if f[mask]],'classes':[sorted(v) for v in classes]})
 events.append(bit_table)
assert len(events)==168
report={'all_monotone_events':len(events),'C4_invariant_events':invariant,'smallest_positive_coefficient_for_test_H':str(min_positive),'nontrivial_zero_partition_examples':zero_examples,'checks':['independent exact determinant coefficient','nonnegative pivotal formula','zero iff identical minimal-set membership','invariant partition/equal block sizes','exact block-diagonal equality','cross derivative trace vanishes']}
P.joinpath('pivotal_exact_results.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2));print('ALL_EXACT_PIVOTAL_CHECKS_PASS')
