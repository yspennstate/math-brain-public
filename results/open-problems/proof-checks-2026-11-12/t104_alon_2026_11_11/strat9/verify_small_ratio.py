"""PROVED: independent padded radial reconstruction and exact SOS replay."""
import json
from fractions import Fraction as F
import sympy as S
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from frame import A,B,C,d,e,f,h,a,r,formula

def psd(rows):
    mat=[[F(v)for v in row]for row in rows]
    assert all(mat[i][j]==mat[j][i]for i in range(len(mat))for j in range(len(mat)))
    while mat:
        p=mat[0][0];assert p>=0
        if p==0:
            assert all(v==0 for v in mat[0]);mat=[row[1:]for row in mat[1:]]
        else:mat=[[mat[i][j]-mat[i][0]*mat[0][j]/p for j in range(1,len(mat))]for i in range(1,len(mat))]

def main():
    data=json.load(open('small_ratio_certificate.json'));rho=F(data['rho'])
    assert 0<rho<F(3,7) and len(data['controls'])==3
    rr,*gen=ring('z0,z1,z2,z3,x0,x1,x2',QQ);z,x=gen[:4],gen[4:]
    U=[sum(((5-j)if i<j else -j)*z[j-1]for j in range(1,5))for i in range(5)]
    span=U[0]-U[4]
    W=[sum((U[4]-U[j+1])*x[j]for j in range(3))]+[span*x[j]for j in range(3)]+[sum((U[j+1]-U[0])*x[j]for j in range(3))]
    t=sum(v*v for v in U);n=sum(v*v for v in W)
    raw=[sum(v**4 for v in U),sum(v**4 for v in W),sum(v*v*w*w for v,w in zip(U,W)),sum(v**3 for v in U),sum(v*v*w for v,w in zip(U,W)),sum(v*w*w for v,w in zip(U,W)),sum(v**3 for v in W),-U[0]*U[4],(U[0]+U[4])**2]
    degrees=[(4,0),(0,4),(2,2),(3,0),(2,1),(1,2),(0,3),(2,0),(2,0)]
    pp,vv=S.symbols('p vv');sym=[A,B,C,d,e,f,h,pp,vv]
    D=20*pp-1-r*(7-5*vv)
    pol=S.Poly(formula(),a)
    H=S.Poly(pol.nth(2),r)
    Rstar=S.Rational(83,64)-S.Rational(75,16)*B-S.Rational(193,48)*C
    phi=S.expand(pol.nth(0)*D*D+2*D*pol.nth(1)+4*(H.nth(0)+r*H.nth(1)+r*r*Rstar))
    # The discarded r^2 term is a sum of a square and Bessel residuals.
    rem=S.expand(H.nth(2)-Rstar-3*(h+e/3)**2-f*f-(C-e*e)/3)
    assert rem==0
    rhoS=S.Rational(rho.numerator,rho.denominator)
    controls=[phi.subs(r,0),phi.subs(r,0)+rhoS*S.diff(phi,r).subs(r,0)/2,phi.subs(r,rhoS)]
    expected=[]
    for control in controls:
        out=rr.zero
        for powers,c in S.Poly(control,*sym).terms():
            ud=sum(p*d[0]for p,d in zip(powers,degrees));wd=sum(p*d[1]for p,d in zip(powers,degrees))
            assert ud%2==wd%2==0 and ud<=6 and wd<=4
            term=QQ(int(c.p),int(c.q))*t**(3-ud//2)*n**(2-wd//2)
            for base,power in zip(raw,powers):term*=base**power
            out+=term
        expected.append(out)
    from small_ratio_polynomial import construct
    assert tuple(expected)==construct(rho)[1]
    count=0
    for control,expect in zip(data['controls'],expected):
        assert not control['failed'];actual=rr.zero;seen=set();mons=control['monomials']
        assert len(mons)==6 and len({tuple(m)for m in mons})==6 and all(sum(m)==2 for m in mons)
        for rec in control['records']:
            mon=tuple(rec['monomial']);assert sum(mon)==10 and mon not in seen;seen.add(mon)
            rows=rec['matrix'];assert len(rows)==6 and all(len(row)==6 for row in rows)
            psd(rows);sc=F(rec['scale'])/rec['denominator'];assert rec['denominator']>0 and sc>0
            for i in range(6):
                for j in range(6):
                    full=mon+tuple(a+b for a,b in zip(mons[i],mons[j]));c=sc*rows[i][j]
                    actual+=rr.from_dict({full:QQ(c.numerator,c.denominator)})
            count+=1
        assert actual==expect
    print('PROVED: padded radial small-ratio bound reconstructed independently; all',count,'rational Gram matrices and coefficients checked.')
    print('PROVED: T6>=0 for every admissible scale whenever 0<r<=',rho,'(strict at smaller radial scales).')
if __name__=='__main__':main()
