# FOREST B01 handoff — exact rational unitization and Q-3-connected equivalence

Run `account04-b01-20260922T051009Z-forest-r12`; outcome **ESSENTIAL_STEP_APPLIED**; parent FOREST remains **OPEN**; context `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account04/B01/account04-b01-20260922T051009Z-forest-r12/report.md`, Git blob `131c9ee124b5ba9c6383bbf869ab09ffb277df19` in `yspennstate/math-open-problems`, creation commit `7254bce571c6d85469bd901ca61552a2ab620560`.

## New exact result

For a unit two-terminal network let `rho=C/D`, where `C,D` count connecting/disconnecting forests. Parallel and series composition give

`rho_parallel=r1+r2`,

`rho_series=r1*r2/(1+r1+r2)`.

Starting from response `1`, use the simple theta `K_{2,3}` (also response `1`, no terminal edge) to implement `P(r)=r+1`, and a fresh unit edge in series to implement `S(r)=r/(r+2)`. Every positive rational `a/b` is obtained by a finite word in `P,S`: invert by `a/b -> (a-b)/b` when `a>b`, and `a/b -> 2a/(b-a)` when `a<b`. The height `a+b` strictly decreases after finitely many inverse steps, so termination is proved.

Therefore **every positive rational response has an exact finite simple unit realization**.

If unmarked base edges are replaced by internally disjoint two-terminal unit networks with responses `r_h`, exact projection of forests gives

`Delta_H(e,f;1)=(prod_h D_h)^2 Delta_G(e,f;r)`.

Consequently the following are equivalent, without the rejected fixed-graph Cocks implication:

1. unit FOREST for every finite simple graph;
2. positive-rational weighted Rayleigh FOREST for every finite simple graph;
3. positive-rational weighted Rayleigh FOREST for every 3-vertex-connected finite simple graph, with `K_3` as the small base.

The implication 3=>2 is by exact two-cut induction. For uv-bridges `B_i`,

`Z=prod D_i + sum_i C_i prod_{j!=i}D_j`.

Same-bridge pair:

`Delta_G=A_i^2 Delta_{B_i+g_i}(e,f; y_g=sum_{j!=i} C_j/D_j)`.

The virtual weight is rational and the augmented bridge is strictly smaller. Cross-bridge pair:

`Delta_G=A_ij^2 R_i(e)R_j(f)`,

`R_i=D_i C_{i,e}-C_i D_{i,e}=Delta_{B_i+g_i}(e,g_i)` for a non-singleton bridge; an original singleton uv separator edge has `R=1`. This explicitly pays all separator-edge and cross-bridge cases.

## Correction to the prior unit-minimal 3-connected claim

The previous account04/B01 `FOREST-UNIT-MINIMAL-3CONN-v2` remains withdrawn, consistently with the current lead correction. The exact unitization above does **not** repair edge-minimality because an exact gadget need not be smaller.

In fact, if a unit two-terminal network with `m` edges has reduced response `a/b`, then `C+D=k(a+b)<=2^m`, so `m>=ceil(log2(a+b))`. A length-ell unit path has response `1/(2^ell-1)` and attains equality; hence no exact unit realization of that path response can use fewer than ell edges. Already a two-edge path produces `1/3`, which cannot be compressed to one unit edge.

Thus any future proof that a **unit-minimal** counterexample itself is 3-connected must genuinely control path-ear attenuations; exact rational unitization plus edge counting cannot do it.

## Named peer applied

Applied account01/B02 run `20260922T041812Z-b02-forest-r11`, report blob `07794d469ced157633cd07c57caaaf3e3bbe4066`: its source correction rejects the fixed-graph Cocks transfer and identifies the gadget family `q=k/(2^a-1)` as the correct class-level mechanism. The new theorem upgrades that dense special family to exact realization of every positive rational and closes the separator induction over Q.

Latest lead version consumed: account01/B01 `20260922T043718Z-b01-forest-auto11`, report blob `adc332e97b112525d92cf601ad1493f2e1745987`, which withdrew the prior full candidate and preserved the complete-graph Hermite theorem.

Regression code/output blobs: `1beebb5779dbf0367b8e5a083bb7ef023288c1f4` / `e7fd2c3ff223ad6cccb9a1f61e46aab4628cb46d`; output `STATUS=PASS` on 4096 rational pairs. Regression is not the proof.

## Remaining target-level obligation

The exact residual is rational-weight Rayleigh pNC on all 3-connected simple graphs (equivalently the parent target by the theorem above). Do not relabel this as an easier closure lemma. The complete-graph unit Hermite result is only one symmetric slice of this residual.
