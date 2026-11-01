# Ranked candidate list (percolation, random graphs, discrete probability on graphs)

Built 13 September 2026 from the six append-only ledgers (last row per id wins):
`Probability_1000_20h_20260906` (P####), `probability_1000_intake_claude_20260907` (C####),
`..._intake_D_20260908`, `..._intake_E_20260908`, `..._intake_F_20260908`, `..._intake_G_20260910`.
1,025 admitted problems in total; 226 fall in the area of this note after keyword screening
(`code/extract2.py` writes a full dump, not included here, with each problem's source,
statement, result status and the *obstruction* field of every recorded attempt — the obstruction
field is the campaign's own record of where the last attempt stopped).


## Ranking principle

Not "how important" but "how close the record says it is to a checkable result". Three bands:

**Band 1 — a finite object decides it.** The statement is an inequality or an identity about
finite graphs, so an exact machine computation can *refute* it outright, or verify it on a range,
or a short conditional argument can settle a sub-family. These are the only ones worth attacking
in a single day.

**Band 2 — a finite reduction exists but the remaining step is asymptotic.** Worth a reduction
memo, not an attack.

**Band 3 — the obstruction named in the ledger is a known hard barrier** (conformal invariance,
arm exponents, `theta(p_c)=0`, scaling limits, replica-symmetry-breaking thresholds). Not
attackable here; they are listed so the ranking is complete.

## Band 1 (attacked today, in the order attacked)

| id | title | why band 1 | what I did |
|----|-------|-----------|-----------|
| C0091 | Negative correlation for the random-cluster model with `q<1` | pure finite-graph inequality in `(p_e, q)`; a single counterexample graph would settle it | attacked — memo `C0091_...md`: exact conditional classification proved + machine-verified, three complete sub-cases proved, coefficient certificate refuted, exhaustive weighted search on all graphs with <=6 vertices found nothing |
| P0001 | Negative correlation in uniform forests (Grimmett Conj. 4.2) | `N(G)N(G/ef) <= N(G/e)N(G/f)`, exact integer arithmetic | attacked — memo `P0001_...md`: exact covariance identity proved + machine-verified, parallel/series/bridge cases proved with an exact value, dense 9–10 vertex search |
| P0037 | BK-type inequality for the weighted uniform spanning tree (Lyons–Peres) | finite: enumerate spanning trees and increasing events | attacked — memo `P0037_...md`: first computer search of the conjecture I could find; none found |
| C0146 | Monotone coupling of random-cluster measures in `p` for `q<1` | equivalent to `Cov(1_A, |omega|) >= 0` for every increasing `A`, which is an exact min-closure (max-flow) computation | attacked — see `C0146_...md`; also produced a clean incompatibility observation |

## Band 1, identified but not attacked (the natural next targets)

| id | title | the finite question |
|----|-------|--------------------|
| G0010 | Tight subcritical bound on the largest component from `Delta(G)` and `lambda(G)` | the conjectural formula `max_H log|H| / log(1/(p lambda(H)))` over induced subgraphs can be tested exactly on small graph families; the ledger says the missing piece is only the multiplicity term |
| E0053 | `MaxBis + MinBis = dn/2 + o(1)` for random `d`-regular graphs | exact for small `d` and small `n` by exhaustive bisection; the ledger's obstruction ("no exact sign symmetry at fixed `d`") is quantifiable numerically at `d=3` |
| P0013 | Expected Lovasz theta of a dense independent-edge graph | an SDP that is computable exactly for small `n` |
| E0088–E0091 | Noise sensitivity/stability of bootstrap percolation | finite-`n` influence spectra are computable exactly on small tori |
| P0169 | Linear Fourier mass vs Boolean degree | the ledger already has the Chebyshev obstruction to the relaxed method; the Boolean-only question is a finite LP for each small `d` |
| G0008 | Monotonicity of `P_p(0 <-> (0,n))` on `Z^2` | the ledger's A002 withdrew the small-`p` claim; a finite-cylinder exact enumeration in `p` is the natural next probe, but it cannot settle the infinite-volume statement |

## Band 2 (reduction-worthy, not attackable today)

G0004 and G0005 (the Flammant / Kozma–Nitzan boundary-connectivity conjectures implying
`theta(p_c)=0`) — G0005 is already reduced in the ledger to a bound on `E[N_A]`, and the open
regime is exactly `A` a face of a box; F0095 (chromatic number of `G(n,d/n)` one-value
concentration) reduces to existence of `lim d_k(n)`; F0096 (Hamiltonicity above density 3/2)
reduces to Robinson–Wormald for unbounded maximum degree; F0104 / F0111 (Talagrand's small
classes) reduce to a rounding problem for fractional covers; P0047, P0045, F0080 (free spanning
forest invariants) reduce to `l2`-Betti-number statements.

## Band 3 (known hard barriers — named, not attacked)

C0017, C0018, C0020, C0023, C0049, C0050, C0063–C0096 (the whole high-dimensional block),
C0125–C0160, D0060, D0062, D0068, D0079, E0001–E0006, E0033–E0036, F0022–F0025, F0038, F0039,
P0022, P0061, P0124, P0128–P0131, P0141–P0160, P0360–P0371 (frozen percolation),
P0408–P0421 (ideal Voronoi). For each of these the ledger's own `obstruction` field names a
barrier that is the subject of a research programme, not of a day's work.

## Note on the ranking

The keyword screen is generous (it pulls in Ising, GFF and dimer items that arguably belong to a
neighbouring area). I did not touch anything outside percolation / random graphs / discrete probability
on graphs. The four problems I attacked were chosen because each reduces to arithmetic on finite
graphs, so a negative day still produces a certificate rather than a feeling.
