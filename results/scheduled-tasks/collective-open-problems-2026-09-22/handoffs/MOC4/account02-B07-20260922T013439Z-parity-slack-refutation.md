# MOC4 handoff — account02/B07 — structured parity-slack gate refuted

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T013439Z-b07-moc4-r11a`  
Outcome: **`CANDIDATE_REFUTED`** for lead intermediate `MOC4-PARITY-SLACK-v1`; parent MOC4 remains OPEN.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `yspennstate/math-open-problems`, `proofnet24/collective-MOC4/account02/B07/20260922T013439Z-b07-moc4-r11a/REPORT.md`, report commit `6f301bb432edb21916f1cfce18f00bca688345ce`, report blob `a1d129f8e4e173edab2d12e64a020bdd4d0210c1`. Exact verifier blob `805f3a362549b61e96ebdb0ce07fc586164f2e98`; exact output blob `da68cca858e07ba9ff71fb0f0275b975b3077066`.

## What was refuted

Lead account03/B07 r12 reduced the exact mixed support inequality to six signed-permutation fibers and proposed the sufficient gate

`2 sum_rho lambda_rho m_rho(K) <= sum_ij (R_ij |K_ij| - D_ij K_ij)`

for some Birkhoff decomposition `R=sum lambda_rho R_rho`. It asked whether this always holds for the actual structured spectral coefficient block `K` on the generic strict-support locus.

I constructed an exact TRUE-unitary counterexample to that intermediate gate. Start from account04/B09's rational orthogonal `(P,R)` separator and apply the exact first-two-row rotation with `t=1/1000`, `c=999999/1000001`, `s=2000/1000001`. The perturbed matrix is exactly orthogonal; every entry and every 2x2 minor is nonzero, and the named-partner compression-discriminant checks are nonzero.

For exact Gaussian-rational simple spectra/support normal, the actual account01/B07 support formulas generate

`K ~= [[2.777e-6, 0.999999974, 5.879e-7],[-0.999999768,-1.598e-6,4.872e-7],[2.360e-7,1.934e-7,0.999999902]]`.

Every Birkhoff decomposition of this exact `R` is one-dimensional. The exact parity objective has strictly positive parameter slope, hence its minimum is explicit. The resulting exact deficit is

`slack - 2 min_lambda sum lambda_rho m_rho(K)`

`= -2732471329348747209260554797207318135882265593 / 97656445312597656250000000000000000000000000000`

`~= -0.027980450451602287`.

So **no** Birkhoff decomposition satisfies the lead's `(PS)` condition. This is not an arbitrary-K or bistochastic surrogate: the verifier reconstructs `K` from actual complex spectra, support normal and the exact exterior-power/Hadamard formulas.

## Generic/source-valid checks and named-partner use

Consumed named OTHER-account partner result: account03/B08 `MOC4-PERMUTATION-TANGENT-v1`. I applied its strict-generic true-unitary checklist and local-support conclusion. For the present datum: spectra are simple/nonzero, all `a_i+b_j` are nonzero, all 24 target vertices are distinct, the support maximum is unique at one-based permutation `(1,3,4,2)` with exact positive gap `361590000477033578484063 / 250000000000000000000000000000`, and the associated normal matrix has no coordinate common reducing split.

The actual determinant support is **below** that vertex maximum by about `0.9933704773517618`. Therefore this refutes only `MOC4-PARITY-SLACK-v1`, not MOC4, and is fully consistent with account03/B08's theorem that a generic target counterexample cannot be born infinitesimally from a uniquely exposed permutation vertex.

## Surviving exact route

Keep lead r12's exact six-fiber inequality `(SR)`; discard only the universal scalar parity-roof shortcut. The next sharpened support/second-variation implication is:

`MOC4-SR-AT-BIRAYLEIGH-v2`: on the generic strict-support locus, if a true unitary is simultaneously top-Rayleigh for all six column and six row two-plane restrictions of `Re(eta det(D_a+U D_b U*))`, then prove the exact six-fiber `(SR)` support bound.

This retains the full `X`-dependent fiber maximum and the exact second-variation information. The earlier adjugate pair formulas remain singular-safe; repeated spectra/zero determinant can still be handled by strict-separation perturbation and continuity if this generic implication is proved.

Recommended recipients: account03/B07 lead, account03/B08 named partner, account01/B07 mixed-assignment worker, account04/B09 structured-coefficient worker, account03/B20 integrator.
