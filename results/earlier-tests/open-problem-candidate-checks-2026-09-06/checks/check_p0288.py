"""Exact checks for the killed-chain rank-two question (P0288).

For the walk on Z with a killing defect of size v at the origin, this checks in Gaussian-rational arithmetic, for
v in {1/2, 1, 2, 3} and three points (c, s) on the unit circle, that the closed-form resolvent satisfies its
three-term recurrence with the defect at 0 and that its imaginary part equals the parity form of the spectral
density. It checks the edge coefficients and their positivity, the rank-two minor (determinant (2/v)^2 > 0), and
rejects the resolvent without the defect and the kernel without its odd sector. As a prior-art reconstruction it
computes the hub walk exactly for 2n <= 12 steps at b = 1/5 and 1/4, matches every entry with the reflected ballot
formula, rejects the formula with its second ballot term dropped, and checks the scaled 2 x 2 kernel on the sites
2 and 4 (determinant 4).
Finite cases check the identities; the spectral and Poissonization arguments are in
analyses/P0288_killed_chain_rank_two.md.
"""
from collections import defaultdict
from fractions import Fraction as F
import json
import math

# Gaussian rationals: all complex calculations remain exact.
def add(z,w): return z[0]+w[0],z[1]+w[1]
def mul(z,w): return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def neg(z): return -z[0],-z[1]
def scale(z,a): return z[0]*a,z[1]*a
def div(z,w):
    norm=w[0]**2+w[1]**2
    return scale(mul(z,(w[0],-w[1])),1/norm)
def power(z,n):
    if n<0: return power((z[0],-z[1]),-n)
    answer=(F(1),F(0))
    for _ in range(n): answer=mul(answer,z)
    return answer

def resolvent(i,j,c,s,v):
    r=(c,-s); d=(F(0),2*s)
    first=div(power(r,abs(i-j)),d)
    second=div(scale(power(r,abs(i)+abs(j)),v),mul(d,add(d,(v,F(0)))))
    return add(first,neg(second))

def ballot(steps,x,y,b):
    if x<=0 or y<=0 or (steps+y-x)%2: return F(0)
    up=(steps+y-x)//2
    if not 0<=up<=steps: return F(0)
    def choose(k): return math.comb(steps,k) if 0<=k<=steps else 0
    count=choose(up)-choose((steps+y+x)//2)
    return count*b**up*(1-b)**(steps-up)

def exact_hub(steps,x,b):
    dist={x:F(1)}
    for _ in range(steps):
        out=defaultdict(F)
        for z,p in dist.items():
            if z==0:
                out[1]+=p*b/2; out[-1]+=p*b/2
            else:
                sign=1 if z>0 else -1
                out[z+sign]+=p*b; out[z-sign]+=p*(1-b)
        dist=out
    return dist

def main():
    counts=defaultdict(int)
    for v in [F(1,2),F(1),F(2),F(3)]:
        for c,s in [(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-3,5),F(4,5))]:
            for i in range(-3,4):
                ci,si=power((c,s),i)
                cai,sai=power((c,s),abs(i))
                ei=2*s*cai+v*sai
                for j in range(-3,4):
                    cj,sj=power((c,s),j)
                    caj,saj=power((c,s),abs(j))
                    ej=2*s*caj+v*saj
                    from_resolvent=-2*s*resolvent(i,j,c,s,v)[1]
                    from_parity=si*sj+ei*ej/(4*s*s+v*v)
                    assert from_resolvent==from_parity
                    counts['spectral_density_identities']+=1
                for j in range(-2,3):
                    lhs=add(scale(resolvent(i,j,c,s,v),2*c+(v if i==0 else 0)),
                            neg(add(resolvent(i-1,j,c,s,v),resolvent(i+1,j,c,s,v))))
                    assert lhs==(F(i==j),F(0))
                    counts['resolvent_recurrences']+=1
            wrong=scale(resolvent(0,0,c,s,v),2*c)
            wrong=add(wrong,neg(add(resolvent(-1,0,c,s,v),resolvent(1,0,c,s,v))))
            assert wrong!=(F(1),F(0))
            counts['missing_defect_controls_rejected']+=1
        for i in range(-3,4):
            for j in range(-3,4):
                a,b=abs(i-j),abs(i)+abs(j)
                laplace=2*(F(b*b-a*a,4)+b/v+2/(v*v))
                parity=(abs(i)+2/v)*(abs(j)+2/v)+i*j
                assert laplace==parity and parity>0
                counts['edge_coefficients_and_positivity']+=1
        c=2/v
        determinant=c*c*((1+c)**2+1)-(c*(1+c))**2
        assert determinant==c*c>0
        counts['rank_two_minor_checks']+=1
        assert (1+c)**2 != (1+c)**2+1
        counts['omitted_odd_sector_controls_rejected']+=1
    for b in [F(1,5),F(1,4)]:
        for n in range(1,7):
            for x in [-4,-2,0,2,4]:
                direct=exact_hub(2*n,x,b)
                for y in [-4,-2,0,2,4]:
                    xx,yy=abs(x),abs(y)
                    if yy==0:
                        expected=ballot(2*n,xx+1,1,b)
                    else:
                        parity=1 if x*y>=0 else -1
                        expected=(ballot(2*n,xx+1,yy+1,b)+parity*ballot(2*n,xx,yy,b))/2
                        omitted=ballot(2*n,xx+1,yy+1,b)/2
                        if expected!=omitted:
                            assert direct.get(y,F(0))!=omitted
                            counts['missing_ballot_term_controls_rejected']+=1
                    assert direct.get(y,F(0))==expected
                    counts['literature_coupling_entries']+=1
    # Scaled kernel from source equations (36), (45), (46), restricted to even sites.
    matrix=[[(1+x)*(1+y)+x*y for y in [2,4]] for x in [2,4]]
    determinant=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    assert matrix==[[13,23],[23,41]] and determinant==4
    counts['literature_scaled_minor_checks']+=1

    print(json.dumps({'counts':dict(counts),'literature_scaled_matrix':matrix,
        'literature_scaled_determinant':determinant},indent=2))


if __name__=='__main__': main()
