# account03/B15 r14 audit

Source: yspennstate/math-open-problems@ec211ba2d77a4a9850168c6af1574ea651feaa7c; short.tex blob c4f2a997cf336ee974e15409b5bccdd8cca039d8; PDF SHA-256 4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423.

Strict complete-pass count remains 0. No theorem-level false statement was found in this invocation.

## L222 reclassification: PASS

This worker withdraws its earlier FALSE classification. The source says: “Factors with beta_i=0 are at most one and are dropped.” In context, “are at most one” refers to the values of the multiplicative factors, not the number of zero-beta indices. If beta_i=|w_i|^2=0, then w_i=0 and the corresponding factor is f_i((Uy)_i)<=1, so any number of these factors may be dropped in an upper bound. The positive-beta frame identity and entropy estimate are unaffected. Optional clearer wording: “Factors corresponding to beta_i=0 are bounded by one and may be dropped.”

## L505/L509: GAP, zero-loss repair

Lemma 5.6 uses h(y)=6+log_+(16/|y|) and g(y)=|y|^(-1/2)1{|y|<=delta} in the rearrangement lemma. At y=0 the displayed real expressions are not literally defined. Set h(0)=g(0)=+infinity. They are then extended-nonnegative, measurable, even, nonincreasing; changing one point does not affect the integrals. Pair-half-moment constant is unchanged.

## L613/L615: GAP, zero-loss repair

J(d) was defined only for d!=0, but E J(R-a) is written at L613 before L615 states that R is atomless. Either move the atomless conclusion from Lemma 5.4 before L613, or define J(0)=+infinity and then use P(R=a)=0. The 77 bound is unchanged.

## Additional reconstruction

L178-L244 (geometric Brascamp-Lieb, projection, Fourier powers) was reconstructed directly. The heat-flow derivative identity, contraction inequality, Gaussian domination, large-time and small-time limits, and monotone truncation check. Corollary 4.4 was rechecked: ell=3 gives an integrable characteristic function and hence a continuous density; ell=2 supplies a half-potential bound only. Conditioning branches later establish absolute continuity plus essential L-infinity, not continuity.

The L505/L613 items were targeted after account02/B15 handoff commit 6096979d399dfd43fd40586e5f2e333350b32c63 flagged them; they were independently verified against the pinned source but are not claimed as independently discovered. L222 PASS agrees with account02/B01 summary commit 1a62646dc4b091eed52be667e66866f499390553 after a fresh source-context check.

Status: WITHOUT_VERIFIED_BRAIN.
