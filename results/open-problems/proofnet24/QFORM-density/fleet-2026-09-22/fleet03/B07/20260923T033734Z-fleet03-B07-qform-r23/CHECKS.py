from fractions import Fraction
import itertools

# Exact deterministic diagnostics for fleet03/B07 r23.
# These checks do not replace the analytic proofs in REPORT.md.

def matrix_checks(entries,m,n):
    M=[list(map(int,entries[r*n:(r+1)*n])) for r in range(m)]
    F2=sum(x*x for row in M for x in row)
    if F2==0:
        return 0
    tested=0
    for i in range(m):
        for a in range(n):
            alpha2=sum(M[i][j]**2 for j in range(n))
            beta2=sum(M[k][a]**2 for k in range(m))
            b=M[i][a]
            # Failure of |b| > alpha beta /(4F), squared without radicals.
            if 16*b*b*F2 <= alpha2*beta2:
                tested += 1
                r2=alpha2-b*b
                c2=beta2-b*b
                # ||r|| ||c|| >= 15 alpha beta /16, squared.
                assert 256*r2*c2 >= 225*alpha2*beta2
                Z=0
                for k in range(m):
                    if k==i:
                        continue
                    for j in range(n):
                        if j==a:
                            continue
                        det=b*M[k][j]-M[k][a]*M[i][j]
                        Z += det*det
                # sqrt(Z) >= 11 alpha beta /16, squared.
                assert 256*Z >= 121*alpha2*beta2
    return tested

nonedge=0
for m,n in [(2,2),(2,3),(3,2)]:
    for entries in itertools.product([-1,0,1], repeat=m*n):
        nonedge += matrix_checks(entries,m,n)

# theta=eta=1/16 low-tail dichotomy on exact integer spectra.
spectra=0
for d in range(3,7):
    for vals0 in itertools.combinations_with_replacement(range(9),d):
        vals=tuple(sorted(vals0,reverse=True))
        S=sum(vals)
        if S==0:
            continue
        T=sum(vals[2:])
        if 16*T >= S:
            continue
        spectra += 1
        lam2=vals[1]
        if 16*lam2 < S:
            # lambda_2+T < S/8.
            assert 8*(lam2+T) < S
        else:
            E2=sum(vals[i]*vals[j]
                   for i in range(d) for j in range(i+1,d))
            # E2 >= 7 S^2 /128.
            assert 128*E2 >= 7*S*S

# Exact collar constants.
theta=Fraction(1,16)
rho2=theta/Fraction(450,1)
assert Fraction(15,16)*rho2 == Fraction(1,7680)
assert Fraction(11,16)*rho2 == Fraction(11,115200)
# kappa^2=1/(256^2*3); 960/(theta*kappa^2).
projection_cap=960*16*(256**2*3)
assert projection_cap==3019898880

print(f"bicore_nonedge_cases={nonedge}")
print(f"lowtail_spectra={spectra}")
print("theta=eta=1/16")
print("inner_star_relative_product=1/7680")
print("sqrt_Z_relative=11/115200")
print(f"projection_cap_at_Lambda1={projection_cap}")
print("STATUS=PASS")
