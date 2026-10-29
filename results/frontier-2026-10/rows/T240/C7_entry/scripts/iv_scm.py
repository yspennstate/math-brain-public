"""Exact outward interval first derivatives of the seven-overlap erf ODE.

All constants are rational intervals except proved pi/sqrt/asin enclosures.
The Gaussian exponential-tilt identity evaluates the quadratic SGD drift.
"""
from iv_exact import I, pi

class J:
    __slots__=('v','d')
    def __init__(self,v,d):
        self.v=I.of(v)
        self.d=tuple(I.of(x) for x in d)
    @classmethod
    def constant(cls,v,n): return cls(v,[0]*n)
    def coerce(self,x):
        if isinstance(x,J):
            if len(x.d)!=len(self.d): raise ValueError('AD dimension mismatch')
            return x
        return J.constant(x,len(self.d))
    def __add__(self,x):
        x=self.coerce(x)
        return J(self.v+x.v,[a+b for a,b in zip(self.d,x.d)])
    __radd__=__add__
    def __neg__(self): return J(-self.v,[-a for a in self.d])
    def __sub__(self,x): return self+-self.coerce(x)
    def __rsub__(self,x): return self.coerce(x)+-self
    def __mul__(self,x):
        x=self.coerce(x)
        return J(self.v*x.v,[a*x.v+self.v*b for a,b in zip(self.d,x.d)])
    __rmul__=__mul__
    def __truediv__(self,x):
        x=self.coerce(x)
        den=x.v.square()
        return J(self.v/x.v,[(a*x.v-self.v*b)/den for a,b in zip(self.d,x.d)])
    def __rtruediv__(self,x): return self.coerce(x)/self
    def square(self): return J(self.v.square(),[2*self.v*a for a in self.d])
    def sqrt(self):
        root=self.v.sqrt()
        return J(root,[a/(2*root) for a in self.d])
    def asin(self):
        den=(1-self.v.square()).sqrt()
        return J(self.v.asin(),[a/den for a in self.d])

def variables(box):
    n=len(box)
    return [J(v,[int(i==j) for j in range(n)]) for i,v in enumerate(box)]

def full_driver(x,eta):
    """Order Q11,Q12,Q22,R11,R12,R21,R22; input values may be jets."""
    n=len(x[0].d)
    c=lambda a:J.constant(a,n)
    eta=eta if isinstance(eta,J) else c(eta)
    mu=c(2/pi())
    Q=[[x[0],x[1]],[x[1],x[2]]]
    R=[[x[3],x[4]],[x[5],x[6]]]
    G=[[Q[0][0],Q[0][1],R[0][0],R[0][1]],
       [Q[1][0],Q[1][1],R[1][0],R[1][1]],
       [R[0][0],R[1][0],c(1),c(0)],
       [R[0][1],R[1][1],c(0),c(1)]]
    A=[[mu/((1+Q[i][i])*(1+Q[j][j])-Q[i][j].square()).sqrt()
        for j in range(2)] for i in range(2)]
    T=[[mu/(2*(1+Q[i][i])-R[i][m].square()).sqrt()
        for m in range(2)] for i in range(2)]
    beta=[(sum(Q[i][j]*A[i][j] for j in range(2))
           -sum(R[i][m]*T[i][m] for m in range(2)))/(1+Q[i][i])
          for i in range(2)]
    C={}
    signs=[-1,-1,1,1]
    for i,j in [(0,0),(0,1),(1,1)]:
        if i==j:
            den=1+2*G[i][i]
            tilted=[[G[a][b]-2*G[a][i]*G[i][b]/den
                     for b in range(4)] for a in range(4)]
        else:
            den=(1+G[i][i])*(1+G[j][j])-G[i][j].square()
            tilted=[[G[a][b]-((1+G[j][j])*G[a][i]*G[i][b]
                    -G[i][j]*(G[a][i]*G[j][b]+G[a][j]*G[i][b])
                    +(1+G[i][i])*G[a][j]*G[j][b])/den
                    for b in range(4)] for a in range(4)]
        risk=c(0)
        for a in range(4):
            for b in range(a,4):
                arg=tilted[a][b]/((1+tilted[a][a])*(1+tilted[b][b])).sqrt()
                risk=risk+(1 if a==b else 2)*signs[a]*signs[b]*mu*arg.asin()
        C[i,j]=A[i][j]*risk
    outQ=[]
    for i,j in [(0,0),(0,1),(1,1)]:
        deterministic=(beta[i]+beta[j])*Q[i][j]
        deterministic=deterministic-sum(A[i][l]*Q[l][j]+A[j][l]*Q[l][i]
                                       for l in range(2))
        deterministic=deterministic+sum(T[i][m]*R[j][m]+T[j][m]*R[i][m]
                                       for m in range(2))
        outQ.append(eta*deterministic+eta.square()*C[i,j])
    outR=[eta*(T[i][m]+beta[i]*R[i][m]-sum(A[i][j]*R[j][m]
                                                        for j in range(2)))
          for i in range(2) for m in range(2)]
    return outQ+outR

def symmetric_driver(box,eta):
    q,c,r=variables(box)
    f=full_driver([q,c,q,r,r,r,r],eta)
    return [f[0],f[1],f[3]]

def determinant(matrix):
    n=len(matrix)
    if n==1: return matrix[0][0]
    return sum((1 if j%2==0 else -1)*matrix[0][j]*determinant(
        [[matrix[a][b] for b in range(n) if b!=j] for a in range(1,n)])
               for j in range(n))
