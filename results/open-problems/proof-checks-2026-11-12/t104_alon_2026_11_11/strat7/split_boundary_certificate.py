"""Exact matrix certificate at the rank-two boundary of the 4+2 split case."""
import itertools
import sympy as s
from concavity_certificate import cone,psd

def matrix(k,g,U):
    R=s.expand(U.dot(U));v2=U.applyfunc(lambda x:x*x/R)
    mass=(4-g)/2
    factor=(mass-1)/k**2
    constant=2*g*(1-g)+factor*(2*(k+1)*(k-2)-4*k*mass+s.Rational(5,2)*(k+2))
    M=constant*s.eye(4)+2*(k+2)/k*g*g*v2*v2.T-factor*2*(k+2)*g*s.diag(*v2)
    Lap=s.zeros(4)
    for i in range(4):
        for j in range(i+1,4):
            value=(s.Rational(1,4)+g*U[i]*U[j]/R)*(U[i]-U[j])**2/R
            Lap[i,i]+=value;Lap[j,j]+=value;Lap[i,j]-=value;Lap[j,i]-=value
    return M-2*g*Lap

def check_coeff(M,variables,label):
    den=s.lcm([s.denom(s.cancel(v)) for v in M])
    pol=[s.Poly(s.cancel(v*den),*variables) for v in M]
    exps=set().union(*(set(p.monoms()) for p in pol))
    fails=[]
    for exp in sorted(exps):
        mat=s.Matrix(M.rows,M.cols,[p.coeff_monomial(exp) for p in pol])
        if not psd(mat):fails.append((exp,mat))
    print(label,'matrices',len(exps),'not PSD',len(fails),'denominator',s.factor(den),flush=True)
    for f in fails[:2]:print(f,flush=True)
    return not fails

def main():
    xyz,U,K=cone();x,y,z=xyz;u=s.symbols('u',nonnegative=True);k=4+u;g=s.symbols('g')
    R=s.expand(U.dot(U));p=-U[0]*U[3]
    # Clear the known positive denominator k^2 R^2 before expanding.
    mass=(4-g)/2;v2=U.applyfunc(lambda v:v*v)
    constant=2*g*(1-g)*k*k*R*R+(mass-1)*(2*(k+1)*(k-2)-4*k*mass+s.Rational(5,2)*(k+2))*R*R
    M=constant*s.eye(4)+2*k*(k+2)*g*g*v2*v2.T-(mass-1)*2*(k+2)*g*R*s.diag(*v2)
    Lap=s.zeros(4)
    for i in range(4):
        for j in range(i+1,4):
            value=(R/4+g*U[i]*U[j])*(U[i]-U[j])**2
            Lap[i,i]+=value;Lap[j,j]+=value;Lap[i,j]-=value;Lap[j,i]-=value
    M-=2*g*k*k*Lap
    M=(K.T*M*K).applyfunc(s.expand)
    coeff=[M.applyfunc(lambda e:e.coeff(g,j)) for j in range(3)]
    conc=coeff[2]
    assert check_coeff(-conc,(*xyz,u),'concavity')
    for gg in [0,R/(4*p)]:
        endpoint=coeff[0] if gg==0 else (16*p*p*coeff[0]+4*p*R*coeff[1]+R*R*coeff[2]).applyfunc(s.expand)
        # Positive definite pure-axis coefficients at u=0 make the endpoint
        # positive definite at every nonzero cone point, even when u>0.
        degree=6 if gg==0 else 10
        for idx in range(3):
            exp=[0,0,0,0];exp[idx]=degree
            axis=s.Matrix(2,2,[s.Poly(v,*xyz,u).coeff_monomial(tuple(exp)) for v in endpoint])
            assert axis[0,0]>0 and axis.det()>0
        if check_coeff(endpoint,(*xyz,u),'endpoint '+str(gg)[:10]):continue
        for perm in itertools.permutations(xyz):
            a,b,c=s.symbols('a b c',nonnegative=True)
            ep=endpoint.subs({perm[0]:a+b+c,perm[1]:b+c,perm[2]:c},simultaneous=True)
            assert check_coeff(ep,(a,b,c,u),'ordering '+str(perm))
    print('PROVED: the rank-two boundary with a tied top edge has T>0 for any selected one-dimensional top subspace, for N>=6.')
if __name__=='__main__':main()
