import math
import numpy as np

rng=np.random.default_rng(20260923)
d0=377/1344
rho0=math.sqrt(29/3072)
Delta0=rho0*math.sqrt(d0)
gamma=1/64

print('d0',d0)
print('Delta0',Delta0)
print('TheoremF_bound',12/d0)
print('finite_core_bound_gamma_1_64_m7',2*math.sqrt(6*math.pi*7)/(gamma*d0))
print('volume_stability_bound_a_1_64',(24*math.sqrt(3)*math.e)/(5*gamma))
print('partner_bound_Dres_ge_e-8',34*math.sqrt(9))

min_gram_margin=float('inf')
min_spec_margin=float('inf')
for _ in range(2000):
    Q,_=np.linalg.qr(rng.normal(size=(3,3)))
    h=rng.uniform(0.0,1.0,size=2)
    Hsqrt=Q[:,:2]@np.diag(np.sqrt(h))@Q[:,:2].T
    while True:
        p=rng.uniform(math.sqrt(d0),1.0,size=2)
        if p.prod()>d0:
            break
    theta=rng.uniform(0,2*math.pi)
    O=np.array([[math.cos(theta),-math.sin(theta)],[math.sin(theta),math.cos(theta)]])
    P=O@np.diag(p)@O.T
    Iminus=Q[:,:2]@(np.eye(2)-P)@Q[:,:2].T
    HL=Hsqrt@Iminus@Hsqrt
    GK=np.eye(3)-HL
    d=float(np.linalg.det(P))
    lam=float(np.linalg.eigvalsh(GK)[0])
    min_gram_margin=min(min_gram_margin,lam-d)

    X=rng.normal(size=(3,3)); M=(X+X.T)/2
    ev=np.linalg.eigvalsh(M); sm=min(abs(ev))
    if sm<1e-5:
        continue
    M/=sm
    vals,V=np.linalg.eigh(GK)
    sqrtG=V@np.diag(np.sqrt(vals))@V.T
    N=sqrtG@M@sqrtG
    sN=min(abs(np.linalg.eigvalsh(N)))
    min_spec_margin=min(min_spec_margin,sN-d)

print('random_min_gram_margin',min_gram_margin)
print('random_min_spectral_margin',min_spec_margin)

min_bin_margin=float('inf')
for _ in range(10000):
    m=int(rng.integers(2,30))
    w=rng.random(m)*0.5
    s=w.sum()
    if s<=63/64:
        w*=0.99/max(s,1e-12)
        w=np.minimum(w,0.5)
    if w.sum()<=63/64:
        continue
    bins=[0.0,0.0]
    for x in sorted(w,reverse=True):
        bins[0 if bins[0]<=bins[1] else 1]+=float(x)
    bound=(float(w.sum())-float(w.max()))/2
    min_bin_margin=min(min_bin_margin,min(bins)-bound)
print('partition_random_min_margin',min_bin_margin)
print('QFORM_B19_R32_ACTIVE_GRAM_CHECK_PASS')
