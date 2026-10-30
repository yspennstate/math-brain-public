# B04 r18 five-eigenvalue audit

Source: `paper.tex`, blob `f3e5fc173cdcee40174c19c955d813d47f32bd91`, SHA-256 `359d1e4c5ffe528dcd749f4315b426d6423944d88678544131fa3ffe090c1362`.

Verdict: **PASS AFTER ONE LOCAL THEOREM-PRESERVING REPAIR.**

I read all 715 lines and the current README, AUDIT, MANIFEST, check sources/logs and both Lean sources.

- Lines 1-199: PASS.
- Lines 200-232 (geometric Brascamp--Lieb heat flow): PASS. The derivative sign, integration by parts, Gaussian domination, large-time Gaussian normalization, small-time Lebesgue-point/Fatou step and monotone truncation all check.
- Lines 233-439: PASS.
- Lines 440-461: PASS.
- Line 462: **GAP, local repair.** The negative hyperbolic tail switches from vector (u) to (u') but reuses the coordinate lower bound selected for (u). Equal norms do not imply the same coordinate is large. Choose a separate original coordinate (i_-) with (|u'_{i_-}|\ge \rho_0/\sqrt2). The cutoff and every constant are unchanged.
- Lines 463-672: PASS after that repair.
- Lines 673-691: PASS.
- Lines 692-715: mathematical content PASS; bibliographic/priority completeness UNCHECKED.

Section 6 random-sign argument: PASS. The exact sign-chaos second moment is correct, compression/Weyl are invoked with the right orientation, and the doubled-singular-value count for the symmetric off-diagonal block is correct.

Final constants independently rechecked: (C_3<15), (C_2<12.2), no-pivot density (<167), no-pivot half moment (<26), diagonal-pivot density (<267), definite-pair density (<51), indefinite-pair density (<269). Hence the headline (270) is safe after the local repair.

Review status: this is one independent B04 end-to-end review, not a self-awarded second validation certificate.
