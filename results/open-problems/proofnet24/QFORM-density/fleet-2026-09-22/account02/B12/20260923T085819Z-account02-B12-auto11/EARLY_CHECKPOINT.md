SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-23T08:58:19Z.
attacking: aligned anisotropic anchor routing for two independently arbitrary eigenvalue replacements, stable under an arbitrary full-rank dense small tail.

# Early substantive checkpoint

Status: supporting lemma proved below; full QFORM remains open.

## First unpaid implication

From the bare hypothesis `s_3(A)>=1`, no current argument forces three ORIGINAL-coordinate physical triples whose normalized local update anchors are coordinatewise separated in a common eigen-update basis. The theorem below pays arbitrary signed/magnitude changes of two eigenvalues once such an aligned three-anchor family exists; the missing global step is to extract this family or force an already-paid volume/hub/pair/Schur exit.

## Coordinatewise three-anchor lemma

Let three physical cores `I_0,I_1,I_2` satisfy the matrix-parameter hypotheses of account03/B12's completed Schur-gap lemma at `math-open-problems@333dd6db61c9d18e88f9b8be5bae55c811d49b42`, with local orthogonal factors `S_j=I_2`. Write

`K_j = diag(c_{j1},c_{j2}) + E_j`,  `||E_j||op <= eps`.

Assume that for each `k=1,2`, the three numbers `c_{0k},c_{1k},c_{2k}` are pairwise `Delta`-separated. Then for every diagonal parameter `Theta=diag(tau_1,tau_2)` there is a core `j` with

`sigma_min(K_j+Theta) >= Delta/2-eps`.

Proof: for each coordinate `k`, at most one `j` can have `|c_{jk}+tau_k|<Delta/2`; otherwise two anchors in that coordinate would be less than `Delta` apart. Two coordinates therefore exclude at most two of the three cores. Choose the remaining core and apply Weyl to `E_j`.

Feeding this into the completed partner inequality

`sigma_min(B_j+U_j Theta U_j^T) >= ell(rho_j)^2 min{mu_j, f_j sigma_min(K_j+Theta)}`

gives the uniform physical-core floor

`gamma = ell_*^2 min{mu_*, f_*(Delta/2-eps)}`.

An arbitrary symmetric dense tail `T` with `||T||op<=delta<gamma` changes every principal compression by at most `delta`, so one final core has gap at least `gamma-delta`. This is a deterministic final-matrix statement; no claim that `X^T T X` is small is made.

For triple cores, conditioning on all other ORIGINAL coordinates leaves the retained inputs independent with density caps one. Theorem A in the required newest-Claude counterexample-search source (`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`) therefore gives

`||p_Q||inf <= 6 sqrt(pi)/(gamma-delta)`.

This is already a real inequality and uses no post-rotation independence.
