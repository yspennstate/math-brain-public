# POS3 handoff — fleet04/B11 — 2026-09-22 06:40Z run

**Classification:** `ESSENTIAL_STEP_APPLIED`  
**Parent POS3 status:** OPEN / NOT PROVED.  
**Scientific report:** `proofnet24/collective-POS3/fleet04/B11/20260922T064000Z-B11-pos3-r17/REPORT.md` in `yspennstate/math-open-problems`, report commit `6a046ab4e6cb33a1311fbf7de41a3391d09999da`.

## Exact result to consume

At the first non-exact lower-fringe boundary after the last exact-two crossed state, use the standard six word counts

`A=N(d y x u)`, `Y=N(x d y u)`, `W=N(x u d y)`

and the inherited fleet03/B10 boundary count `B=Y+Z+W`, `Z=K-A`. Then the strict same-polarity overload is exactly

`delta = K-B = A-Y-W > 0`.

Two fixed-position relabellings are exact injections under only the current exact-two identities

`Pred(y)=Pred(x) union {d}`, `Succ(x)=Succ(y) union {u}`:

- `x d y u -> d y x u` (`Y -> A`);
- `x u d y -> d y x u` (`W -> A`).

Their images need not be disjoint, but this is enough: at least `delta=A-Y-W` A-extensions lie outside their union. For every such extension the inverse `A -> Y` relabelling is invalid. Every invalidity has a canonical Hasse witness in

`G1={r:r lessdot x, r||d}` or `G2={r:d lessdot r, r||x}`.

Width at most three gives `|G1|<=2`, `|G2|<=2`. Hence at least `delta` marked original full extensions are exported to at most four actual incomparable-pair channels, so one channel gets at least `ceil(delta/4)` marks.

In the same-polarity no-span branch `d prec_* x`, the witnesses are genuinely outer-ray:

- `r in G1 => r prec_* d`, and the marked event `d<r` is the minority orientation;
- `r in G2 => x prec_* r`, and the marked event `r<x` is the minority orientation.

Thus the first non-exact boundary cannot absorb the overload in the exhausted interval. It exports it immediately to a concrete Hasse minority channel on one of the two outer strong-order rays.

## Partner quantitative application

Applying fleet01/B19 r13, if the same conserved `K` has a four-pair exact-two window at depth `s`,

`K/E >= 4/11-eps_s`, `eps_s=[10/(3(1-rho^2))]rho^s`, `rho=(3-sqrt(5))/2`.

Since a surviving boundary has `B<E/3`,

`delta/E > 1/33-eps_s`,

so one outward boundary Hasse channel receives more than

`(1/132-eps_s/4)E`

marked full extensions. At `s=6` this is already `>0.00454565 E`; asymptotically it approaches `E/132`.

## Exact dependencies

- lead fleet04/B10 r15: `proofnet24/collective-POS3/fleet04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`, blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`;
- assigned partner fleet01/B19 r13: `proofnet24/collective-POS3/fleet01/B19/20260922T054717Z-b19-pos3-r13/REPORT.md`, blob `19f1baa7b3bbe4ed45e19df6ca396f97f6fa5131`;
- first-boundary zero-defect/overload: fleet03/B10 `proofnet24/collective-POS3/fleet03/B10/b10-20260922t061504z-r11/REPORT.md`, blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`;
- Hasse blocker canonicalization template: fleet03/B11 `proofnet24/collective-POS3/fleet03/B11/20260922T061153Z-fleet03-B11-pos3-r11/REPORT.md`, blob `007674a740f490d5c90b2820dadde4d5ee48de52`.

Verifier in the B11 scientific run enumerated naturally labelled width-at-most-three posets through n=6 and checked 2811 exact-two states / 106811 extension instances; terminator `POS3_BOUNDARY_OVERLOAD_EXPORT_CHECK_PASS`. This is regression evidence only; the arbitrary-size proof is symbolic.

## First unpaid implication

`OUTER-RAY REUSE EXCLUSION`: prove that the successive outer-ray Hasse packets from heavy gaps and first non-exact boundaries cannot reuse/reverse already exposed strong-order territory indefinitely in a finite minimal width-three no-balanced core without balance, strict span descent, a four-antichain, a proper autonomous/ordinal reduction, or a separately controlled multi-distinguisher exit carrying the conserved charge onward.

Do **not** replace this by a bounded corridor-length claim; the earlier fleet04/B11 `R_N` family refutes that shortcut even at width three with bounded incomparability range and bounded rank variance.
