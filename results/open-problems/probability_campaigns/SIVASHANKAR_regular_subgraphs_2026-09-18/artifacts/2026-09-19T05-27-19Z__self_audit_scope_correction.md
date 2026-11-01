# Self-audit scope correction — 2026-09-19T05-27-19Z run

This artifact preserves the immutable run report and corrects one overbroad interpretation before the next run. It is **not** a second run report.

Report being audited:

`probability_campaigns/SIVASHANKAR_regular_subgraphs_2026-09-18/runs/2026-09-19/2026-09-19T05-27-19Z__report.md`

## Correct scope of Theorem 6.1

The proof in Section 6 is valid as a theorem about the **positive exact-zero-slack barrier subsystem** in the clean single-gap one-cycle model:

- on an odd cycle, one selected vertex pierces every positive row;
- on an even cycle, two selected vertices pierce every positive row.

It does **not** by itself prove a feasible omitted set for the **full all-signed Tutte system**, and therefore it does not prove an actual bound on `g_k(B)` even inside that clean model.

The phrases “integral signed repair number” and “any surviving one-cycle counterexample must use multiple zero intervals” in the immutable report must be read with this correction: the proved quantity is the positive-row piercing number only. The source metric was correctly left unchanged.

## Why positive piercing is insufficient

Recall the exact all-signed condition

\[
k\bigl(|X\cap T|-|X\cap S|\bigr)\ge \operatorname{def}_k(S,T)
\qquad\text{for every disjoint }S,T.
\]

For an exact nontrivial zero-slack row in the cactus substrate, every `U`-component has exactly one edge to `S` and one edge to `T`, `d-q=0`, and `Delta_d=d_B(T)-d_B(S)=0`. Because `k` is even, reversing the signed pair preserves the parity-component count: `(T,S)` is also an exact zero-slack row.

If the original row has `h=|T|-|S|=1`, then

\[
\operatorname{def}_k(S,T)=k,
\qquad
\operatorname{def}_k(T,S)=-k.
\]

Thus a set `X` feasible for **both** orientations must satisfy

\[
|X\cap T|-|X\cap S|\ge1
\]

and

\[
|X\cap S|-|X\cap T|\ge-1,
\]

so in fact

\[
\boxed{|X\cap T|-|X\cap S|=1.}
\tag{A}
\]

This equality requirement is strictly stronger than merely piercing the positive row.

In particular, in the even-cycle proof of the immutable report the chosen two vertices can both lie in `T` for a positive row whose unique gap is elsewhere. Then the signed difference is 2: the positive row is satisfied, but its reverse row violates (A). Therefore the two-vertex positive-piercing construction is **not** an all-signed support-rounding construction.

For the odd-cycle proof, the one common positive atom gives signed difference exactly 1 on each positive row and therefore also satisfies each immediate reverse row. However, zero-demand (`rho=0`) or other nonpositive rows not included in the clean positive family may still be violated. No `g_k(B)` theorem follows without controlling them as well.

## Correct mathematical takeaway

The run establishes a genuine orientation-compression fact:

> In the clean single-gap one-cycle exact-cactus model, first-scale deficiency mass prevents the **positive** barriers from forming an unbounded piercing obstruction: their positive piercing number is at most 1 on odd cycles and at most 2 on even cycles.

The run does **not** yet establish bounded all-signed rounding. The irreducible obstruction is sharper than stated in Section 7 of the report: it may already occur with one gap through the simultaneous negative/reverse rows, especially on even cycles; multiple gaps are not yet necessary.

## Correct next obligation

Before increasing the number `z` of zero/U intervals, the next run must first solve or refute the **all-signed single-gap one-cycle** problem:

\[
\text{find bounded }|X|\text{ satisfying every signed row, not only every positive row.}
\]

A useful exact subquestion is whether the graph-realizable exact-cycle structure forces enough compatibility among the reverse and `rho=0` rows to round the fractional equality system. If not, construct a genuine graph-realizable even-cycle family with one gap per positive row and unbounded integral all-signed repair while the first-scale LP remains `<2`.

Only after this all-signed `z=1` question is decided should the campaign promote `z=2` / multi-gap deformation as the next obstruction.

## Status impact

- `beta_even`: unchanged at `>=1/2`.
- source status: `PARTIAL / OPEN`.
- post-Recovery-2 unchanged count: `1`.
- recovery state: `2/2 consumed`; no Recovery 3.
- no audit status changes.
