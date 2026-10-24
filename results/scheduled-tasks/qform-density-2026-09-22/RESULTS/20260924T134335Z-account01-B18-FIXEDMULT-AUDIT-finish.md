# account01/B18 finish — QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Actual finish: 2026-09-24T13:43:35Z.

Pinned manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Substantive result: complete 790-line B18 reconstruction now returns mathematical **PASS** for the 17-eigenvalue theorem, with a nonfatal prior-art/bibliography presentation gap. This run explicitly corrects B18's earlier false-positive Schur GAP: from the invertible regularizations one has `s_m(S_epsilon)>=t-|epsilon|`, and singular-value continuity gives `s_m(S)>=t`; the baseline moving-threshold proof is valid. No repair to the baseline is mathematically required.

Primary-source scope: BCCT and Rudelson–Vershynin are valid provenance; published metadata was verified. Directly relevant omitted prior art is Livshyts–Paouris–Pivovarov (sharp product-marginal density `2^{d/2}`) and Banks–Garza Vargas–Kulkarni–Srivastava (Theorem 2.1 “Density of Quadratic Forms” for bilinear-affine bounded-density inputs). The latter does not cover the arbitrary same-bank quadratic phases retained by this manuscript, so it does not close the present theorem or the 16-direction endpoint. Herry–Malicet–Poly has materially narrower iid/Gaussian-field hypotheses. No novelty claim is inferred from search absence.

Constant: the written proof supports `(2010+1200 log 16) K^2/s = 5337.106466... K^2/s < 5338 K^2/s`, preserving every hypothesis. This tightening was already identified in the preceding B18 artifact and is reverified here.

Threshold: no full-hypothesis reduction below 17 is certified. The determinant receiver needs crossing order 5 because order 4 gives the nonintegrable `|t|^-1` endpoint; the interpolation worst case `r=4` needs `m-3r>=r+1`, hence `m>=17`. Fresh B20's `s_16` endpoint localization remains unpaid because its second crossing may align with the rank-four carrier, and the strongest located bilinear prior art does not tolerate both arbitrary same-bank phases.

Immutable audit: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/audits/account01/B18/20260924T132305Z-account01-B18-r11/AUDIT.md` (creation commit `4825d68f2b8df61d43d6789917873615ab1015e4`, read-back blob `ef6950a664b2caa692cff0b837e2a552b13e7d15`).

Immutable improvement: `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account01/B18/20260924T132305Z-account01-B18-r11/PRIOR_ART_CONSTANT_AND_THRESHOLD.md` (creation commit `049f40412af5663c77ffd47dcaf601a07f3e8506`, read-back blob `cc16d84963d40a90e43fd45387c1a4ed8a4cb77f`).

Support bundle status: `proof_map.csv`, `SOURCE_MANIFEST.json`, `verify.py`, and `checks.json` are present now; the earlier B18 missing-file packaging report is stale. Recorded finite suite PASS is evidence only, not proof or an independent rerun by this invocation.

Validation: this same-slot correction/review is not counted twice. A distinct B20 reconstruction also reports PASS, but this worker does not self-award release/independent-validation status; reconciliation remains with the designated release gate.

Execution: `WITHOUT_VERIFIED_BRAIN`. Model/effort metadata: UNKNOWN unless platform-exposed separately. No email/push, task creation/restart, cadence/state change, cross-account authentication, paid call, public release, repository visibility change, or permission expansion.