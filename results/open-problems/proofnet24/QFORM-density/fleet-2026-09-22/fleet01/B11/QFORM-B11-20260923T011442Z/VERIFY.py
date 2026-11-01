from fractions import Fraction
import math

qs=[(0,1),(1,0),(1,1),(2,-1),(1,3)]
x=[Fraction(2),Fraction(-1),Fraction(3),Fraction(1,2),Fraction(-2)]

def det2(q,r):
    return q[0]*r[1]-q[1]*r[0]

def nu(q):
    u,v=q
    return (u*u,u*v,v*v)

def det3_rows(rows):
    (a,b,c),(d,e,f),(g,h,i)=rows
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

n=len(qs)
A=[[Fraction(0) for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i!=j:
            A[i][j]=Fraction(det2(qs[i],qs[j])**2)

Q=sum(x[i]*A[i][j]*x[j] for i in range(n) for j in range(n))
L20=sum(Fraction(qs[i][0]**2)*x[i] for i in range(n))
L11=sum(Fraction(qs[i][0]*qs[i][1])*x[i] for i in range(n))
L02=sum(Fraction(qs[i][1]**2)*x[i] for i in range(n))
Qdet=2*(L20*L02-L11*L11)
assert Q==Qdet

# Hub h=0, q_h=(0,1).
d=[A[0][j] for j in range(1,n)]
B=[[A[i][j] for j in range(1,n)] for i in range(1,n)]
W=sum(di*di for di in d)
curv=sum(d[i]*B[i][j]*d[j] for i in range(n-1) for j in range(n-1))
t=[Fraction(qs[j][1],qs[j][0]) for j in range(1,n)]
weights=[di*di for di in d]
mu=sum(weights[k]*t[k] for k in range(n-1))/W
var=sum(weights[k]*(t[k]-mu)**2 for k in range(n-1))/W
assert curv==2*W*W*var

for tri in [(0,1,2),(1,2,3),(2,3,4)]:
    i,j,k=tri
    lhs=det3_rows([nu(qs[r]) for r in tri])
    rhs=det2(qs[i],qs[j])*det2(qs[i],qs[k])*det2(qs[j],qs[k])
    assert lhs==rhs

Dprime_h_two_thirds=72*math.sqrt(3*math.e)
assert abs(Dprime_h_two_thirds-205.60816860279425)<1e-12

print('Q=',Q)
print('W=',W)
print('weighted_variance=',var)
print('aTBa=',curv)
print('2W2Var=',2*W*W*var)
print('Dprime_h=2/3_prefactor=',Dprime_h_two_thirds)
print('QFORM_B11_PROJECTIVE_CONIC_CHECK_PASS')
