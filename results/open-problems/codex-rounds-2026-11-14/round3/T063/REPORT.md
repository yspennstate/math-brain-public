VERDICT: PROVED free-energy minimality of every near-balanced torus subsequential limit

For a=b=1 and every c>0, let mu_L be the infinite-cylinder limit in the sector with n_L right arrows per transverse cut. If n_L/L tends to 1/2, every local subsequential limit of mu_L minimises specific free energy among all translation-invariant allowed arrow laws. This is the new result beyond the earlier literature handoff. It does not prove a GFF limit.

The complete argument is in [PROOF.md](PROOF.md). Two weight-preserving constructions suffice: four reflected rectangles give a balanced torus, and insertion of straight rows embeds a smaller balanced torus into a near-balanced sector. If p_c is the variational pressure, H=2 min(n,L-n)>=2, and p_L(n) is the sector strip pressure, the explicit bound is

\[
p_L(n)\ge \frac{H}{L}p_c-\frac{3\log2}{L}.
\]

Fixed-block entropy subadditivity then proves that all near-balanced subsequential states attain p_c. This avoids the September manuscript's rectangle operator-norm estimate and any Bethe-ansatz free-energy formula.

The earlier finding holds: Yan Ru Pei's [November preprint](https://hexagonmath.org/pdf/2611.00291v1), identifier hexagon:2611.00291v1, makes its state identification conditional on existence (O1) and free-energy minimality (O2). The present proof supplies O2 for every subsequential state. If its Corollary 1.3, uniqueness of the translation-invariant minimiser for 1<c<=2, is valid, compactness now gives O1 and identification for the whole near-balanced sequence. That uniqueness proof has not been audited here. There is no arXiv identifier for this November item in the opened record.

The literature check lasted under five minutes and found no newer resolution than the earlier report. Opened the November PDF, the [September OpenAI manuscript](https://mathcommunity.github.io/oai-math-revised/papers/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf), and [arXiv:2610.07454](https://arxiv.org/abs/2610.07454) by Emile Averous, Hugo Duminil-Copin, Tiancheng He, Piet Lammers and Ioan Manolescu. No full-range solution was certified. The earlier folder contained no PROOF.md or scripts; its theorem-scope summary and parameter identities were independently rechecked.

Verification command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 check_surgery.py
```

[check_surgery.py](check_surgery.py) uses exact integer and rational arithmetic. It passed 72 row-insertion comparisons, 12 rectangle comparisons, checks at c=1/2, hand formulas for a single vertex and the balanced 2x2 torus, 348 direct gluing-map images, and 30 direct insertion checks. Every image was checked for seam compatibility, balanced flux, and preservation of weight. The largest matrix has dimension 20. Final runtime was about 0.17 seconds and measured peak resident memory 14,925,824 bytes. The nice launcher reports a failed priority change because priority is already inherited at nice 20; the script prints that value. Full outputs and the coefficient audit are in [LOG.md](LOG.md).

What failed or remains uncertain: the direct September PDF open initially failed; its landing-page link worked. An initial diagonal-selection formulation used insufficient individual-pattern error control; the final proof uses total variation on the entire finite marginal. No remaining failed finite checks. Global novelty of this elementary minimisation lemma is not claimed. Neither the November uniqueness argument nor the September root/correlation and GFF arguments have been verified. The minimisation lemma itself does not require either manuscript.

Next worker: audit the November Corollary 1.3 and its dependencies. If sound, combine it with this proof to certify auxiliary-state existence and identification, then examine the September correlation argument separately. Do not infer GFF convergence from state identification alone.

Task: “take the NEXT checkable step on this problem, building on that work” (T063); received about 01:07 Asia/Tbilisi, 15 November 2026.
