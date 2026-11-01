# P0282 route pivot before production validation — lower the asymptotic cutoff slope and isolate the finite bottleneck

Date: 2026-09-19 UTC

The first affine-cutoff idea used `r_s=ceil(3s/10+2)` and already suggested that a finite additive buffer can decouple the low-rank Plancherel tail from the asymptotic cutoff slope. Before production validation, push that observation further rather than merely checking the first constant.

New good-parent cutoff:

`r_s := ceil(s/5 + 8)`; good means `mu_1 < r_s`.

Then every addable content satisfies `C < s/5+8`, so the retained Kerov moment identity gives

`G_mu(K) <= 1/K + s/[K^2 (K-s/5-8)]`.

The low-rank obstruction is now isolated: the cutoff at `s=66` is still `r=22`, so its true Plancherel tail can be checked exactly by Gessel/Toeplitz rather than paid by the very loose union bound. For larger `s`, the elementary RSK union bound should become sufficient again.

Candidate rational boundary for exact validation:

`K >= (15661/10000) j + 1`, equivalently

`10000 n >= 25661 j`,

hence

`k/n >= 15661/25661 ~= 0.6103035735`.

Planned closing inequalities for this route:

1. exact Gessel/Toeplitz Plancherel tails for the finite bottleneck `66 <= s <= 112` and the exact `R^2` normalization factor imply tilted bad mass `<1/(700j)`;
2. for `s>=113`, prove `p_s=binom(s,r_s)/r_s! <1/[5600(s+1)]` from five exact residue-class bases plus a five-step contraction, hence again tilted bad mass `<1/(700j)`;
3. prove by exact rational algebra that the deterministic good-parent factor at the candidate boundary is `>1+1/(695j)` for all `j>=67`, preferably by shifting the cleared numerator to `j=67+x` and obtaining positive coefficients;
4. combine `(1+1/(695j))(1-1/(700j))>1`;
5. independently advance the frozen metric from row 106 to row 107 with an exact Gessel/CRT seam certificate.

If any item fails, record the obstruction and do not claim the candidate boundary.