import itertools, math

signs=[(1,s,t) for s in (1,-1) for t in (1,-1)]

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def check(x,y,z,eta):
    r=(x,y,z)
    lhs=sum(det3(r,signs[i],signs[j])**2 for i,j in itertools.combinations(range(4),2))
    rhs=16*(x*x+y*y+z*z)
    assert abs(lhs-rhs) < 1e-10*max(1,abs(rhs))
    c=math.sqrt(1-eta*eta)
    d0=(8/3)*c*c*(1-eta**6)
    C=3*(16**(2/3))*d0**(-1/3)
    return lhs,d0,C

eta=1/64
c=math.sqrt(1-eta**2)
x=math.sqrt(1-eta**4-eta**6)-c*eta
y=math.sqrt(2*c*eta*x)
z=-eta
assert abs(x*x+y*y+z*z-(1-eta**6)) < 1e-12
lhs,d0,C=check(x,y,z,eta)
print('sum_squared_determinants =',lhs)
print('quadratic_det_lower_bound =',d0)
print('density_bound_endpoint =',C)
assert C < 13.738
