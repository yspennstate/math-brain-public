import sympy as S
from pathlib import Path
import json, math
base=Path(__file__).resolve().parent
t=S.symbols('t')
a,b,c=map(S.Rational,['1/3','2/5','3/4']);u,v=map(S.Rational,['1/12','9/80'])
P=S.zeros(3);atoms=[]
for mask in range(8):
 bits=[(mask>>i)&1 for i in range(3)];sg=[2*q-1 for q in bits];m=[z if bit else 1-z for z,bit in zip([a,b,c],bits)]
 p0=S.prod(m);f=-u*sg[0]*sg[1]*m[2]-v*sg[1]*sg[2]*m[0];p=p0+t*f
 d0=S.Matrix([sg[i]*S.prod(m[j] for j in range(3) if j!=i) for i in range(3)])
 e=S.Matrix([-v*S.prod(sg),0,-u*S.prod(sg)]);d=d0+t*e
 E=S.Matrix(3,3,lambda i,j:0 if i==j else sg[i]*sg[j]*m[3-i-j])
 P+=(e*d.T+d*e.T)/p-f*(d*d.T)/p**2+f*E/p
 atoms.append(p)
P=P.applyfunc(S.factor)
print('atoms',atoms,flush=True)
D=S.factor(S.lcm([S.denom(z) for z in P]));N=(P*D/t).applyfunc(S.cancel)
N=N.applyfunc(S.expand)
assert all(S.Poly(z,t).degree()>=0 for z in N)
print('D',D,'N degrees',[S.degree(z,t) for z in N],flush=True)

def primitive(poly):
 q=S.Poly(poly,t);content,q=q.clear_denoms();cont,q=q.primitive();coeff=list(reversed(q.all_coeffs()));return q,content/cont

def bern(poly,n=None):
 q=S.Poly(poly,t);n=q.degree() if n is None else n;power=[q.nth(k) for k in range(n+1)]
 return [sum(power[k]*S.Rational(math.comb(i,k),math.comb(n,k)) for k in range(i+1)) for i in range(n+1)]
report={'diagonal':[str(a),str(b),str(c)],'edge_squares':[str(u),str(v)],'atoms':[str(z) for z in atoms],'D':str(D),'N':[[str(z) for z in row] for row in N.tolist()],'N_coefficients':[[[str(S.Poly(z,t).nth(i)) for i in range(S.Poly(z,t).degree()+1)] for z in row] for row in N.tolist()],'D_coefficients':[str(S.Poly(D,t).nth(i)) for i in range(S.Poly(D,t).degree()+1)],'minors':[]}
for k in [1,2,3]:
 Q=S.factor(N[:k,:k].det(method='domain-ge'));q,_=primitive(Q)
 print('minor',k,'degree',q.degree(),'factors',S.factor(q.as_expr()),flush=True)
 bs=bern(q)
 print('bern sign min/max',min(bs),max(bs),'negative',sum(int(bool(z<0)) for z in bs),flush=True)
 # Degree elevation preserves the represented polynomial and can resolve
 # positive polynomials whose initial Bernstein control points are negative.
 n=q.degree()
 while min(bs)<0 and n<q.degree()+300:
  n+=1;bs=bern(q,n)
 print('final degree',n,'min',min(bs),'negative',sum(int(bool(z<0)) for z in bs),flush=True)
 report['minors'].append({'order':k,'polynomial_coefficients':[str(q.nth(i)) for i in range(q.degree()+1)],'bernstein_degree':n,'bernstein_coefficients':[str(x) for x in bs], 'all_nonnegative':all(z>=0 for z in bs),'positive_interior':any(z>0 for z in bs)})
(base/'rational_family_certificate.json').write_text(json.dumps(report,indent=2)+'\n')
