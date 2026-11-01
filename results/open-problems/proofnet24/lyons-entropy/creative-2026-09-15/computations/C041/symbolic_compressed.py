exec(open(__file__.replace('symbolic_compressed.py','explore.py')).read().split('edges=')[0])
cs=[0,1,2,0,1,2]
K=sp.Matrix(6,6,lambda i,j:sp.Rational(1,2)*(int(cs[i]==cs[j])-sp.Rational(1,3)))
U=sp.Matrix(6,4,lambda i,j: 1 if j==0 else (int(i==j-1)-int(i==j+2)))
UP=list(it.combinations(range(4),2))
Q=sp.Matrix([[U.extract(ij,kl).det() for kl in UP] for ij in pairs])
a,b,c,d,e,f,g=sp.symbols('a b c d e f g',real=True)
spec={(0,0,0):0,(0,0,1):a,(0,0,2):b,(0,1,1):c,(0,1,2):d,(1,1,1):e,(0,2,2):f,(1,1,2):g}
fs=[spec.get(tuple(sorted([len([i for i in S if i//2==j]) for j in range(3)])),0) for S in SS]
T=operator(K,fs)
TC=sp.simplify(Q.T*T*Q)
print('TC',TC)

z=sp.Matrix([0,-1,0,1,-1,1,-1,0,1,0,-1,0,1,-1,0])
print('negative witness',sp.expand((z.T*T*z)[0]))
# orthogonal conjugacy? normalize U col norm (6,2,2,2) and 2forms (12,12,12,4,4,4)
DD=sp.diag(1/sp.sqrt(12),1/sp.sqrt(12),1/sp.sqrt(12),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,2))
NC=sp.simplify(DD*TC*DD)
print('normalized',NC)

x,y,r,s=sp.symbols('x y r s',real=True)
CS=sp.simplify(TC.subs({b:x-g+2*d,c:y-g+2*d-r,e:d-r,f:g+s}))
print('CS',CS)
G=sp.Matrix([[1,0,0,0],[1,0,0,1],[0,1,-1,1],[0,1,1,0],[0,1,0,0]])
rays=[]
for ids in it.combinations(range(5),3):
 ns=G[list(ids),:].nullspace()
 if len(ns)!=1:continue
 w=ns[0]
 for sig in [1,-1]:
  t=sig*w
  if all(h>=0 for h in G*t):
   t=t/sp.gcd_list(list(t))
   if t not in rays:rays.append(t)
for ray in rays:
 CC=CS.subs(dict(zip([x,y,r,s],ray)))
 print('ray',list(ray),'eig',CC.eigenvals())
