# account02/B19 r14 correction handoff

This file supersedes the numerical constant in the primary r14 handoff, not the theorem's scope or the high-Schur-offdiagonal branch conclusion.

The TT* conditional interval has length `h` after dividing the difference inequality by the factor `2` in `2(C^TZ)^T V`; the correct conditional probability is `h sqrt(e)/||C^TZ||`. Therefore

`QFORM-CROSSCUT-HALF-HOLDER-v1-corrected:`

`P(F(U)+2U^T C V+G(V) in K)`
` <= sqrt(2e) pi^(1/4) |K|^(1/2) (s1(C)s2(C))^(-1/4)`.

The Ky-Fan cut argument still gives `s1(C)s2(C)>7 tau^2/256` on the two-channel branch. At `tau=3/10`, the corrected explicit constant is `13.9371688286<13.938`.

One proof sentence is also corrected: `s1+s2>tau/2` and `s2>=tau/16` do not by themselves imply `s1>7tau/16`; the product bound follows by splitting `s2 in [tau/16,tau/4]` from `s2>=tau/4`. The inequality `s1>7tau/16` is used only in the complementary near-rank-one branch `s2<tau/16`, where it is valid.

The named-partner splice only needs a finite Hölder constant with exponent `1/2>1/4`, so `QFORM-HIGH-SCHUR-OFFDIAG-PAID-v1` remains valid.

Canonical corrected mathematics: `yspennstate/math-open-problems@59b8c468c9814e99833f427dcebfc67f6197fedd`, correction file `CORRECTION.md`, corrected verifier terminator `QFORM_CROSSCUT_HALF_HOLDER_CORRECTION_PASS`. Full QFORM remains OPEN.