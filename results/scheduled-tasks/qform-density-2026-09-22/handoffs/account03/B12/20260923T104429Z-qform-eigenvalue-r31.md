SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T10:44:29Z.

attacking: compression-footprint stability for arbitrary added spectrum; charge only the protected compression and let arbitrary cross/complementary spectrum pass for free.

# account03/B12 r31 handoff

Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN / NOT INDEPENDENTLY REVIEWED**. Continuity is proved only in the separate volume branch below, not for the compression branch or full target.

Canonical mathematics (read back):

`yspennstate/math-open-problems@f6d5af0d6f222415ccd5c7d5391fd0de8be32013`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260923T104429Z-qform-eigenvalue-r31/REPORT.md`

Core result `QFORM-COMPRESSION-FOOTPRINT-STABILITY-v1`: if an ACTUAL `m`-coordinate physical block `H=A[I,I]` has a subspace compression `C=P_E H P_E|_E` within operator distance `delta<mu` of a symmetric reference `B0` having at least three eigenvalues of modulus at least `mu`, then Hermitian threshold-count interlacing gives

`N_abs(H;mu-delta)>=3`, hence

`||p_(X^TAX)||inf <= 2 sqrt(6 pi m)/(mu-delta)`.

All cross coupling between `E` and `E^perp`, the entire complementary compression, all outside eigenvalues and all outside couplings are arbitrary. For a signed spectral update `R=sum tau_r v_r v_r^T`, only the protected footprint is charged:

`delta_E=||P_E R[I,I] P_E|| <= sum |tau_r| ||P_E(v_r|_I)||^2`.

Thus individual added eigenvalues can be arbitrarily large and of either sign when their protected overlap is small; directions orthogonal to the protected subspace cost exactly zero.

Actual designated-partner application: account04/B12 r4 at `math-open-problems@3948d77b0bde5af1bd37cd7c975d4f540eba901b` uses a complementary block `D=Z^T B Z` with `Z^T U=0`. Since `Z^T(B+U Theta U^T)Z=D`, `D` is literally a Hermitian compression. Therefore three eigenvalues of `D` with modulus at least `mu` imply three eigenvalues of the full physical block with modulus at least `mu`, **without the prior shear factor `ell(rho)^2` and without global invertibility of D**. With local dense tail norm `delta`, the partner receiver becomes

`||p_Q||inf <= 2 sqrt(6 pi m)/(mu-delta)`.

For its five-coordinate example `D=diag(2,-2,2)` and local dense tail `<=1/5`, while allowing arbitrary top block, arbitrary cross block and arbitrary symmetric hostile update, this gives `s3>=9/5` and `||p_Q||inf<=10.7868106253...`.

Newest Claude-derived volume theorem actually applied: `math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`. If an actual baseline original-coordinate cross block `M0=A0[J,K]` has `s3(M0)>=a`, row-range leverage `<=1/2`, and a signed spectral update obeys

`sum |tau_r| ||(v_r)_J|| ||(v_r)_K|| <= a/16`,

then its actual final cross perturbation has operator norm `<=a/16`, so the full ambient output has a continuous `C0` density with

`||p_Q||inf <=24 sqrt(3)e/(5a)<23/a`.

The early checkpoint in this run tried only to improve the previous leakage rank payment from `2k` to `k`; it is preserved but superseded by the zero-leakage-cost compression argument.

Finite checks beside the report ran 10,000 compression-footprint and 10,000 partner-style mixed-sign instances with zero violations; these are sanity checks only.

Remaining full-target gap: the bare global condition `s3(A)>=1` must still force a bounded-size original-coordinate carrier of such a protected compression, an actual diffuse cross block, or an already-paid grouped-bank/hub/ridge/pair mechanism. A protected subspace spread over unboundedly many original coordinates leaves the finite-core bound with `sqrt(m)` loss. Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.

Final control refresh before publication: brain main `d630bdc30c8bcd181fee484bb0d3dbfa988b5b87`, OWNER CONTROL `2026-09-22.15`, programme revision `2026-09-22.5`, no B12 pause/stop. Execution remains `WITHOUT_VERIFIED_BRAIN`.
