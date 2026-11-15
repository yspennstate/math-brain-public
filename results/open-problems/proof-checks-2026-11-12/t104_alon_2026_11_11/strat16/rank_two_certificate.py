"""Exact low-rank boundary certificate, selected top vector arbitrary."""
import itertools
import time
import json
from pathlib import Path
import sympy as s
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
from concavity_certificate import is_psd


def construct(g):
    rr,x,y,z,t,h=ring('x,y,z,t,h',QQ)
    gaps=(x,y,z,t);k=5+h
    U=[sum((5-j if i<j else -j)*gaps[j-1]for j in range(1,5))for i in range(5)]
    R=sum(a*a for a in U);p=-U[0]*U[4]
    K=[[rr.zero for j in range(3)]for i in range(5)]
    for c,j in enumerate(range(1,4)):
        K[0][c]=U[4]-U[j];K[j][c]=U[0]-U[4];K[4][c]=U[j]-U[0]
    # g=G/H; denominator 5 handled in QQ.
    G,H=(rr(g),rr.one)if isinstance(g,int)else (R,5*p)
    # Matrix k^2 R^2 H^2 F, with F derived directly from (1).
    # M=(5-g)/2, M-1=(3-g)/2.
    constant=2*G*(H-G)*k*k*R*R+(3*H-G)/2*((2*(k+1)*(k-2)-10*k+s.Rational(13,5)*(k+2))*H+2*k*G)*R*R
    F=[[constant*int(i==j)+2*k*(k+2)*G*G*U[i]**2*U[j]**2
        -int(i==j)*(3*H-G)*(k+2)*G*R*U[i]**2
        for j in range(5)]for i in range(5)]
    for i in range(5):
        for j in range(i+1,5):
            a=-2*G*k*k*(R*H/5+G*U[i]*U[j])*(U[i]-U[j])**2
            F[i][i]+=a;F[j][j]+=a;F[i][j]-=a;F[j][i]-=a
    M=[[sum(K[i][a]*F[i][j]*K[j][b]for i in range(5)for j in range(5))for b in range(3)]for a in range(3)]
    return rr,M


def coefficients(M):
    n=len(M);es=set().union(*(set(p)for row in M for p in row))
    return [(e,s.Matrix(n,n,[s.Rational(p.get(e,0))for row in M for p in row]))for e in sorted(es)]


def main():
    tick=time.monotonic();records=[]
    for gap in (0,'max'):
        rr,M=construct(gap)
        coeff=coefficients(M);bad=[e for e,A in coeff if not is_psd(A)]
        print('g',gap,'raw',len(coeff),'not PSD',len(bad),flush=True)
        rec=dict(gap=gap,raw_count=len(coeff),raw_failed=len(bad),cones=[])
        degree=6 if gap==0 else 10
        for hpower in (0,2):
            for axis in range(4):
                mon=tuple((degree if i==axis else 0)if i<4 else hpower for i in range(5))
                A=s.Matrix(3,3,[s.Rational(p.get(mon,0))for row in M for p in row])
                assert all(A[:j,:j].det()>0 for j in range(1,4)),(gap,axis,hpower,A)
        rec['strict_pure_axes_finite_and_infinity']=8
        if bad:
            for perm in itertools.permutations(range(4)):
                dest,*gens=ring('a,b,c,d,h',QQ);repl=[None]*5;repl[4]=gens[4]
                for j,i in enumerate(perm):repl[i]=sum(gens[j:4])
                powers=[[a**j for j in range(11)]for a in repl]
                def compose(p):
                    out=dest.zero
                    for m,c in p.items():
                        a=dest(c)
                        for j,e in enumerate(m):a*=powers[j][e]
                        out+=a
                    return out
                MM=[[compose(p)for p in row]for row in M]
                cs=coefficients(MM);fails=[e for e,A in cs if not is_psd(A)]
                rec['cones'].append(dict(permutation=perm,count=len(cs),failed=len(fails)))
                print('g',gap,perm,'not PSD',len(fails),flush=True)
        records.append(rec)
    Path('rank_two_checks.json').write_text(json.dumps(dict(checks=records,seconds_NUMERICAL=time.monotonic()-tick),indent=2)+'\n')
    assert all((not r['raw_failed']or all(not c['failed']for c in r['cones']))for r in records if r['gap']in(0,'max'))
    print('PROVED (rank_two_certificate.py): rank-at-most-two boundary strict positivity for k>=5 and infinity.')

if __name__=='__main__':main()
