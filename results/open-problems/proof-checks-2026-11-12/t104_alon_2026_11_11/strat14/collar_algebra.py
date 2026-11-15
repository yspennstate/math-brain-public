"""Exact rational physical charts at the two disconnected equality types."""
from fractions import Fraction as F
from functools import lru_cache
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
import sympy as S
from itertools import product

BASES = {
    'edges': ([-4,1,1,1,1], [0,1,-1,-1,1], [0,1,1,-1,-1], [0,1,-1,1,-1]),
    'triangle': ([3,3,-2,-2,-2], [1,-1,0,0,0], [0,0,1,-1,0], [0,0,1,1,-2]),
}

@lru_cache(None)
def chart(kind):
    rr,x,y,k,p,q,v,z = ring('x,y,k,p,q,v,z',QQ)
    U,W,X,Y = BASES[kind]
    nu,nw = sum(a*a for a in U),sum(a*a for a in W)
    B = [[U[i]+p*X[i]+q*Y[i], W[i]+v*X[i]+z*Y[i]] for i in range(5)]
    gram = [[sum(b[i]*b[j] for b in B) for j in range(2)] for i in range(2)]
    den = gram[0][0]*gram[1][1]-gram[0][1]**2
    adj = [[gram[1][1],-gram[0][1]],[-gram[1][0],gram[0][0]]]
    Qn = [[sum(B[i][a]*adj[a][b]*B[j][b] for a in range(2) for b in range(2))
           for j in range(5)] for i in range(5)]
    K = [[(1+x)/nu,k/nu],[k/nu,(1+y)/nw]]
    gap = [[sum(B[i][a]*K[a][b]*B[j][b] for a in range(2) for b in range(2))
            for j in range(5)] for i in range(5)]
    tau = sum(gap[i][i] for i in range(5)); lam=(2+tau)/4
    weights = {(i,j):lam/5+gap[i][j] for i in range(5) for j in range(i+1,5)}
    tr2 = sum(gap[i][j]**2 for i in range(5) for j in range(5))
    diag2 = sum(gap[i][i]**2 for i in range(5))
    Mn = sum(Qn[i][i]*gap[i][i] for i in range(5))
    QdiagS2 = sum(Qn[i][i]*sum(gap[i][j]**2 for j in range(5)) for i in range(5))
    Rn = sum(Qn[i][j]*gap[i][j]**2 for i in range(5) for j in range(5))
    Rn += 2*sum(Qn[i][i]*gap[i][j]*gap[j][j] for i in range(5) for j in range(5))
    Pi = [[den*(int(i==j)-QQ(1,5))-Qn[i][j] for j in range(5)] for i in range(5)]
    num = 2*den*(lam*tau-tr2)+QQ(10,3)*sum(Pi[i][j]*gap[i][j]**2 for i in range(5) for j in range(5))
    num += (1-lam)/3*(2*den*tau-QQ(10,3)*sum(Pi[i][i]*gap[i][i] for i in range(5)))
    num -= 2*sum(w*(2*den-Qn[i][i]-Qn[j][j]+2*Qn[i][j])*(gap[i][i]+gap[j][j]-2*gap[i][j]) for (i,j),w in weights.items())
    return rr,B,K,gap,den,Qn,weights,num

def part(poly,degree):
    return poly.ring.from_dict({m:c for m,c in poly.items() if sum(m)==degree})

def tangent(kind):
    rr,B,K,gap,den,Qn,weights,num=chart(kind)
    d0=part(den,0); L=part(num,1)/d0
    Q=(part(num,2)-L*part(den,1))/d0
    active=[ij for ij,w in weights.items() if not part(w,0)]
    gs=[part(weights[ij],1) for ij in active]
    mat=S.Matrix([[S.Rational(g.get(tuple(int(i==j) for i in range(7)),0))
                   for j in range(7)] for g in gs])
    lin=S.Matrix([[S.Rational(L.get(tuple(int(i==j) for i in range(7)),0)) for j in range(7)]])
    return L,Q,active,gs,mat,lin

def derivative_bound(poly,order,radius):
    out=F(0)
    for mon,c in poly.items():
        d=sum(mon)
        if d<order:continue
        falling=1
        for j in range(order):falling*=d-j
        out+=abs(F(str(c)))*falling*radius**(d-order)
    return out

@lru_cache(None)
def local_data(kind):
    rr,B,K,gap,den,Qn,weights,num=chart(kind)
    L,Q,active,gs,A,l=tangent(kind)
    # A rational left inverse, including the redundant eighth edge at the
    # two-edge limit, found by the exact normal-equation formula.
    J=(A.T*A).inv()*A.T
    assert J*A==S.eye(7)
    lm=(S.Matrix([[S.Rational(2)]*4+[S.Rational(1,3)]*4]) if kind=='edges'
        else S.Matrix([[S.Rational(136,27)]+[S.Rational(128,81)]*6]))
    assert lm*A==l
    c=F(1,10) if kind=='edges' else F(1,6)
    caps=[F(lm[j])+c*sum(abs(F(J[i,j])) for i in range(7)) for j in range(len(active))]
    for signs in product((-1,1),repeat=7):
        row=lm-S.Rational(c)*S.Matrix([signs])*J
        assert min(row)>=0 and row*A==l-S.Rational(c)*S.Matrix([signs])
    R=F(1,100);Dmin=F(str(part(den,0).get((0,)*7)))
    # Orthogonality gives four squares and one squared minor.
    U,W,X,Y=BASES[kind]
    nu,nw,nx,ny=[sum(a*a for a in b) for b in (U,W,X,Y)]
    x,y,k,p,q,v,z=rr.gens
    assert den==nu*nw+nw*nx*p*p+nw*ny*q*q+nu*nx*v*v+nu*ny*z*z+nx*ny*(p*z-q*v)**2
    P0,P1,P2=[derivative_bound(num,i,R) for i in range(3)]
    D0,D1,D2=[derivative_bound(den,i,R) for i in range(3)]
    MT=P2/Dmin+(2*P1*D1+P0*D2)/Dmin**2+2*P0*D1**2/Dmin**3
    MG=[derivative_bound(weights[ij],2,R) for ij in active]
    M=(MT+sum(a*b for a,b in zip(caps,MG)))/2
    rounded=(M.numerator+M.denominator-1)//M.denominator
    rho=min(R,c/(2*rounded))
    assert rounded*rho<=c/2
    assert (1-R)**2/F(nu*nw)-R**2/F(nu**2)>0
    deriv=max(derivative_bound(g,1,R) for row in gap for g in row)
    factor=(deriv.numerator+deriv.denominator-1)//deriv.denominator
    return dict(kind=kind,coordinates=list(map(str,rr.gens)),
                basis=[list(b)for b in BASES[kind]],active_edges=[list(e) for e in active],
                active_linear=list(map(str,gs)),linear=str(L),quadratic=str(Q),
                derivative_matrix=[[str(v) for v in row] for row in A.tolist()],
                left_inverse=[[str(v) for v in row] for row in J.tolist()],
                multipliers=list(map(str,list(lm))),multiplier_caps=list(map(str,caps)),
                linear_norm_c=str(c),derivative_cube_radius=str(R),
                gram_determinant=str(den),gram_lower=str(Dmin),
                numerator_derivative_bounds=list(map(str,(P0,P1,P2))),
                denominator_derivative_bounds=list(map(str,(D0,D1,D2))),
                T_hessian_bound=str(MT),edge_hessian_bounds=list(map(str,MG)),
                remainder_bound=str(M),remainder_rounded=rounded,
                collar_radius_l1=str(rho),conclusion_c=str(c/2),
                matrix_derivative_bound=str(deriv),matrix_distance_factor=factor)

def physical_ball_data(kind):
    """Recover the local chart from an arbitrary nearby rank-two gap matrix."""
    U,W,X,Y=BASES[kind]
    nu,nw,nx,ny=[sum(a*a for a in b)for b in (U,W,X,Y)]
    norms=[nu,nw];l1=[sum(abs(x)for x in b)for b in (U,W,X,Y)]
    coeff=[[F(l1[i]*l1[j],n*m)for j,m in enumerate(norms)]for i,n in enumerate(norms)]
    lower=[[F(l1[i+2]*l1[j],n*m)for j,m in enumerate(norms)]for i,n in enumerate([nx,ny])]
    e=F(1,1000);a,b=coeff[0];_,d=coeff[1]
    det=(F(1,nu)-a*e)*(F(1,nw)-d*e)-b*b*e*e
    assert det>0 and F(1,nu)-a*e>0
    ki=[[(F(1,nw)+d*e)/det,b*e/det],[b*e/det,(F(1,nu)+a*e)/det]]
    bound=nu*a+nw*d+nu*b+sum(sum(lower[i][j]*ki[j][k]for j in range(2))for i in range(2)for k in range(2))
    rounded=(bound.numerator+bound.denominator-1)//bound.denominator
    local=local_data(kind)
    radius=min(e,F(local['collar_radius_l1'])/rounded)
    return dict(extraction_cube=str(e),K_determinant_lower=str(det),
                extraction_bound=str(bound),extraction_factor=rounded,
                matrix_ball_radius=str(radius),
                T_distance_c=str(F(local['conclusion_c'])/local['matrix_distance_factor']))

def connected_expansion(kind):
    rr,B,K,gap,den,Qn,weights,num=chart(kind)
    x,y,k,p,q,v,z=rr.gens;U,W,_,_=BASES[kind]
    nu,nw=[sum(a*a for a in b)for b in (U,W)]
    tau=sum(gap[i][i]for i in range(5));lam=(2+tau)/4
    tr2=sum(gap[i][j]**2 for i in range(5)for j in range(5))
    connected=lam*lam-lam*tau+(tau*tau-tr2)/2
    quadratic=(y-3*x)*(x-3*y)/16-QQ(nw,nu)*k*k
    assert part(connected,0)==0 and part(connected,1)==0 and part(connected,2)==quadratic
    return str(quadratic)

if __name__=='__main__':
    for kind in BASES:
        L,Q,active,gs,mat,lin=tangent(kind)
        print(kind,'L=',L,'Q=',Q,'active=',active,'g=',gs,'rank=',mat.rank())
        print('multipliers=',S.linsolve((mat.T,lin.T)))
        print('kernel=',mat.nullspace())
