# P04 / I0101 readback receipt — 2026-09-16T19:39:40Z

Status: **COMPLETE_READBACK_VERIFIED**

Canonical report:
`proofnet24/P04-closure-local-paley/runs/2026-09-16/2026-09-16T19-39-40Z__run-report.md`

Creation commit:
`9bb357ca31a6519a42f262cc640f1f0c35cfbc8b`

Verified report blob:
`c22a00c16c5c7b7e92c01f344aa5ef33145ae1bf`

Readback was performed against the exact returned creation commit, not moving `master`, in contiguous ranges covering lines 1 through the end of the report. Every returned range reported the same blob SHA. The final range contained the literal terminal marker:

`**End of complete run report.**`

Verified report headline state:
- actual runtime disclosure: GPT-5.6 Sol / reasoning UNVERIFIED; no false GPT-6 claim;
- source: Bandeira Randomstrasse 2025 Conjecture 27 / I0101;
- metric: `149 -> 257`;
- exact-certified domain: `{149,257}`;
- status: `PARTIAL / source OPEN`;
- Section-B moves: `18,21,25`.

Exact finite artifacts were also read back at their creation commits:

- checker `proofnet24/P04-closure-local-paley/artifacts/2026-09-16T19-39-40Z__p257_degree_dual_checker.py`
  - commit `c9bc0d38dd709da4c35a9b1537a10e5aaca78827`
  - blob `ba5df06aa8bc3db86dacf840e30ae2824ac0bc2a`;
- output `proofnet24/P04-closure-local-paley/artifacts/2026-09-16T19-39-40Z__p257_degree_dual_checker.out`
  - commit `32bdec141263627aa2aa13d23f7582ff3e37bfe7`
  - blob `0783b20cb580aabaceb104795c4b6b905977c138`
  - contains `P04-I0101-P257-DEGREE-AWARE-DUAL=PASS` and `EXACT_RECONSTRUCTION=PASS`.

No truncation, overwrite, or theorem-changing transport defect was detected.
