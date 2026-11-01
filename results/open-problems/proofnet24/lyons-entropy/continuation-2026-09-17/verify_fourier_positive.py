"""Exact self-checks for the full Fourier Hessian at nonnegative imbalance."""
from fractions import Fraction as F
from pathlib import Path
import json
import verify_fourier_extension as core
from verify_fourier_barriers import fourier_jets,curvature,count
from verify_fourier_extension import logsum
from verify_shuffle_obstruction import enclose_decimal


def main():
    # Rational end comparisons used by the all-rho analytic lemma.
    assert 1+F(8,5)+F(8,5)**2/2+F(8,5)**3/6==F(1711,375)>F(9,2)
    assert 1+F(4,5)+F(4,5)**2/2>2
    core.NN=8
    variables=[]
    for i in range(8):
        k=[0]*8;k[i]=1;variables.append(core.Poly({tuple(k):1}))
    a,b,x,y,c,d,u,v=variables;lam=[a+x,b+y,a-x,b-y];slopes=[c+u,d+v,c-u,d-v]
    h=[core.Poly() for _ in range(3)]
    for i in range(4):
        for j in range(4):
            if i==j:continue
            for k,p in enumerate(core.count([lam[l] for l in range(4) if l not in [i,j]])):h[k]+=slopes[i]*slopes[j]*p
    core.identity('sum of count accelerations',sum(h),2*c*c+2*d*d+8*c*d-2*u*u-2*v*v)
    bases=[('1/2','1/2','2/5','2/5'),('1/2','1/2','-49/100','49/100'),('7/10','2/5','29/100','7/20'),('9/10','4/5','2/25','19/100'),('3/5','2/5','1/4','1/5'),('49/100','49/100','1/100','2/100'),('7/10','3/10','1/5','1/5'),('19/20','1/20','1/50','3/100'),('4/5','1/10','3/100','1/25')]
    directions=[(1,-1,0,0),(-5,2,-1,2),(2,-1,3,-2),(1,1,-1,2),(0,0,1,-1)]
    records=[]
    for base in bases:
        aa,bb,xx,yy=map(F,base);ll=[aa+xx,bb+yy,aa-xx,bb-yy]
        assert all(0<t<1 for t in ll)
        for direction in directions:
            cc,dd,uu,vv=map(F,direction);sl=[cc+uu,dd+vv,cc-uu,dd-vv]
            bits,atoms=fourier_jets(ll,sl);lookup=dict(zip(bits,atoms))
            P=lookup[(1,1,0,0)];O=lookup[(1,0,1,0)];p0=lookup[(0,0,0,0)][0];p4=lookup[(1,1,1,1)][0]
            c1=lookup[(1,0,0,0)][0];c3=lookup[(1,1,1,0)][0];f=count(ll)
            assert O[0]<=2*P[0]
            positive_imbalance=O[0]>=P[0]
            shifted=([c1*c1/(p0*O[0]),P[0]*P[0]/(c1*c3),c3*c3/(p4*O[0])] if positive_imbalance else [c1*c1/(p0*P[0]),P[0]*O[0]/(c1*c3),c3*c3/(p4*P[0])])
            assert all(t>=1 for t in shifted)
            gv=[F(0)]*4;hv=[F(0)]*3
            for i in range(4):
                for k,p in enumerate(count([ll[j] for j in range(4) if j!=i])):gv[k]+=sl[i]*p
                for j in range(4):
                    if i==j:continue
                    for k,p in enumerate(count([ll[l] for l in range(4) if l not in [i,j]])):hv[k]+=sl[i]*sl[j]*p
            Q=[gv[k]**2/f[k]-2*gv[k]*gv[k+1]/f[k+1]+gv[k+1]**2/f[k+2] for k in range(3)]
            for k in range(3):
                assert f[k+1]**2/(f[k]*f[k+2]*shifted[k])>=2
                local=logsum([(-hv[k],shifted[k])],F(3,5)*Q[k])
                assert local[0]>=0
            count_fisher=gv[0]**2/f[1]+gv[3]**2/f[3]+sum(Q)
            variance=sum(t*(1-t) for t in ll)
            assert variance<=1 and count_fisher*variance>=4*(cc+dd)**2
            excess=8*(O[0]*P[1]-P[0]*O[1])**2/(P[0]*O[0]*f[2])
            if positive_imbalance:
                coeff=2*(uu*uu+vv*vv-(cc+dd)**2);constant=F(8,5)*(cc+dd)**2+excess
            else:
                assert logsum([(variance,P[0]/O[0])])[1]<F(8,5)
                coeff=4*cc*dd;constant=F(8,5)/variance*(cc+dd)**2+excess
            lower=logsum([(coeff,O[0]/P[0])],constant)
            full=curvature(atoms)
            gap=logsum([(2*p[2],p[0]) for p in atoms]+[(-coeff,O[0]/P[0])],sum(p[1]**2/p[0] for p in atoms)-constant)
            assert lower[0]>=0 and gap[0]>0
            records.append(dict(base=list(base),direction=direction,full_negative_curvature=enclose_decimal(full),proved_lower_bound=enclose_decimal(lower),positive_remainder=enclose_decimal(gap)))
    out=dict(status='PASS: exact self-checks; full Fourier Hessian proved on the stated atom-ratio domain',polynomial_identities=core.checks,rational_scalar_comparisons=2,rational_curvature_cases=records)
    Path(__file__).with_name('fourier_positive_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status=out['status'],polynomial_identity_count=len(core.checks),rational_scalar_comparisons=2,rational_curvature_case_count=len(records)),indent=2))


if __name__=='__main__':main()
