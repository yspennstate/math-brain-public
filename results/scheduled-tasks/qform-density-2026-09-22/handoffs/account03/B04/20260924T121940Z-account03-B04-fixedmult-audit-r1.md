SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B04, 2026-09-24T12:19:40Z.
attacking: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`; independent 790-line audit with B04 heat-flow lens, then a product-Fourier threshold reduction.

Current later owner objective superseded the older instruction to spend this run primarily on the unstructured three-eigenvalue attack. The unrestricted three-eigenvalue conjecture remains OPEN.

Baseline audited: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`.

Audit result: PASS for the candidate 17-eigenvalue theorem under this worker's end-to-end review; no fatal mathematical gap found. One nonfatal wording gap in the projection-density proof: after zero-leverage rows are dropped the proof should use `sum_{b_i>0}(1-b_i)<=d`, not equality. The `e^{d/2}` conclusion is unchanged. The geometric Brascamp--Lieb heat-flow proof and its `t downarrow 0` / `t to infinity` limits were independently reconstructed and pass. Root reproducibility files named by README/AUDIT (`SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, `checks.json`) were still absent at final refresh.

Immutable audit: `yspennstate/math-open-problems@654ac816fcb1d12925b28ae6c8186b717e5faa88`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.

New candidate improvement: a self-contained weighted-subset/grouped product-Fourier compiler, derived from the baseline BL/projection/Fourier lemmas, gives

`||p_Q||_inf <= C3 E3(M)^(-1/6)`, `C3=3 sqrt(2)e(9/2)^(1/6)<14.819`,

for every literal original-coordinate cross block, and

`sup_a E|Q-a|^(-1/2) <= C2 E2(M)^(-1/8)`, `C2=8 sqrt(e)2^(-1/8)<12.096`.

Combining these with the audited spectral-to-volume proposition and the manuscript pivot analysis yields the candidate theorem

`boxed: s_9(A)>=s, f_i<=K => ||p_Q||_inf <=6010 K^2/s`.

Normalized branch bounds: no pivot `<2371`; scalar pivot `<=6010`; definite pair `<32`; indefinite pair `<251`. No-pivot continuity is `C_0`; the full candidate theorem currently claims only essential boundedness.

Immutable improvement proof: `yspennstate/math-open-problems@8ff490c177d0cd7d6f33130f1431785e312a9d10`, path `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B04/20260924T121940Z-account03-B04-fixedmult-audit-r1/REPORT.md`.

Constant diagnostics: `yspennstate/math-open-problems@3c02458a4d39b7ae1a0e70dd18e0c5f6b98906f0`, same improvement directory, `CHECKS.json`.

Status of nine-eigenvalue reduction: NEW CANDIDATE IMPROVEMENT / PENDING INDEPENDENT END-TO-END REVIEW. Do not replace the pinned 17-eigenvalue baseline yet. The current interpolation rank count still needs nine in the no-pivot order-three branch (`r=2` requires `m>=4r+1=9`); this is a limitation of this proof route, not evidence that eight is impossible.

Final control/correction refresh: `CURRENT_OBJECTIVE.md` still names `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`; the old QFORM correction ledger contains no event refuting this physical-coordinate product-Fourier compiler. Execution status `WITHOUT_VERIFIED_BRAIN`.
