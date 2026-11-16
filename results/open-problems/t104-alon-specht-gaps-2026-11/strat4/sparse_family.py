"""Exact reduction and high-precision polish of the triangle-pendant family."""
import sympy as s
import mpmath as mp
import json
x=s.symbols('x',positive=True)
# Edges 01=03=A, 02=B, 13=C, vertex4 isolated. Set B=x*A.
# Quotient eigenvalue lambda=A+2C is repeated iff C=(A+2B+sqrt(9A^2-4AB+4B^2))/4.
# Instead parameterize by l=lambda/A; quotient determinant gives B/A=l*(l-3)/(2*l-4).
l=s.symbols('l',real=True)
B=l*(l-3)/(2*l-4)
C=(l-1)/2
A=s.factor(1/(2+B+C)); B=s.factor(B*A); C=s.factor(C*A)
lam=s.factor(l*A); gap=s.factor(3*lam-2)
W=s.zeros(5)
for i,j,z in [(0,1,A),(0,2,B),(0,3,A),(1,3,C)]:W[i,j]=W[j,i]=z
L=s.diag(*[sum(W.row(i)) for i in range(5)])-W
H=s.eye(5)-s.ones(5)/5
G=s.simplify(lam*H-L)
# Rank-two G projector: Q=(sG-G^2)/(ab), a=lam, b=3lam-2.
Q=s.simplify(((lam+gap)*G-G*G)/(lam*gap));Pi=s.simplify(H-Q)
X1=s.factor(2*(lam*s.trace(G)-s.trace(G*G)))
X2=s.factor(s.Rational(10,3)*sum(Pi[i,j]*G[i,j]**2 for i in range(5) for j in range(5)))
X3=s.factor((1-lam)/3*(2*s.trace(G)-s.Rational(10,3)*sum(Pi[i,i]*G[i,i] for i in range(5))))
Y=s.factor(2*sum(W[i,j]*(Pi[i,i]+Pi[j,j]-2*Pi[i,j])*(G[i,i]+G[j,j]-2*G[i,j]) for i in range(5) for j in range(i+1,5)))
T=s.factor(X1+X2+X3-Y);R=s.factor(T/(X1+X2+X3))
print('A',A,'B',B,'C',C,'lambda',lam,'gap',gap)
spectral_var=s.symbols('t')
assert s.factor(L.charpoly(spectral_var).as_expr()-spectral_var**2*(spectral_var-lam)**2*(spectral_var-(lam-gap)))==0
assert s.simplify(Pi*Pi-Pi)==s.zeros(5)
assert s.simplify(L*Pi-lam*Pi)==s.zeros(5)
assert s.factor(2*A+B+C-1)==0
print('PROVED: exact spectrum, projector, and total weight checks passed.')
print('spectrum check',s.factor(L.charpoly().as_expr()))
print('T',T);print('den',s.factor(X1+X2+X3));print('ratio',R)
print('derivative numerator',s.factor(s.together(s.diff(R,l))).as_numer_denom()[0])
mp.mp.dps=80
rf=s.lambdify(l,R,'mpmath');der=s.lambdify(l,s.diff(R,l),'mpmath')
root=mp.findroot(der,(6,7))
print('l',mp.nstr(root,80),'ratio',mp.nstr(rf(root),80))
Dpoly=s.together(s.diff(R,l)).as_numer_denom()[0]
lo=s.Rational(int(mp.floor(root*10**60)),10**60);hi=lo+s.Rational(1,10**60)
assert Dpoly.subs(l,lo)<0 and Dpoly.subs(l,hi)>0
print('PROVED: exact rational root bracket',lo,hi)
shift=s.symbols('t')
sextic=28*shift**6+140*shift**5-31*shift**4-1250*shift**3-3282*shift**2-3960*shift-1638
assert s.factor(s.diff(R,l)-18*sextic.subs(shift,l-3)/s.denom(R)**2)==0
print('PROVED: shifted derivative polynomial checked.')
record={'l':mp.nstr(root,80),'ratio':mp.nstr(rf(root),80),'weights':{},'root_bracket':[str(lo),str(hi)]}
for i in range(5):
 for j in range(i+1,5):record['weights'][str(i)+str(j)]=mp.nstr(s.lambdify(l,W[i,j],'mpmath')(root),80)
with open('polished_point.json','w') as fp:json.dump(record,fp,indent=2)
for name,z in [('A',A),('B',B),('C',C),('lambda',lam),('g1',lam),('g2',gap),('T',T),('den',X1+X2+X3)]:print(name,mp.nstr(s.lambdify(l,z,'mpmath')(root),80))
with open('sparse_symbolic.txt','w') as f:
 for name,z in [('A',A),('B',B),('C',C),('lambda',lam),('gap',gap),('T',T),('den',s.factor(X1+X2+X3)),('ratio',R),('derivative',s.factor(s.together(s.diff(R,l))).as_numer_denom()[0])]:f.write(name+' = '+str(z)+'\n')
