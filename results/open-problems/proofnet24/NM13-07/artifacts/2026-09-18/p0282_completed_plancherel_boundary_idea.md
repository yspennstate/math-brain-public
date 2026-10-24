# P0282 route note — completed residual-Plancherel boundary transfer

Date: 2026-09-18 UTC
Worker: NM13-07
Source: P0282 / Chen fixed-size LIS log-concavity

This note fixes the mathematical route before the archived checker for this invocation. It does not claim the source conjecture is solved.

## Fresh Section-B routes

- **#18 SAY IT IN ANOTHER LANGUAGE.** Replace the source count at fixed defect by the completed residual-partition polynomial count supplied by the Kauers–Wang fixed-defect polynomial. The completed object is a positive sum over all residual partitions and therefore naturally majorizes the source count when the first-row compatibility constraint cuts out residual shapes.
- **#20 FIND WHY THE ALGORITHM FAILS.** Push that completion transfer one boundary step below the stable range and determine exactly where equality with the source count stops. The intended falsification test is the shifted forced-factor quotient at `n=2j-2`, not another generic finite census.
- **#24 FIND THE EXTREMAL OBJECT.** Identify the first omitted residual partition that causes the completion error. At `n=2j-1` the only invalid residual shape is `(j)` and its residual hook factor vanishes, so completion is still exact. At `n=2j-2`, `(j)` acquires nonzero weight and is the natural candidate obstruction.

## Completed residual count

Retain the already proved polynomial identity from the preceding report. For `mu |- j`, padded by zero parts,

`R_mu(n-j) = prod_{i=1}^j (n-j+i-mu_i)`,

and

`P_j(n) = (1/j!) sum_{mu|-j} (f^mu)^2 R_mu(n-j)^2`.

Define the completed count

`Etilde_j(n) := P_j(n)/j!`

so that

`Etilde_j(n) = (1/(j!)^2) sum_{mu|-j} (f^mu)^2 R_mu(n-j)^2`.

For the source count `E_j(n)=ell_{n,n-j}`, writing the first row as `N=n-j`, the valid residual diagrams are exactly those with `mu_1 <= N`. The source summand is the same squared residual factor. Therefore

`Etilde_j(n) >= E_j(n)`

whenever the source count is defined, because completion merely adds nonnegative squared terms.

If `n>=2j`, every residual partition is valid, so equality is the standard stable identity. The new boundary observation is that equality persists at `n=2j-1`: now `N=j-1`; the only invalid residual partition is `mu=(j)`, but its first residual factor is

`N+1-mu_1 = (j-1)+1-j = 0`,

so its completed contribution vanishes. Hence

`Etilde_j(n)=E_j(n)` for every `n>=2j-1`.

At a fixed source pair `(n,j)` with `n>=2j-1`, this gives

`Etilde_{j-1}(n)=E_{j-1}(n)`,
`Etilde_j(n)=E_j(n)`,
`Etilde_{j+1}(n)>=E_{j+1}(n)`.

Thus strict completed Turan positivity

`Etilde_j(n)^2 > Etilde_{j-1}(n) Etilde_{j+1}(n)`

is sufficient for the strict source inequality at that boundary. In polynomial normalization this is exactly `D_j(n)>0` up to the positive scalar `(j+1)(j!)^2`.

## Exact obstruction predicted one step lower

At `n=2j-2`, `N=j-2`. For the middle defect `j`, the invalid residual `(j)` now contributes

`c_j = [ (2j-2)! / ((j-1)! j!) ]^2 > 0`

to `Etilde_j(n)`. The other newly invalid shape `(j-1,1)` has zero first residual factor at this boundary. Thus `(j)` is the first nonzero completion error in the middle count.

The checker should therefore do two logically separate things:

1. test coefficient positivity of the already forced-factor quotient
   `H_j(n)=D_j(n)/(n)_floor((j+1)/2)`
   after the sharper shift `n=m+2j-1` for the current finite defect range;
2. deliberately test the lower shift `n=m+2j-2` and record the first failure rather than hiding it.

A successful boundary certificate at `2j-1` would improve the existing stable-sector theorem by two rows for the certified defect range. A failure at `2j-2` would be useful: it would show the completion language has located its exact obstruction and that the next route must correct excluded residual shapes rather than simply extend the same positive-coefficient argument.

Independently of this restricted theorem, the frozen metric remains `N_exact`; a new full-row certificate is only counted if the checker exactly verifies the entire next row and the Plancherel mass identity.