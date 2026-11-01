# Repair of `lem:schur` for singular ambient matrices

Source pinned for review: manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, baseline commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`.

## Problem in baseline

The invertible part of Lemma `lem:schur` is correct. The final paragraph for singular `A` invokes the invertible result at the moving threshold `t-|epsilon|` and then appeals to continuity. That passage is not justified at a moving threshold.

## Replacement proof for the singular case

Let

`A = [[B,C],[C^T,D]]`, with `B` invertible, and `S=D-C^T B^{-1} C`.

Fix `t>0` and an arbitrary `delta` with `0<delta<t`. Choose a sequence `epsilon_m -> 0` such that:

1. `A_m := A + epsilon_m I` is invertible;
2. `B_m := B + epsilon_m I_k` is invertible (automatic for all sufficiently small `epsilon_m` because `B` is invertible);
3. `|epsilon_m|<delta/2`.

Let

`S_m := D + epsilon_m I - C^T (B+epsilon_m I)^{-1} C`.

Then `S_m -> S` in operator norm.

For every eigenvalue `lambda` of `A` with `|lambda|>=t`, the corresponding eigenvalue of `A+epsilon_m I` is `lambda+epsilon_m`, hence

`|lambda+epsilon_m| >= t-|epsilon_m| > t-delta`.

Therefore

`N_{A_m}(t-delta) >= N_A(t)`.

Apply the already-proved invertible case of the lemma to `A_m` at the **fixed** threshold `t-delta`:

`N_{S_m}(t-delta) >= N_{A_m}(t-delta)-k >= N_A(t)-k`.

Because `S_m -> S`, the ordered eigenvalues of `S_m` converge to those of `S`. If at least `q` eigenvalues of every `S_m` have modulus at least `t-delta`, then at least `q` eigenvalues of `S` have modulus at least `t-delta`. Hence

`N_S(t-delta) >= N_A(t)-k`.

Finally let `delta downarrow 0`. In finite dimension,

`N_S(t-delta) downarrow N_S(t)`

because an eigenvalue with modulus `<t` is eventually excluded while one with modulus `>=t` remains counted. Consequently

`N_S(t) >= N_A(t)-k`.

This proves the singular case with no change of statement, constants, or later arguments.

## Suggested literal manuscript replacement

Replace the baseline paragraph beginning “For singular $A$...” by:

> For singular $A$, fix $0<\delta<t$ and choose $\varepsilon_m\to0$ such that $A+\varepsilon_m I$ is invertible and $|\varepsilon_m|<\delta/2$. For all large $m$, $B+\varepsilon_m I$ is also invertible, and the corresponding Schur complements
> \[
> S_m=D+\varepsilon_m I-C^T(B+\varepsilon_m I)^{-1}C
> \]
> converge to $S$. Since every eigenvalue of $A$ of modulus at least $t$ is shifted by at most $|\varepsilon_m|$, we have
> \[
> N_{A+\varepsilon_m I}(t-\delta)\ge N_A(t).
> \]
> Applying the invertible case at the fixed threshold $t-\delta$ gives
> \[
> N_{S_m}(t-\delta)\ge N_A(t)-k.
> \]
> Passing to the limit $m\to\infty$ yields $N_S(t-\delta)\ge N_A(t)-k$. Finally let $\delta\downarrow0$; finite-dimensional spectral continuity gives $N_S(t-\delta)\downarrow N_S(t)$, proving the claim.

## Downstream closure

This repair restores every invocation of `lem:schur` in `prop:pivot-H` and the main proof. No other line needs a mathematical change for this issue.
