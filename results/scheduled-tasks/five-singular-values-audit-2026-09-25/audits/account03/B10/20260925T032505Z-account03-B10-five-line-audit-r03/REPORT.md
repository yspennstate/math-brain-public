# account03/B10 r03 audit report

Run: 20260925T032505Z-account03-B10-five-line-audit-r03
Objective: QFORM-FIVE-SINGULAR-VALUES-LINE-AUDIT-20260925
Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c, short/short.tex and the pinned 14-page short.pdf only.
Control observed before work: math-research-brain@c7211eaee966dec62a3bc96409b4bf102f7ca5e8.
Execution: WITHOUT_VERIFIED_BRAIN.

## Pass-1 closure

B10 pass 1 is now coverage-complete: every source clause has a status. This is not a literal manuscript PASS because the existing FALSE/GAP ledger is preserved.

Line 62, PDF p1, current-open-status sentence: GAP. A targeted current literature search found no resolution of the stated three-eigenvalue question, but absence of a search hit cannot establish that a problem is globally open. Safe repair: "The present argument does not settle whether three eigenvalues of modulus at least s always suffice for a bound CK^2/s." No theorem impact.

Line 74, PDF p2, related work: PASS on the substantive citation claims. BGKS arXiv:2005.08930, Rogozin/Ball, Rudelson-Vershynin/Livshyts-Paouris-Pivovarov, Ball/Barthe, Carlen-Lieb-Loss/BCCT, Carbery-Wright, Costello-Tao-Vu, and de la Pena-Gine were checked against primary or publisher/author records. These are contextual citations; the proof's needed analytic statements are proved inside the manuscript.

Lines 649-673, PDF p14, bibliography: PASS. All eleven entries were checked for authors/title/venue/year/pages or arXiv identifier; no material metadata mismatch was found.

Line 398, PDF p9, Lemma 5.1 density display: GAP. At z=v the strict support indicator is zero while the denominator sqrt(|a||z-v|) is zero, so the displayed pointwise expression is not literally defined there. Repair: state the formula for z != v or a.e. and set p_T(v) to any finite value. No downstream change because densities are defined a.e. Fresh main surfaced a separate account02/B01 note before this reconstruction, so this is independently reproduced, not independently discovered.

Cumulative literal-source issue ledger after pass 1:
- abstract random-sign description missing no-pivot qualification: FALSE, expository;
- outline universal "has a singularity" wording: FALSE, expository;
- line 222 "beta_i=0 are at most one": FALSE; delete "are at most one";
- Lemma 4.3 omitted explicit Jensen: GAP;
- line 398 critical-point density display: GAP;
- elliptic polar "global diffeomorphism" across angular seam: FALSE;
- hyperbolic critical-level nullity omitted: GAP;
- line 62 current open-status assertion: GAP;
- Lemma 2.5 "Both follow" wording for three assertions: minor wording defect.

No theorem-level counterexample has been found; the proof-bearing issues have local repairs already reconstructed, but the literal source is not defect-free.

## Pass 2 started: backwards theorem-front reconstruction

Theorem quantifiers/scaling: PASS on this pass-2 slice. Finite density cap K implies K>0. With Y=KX,
Q=(s/K^2)[Y^T(A/s)Y+(K/s)b^T Y+(K^2/s)c],
so the normalized cap rescales exactly by K^2/s and arbitrary affine b,c are retained. No coordinate rotation occurs. The interval formulation is equivalent to an essential-supremum density bound by open-set decomposition, outer regularity, and Radon-Nikodym.

Introductory examples: PASS. For X uniform on [0,1], X^2 has density 1/(2 sqrt y). For independent X1,X2 uniform on [0,1], for 0<z<1,
p_{X1^2-X2^2}(z)=(1/4) int_z^1 [y(y-z)]^{-1/2}dy
=(1/2) arcosh(1/sqrt z)
=(1/2) asinh(sqrt((1-z)/z)),
which diverges logarithmically as z decreases to 0. Thus the one/two-eigenvalue examples are correct.

The exact diagnostic/check script for this pass is check_r03.py and its committed output is check_r03.out.

Next B10 cursor: continue pass 2 backwards from Section 7 through Sections 6 and 5, re-derive constants and boundary cases under the new reconstruction order, and regression-test every local repair. No constant optimization or lower-threshold research was done.
