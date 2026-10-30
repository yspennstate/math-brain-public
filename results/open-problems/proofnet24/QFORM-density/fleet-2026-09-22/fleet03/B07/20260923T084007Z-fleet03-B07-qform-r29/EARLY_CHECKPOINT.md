SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T08:40:07Z.
attacking: the r28 four-hub curvature survivor — prove that a large hub-times-far-core motif either already contains the transverse-star branch or forces a single physical anchor with aggregate incident E2 mass, then lift that bank through the completed anchored-compound ladder instead of selecting one tiny minor.

# Early substantive checkpoint — r29


Incoming r28 source: `yspennstate/math-open-problems@1ffce50d452b85f4f080ce0b61c68023e8f0d66c:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260923T073755Z-fleet03-B07-qform-r28/REPORT.md`.

Its four-hub failure branch writes the physical cross block as

`N = [[A,B],[C,D]]`, with `A` a 2x2 physical hub block,

and supplies one of five positive motifs. The present checkpoint attacks

`M4 = ||A||_F^2 ||D||_F^2`.

Let

`W11 = sum_{h in H, l in L, r notin H, t notin L} det N[{h,r},{l,t}]^2`.

For each quadruple the determinant is `A_hl D_rt - B_ht C_rl`. Treating these arrays as vectors in `(h,l,r,t)`, the reverse triangle inequality gives

`sqrt(W11) >= | ||A||_F||D||_F - ||B||_F||C||_F | = |sqrt(M4)-sqrt(M5)|`,

where `M5=||B||_F^2||C||_F^2`.

Hence the following cancellation-free dichotomy is rigorous:

* either `M5 >= M4/4`;
* or `W11 > M4/4`.

In the second branch write

`H2(h,l)=sum_{r notin H,t notin L} det N[{h,r},{l,t}]^2`.

There are four hub anchor pairs `(h,l)`, so some physical pair satisfies

`H2(h,l) >= W11/4 > M4/16`.

This already improves the r28 motif ledger: a large hub-times-core product cannot be lost to determinant cancellation unless the transverse-star motif is itself large. No local determinant is inverted.

Next intended step in this same run: apply the completed anchored-compound tail ladder from `yspennstate/math-open-problems@33b7581b6dc153541b2aa4f6c706192bd8a81eaa:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B07/fleet01-B07-20260923T050509Z-r16/REPORT.md`, namely `H3 >= (T2(N)/2) H2`, to obtain a rank-two-tube versus anchored-third-volume alternative at this actual four-hub anchor. Then route the third-volume branch through the current volume-stability package while preserving original-coordinate product provenance.

Status: supporting calculation proved; full QFORM remains open.
