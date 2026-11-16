"""Exact matrix coefficient certificate for fixed-top-projector concavity."""
import itertools
import sympy as s

def psd(M):
    for r in range(1,M.rows+1):
        for ids in itertools.combinations(range(M.rows),r):
            if M.extract(ids,ids).det()<0:return False
    return True

def cone():
    x,y,z=s.symbols('x y z',nonnegative=True)
    U=s.Matrix([3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z])
    K=s.zeros(4,2)
    for col,j in enumerate([1,2]):
        K[0,col]=U[3]-U[j];K[j,col]=U[0]-U[3];K[3,col]=U[j]-U[0]
    return (x,y,z),U,K

def main():
    xyz,U,K=cone();u=s.symbols('u',nonnegative=True);k=4+u
    R=s.expand(U.dot(U));P=U*U.T/R;p=P.diagonal().T
    a,b,c=s.symbols('a b c');V=s.Matrix([[a,b],[b,c]]);E=K*V*K.T
    ed=E.diagonal().T;em=s.trace(E)/2
    B=sum(P[i,j]*E[i,j]**2 for i in range(4) for j in range(4))
    Q=-2*s.trace(E*E)+(2*(k+2)/k-4)*B+4*sum(P[i,i]*(E*E)[i,i] for i in range(4))-2*(p.T*E*ed)[0]
    Q+=em/k**2*(-4*k*em+2*(k+2)*(p.dot(ed)))
    # Negative quadratic form must be PSD, with R*k^2 cleared.
    expr=s.Poly(s.expand(s.cancel(-Q*R*k*k)),a,b,c)
    M=s.zeros(3)
    vv=[a,b,c]
    for i in range(3):
        for j in range(3):M[i,j]=s.expand(expr.coeff_monomial(vv[i]*vv[j])/(1 if i==j else 2))
    polys=[s.Poly(M[i,j],*xyz,u) for i in range(3) for j in range(3)]
    exps=set().union(*(set(pp.monoms()) for pp in polys))
    fails=[]
    for exp in sorted(exps):
        mat=s.Matrix(3,3,[pp.coeff_monomial(exp) for pp in polys])
        if not psd(mat):fails.append((exp,mat))
    print('coefficient matrices',len(exps),'not PSD',len(fails),flush=True)
    for v in fails[:3]:print(v,flush=True)
    if fails:
        # Refine the cone according to the order of its three gap coordinates.
        for perm in itertools.permutations(xyz):
            aa,bb,cc=s.symbols('aa bb cc',nonnegative=True)
            MM=M.subs({perm[0]:aa+bb+cc,perm[1]:bb+cc,perm[2]:cc},simultaneous=True)
            pp=[s.Poly(v,aa,bb,cc,u) for v in MM]
            ee=set().union(*(set(v.monoms()) for v in pp))
            bad=[ex for ex in ee if not psd(s.Matrix(3,3,[v.coeff_monomial(ex) for v in pp]))]
            print('ordering',perm,'matrices',len(ee),'not PSD',len(bad),flush=True)
            assert not bad
    print('PROVED: T is concave in L4 when its one selected top eigenvector and the tied edge are fixed, for N>=6.')
if __name__=='__main__':main()
