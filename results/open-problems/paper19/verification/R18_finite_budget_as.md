# R18 verification - finite-budget almost-sure lower side

## Scope

Round R18 checked whether the finite-budget union-bound corollary can be
upgraded pathwise without passing to a fixed exponential scale.  The target was
the statement that a bound
\[
  \PP\{Y_m^*\le \exp[-(\log|\mathcal T_m|+\log C_m+u_m)/a_m]\}\le e^{-u_m}
\]
implies an eventual almost-sure lower bound at the same threshold whenever
\(\sum_m e^{-u_m}<\infty\).

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0a58-1001-7df3-95c1-95dfabd3fac6` checked the abstract finite-budget
   Borel--Cantelli corollary and the deterministic-data hypotheses.
2. `019f0a58-1fa3-7513-9f55-f51585308964` checked the square and fixed-excess
   finite-entropy applications and the need to keep polynomial slack.
3. `019f0a58-2fd2-77a1-a41f-dcf694ee48aa` checked the two-sided finite-entropy
   application and overlap guardrails.
4. `019f0a58-41c2-7351-94a8-260e77f565da` checked the master Lane O insertion
   point and confirmed the new finite-budget sentence complements the older
   exponential-scale almost-sure paragraph.
5. `019f0a58-4f8d-7192-b29b-83d7a0be9a69` red-teamed random index families,
   random thresholds, tiny exponents, nonuniform constants, strictness, and
   upper-side overclaims.

## Result

The upgrade is valid for deterministic nonempty finite \(\mathcal T_m\) and
deterministic \(C_m\ge1\), \(a_m>0\), and \(u_m>0\).  First Borel--Cantelli gives
\[
  Y_m^*>
  \exp[-(\log|\mathcal T_m|+\log C_m+u_m)/a_m]
\]
eventually almost surely if \(\sum_m e^{-u_m}<\infty\).  No independence across
dimensions and no independence inside the family \(\mathcal T_m\) is used.

The strict inequality is intentional: the controlled bad event is
\(Y_m^*\le t_m\), so Borel--Cantelli gives eventual avoidance of that event
without any continuity assumption.

## Guardrails

The theorem is not stated for random or value-dependent index families.  A
random-budget version would need conditional small-ball control after the
random budget data are fixed.  The applications must keep the polynomial
hard-edge terms, fixed constants hidden in \(O(1)\), and the summable \(u_m\)
slack, especially in small finite-entropy regimes.

The upgrade is lower-side only.  It does not imply a matching upper side, exact
moving-aspect base, two-sided Poisson/extreme process, or supercritical
phase-retrieval reduction.

## Manuscript changes

- `parts/principle.tex`: added `cor:as-finite-budget`.
- `parts/universality.tex`: invoked the corollary for the square finite-entropy
  lower side.
- `parts/geometric.tex`: invoked the corollary for fixed-excess and two-sided
  finite-entropy lower sides.
- `master/chO_phase_retrieval_rmt.tex`: added a compact finite-budget
  Borel--Cantelli sentence in Lane O.
- `PLAN.md`, `STATE.md`, `MASTER_STATE.md`, and `master/ch_overview.tex` were
  updated.

## Build verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  run twice in `paper19`, producing `extremal_hard_edge.pdf` with 33 pages
  and 561,195 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice in `math-open-problems-fleet/master`, producing `master.pdf` with
  853 pages and 7,757,631 bytes; copied to `~/Downloads/master.pdf`.
- Targeted log scan found no LaTeX errors, undefined control sequences,
  undefined references/citations, rerun requests, fatal errors, or emergency
  stops.
