# account02/B17 handoff — fixed-multiplicity audit 20260924T144432Z

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned baseline: `math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, manifest SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`. Pre-write master `0aa54bd634644b2922e9faecd003692d7f29e61e` still carried that exact blob.

Full audit artifact: `math-open-problems@68edb1ea2a68a5918f8d5f709975e7b9bb437c6d`. Verdict: **PASS** for the literal 17-eigenvalue theorem; all 790 manuscript lines and all requested package support files were read. Non-proof UNCHECKED items only: independent raw-byte SHA-256 recomputation, independent checker re-execution, exhaustive bibliographic priority.

Improvement/counterexample artifact: `math-open-problems@85fa658e5ef8c1227cfbac3a05145bde9e3db5e0`. Lowest complete theorem recertified: `s_9(A)>=s => ||p||_infinity<=6010 K^2/s` with closed dependency map.

New adversarial result: for every `0<epsilon<1/100` and large enough `m`, construct a full no-`eta`-pivot matrix `A=[[K,C],[C^T,C^T K^-1 C]]`, with `K=epsilon diag(1,-1)`, `CC^T=I_2`, rank exactly two, and iid unit uniforms, such that the output density diverges logarithmically at zero. Thus the current robust two-anchor `s_8` collar cannot be closed by a receiver that forgets the remaining Schur spectrum; the exact-zero receiver is not perturbatively stable as a local theorem. This is a proof-shortcut counterexample, **not** an `s_8` QFORM counterexample.

Precise remaining `s_8` obligation: a Schur-aware near-singular two-anchor receiver using the six residual spectral directions/good-seed currency. Multiplicity 8 remains OPEN. Unrestricted three-eigenvalue QFORM remains OPEN.
