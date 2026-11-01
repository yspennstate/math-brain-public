# R19 verification - nonuniform finite-budget lower side

## Scope

Round R19 checked whether the finite-budget lower-side principle can keep
per-index constants instead of replacing them by a uniform supremum.  The goal
was a weighted union-bound budget of the form
\(\sum_{T\in\mathcal T_m}C_{m,T}\).

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0a5f-a8ba-7ec2-8e46-cbb05f1a6f0f` checked the abstract nonuniform
   finite-budget corollary and caught the \(t\le1\) issue.
2. `019f0a5f-c55e-79a0-ab7c-7339f12263c1` checked square row-submatrix
   heterogeneous-density constants and showed the weighted budget recovers the
   existing global-\(K_m\) polynomial factor.
3. `019f0a5f-d92c-7e83-8271-0897a31dfe44` checked fixed-excess and two-sided
   weighted budgets and recommended avoiding a new single-\(\rho\) theorem.
4. `019f0a5f-e9d5-7243-850b-e22f214c7434` checked the compact Lane O insertion
   and recommended mirroring only the abstract nonuniform budget.
5. `019f0a5f-fde8-7713-945d-32c7b48752fe` red-teamed heterogeneous-density
   shortcuts, random constants, nonuniform exponents, and upper-side overclaims.

## Result

The safe statement is abstract and deterministic.  If
\[
  \PP\{Y_{m,T}\le t\}\le C_{m,T}t^{a_m},\qquad 0<t\le1,
\]
with common deterministic \(a_m>0\), deterministic \(C_{m,T}\ge0\), and
\[
  B_m\ge 1\vee\sum_{T\in\mathcal T_m}C_{m,T},
\]
then
\[
  \PP\left\{Y_m^*\le
  \exp[-(\log B_m+u_m)/a_m]\right\}\le e^{-u_m}.
\]
The condition \(B_m\ge1\) keeps the threshold inside the small-ball range
\(0<t\le1\) and avoids any \(\log0\) convention.

## Guardrails

The corollary uses a common exponent \(a_m\).  Nonuniform exponents require an
implicit budget such as \(\sum_T C_{m,T}t^{a_{m,T}}\le e^{-u_m}\), or a
conservative reduction to the smallest exponent.  The constants and index
families are deterministic; random or value-dependent budgets need conditional
statements after the budget data are frozen.

The agents identified valid heterogeneous-density weighted budgets, but the
notation is bulky and easy to misuse.  The manuscript therefore adds only the
abstract weighted-budget corollary now.  No heterogeneous-density theorem,
upper-side result, exact base, or pair-correlation statement is claimed.

## Manuscript changes

- `parts/principle.tex`: added `cor:nonuniform-finite-budget`.
- `master/chO_phase_retrieval_rmt.tex`: added the compact nonuniform-budget
  version inside Lane O's finite-entropy paragraph.
- `PLAN.md`, `STATE.md`, and `MASTER_STATE.md` were updated.

## Build verification

- Standalone: after a BibTeX refresh, `pdflatex -interaction=nonstopmode
  -halt-on-error extremal_hard_edge.tex` was run to convergence in `paper19`,
  producing `extremal_hard_edge.pdf` with 33 pages and 564,393 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice in `math-open-problems-fleet/master`, producing `master.pdf` with
  853 pages and 7,758,105 bytes; copied to `~/Downloads/master.pdf`.
- Targeted log scan found no LaTeX errors, undefined control sequences,
  undefined references/citations, rerun requests, fatal errors, or emergency
  stops.
