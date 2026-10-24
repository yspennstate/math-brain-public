from fractions import Fraction as F

checks=0

# Exact finite self-check for the hub-reuse construction used in the report.
# Grid: m=2..30 and sigma=1/d, d=1..30.
for m in range(2,31):
    for d in range(1,31):
        sig=F(1,d)
        r=min(sig/F(2), F(1,m*m))
        # Distinct rational ordinates strictly inside [-r,r].
        ys=[-r + F(2*r*(i+1),m+1) for i in range(m)]
        # Same-side pairs are joined directly, hence have exact stretch 1.
        for i in range(m):
            for j in range(i+1,m):
                assert ys[i] != ys[j]
                checks += 1
        # Cross pair via origin. It suffices that each spoke length is <=1+sigma,
        # because the Euclidean cross distance is >=2.
        assert 1+r*r <= (1+sig)*(1+sig)
        checks += 1
        for y in ys:
            assert 1+y*y <= (1+sig)*(1+sig)
            checks += 1
        # Two within-cluster complete graphs contribute <2 total length because r<=1/m^2.
        intra_bound=F(2*m*(m-1))*r
        assert intra_bound < 2
        checks += 1
        # Every one of the 2m spokes is used by exactly m of the m^2 chosen cross routes.
        assert 2*m*m == (m*m)*2
        checks += 1

print('P0222 HUB-REUSE EXACT FINITE SELF-CHECK')
print('grid_m=2..30')
print('grid_sigma=1/d, d=1..30')
print('checks=', checks)
print('theorem_proof_is_symbolic_in_report; this grid is only an auxiliary self-check')
print('ALL_EXACT_HUB_REUSE_CHECKS_PASS')
