import sympy as s,json,time
from pathlib import Path
b,c,r,U,V,t,K=s.symbols('b c r U V t K',real=True)
pi=[(1-b)*(1-c)-r*r,b*(1-c)+r*r,(1-b)*c+r*r,b*c-r*r]
ks=[-((1-c)*U+(1-b)*V+2*r*t)/pi[0],((1-c)*U-b*V+2*r*t)/pi[1],(-c*U+(1-b)*V+2*r*t)/pi[2],(c*U+b*V-2*r*t)/pi[3]]
alt=ks[0]-ks[1]-ks[2]+ks[3]
T=s.diag(((r*r*U+(1-b)**2*V+2*r*(1-b)*t)/(pi[0]*pi[2])),(((1-c)**2*U+r*r*V+2*r*(1-c)*t)/(pi[0]*pi[1])))+alt*s.Matrix([[b,r],[r,c]])
T=T.applyfunc(s.factor)
print('T',T,flush=True)
detT=s.factor(T.det());print('detT',detT,flush=True)
g=s.Matrix([[s.diff(p,q) for q in (b,c,r)] for p in pi]);F=g.T*s.diag(*[1/p for p in pi])*g
N=F-K*s.Matrix([[0,1,0],[1,0,0],[0,0,-2]])
# adj(T) in trace-coordinate functional
z=s.Matrix([T[1,1],T[0,0],-2*T[0,1]])
num=s.factor((z.T*N.adjugate()*z)[0]);dn=s.factor(N.det())
print('detN',dn,flush=True)
print('num',num,flush=True)
Path('data/symbolic_general.json').write_text(json.dumps(dict(T=str(T),detT=str(detT),detN=str(dn),numerator=str(num)),indent=2)+'\n')
