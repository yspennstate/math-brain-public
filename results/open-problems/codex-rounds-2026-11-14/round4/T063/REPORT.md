VERDICT: PROVED free-energy minimality for simultaneous near-balanced torus limits with one or both fluxes fixed

The earlier result holds. Its reflection and row-insertion argument was independently re-derived, its unchanged script passed again, and a new edge enumerator reproduced all 348 small gluing images. No newer full-range GFF solution was certified in the literature check, which took under five minutes.

The new result removes the earlier requirement to take an infinite-cylinder limit first. Fix a=b=1 and any c>0. Let Z(N,L;n,m) prescribe n right arrows per vertical cut and m up arrows per horizontal cut, and let p_c be the maximal specific pressure among all translation-invariant allowed arrow laws. Set

\[
H=2\min(n,L-n),\qquad W=2\min(m,N-m).
\]

For W,H>=2, the finite-volume bound is

\[
\log Z(N,L;n,m)\ge WHp_c-3(W+H)\log2.
\]

Thus, whenever N,L both tend to infinity and n/L,m/N tend to 1/2, the pressure tends to p_c and every local subsequential limit minimises specific free energy. No aspect ratio bound is needed. These limits are also zero-slope gradient Gibbs measures, by a direct check that bounded local replacements preserve the winding sectors.

The original ensemble with only n fixed has the same conclusion for arbitrary simultaneous limits with n/L tending to 1/2: retain the summand m=floor(N/2) in its partition function. This also handles odd dimensions. [PROOF.md](PROOF.md) contains the complete argument, including the local entropy estimate and conditional uniqueness implication. It establishes no uniqueness or GFF convergence.

The new [check_two_flux.py](check_two_flux.py) uses exact integer partition polynomials. It compares two independent edge enumeration methods on six shapes, verifies 348 gluing images and 2296 row-and-column insertion images with explicit inverses, and passes 60 coefficientwise partition comparisons. The reported run took 0.474 seconds with peak RSS 14,663,680 bytes. Coefficientwise inequalities check every c>0 simultaneously.

Commands:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 check_two_flux.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 ~/codex_op_1114r3/briefs/T063/check_surgery.py
```

What failed or remains uncertain: no finite checks failed. The nice launcher reports a denied priority change because inherited priority is already nice 20; both scripts confirm that value. Neither the uniqueness proof in Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, nor the September correlation argument has been audited. No arXiv identifier is assigned here to the Hexagon item. The other opened paper was Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu, [Conformal invariance of the six-vertex model's height function](https://arxiv.org/abs/2610.07454). Global novelty of the elementary finite-volume extension is not claimed. c=0 and extreme fluxes are outside the stated finite bound.

Next worker: audit Pei's Corollary 1.3 and its dependencies. If its unique-minimiser assertion is sound, the present theorem identifies all these simultaneous near-balanced limits with the balanced plane state. Correlation asymptotics and GFF convergence still require a separate proof-level audit.

All files written are in this folder. Both earlier folders were read only; no git, subagents, external messages, accounts, or publication were used. [LOG.md](LOG.md) records the search, rechecks, outputs and audit.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received approximately 04:32 Asia/Tbilisi, 15 November 2026.
