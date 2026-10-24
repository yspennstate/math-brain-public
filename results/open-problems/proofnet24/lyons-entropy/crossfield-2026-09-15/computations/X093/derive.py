import sympy as s
from itertools import combinations
Z=s.Matrix([[1,0],[0,1],[1,1],[1,2]])
W=s.Matrix([[-1,-1],[-1,-2],[1,0],[0,1]])
G=Z.T*Z
P=Z*G.inv()*Z.T
Q=s.eye(4)-P
Y=s.Matrix([[0,-s.I],[s.I,0]])
U=Z*Y*Z.T/3
R=W*Y*W.T/3
b,c,t=s.symbols('b c t', real=True)
K=P+t*(b*U+c*R)
rows=[]
for mask in range(16):
    ids=[i for i in range(4) if mask>>i&1]
    M=s.Matrix.hstack(*[(K if i in ids else s.eye(4)-K)[:,i] for i in range(4)])
    a=s.expand(M.det()).coeff(t,2)*2
    q=s.simplify(P.extract(ids,ids).det()) if len(ids)==2 else None
    rows.append((mask,ids,q,s.factor(a)))
print('P=',P)
print('U=',U)
print('R=',R)
print('Z gram',G, 'W gram',W.T*W, 'orth',Z.T*W)
for row in rows: print(row)
