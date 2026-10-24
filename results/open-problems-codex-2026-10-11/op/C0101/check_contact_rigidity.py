from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,math,time
R=Path(__file__).parent
start=time.time()
# Exact, homogeneous finite-jet arithmetic, including both endpoints.
count=0
for d in range(1,9):
 for ai in range(13):
  for bi in range(13-ai):
   a,b=F(ai,12),F(bi,12)
   top=min(2*d*a+1,2*d*b+1)
   for ci in range(math.floor(12*top)+1):
    c=F(ci,12)
    assert -1<=c-a-b<=d
    count+=1
# Check the finite contact construction on all previously certified witnesses.
data=json.loads((R/'periodic_phase_results.json').read_text())
residues=list(product(range(2),repeat=3));index={x:i for i,x in enumerate(residues)}
certificates=[]
for rec in data['cases']:
 if not rec.get('exact_verified'):continue
 A=[[F(v) for v in row] for row in rec['A']];b=list(map(F,rec['linear_phase']));z=rec['witness_values']
 def q(x):return sum(A[i][j]*x[i]*x[j]/2 for i in range(3) for j in range(3))
 def g(x):
  r=tuple(t%2 for t in x)
  ans=F(z[index[r]])+q(x)-q(r)+sum(b[i]*(x[i]-r[i]) for i in range(3))
  assert ans.denominator==1
  return ans
 for epsilon in [F(1,100),F(1,1000)]:
  def H(x):return g(x)-q(x)+epsilon*sum(t*t for t in x)
  # For each residue class the periodic error is constant. Completing the
  # square reduces its global minimum to nearest points around -b/(2ε).
  candidates=[]
  for r in residues:
   options=[]
   for i in range(3):
    ideal=(-b[i]/(2*epsilon)-r[i])/2
    k=math.floor(ideal);options.append([r[i]+2*k,r[i]+2*(k+1)])
   candidates.extend(product(*options))
  x0=min(candidates,key=H)
  delta=5-sum(A[i][i] for i in range(3))+6*epsilon
  def shift(y):return tuple(x0[i]+y[i] for i in range(3))
  def h(y):return H(shift(y))-H(x0)
  M=[[0]*3 for _ in range(3)]
  for i in range(3):
   ep=[0]*3;ep[i]=1;em=[0]*3;em[i]=-1
   assert h(ep)>=0 and h(em)>=0
   M[i][i]=int(g(shift(ep))+g(shift(em))-2*g(x0))
   err=F(M[i][i])-A[i][i]+2*epsilon
   assert 0<=err<=delta
   for j in range(i+1,3):
    ej=[0]*3;ej[j]=1;eij=ep[:];eij[j]=1
    M[i][j]=M[j][i]=int(g(shift(eij))-g(shift(ep))-g(shift(ej))+g(x0))
    err=F(M[i][j])-A[i][j]
    assert -delta<=err<=3*delta
  if delta<1:assert sum(M[i][i] for i in range(3))==5
  certificates.append({'A':rec['A'],'phase':rec['linear_phase'],'epsilon':str(epsilon),'delta_epsilon':str(delta),'contact':list(x0),'integer_contact_matrix':M})
# The loss of PSD is real at the level of the stated entrywise bounds.
# It must not be silently added as an extra conclusion of Theorem 12.
delta=F(1,10)
D=[[delta/2,delta,0],[delta,delta/2,0],[0,0,0]]
assert sum(D[i][i] for i in range(3))==delta
assert D[0][0]*D[1][1]-D[0][1]**2<0
out={'all_passed':True,'finite_jet_checks':count,'global_contact_checks':len(certificates),'contact_certificates':certificates,'entrywise_bounds_do_not_imply_psd':[[str(v) for v in row] for row in D],'elapsed_seconds':time.time()-start}
(R/'contact_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print({k:v for k,v in out.items() if k!='contact_certificates'},flush=True)
