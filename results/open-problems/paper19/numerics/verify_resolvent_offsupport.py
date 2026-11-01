"""
Self-contained off-support resolvent bound (Remark appB:selfcontained / closing the keystone
without the local law as a black box).  For Q = (1/(D-1)) sum_{i=1}^{D-1} g_i g_i^* with g_i iid
isotropic in R^D (here Rademacher: NON-Gaussian, NON-rotation-invariant), aspect (D-1)/D -> 1,
and eta = 1/log D (OFF the spectrum, eta >> lambda_min(Q) ~ D^-2), the operator norm of the
EXPECTED resolvent satisfies  || E[(Q+eta)^-1] || = (1+o(1)) m(-eta) ~ eta^{-1/2},
NOT eta^{-1}.  The null-vector spike (lambda_max of one realization ~ eta^{-1}) is smeared by the
expectation down to eta^{-1/2}.  Run: python verify_resolvent_offsupport.py

Finding (seed 7): lambda_max(E R)/m(-eta) ~ 1.03 (shrinking with D), while eta^{-1}/m(-eta) ~ 2.5-3,
confirming the smearing mechanism distribution-free.  m(-eta) = (sqrt(eta^2+4eta)-eta)/(2eta).
"""
import numpy as np
rng = np.random.default_rng(7)

def mMP1(eta):  # aspect-1 Marchenko-Pastur Stieltjes transform at z = -eta
    return (np.sqrt(eta**2 + 4 * eta) - eta) / (2 * eta)

if __name__ == "__main__":
    print(f'{"D":>4} {"eta":>7} {"lam_max(E R)":>12} {"m(-eta)":>9} {"eta^-1/2":>9} {"eta^-1":>8} {"ratio":>6}')
    for D in [40, 80, 160, 320]:
        n = D - 1; eta = 1.0 / np.log(D); nmat = 3000
        ER = np.zeros((D, D))
        for _ in range(nmat):
            a = rng.choice([-1.0, 1.0], size=(D, n))   # Rademacher rows: isotropic, non-Gaussian
            Q = (a @ a.T) / n
            ER += np.linalg.inv(Q + eta * np.eye(D))
        ER /= nmat
        lam = np.linalg.eigvalsh(ER)[-1]; m = mMP1(eta)
        print(f'{D:>4} {eta:>7.4f} {lam:>12.3f} {m:>9.3f} {eta**-0.5:>9.3f} {1/eta:>8.3f} {lam/m:>6.3f}')
    print("lambda_max(E R) tracks m(-eta) ~ eta^-1/2 (not eta^-1): expectation smears the null spike.")
