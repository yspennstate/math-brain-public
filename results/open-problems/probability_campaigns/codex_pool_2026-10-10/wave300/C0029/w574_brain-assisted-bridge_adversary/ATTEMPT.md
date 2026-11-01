# C0029: independent adversarial checkpoint

## Independent obstruction S1.w574.1

Saved before reading w573's proof or any other worker's candidate proof. For n>=1 take X_n uniform on [0,n/(n+1)]. Its distribution function on t>=0 is F_n(t)=min((1+1/n)t,1). Thus F_n(t)<=(1+1/n)t uniformly in t. At t_n=1/n, n>=2, F_n(t_n)-t_n=1/n^2. This exceeds C exp(-cn) eventually, for every fixed c,C>0.

Consequently a theorem with a uniform 1+o(1) coefficient cannot, by deleting that coefficient, yield coefficient one with an exponentially small additive error. The missing input must control the excess on intermediate shrinking thresholds. These X_n are an implication counterexample, not singular values of Bernoulli matrices. The precise source and target hypotheses remain to be recovered.

## Recovered target and source scope

Let B_n be an n by n real matrix of independent entries, each uniform on {-1,1}, and let s_min(B_n)=min_{||x||_2=1}||B_n x||_2. C0029 asks for a base rho in (0,1) and an integer n_0, independent of t, such that P(sqrt(n) s_min(B_n)<=t)<=t+rho^n for every n>=n_0 and every t>=0. The original source is Spielman--Teng, ICM 2002, Conjecture 2, printed page 605 (arXiv math/0212413, PDF page 9). It uses an inverse-norm tail; passage to non-strict singular-value thresholds uses continuity from above. Singularity is included at t=0.

Sah--Sahasrabudhe--Sawhney, arXiv 2405.20308v2, Theorems 1.1--1.2, applies to a fixed real iid centered variance-one subgaussian entry law. It has a uniform multiplicative error bounded by a law-dependent constant times (log n)^(-1/16), and an exponentially small additive error. It covers the entry law needed here, but its coefficient does not equal one. Primary quote (Theorem 1.1): "where the $o(1)$ term decays as $C_{\\xi}(\\log n)^{-1/16}$". Current exact-constant openness: UNKNOWN; the checked 2025 theorem does not settle it and a bounded recent search found no newer resolution.

## Independent rescaling obstruction S1.w574.2

This derivation was saved before reading w573's proof. It tests the signed rescaling step in SSS Lemma 9.2 rather than redoing the paired prover's Gaussian-slack computation.

Let Z be a standard real Gaussian, R>=0 finite almost surely and independent of Z, and h(t)=P(|Z|<=tR), t>0. Put a=sqrt(2/pi). Conditioning on R gives

    h(t)/t = a E[integral_0^R exp(-t^2 u^2/2) du].

The integrand decreases as t increases. Consequently h(t)>= (t/t0) h(t0) whenever 0<t<=t0, with strict inequality if t<t0 and P(R>0)>0. A bound in the opposite direction with no remainder cannot follow from Gaussian concavity. If E[R^3]<infinity, subtraction of these integrals and 1-exp(-v)<=v yield the precise repair

    0 <= h(t) - (t/t0)h(t0)
       <= a t (t0^2-t^2) E[R^3]/6.

The SSS statement includes a spectral cutoff s_(n-1)(M*) >= (log n)^(-1) n^(-1/2) and an O(delta_n t) remainder. Neither can be discarded. This is not an objection to that published lemma; it is an obstruction to an exact-zero-remainder strengthening.

## Unconditional moment obstruction S1.w574.3

For the one-row 1 by 2 Gaussian matrix M*=(A,B), take R_0=sqrt(A^2+B^2), the nonzero singular value. Let W be an independent standard real Gaussian and R=|W|/(sqrt(2) R_0). R is the untruncated rescaling radius n^(-1/2) chi(Z) for n=2. The radial density of R_0 is r exp(-r^2/2), r>0; hence E[R_0^(-3)]=integral_0^infinity r^(-2) exp(-r^2/2) dr=infinity, and E[R^3]=infinity. For each fixed full-rank M*, the conditional third moment is finite. Thus conditional finiteness alone does not justify the averaged cubic-error estimate in S1.w574.2. A deterministic spectral cutoff or an integrable moment bound is a minimal missing premise for that route.

This small-dimensional example is a counterexample to an unconditional-moment inference, not to the large-n Bernoulli conjecture. No novelty or parent-problem solution is asserted. The independent referee is w575; checks and served-model evidence remain pending.

## Measured math-brain failure S1.w574.4

Command: python -X utf8 scoped_recall.py. The live store was opened mode=ro/query_only. Exactly 34 title-matching nodes were passed to the native retrieval engine; no whole-store iteration or global graph traversal was used. Query 1 returned the C0029 attempt at rank 1. Its exact sentence is: "For the Gaussian matrix Edelman's exact law gives P(sqrt n s_n <= t) = 1 - e^{-t^2/2 - t} ~ t as t -> 0". The card is explicitly an author-checked, unverified concept; this is a mathematical statement correction, not evidence that the engine promoted it to a theorem.

The finite-n identity is false: for n=1, sqrt(n) s_min(G_1)=|Z| and its CDF is sqrt(2/pi) integral_0^t exp(-u^2/2) du. Its derivative at zero is sqrt(2/pi), whereas 1-exp(-t-t^2/2) has derivative one. The latter is the hard-edge limiting distribution; finite-n or polynomial approximation errors must remain explicit. The minimal repair is a small correction concept linked to the archival attempt, preserving its historical provenance. Numerical evaluation is an optional arithmetic check, not the proof.

Query 2, for independent Gaussian random-radius rescaling with third-moment and spectral-cutoff control, returned a generic anti-concentration definition at rank 1. None of its top-five cards supplies the signed rescaling identity and its moment hypothesis. The bounded proposed repair adds that exact bridge as a DRAFT concept and measures whether the same query can retrieve it. Two probes cannot establish a global recall improvement.

## Paired proof boundary

After the independent derivations above were saved, w573/CLAIMS.jsonl was read. Its first claim concerns the same coefficient-removal implication as S1.w574.1; the inference obstruction is supported by the explicit continuous-CDF witness here. Its unfinished gap is Gaussian finite-n slack. No full paired proof was available at this checkpoint. The disjoint adversarial lane here is the signed rescaling remainder and the cutoff needed before averaging. Exact large-n Bernoulli coefficient one remains the hardest unchecked piece.

NEXT: Measure the targeted DRAFT overlay, complete exact-edge evidence and the paired-proof audit, and submit the review packet to w575.
