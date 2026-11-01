# PROB10-04 idea before code — global annulus certification after the local covariance-transport compiler

Runtime model: **GPT-5.6 Sol; reasoning level UNVERIFIED**.  This is an idea-first artifact, not a threshold claim.

## Frozen source/model state

Exact source model: `m=floor(alpha n)` iid uniformly sampled proper signed 3-clauses on `n` Boolean variables, with three distinct variables per clause and independent fair literal signs.  External explicit-decimal bracket tracked by this lane remains `[3.52,4.4898]`, width `0.9698`; neither finite SAT experiments nor the neighboring unaudited interpolation candidate move that external metric here.

Scoped ownership remains the PROB10-04 cluster-aware weighted-counting / overlap-variational route in `operations/claims/PROB10-04.md`.  The pre-refocus HARD7-06 F0095/binary-cascade work remains frozen in its immutable handoff and is not relabeled as 3-SAT progress.

## Inherited exact reduction

Write the remaining Diaz outer exponent as

`Phi(y)=K(y)+V(y)+C(y)+const`, `y=(u,v,w)`,

where `V,C` are finite-support maximum-entropy value functions.  On the interior,

`nabla^2 Phi = H_copy - Sigma_V^{-1} - Sigma_C^{-1}`.

The previous run proved an exact finite-support covariance-transport theorem and an inverse-free split certificate.  At the inherited rationalized saddle surrogate a fixed split certifies strict concavity on the Euclidean mean ball `||y-y0||<=0.0015`.  A single center cannot globalize because the variable covariance transport becomes vacuous after finite mean displacement.

## Three materially different nonexhausted attacks for this run

### A. Mean-dependent covariance domination (global theorem attempt)

Do not use the already-failed support-only Popoviciu shortcut.  Instead exploit the *known mean* `y` inside each finite support block.  For a scalar projection `X=x·S` with support interval `[a,b]` and mean `m`, Bhatia-Davis gives

`Var(X) <= (b-m)(m-a)`,

which can be much smaller than `(b-a)^2/4` near exposed faces.  The exact target is a matrix/dual version strong enough that for every `y` in the projected intersection polytope,

`x^T Sigma_V(y) x <= B_V(y,x)` and `x^T Sigma_C(y) x <= B_C(y,x)`

with computable mean-dependent bounds, and then a variational split in `x` proves

`x^T H_copy(y)x < x^T Sigma_V(y)^{-1}x + x^T Sigma_C(y)^{-1}x`.

**Missing lemma A:** derive a finite-support mean-dependent quadratic covariance majorant whose inverse lower bound can be optimized exactly in three dimensions and that beats the known support-only counterdirection.  Falsification criterion: exhibit one feasible `(y,x)` where the best such blockwise Bhatia-Davis/S-procedure relaxation still fails the copy curvature.

### B. Recentered certified-ball cover (constructive global proof route)

Use the exact mean-space covariance transport locally, but allow a new split matrix `T_j` and new Gibbs center at each recentering point.  The support oracles `h_V,h_C` first prune boxes not meeting the projected polytope.  For a surviving box, solve the two three-parameter Gibbs inverse maps at its center, construct the parallel-sum split, and use transport to certify the entire box/ball.

**Missing lemma B:** a finite-cover theorem with a computable stopping rule: every feasible high-value point either lies in a certified negative-Hessian ball or belongs to a box on which an affine/convex upper bound certifies an exponent gap.  The proof must account for interval localization of every recentered Gibbs point; a floating cover is only diagnostic.

### C. Boundary-value gap instead of Hessian globalization

The local saddle is already strictly concave.  Rather than prove global concavity, try to show all possible competing maxima on the boundary are strictly lower.  Since `V,C` are concave Legendre transforms, any fixed natural parameters give affine upper bounds for them.  On a face of the copy simplex or an exposed face from `h_V/h_C`, this converts `Phi` to `K(y)+affine`, a convex function; its maximum on a compact face occurs at an extreme point.  One can therefore recursively reduce a boundary supremum to finitely many exposed face/extreme-point checks, provided the entropy singularities are handled correctly.

**Missing lemma C:** prove that the complement of a small certified saddle neighborhood can be reduced to finitely many boundary/exposed-face upper bounds with a strictly negative value gap.  Critical issue: a tangent upper bound for `V+C` is too loose in the interior (`Phi-Phi0 <= D_K`), so the reduction must force the optimizer onto a face or use several dual tangents (a lower envelope of affine entropy majorants).

## Planned mathematical order

1. First test route A analytically against the known bad support-only direction; if a mean-dependent inequality survives, pursue a complete proof.
2. Independently derive the multi-tangent boundary theorem in route C.  This is different from local Hessian transport and may certify the annulus even when global concavity fails.
3. Only then run a diagnostic recentered cover for route B to learn whether the high-value feasible set is geometrically small enough for an interval proof.  Code is diagnostic unless every outward bound is certified.

A successful run need not move the source endpoint, but it must either (i) prove one of the missing lemmas above, or (ii) leave a precise quantified obstruction showing which route fails and why.  The final report will keep theorem progress, diagnostic numerics, and source-metric movement separate.
