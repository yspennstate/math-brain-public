"""Exact finite illustrations of the analytic C078 comparison lemmas.

All feasibility, atom, channel, Fisher, and characteristic-polynomial assertions
use rational arithmetic. Decimal entropy values are explicitly illustrations.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import mpmath as mp


def det(a):
    n=len(a)
    if n==0:return Q(1)
    return sum(((-1)**j)*a[0][j]*det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(n))


def transpose(a):return [list(x) for x in zip(*a)]
def mm(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,x):return [sum(u*v for u,v in zip(row,x)) for row in a]
def minus(a,b):return [[u-v for u,v in zip(rowa,rowb)] for rowa,rowb in zip(a,b)]


def atoms(d,r,q):
    out=[]
    for s in range(8):
        a=[d[i]-(0 if (s>>i)&1 else 1) for i in range(3)]
        sign=(-1)**(3-s.bit_count())
        out.append(sign*(a[0]*a[1]*a[2]-sum(a[i]*r[i] for i in range(3))+q))
    return out


def fiber_matrix(d):
    return [[-((-1)**(3-s.bit_count()))*(d[i]-(0 if (s>>i)&1 else 1)) for i in range(3)] for s in range(8)]


def fisher(d,r,q):
    p=atoms(d,r,q);b=fiber_matrix(d)
    return [[sum(b[s][i]*b[s][j]/p[s] for s in range(8)) for j in range(3)] for i in range(3)]


def psd_minors(a):
    out=[]
    for size in range(1,len(a)+1):
        for inds in combinations(range(len(a)),size):
            value=det([[a[i][j] for j in inds] for i in inds])
            assert value>=0,(inds,value)
            out.append((list(inds),str(value)))
    return out


def strict_feasible(d,r,q):
    assert all(0<x<1 for x in d)
    assert all(x>=0 for x in r)
    assert q*q<=4*r[0]*r[1]*r[2]
    minors_k=[*d];minors_c=[1-x for x in d]
    for i in range(3):
        j,k=[x for x in range(3) if x!=i]
        minors_k.append(d[j]*d[k]-r[i])
        minors_c.append((1-d[j])*(1-d[k])-r[i])
    minors_k.append(d[0]*d[1]*d[2]-sum(d[i]*r[i] for i in range(3))+q)
    minors_c.append((1-d[0])*(1-d[1])*(1-d[2])-sum((1-d[i])*r[i] for i in range(3))-q)
    assert min(minors_k)>0 and min(minors_c)>0
    p=atoms(d,r,q)
    assert min(p)>0 and sum(p)==1
    for i in range(3):assert sum(p[s] for s in range(8) if s>>i&1)==d[i]
    for i in range(3):
        j,k=[x for x in range(3) if x!=i]
        assert sum(p[s] for s in range(8) if s>>j&1 and s>>k&1)==d[j]*d[k]-r[i]
    return {'K_principal_minors':list(map(str,minors_k)),'I_minus_K_principal_minors':list(map(str,minors_c)),'atom_min':str(min(p))}


def atom_channel(dmix):
    out=[[Q(i==j) for j in range(8)] for i in range(8)]
    for inds in ([1,2,4],[6,5,3]):
        for i in range(3):
            for j in range(3):out[inds[i]][inds[j]]=dmix[i][j]
    return out


def charpoly(d,r,q):
    assert d[0]==d[1]==d[2]
    x=d[0];t=sum(r)
    return [Q(1),-3*x,3*x*x-t,-(x*x*x-x*t+q)]


def dec(x):return mp.mpf(x.numerator)/x.denominator
def entropy(p):return -sum(dec(x)*mp.log(dec(x)) for x in p)


def main():
    mp.mp.dps=70
    d=[Q(9,20)]*3
    r=[Q(1,25),Q(1,36),Q(1,16)]
    q=Q(1,480)
    dmix=[[Q(1,2),Q(0),Q(1,2)],[Q(0),Q(1),Q(0)],[Q(1,2),Q(0),Q(1,2)]]
    rbar=mv(dmix,r)
    swapped=[r[2],r[1],r[0]]
    radial=[x/4 for x in r]
    unequal_d=[Q(43,100),Q(51,100),Q(61,100)]
    allones=[[Q(1,3)]*3 for _ in range(3)]
    balanced=mv(allones,r)
    result={'status':'exact rational assertions passed; decimals below are illustrations','q':str(q),'r':list(map(str,r))}
    for label,dd,rr in [('base',d,r),('pair_balanced',d,rbar),('fully_balanced',d,balanced),('radial_real_cycle',d,radial),('unequal_diagonal',unequal_d,r),('unequal_diagonal_radial',unequal_d,radial)]:
        result[label]=strict_feasible(dd,rr,q)
    assert 4*radial[0]*radial[1]*radial[2]==q*q
    assert 4*r[0]*r[1]*r[2]==64*q*q
    assert charpoly(d,r,q)==charpoly(d,rbar,q)==charpoly(d,balanced,q)
    result['common_characteristic_polynomial']=list(map(str,charpoly(d,r,q)))
    p=atoms(d,r,q);pbar=atoms(d,rbar,q);pbal=atoms(d,balanced,q)
    channel=atom_channel(dmix)
    assert mv(channel,p)==pbar
    assert mm(channel,fiber_matrix(d))==mm(fiber_matrix(d),dmix)
    assert mv(atom_channel(allones),p)==pbal
    for rr in (rbar,balanced):assert rr[0]*rr[1]*rr[2]>=r[0]*r[1]*r[2]
    g=fisher(d,r,q);gbar=fisher(d,rbar,q);gswap=fisher(d,swapped,q)
    channel_loss=minus(g,mm(transpose(dmix),mm(gbar,dmix)))
    result['channel_fisher_loss_principal_minors']=psd_minors(channel_loss)
    avg_g=[[ (g[i][j]+gswap[i][j])/2 for j in range(3)] for i in range(3)]
    result['matrix_convex_fisher_gap_principal_minors']=psd_minors(minus(avg_g,gbar))
    # Exact score-variance identity for a non-count-preserving tangent.
    x=[Q(2),Q(-1),Q(3)]
    u=mv(fiber_matrix(d),x);ubar=mv(channel,u)
    lhs=sum(u[s]*u[s]/p[s] for s in range(8))-sum(ubar[s]*ubar[s]/pbar[s] for s in range(8))
    rhs=sum(channel[i][j]*p[j]*(u[j]/p[j]-ubar[i]/pbar[i])**2 for i in range(8) for j in range(8))
    assert lhs==rhs and lhs>0
    result['exact_score_variance_gap']=str(lhs)
    # A genuinely unequal-diagonal fiber chord gives exact atom mixtures.
    t=Q(2,5);rmix=[(1-t)*r[i]+t*radial[i] for i in range(3)]
    p0=atoms(unequal_d,r,q);p1=atoms(unequal_d,radial,q)
    assert atoms(unequal_d,rmix,q)==[(1-t)*a+t*b for a,b in zip(p0,p1)]
    strict_feasible(unequal_d,rmix,q)
    # Exact pair-imbalance Fisher monotonicity, with a fixed imbalance tangent.
    xpair=[Q(1),Q(0),Q(-1)]
    def quad(a,x):return sum(xi*yi for xi,yi in zip(x,mv(a,x)))
    assert quad(g,xpair)>quad(gbar,xpair)>0
    result['pair_imbalance_fisher']={'before':str(quad(g,xpair)),'after':str(quad(gbar,xpair))}
    result['decimal_entropy_illustrations']={
        'original_equal_diagonal':mp.nstr(entropy(p),45),
        'pair_balanced_gain':mp.nstr(entropy(pbar)-entropy(p),45),
        'fully_balanced_gain':mp.nstr(entropy(pbal)-entropy(p),45),
        'radial_real_cycle_gain':mp.nstr(entropy(atoms(d,radial,q))-entropy(p),45),
        'unequal_diagonal_radial_gain':mp.nstr(entropy(p1)-entropy(p0),45),
    }
    dest=Path(__file__).with_name('results.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
