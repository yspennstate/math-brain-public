# fleet02/B05 second review

Run: fleet02-B05-20260924T2324Z-auto11
Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924

Source pin:
- master observed before delivery: 10d94ebd960fde3f0ae7db989b5a4cc5cd7f9590
- last paper change: 5ba2a4d6b689721601cce7ec7e22ffea9fa98f90
- paper.tex blob: bbebd6f6c5a27e9f639186a305008ab43a481e70
- MANIFEST SHA-256: 040d03beea0f9d652992b9ea9dca71e4f2df98cdeef942b291b1c73ec65cdab3
- paper length: 715 lines / 65367 bytes

Read in full: README.md, AUDIT.md, MANIFEST.txt, paper.tex, check logs, five-specific Lean logs, and shared Section 2-5 axiom logs.

Verdict: PASS. No new theorem-bearing GAP or FALSE statement was found in current master. The old Lemma 5.3 presentation gap is repaired at line 456: positive and negative hyperbolic tails select separate original coordinates. Bibliographic and priority attribution, lines 687-714, is UNCHECKED only as literature attribution.

Claims retained:
s_5(A) >= s > 0 implies essential density <= 270 K^2/s.
s_3(A) >= s > 0 implies sup_a E|Q-a|^(-1/2) <= 77 K/sqrt(s).

Section 6 was read for dependency closure but not re-proposed: current control says it is machine-checked end to end. The current Lean logs terminate successfully and report only propext, Classical.choice and Quot.sound.

Line ledger:
- 1-102 PASS: theorem quantifiers, scaling and architecture.
- 103-199 PASS: Section 2 Fourier, conditioning/measurability, singular values, Schur count and Gram identities.
- 200-267 PASS: Section 3 Brascamp-Lieb, product projection and scalar Fourier powers.
- 268-417 PASS: Section 4 entropy, grouped hub compiler and order 3/2/1 consequences.
- 418-537 PASS: Section 5 square/definite/hyperbolic profiles, concentration, singular kernels and pair half-potential. Line 456 is the corrected two-coordinate tail selection.
- 538-606 PASS: Section 6 machine-checked end to end; spectral facts not re-proposed.
- 607-672 PASS: Section 7 no-pivot, half-potential, five-density theorem and scaling.
- 673-685 PASS: mathematical threshold remarks.
- 687-714 UNCHECKED: bibliography/priority only.
- 715 PASS: end document.

B05 lens: for cap-one product inputs and full-row-rank B, ||p_(BX)||_infty <= exp(d/2)/sqrt(det(B B^T)). This is a marginal bound only. Rotated uniforms show projected conditional caps can diverge; 2 X1 X2 has a genuine logarithmic singularity and X1^2 a genuine inverse-square-root singularity. The proof avoids these traps by conditioning only on literal banks and averaging a.e. density majorants with Tonelli/rearrangement.

Checks: constants_exact ALL PASS 41/41; verify_five ALL PASS 35/35; two_star_affine ALL PASS. Current Lean logs show no error/sorry/admit markers and only propext, Classical.choice, Quot.sound.

Four-eigenvalue density remains OPEN. Unrestricted three-eigenvalue density remains OPEN.
