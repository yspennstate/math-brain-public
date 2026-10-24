SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-23T08:34:34Z.
attacking: the first unpaid rough-input implication after the ruled one-sheet theorem: pay heat modes separated from the critical value, and test whether the newest Gaussian-mode posterior condition can by itself close the critical/two-sheet side.

# Early substantive checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target status: **OPEN**. Execution context: `WITHOUT_VERIFIED_BRAIN`.

The completed ruled result at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, gives for an exact rank-three affine-completed signature `(2,1)` block with eigenvalue magnitudes at least `kappa` a majority-side submeasure density cap

\[
C_+\le \pi\sqrt2/\kappa.
\]

The newest compatible partner result actually used is account03/B15 at `math-open-problems@30e0239b97649cbaa02bd11bd3bd5a5bd514b5f0`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260923T073059Z-account03-B15-qform-auto15/REPORT.md`. At every global Gaussian heat mode `y_*`, with posterior residual `U=(Q-y_*)/epsilon`, it proves

\[
E e^{vU}\le e^{v^2/2}\quad(v\in\mathbb R),\qquad EU=0.
\]

Let `c` be the critical value and suppose `d=(y_*-c)/epsilon>0`, so the heat mode lies on the ruled/majority side. If `alpha` denotes posterior mass on `{Q>=c}`, then

\[
H_+(y_*)=\alpha H(y_*)\le C_+.
\]

The partner subgaussian bound gives `alpha>=1-exp(-d^2/2)`. More sharply for `0<d<=e^{-2}`, write

\[
d(1-\alpha)\le E U_+\le \alpha T+\int_T^\infty e^{-t^2/2}dt
\le \alpha T+e^{-T^2/2}/T.
\]

With `T=sqrt(2 log(1/d))>=2`, this yields

\[
\alpha\ge {d(1-1/T)\over T+d}\ge {d\over 3T}.
\]

Hence the actual heat height is paid away from the critical value:

\[
\boxed{\kappa H(y_*)\le {\pi\sqrt2\over1-e^{-d^2/2}}}
\]

for every `d>0`, and in the near-critical majority regime

\[
\boxed{\kappa H(y_*)\le {6\pi\sqrt{\log(1/d)}\over d}}
\qquad(0<d\le e^{-2}).
\]

This is a real inequality obtained by composing the specified completed ruled theorem with the completed partner mode theorem. It does not use continuity to infer height.

The remaining local obligation is now modes at the critical value or on the minority/two-sheet side. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction still applies.

A source-valid abstract obstruction shows the partner posterior condition alone cannot bridge that endpoint. For `0<p<=1/4`, put `a=3p/[4(1-p)]` and define a centered probability density `nu_p` with mass `1-p` uniform on `[-3a/2,-a/2]` and mass `p` uniform on `[1/2,1]`. Its support has diameter at most `11/8<2`; Hoeffding's lemma gives

\[
E_{nu_p}e^{vU}\le e^{v^2/2}.
\]

Let `gamma=gamma_1`, `M_p=\int gamma(u)^{-1}dnu_p(u)`, and define

\[
d\mu_p(u)={1\over M_p\gamma(u)}d\nu_p(u).
\]

Then `mu_p` is an absolutely continuous compactly supported probability law, its Gaussian posterior at zero is exactly `nu_p`, and the partner equivalence implies zero is a global heat mode. Moreover

\[
H_p(0)=(\mu_p*\gamma)(0)=1/M_p\to\gamma(0),
\]

whereas the density of the positive-half-line submeasure is bounded by

\[
C_p={2p\over M_p\gamma(1)},
\qquad
{H_p(0)\over C_p}={\gamma(1)\over2p}\to\infty.
\]

Therefore no inequality `heat height at a global mode <= K * majority-side density cap` follows from absolute continuity plus the exact 1-subgaussian Gaussian-posterior condition. This is **not** a QFORM counterexample; it refutes only that proof interface. Product-provenance-sensitive two-sheet geometry remains necessary at critical/minority modes.
