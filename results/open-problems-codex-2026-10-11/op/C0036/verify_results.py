from fractions import Fraction as F
from math import prod
import pathlib,json
import numpy as np
P=pathlib.Path(__file__).resolve().parent
rec=json.loads((P/'exact_symmetrization_obstruction.json').read_text())
r=list(map(F,rec['parameters']));p=F(rec['geometric_mean']);U=set(rec['upset'])
assert prod(r)==p**6 and all(0<v<1 for v in r)
assert {((s<<1)&63)|(s>>5) for s in U}==U
assert all(s|(1<<i) in U for s in U for i in range(6))
def intended(s):
 if s.bit_count()>=5:return True
 if s.bit_count()!=4:return False
 i,j=[i for i in range(6) if not(s>>i&1)]
 return min(j-i,6-(j-i)) in [1,3]
assert U=={s for s in range(64) if intended(s)}
a=sum(prod(r[i] if s>>i&1 else 1-r[i] for i in range(6)) for s in U)
b=sum(p**s.bit_count()*(1-p)**(6-s.bit_count()) for s in U)
assert a==F(rec['product_event_probability']) and b==F(rec['iid_event_probability'])
assert a-b==F(rec['gap'])<0
assert b==9*p**4*(1-p)**2+6*p**5*(1-p)+p**6
print('EXACT_AVERAGING_COUNTEREXAMPLE_PASS:',a-b)
# Recheck atom normalization and lower-bound errors from every numerical experiment.
R=json.loads((P/'finite_results.json').read_text())
for v in R:
 for k in ['lower','complement_lower']:
  z=v[k];assert z['normalization_error']<1e-11
  assert z['minimum_atom']>-1e-11
  assert z['rounded_gap']>=-1e-8
print('NUMERICAL_RECORDS_PASS:',len(R),'kernels',2*len(R),'comparisons')
# Independent cross-check of Boolean Mobius inversion against L-ensemble masses.
namespace={'__file__':str(P/'finite_search.py')};exec((P/'finite_search.py').read_text().split('records=[];')[0],namespace)
rng=np.random.default_rng(19936)
for n in [2,3,6]:
 for trial in range(5):
  B=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));H=B+B.conj().T
  _,V=np.linalg.eigh(H);lam=rng.uniform(.05,.95,n);Q=(V*lam)@V.conj().T
  J=Q@np.linalg.inv(np.eye(n)-Q);mu=namespace['law'](Q)
  for s in range(1<<n):
   ix=[i for i in range(n) if s>>i&1]
   mass=np.linalg.det(np.eye(n)-Q)*(np.linalg.det(J[np.ix_(ix,ix)]) if ix else 1)
   assert abs(mass-mu[s])<1e-10
print('INDEPENDENT_MOBIUS_L_ENSEMBLE_CHECK_PASS')
print('ALL_CHECKS_PASS')
