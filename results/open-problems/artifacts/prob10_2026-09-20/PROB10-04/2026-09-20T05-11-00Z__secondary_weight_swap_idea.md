# PROB10-04 new route — use secondary-weight maximality to unlock one-rescue swaps

The heterogeneous Hamming-improvement compiler written earlier in this run still requires a center with at least two `nu` copies: with `j` rescued leaves the ordinary Hamming gain is `j-1`, so `j=1` was invisible.  The source's degree distribution, however, contains many more `t_{i,1}` centers than the rare diagonal `t_{r,r}` family.  The way around the zero Hamming gain is to change the extremal representative, not the formula model.

## Lexicographic extremal representative

Among all flat-satisfying assignments of a fixed simple formula, first maximize the number of true light variables.  Among those Hamming maximizers, maximize a secondary additive potential

`W_K = number of true light variables whose post-unbalancing degree class is (k,1) with k>K`.

Every satisfiable formula has such a representative.  Because the first coordinate is Hamming weight, it is still a single-flip/blocked representative of the kind used in the Diaz count.

Fix `1<=i<=K`.  Consider a true center `y` of class `t_{i,1}` with

- all `i` `ps` copies in multiply-satisfied safe clauses (`Q_safe` from the preceding idea), and
- its unique `nu` copy in a canonical `nu` slot of a negative-unique-satisfied blocker (`B_can`).

Suppose the corresponding blocker `ns1` slot is occupied by the unique negative copy of a false leaf `x` of class `f_{k,1,1}` with `k>K`.

Flip `y:1->0` and `x:0->1`.

Exactly the same deterministic clause check as in the previous rescue lemma shows that satisfiability is preserved: the center's `nu` occurrence rescues the leaf's only endangered clause; every positive leaf occurrence becomes true; every center `ps` loss occurs in a clause that had another satisfied literal, and that other literal cannot be the leaf's disappearing `ns1` because an `ns1` clause had only one satisfied literal before the move.

The Hamming weight changes by `+1-1=0`, so the new assignment remains a Hamming maximizer.  But `W_K` changes by `+1`: the leaf class has `k>K`, whereas the center class `(i,1)` has `i<=K` and contributes zero.  This contradicts secondary maximality.

Therefore a lexicographically maximal representative contains **no such one-rescue swap**.

## Exact matching penalty

Let

`E_{>K} = sum_{k=K+1}^M f_{k,1,1}`

and retain the pools `P,Q_safe,U,B_can,L1` from the preceding negative-association compiler.  For a `t_{i,1}` center with `i<=K`, the exact one-center completion factors are

`a_i=(Q_safe)_i/(P)_i`,

`b_1=B_can/U`,

`e_K=E_{>K}/L1`.

The same sampling-without-replacement negative-association proof now gives the finite bound

`P(no secondary-improving one-rescue swap)`
` <= product_{i=1}^K (1-a_i b_1 e_K)^{C_{i,1}}`.                (SWAP-K)

At a fixed interior type this yields the explicit asymptotic correction

`J_K(x) = -sum_{i=1}^K t_{i,1}(x) log(1-q(x)^i d_K(x))`,

where

`q=Q_safe/P`, `d_K=(B_can/U)(E_{>K}/L1)`.

This is **first order** in the blocker/leaf factor rather than quadratic or higher.  It is therefore potentially orders of magnitude larger than the Hamming-improving `j>=2` correction.

## Exact missing lemma for a source endpoint

The local theorem above is not yet a new threshold decimal.  To turn it into `alpha_U<4.4898`, the remaining obligation is now precise:

> Reconstruct the Diaz `M=23` objective and feasible polytope with outward interval arithmetic, add `J_K` to `-log F`, and certify the **global** refined maximum (including all boundary/grid boxes) below one at some explicit density `<4.4898`.

The old source maximizer can move after the correction; evaluating `J_K` only at the printed saddle is not a global proof.  This is the next computation worth doing if the rounded-saddle diagnostic shows a correction comparable to or larger than the source's published exponential margin.