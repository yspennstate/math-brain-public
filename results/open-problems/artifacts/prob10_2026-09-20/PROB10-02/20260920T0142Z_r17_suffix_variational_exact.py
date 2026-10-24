from itertools import product
from fractions import Fraction
import sympy as sp


def T(z,k,v,c,u):
    x=z[:k]; g=z[k:]
    d=[0]*(k+1); d[0]=c
    for j in range(1,k+1):
        d[j]=(1-g[j-1]) * int(bool(d[j-1] or (x[j-1]==v)))
    gp=[]
    for j in range(1,k):
        val=g[j]+d[j+1]-d[j]
        assert val in (0,1)
        gp.append(val)
    gp.append((1-d[k])*int(u==v))
    return tuple(x[1:]+(u,)+tuple(gp))


def effective_c(first_x,first_g,v,c):
    return (1-first_g)*int(bool(c or (first_x==v)))

# 1. Projection lemma: dropping the first site after a (k+1)-transition
# is exactly the k-transition with the effective incoming carry.
for k in range(1,6):
    checked=0
    for bits in product((0,1), repeat=2*(k+1)):
        z=tuple(bits)
        for v,c,u in product((0,1), repeat=3):
            znew=T(z,k+1,v,c,u)
            proj=tuple(z[1:k+1]+z[k+2:])  # x_2..x_{k+1}, g_2..g_{k+1}
            ce=effective_c(z[0],z[k+1],v,c)
            rhs=T(proj,k,v,ce,u)
            lhs=tuple(znew[1:k+1]+znew[k+2:]) # drop first new x and first new g
            assert lhs==rhs, (k,z,v,c,u,lhs,rhs)
            checked+=1
    print(f'PROJECTION_PASS k={k} cases={checked}')

# 2. Exact obstruction to the naive claim that a changed incoming carry only
# matters when it survives all the way to the right endpoint.
# Here the carry discrepancy dies at site 2 because g_2=1, yet it changes
# the first outgoing gradient.
k=2
z=(0,0, 0,1)  # x=(0,0), g=(0,1)
v=1; u=0
z0=T(z,k,v,0,u)
z1=T(z,k,v,1,u)
assert z0!=z1
assert z0[-1]==z1[-1]  # same terminal gradient: discrepancy has died
print('EARLY_EXTINCTION_STATE_CHANGE_PASS', 'z=',z,'v=',v,'u=',u,'c0->',z0,'c1->',z1)

# 3. k=1 exact controlled bound p_1^*=1/3.
# Upper bound is analytic: d >= (1-g)1{x=v}; with v fair independent,
# E d >= (1-p)/2; stationarity gives p=(1-E d)/2, hence p<=1/3.
# Achievability: c=0 stationary chain, solved exactly below.
states=list(product((0,1), repeat=2))  # (x,g)
idx={s:i for i,s in enumerate(states)}
P=[[Fraction(0) for _ in states] for _ in states]
for i,z in enumerate(states):
    for v,u in product((0,1), repeat=2):
        zn=T(z,1,v,0,u)
        P[i][idx[zn]] += Fraction(1,4)
PM=sp.Matrix([[sp.Rational(x.numerator,x.denominator) for x in row] for row in P])
# Solve pi P=pi, sum pi=1.
p0,p1,p2,p3=sp.symbols('p0:4')
pi=sp.Matrix([[p0,p1,p2,p3]])
eqs=list((pi*PM-pi)) + [p0+p1+p2+p3-1]
sol=sp.solve(eqs,[p0,p1,p2,p3], dict=True)[0]
pi_vals=[sp.simplify(sol[x]) for x in (p0,p1,p2,p3)]
p=sum(pi_vals[i]*states[i][1] for i in range(4))
assert sp.simplify(p-sp.Rational(1,3))==0
print('K1_EXACT_PASS stationary=',pi_vals,'p_star=1/3','Gamma_1=2/3')
print('ALL_EXACT_CHECKS_PASS')
