import sympy as s,json
from pathlib import Path
m=4;x=s.symbols('x0:4');mass=sum(x)
V=s.Matrix([2*x[0]*x[1]+x[0]*(x[2]+x[3]),x[0]**2+x[1]**2+x[1]*(x[2]+x[3]),x[3]*mass,x[2]*mass])
c=s.ones(4,1)/4;A=V.jacobian(x).subs(dict(zip(x,c)));B=A-s.ones(4,4)/4
N=s.eye(4)-B.T*B
Es=[]
for steps in range(5):
 R=s.ones(1,4)
 for t in range(steps):R=R.col_join(N*B**t)
 Es.append(R.nullspace())
assert [len(e) for e in Es]==[3,2,2,2,2]
P=s.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
for d in Es[3]:
 assert B*d==P*d
 assert s.simplify(V.subs(dict(zip(x,c+d)))-(c+B*d))==s.zeros(4,1)
a,b=s.symbols('a b');pt=s.Matrix([a,a,b,1-2*a-b]);assert s.simplify(V.subs(dict(zip(x,pt)))-P*pt)==s.zeros(4,1)
Avg=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0,0],[s.Rational(1,2),s.Rational(1,2),0,0],[0,0,1,0],[0,0,0,1]])
# Global projection identity on mass-one hyperplane, not only the equality locus.
w=s.Matrix([x[0],x[1],x[2],1-x[0]-x[1]-x[2]])
assert s.simplify(Avg*V.subs(dict(zip(x,w)))-P*Avg*w)==s.zeros(4,1)
# An independent contracting linear example with several strict preimage reductions.
C=s.Matrix([[s.Rational(1,2),s.Rational(1,2),0,0],[s.Rational(1,2),s.Rational(1,2),0,0],[0,0,1,0],[0,0,0,1]])
R=s.Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]);D=R*C;Nd=s.eye(4)-D.T*D;dims=[]
for steps in range(5):
 M=s.ones(1,4)
 for t in range(steps):M=M.col_join(Nd*D**t)
 dims.append(len(M.nullspace()))
assert dims==[3,2,1,0,0]
out={'nonlinear_B':str(B),'nonlinear_E_dimensions':[len(e) for e in Es],'nonlinear_periodic_family':'(a,a,b,1-2a-b), coordinate swap 3 and 4','linear_preimage_dimensions':dims,'checks':'All symbolic assertions passed exactly over rationals.'}
Path('exact_linearisation_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(out)
