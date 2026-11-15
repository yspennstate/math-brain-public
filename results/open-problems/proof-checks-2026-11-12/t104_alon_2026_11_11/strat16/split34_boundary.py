"""Exact matrix coefficients for rank <=2 four-part and triangle corners."""
import itertools
import json
from pathlib import Path
import sympy as s
from concavity_certificate import is_psd
from split34_algebra import variables,triangle


def construct(corner,endpoint):
    rr,x,y,z,a,b,h=variables();k=5+h
    U=[3*x+2*y+z,-x+2*y+z,-x-2*y+z,-x-2*y-3*z];Rv=sum(v*v for v in U);p=-U[0]*U[3]
    G,H=(rr.zero,rr.one)if endpoint==0 else(Rv,4*p)
    K=[[rr.zero for j in range(2)]for i in range(4)]
    for c,j in enumerate((1,2)):
        K[0][c]=U[3]-U[j];K[j][c]=U[0]-U[3];K[3][c]=U[j]-U[0]
    W,R,D,L=triangle(rr,corner);tr=sum(L[i][i]for i in range(3));tr2=sum(L[i][j]**2 for i in range(3)for j in range(3))
    B=sum(W[i]*W[j]*(int(i==j)*D-L[i][j])**2 for i in range(3)for j in range(3))
    hn=sum(W[i]**2*L[i][i]for i in range(3))
    Y=-2*sum(L[i][j]*(W[i]-W[j])**2*(2*D-L[i][i]-L[j][j]+2*L[i][j])for i in range(3)for j in range(i+1,3))
    J=(D+tr)*H-G*D;massnum=(3*D+tr)*H-G*D
    const=2*G*(H-G)*Rv*Rv*k*k*D*D*R+2*(D*tr-tr2)*Rv*Rv*k*k*R*H*H
    const+=2*k*(k+2)*B*Rv*Rv*H*H-Y*Rv*Rv*k*k*H*H
    const+=J/2*(2*(k+1)*(k-2)*D*H*R-2*k*massnum*R+2*(k+2)*(QQ(3,4)*D*H*R+hn*H))*Rv*Rv
    F=[[const*int(i==j)+2*k*(k+2)*G*G*D*D*R*U[i]**2*U[j]**2
        -int(i==j)*(k+2)*G*J*D*R*Rv*U[i]**2 for j in range(4)]for i in range(4)]
    for i in range(4):
        for j in range(i+1,4):
            w=-2*G*k*k*D*D*R*(Rv*H/4+G*U[i]*U[j])*(U[i]-U[j])**2
            F[i][i]+=w;F[j][j]+=w;F[i][j]-=w;F[j][i]-=w
    M=[[sum(K[i][a]*F[i][j]*K[j][b]for i in range(4)for j in range(4))for b in range(2)]for a in range(2)]
    return rr,M


def coeffs(M):
    es=set().union(*(set(p)for row in M for p in row))
    return [(e,s.Matrix(2,2,[s.Rational(p.get(e,0))for row in M for p in row]))for e in sorted(es)]


def main():
    records=[]
    for corner in ('balanced','path'):
        for ep in (0,1):
            rr,M=construct(corner,ep);cs=coeffs(M);bad=[e for e,A in cs if not is_psd(A)]
            print(corner,ep,'matrices',len(cs),'not PSD',len(bad),flush=True)
            assert not bad
            # Pure gap axes and pure triangle flux axes prove strictness,
            # at both finite k and infinity. Denominators remain positive.
            vd=6 if ep==0 else 10
            for axis in range(3):
                for hp in (0,2):
                    for tri_axis in ((3,4)if corner=='path'else(-1,)):
                        mon=[0]*6;mon[axis]=vd;mon[5]=hp
                        if tri_axis>=0:mon[tri_axis]=6
                        A=s.Matrix(2,2,[s.Rational(p.get(tuple(mon),0))for row in M for p in row])
                        assert A[0,0]>0 and A.det()>0,(corner,ep,mon,A)
            records.append(dict(triangle=corner,endpoint=ep,matrices=len(cs),negative=0))
    Path('split34_boundary_checks.json').write_text(json.dumps(records,indent=2)+'\n')
    print('PROVED (split34_boundary.py): the four-part rank-at-most-two boundary is strictly positive, k>=5 and infinity.')


from sympy.polys.domains import QQ
if __name__=='__main__':main()
