"""Exact finite-core self-checks for FOURIER_ALL_MEANS.md."""
from fractions import Fraction as F
from pathlib import Path
import json
import verify_fourier_extension as core
from verify_fourier_extension import Poly, count, identity, checks, logsum
from verify_shuffle_obstruction import enclose_decimal


def main():
    core.NN=8
    variables=[]
    for i in range(8):
        k=[0]*8;k[i]=1;variables.append(Poly({tuple(k):1}))
    a,b,x,y,c,d,u,v=variables
    lam=[a+x,b+y,a-x,b-y];slopes=[c+u,d+v,c-u,d-v]
    f=count(lam);g=[Poly() for _ in range(4)];h=[Poly() for _ in range(3)]
    for i in range(4):
        for k,p in enumerate(count([lam[j] for j in range(4) if j!=i])):g[k]+=slopes[i]*p
        for j in range(4):
            if j==i:continue
            for k,p in enumerate(count([lam[l] for l in range(4) if l not in [i,j]])):h[k]+=slopes[i]*slopes[j]*p
    def deriv(p):return sum(variables[4+i]*p.diff(i) for i in range(4))
    U=count([a+x,a-x]);V=count([b+y,b-y]);O=U[1]*V[1]/4
    P=(U[1]*V[1]+2*U[2]*V[0]+2*U[0]*V[2])/8
    atoms=[f[0],f[1]/4,P,O,f[3]/4,f[4]];multiplicities=[1,4,4,2,4,1]
    identity('pair count mass',f[2],4*P+2*O)
    identity('opposite atom upper bound identity',2*P-O,(U[2]*V[0]+U[0]*V[2])/2)
    identity('middle beta lower bound identity',f[2]**2-32*P*O,(4*P-2*O)**2)
    identity('general opposite acceleration',2*deriv(deriv(O))+h[1],4*c*d)
    for k in range(5):
        identity('general count derivative '+str(k),deriv(f[k]),(g[k-1] if k else 0)-(g[k] if k<4 else 0))
        identity('general count second derivative '+str(k),deriv(deriv(f[k])),(h[k] if k<3 else 0)-2*(h[k-1] if 1<=k<=3 else 0)+(h[k-2] if k>=2 else 0))
    coefficients=[h[0],h[1]-2*h[0],h[0]-h[1]+h[2]-4*c*d,-h[1]+4*c*d,h[1]-2*h[2],h[2]]
    for i,(p,m,w) in enumerate(zip(atoms,multiplicities,coefficients)):
        identity('frozen log coefficient '+str(i),m*deriv(deriv(p)),w)
    # Clear the positive denominators of the pair-layer Fisher identity.
    identity('Fisher excess identity',4*deriv(P)**2*O*f[2]+2*deriv(O)**2*P*f[2]-deriv(f[2])**2*P*O,8*(O*deriv(P)-P*deriv(O))**2)
    bases=[('49/100','49/100','48/100','47/100'),
           ('9/10','1/2','99/1000','19/50'),
           ('7/10','3/10','1/5','1/5'),
           ('3/5','2/5','1/100','3/100'),
           ('4/5','1/5','0','0'),
           ('1/2','1/2','1/10','1/5')]
    directions=[(0,0,1,1),(0,0,2,-3),(1,1,2,-1),(1,-1,0,0),(2,-1,1,3),(1,0,-1,2)]
    records=[]
    for base in bases:
        for velocity in directions:
            values=list(map(F,base))+list(map(F,velocity));cv,dv,uv,vv=map(F,velocity)
            ev=lambda p:p.at(values)
            fv=list(map(ev,f));gv=list(map(ev,g));hv=list(map(ev,h));av=list(map(ev,atoms))
            assert all(0<ev(p)<1 for p in lam)
            assert sum(m*p for m,p in zip(multiplicities,av))==1
            Pv,Ov=av[2:4];ff=fv[2]
            alpha_args=[av[1]**2/(av[0]*Pv),Pv*Ov/(av[1]*av[4]),av[4]**2/(av[5]*Pv)]
            beta_args=[16*Pv/ff,ff**2/(16*Pv*Ov),16*Pv/ff]
            assert all(z>=1 for z in alpha_args) and all(z>=2 for z in beta_args)
            count_fisher=sum(ev(deriv(p))**2/ev(p) for p in f)
            measured_fisher=sum(m*ev(deriv(p))**2/ev(p) for m,p in zip(multiplicities,atoms))
            excess=8*(Ov*ev(deriv(P))-Pv*ev(deriv(O)))**2/(Pv*Ov*ff)
            assert measured_fisher-count_fisher==excess
            Q=[gv[k]**2/fv[k]-2*gv[k]*gv[k+1]/fv[k+1]+gv[k+1]**2/fv[k+2] for k in range(3)]
            boundary=gv[0]**2/fv[1]+gv[3]**2/fv[3]
            assert count_fisher==boundary+sum(Q) and all(z>=0 for z in Q)
            for k in range(3):
                assert hv[k]*(fv[k+1]**2-fv[k]*fv[k+2])<=2*gv[k]*gv[k+1]*fv[k+1]-gv[k]**2*fv[k+2]-gv[k+1]**2*fv[k]
            full=logsum([(m*ev(deriv(deriv(p))),ev(p)) for m,p in zip(multiplicities,atoms)],measured_fisher)
            # Expanded identity (13); the symbolic check already compared all
            # log coefficients. This evaluates that identity independently.
            rewritten=logsum([(-hv[k],alpha_args[k]) for k in range(3)]+[(4*cv*dv,Ov/Pv)],excess+boundary+sum(Q))
            assert max(full[0],rewritten[0])<=min(full[1],rewritten[1])
            lower_terms=[(hv[k],beta_args[k]) if hv[k]>=0 else (-hv[k],alpha_args[k]) for k in range(3)]+[(4*cv*dv,Ov/Pv)]
            lower=logsum(lower_terms,excess+boundary)
            favorable=cv*dv*(Ov-Pv)>=0
            if favorable and not (values[2]==values[3]==0 and cv==dv==0):assert lower[0]>0
            assert full[0]>0 or (values[2]==values[3]==0 and cv==dv==0 and full[0]<=0<=full[1])
            records.append(dict(base=list(base),velocity=velocity,favorable_sign=favorable,full_negative_curvature=enclose_decimal(full),quantitative_lower_bound=enclose_decimal(lower)))
    out=dict(status='PASS: exact self-checks; not independent audits',polynomial_identity_count=len(checks),polynomial_identities=checks,rational_curvature_case_count=len(records),rational_curvature_cases=records)
    Path(__file__).with_name('fourier_all_means_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if not isinstance(v,list)},indent=2))


if __name__=='__main__':main()
