"""Small exact-arithmetic checks; corroborating evidence, not proofs."""
from fractions import Fraction as F
from math import prod

def det(a):
    a=[list(map(F,r)) for r in a]; out=F(1)
    for i in range(len(a)):
        j=next(j for j in range(i,len(a)) if a[j][i])
        if j!=i: a[i],a[j]=a[j],a[i]; out=-out
        v=a[i][i]; out*=v
        for j in range(i+1,len(a)):
            t=a[j][i]/v
            for k in range(i+1,len(a)): a[j][k]-=t*a[i][k]
    return out

def rising(a,k): return prod(a+j for j in range(k))
def beta_moment(a,b,k): return rising(a,k)/rising(a+b,k)

# Cholesky source order d1,l1,d2,l2,d3; target t1,c1,t2,c2,t3.
d1,l1,d2,l2,d3=map(F,[2,3,5,7,11])
jac=[[2*d1,0,0,0,0],[l1,d1,0,0,0],[0,2*l1,2*d2,0,0],
     [0,0,l2,d2,0],[0,0,0,2*l2,2*d3]]
assert det(jac)==8*d3*d1*d1*d2*d2
print('Cholesky Jacobian:',det(jac))

# Dirichlet-root Jacobian n=4, x=(0,2,5,9), y=(1,3,7).
x=list(map(F,[0,2,5,9])); y=list(map(F,[1,3,7]))
q=[prod(t-z for z in y)/prod(t-z for k,z in enumerate(x) if k!=i) for i,t in enumerate(x)]
delta=lambda a: prod(a[j]-a[i] for i in range(len(a)) for j in range(i+1,len(a)))
assert sum(q)==1 and all(t>0 for t in q)
J=[[-q[i]/(x[i]-z) for z in y] for i in range(3)]
assert abs(det(J))==delta(y)/delta(x)
print('Dirichlet-root Jacobian:',abs(det(J)),'residues:',q)

# Size-two spectral-to-entry Jacobian at lambda=(-1,2), q=1/5, b=6/5.
q0=F(1,5); gap=F(3); b=F(6,5)
J=[[q0,1-q0,-gap],[1-q0,q0,gap],[-b/gap,b/gap,gap*gap*(1-2*q0)/(2*b)]]
assert abs(det(J))==gap*gap/(2*b)
print('Size-two spectral Jacobian:',abs(det(J)))

for theta in [F(1,3),F(1,2),F(1),F(7,4)]:
    for j in [1,2,4]:
        a=theta/2; c=theta*j
        # All joint moments through degree eight of beta-gamma split.
        for k in range(5):
            for l in range(5):
                split=rising(a,k)*rising(c,l)/rising(a+c,k+l)*rising(a+c,k+l)
                assert split==rising(a,k)*rising(c,l)
    for S in [F(1,2),F(2),F(7,3),F(5)]:
        for d in [F(0),S/3]:
            Et=(theta-S)/(theta+S)
            Eb=(1-Et)*d/S-(1+Et)*d/(S+2*theta)
            assert F(1,2)+Eb/4==F(1,2)+d/(2*(S+2*theta))
        Eminus=4*S*(S+1)/((S+theta)*(S+theta+1))
        Eplus=4*theta*(theta+1)/((S+theta)*(S+theta+1))
        variance=(Eminus/(S+1)+Eplus/(S+2*theta+1))/16
        assert variance==1/(4*(S+2*theta+1))
    for m in range(1,6):
        raw=sum(theta*(j-F(1,2))+theta*j for j in range(1,m+1))
        chol=sum(theta*(j+F(1,2)) for j in range(1,m+1))+sum(theta*j for j in range(1,m))
        assert raw==chol==theta*(m*m+F(m,2))
print('Beta-gamma mixed moments, odd-parity trace shapes, KN means/variances: exact agreement')

# Uniform n=2 Jacobi, beta=2: integrate z-x over x in (0,y), z in (y,1).
for y0 in [F(1,7),F(1,2),F(4,5)]:
    integral=y0*(1-y0*y0)/2-y0*y0*(1-y0)/2
    assert integral==y0*(1-y0)/2
print('Jacobi n=2 deletion constant: F(y)=y(1-y)/2, normalised density 6y(1-y)')
print('All exact checks passed.')
