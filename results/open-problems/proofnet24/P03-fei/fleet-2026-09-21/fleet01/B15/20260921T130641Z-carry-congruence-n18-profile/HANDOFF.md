# B15 handoff — signed carry moments after the n=18 record profile

Full FEI remains **OPEN / NOT PROVED**. This run was `WITHOUT_VERIFIED_BRAIN` and did not rerun the settled read-once certificate.

## Proved in this run

For a signed Fourier packet `A` with `V(x)=sum_{S in A} eps_S chi_S(x)` and `M_T=sum_{S superset T} eps_S`, the exact valuation criterion is

`r(V) >= r` iff `2^(r-|T|)` divides `M_T` for every `|T|<r`.

The proof is Boolean-cube Möbius inversion applied to

`V(x)=sum_T (-2)^|T| M_T x_T`.

If `m=|A|`, Parseval plus the finite-group uncertainty inequality gives the dimension-free carry obstruction

`m >= 2^r(V)`.

For an equal-magnitude Fourier packet this is `r_a <= log2 |A_a|`. This does not prove FEI; it says deep 2-adic carry requires exponentially many equal-magnitude coefficients.

## Exact n=18 record profile

The Numaro external seed is accepted only after the published truth-table SHA-256 matches. Exact integer-Walsh data:

- `I=261/128`, 2770 nonzero coefficients, 10 magnitude packets.
- `R=39021/32768` exactly.
- `N=19523/8` exactly.
- certified `D` interval inherited from the certified entropy and exact `H=2R+2D`:
  `2.197476238487364041259895110945941157393617519 <= D <= 2.1974762384873640412598951109459411573936175195`.
- valuation masses: `r=0:15827/32768`, `r=1:81/32768`, `r=2:1455/4096`, `r=3:1305/8192`; nothing deeper than 3.
- both depth-3 packets have multiplicity 72.

Against the prior n=14 packet profile, the normalized valuation ledger rises exactly by `16119259/18045440 = 0.893259405146120...`, while the normalized free-energy ledger falls by about `0.861526537746468`. The total record gain is only about `0.0317328674`. Thus the current record is again a large `R <-> D` transfer, not growth of an uncontrolled deep-`D` tail.

## Primary-source boundary

Current primary sources checked 21 September 2026: Numaro NUMARO-2026-016 / Optimization Problems PR #130 for the n=18 record, and Potapov arXiv:2609.21563 for sharp FEI constant 4 on plateaued functions. No publication-priority claim is made for the packet lemmas here.

## Next nonoverlapping B15 step

Derive how the signed upper-incidence moments `M_T` change under a one-coordinate restriction. Try to telescope loss of carry congruence levels against that coordinate's influence. If a local influence charge is false, preserve the smallest genuine Boolean unequal-magnitude counterexample rather than replacing it by a flat-spectrum surrogate.
