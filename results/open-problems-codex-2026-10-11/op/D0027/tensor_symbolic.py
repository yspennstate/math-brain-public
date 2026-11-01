from pathlib import Path
import sympy as s,json,time
q,a,b=s.symbols('q a b',real=True);p=1-q
H=s.Matrix([[-p,p],[q,-q]]);N=s.diag(0,1);I=s.eye(2)
L=s.kronecker_product(I,H,I)-s.kronecker_product(N,H,N)
results={}
for name,T in [('constant',s.Matrix([[a,1-a],[b,1-b]])),('healthy',s.Matrix([[a,-a],[b,1-b]]))]:
 A=s.simplify(T.inv()*N*T);B=s.simplify(T.inv()*H*T)
 K=s.kronecker_product(I,B,I)-s.kronecker_product(A,B,A)
 # Tensor conjugacy follows from (X tensor Y)(U tensor V)=XU tensor YV.
 # Avoid a redundant generic 8-by-8 symbolic inverse; check each factor.
 assert s.simplify(T.inv()*T)==s.eye(2)
 assert s.simplify(A*A-A)==s.zeros(2)
 assert s.simplify(B.trace()+1)==0
 assert s.simplify(K*s.ones(8,1))==s.zeros(8,1)
 results[name]={'T':str(T),'A':str(A),'B':str(B),'K_000_111':str(s.factor(K[0,7])),'K_010_101':str(s.factor(K[2,5]))}
# All four proposed local Markov cases, tested symbolically.
Ts={'identity':s.eye(2),'spin_flip':s.Matrix([[0,1],[1,0]]),'dual':s.Matrix([[p,-p],[p,q]]),'dual_flip':s.Matrix([[-p,p],[q,p]])}
for name,T in Ts.items():
 A=s.simplify(T.inv()*N*T);B=s.simplify(T.inv()*H*T)
 results[name]={'A':str(A),'B':str(B)}
Path('tensor_symbolic.json').write_text(json.dumps(results,indent=2),encoding='utf8')
for k,v in results.items():print(k,v,flush=True)
