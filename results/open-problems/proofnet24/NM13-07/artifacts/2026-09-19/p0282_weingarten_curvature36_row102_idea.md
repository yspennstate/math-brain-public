# P0282 idea before validation — Jucys/Weingarten norm language, then a finite diagonal-curvature block and row 102

Date: 2026-09-19 UTC  
Track: `proofnet24/NM13-07`  
Canonical claim: `P0282` — Chen fixed-size LIS log-concavity  
Frozen metric on entry: `N_exact = 101`  
Retained complete Chen fixed-defect theorem: `j=n-k <= 66`.  
Retained growing-defect theorem: `j+1 <= n^(29/30)/8`.

All thirty numbered Section-B methods have already genuinely been used on this source. This invocation therefore labels recycled methods honestly. The planned substantive triple is **#21 ASK WHO ELSE HAS THIS SHAPE**, **#14 FIND THE GROUP ACTING**, and **#4 PROVE SOMETHING WEAKER, COMPLETELY**. This differs from the predecessor's #18/#25/#30.

## 1. #21 / #14: put the retained hook correction into the symmetric-group algebra

The retained stable hook factorization is

`F_j(n)=ell_{n,n-j}=(n)_j^2/j! * A_j(1/n)`,

with

`A_j(t)=E_{mu~Plancherel(j)} R_mu(t)^2`,

`R_mu(t)=prod_{x in contents(mu)} (1-(j+x)t)/(1-(j+x-1)t)`.

Let `J_1,...,J_j` be the Jucys-Murphy elements in `Q[S_j]`, with `J_r=sum_{a<r}(a r)`. Because a symmetric rational function of the commuting Jucys-Murphy elements is central and acts on the irreducible indexed by `mu` by evaluation on the content multiset, define

`Z_j(t)=prod_{r=1}^j (1-(j+J_r)t)/(1-(j+J_r-1)t)`.

On the `mu`-isotypic component, `Z_j(t)` has scalar eigenvalue `R_mu(t)`. The normalized regular trace is the Plancherel average, so formally near `t=0` (and as an honest rational identity wherever the denominators are invertible)

`A_j(t)=[e] Z_j(t)^2`.

Moreover `Z_j(t)` is central and self-adjoint under `sigma -> sigma^{-1}`. If

`Z_j(t)=sum_{sigma in S_j} z_sigma(t) sigma`,

then

`[e]Z_j(t)^2=sum_sigma z_sigma(t) z_{sigma^{-1}}(t)=sum_sigma z_sigma(t)^2`.

Thus the Plancherel correction is an exact **group-algebra L2 norm square**.

At `t=1/n`, writing `k=n-j`, this becomes

`Z_j(1/n)=prod_{r=1}^j (k-J_r)/(k+1-J_r)`.

This is adjacent to the unitary Weingarten calculus: the classical identity used by Novak expresses `prod_r (N+J_r)^(-1)` as the group-algebra element whose coefficients are unitary Weingarten functions, and the inverse-product expansion is governed by complete homogeneous symmetric functions in the Jucys-Murphy elements / monotone Hurwitz factorizations. I will treat that mechanism as prior art, not novelty. The new research question is whether the *adjacent quotient* above has an `S_j -> S_{j+1}` norm/conditional-expectation inequality strong enough to imply Chen, rather than merely supplying another Taylor coefficient.

A first exact consequence worth recording even if the norm comparison does not close is the L2 identity itself, because it turns the retained Plancherel expectation into a single central group-algebra norm and gives a concrete target for Cauchy-Schwarz, conditional expectation, or Weingarten/monotone-factorization methods.

## 2. #4 fallback: extend the exact diagonal-curvature block, but only as a finite theorem

The predecessor proved the finite-degree lemma `deg_j D_m <= m` for

`G_j(t)=log A_j(t)=sum_{m>=1}D_m(j)t^m`,

and exactly certified

`C_m(j):=2D_m(j)-D_m(j-1)-D_m(j+1) > 0`

for `2<=m<=28` whenever `j>=m`.

Before writing production code, I derived a faster exact route that avoids exponentiating a Taylor series separately for every partition. Use the already proved numerator polynomial

`A_j(t)=P_j(t)/Delta_j(t)^2`,

where

`P_j(t)=E_Plancherel(j) prod_{r=1}^j (1-(j+mu_r-r)t)^2`

is a degree-`2j` polynomial and `Delta_j(t)=prod_{s=1}^{j-1}(1-st)`. Compute `P_j` exactly by integer partition/hook arithmetic, obtain `log P_j` from the exact coefficient recurrence

`L_m = p_m - (1/m) sum_{r=1}^{m-1} r L_r p_{m-r}`,

and then recover

`D_m(j)=L_m + (2/m) sum_{s=1}^{j-1}s^m`.

Together with `deg D_m<=m`, values at `j=0,...,m` determine the global polynomial exactly. The production checker will test unused interpolation values as well, inspect every coefficient of `C_m(m+x)`, and either record the first failure beyond 28 or certify a larger finite block. A passing finite block is not an all-order theorem.

If the block reaches order 36, the post-order-36 tail starts at 37. The retained analytic disk would give

`|2R_j-R_{j-1}-R_{j+1}| <= 32*6^37*(j+1)^37/n^37`.

Only after exact arithmetic confirms the power-of-two envelope and coefficient positivity will any corresponding growing-defect exponent be stated.

## 3. Frozen metric route kept separate

Independently of the structural work, row `n=102` is the next frozen-metric target. The retained all-`n` theorem `j<=66` covers `k>=36`, so an exact Gessel/Toeplitz seam calculation needs only `k=2,...,35` (while reconstructing through `k=36` for the final neighbor). The row certificate will use enough independently checked CRT primes to make the reconstruction modulus exceed `2*102!`, plus the exact Catalan `u_2(102)` cross-check.

No row movement is claimed until the checker has actually run and its output is archived.
