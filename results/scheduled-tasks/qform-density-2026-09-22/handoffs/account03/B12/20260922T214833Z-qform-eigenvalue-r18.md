SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-22T21:48:33Z.
attacking: two-bank spectral-leakage stability: use a quantitative indefinite two-bank pair plus any third global core singular direction, then absorb arbitrary outside eigenvalues with the account04/B12 mixed-norm shear compiler.

# account03/B12 handoff — two-bank third-source stability

Status: **PROVED SUPPORTING TARGET-LEVEL REDUCTION; full QFORM OPEN.** Essential boundedness only; continuity not proved.

New result `QFORM-TWO-BANK-THIRD-SOURCE-ARBITRARY-COMPLETION-v1`: take two disjoint original-coordinate banks `Y_j=u_j^T X_{T_j}` with `||u_j||_2=1`, a disjoint original-coordinate core `Z`, and arbitrary outside coordinates `R`. If

`Q=W^T H W+2W^T C R+psi(R)`, `W=(Y1,Y2,Z)`,

with `s_3(H)>=s>0`, and the `2x2` bank pair `B` is invertible indefinite with `D=|det B|`, `kappa=sigma_min(B)`, then

`||p_Q||_infinity <= 6*400^(1/3)*(D^2*kappa*s)^(-1/6)`.

The third singular direction may lie anywhere in the reduced core `Z`; a third disjoint scalar bank is no longer needed. The outside function `psi` may be any measurable function, hence in particular an arbitrary quadratic block with arbitrarily many extra eigenvalues of either sign/magnitude, and `C` is unrestricted. For a definite bank pair the simpler bound is `2*pi/sqrt(|det B|)`.

Proof splice: normalized bank projections have density cap `sqrt(2)`; scaling the two banks by `sqrt(2)` sends `B -> B/2` and, by singular-value product inequalities, `s_3(H)->>=s/2`. Apply the completed arbitrary-rank indefinite physical-pair theorem to every fixed outside fiber, giving the displayed constant. Then apply the ASSIGNED PARTNER account04/B12 mixed-norm shear compiler (`math-open-problems@9ce47e2a0f2c8434d901df13a218450c2189d80e`) to add the actual dependent remainder `psi(R)` without convolution.

New result `QFORM-TWO-BANK-SPECTRAL-LEAKAGE-STABILITY-v1`: for a protected core `H0` with `s_3(H0)>=s0` and pair gap `sigma_min(B0)>=beta0`, add signed rank-one terms `sum tau_r(v_r^T(W,R))^2`. Let

`Delta=||sum tau_r v_{r,c}v_{r,c}^T|| <= sum |tau_r| ||v_{r,c}||^2`.

If `Delta<min(s0,beta0)`, the indefinite pair remains indefinite and

`||p_Q||_infinity <=6*400^(1/3)*[(beta0-Delta)^5(s0-Delta)]^(-1/6)`.

For a definite pair the bound is `2*pi/(beta0-Delta)`. All outside components/cross couplings are free. In particular, if `v_{r,c}=0` for every added direction, arbitrarily many arbitrarily large added eigenvalues cost exactly zero. At `s0=beta0=1, Delta<=1/2`, the indefinite constant is `12*400^(1/3)=88.4167559674...`.

Canonical mathematics and check bundle: `yspennstate/math-open-problems@e71ed8023266f157a6f5c7a04ea6f9c53acc59c5`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T214833Z-qform-eigenvalue-r18/`. Report read back; arithmetic checker records the normalization factor `64^(1/6)=2` and constants.

Fresh pre-publication control: `math-research-brain@744e0110da52416b912170eb98a6e64dfec3145f`, OWNER CONTROL `2026-09-22.15`, programme revision `2026-09-22.5`; correction inbox blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`, unchanged from the prior B12 run.

Remaining implication: from only `s_3(A)>=1`, extract TWO disjoint scalar banks with a quantitative nonsingular pair while retaining any third singular direction in the remaining reduced core, or fall into an already-paid physical-pair/ridge/localized branch. Heavy overlapping/Hadamard frames remain the stress case. Do not infer that arbitrary extra spectrum helps without a certificate.

`WITHOUT_VERIFIED_BRAIN`. No scheduler/task mutation, email/push notification change, Drive/public release, paid API/model/Codex use, or cross-account authentication.
