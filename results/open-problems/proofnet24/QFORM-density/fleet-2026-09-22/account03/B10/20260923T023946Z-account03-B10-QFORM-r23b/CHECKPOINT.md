# account03/B10 r23b — early mathematical checkpoint

Programme: QFORM-DENSITY-3EIG-20260922  
Assignment: rank-three coupled case  
Status: substantive checkpoint; full target open.

## Source-matching theorem ends the old near-null exact-coloop gap

A fresh current-source read found a theorem that exactly matches the active B10 subproblem `near-null nonzero coloop interpolation`:

- `QFORM-CROSS-TRANSVERSE-PROJECTION-PRODUCT-v1` and its exact-coloop corollary,
- `yspennstate/math-open-problems@3ba3125a5d8dd06d778b7c79849c4c3106da9855`,
- `proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260923T003846Z/REPORT.md`.

Write an exact-rank-three coloop core in an orthonormal spectral basis as

`B=[[a,b^T],[b,C]]`, `D=|det B|=|det Lambda|>=1`.

The original coloop scalar is genuinely independent of the remaining two-dimensional product projection, whose joint density is at most 2. For `|a|<=1/2`, rotate only inside the receiver plane so `b=(beta,0)` and `C=[[c,d],[d,e]]`. The source theorem uses the cross-transverse resource `P=beta^2|e|`. The inverse-cofactor identity gives

`|det C|/D=|(B^{-1})_00|<=1`,

hence

`P=|a det C-det B| >= D-|a||det C| >= D/2`.

Applying the completed cross-transverse theorem with receiver cap `M<=2` gives

`||p_Q||_inf <= 103680^(1/3) 2^(2/3) (D P)^(-1/6)`

`<=103680^(1/3) 2^(5/6) D^(-1/3) <83.707`.

For `|a|>1/2`, the completed orientation-free scalar-pivot/rank-two half-Riesz theorem gives

`||p_Q||_inf <=128(|a|D)^(-1/4) <152.219`.

Therefore every exact spectral coloop satisfies

`||p_Q||_inf <153`.

This includes `a=0` and every nonzero near-null value. I will not duplicate the proof of this now-source-matching theorem.

## New B10 proof-graph splice: pay both ends of the Pluecker-disjointness parameter

Let `R^T R=I_3`, `A=R Lambda R^T`, and let `w_S=det(R_S)^2` be the rank-three Pluecker basis law. For independent `S,T~w`, write

`d=P(S cap T=emptyset)`.

A completed compatible account04 result, `account04/B16` `QFORM-RULED-PLUECKER-ENDPOINT-v1`, gives

`d>=1/64  =>  ||p_Q||_inf <=12 d^(-1/6) <=24`,

using `|det Lambda|>=1`. This is an actual inequality-level application of account04 mathematics.

At the opposite endpoint `d=0`, the completed base-packing classification from account02/B16 has only three cases:

1. at most five nonzero physical rows, paid by one physical triple: `<224.529`;
2. one spectral line plus at most three exceptional rows, paid by finite line-bank compression: `<330.869`;
3. an exact spectral coloop, now paid above by `<153`.

Hence

`d=0 => ||p_Q||_inf <331`.

Thus the old exact-coloop interpolation is no longer a B10 debt. In this Pluecker route the first genuinely unpaid collar is

`0<d<1/64`

with no exact coloop. Current finite-heavy-core work further confines a complementary formulation of this collar to a fixed-cardinality near-null near-line/near-plane heavy core on the minority-sign two-sheet side. The final report will pin that successor precisely and keep continuity separate.
