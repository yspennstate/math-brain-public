import math
import numpy as np

# Deterministic constants in QFORM-ANISOTROPIC-THREE-SHIELD-LEAKAGE-STABILITY-v1.
mu0 = 3.0
rho0 = 1.0/3.0
eta = 0.25
epsilon = 0.25
mu = mu0-epsilon
rho_bar = (rho0*mu0+eta)/mu
ell = (math.sqrt(rho_bar*rho_bar+4.0)-rho_bar)/2.0
gamma = mu*ell*ell
gamma_exact = (267.0-5.0*math.sqrt(509.0))/88.0
density_bound = 2.0*math.sqrt(30.0*math.pi)/gamma
claude_volume_constant = 24.0*math.sqrt(3.0)*math.e/5.0

assert abs(gamma-gamma_exact) < 1e-12
assert gamma > 1.0
assert claude_volume_constant < 23.0

# Finite sanity check only: this is not part of the proof.
# H=[[G,C0+F],[(C0+F)^T,D0+EZ]], with G arbitrary and
# ||F||op,||EZ||op <=1/4.  The theorem says s_3(H)>=gamma.
rng = np.random.default_rng(12345)
C0 = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0]])
D0 = np.diag([3.0,-3.0,3.0])
min_ratio = float('inf')
trials = 10000
for _ in range(trials):
    F = rng.normal(size=(2,3))
    op = np.linalg.norm(F, 2)
    if op:
        F *= rng.random()*0.25/op

    R = rng.normal(size=(3,3))
    EZ = (R+R.T)/2.0
    op = np.linalg.norm(EZ, 2)
    if op:
        EZ *= rng.random()*0.25/op

    Rg = rng.normal(size=(2,2))
    G = (Rg+Rg.T)/2.0
    G *= 10.0**rng.uniform(-6.0, 6.0)

    H = np.block([[G, C0+F], [(C0+F).T, D0+EZ]])
    singular_values = np.linalg.svd(H, compute_uv=False)
    ratio = singular_values[2]/gamma
    min_ratio = min(min_ratio, ratio)
    assert ratio >= 1.0-1e-10

print({
    'mu': mu,
    'rho_bar': rho_bar,
    'ell': ell,
    'gamma': gamma,
    'density_bound': density_bound,
    'claude_volume_constant': claude_volume_constant,
    'trials': trials,
    'minimum_sampled_s3_over_gamma': min_ratio,
})
