# P0282 idea before production validation — Gelfand–Tsetlin stay probability and a linear defect window

Date: 2026-09-19 UTC
Track: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity

This note records the mathematical route before any new production checker is written.

Retain the stable factorization for defect `j=n-k`:

`F_j(n)=ell_{n,n-j}=((n)_j^2/j!) A_j(n)`,

where under Plancherel measure on `mu |- j`,

`A_j(n)=E R_{j,n}(mu)^2`,

`R_{j,n}(mu)=prod_{x in mu} (k-c(x))/(k-c(x)+1)`, `k=n-j`.

## Route 1: say the correction in Schur/Gelfand–Tsetlin language

By the hook-content formula,

`R_{j,n}(mu)=s_{mu'}(1^k)/s_{mu'}(1^{k+1})`.

Under the multiplicity-free branching `U(k+1) -> U(k)`,

`s_lambda(1^{k+1}) = sum_{nu interlaces lambda} s_nu(1^k)`.

Hence for `lambda=mu'`, the ratio above is exactly the branching probability of the self-branch `nu=lambda` when the next row is chosen proportionally to its `U(k)` dimension. Equivalently it is the probability that the next row in a uniformly sampled Gelfand–Tsetlin pattern with top `mu'` stays unchanged.

Thus `A_j(n)` is the Plancherel average of the square of a concrete stay probability.

## Route 2: couple adjacent defects by Plancherel growth

Let `mu |- s`, let `lambda` cover `mu` by a new box of content `c0`, and keep the total permutation size `n` fixed. Put `K=n-s`. Direct cancellation gives

`R_{s+1,n}(lambda)/R_{s,n}(mu)`

`= prod_{x in mu} (1 - 1/(K-c(x))^2) * (1 - 1/(K-c0))`.

In the stable regime every factor lies in `(0,1)`. Therefore the stay probability strictly decreases along every Plancherel-growth edge as the defect grows.

The Plancherel growth transition

`p(mu->lambda)=f^lambda/((s+1) f^mu)`

has Plancherel marginals. Consequently `A_{s+1}(n)<A_s(n)` whenever both stable factorizations apply.

More importantly, for the transition `j-1 -> j`, write `d=n-2j=k-j`. Since old contents are at most `j-2` and the new-box content is at most `j-1`, every edge ratio is at least

`q_j(d)=(1-1/(d+3)^2)^(j-1) * (d+1)/(d+2)`.

Therefore

`A_j/A_{j-1} >= q_j(d)^2`,

while the next transition gives `A_{j+1}/A_j<1`. Hence

`A_j^2/(A_{j-1}A_{j+1}) > q_j(d)^2`.

The literal Chen ratio is

`Q_j(n)=((j+1)/j)*((k+1)/k)^2 * A_j^2/(A_{j-1}A_{j+1})`.

So it is enough to prove

`((j+1)/j)*((j+d+1)/(j+d))^2 * q_j(d)^2 > 1`.

## Route 3: elementary log bound in a linear region

Assume `d>=2j`, equivalently `n>=4j`. Using

`log(1+x)>=x-x^2/2` for `x>=0`,

and

`log(1-y)>=-y/(1-y)` for `0<=y<1`,

the logarithm of the displayed lower bound is at least

`1/j - 1/(2j^2)
 + 2/(j+d) - 1/(j+d)^2
 - 2/(d+1)
 - 2(j-1)/((d+2)(d+4))`.

Because `d>=2j`,

`2/(j+d)-2/(d+1) > -1/(3j)`,

`-1/(j+d)^2 >= -1/(9j^2)`,

and

`-2(j-1)/((d+2)(d+4)) > -1/(2j)`.

Thus the logarithm is strictly larger than

`1/(6j)-11/(18j^2)=(3j-11)/(18j^2)`,

which is positive for every `j>=4`.

If all details survive validation, this gives a theorem-sized linear window:

`n>=4j  ==>  F_j(n)^2>F_{j-1}(n)F_{j+1}(n)` for `j>=4`.

The already retained all-`n` fixed-defect theorem covers the small defects, so the combined source-valid region would be `j<=n/4`, a qualitative improvement over the current sublinear `33/34` window.

Before promotion: verify every cancellation and inequality exactly, refresh literature for this Schur/Gelfand–Tsetlin formulation, and separately move the frozen row metric only if an exact row-103 checker succeeds.
