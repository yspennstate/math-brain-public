from fractions import Fraction as F
from itertools import permutations
from functools import reduce


def q(re=0, im=0): return (F(re), F(im))
def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0], -z[1])
def smul(s,z): return (s*z[0], s*z[1])
def sgn(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)) % 2 else 1

def det4(M):
    out=q()
    for p in permutations(range(4)):
        t=q(1)
        for i,j in enumerate(p): t=mul(t,M[i][j])
        out=add(out,smul(F(sgn(p)),t))
    return out

def outer(v,w): return [[mul(v[i],conj(w[j])) for j in range(4)] for i in range(4)]
def madd(X,Y): return [[add(X[i][j],Y[i][j]) for j in range(4)] for i in range(4)]
def mscale(z,X): return [[mul(z,X[i][j]) for j in range(4)] for i in range(4)]

# Exact account03/B08 r11 stress point.
U=[
 [F(-64884,690625),F(147,3125),F(-41416,138125),F(-7704,8125)],
 [F(118503,690625),F(3076,3125),F(4872,138125),F(168,8125)],
 [F(668888,690625),F(-504,3125),F(-25413,138125),F(-372,8125)],
 [F(-106296,690625),F(168,3125),F(-129204,138125),F(2549,8125)],
]
a=[q(3,3),q(-4,-5),q(2,5),q(5,4)]
b=[q(-1,-2),q(5,5),q(5,3),q(5,2)]
cols=[[q(U[i][j]) for i in range(4)] for j in range(4)]
Acoef,Bcoef=F(-985),F(-12348)
def L(z): return Acoef*z[0]+Bcoef*z[1]

def pair_projector(p,r,kind):
    up,ur=cols[p],cols[r]
    Pp,Pr=outer(up,up),outer(ur,ur)
    C,Ch=outer(up,ur),outer(ur,up)
    if kind=='p': return Pp
    if kind=='r': return Pr
    out=[[q() for _ in range(4)] for __ in range(4)]
    for i in range(4):
        for j in range(4):
            if kind=='plus':
                out[i][j]=smul(F(1,2),add(add(Pp[i][j],Pr[i][j]),add(C[i][j],Ch[i][j])))
            elif kind=='iplus':
                out[i][j]=smul(F(1,2),add(add(Pp[i][j],Pr[i][j]),add(mul(q(0,-1),C[i][j]),mul(q(0,1),Ch[i][j]))))
    return out

def det_pair(p,r,Pv):
    X=[[q() for _ in range(4)] for __ in range(4)]
    for i in range(4): X[i][i]=a[i]
    for k in range(4):
        if k not in (p,r): X=madd(X,mscale(b[k],outer(cols[k],cols[k])))
    PW=madd(outer(cols[p],cols[p]),outer(cols[r],cols[r]))
    X=madd(X,mscale(b[r],PW))
    X=madd(X,mscale(sub(b[p],b[r]),Pv))
    return det4(X)

# One-based pair (2,4). Reconstruct the off-diagonal entry of the exact
# Hermitian support compression from four rank-one projectors.
p,r=1,3
Dp=det_pair(p,r,pair_projector(p,r,'p'))
Dr=det_pair(p,r,pair_projector(p,r,'r'))
Dplus=det_pair(p,r,pair_projector(p,r,'plus'))
Diplus=det_pair(p,r,pair_projector(p,r,'iplus'))
hp,hr,hplus,hiplus=map(L,(Dp,Dr,Dplus,Diplus))
re12=hplus-(hp+hr)/2
im12=(hp+hr)/2-hiplus
assert re12>0 and im12==0
assert 2*re12 == F(9452115645066623088,11924072265625)

# Exact column-label orbit barycenter equals the permutation-vertex barycenter.
def det_label_perm(p):
    B=[[q() for _ in range(4)] for __ in range(4)]
    for j in range(4): B=madd(B,mscale(b[j],outer(cols[p[j]],cols[p[j]])))
    M=[[B[i][j] for j in range(4)] for i in range(4)]
    for i in range(4): M[i][i]=add(M[i][i],a[i])
    return det4(M)
Ds=[det_label_perm(p) for p in permutations(range(4))]
V=[reduce(mul,[add(a[i],b[p[i]]) for i in range(4)],q(1)) for p in permutations(range(4))]
avgD=(sum(z[0] for z in Ds)/24,sum(z[1] for z in Ds)/24)
avgV=(sum(z[0] for z in V)/24,sum(z[1] for z in V)/24)
assert avgD==avgV==(F(9620,3),F(2677,6))

print('PASS exact pair-compression/orbit-barycenter checks')
print('pair_24_support_current =',hp)
print('pair_24_support_swapped =',hr)
print('pair_24_H12_real =',re12)
print('pair_24_H12_imag =',im12)
print('pair_24_directional_derivative_phi0 =',2*re12)
print('orbit_average_det =',avgD)
print('orbit_average_vertex =',avgV)
print('orbit_average_support =',L(avgD))
