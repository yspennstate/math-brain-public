"""Exact rational coefficient test for the four-vertex tree + top edge case."""
import itertools
import sympy as s

def functional(W,P,k):
    n=W.rows;L=s.diag(*list(W*s.ones(n,1)))-W
    A=s.eye(n)-L
    mass=s.trace(L)/2
    hd=sum(P[i,i]*L[i,i] for i in range(n))
    B=sum(P[i,j]*A[i,j]**2 for i in range(n) for j in range(n))
    Y=2*sum(W[i,j]*(P[i,i]+P[j,j]-2*P[i,j])*(2-L[i,i]-L[j,j]+2*L[i,j]) for i in range(n) for j in range(i+1,n))
    X1=2*(s.trace(L)-s.trace(L*L))
    X2=2*(k+2)/k*B
    X3=(mass-1)/k**2*(2*(k+1)*(k-2)-4*k*mass+2*(k+2)*hd)
    return X1+X2+X3-Y

def main():
    x,y,z,u=s.symbols('x y z u',nonnegative=True)
    cases=[('star',s.Matrix([-x-y-z,x,y,z]),[(0,1,x/(2*x+y+z)),(0,2,y/(x+2*y+z)),(0,3,z/(x+y+2*z))]),
           ('path',s.Matrix([x,-x-y,y+z,-z]),[(0,1,x/(2*x+y)),(1,2,y/(x+2*y+z)),(2,3,z/(y+2*z))])]
    for name,v,edges in cases:
        W=s.zeros(6);P=s.zeros(6)
        for i,j,w in edges:W[i,j]=W[j,i]=w
        W[4,5]=W[5,4]=s.Rational(1,2)
        P[:4,:4]=v*v.T/(v.dot(v));P[4:6,4:6]=s.Matrix([[1,-1],[-1,1]])/2
        expr=functional(W,P,4+u)
        num,den=s.fraction(s.factor(expr))
        poly=s.Poly(num,x,y,z,u)
        assert num.subs(u,0)!=0
        neg=sum(bool(c<0) for c in poly.coeffs())
        print(name,'terms',len(poly.terms()),'negative',neg,flush=True)
        if neg:
            for perm in itertools.permutations([x,y,z]):
                a,b,c=s.symbols('a b c',nonnegative=True)
                pp=s.Poly(s.expand(num.subs({perm[0]:a+b+c,perm[1]:b+c,perm[2]:c},simultaneous=True)),a,b,c,u)
                nneg=sum(bool(v<0) for v in pp.coeffs())
                print('  ordering',perm,'negative',nneg,flush=True)
                assert not nneg
        print('positive denominator:',s.factor(den),flush=True)
    print('PROVED: every weighted four-vertex tree plus a tied edge, padded to N>=6, has T>=0.')
if __name__=='__main__':main()
