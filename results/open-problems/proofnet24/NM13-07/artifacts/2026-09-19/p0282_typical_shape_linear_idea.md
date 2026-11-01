# P0282 idea before validation — typical-shape Kerov splitting beyond the one-third barrier

Date: 2026-09-19 UTC
Worker: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity
Status at write: IDEA BEFORE CHECKER; no theorem claim yet.

The preceding run proves Chen for defects `j=n-k <= n/3` by taking a shape-independent worst-case upper bound on the Kerov transition Cauchy transform. The one-row Young diagram is the obstruction to improving that bound pointwise. It is also violently atypical under Plancherel measure. The new route is therefore to reverse the order of `for all shapes` and averaging: prove a much sharper conditional edge bound on a high-probability set of parent diagrams and pay explicitly for the rare tail under the `R^2`-tilted Plancherel law.

Retain, for a parent `mu |- s`, `K=n-s`,

`R(mu)=prod_{x in mu} (K-c(x))/(K+1-c(x))`,

and for a Plancherel-growth child obtained by adding content `C`,

`h = R(child)/R(parent) = B_mu(K) * (1 - 1/(K-C))`,

with the exact Kerov identity

`B_mu(K) * K * G_mu(K)=1`, `G_mu(K)=E[1/(K-C)]`,

and exact transition moments `E C=0`, `E C^2=s`.

## 1. Uniform lower bound needed only to control the tilt

Order the `s` boxes of `mu` row by row. The content of the r-th box is at most `r-1`, and `c -> (K-c)/(K+1-c)` is decreasing. Hence

`R(mu) >= prod_{r=1}^s (K-r+1)/(K-r+2) = (K-s+1)/(K+1)`.

Equality is the one-row diagram. Therefore

`A_s = E_Pl R(mu)^2 >= rho0^2`, `rho0=(K-s+1)/(K+1)`.

If `nu(mu)=Pl_s(mu)R(mu)^2/A_s` is the tilted parent law, then for any event E,

`nu(E) <= Pl_s(E)/rho0^2`,

because `R(mu)^2<=1`.

## 2. Typical first-row split

Take

`r_s = ceil(9s/25)`

and call a parent good if `mu_1 < r_s`. On a good parent every addable content satisfies

`C <= mu_1 < 9s/25`.

Using

`1/(K-C)=1/K + C/K^2 + C^2/[K^2(K-C)]`

and the exact transition moments gives

`m:=G_mu(K) <= U := 1/K + s/[K^2(K-9s/25)]`.

Since `B_mu(K)=1/(K m)`, conditional Jensen gives

`E[h^2 | mu] >= ((1-m)/(K m))^2 >= ((1-U)/(K U))^2 =: J`.

Thus only the tilted probability of bad parents has to be paid.

## 3. RSK gives an explicit rare-tail certificate

Under Plancherel measure on partitions of `s`, `mu_1` has the law of the LIS length of a uniform permutation of `s`. Therefore a union bound over subsets of `r_s` positions gives

`Pl_s(mu_1 >= r_s) <= binom(s,r_s)/r_s! =: p_s`.

The proposed finite certificate is

`p_s <= 1/[14000(s+1)]` for every `s>=66`.

This can be proved with only 25 exact base cases, `s=66,...,90`, and a residue-class induction. Since `r_{s+25}=r_s+9`,

`p_{s+25}/p_s`

is an exact factorial ratio. Bounding `r_s>=9s/25` and `s-r_s+1>=16s/25` gives

`p_{s+25}/p_s <= 25^34 (s+25)^25 / (9^18 16^16 s^34)`.

The right side decreases for `s>=66`, and its value at 66 is <1/25, which is far stronger than needed to propagate the base inequality.

## 4. Candidate linear theorem

Now take the Chen transition `s=j-1`. Impose

`221 n >= 576 j`.

Then

`K=n-j+1 >= (355/221)j + 1`.

At the threshold, the uniform tilt lower bound satisfies

`rho0 > 134/355`,

so `rho0^{-2}<8`. Hence for `j>=67`,

`nu(bad) < 8 p_{j-1} <= 1/(1750 j)`.

On good shapes, put

`y=K U = 1 + s/[K(K-9s/25)]`.

After including the exact factorial part of the Chen ratio, the deterministic good-shape factor is

`B(j,K)=(j+1)/j * ((K-y)/((K-1)y))^2`.

It increases with K. At the threshold `K=(355/221)j+1`, exact algebra suggests

`B(j,K) > 1 + 1/(1000j)`

for every positive integer j; after clearing denominators the numerator is a degree-six polynomial with all positive coefficients.

Therefore the candidate conclusion is

`Q_j(n) > (1+1/(1000j))(1-1/(1750j)) > 1`,

hence

`221 n >= 576 j  ==>  ell_{n,n-j}^2 > ell_{n,n-j-1} ell_{n,n-j+1}`

for `j>=67`, while the retained all-n fixed-defect theorem handles `j<=66`.

Equivalently the proposed new global sufficient linear region is

`j/n <= 221/576`, i.e. `k/n >= 355/576 = 0.616319444...`.

This would improve the preceding `k/n >= 2/3` theorem. It is still only PARTIAL relative to Chen's all-k conjecture.

## 5. Route that failed before this split

A seemingly natural refinement keeps all shapes but retains the variance discarded by Jensen. Writing `X=1/(K-C)`, Cauchy--Schwarz gives

`Var(X) >= Cov(C,X)^2/Var(C) = (K G_mu(K)-1)^2/s`.

This yields an exact extra nonnegative term in `E[h^2|mu]`. However, combined with the preceding run's worst-shape upper bound on `G_mu(K)`, that correction is only of order `j^{-3}` at a linear boundary, whereas the obstruction to crossing `n=3j` is order `j^{-1}`. So variance alone cannot move the asymptotic one-third defect fraction while the one-row worst-shape bound is retained. The typical-shape split is meant to remove that obstruction rather than polish it.
