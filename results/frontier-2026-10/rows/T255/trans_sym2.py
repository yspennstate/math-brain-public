# shape independence: general lower-triangular transverse block s*T (T symbolic), exact limit s->0 of drift(log Phi)/|W|^2
import sympy as sp, sys
g2,s=sp.symbols('g2 s',positive=True)
m=int(sys.argv[1])
syms=[]; T=sp.zeros(m-1,m-1)
for i in range(m-1):
    for j in range(i+1):
        t=sp.Symbol('t%d%d'%(i,j)); syms.append(t); T[i,j]=t
P=sp.eye(m)-sp.ones(m,m)/m
L=sp.zeros(m,m); L[0,0]=1
for i in range(m-1):
    for j in range(m-1): L[i+1,j+1]=s*T[i,j]
V=L*L.T; W=P*V*P; trW=W.trace(); D=sp.Matrix([W[i,i]-trW/m for i in range(m)]); v=sp.Matrix([V[i,i] for i in range(m)])
VD=V*D; nW2=sum(W[i,j]**2 for i in range(m) for j in range(m))
b=g2*(V*nW2/m**2+(v*VD.T+VD*v.T)/(2*m)); k=g2/m
bl=b.trace()-b[0,0]; ba=b[0,0]; ql=0; qa=0
for i in range(m):
    for j in range(m):
        N=sp.zeros(m,m); N[i,j]=1; X=L*N*L.T*P*V; E=k*(X+X.T)
        ql+=sp.expand(E.trace()-E[0,0])**2; qa+=E[0,0]**2
l=sp.expand(V.trace()-V[0,0])
d=bl/l-ba-ql/(2*l**2)+qa/2
lim=sp.limit(sp.together(d/nW2),s,0)
print("m",m,"limit:",sp.factor(sp.simplify(lim)),"| shape-free:",all(sp.simplify(sp.diff(lim,t))==0 for t in syms),flush=True)
