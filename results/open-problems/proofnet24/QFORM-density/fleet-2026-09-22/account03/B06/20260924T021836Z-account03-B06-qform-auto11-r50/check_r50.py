import math
import numpy as np

rng=np.random.default_rng(202609240506)
J0=np.array([[0.0,-1.0],[1.0,0.0]])
N=3000
errs={
    "core_reconstruction":0.0,
    "rr_factor":0.0,
    "rr_simplified":0.0,
    "packet_Bz":0.0,
    "packet_kappa":0.0,
    "deletion_det":0.0,
}
min_cross_margin=float("inf")
pure_min_gap=float("inf")
used=0

for _ in range(N):
    X=rng.normal(size=(2,2))
    H=(X+X.T)/2
    if abs(np.linalg.det(H))<0.2:
        H=H+np.diag([1.3,-0.9])
    delta=np.linalg.det(H)
    if abs(delta)<1e-7:
        continue
    m=7
    E=rng.normal(size=(2,m))
    G=E@E.T
    W=np.linalg.det(G)
    if W<1e-7:
        continue
    v=rng.normal(size=2)
    v/=np.linalg.norm(v)
    lam=rng.normal()
    if abs(lam)<0.15:
        lam += 0.35 if lam>=0 else -0.35
    d=rng.normal(size=m)
    Hi=np.linalg.inv(H)
    U=Hi+lam*np.outer(v,v)

    R=np.zeros((3,m+2))
    R[:2,:2]=np.eye(2)
    R[:2,2:]=Hi@E
    R[2,2:]=v@E
    M3=np.zeros((3,3))
    M3[:2,:2]=H
    M3[2,2]=lam
    core=R.T@M3@R
    target=np.block([[H,E],[E.T,E.T@U@E]])
    den=1+np.linalg.norm(core)+np.linalg.norm(target)
    errs["core_reconstruction"]=max(
        errs["core_reconstruction"],np.linalg.norm(core-target)/den)

    detrr=np.linalg.det(R@R.T)
    rhs1=v@G@v + W*np.linalg.norm(Hi@J0@v)**2
    rhs2=v@G@v + W*np.linalg.norm(H@v)**2/delta**2
    errs["rr_factor"]=max(
        errs["rr_factor"],abs(detrr-rhs1)/(1+abs(detrr)+abs(rhs1)))
    errs["rr_simplified"]=max(
        errs["rr_simplified"],abs(detrr-rhs2)/(1+abs(detrr)+abs(rhs2)))

    j=int(rng.integers(m))
    ej=E[:,j]
    z=np.r_[-U@ej,1.0]
    Bj=np.block([[H,ej[:,None]],
                 [ej[None,:],np.array([[d[j]+ej@U@ej]])]])
    bz=Bj@z
    bz0=np.r_[-lam*(v@ej)*(H@v),d[j]]
    errs["packet_Bz"]=max(
        errs["packet_Bz"],
        np.linalg.norm(bz-bz0)/(1+np.linalg.norm(bz)+np.linalg.norm(bz0)))

    L=np.linalg.norm(z)
    r0=1+lam*(v@H@v)
    kap=(z@Bj@z)/L**2
    kap0=(d[j]+lam*r0*(v@ej)**2)/L**2
    errs["packet_kappa"]=max(
        errs["packet_kappa"],abs(kap-kap0)/(1+abs(kap)+abs(kap0)))

    idx=[k for k in range(m) if k!=j]
    EJ=E[:,idx]
    alpha=ej@np.linalg.inv(G)@ej
    WJ=np.linalg.det(EJ@EJ.T)
    WJ0=W*(1-alpha)
    errs["deletion_det"]=max(
        errs["deletion_det"],abs(WJ-WJ0)/(1+abs(WJ)+abs(WJ0)))

    Mc=np.vstack([EJ,(ej@U@EJ)[None,:]])
    sv=np.linalg.svd(Mc,compute_uv=False)
    cross=sv[0]*sv[1]
    min_cross_margin=min(min_cross_margin,cross-math.sqrt(max(WJ,0.0)))
    used+=1

for _ in range(1000):
    c=(1 if rng.random()<0.5 else -1)*10**rng.uniform(-4,2)
    H=np.array([[0.0,c],[c,0.0]])
    E=rng.normal(size=(2,7))
    G=E@E.T
    W=np.linalg.det(G)
    v=rng.normal(size=2)
    v/=np.linalg.norm(v)
    lam=(1 if rng.random()<0.5 else -1)*10**rng.uniform(-3,2)
    delta=np.linalg.det(H)
    P=abs(lam)*(abs(delta)*(v@G@v)+W*np.linalg.norm(H@v)**2/abs(delta))
    pure_min_gap=min(pure_min_gap,P-abs(lam)*W)

CE=3*2**(2/3)*(1.5+2*math.pi)
K=2*math.pi*math.sqrt(3*CE/2)
Csh=4/math.pi*(K/6)**(3/4)
Cbank=2**(3/8)*Csh

print(f"used_random_instances={used}")
for k,vv in errs.items():
    print(f"max_{k}_normalized_error={vv:.17g}")
print(f"minimum_cross_minus_sqrt_deleted_area={min_cross_margin:.17g}")
print(f"minimum_pure_hyperbolic_P_minus_abs_lambda_W={pure_min_gap:.17g}")
print(f"C_sh={Csh:.15f}")
print(f"C_sh_rightbank={Cbank:.15f}")
print(f"three_e={3*math.e:.15f}")
assert max(errs.values())<2e-11
assert min_cross_margin>-1e-10
assert pure_min_gap>-1e-9
assert Cbank<7.713
print("QFORM_B06_R50_CHECK_PASS")
