# PROB10-04 idea before code — classify clause-local multiplicative weights before attempting cluster weights

Exact source model stays classical proper random 3-SAT. The source metric is the rigorously verified explicit bracket `[3.52,4.4898]`, width `0.9698`; this idea does not claim movement.

A natural cluster-aware program should first determine whether a simpler weighted second moment can already work. Consider

`X_w(F)=sum_{sigma in {0,1}^n} prod_{C in F} w_{N_C(sigma)}`,

where `N_C(sigma)` is the number of literals of clause `C` made true by `sigma`, `w_0=0`, and `w_1,w_2,w_3>0`. Then `X_w>0` iff `F` is satisfiable. This contains the standard true-surface exponential tilts but allows arbitrary positive clause-type weights.

For a pair of assignments with agreement fraction `q`, let `g_w(q)` be the one-clause expected product weight in the asymptotic proper-clause model, and let `A_w=(3w_1+3w_2+w_3)/8` be the one-assignment factor. The normalized overlap exponent is

`Phi_alpha(q)=H(q)-log 2 + alpha log(g_w(q)/A_w^2)`.

The planned exact calculation tests two necessary conditions for any successful Paley-Zygmund argument:

1. At `q=1/2`, one must have a stationary overlap exponent. I expect the derivative to collapse to a square and force one linear relation among the three weights.
2. Even after imposing stationarity, the identical-pair point `q=1` gives a diagonal obstruction. Optimize that obstruction over all positive weights.

If this universal diagonal barrier lies below the already rigorous `3.52` lower bound, then **every clause-local multiplicative weight of this form is structurally incapable of improving the source metric**. The next route must genuinely quotient/penalize whole solution clusters rather than merely reweight clause satisfaction types.

This is deliberately complementary to the current NM13-06 four-parameter constructive algorithm route.