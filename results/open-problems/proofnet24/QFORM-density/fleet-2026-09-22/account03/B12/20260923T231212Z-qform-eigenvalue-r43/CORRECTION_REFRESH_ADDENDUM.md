# Prepublication control/correction refresh — account03/B12 r43

A final source refresh was performed after the main calculation.

- Fresh `math-research-brain/main` head observed: `c4445ef9c24eb6bc5de33dd21fe2720998e4ca4f`.
- `scheduled_tasks/README.md` still has latest owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`, OWNER CONTROL revision `2026-09-22.15`, sole target QFORM, no account03/B12 pause or scope change.
- The live correction stream was reread. Two newer correction events not present in the earlier r42 snapshot were checked explicitly:
  - `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1`, brain commit `33836fccce9b2f9cbf625f8cb9b1ead8a8d4b4a8`. It refutes a critical half-Riesz bound for a **one-nonzero-eigenvalue** same-bank rank-one bilinear/square configuration. The r43 scalar corollary instead invokes the completed source theorem only after the exact Schur budget proves **two** residual singular values at the stated scale. Therefore this correction does not challenge r43 Theorem 2.1 or Corollary 4.1.
  - `QFORM-B01-COMPOUND-ALTERNATIVES-NOT-EXCLUSIVE-v1`, brain commit `f2cf1b956023e808a060560ea478d25df136c1f3`. This is a wording correction to an unrelated B01 compound-energy trichotomy and has no premise overlap with r43.

The new r43 theorem remains purely deterministic singular-value/rank algebra. It uses no pointwise phase decay, conditional-density-as-independence step, arbitrary-joint coarea, rank-one same-bank critical half-Riesz statement, or deletion of a nonzero quadratic tail.

Full unrestricted QFORM remains OPEN; no continuity upgrade is claimed.
