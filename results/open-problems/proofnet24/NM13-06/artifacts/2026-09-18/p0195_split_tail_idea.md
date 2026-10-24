# P0195 split-graph blocker: finite Bernstein tail route

Date: 2026-09-18 UTC
Track: `proofnet24/NM13-06`
Source: P0195, LPW ferromagnetic Ising spectral-gap edge-addition clause
Frozen metric: `n_edge^* >= 6`

This is an idea note written before the checker.

The mandatory stuck-recovery report isolated the unique densest unresolved cutwidth tie

- `G = K_3 \vee 3K_1`, canonical six-vertex mask `4095`,
- `H = G + {b_1b_2}`, mask `8191`.

The remaining unused Section-B methods on P0195 are #8, #27, #28.

## #8 GO THE OTHER WAY AND DISCRETIZE

Use `x=tanh(beta)` and then the low-temperature coordinate `t=1-x`.  The true second eigenvalue of each endpoint is already known from the track's monotone-eigenfunction plus spin-flip/automorphism-averaging lemma to occur in the odd automorphism quotient.  For this pair the quotient dimensions are 8 and 12.

Instead of a degree-520 cross-resultant over the whole temperature interval, try a finite Bernstein certificate on a compact tail `0<=t<=1/10`.  A single rational barrier

`q(t) = 1 - t^7/32`

would prove `lambda_2(H)>lambda_2(G)` if one can certify simultaneously:

1. each odd quotient has exactly one eigenvalue above `9/10` throughout the tail;
2. `f_G(1-t,q(t))>0` and `f_H(1-t,q(t))<0` for `0<t<=1/10`, where `f_G,f_H` are the cleared odd-quotient characteristic polynomials.

Both claims can be reduced to signs of univariate rational polynomials on `[0,1/10]`; convert those polynomials to the exact Bernstein basis on that interval and require every Bernstein coefficient to have the asserted sign.

The endpoint asymptotics suggest this barrier is natural: implicit expansion at `(x,L)=(1,1)` gives candidate gap leading terms `9/160 * t^7` for `G` and `9/608 * t^7` for `H`, while `1/32` lies strictly between them.

## #27 SWAP THE QUANTIFIERS

Do not attack all 399 remaining marked six-vertex transitions for all temperatures.  Instead, fix this one maximally symmetric unresolved marked type and seek a theorem uniform over an explicit temperature tail.  That is a source-valid restricted theorem and directly addresses the blocker selected by the mandatory stuck recovery.

## #28 REPLACE FOR ALL WITH FOR TYPICAL

As route selection only, inspect a generic intermediate temperature (`x=1/2`) across all 402 connected six-vertex marked edge-addition types.  If every sampled comparison has the desired sign, record the minimum numerical margin and its marked type, but do not call that finite floating-point census a theorem or metric movement.  Its only purpose is to decide whether the blocker-tail proof is worth pursuing versus returning to counterexample search.

If the exact Bernstein signs pass, archive a checker and output and state only the proved tail theorem.  Do not infer full all-temperature monotonicity for the blocker and do not move `n_edge^*`.