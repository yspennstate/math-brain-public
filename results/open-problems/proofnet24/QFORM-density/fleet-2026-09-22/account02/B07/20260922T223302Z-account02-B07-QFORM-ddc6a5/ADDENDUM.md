# Late-source audit and sharpening

A correction/source sweep after `REPORT.md` found the completed account03/B01 r18 theorem

`yspennstate/math-open-problems@7acff3e983f6e6a3ede04ecbaf8405a3ce4ee8e2`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260922T202731Z-r18/REPORT.md`.

It already proves, for `T=2XU+R` with `X` independent of `(U,R)`, cap-one `X`, and `||p_U||_infinity<=M`, the nonsharp all-real-`p` estimate

`||p_T||_p <= p M^(1-1/p)`, `1<p<infinity`.

Thus the B07 `p=3` random-shift mechanism in the main report is not a new qualitative existence theorem. Its contribution is a sharper three-copy constant and, more importantly for this assignment, the explicit application to the determinant-weighted O0 two-star/near-leaf branch. The same order-statistic proof in fact gives the following strict strengthening at every integer exponent.

## `QFORM-RANDOMSHIFT-SHARP-INTEGER-LP-v1`

Let `X` be independent of `(U,H)`, with `X` having probability density bounded by `N`, `U` having probability density bounded by `M`, and `H` arbitrary and possibly dependent on `U`. For `kappa!=0`, put

`Z=kappa XU+H`.

Then for every integer `m>=2`,

`boxed:
||p_Z||_m^m <= m! (2NM/|kappa|)^(m-1).
`                                                               (A.1)

For `kappa=2`, `N=1`, this is

`||p_Z||_m <= (m!)^(1/m) M^(1-1/m)`,                            (A.2)

which improves the account03/B01 constant `m` to `(m!)^(1/m)`. The constant in (A.2) is sharp already for `X,U` iid `Uniform[-1/2,1/2]`, `H=0`, because `2XU` has density

`log(1/(2|t|)) 1_(0<|t|<1/2)`

and therefore

`||p_(2XU)||_m^m=int_0^1 (-log s)^m ds=m!`.                    (A.3)

### Proof of (A.1)

Expand the `m`th power using `m` iid copies `(U_a,H_a)`. Order `T_a=|U_a|` as

`T_(1)<=...<=T_(m)`.

In the common `z` integral, integrate the density factor corresponding to `T_(1)` and bound the remaining `m-1` copies of the density of `X` by `N`. Exactly as in the three-copy proof,

`||p_Z||_m^m
 <= N^(m-1)|kappa|^(1-m) R_m`,                             (A.4)

where

`R_m=E[1/(T_(2)...T_(m))]`, `R_1=1`.                           (A.5)

Let `F(t)=P(|U|<=t)<=2Mt`. By symmetry, after declaring copy 1 to be the minimum and conditioning on the other `m-1` copies,

`R_m
 =m E[ F(min(T_2,...,T_m))/(T_2...T_m)]`
` <=2Mm E[ min(T_2,...,T_m)/(T_2...T_m)]`
` =2Mm R_(m-1).`                                                (A.6)

Iteration yields

`R_m <= m!(2M)^(m-1)`.                                         (A.7)

Substitution in (A.4) proves (A.1). No property of the shifts `H_a` is used.

For `m=3`, (A.1) gives exactly the main report's `24N^2M^2/|kappa|^2` bound. Thus Corollary 5.1 and the O0 strong-star constant `17.913815821223174...` remain valid unchanged.

## New live correction consumed

The same late sweep found account02/B01 r29, event `QFORM-NONZERO-MUTUAL-EDGE-TWO-SLOPE-INSUFFICIENT-v1`, canonical report

`yspennstate/math-open-problems@c396b6e553f98ca1cd735ae10eb0e6ec24a96cc4`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260922T223353Z-account02-B01-qform-r29/REPORT.md`.

Its rank-two factorized family has zero physical diagonals but an arbitrarily small nonzero mutual edge and a logarithmically unbounded **density**. This does not conflict with the present theorem: (A.1) gives finite `L^m` norms for every finite integer `m`, and the B07 application claims only an `H_(1/2)` bound before the outer-square transducer, not an `L^infinity` bound for the zero-self residual itself. The B01 correction therefore confirms the endpoint distinction rather than invalidating it.

The status after this audit is still `ESSENTIAL_STEP_APPLIED`: the new branch closure is the B07 use of the sharp random-shift finite-`L^p` endpoint to absorb arbitrary complementary curvature at a strong zero-self star. Full QFORM remains open.
