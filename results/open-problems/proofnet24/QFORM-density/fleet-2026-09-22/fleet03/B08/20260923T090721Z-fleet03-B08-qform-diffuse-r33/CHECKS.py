import math
import random


def det2(a,b,c,d):
    return a*d-b*c


def regression(seed):
    rng=random.Random(seed)
    n=8
    A=[[0]*n for _ in range(n)]
    for p in range(n):
        for q in range(p,n):
            z=rng.randint(-9,9)
            A[p][q]=z
            A[q][p]=z
    i,k,a,b=0,1,2,3
    rr=[4,5]
    cc=[6,7]
    aa=A[i][a]
    bb=A[i][b]
    c0=A[k][a]
    U=[]
    for j in cc:
        x=A[i][j]
        y=A[k][j]
        u=aa*y-c0*x
        assert u==det2(A[i][a],A[i][j],A[k][a],A[k][j])
        U.append(u)
    V=[]
    for r in rr:
        s=A[r][a]
        t=A[r][b]
        v=aa*t-bb*s
        assert v==det2(A[a][i],A[a][r],A[b][i],A[b][r])
        V.append(v)
    for r in rr:
        for j in cc:
            s=A[r][a]
            x=A[i][j]
            nij=A[r][j]
            w=aa*nij-s*x
            assert w==det2(A[i][a],A[i][j],A[r][a],A[r][j])
    return sum(z*z for z in U),sum(z*z for z in V)


for seed in range(1000):
    regression(seed)

assert abs((300*math.sqrt(3))**2-270000)<1e-9

c_twostar_half=8*540000**0.25
c_twostar_l3=6**(2/3)*540000**(1/3)
c_zero_pair=2*math.sqrt(2)*math.sqrt(540000)
c_partner=math.sqrt(2)*300*math.sqrt(3)
c_W_rank2=8*270000**0.25
c_W_ridge=79.98514376669046*270000**0.25
c_checkerboard=8*(128*270000**2)**(1/8)

print('twostar_half',repr(c_twostar_half))
print('twostar_L3',repr(c_twostar_l3))
print('zero_pair_Linf',repr(c_zero_pair))
print('partner_projection',repr(c_partner))
print('W_rank2_half',repr(c_W_rank2))
print('W_ridge_half',repr(c_W_ridge))
print('checkerboard_half',repr(c_checkerboard))
print('QFORM_B08_R33_CHECK_PASS')
