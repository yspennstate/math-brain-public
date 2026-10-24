# Worker-owned memory snapshot — account03/B20 r4

Source objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.
Pinned source: `math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Durable facts from this run:

- Retract B20 r2's claim that the singular-`A` Schur passage is a gap. The moving threshold is legitimate because it yields `s_m(S_eps)>=t-|eps|` and singular-value continuity gives `s_m(S)>=t`.
- Pinned 17-direction proof: PASS mathematically in this B20 review; essential boundedness, not a global continuity theorem.
- Release-grade lower threshold: 9, with two separate complete reconstructions supporting `<5338 K^2/s` for `s_9(A)>=s`; arbitrary rough product laws, signs, affine terms, dimension and remaining spectrum retained.
- Multiplicity 8 remains open for `L^infinity`. Current robust pair has `det(CC^T)>=0.3649442658827020...`; all finite `L^p` and `h log(1/h)` control are known, but local robust-cross data alone are insufficient.
- B17 overlap-two good-seed determinant: `|det A[S union H,T union H]| >= gamma_* |det B|`, `gamma_*=0.8939339828220179...`.
- New theorem `QFORM-OVERLAP4-ONE-SYMMETRIZATION-L2-BARRIER-v1`: the bilinear oscillatory `L2` operator norm in dimension `d` is exactly `(2pi)^(d/2)|t|^(-d/2)|detM|^(-1/2)`. After one symmetrization at `d=4`, taking a square root leaves only `|phi(t)|=O(1/|t|)`. Therefore a one-symmetrization + separated-L2 + Plancherel overlap-four compiler cannot close the endpoint by absolute Fourier inversion.
- Next target: `QFORM-S8-SHARED-ANCHOR-SIX-SCHUR-ENDPOINT-v1`.

Full immutable report: `math-open-problems@cfddd974d2da2b25d027bb64c2e1e48e7b6fc866`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B20/20260924T144348Z-account03-B20-fixedmult-auto11-r4/REPORT.md`.

Brain status: `WITHOUT_VERIFIED_BRAIN`; repository transport/source-memory writeback occurred, native learned-memory receiver use was not exposed or verified.
