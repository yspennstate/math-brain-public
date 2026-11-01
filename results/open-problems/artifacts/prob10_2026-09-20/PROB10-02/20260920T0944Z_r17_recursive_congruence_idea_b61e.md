# R17 PROB10-02 idea note — recursive Bellman congruence before archival checker

Target remains the true binary Chvátal–Sankoff constant.  This note fixes the mathematical route before persisting the checker; no independent-Bernoulli match model is introduced.

## Starting obstruction

The old C049 lower-side route reduced source movement to an exact `ell=22` Kiwi–Soto/Lueker/Heineman Bellman certificate with increment

\[
r>r_0:=\frac{99083249}{150916751},
\]

which transfers to a lower bound above `0.792665992`.  Complement/swap symmetry alone leaves `4,398,048,608,256` orbits at `ell=22`, so a dense symmetry quotient is still unusable.

## Attack 1 — recursive exact lumping, not another group quotient

Write the one-vector binary lookahead operator on `S_ell={0,1}^ell x {0,1}^ell` as

\[
(T_\ell h)(a,b)=1+\frac14\sum_{u,v}h(a^{(u)},b^{(v)})
\]
when the leading bits agree, and

\[
(T_\ell h)(a,b)=\max\left\{\frac12\sum_u h(a^{(u)},b),\frac12\sum_v h(a,b^{(v)})\right\}
\]
when they disagree.  Here `a^(u)` deletes the leading source bit and appends the fresh source bit `u`.

Define an equivalence `~_ell` recursively.

* If the leading bits agree in both states, delete those leading bits and compare the two tail pairs under `~_(ell-1)`; the common leading symbol itself is forgotten.
* If the leading bits disagree, identify exactly the orbit under simultaneous complement and string exchange.
* Never identify a leading-match state with a leading-mismatch state.

The intended theorem is that this is a Bellman congruence: every `~_ell`-constant potential is sent by `T_ell` to another `~_ell`-constant potential.  The key lemma to prove is right-extension compatibility: if `(alpha,beta)~_k(alpha',beta')`, then the multisets of `~_(k+1)`-classes of `(alpha u,beta v)` and `(alpha' u,beta' v)` over `u,v in {0,1}` agree.  On mismatch classes this follows by relabelling appended bits under complement/exchange; on match classes it reduces recursively to the same statement one level lower.

If this works, the class count obeys

\[
c_1=2,\qquad c_\ell=c_{\ell-1}+2^{2\ell-3}+2^{\ell-2},
\]

because the match classes are exactly the `c_(ell-1)` tail classes, while Burnside gives `2^(2ell-3)+2^(ell-2)` complement/exchange orbits on the leading-mismatch states.  Hence

\[
c_\ell=\frac{2\,4^{\ell-1}+3\,2^{\ell-1}+1}{3}.
\]

This would give `c_22=2,932,033,104,555`: an exact extra factor about `3/2` beyond the old complement/swap quotient, but still far too large for a dense `ell=22` solve.  Thus the theorem would both give a valid quotient and localize the remaining obstruction inside the mismatch-root sector.

## Attack 2 — attack the possibility of further plain behavioral lumping

Independently run ordinary exact partition refinement from the head-match/head-mismatch reward partition.  Compare its stable partition with `~_ell` for every exhaustively feasible small `ell`.  If refinement is strictly coarser, use the merger to strengthen the theorem.  If it agrees, record this only as finite evidence that ordinary bisimulation will not magically collapse the state space; do not extrapolate coarseness to `ell=22` without proof.

## Attack 3 — certificate-specific decision-diagram compression

The full Bellman congruence may be much larger than the particular potentials used in a lower certificate.  Therefore compute the exact integer iterate `h_29=T_ell^29 0` (common denominator `4^29`) and reduce its exact terminal array as an ordered algebraic decision diagram under three fixed variable orders: interleaved `(a_1,b_1,...,a_ell,b_ell)`, all-`a`-then-`b`, and reverse interleaved.  Count terminals and internal nodes exactly.  This tests the old C048/C049 BDD proposal on an actual Bellman iterate rather than on a generic function.

A finite node count is mechanism evidence only.  It is source progress only if a compact exact witness can be lifted through the known feasible-triplet transfer and crosses `r_0`.