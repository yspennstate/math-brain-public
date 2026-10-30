# fleet02/B11 early checkpoint — four-bank indefinite log-to-Fresnel closure

Status: `SUBSTANTIVE_CHECKPOINT / FULL_QFORM_OPEN`.

Fresh compatible inputs actually read before this checkpoint:

- newest-Claude package `e5f71d79eff325201dd0274053d20268ce65b837`, especially `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`;
- designated partner fleet03/B11 r26, commit `c5a085c3995af258cb161d94cb051d58bbd98b24`, which constructs the balanced target-valid near-rank-one family
  `A=(1-2 delta)J+delta vv^T-delta uu^T+2 delta I` and proves every fixed physical packet loses the second/third directions.

## First unpaid implication attacked

The partner leaves `QFORM-BALANCED-FOUR-BANK-AGGREGATION-v1`: aggregate the four sign banks before reciprocal-minor payment. The first calculation closes the partner's explicit obstruction family outright by a product-preserving Fresnel/Brascamp--Lieb estimate.

Let

`r0=1/sqrt(n) * 1`, `rv=v/sqrt(n)`, `ru=u/sqrt(n)`.

They are orthonormal and every physical row of the `n x 3` frame `R=[r0 rv ru]` has leverage exactly

`|R_i|^2=3/n`.

Rewrite the partner matrix as

`A=2 delta I + ((1-2 delta)n) r0 r0^T + (delta n) rv rv^T - (delta n) ru ru^T`.

For `n>=8`, `3/n<=1/2`. Theorem F of the pinned Claude package applies with `I` equal to all original coordinates, diagonal twist `2 delta I`, and `G_I=I_3`. Hence, for arbitrary independent cap-one input laws,

`||p_{X^T A X}||_infinity
 <= 12 [ (1-2 delta) delta^2 n^3 ]^(-1/3)
 = 12 / [ n delta^(2/3) (1-2 delta)^(1/3) ].`              (C1)

This is a real use of the pinned source theorem: it pays the many-coordinate obstruction without selecting a physical minor and without declaring the three spectral projections independent.

If the partner family is in the target class, its negative eigenvalue has magnitude `delta(n-2)>=1`. Since `delta<1/4`, `delta^2(1-2delta)` is increasing on this interval up to `1/4`, so (C1) is worst at `delta=1/(n-2)`:

`||p||_infinity <= 12(n-2)/[n(n-4)^(1/3)].`

For multiples of four `n>=8`, this decreases in `n`, because

`d/dn log[(n-2)/(n(n-4)^(1/3))]
 =2/[n(n-2)]-1/[3(n-4)] <0`,

with the last inequality equivalent to `n(n-2)>6(n-4)`. Therefore

`boxed: ||p||_infinity <= 9 / 4^(1/3) = 5.6696...`                 (C2)

throughout the target-valid partner family.

## Rank-two logarithmic control in the same four-bank geometry

Partition the coordinates by the four sign pairs of `(u_i,v_i)` and write the corresponding coordinate sums as `S_{++},S_{+-},S_{-+},S_{--}`. For the normalized projections `U=<ru,X>`, `V=<rv,X>`,

`V+U=(2/sqrt(n))(S_{++}-S_{--})`,
`V-U=(2/sqrt(n))(S_{-+}-S_{+-})`.

Thus

`V^2-U^2=(4/n)(S_{++}-S_{--})(S_{-+}-S_{+-}).`                     (C3)

The two factors use disjoint original-coordinate banks and are genuinely independent. For centered unit-uniform inputs each factor has a continuous density positive at zero, so their product has a logarithmically divergent density at zero. Indeed if both factor densities are at least `c>0` on `[-eps,eps]`, then for `0<|t|<eps^2`

`p_{YZ}(t) >= 2 c^2 log(eps^2/|t|).`                                (C4)

Hence the rank-two opposite-sign singularity is present inside exactly the same balanced four-bank construction.

The third common mode `r0` removes it in the full three-mode form not by independence or convolution: algebraically the Schur complement after the `r0` mode is precisely the opposite-sign rank-two saddle, while analytically Theorem F contributes three joint Fresnel half-powers, `|t|^{-3/2}`, in the ORIGINAL-coordinate product integral. Two modes give only the nonintegrable endpoint `|t|^{-1}`, matching (C4).

The full report will record the sign-specific ruled comparison and the arbitrary-diagonal-twist generalization. Full QFORM remains open.
