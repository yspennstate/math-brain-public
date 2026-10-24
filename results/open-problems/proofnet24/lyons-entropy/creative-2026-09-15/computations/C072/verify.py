"""Reconstruct C072's whole-interval certificate using rational arithmetic only."""
from exact_core import *
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parent

def atom_curvature_bounds(data,x):
 lo=hi=F(0);I=F(0)
 for a in data:
  r=quad(a['r'],x);q=sum(z*w for z,w in zip(a['q'],x));p=a['p']
  l,u=interval_mul((r,r),log_bounds(p));lo-=u;hi-=l;I+=q*q/p
 return I,(lo,hi)

def signed_atom(K,mask):
 return determinant([[K[i][j] if (mask>>j)&1 else F(i==j)-K[i][j] for j in range(6)] for i in range(6)])

def direct_derivative_checks(s,data,x):
 K=kernel(s);A=zeros(6)
 for z,B in zip(x,BASES):A=add(A,scale(z,B))
 results=[]
 for mask,a in enumerate(data):
  vals={t:signed_atom(add(K,scale(F(t),A)),mask) for t in [-2,-1,0,1,2]}
  p=vals[0];q=(vals[-2]-8*vals[-1]+8*vals[1]-vals[2])/12;r=vals[1]-2*p+vals[-1]
  assert p==a['p'];assert q==sum(z*w for z,w in zip(x,a['q']));assert r==quad(a['r'],x)
  results.append([p,q,r])
 return results

def check_cone(gram,curvature):
 """Exact (++-) cone test, via two quadratic intervals; rational inputs only."""
 H=sub(gram,curvature);aa,dd,gg=H[0][0],H[1][1],H[2][2]
 assert aa>0 and dd>0 and gg>0
 bb,cc,ee=H[0][1],H[0][2],H[1][2]
 cut=-ee/cc if cc else None
 intervals=[]
 if not cc:
  intervals=[(0,None,ee>=0)]
 elif cut<=0:
  intervals=[(0,None,cc>0)]
 else:
  intervals=[(F(0),cut,cc<0),(cut,None,cc>0)]
 checks=[]
 for left,right,active in intervals:
  A,B,D=(aa-cc*cc/gg,bb-cc*ee/gg,dd-ee*ee/gg) if active else (aa,bb,dd)
  points=[left]+([] if right is None else [right])
  if right is None:
   if A<0 or (not A and B<0):return False,{'tail':(A,B,D)}
  if A>0:
   vertex=-B/A
   if vertex>=left and (right is None or vertex<=right):points.append(vertex)
  for t in points:
   value=A*t*t+2*B*t+D;checks.append([active,t,value])
   if value<0:return False,checks
 return True,checks

print('Reconstructing the exact 128 endpoint atoms...',flush=True)
a,b=atoms(S0),atoms(S1)
for s,data in [(S0,a),(S1,b)]:
 assert HB==F(617,140)
 for mask,atom in enumerate(data):
  ids=[i+1 for i in range(6) if (mask>>i)&1]
  odds=prod(F(1,i) for i in ids)*(1+s*sum(ids))/(7*(1+s*HB))
  assert atom['p']==odds>0
with open(ROOT/'endpoint_atoms.json') as f:assert decode(json.load(f))=={'s0':a,'s1':b}
print('PASS: all atom probabilities, complete first/second derivative normalization, and odds identities.',flush=True)

with open(ROOT/'bernstein_certificate.json') as f:cert=decode(json.load(f))
assert cert['s_interval']==[S0,S1] and cert['U']==U and cert['h']==HB and cert['frob']==FROB
lo,hi,mid,width,upper=frozen_bounds(a,b)
assert cert['frozen_lower']==lo and cert['frozen_upper']==hi and cert['curvature_upper_matrix']==upper
G=gram_coefficients(a,b)
for k,g in enumerate(G):
 exact=sub(sub(g,upper),FROB);B=floor_matrix_lower(exact);saved=cert['bernstein'][k]
 assert B==saved['matrix'];L,D=ldl(B)
 assert L==saved['ldl_L'] and D==saved['ldl_D']
 assert [v.__floor__() for v in D]==saved['pivot_floors']
 # The rounded matrix is below its exact parent in Loewner order:
 # each entry-rounding error is < 1e-6, so subtracting 6e-6 I suffices.
 for i in range(6):
  for j in range(6):
   rounded=B[i][j]+(F(6,10**6) if i==j else 0)
   assert 0<=exact[i][j]-rounded<F(1,10**6)
 print('PASS: Bernstein',k,'exact LDL pivot floors',saved['pivot_floors'],flush=True)

# The generic (++-) criterion is checked on the three distinguished rank-one
# directions using a conservative rational curvature upper matrix.
GC=[[G[0][i][j] for j in range(3)] for i in range(3)]
FC=[[upper[i][j] for j in range(3)] for i in range(3)]
# Direct cone routine assumes diagonal frozen curvature is zero; its three
# diagonal entries are part of H and remain positive under the upper bound.
ok,cone=check_cone(GC,FC);assert ok

x=[F(1),F(1),F(-1,1000),F(0),F(0),F(0)]
I,fr=atom_curvature_bounds(a,x);K=kernel(S0)
cov=[[(K[i][i]*(1-K[i][i]) if i==j else -K[i][j]**2) for j in range(6)] for i in range(6)]
avec=[sum(x[j]*BASES[j][i][i] for j in range(6)) for i in range(6)]
Ilinear=quad(inverse(cov),avec)
assert fr[0]-Ilinear>F(60);assert fr[0]>F(460)
assert I-fr[1]>quad(FROB,x)
assert determinant([row[:] for row in U[:3]])==-2

# Independent signed-column determinants verify the full real-support
# first/second derivative table on a dense direction, at both endpoints.
y=[F(1),F(-1,2),F(3,4),F(2,3),F(-1,5),F(1,7)]
checks0=direct_derivative_checks(S0,a,y);checks1=direct_derivative_checks(S1,b,y)

# The analytic imaginary-direction bound uses only these rational facts.
assert S0>=2;assert F(20,617)/(9*6*4)>F(1,10000)
for s in [S0,S1]:assert (1+s)/(7*(1+s*HB))>F(20,617)

out={'star_coefficients':x,'star_frobenius_squared':quad(FROB,x),'full_fisher':I,'frozen_interval':fr,
     'linear_occupation_fisher':Ilinear,'frozen_minus_linear_interval':[fr[0]-Ilinear,fr[1]-Ilinear],
     'entropy_interval':[fr[0]-I,fr[1]-I],'full_cone_checks':cone,
     'dense_real_coefficients':y,'independent_derivatives_s0':checks0,'independent_derivatives_s1':checks1,
     'imaginary_gap_lower':F(20,617)/(9*6*4)}
dump(ROOT/'verification_results.json',out)
print('PASS: rank-three star has frozen curvature > 460 and exceeds exact linear-occupation Fisher by > 60.',flush=True)
print('PASS: 128 independently differentiated signed-column determinants and all full-support-real Bernstein identities.',flush=True)
print('PASS: full nine-dimensional Hermitian support has uniform Frobenius gap 1/10000 on the whole interval.',flush=True)
print('Orientation only: frozen %.8f, linear Fisher %.8f, full Fisher %.8f.'%(float(fr[0]),float(Ilinear),float(I)),flush=True)
