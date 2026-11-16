"""Exact local bounds uniform on 7<=N<=infinity, in physical coordinates."""
import sys,json,importlib.util
from fractions import Fraction as F
from itertools import product
from math import factorial
import sympy as S
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
sys.path.append(str(HERE/'STRAT14/STRAT13'))
from collar_algebra import BASES,chart,part,derivative_bound,physical_ball_data

def physical_controls(kind):
    rr,B,K,gap,den,Qn,weights,num6=chart(kind)
    tau=sum(gap[i][i]for i in range(5));lam=(2+tau)/4
    Pi=[[den*(int(i==j)-S.Rational(1,5))-Qn[i][j]for j in range(5)]for i in range(5)]
    kn=sum(Pi[i][j]*gap[i][j]**2 for i in range(5)for j in range(5))
    hd=sum(Pi[i][i]*(4*lam/5-gap[i][i])for i in range(5))
    dn=hd-lam*den
    Bn=4*kn+(1-lam)*(2*dn-4*den)
    En=4*(1-lam)*dn
    inf=num6-Bn/4-En/16
    controls=[inf,inf+Bn/10,inf+Bn/5+En/25]
    # Exact degree-two Bernstein identity in v=1/(N-2), 0<=v<=1/5.
    # Check its three coefficients without introducing an eighth variable.
    assert controls[0]==inf
    assert -10*controls[0]+10*controls[1]==Bn
    assert 25*controls[0]-50*controls[1]+25*controls[2]==En
    return rr,B,K,gap,den,Qn,weights,controls

def local(kind):
    rr,B,K,gap,den,Qn,weights,polys=physical_controls(kind)
    active=[ij for ij,w in weights.items()if not part(w,0)]
    gs=[part(weights[ij],1)for ij in active]
    A=S.Matrix([[S.Rational(g.get(tuple(int(i==j)for i in range(7)),0))for j in range(7)]for g in gs])
    J=(A.T*A).inv()*A.T;assert J*A==S.eye(7)
    R=F(1,100);d0=F(str(part(den,0).get((0,)*7)))
    U,W,X,Y=BASES[kind];nu,nw,nx,ny=[sum(a*a for a in v)for v in (U,W,X,Y)]
    x,y,k,p,q,v,z=rr.gens
    assert den==nu*nw+nw*nx*p*p+nw*ny*q*q+nu*nx*v*v+nu*ny*z*z+nx*ny*(p*z-q*v)**2
    rows=[];c=F(1,6)
    for num in polys:
        assert part(num,0)==0
        L=part(num,1)/d0
        l=S.Matrix([[S.Rational(L.get(tuple(int(i==j)for i in range(7)),0))for j in range(7)]])
        mu=l*J;assert mu*A==l
        for signs in product((-1,1),repeat=7):
            row=mu-S.Rational(c)*S.Matrix([signs])*J
            assert min(row)>=0,(kind,L,mu,c)
            assert row*A==l-S.Rational(c)*S.Matrix([signs])
        caps=[F(mu[j])+c*sum(abs(F(J[i,j]))for i in range(7))for j in range(len(active))]
        def envelope(poly):
            assert all(sum(m)>=2 for m in poly)
            # Multinomial theorem: for each homogeneous degree d, its absolute
            # value is <= max_alpha |p_alpha|/binom(d,alpha) * ||h||_1^d.
            bydegree={}
            for m,a in poly.items():
                d=sum(m);multi=factorial(d)
                for j in m:multi//=factorial(j)
                bydegree[d]=max(bydegree.get(d,F(0)),abs(F(str(a)))/multi)
            return sum((a*R**(d-2)for d,a in bydegree.items()),F(0))
        M=envelope(num-den*L)/d0+sum(cap*envelope(weights[ij]-g)for cap,ij,g in zip(caps,active,gs))
        rounded=(M.numerator+M.denominator-1)//M.denominator
        rows.append(dict(linear=str(L),quadratic=str(part(num,2)/d0),multipliers=list(map(str,mu)),
                         multiplier_caps=list(map(str,caps)),remainder_exact=str(M),remainder_integer=rounded))
    M=max(r['remainder_integer']for r in rows);rho=min(R,c/(2*M))
    old=physical_ball_data(kind);factor=old['extraction_factor']
    radius=min(F(old['extraction_cube']),rho/factor)
    deriv=max(derivative_bound(g,1,R)for row in gap for g in row)
    forward=(deriv.numerator+deriv.denominator-1)//deriv.denominator
    return dict(kind=kind,controls=rows,left_inverse=[[str(a)for a in row]for row in J.tolist()],
        derivative_cube_radius=str(R),gram_lower=str(d0),linear_norm_c=str(c),
        remainder_integer=M,chart_radius=str(rho),chart_conclusion_c=str(c/2),
        extraction_factor=factor,extraction_check=old,matrix_ball_radius=str(radius),
        matrix_distance_factor=forward,matrix_conclusion_c=str(c/(2*forward)))

def main():
    results={kind:local(kind)for kind in BASES}
    (HERE/'local_uniform.json').write_text(json.dumps(results,indent=2)+'\n')
    for kind,r in results.items():print(kind,r,flush=True)
    print('PROVED (local_uniform.py): uniform physical ball estimates for every real N>=7 and N=infinity.')
if __name__=='__main__':main()
