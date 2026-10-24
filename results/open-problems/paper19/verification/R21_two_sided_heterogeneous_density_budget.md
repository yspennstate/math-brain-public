# R21 verification - two-sided heterogeneous-density finite budget

## Scope

Round R21 checked a conservative two-sided finite-budget refinement for
entry-dependent deterministic scalar density bounds.  It is a lower-side
union-bound result only.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0c5f-6b0c-7102-a44a-e789778e111a` checked the fixed-minor
   distance-to-hyperplane proof and confirmed the bound
   \(C_\F k^{d_\F}t^{d_\F}\sum_{i\in R}\max_{j\in C}K_{k,i,j}\).
2. `019f0c5f-d1ad-7251-81e6-1e7db7922913` checked the weighted-family
   combinatorics and the uniform-density specialization.
3. `019f0c5f-e92a-7b62-a268-56305b4cfa97` checked the asymptotic consequence
   and recommended a corollary after the two-sided finite-entropy result.
4. `019f0c60-074c-74e0-8e88-5db526c9b67a` red-teamed random budgets, singular
   parts, complex-density assumptions, coordinate choice, and exact-base
   overreach.
5. `019f0c60-1e45-7a83-acbf-8666c12ce69b` checked placement, labels, Lane O
   wording, and ledger updates.

## Result

For fixed row and column sets \(R,C\), \(|R|=|C|=k\), put
\[
  K_{k,i,C}=\max_{j\in C}K_{k,i,j}.
\]
The one-minor estimate is
\[
  \PP\{\smin(A_{R,C})\le t\}
  \le
  C_\F k^{d_\F}t^{d_\F}\sum_{i\in R}K_{k,i,C},
  \qquad 0<t\le1.
\]
The exact weighted family sum is
\[
  \sum_{\substack{|R|=k\\ |C|=k}}\sum_{i\in R}K_{k,i,C}
  =
  \binom{N_k-1}{k-1}
  \sum_{i=1}^{N_k}\sum_{\substack{C\subset[n_k]\\ |C|=k}}K_{k,i,C}.
\]
Thus the finite threshold has numerator
\[
  \log\binom{N_k-1}{k-1}
  +\log\sum_i\sum_{|C|=k}K_{k,i,C}
  +d_\F\log k+O_\F(1)+u_k.
\]
If all \(K_{k,i,j}=K_k\), this becomes the existing two-sided finite-entropy
budget
\[
  L_k^{\rm two}+\log K_k+(d_\F+1)\log k+O_\F(1)+u_k.
\]

## Guardrails

The density bounds are deterministic and the entries are independent.  The
complex case requires genuine two-real-dimensional densities on
\(\C\simeq\R^2\).  The coordinate chosen in the distance-to-hyperplane proof is
normal-dependent, so the proof pays \(\max_{j\in C}K_{k,i,j}\).  Singular or
atomic parts, random or value-dependent budgets, nonuniform exponents, upper
sides, exact bases, Poisson laws, and pair-correlation claims are not covered.

## Manuscript changes

- `parts/geometric.tex`: added `two:heterogeneous-finite-budget`.
- `master/chO_phase_retrieval_rmt.tex`: added a compact Lane O finite-budget
  sentence.
- `PLAN.md`, `STATE.md`, and `MASTER_STATE.md` were updated.

## Build verification

`bibtex extremal_hard_edge` was run after the first standalone pass exposed
stale citation state, followed by the needed `pdflatex` passes from `paper19/`.
The final standalone PDF is 36 pages / 577,951 bytes.

`pdflatex -interaction=nonstopmode -halt-on-error master.tex` was run from
`math-open-problems-fleet/master/`; the final master PDF is 853 pages /
7,758,359 bytes and was copied to `~/Downloads/master.pdf`.

Targeted log scans found no LaTeX errors, undefined control sequences,
undefined references, undefined citations, fatal stops, emergency stops, or
rerun requests.  The only targeted matches were the two expected
`Output written` lines.
