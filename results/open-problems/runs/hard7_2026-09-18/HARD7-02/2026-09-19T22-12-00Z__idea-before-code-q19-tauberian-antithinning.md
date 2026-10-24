Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. **Frozen metric at entry: `T_corr=4`. Planned methods: B5/B11/B30, different from the preceding B8/B16/B26 triple. This checkpoint is the mathematical idea before code; no new theorem is certified by this file alone.**

# HARD7-02 idea checkpoint — Q1.9 Tauberian anti-thinning route

Target remains the exclusively claimed Campbell--O'Rourke (2022) Question 1.9 in `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md`:

> **Question 1.9.** How does the tail behavior of `mu_{alpha,theta_d}` vary with respect to `theta_d`?

The newest completed HARD7-02 report proves, on page but without independent audit, two inputs for every C2 angular probability law with positive off-axis mass:

1. for every `0<p<alpha`, the radial `p`-moment is finite, hence with `F(r)=mu_{alpha,theta}({|z|>r})` there is a finite `M_p` such that

   `F(r) <= M_p r^(-p)`;

2. there are `A>0` and `r_0<infinity` such that the integrated radial tail

   `V(r):=int_r^infinity F(t) dt/t`

   obeys

   `V(r) >= A r^(-alpha)` for `r>=r_0`.

The preceding run used these only to show divergence of the critical `alpha`-moment. The new question is whether these two facts force a substantially sharper *pointwise* lower tail, ruling out arbitrarily thin `r^{-alpha+o(1)}` profiles.

## B5 — add a scale parameter

For `delta>0`, set

`R=r^(1+delta)`.

Choose any

`p in (alpha/(1+delta), alpha)`.

Then the subcritical moment bound gives

`V(R) <= (M_p/p) R^(-p) = (M_p/p) r^(-(1+delta)p) = o(r^(-alpha))`.

So for each fixed `delta`, eventually the part of the integrated tail beyond `R` consumes at most half of the lower signal `A r^{-alpha}`.

## B11 — dualize integrated tail into pointwise tail

Since `F` is nonincreasing,

`V(r) = int_r^R F(t)dt/t + V(R)`
`     <= F(r) log(R/r) + V(R)`
`     = delta F(r) log r + V(R)`.

Once `V(R) <= (A/2) r^{-alpha}`, the lower bound on `V(r)` forces

`F(r) >= [A/(2 delta)] r^(-alpha)/(log r)`.

Crucially `delta>0` is arbitrary. Therefore for every prescribed `L<infinity`, choose `delta < A/(2L)` and then the associated `p`. The threshold in `r` may depend on `L`, but eventually

`r^alpha (log r) F(r) >= L`.

The proposed theorem is thus the qualitative anti-thinning law

`lim_{r->infinity} r^alpha log(r) F(r) = +infinity`.

This is stronger than the previously proved logarithmic power exponent `alpha` and stronger than mere divergence of the critical moment. It still does **not** prove regular variation or a sharp tail constant.

A direct corollary would be quantitative critical-moment divergence. If

`Q_alpha(R):=int min(|z|^alpha,R^alpha) mu(dz) = alpha int_0^R t^(alpha-1)F(t)dt`,

then for every fixed `L` the pointwise lower bound gives

`Q_alpha(R) >= alpha L (log log R - O_L(1))`,

hence, if the proposed theorem is correct,

`Q_alpha(R)/(log log R) -> +infinity`.

## B30 — localize one radial scale at a time

The scale interval `[r,r^(1+delta)]` is the gluing unit. The proof does not infer a pointwise tail from finite matrices or simulations: it localizes the already proved limiting-law integral `V(r)`, makes the remote tail negligible using one source-valid subcritical moment, and uses monotonicity of the exact limiting radial tail on the remaining annulus.

## Counterexample-first stress test

A tail such as `F(r)=r^(-alpha)/(log r)` has the same logarithmic power exponent `alpha` and an infinite critical moment, so those two previously known facts alone would permit it. But its integrated tail is asymptotic to a constant multiple of `r^(-alpha)/(log r)`, contradicting the uniform lower signal `V(r)>=A r^(-alpha)`. Thus the previous integrated-tail estimate genuinely forbids this natural counterexample profile.

The same argument does **not** rule out profiles such as `F(r)=r^(-alpha)(log log r)/(log r)`, so an exact `c r^{-alpha}` lower bound is not being claimed.

## Metric discipline

The fixed source metric remains `T_corr=4` at this checkpoint. The preceding global theorem already covers all positive-off-axis C2 families, so merely naming another covered family would be bookkeeping rather than new metric movement. If this run proves only the anti-thinning law, the final report will honestly record `T_corr=4 -> 4 (no movement)` while preserving the stronger new quantitative tail statement as substantive mathematical progress.

No checker has yet been written. The next step is to verify the scale inequalities symbolically, then write the full on-page proof and refresh source/current-literature/ownership status. Question 1.9 remains OPEN unless the source's full tail dependence is actually classified.
