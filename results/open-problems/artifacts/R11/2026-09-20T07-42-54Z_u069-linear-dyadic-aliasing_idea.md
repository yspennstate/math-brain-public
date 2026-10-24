# R11 / I0054 idea-before-code: critical-scale dyadic logit oscillation

Methods being tried this run: **#6 deform to a solvable point, #17 look for the numbers somewhere else, #24 find the extremal object.**

Starting point is U068/C086.  On the active logit interval `[0,L)`, `L=log 4`, C086 uses

\[
S_N(y)=b_N y \pmod L,
\]

with `b_N=2^{floor((log_2 N)/2)}=O(sqrt N)`.  The previous proof is pure bounded-variation quadrature and therefore only uses `b_N=o(N)`.  That restriction may be an artefact of the proof rather than the model.

## New route

Try the genuinely critical sampling scale

\[
b_N=2^{\lfloor \log_2 N\rfloor}\asymp N,
\]

so the number of Bernoulli-shift branches is of the same order as the number of harmonic-grid sample points.  The BV estimate no longer tends to zero.

For a fixed specified split `(i,j)`, after writing the active contribution in logit coordinate and Fourier-expanding the one-periodic observable, the nonzero Fourier modes reduce to weighted exponential sums of the form

\[
\frac1N\sum_{s\in [N/2,4N/5]}
 w(s/N)\exp\!\left(i\,t_N\log\frac{s}{N-s}\right),
\qquad t_N\asymp k b_N,
\]

with smooth bounded weight `w` and fixed nonzero Fourier index `k`.

When `b_Nasymp N`, this is a discrete nonstationary/stationary-phase problem rather than a Riemann-sum problem.  Writing

\[
f_N(s)=t_N\log\frac{s}{N-s},
\]

one has away from the endpoint `s=N/2`

\[
f_N''(s)=t_N\left(-\frac1{s^2}+\frac1{(N-s)^2}\right),
\]

so on fixed subintervals bounded away from `N/2`, `|f_N''|asymp b_N/N^2asymp 1/N`.  A van-der-Corput second-derivative estimate should give an unnormalized sum `O(sqrt N)` and therefore normalized error `O(N^{-1/2})`.  The `N/2` endpoint is the only degeneracy because `f_N''=0` there; there `f_N'''asymp b_N/N^3asymp N^{-2}`, suggesting a third-derivative / short-interval split, still giving `o(N)`.

A cleaner proof may avoid the third-derivative endpoint issue by splitting off `[1/2,1/2+delta_N]` with `delta_N -> 0` but `N delta_N -> infinity`; its normalized contribution is `O(delta_N)`.  On the remainder, second derivative has lower bound `asymp b_N delta_N/N^2`.  Choosing `delta_N=N^{-1/4}` should make the van-der-Corput error vanish.

More generally this suggests an oscillatory compiler for `b_N -> infinity` well beyond the old `b_N=o(N)` regime, plausibly at least `b_N=O(N)` and possibly all `b_N=o(N^2)` after optimizing the split.

## Negation / extremal test

The failure mechanism should be **aliasing**, not variation growth.  If `b_N` becomes too large, the phase increment between adjacent harmonic-grid points can cross many periods; this does not itself imply failure because oscillatory cancellation may improve.  To locate a true obstruction, inspect the discrete phase condition

\[
t_N\,\frac{d}{ds}\log\frac{s}{N-s}\approx 2\pi m.
\]

Poisson/stationary-phase resonances should contribute only `O(N^{-1/2})` after normalization when nondegenerate, so isolated resonances do not destroy convergence.  A genuine failure would require a macroscopic near-lattice lock, which seems unlikely for the nonlinear logit phase.  This is why linear branch complexity may still converge.

## Candidate new hierarchy C087 if the proof closes

Use the same compact doubling map `D(y)=2y mod log 4` on `[0,log 4)` and identity outside, but iterate

\[
r_N=\max\{1,\lfloor\log_2 N\rfloor\}
\]

times.  Then `b_N=2^{r_N}` satisfies `N/2 <= b_N <= N` for `N>=2`.  Harmonic-grid clocks remain `N/[2s(N-s)]`; each proposal colors leaves iid with bias `sigma(D^{r_N}(logit(s/N)))`.

If the exponential-sum bound closes for every fixed split type, hidden-label lumpability and finite-state uniformization from U068 give the full finite-restriction path limit to CTCS(infinity).  A finite root-topology/rate-ratio witness will then separate C087 from source CTCS and, at a size where its branch count differs from C086, from C086 as well.

No theorem claim is made in this idea file.  Next step is to prove the oscillatory bound on paper, then only if it closes write a checker for the finite witness and elementary algebraic identities.