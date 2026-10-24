SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-24T14:32:40Z.
attacking: audit the fixed-multiplicity candidate with emphasis on definite/hyperbolic pair envelopes and attempt a rigorous 9-to-8 threshold reduction via a three-bank/product-set receiver.

Current objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924` (later owner objective, controlling this run). Baseline source `math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

New result: `QFORM-STRONGCROSS-WEAKSELF-NEEDS-SCHUR-SPECTRUM-v1`. The current multiplicity-eight B15 terminal reduction supplies a physical pair with weak self-block and `det(CC^T)>=0.364944...`. I proved these local data alone cannot pay a density bound: for `m=243`, `c=1/20`,

`A=c[[0,J_m],[J_m,0]]`

has no `eta=0.01` pivot, and for `H={p_1,r_1}` has `||B||=0.05` and `det(CC^T)=14641/40000=0.366025`, but `rank A=2`, the pair Schur complement is exactly zero, and under iid `Unif[-1/2,1/2]` inputs `Q=(1/10)UV` with independent sums `U,V`; its density diverges logarithmically at zero. Thus the remaining threshold-eight receiver must explicitly spend the six Schur spectral directions forced by `s_8(A)>=1` after an invertible pair pivot (or equivalent global spectral provenance). This is not an `s_8` counterexample.

Full proof: `yspennstate/math-open-problems@7ad88b5e660fe2b0caa033671ebef67d7552c7cc`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B13/20260924T143240Z-account03-B13-fixedmult-audit-r5/IMPROVEMENT.md`.

Fresh end-to-end baseline audit: PASS, no new fatal defect. Audit report: `yspennstate/math-open-problems@96bda0cfcbb54024800c3c9733cb4b8b659bd8ce`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B13/20260924T143240Z-account03-B13-fixedmult-audit-r5/REPORT.md`.

Designated partner account04/B13 applied: its exact no-attainment purification (`math-open-problems@d9f6bcd057b7804ea7ba06fea8dad5f54e357990`) converts the current reviewed nine-direction slab inequality with constant `<2582` exactly into the corresponding unit-product-set geometric slab inequality and back; no interval/centered/bounded-fragment extremality is introduced.

Current theorem status: nine-direction candidate has canonical `C_0` density with height `<2582 K^2/s` from current source-backed B14/B15 work. Multiplicity eight remains OPEN; exact-zero strong-cross subchamber is paid, nonzero weak-self + six-Schur-direction receiver is open. Full three-eigenvalue QFORM remains OPEN. Execution context remains `WITHOUT_VERIFIED_BRAIN`.
