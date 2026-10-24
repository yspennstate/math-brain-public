# Strengthening: push the diffuse-range payment up to leverage 1/44

This file strengthens, without contradicting, the `1/672` half-cut subcase in `REPORT.md`.

Keep the exact account02/B20 packet and the target-scale restoration

`A=D+R+E`, `rank(R)=r<=42`,
`R=VKV^T`, `V^TV=I`,
`||D||op<d0=0.007619480067767874...`,
`||E||F<eta0=0.008411726321812482`,
`s3(R)>gamma0=0.9839687936104196...`.

Let `q=max_i (VV^T)_ii`.

## General physical half-cut estimate

For a Bernoulli physical half-cut `I`,

`E ||V_I^T V_I-(1/2)I_r||F^2 <= q r/4`.

Therefore some literal original-coordinate partition `I sqcup J=[n]` satisfies

`||V_I^TV_I-(1/2)I_r||op <= (1/2)sqrt(qr)`.

If `qr<1`, both physical Gram matrices are bounded below by

`g(q,r) I_r`,
`g(q,r):=(1-sqrt(qr))/2`.

Exactly as in `REPORT.md`, polar factorization gives

`s3(R[I,J]) >= g(q,r) s3(R)`,

and because the diagonal term has no cross block while the nonzero tail is retained,

`s3(A[I,J]) > g(q,r) gamma0-eta0`.                               (S.1)

## Universal 1/44 threshold

If

`q<=1/44`,

then `r<=42` implies

`g(q,r) >= g44 := (1-sqrt(21/22))/2
                 =0.01149578954080277...`.

Hence the actual physical cross block satisfies

`s3(A[I,J]) > c44 := g44 gamma0-eta0
                    =0.0028997718442504983... >0`.               (S.2)

Thus

`e3(A[I,J]A[I,J]^T)>c44^6
 =5.945425920261305e-16`,

and the source-pinned marginal-free physical-E3 theorem yields

`boxed: ||p_Q||infinity < C3/c44
                       < 3567.551`,

with a continuous `C0` density on this paid branch.

Therefore every **unpaid** active-localized carrier must satisfy

`boxed: max_i (VV^T)_ii > 1/44.`                                 (S.3)

Define the heavy range set

`L44={i:(VV^T)_ii>1/44}`.

Since `sum_i(VV^T)_ii=r<=42`,

`boxed: |L44|<=1848.`                                            (S.4)

Combining it with account02/B20's active localization set `H`, `|H|<=28224`, gives

`F44=H union L44`,
`boxed: |F44|<=30072`,                                           (S.5)

while retaining

`||(Vu)_F44||^2>1/2`,
`||Ku||>=0.0009524350084709843...`,
`(VV^T)_ii<=1/44 for every i outside F44`,
`s3(R)>0.9839687936104196...`,
`||D||op<0.007619480067767874...`,
`||E||F<0.008411726321812482`.

So the strongest compiler from this run is

`QFORM-R44-ACTIVELOCALIZED-LEVERAGE1OVER44-PAID-OR-30072CORE-v1`:

> the account02/B20 active-localized branch is either paid continuously by a literal physical `E3` block, or all carrier rows with leverage above `1/44` and more than half of the supplied active direction can be placed in one set of at most `30072` original coordinates, with every complement row leverage at most `1/44`.

The earlier `1/672` statement remains useful as a stronger-density subcase (`||p_Q||infinity<28.691`), but (S.3)-(S.5) are the sharper structural endpoint.

Full QFORM and full-target continuity remain OPEN.
