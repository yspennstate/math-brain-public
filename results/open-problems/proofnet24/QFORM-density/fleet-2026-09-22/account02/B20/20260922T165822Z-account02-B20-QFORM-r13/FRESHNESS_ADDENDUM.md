# Freshness addendum — newest designated partner account03/B20 r13

This addendum is part of run `20260922T165822Z-account02-B20-QFORM-r13` and **supersedes only the partner-freshness statements** in the earlier `REPORT.md`. The mathematical Theorems A–C there remain unchanged.

A final source refresh found a newer completed designated-partner result than the r12 snapshot initially available to this run: account03/B20 `20260922T165009Z-account03-B20-QFORM-r13`, canonical proof `yspennstate/math-open-problems@06ef7346c08f41c3fac240e1acdeb1b42dc2995d`, theorem `QFORM-NESTED-CUT-THREE-RESOURCE-v1`. The proof was read at that exact commit before publication. Live owner control remained revision `2026-09-22.8`.

## Exact partner theorem consumed

In the already-paid account03/B19 complement, every unresolved target matrix has `H=A-diag(A)` with

` s_2(H)>3/20. `

The partner proves that some **original-coordinate** cut `L disjoint_union R`, `C=A[L,R]`, satisfies one of:

1. `s_2(C)>=3/160`;
2. `s_1(C)>9/160` and some physical pivot on one side has `|A_ii|>=157/320`;
3. `s_1(C)>9/160` and one side has a nested original-coordinate cut `S=S_1 disjoint_union S_2` with `s_1(A[S_1,S_2])>157/640`.

It also applies the prior high-window conditioning theorem to these physical banks: with `P=1_{|A|>=1/64}=UU^T`, every unresolved outer cut must satisfy

`||U_L^TU_L||op>1/2 OR max_{i in R}P_ii>1/64`,

and the swapped condition with `L,R`; the same test is available on a nested bank.

## New exact application: `QFORM-NESTED-RESOURCE-PACKETS-v1`

Under the partner hypotheses above, one of the following source-realizable aggregate packets exists.

### A. Two-direction four-bank determinant packet

If `s_2(C)>=3/160`, then by Cauchy-Binet

`e_2(CC^T)=sum_{|I|=|J|=2} det C[I,J]^2`
`          =sum_{r<s} s_r(C)^2 s_s(C)^2`
`          >=s_1(C)^2s_2(C)^2`
`          >=(3/160)^4`
`          =81/655360000.`

Independently 2-color `L` and `R`. Every squared `2x2` minor survives with its two rows separated and two columns separated with probability `1/4`. Hence there are physical partitions

`L=L_1 disjoint_union L_2`, `R=R_1 disjoint_union R_2`

with

`sum_{i in L_1,j in L_2,a in R_1,b in R_2}`
`det C[{i,j},{a,b}]^2 >= 81/2621440000.`

Thus the two-direction singular-value certificate becomes a four-bank original-coordinate determinant-mass certificate without selecting a single minor.

### B. Physical pivot plus outer cross-energy packet

If the partner is in alternative 2, then

`|A_ii|>=157/320`

for an original coordinate `i`, while

`||C||_F^2>=s_1(C)^2>(9/160)^2=81/25600.`

So the unresolved branch contains simultaneously a macroscopic physical square and a macroscopic product-preserving outer cross bank. No Schur-complement independence is asserted.

### C. Nested two-cross energy packet

If the partner is in alternative 3, then

`||C||_F^2>81/25600`

and, on a disjoint nested physical partition,

`||A[S_1,S_2]||_F^2 > (157/640)^2 = 24649/409600.`

These are two distinct source-realizable cross resources on a nested original-coordinate geometry.

This is an exact application of the newest designated partner result, not merely a citation. It converts its singular-value alternatives into physical aggregate currencies compatible with the correction ledger.

## Updated synthesis after the final freshness read

The strongest current conditional route is now:

- already-paid branches close first;
- every remaining matrix satisfies the partner r13 nested three-resource theorem and its high-window localization alternatives;
- independently, account03/B07 supplies O0/O1/O2/O3 third-compound structure;
- O0 diffuse ridge is already paid;
- O0 ridge-heavy is converted by this run's Theorems A–B into a six-block `3x3` determinant packet of mass `>1/110592`;
- the partner r13 alternatives are converted above into a four-bank `2x2` determinant packet, a pivot-plus-cross packet, or a nested two-cross packet.

Hence every fully unresolved candidate carries **both** a third-compound alternative and one of the explicit newest-partner resource packets. In the O0 ridge-heavy subbranch it carries the six-block `3x3` packet as well.

### Updated first unpaid universal implication

`QFORM-AGGREGATE-RESOURCE-SPLICE-v1`: under the exact target hypotheses and the partner-forced localization alternatives, combine one of the three source-realizable packets above with the simultaneous third-compound alternative to obtain a universal density payment, or transfer a fixed fraction into an already-paid ridge/grouped-square/rank-two branch. In the O0 ridge-heavy case the available third-compound information is the explicit six-block mass `>1/110592` proved in `REPORT.md`.

The analytic obstruction remains same-bank contamination: the variables producing the cross/pivot currencies also occur in arbitrary self blocks. No convolution independence, spectral-coordinate conditioning cap, single-minor extraction, or pointwise oscillatory decay is assumed.

Full QFORM remains **OPEN**. The classification remains `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_REDUCTION_PROVED / FULL_TARGET_OPEN`. Continuity is claimed only on previously paid branches whose cited proofs establish it.
