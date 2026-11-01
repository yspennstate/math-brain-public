# HARD8-03 — 2026-09-16T09:22:00Z checkpoint verification addendum

This is an append-only verification/strengthening companion to:

`hard8_2026-09-16/HARD8-03/runs/2026-09-16/2026-09-16T09-22-00Z__report.md`.

## 1. GitHub receipts

- Primary mathematical report creation commit: `90419f340dbd3e30423e9a5f51fa52d4045b7dac`.
- Primary report read back successfully at exactly commit `90419f340dbd3e30423e9a5f51fa52d4045b7dac`: **VERIFIED**.
- Exact verifier path: `hard8_2026-09-16/HARD8-03/artifacts/2026-09-16T09-22-00Z__optimized_rank_tail_verifier.py`.
- Verifier creation commit: `afe109f6bb575c10e77894e8f10b2817367d81b0`.
- Verifier read back successfully at exactly that commit: **VERIFIED**.
- Verifier blob SHA returned on readback: `452ca7541c97aae7cc4fd309a89b89523b90f960`.
- Approval/security denial: **NOT EXPOSED**.

## 2. Exact execution completed

The archived pure-Python verifier was executed successfully using exact integer and `fractions.Fraction` arithmetic.

### Heterogeneous coordinate-partition checks

It exhaustively enumerated every maximal dissociated set for the following representative heterogeneous families and confirmed the report formulas for rank, maximal-set classification, omitted-column widths, and optimized profile:

- `h=(2,3)`: rows `6`, columns `5`, rank `4`, maximal sets `5`, optimized profile `{0:1,1:0,2:0,3:0}`.
- `h=(2,4)`: rows `8`, columns `6`, rank `5`, maximal sets `6`, optimized profile `{0:1,1:0,2:0,3:0,4:0}`.
- `h=(2,2,3)`: rows `12`, columns `7`, rank `5`, maximal sets `16`, optimized profile `{0:2,1:0,2:0,3:0}`.
- `h=(2,3,3)`: rows `18`, columns `8`, rank `6`, maximal sets `21`, optimized profile `{0:2,1:1,2:0,3:0}`.

In each case it also checked that choosing a maximum-size group as the unique complete group simultaneously attains every threshold optimum.

### Direct-sum check

For two copies of the `(2,2)` coordinate configuration, each block has optimized profile

`{0:1,1:0,2:0}`,

while their disjoint row-block direct sum has profile

`{0:2,1:0,2:0}`.

The verifier exhaustively found `16` maximal dissociated sets in the direct sum and checked exact rank additivity, providing a finite execution check of Theorem 5.1/Corollary 5.2.

### Rank-5 basis-dependence configuration

For the 14-column configuration in Sections 6–7 of the report, the verifier checked:

- the displayed six-vector bad set is dissociated and has real rank `5`;
- its eight omitted target columns have exact minimum negative widths
  `2,3,2,2,2,2,2,2`;
- those eight heavy columns span full rank `5`;
- the complete 14-column configuration has exactly `623` maximal dissociated sets, of sizes `6` and `7`;
- exhaustive optimization over all `623` maximal sets gives

`rho_V(0)=2`,

`rho_V(1)=rho_V(2)=rho_V(3)=0`.

Thus the basis dependence is even stronger than the main report needed: the same configuration ranges from a maximal set with **full rank-5** `k=1` heavy tail to a maximal set with **no** `k=1` heavy columns at all.

This strengthens, but does not contradict, Section 7 of the primary report. Section 7 exhibited a second maximal set with heavy rank `2`; it did not claim that set was optimal.

## 3. Explicit width-at-most-one optimized basis for the rank-5 configuration

An exact maximizing/repairing maximal dissociated set is

`G = {g1,...,g6}` with

- `g1=(0,0,1,0,0)`,
- `g2=(0,1,0,1,0)`,
- `g3=(1,0,1,1,0)`,
- `g4=(1,1,1,1,0)`,
- `g5=(1,0,0,0,1)`,
- `g6=(0,1,0,1,1)`.

Every one of the 14 configuration columns has a signed representation over `G` using at most one negative coefficient. The eight omitted columns admit the following explicit coefficient vectors in the order `(g1,...,g6)`:

- `(1,0,0,1,0)`: `(-1,0,1,0,0,0)`;
- `(0,0,1,1,1)`: `(1,0,1,-1,0,1)`;
- `(1,0,1,1,1)`: `(0,-1,1,0,0,1)`;
- `(1,1,1,1,1)`: `(0,-1,0,1,0,1)`;
- `(0,1,1,0,0)`: `(1,0,-1,1,0,0)`;
- `(0,1,0,0,1)`: `(1,1,-1,0,1,0)`;
- `(1,0,1,0,1)`: `(1,0,0,0,1,0)`;
- `(1,1,1,0,1)`: `(1,0,-1,1,1,0)`.

The other six columns are the members of `G` themselves and have width zero. The verifier checks that `G` is dissociated; since every omitted column is representable, adding any one of them creates a signed relation, so `G` is maximal.

This gives a fully inspectable exact certificate for `rho_V(1)=0` in this configuration.

## 4. Interpretation for the next run

The new finite witness should **not** be used to weaken the optimized rank-tail conjecture. It says the opposite: optimizing the maximal dissociated set can completely eliminate a full-rank heavy tail that is present for a poor maximal set.

The useful falsification target remains the optimized quantity

`rho_V(k)=min_S rank(H_k(S))`.

Because the primary report proved direct-sum additivity, any finite configuration with `(k+1)rho_V(k)>rank(V)` would amplify to arbitrary rank and refute the proposed constant-1 route. The next bounded search should therefore optimize over all maximal sets from the start rather than examine local widths of a fixed HLS basis.
