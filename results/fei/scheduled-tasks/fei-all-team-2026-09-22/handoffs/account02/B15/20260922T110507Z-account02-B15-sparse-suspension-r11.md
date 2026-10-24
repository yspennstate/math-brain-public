# account02/B15 handoff — universal likelihood-shell compiler

**Run:** `20260922T110507Z-account02-B15-sparse-suspension-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Recipient:** `account04/B17`  
**Full FEI:** `OPEN / NOT PROVED`.

## Immutable scientific source

`yspennstate/math-open-problems@9fae0892725eaaa8c36dc5931f0aac6d29531d20`

`proofnet24/P03-fei/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-sparse-suspension-r11/REPORT.md`

Claim cards were added in commit `d5bc2dee3872ac8e6cbec3018ecbe557f9875150`; checker/output in `106b776070524b99df63b552160e2dc1e276b96b` and `da9d1d109da47971f3a5a17b1fbd84c8dc8b0d89`.

## New theorem to consume

For the exact nonempty spectral law `P=w+`, its occurrence I-projection `Q_r`, and

`mu=sum_i r_i=E_P |S|`,

retain every singleton by original coordinate identity. On every higher atom retain the actual Fourier sign and the shell

`floor(delta^{-1} log2(P(S)/Q_r(S)))`.

If `K_shell,delta` is the KL of this statistic, then

`0 <= K_occ-K_shell,delta <= delta P(|S|>=2) <= delta(mu-1)`.

At physical gate normalization this is

`v(K_occ-K_shell,delta) <= delta(sum_i It_i-v)`.

Thus the exact common remainder is

`R_Gamma = B_inf^Gamma + K_shell,delta + L_delta`,

with `0 <= L_delta <= delta(mu-1)`.

This is proved for every nonempty spectral source, not only suspensions. It preserves the actual signed source and original coordinate singleton identities.

## Exact use for your Path-C suspension transport

For the canonical suspension in your `20260922T102740Z-b17-fei-r17` report, `mu-1=J`. Therefore at unit shell width

`0 <= K_susp-K_shell <= J`.

Your exact identity

`F-rho J = B_rho(q)-K_susp`

becomes the two-sided source-exact estimate

`B_rho(q)-K_shell-J <= F-rho J <= B_rho(q)-K_shell`.

So the full suspension KL may be replaced by the one-dimensional shell KL at a cost of at most one `J`, while the constant-mode and reference-mismatch decomposition remains intact. Do not drop those credits.

## Composition/hierarchy compatibility

Using account04/B15's exact hierarchy factorization, the pointwise global score is

`ell_F = log(P0/Q_A) + sum_{i in T} log(P_i/Q_i^(zeta))`.

Quantize **after this total is formed**. Then

`K_shell,delta(F) >= K_occ(G)+sum_i alpha_i K_occ(f_i)+C_hier-delta(mu_F-1)`.

Hence `C_hier` is retained before a single global surcharge; no recursive re-spending is needed.

## Stress families

* Sparse one-point suspensions: `K_shell,1=K_occ` exactly for every `m>=2`; rare-event `m I` logarithm is preserved.
* Recursive ternary majority: since `H=4(I-1)`, unit shells satisfy `B_inf^5+K_shell,1>=0` at every depth. This passes the low-level-projection barrier analytically.
* Heterogeneous four-bit prime witness `(0,-4,-4,0,-4,0,0,-4,-12,0,0,4,0,4,4,0)`: the signed unit-shell compiler is exact numerically.

## Named partner result applied

Latest compatible completed account03/B15 source: `yspennstate/math-open-problems@2c1afb444c3a4fa2cbee12f73fd8c19c44af9e56`, `.../20260922T092409Z-complement-packet-kl-gap/REPORT.md`.

Its `c<1` theorem `K_occ>=d^2/(L^2 ln2)` combines with the shell theorem to give

`K_shell,delta >= d^2/(L^2 ln2)-delta(I-1)`.

Sparse suspensions are on the incompatible `c=1` branch, where the new likelihood shells supply the logarithm.

## Exact remaining implication

The compiler subproblem is now universal, but FEI remains open. At balanced uniform bias the next exact target is

`K_shell,1(f) >= H_max(r)-C(I(f)-1)`

for one finite universal `C`, or a genuine Boolean counterfamily to that shell payment. A proof closes FEI; conversely any FEI constant `C0` implies this shell inequality with `C0+1`.
