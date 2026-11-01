# PROB10-02 / R17 third idea-before-code — eliminate persistent one-sided debt by an exact Snell envelope

The first two candidate pivots in this run were rejected before implementation for substantive reasons rather than silently rotated away. (1) The forced-clear/bounded-imbalance SMDP is a fixed diagonal-strip process and duplicates the P13 / Chia--Bundschuh finite-width route. (2) A bounded scalar cylinder-gradient upper dual is forced to the trivial value 1 by periodic matching environments; the natural finite-state closed edge-cocycle relaxation numerically shows the same obstruction and is being treated as an obstruction, not an endpoint claim. A defect relaxation immediately turns into a cycle-hitting/cover problem of the kind already owned by P02. R17 therefore returns to its distinct one-sided information-debt route from the 10:46 report, but changes the mathematics inside that route.

## Exact debt elimination observation

Recall a debt state `A_u=(a,b,A_u)`: the next X bit `u` has already been exposed but not consumed. While `head(a) != head(b)`, the exact debt Bellman branch is

`max{ consume X using u and return to N, advance Y using a fresh source bit and keep A_u }`.

If the heads agree, matching them is safe and the debt is consumed. Crucially, **while the debt persists, `a` and the exposed bit `u` are frozen and only the Y window shifts**. Thus the debt coordinate is not a generic two-dimensional Bellman process. For every fixed `(a,u)` it is a one-dimensional optimal stopping problem on the binary de Bruijn shift of `b`.

For an average-reward candidate `rho` and an ordinary-state potential `H(a,b)`, let `b_t` be the Y window after `t` successive Y shifts, with genuine fresh iid fair refill bits, and let

`T = inf{t>=0 : head(b_t)=head(a)}`.

At any mismatch time `t<T` the controller may stop by consuming X. Waiting until `T` forces a match. Therefore the minimal debt potential compatible with the Bellman subsolution is the Snell envelope

`D_{a,u}(b) = sup_tau E[ terminal_H - rho * (# Bellman microsteps) + terminal_match_reward ]`,

where `tau` ranges over causal stopping times bounded by the first match `T`: stopping at a mismatch time `t<T` gives

`H(sigma_u a,b_t) - (t+1) rho`,

while waiting to the first match gives

`1 + H(sigma_u a,b_{T+1}) - (T+1) rho`.

This is exactly equivalent to the debt-state Bellman inequalities; it does not resample the exposed bit and does not change the source law.

## Geometric tail and a proved truncation target

For any formal starting window `b`, after at most `ell` Y-shifts every old head symbol has left the window. Conditional on surviving to that point, each subsequently exposed head is a fresh fair bit. Hence for `H>=ell`,

`P(T>H) <= 2^{-(H-ell+1)}`.

If `S=span(H)` then the extra value obtainable by allowing the stopping problem to continue beyond horizon `H` is bounded explicitly by a geometric-tail term of order

`2^{-(H-ell)} * (S + 1 + O(rho))`.

The run will derive a sharp version of this inequality. This gives a rigorous finite approximation to the *persistent* debt state, rather than imposing a false finite memory. It is exactly the kind of finite-to-infinite error missing from earlier finite calculations.

## Three concrete attacks in this method

1. **Exact Snell equivalence.** Prove both directions: every full debt subsolution restricts to an ordinary potential whose debt coordinates dominate the Snell envelope, and adjoining the Snell envelopes to an ordinary potential gives the least debt extension satisfying all debt-state inequalities.
2. **Finite-horizon truncation with explicit error.** Define `D^(H)` by forced X-clear at horizon `H`; prove monotonicity `D^(H)<=D` and an explicit uniform upper bound on `D-D^(H)` using the first-match geometric tail and the span of `H`.
3. **Separation/compression test.** Use the eliminated form to evaluate ordinary-state residuals without storing debt as independent optimization variables, and test whether states with the same deterministic prefix-to-first-match profile can be lumped for the *inequality* problem. Preserve a smallest exact counterexample if terminal `H` values prevent such lumping.

The source endpoint moves only if an exact subsolution obtained through this elimination gives `rho > 99083249/150916751`, equivalently `2rho/(1+rho)>0.792665992`. Otherwise the theorem and error bound are recorded only as auxiliary mechanism progress. Status stays OPEN/PARTIAL.