# R17 verification - finite-entropy two-sided lower side

## Scope

Round R17 checked the two-sided analogue of the R16 finite-budget lower sides.
The question was whether the two-sided row-column entropy can be kept exactly:
\[
  L_k^{\rm two}
  =\log\binom{N_k}{k}+\log\binom{n_k}{k}.
\]
Only lower-side union-bound estimates were considered.

## Five-agent audit

Exactly five read-only agents were launched and then closed after reporting.

1. `019f0a50-3a81-7492-bdc1-820c4d4ead79` checked the constants and the single \(K_k\) power.
2. `019f0a50-3ad5-7a71-a369-f26b7c203f0a` adversarially checked barely-square, one-side-huge, fast-density, non-identical-entry, complex, and overlap cases.
3. `019f0a50-3b29-7d03-bf04-2cd410a64376` scouted the standalone insertion point and ledger updates.
4. `019f0a50-3b71-7932-9827-cffca26c6aa2` checked the compact Lane O formulation.
5. `019f0a50-3bb7-7c21-9427-82f7512194c9` checked whether a full theorem would be redundant and recommended a compact corollary/paragraph.

## Result

For independent entries with \(d_\F\)-dimensional scalar densities bounded by
\(K_k\), one selected \(k\times k\) minor satisfies
\[
  \PP\{\sigma_{\min}(A_{R,C})\le t\}
  \le C_\F K_k k^{d_\F+1}t^{d_\F}.
\]
Applying the finite-budget principle to
\(\mathcal T_k=\{(R,C):|R|=|C|=k\}\) gives
\[
  \PP\left\{M_k^{\rm two}\le
  \exp\left[-\frac{
  L_k^{\rm two}+\log K_k+(d_\F+1)\log k+O_\F(1)+u_k}{d_\F}\right]\right\}
  \le e^{-u_k}.
\]
The density cost is a single \(\log K_k\), not two powers and not \(k\log K_k\).
Row-column overlap is irrelevant for this lower side because the proof is only
a union bound.

## Guardrails

The statement is lower-side only.  It does not prove a moving-aspect two-sided
upper side, exact base, or Poisson extreme process.  If
\(L_k^{\rm two}=O(\log k)\), the polynomial hard-edge factor can affect the
finite scale, so the displayed polynomial slack should not be dropped.

## Manuscript changes

- `parts/geometric.tex`: added `two:finite-entropy` after the two-sided
  density-rate lower side and referenced it in the moving-aspect remark.
- `master/chO_phase_retrieval_rmt.tex`: added a compact two-sided finite-entropy
  paragraph after the two-sided lower-side theorem.
- `PLAN.md`, `STATE.md`, and `MASTER_STATE.md` were updated.

## Build verification

- Standalone: `pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex`
  run twice in `paper19`, producing `extremal_hard_edge.pdf` with 32 pages
  and 554,966 bytes.
- Master: `pdflatex -interaction=nonstopmode -halt-on-error master.tex` run
  twice in `math-open-problems-fleet/master`, producing `master.pdf` with
  853 pages and 7,757,237 bytes; copied to `~/Downloads/master.pdf`.
- Targeted log scan found no LaTeX errors, undefined control sequences,
  undefined references/citations, rerun requests, fatal errors, or emergency
  stops.
