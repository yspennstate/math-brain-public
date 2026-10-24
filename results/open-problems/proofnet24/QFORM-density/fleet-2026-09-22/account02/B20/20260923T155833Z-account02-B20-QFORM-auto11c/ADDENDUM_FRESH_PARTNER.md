# Fresh-partner addendum — account03/B20 20260923T154628Z consumed

A prepublication refresh found a newer completed designated-partner result than r33:

`yspennstate/math-open-problems@5d0600968569ced59d5a9efe08311ae656debed6`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T154628Z-account03-B20-QFORM-auto11/REPORT.md`.

Its theorem `QFORM-ALIGNED-TRANSVERSE-OR-INPLANE-R5-v1` reduces the aligned strict-N3 survivor to either:

- an in-plane skeleton `S0` with `rank(S0)<=5`, `s3(S0)>0.7985866375852596`, and actual non-diagonal residual of operator norm `<0.201414`; or
- a literal original-coordinate self-bank cross block `M` with

  `E_M:=||M||F^2 > E_perp`,
  `E_perp=(1/16-2^-20)^2/4=4294836225/4398046511104`,

  top-four energy `> (63/64)E_M`, and, after its grouped-rank-three exit,

  `s3(M)<1/256`.

The partner already pays the fifth-volume-diffuse subbranch by `<3178.184`, the `s3(M)>=1/256` grouped-rank-three subbranch by `<1318.595`, and the exact rank-three-plus-diagonal diffuse in-plane endpoint by `<15.027`.

## New theorem — `QFORM-ALIGNED-TRANSVERSE-R2-FROBENIUS-COLLAR-v1`

In every still-unpaid transverse self-bank state above, write the squared singular values of `M` as

`x1>=x2>=x3>=...`,

and put

`U=sum_(r>=3) x_r = ||M-M_2||F^2`,

where `M_2` is the best rank-two truncation. Because `s3(M)<1/256`, every `x_r` for `r>=3` satisfies

`0<=x_r<c:=1/65536`.

The partner's strong-top-four inequality gives

`4x1 >= x1+x2+x3+x4 > (63/64)E_M`,

hence

`x1 > (63/256)E_perp`.

Assume

`U>=1/16384=4c`.

For the tail sequence `(x3,x4,...)`, the same ordered-tuples argument used in the main report gives

`e4(x3,x4,...) >= U(U-c)(U-2c)(U-3c)/24 >= c^4`.

Therefore the physical fifth volume obeys

`Z5=e5(M^T M)
 >= x1 e4(x3,x4,...)
 > [(63/256)E_perp] c^4
 =270574682175/20769187434139310514121985316880384
 =1.3027697064847294e-23.`

Apply the required pinned unrestricted D5 theorem from
`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`:

`||p_Q||inf
 <5 sqrt(2e) Z5^(-1/10)
 =2265.4030349... <2265.404.`

Thus every still-unpaid newest-partner transverse state satisfies the stronger Frobenius rank-two collar

`boxed: sum_(r>=3)s_r(M)^2 <1/16384,`

or equivalently

`boxed: ||M-M_2||F <1/128.`

In particular its top-two singular directions retain the fixed physical energy

`boxed: s1(M)^2+s2(M)^2 > E_perp-1/16384
 =4026400769/4398046511104
 =0.000915497541654986... .}`

No small random tail is deleted: D5 pays exactly the branch where the aggregate tail is larger, and the nonzero tail is retained in the unpaid branch.

## Updated first unpaid implication

After consuming the newest designated partner, the freshest closure edge is

`QFORM-ALIGNED-INPLANE-R5-OR-TRANSVERSE-R2-FROBENIUS-PAYMENT-v1`:

1. pay the in-plane carrier `rank(S0)<=5`, `s3(S0)>0.7985866375852596` while retaining its actual non-diagonal residual `||A-S0||op<0.201414`; or
2. pay the literal physical self-bank cross block with
   `||M||F^2>E_perp`, strong-top-four energy, `s3(M)<1/256`, and the new aggregate tail bound `||M-M2||F<1/128`.

The route counterexample in the main report remains relevant as a correction to a tempting mechanism: a finite E2 half-Riesz bound cannot by itself imply L-infinity without spending a third spectral resource. It is not a QFORM counterexample because that construction has only two large eigenvalues.

Full QFORM and unrestricted continuity remain open.
