import numpy as np, math

rng=np.random.default_rng(43011)
beta=289/15984
a0=beta/16
eta=math.sqrt(191)/16*beta
theta=eta/2

assert abs(beta - 0.01808058058058058) < 1e-15
assert abs((3/4 - 1/256)*beta**2 - eta**2) < 1e-18
assert abs(theta - eta/2) < 1e-18

min_area2 = float("inf")
heavy_pairs = 0
max_star_err = 0.0
for n in (4,5,6,8):
    for _ in range(1000):
        E=np.linalg.qr(rng.normal(size=(n,3)))[0][:,:3]
        P=E@E.T
        q=np.diag(P)
        inds=np.where(q>0.75)[0]
        for aa in range(len(inds)):
            for bb in range(aa+1,len(inds)):
                i,j=inds[aa],inds[bb]
                area2=q[i]*q[j]-P[i,j]**2
                min_area2=min(min_area2,area2)
                heavy_pairs += 1
                assert area2 > 0.5 - 1e-12

        O=np.linalg.qr(rng.normal(size=(3,3)))[0]
        C=O@np.diag([1.3,2.1,-1.1])@O.T
        for i in range(n):
            z=E[i]
            v=C@z
            a=z@v
            lhs=np.linalg.norm(E[np.arange(n)!=i]@v)**2
            rhs=np.linalg.norm(v)**2-a*a
            max_star_err=max(max_star_err,abs(lhs-rhs))

assert max_star_err < 1e-10
partnerC=256/beta
pivotC=128*(64/(3*beta**2))**0.25
edge_scalar=256/math.sqrt(theta)
edge_pair=8*math.sqrt(5)*((45/64)*theta**3)**(-0.25)

print(f"beta0={beta:.15f}")
print(f"eta0={eta:.15f}")
print(f"theta0={theta:.15f}")
print(f"two-heavy partner coefficient={partnerC:.12f}")
print(f"scalar-pivot coefficient={pivotC:.12f}")
print(f"strong-edge scalar coefficient={edge_scalar:.12f}")
print(f"strong-edge pair-log coefficient={edge_pair:.12f}")
print(f"heavy_pairs_checked={heavy_pairs}")
print(f"minimum_E_frame_area_squared={min_area2:.15f}")
print(f"maximum_star_identity_error={max_star_err:.3e}")
print("QFORM_B11_R43_UNIQUE_HEAVYROW_CHECK_PASS")
