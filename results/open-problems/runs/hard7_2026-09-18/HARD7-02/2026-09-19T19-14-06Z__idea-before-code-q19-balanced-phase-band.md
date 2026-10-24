Model: GPT-5.6 Sol. Reasoning: UNVERIFIED; this run did **not** run on GPT-6 at verified maximum reasoning. Frozen source metric at entry: `T_corr=1`. Methods selected for this run: **B14 / B15 / B4**, different from the preceding B6/B11/B29 triple.

# HARD7-02 idea checkpoint before code — Q1.9 balanced-phase amplitude-band route

Status at checkpoint: **exploration only; no theorem promoted yet in this file.** Active exclusive claim remains `operations/claims/CAMPBELL-OROURKE-2022-Q1.9.md` for Campbell--O'Rourke Question 1.9.

The preceding run classified the fixed-amplitude two-orbit family `vartheta_x` and moved `T_corr` from 0 to 1. The present route tests whether that power-law exponent was an artefact of the rigid constraint `|W_1W_2|=constant`.

## New object before verification

Fix `0<alpha<2`, let `Phi` be Haar-uniform on the circle, and let `H` be independent of `Phi`, symmetric under `h -> 1-h`, with support in a compact band `[delta,1-delta]`, `0<delta<1/2`. Put

`W_H=(sqrt(H)e^{i Phi}, sqrt(1-H)e^{-i Phi})`,

and let `theta_H=Law(W_H)`.

The concrete second family to be frozen if the argument closes is

`H_delta ~ Uniform[delta,1-delta]`, `theta_delta=Law(W_{H_delta})`,

with `delta=1/4` as an exact worked slice. This has continuum amplitude support, so it is not a reparametrization of the previously classified two-point amplitude family.

## B14 — find the group acting

The circle action

`T_u(z,w)=(u z,u^{-1}w)`, `|u|=1`,

leaves `theta_H` invariant. The orbit invariant is

`zw=sqrt(H(1-H))`.

This suggests that the phase-Mahler peeling mechanism from the preceding run should survive after randomizing the amplitude: condition on `H`, average exactly over the Haar orbit, and only then average the invariant product. The determinant still has Laurent degree one in the selected edge phase.

## B15 — break the symmetry on purpose

Break the previous constant-product rigidity by making `H` genuinely random. If the same exponent survives, then the earlier theorem was not a sporadic consequence of a fixed reciprocal product. The uniform band is chosen because it is source-valid, visibly non-i.i.d./non-Hermitian, and has exact elementary values for `E H^(alpha/2)` and `E log sqrt(H(1-H))` at several rational `alpha`/`delta` choices.

The counterexample-oriented stress test is the following: if amplitude randomness can make `E log sqrt(H(1-H))` finite but very negative, does the determinant lower-tail argument lose the power exponent or only its constant? The working prediction is: only the constant changes, provided the logarithmic product moment is finite.

## B4 — prove a weaker statement completely

Rather than classify arbitrary `theta_d`, try to prove the following complete class theorem.

> Candidate theorem. For every `0<alpha<2` and every balanced-phase `theta_H` above with `H` bounded away from `0,1`, the limiting Campbell--O'Rourke law `mu_{alpha,theta_H}` has exact radial power exponent `alpha`:
>
> `lim_{r->infinity} -log mu_{alpha,theta_H}(|z|>r)/log r = alpha`.

A complete proof route appears available:

1. Use an exact Pareto-alpha representative `P(R>r)=r^{-alpha}`, normalization `a_n=n^(1/alpha)`, and `RW_H` off-diagonal pairs.
2. Prove all moments `p<alpha` uniformly at finite `n` from row-norm truncation. This gives the upper-tail exponent bound `liminf >= alpha`.
3. For exceedance edges `R>s n^(1/alpha)`, condition on `H=h`. The normalized reciprocal product is `q=s^2 sqrt(h(1-h))Y^2` with `P(Y>y)=y^{-alpha}`.
4. Reuse the exact Laurent determinant identity and Mahler middle-coefficient lower bound. For `X=Y^2` with density `beta x^{-beta-1}`, `beta=alpha/2`, the same interval argument should yield the uniform logarithmic anti-concentration bound `E log|X-c| >= -alpha` for all complex `c`.
5. Peel all isolated exceedance edges. Their density is asymptotic to `e^{-2/s^alpha}/(2s^alpha)`.
6. Circle-average by Jensen. The random amplitude contributes only `ell_H=E log sqrt(H(1-H))`, hence changes a radial constant but not the `s^{-alpha}` power.
7. Transfer the circular logarithmic potential to the limiting ESD using the `p<alpha` moment bound, then convert the integrated potential lower bound to a pointwise radial tail lower bound via a long multiplicative window `r` to `r^gamma`.

If each step checks, the explicit uniform-band family increments `T_corr` from 1 to 2 while the source Question 1.9 remains open.

## Source/status and ownership refresh before code

The governing files, root exclusion/ledger files, campaign INDEX/RANKING, active claim, newest own checkpoint, and the neighboring C0032 terminal handoff were re-read. Repository-wide searches still show Question 1.9 owned exclusively by HARD7-02; C0032 is the distinct i.i.d. heavy-tailed circular-law density target and is in terminal handoff.

Primary source remains Andrew Campbell and Sean O'Rourke, *Spectrum of Heavy-Tailed Elliptic Random Matrices*, EJP 27 (2022), paper 127, arXiv:2010.01261v3, Section 1.3, Question 1.9: `How does the tail behavior of mu_{alpha,theta_d} vary with respect to theta_d?`

A bounded fresh 19 September 2026 literature refresh using the exact title/authors, `Question 1.9`, `theta_d`, `mu_{alpha,theta_d}`, `tail behavior`, `heavy-tailed elliptic`, and 2023--2026 follow-up terms found the original source and later related heavy-tailed/sparse elliptic work but no located general resolution of Q1.9 or this balanced-phase amplitude-band class. This is bounded negative evidence only, not a novelty certificate.

No code or certificate has been written before this idea checkpoint.