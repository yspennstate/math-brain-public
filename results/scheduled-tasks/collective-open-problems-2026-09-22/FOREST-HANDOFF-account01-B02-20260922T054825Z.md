# FOREST handoff — account01/B02 — rank-CLC correction + disconnecting switch

Outcome: `CANDIDATE_REFUTED` for the rank-homogeneous strengthening in lead `FOREST-TRIANGLEFREE-SIMPSON-BUDGET-v1`; parent FOREST remains open. Context: `WITHOUT_VERIFIED_BRAIN`.

Canonical report: `yspennstate/math-open-problems`, `proofnet24/P14-probability-correlation/collective-2026-09-22/account01/B02/20260922T054825Z-b02-forest-auto11/report.md`, creation commit `4526e04cfaf0f4e752283e9c2003b0fa2f35a238`, report blob `7b500e2bc01d8788d526de9db984f52d6abe5d65`.

## Decisive correction

The lead's polynomial `sum_I y^(R-|I|) z^I` with `R=rank(M)` is not the ALOV independent-set CLC homogenization. ALOV III arXiv:1811.01600 uses the **ground-set size** `n` in `y^(n-|I|)`. The rank-degree substitute fails already on `K_3`: for `(y,z1,z2)`, `grad h grad h^T-h Hess h=[[11,8,8],[8,9,2],[8,2,9]]` has determinant `-49`. The lead's rank-(A2) fails by `8/245`, its derived variance bound fails by `3/98`, and its rank slack-edge-edge block has determinant `-1/2401`. Revert to the source-valid ground-set-degree (`m-mu`) CLC budget unless an independent proof of the stronger rank edge-row inequality is supplied. The triangle-free Simpson conditioning theorem itself survives this correction.

## Named OTHER-account result applied

Applied account02/B03 `20260922T051049Z-b03-forest-auto11`, report blob `57bd1c4cceaa39ba9db44f4f024a3b9a4f41c65c`: its exact rational unitizer/parallel-class desingularization proves that a global `{1,2}` STAR-2 theorem can be converted exactly to unit simple graphs with Rayleigh gap scaled by a positive square. Conversely, attaching one pendant weight-2 edge to any unit graph multiplies the queried gap by `9`. Hence **global STAR-2 is parent-equivalent**. The only useful debt is the minimality-conditioned contraction instance from the lead.

## Source-exact new target and switching primitive

For `g=uv`, deletion of `g` is a bijection

`{F forest of G: g in F} <-> {A forest of G-g: u and v disconnected}`,

preserving queried `e,f`. Thus the lead's STAR-2 conditional gap is exactly

`D_10 D_01 >= D_00 D_11`,

where `D_ij` counts forests of the smaller simple graph `H=G-g` with `u not connected v` and `(e,f)` status `(i,j)`.

A multiplicity-one repair involution is proved: if `F` is such a disconnected forest and `x` is an absent edge for which `F+x` connects `u,v`, let `P` be the unique `u-v` path in `F+x`; for any marked `h in P-{x}`, `F'=F+x-h` is again a forest with `u,v` disconnected, and `(F;x,h) <-> (F';h,x)` is an exact involution. The remaining debt is to choose/charge `h` in the full `D_00 x D_11 -> D_10 x D_01` exchange so fibers cancel.

## No-go for scalar-only proof

Formal strata `g=0:(4,7,9,9)`, `g=1:(6,4,0,0)` in `(ef)=(00,10,01,11)` have `Delta_ef(t)=27-18t`: deletion `27`, unit `9`, contraction endpoint `0`, and unit pair gaps `(ef,eg,fg)=(9,44,180)` are all nonnegative, yet doubling gives `-9`. This is not claimed graph-realizable; it proves scalar endpoint/unit signs alone cannot pay STAR-2. Graphic switching is essential.

Exact checker/output are in the canonical run and return `STATUS=PASS`.
