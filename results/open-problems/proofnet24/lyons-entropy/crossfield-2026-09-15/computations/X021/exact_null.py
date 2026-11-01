import sympy as s
I=s.I
K=s.Matrix([[s.Rational(1,5),s.Rational(1,10),I/20],[s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],[-I/20,s.Rational(1,10),s.Rational(4,5)]])
d1,d2,d3,u12,u23,v13=s.symbols('d1 d2 d3 u12 u23 v13', real=True)
B=s.Matrix([[d1,u12-I,-1+I*v13],[u12+I,d2,u23-I],[-1-I*v13,u23+I,d3]])
gs=[G[:,k] for k in range(3) for G in [s.eye(3)-K,K]]
sol=s.solve([(g.conjugate().T*B*g)[0].expand() for g in gs],[d1,d2,d3,u12,u23,v13]); B=s.simplify(B.subs(sol))
print('B=',B)
print('common denominator=',s.ilcm(*[s.denom(s.re(x)) for x in B],*[s.denom(s.im(x)) for x in B]))
print('trB=',s.trace(B),'e2=',s.expand((s.trace(B)**2-s.trace(B*B))/2),'det=',s.factor(B.det()))
print('trKB=',s.trace(K*B).simplify())
print('K minors=',[K[:n,:n].det() for n in [1,2,3]])
print('I-K minors=',[(s.eye(3)-K)[:n,:n].det() for n in [1,2,3]])
p=[]
for mask in range(8):
 mat=s.Matrix.hstack(*[K[:,j] if mask>>j&1 else (s.eye(3)-K)[:,j] for j in range(3)])
 p.append(s.factor(mat.det()))
print('p=',p)
# derivative score direction A=adj B: adj A=det(B) B, positive scalar.
A=B.adjugate(); print('A=',A)
def directional(mask):
 C=s.Matrix.hstack(*[K[:,j] if mask>>j&1 else (s.eye(3)-K)[:,j] for j in range(3)])
 D=s.Matrix.hstack(*[A[:,j] if mask>>j&1 else -A[:,j] for j in range(3)])
 return s.simplify(p[mask]*s.trace(C.inv()*D))
fisher=sum(directional(mask)**2/p[mask] for mask in range(8))
print('fisher A approx=',s.N(fisher,14))
for k in range(3):
 R=[j for j in range(3) if j!=k]; r0=1<<R[0]; r1=1<<R[1]
 l0=s.log(p[r0]*p[r1]/(p[0]*p[r0+r1])); shift=1<<k
 l1=s.log(p[shift+r0]*p[shift+r1]/(p[shift]*p[shift+r0+r1]))
 print('lambda',k,0,l0,'positive?',s.exp(l0)>1,'and',1,l1,'positive?',s.exp(l1)>1)
assert all((g.conjugate().T*B*g)[0].simplify()==0 for g in gs)
assert all(B[k,k]>0 for k in range(3))
assert B.det()>0
assert ((s.trace(B)**2-s.trace(B*B))/2).expand()<0
