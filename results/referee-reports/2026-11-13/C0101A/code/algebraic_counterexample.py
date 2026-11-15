"""Exact algebraic and Descartes certificate for a residual maximal point.

This is a theorem-based nonperiodic certificate. It does not claim an irrational
matrix can have a full-rank affine-periodic integer representative.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import json
from pathlib import Path
import sympy as S
ROOT=Path(__file__).resolve().parents[1]


def main():
 t,z=S.symbols('t z');f=t**4+4*t**2-1
 p=z**4-26*z**3+46*z**2-26*z+1
 T=S.Matrix([[2,2,2,-1],[3,6,6,-2],[10,15,18,-6],[0,0,1,0]])
 assert T.charpoly(z).as_expr()==p
 a=1-t;b=t**3+4*t-1
 lam=(11*t**3+5*t**2+47*t+23)/2
 assert S.rem(p.subs(z,lam),f,t)==0
 adj=(z*S.eye(4)-T).adjugate();w=adj[0,:]
 C=S.Matrix([1,1,4,0]);X=S.Matrix([1,1,1,-1]);Y=S.Matrix([0,2,4,0])
 den=(w*C)[0];nx=(w*X)[0];ny=(w*Y)[0]
 assert S.rem((nx-a*den).subs(z,lam),f,t)==0
 assert S.rem((ny-b*den).subs(z,lam),f,t)==0
 norm=S.rem(a*a+b*b,f,t)
 assert S.expand(norm)==6-10*t+2*t*t-2*t**3
 # Linear independence excludes EVERY rational circle, not just a finite list.
 polynomials=[S.Integer(1),a,b,norm]
 coeff=S.Matrix([[S.expand(v).coeff(t,i) for v in polynomials] for i in range(4)])
 assert coeff.det()!=0
 assert S.Poly(f,t).is_irreducible
 # Exact Descartes sequence; each step uses the other Soddy circle.
 circles=[(1,1,0),(1,1,2),(4,1,4)];outer=(0,-1,0)
 sequence=[]
 for n in range(120):
  new=tuple(2*sum(c[k] for c in circles)-outer[k] for k in range(3))
  assert new[0]>max(c[0] for c in circles)
  j=n%3;outer,circles[j]=circles[j],new
  # Exact oriented pairwise tangency identity for proper circles.
  for i in range(3):
   for j2 in range(i):
    c,x,y=circles[i];d,u,v=circles[j2]
    assert (d*x-c*u)**2+(d*y-c*v)**2==(c+d)**2
  if n<18 or n%12==11:
   sequence.append({'step':n+1,'circle':list(new),'center':[str(S.Rational(new[1],new[0])),str(S.Rational(new[2],new[0]))],'radius':str(S.Rational(1,new[0]))})
 root=S.sqrt(S.sqrt(5)-2)
 P=[S.N(a.subs(t,root),80),S.N(b.subs(t,root),80)]
 cert={'interpretation':'Loewner-maximal points of the closed obstacle class; not a claim about cone peaks',
 't_minimal_polynomial':str(f),'t_isolating_interval':['48/100','49/100'],
 'point':['1-t','t^3+4*t-1'], 'point_equivalent':['1-sqrt(sqrt(5)-2)','sqrt(sqrt(5)+2)-1'],
 'decimal_point':[str(v) for v in P],
 'A_star':[['(1-t)/2','(t^3+4*t-1)/2','0'],['(t^3+4*t-1)/2','(t-1)/2','0'],['0','0','0']],
 'cycle_matrix':T.tolist(),'cycle_polynomial':str(p),'dominant_root_in_t':str(lam),
 'left_eigenvector':[str(v) for v in w], 'denominator':str(den),'x_numerator':str(nx),'y_numerator':str(ny),
 'norm_squared':str(norm),'independence_matrix':coeff.tolist(),'independence_determinant':str(coeff.det()),
 'checks':{'algebraic_identities':True,'irreducible_quartic':True,'exact_descartes_steps':120,'exact_pairwise_tangencies':True},
 'sequence':sequence}
 # Sympy integers need conversion for JSON.
 (ROOT/'data'/'algebraic_counterexample.json').write_text(json.dumps(cert,indent=2,default=str))
 print('P =',P,'; independence determinant =',coeff.det(),flush=True)
 print('120 exact Descartes steps and algebraic identities passed',flush=True)

if __name__=='__main__':main()
