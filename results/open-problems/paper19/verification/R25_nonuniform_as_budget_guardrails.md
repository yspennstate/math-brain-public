# R25 verification - weighted almost-sure budgets and guardrails

## Scope

Round R25 added the almost-sure version of the nonuniform finite-budget lower
side and applied it to the deterministic heterogeneous budgets already present
in the manuscript.  The same round also incorporated read-only audit fixes for
rectangular/two-sided notation, phase-retrieval wording, citations, and compact
Lane O hypotheses.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0c76-2139-71f3-93e7-6d0e65b6a14d` checked the new fixed-excess
   entrywise heterogeneous proof and found no proof-soundness issue.
2. `019f0c76-4625-7363-98f8-27444fc277b0` identified the nonuniform
   almost-sure finite-budget corollary as the lowest-risk theorem-quality next
   addition.
3. `019f0c76-afd3-7d61-8294-0e9826d43c1f` compared standalone statements with
   Lane O and flagged missing deterministic/independence guardrails in compact
   master wording.
4. `019f0c77-1203-7462-b8ee-557e60dac03c` audited the phase-retrieval and
   citation surface, flagging overstrong Randomstrasse wording, a local
   full-spark citation gap, and missing DOIs.
5. `019f0c77-3e04-79f2-a04d-7866cadcb685` audited notation in
   `parts/geometric.tex`, flagging row/column dummy-variable confusion and
   local `A_k` versus `A_{R,C}` mismatches.

## Result

The new abstract corollary is `cor:as-nonuniform-finite-budget`.  If
\[
  \PP\{Y_{m,T}\le t\}\le C_{m,T}t^{a_m},\qquad
  B_m\ge 1\vee\sum_T C_{m,T},
\]
all finite-budget data are deterministic, and \(\sum_m e^{-u_m}<\infty\), then
on any common coupling,
\[
  Y_m^*>\exp[-(\log B_m+u_m)/a_m]
\]
eventually almost surely.  The proof is exactly the nonuniform union bound plus
the first Borel--Cantelli lemma; it uses no independence across dimensions or
inside the tested family.

This was then connected to:

- the square entrywise density-profile budget `cor:entrywise-profile-square`;
- the fixed-excess row-wise heterogeneous budget
  `rect:heterogeneous-row-density`;
- the fixed-excess entrywise heterogeneous budget
  `rect:entrywise-heterogeneous-fixed-excess`;
- the heterogeneous two-sided finite budget
  `two:heterogeneous-finite-budget`.

## Guardrails and cleanup

The rectangular proof now uses `C_q` for the conditioned column and row dummy
`a` for products over row blocks.  The two-sided finite-budget corollaries now
write the local minor as `((A_k)_{R,C})` and make the row/column domains
explicit.  The heterogeneous two-sided proof names the bad row before using
`K_{k,i,j}`.

The phase-retrieval prose now states that Shmalo answers the Randomstrasse
problem at the exponential-base level, not as an exact finite-\(m\) formula.
The Rademacher obstruction corollary cites the complement-property/full-spark
equivalence locally.  The complex open problem now says the generic \(4m-4\)
threshold.  DOIs were added for the Balan--Wang, Bandeira--Cahill--Mixon--Nelson,
and Conca--Edidin--Hering--Vinzant ACHA references.

Lane O now marks the finite density budgets as deterministic where needed and
restates the independent-entry setup for the fixed-excess entrywise and
proportional-excess density-rate summaries.

## Build verification

`pdflatex -interaction=nonstopmode extremal_hard_edge.tex`, `bibtex
extremal_hard_edge`, and two further `pdflatex` passes were run.  The final
standalone PDF has 39 pages and is 599,275 bytes.

`pdflatex -interaction=nonstopmode master.tex` was run twice in
`~/math-open-problems-fleet/master`.  The final master PDF has 853
pages and is 7,759,894 bytes.  It was copied to
`~/Downloads/master.pdf`.

Targeted log scans found no errors, undefined references/citations, or rerun
requests; the only matched lines were the two final `Output written` lines.
