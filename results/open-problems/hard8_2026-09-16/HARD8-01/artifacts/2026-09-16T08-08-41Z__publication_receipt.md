# HARD8-01 checkpoint 3 publication receipt

Run report:

`hard8_2026-09-16/HARD8-01/runs/2026-09-16/2026-09-16T08-08-41Z__report.md`

Creation commit: `f78d06b13565424099246de388b9c9a64d529f6e`  
Readback: **VERIFIED** by fetching this exact path at ref `f78d06b13565424099246de388b9c9a64d529f6e` after publication.

Exact verifier:

`hard8_2026-09-16/HARD8-01/artifacts/2026-09-16T08-08-41Z__cyclic_defect_one_exact_verifier.py`

Creation commit: `a70db2b38fa57fc6efacf2e1435ff930b8b2ac73`  
Readback: **VERIFIED** by fetching this exact path at ref `a70db2b38fa57fc6efacf2e1435ff930b8b2ac73` after publication.

Exact local execution performed before publication covered every `2 <= n <= 13`, every `1 <= d < n`, and returned:

* 57 coprime exact reset-threshold cases passed;
* 21 non-coprime nonsynchronizing cases passed;
* 56 coprime exact `(n-1)`-subset threshold cases passed;
* no assertion failures.

The finite computation is supporting verification only; the report contains uniform proofs for all `n` in the stated theorems.
