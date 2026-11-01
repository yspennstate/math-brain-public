# R17 PROB10-02 — idea before code: second-class defect geometry + environment-weighted Collatz dual

Target remains the true iid-uniform binary Chvatal--Sankoff constant.  This note keeps the exact correlated strip recursion: the same fresh source bit `v` is compared against the whole raw `x` window.  No independent Bernoulli matching array is substituted.

The previous R17 run built the exact single-defect substochastic chain `Q_m` and used only the scalar block survival coefficient `alpha_m(T)=||Q_m^T 1||_infty`.  Three different attacks are fixed here before any new checker is written.

## Attack A — second-class-particle / carrier geometry

For an ordered edge pair whose lower and upper fronts differ only at coordinate `j`, derive the exact coordinate update from the carrier recursion.  The intended statement is that, while the defect survives, its space-time coordinate `Z_t=t+j_t` never decreases.  More precisely, for fresh `v`, let `A_v=d_{j-1} OR [x_j=v]` in the lower copy.  If `A_v=0`, the defect moves one site left (or dies at the left edge).  If `A_v=1`, it jumps right to immediately before the first later carrier-stopping site `k` with `g_k=1` or `x_k=v`; if no such site exists, it reaches the right boundary and survives there iff `u=v`.  This should be proved directly from the two carrier streams, not inferred from numerics.

This recasts a surviving discrepancy as a second-class particle in a finite carrier system and may expose an exact queue/workload variable for later width-uniform analysis.

## Attack B — environment-weighted one-step upper dual

The scalar block contraction from the previous run throws away the environment after every `T` steps.  Retain it through the exact positive vector

`h_T := Q_m^T 1`.

Define

`lambda_T := max_{e:h_T(e)>0} (Q_m h_T)(e)/h_T(e)`.

Then the componentwise Collatz inequality `Q_m h_T <= lambda_T h_T` should imply

`Q_m^(T+k) 1 <= lambda_T^k h_T`,

so after the `m`-edge Hamming path union bound the post-alignment coupling tail is bounded by

`m alpha_T lambda_T^k`,  `alpha_T=||h_T||_infty`.

When `m alpha_T<1`, this yields the exact finite-horizon/stationary reward error

`C_m(T) <= m + T + m alpha_T/(1-lambda_T)`.

This is a genuinely different dual from the old block-only bound: it is a one-step environment-weighted Bellman/Collatz certificate after a finite burn-in.  Compute it exactly at the existing `T=4m` through `m=8`; a strict decrease of the previous `C_8<50` certificate is useful mechanism progress even if it does not move the source interval.

## Attack C — try to turn the monovariant into deterministic regeneration, and falsify it if false

A tempting consequence of nondecreasing `Z_t` is that every surviving defect must hit a killing boundary within `O(m)` steps.  Test that statement before using it.  In particular inspect the monochromatic state `x=0^m`, lower `g=0^m`, defect at an interior coordinate, under the repeated true-source letter `(u,v)=(0,0)`.  If this is a nonabsorbing self-loop, it exactly rules out deterministic bounded-time boundary regeneration and any rank that strictly decreases on every nonabsorbing transition.  The stochastic weighted dual in Attack B would then be the correct replacement.

## Source-level criterion

The source metric is the certified interval width `U-L`.  A smaller strip mixing/error constant is auxiliary only.  It changes the source metric only if coupled to an exact finite computation that raises `L`, or to a separate valid width-to-full upper transfer that lowers `U`.  No such promotion will be made without that transfer.
