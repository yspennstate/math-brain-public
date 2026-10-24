# R30 verification - directional row anti-concentration

Date: 2026-06-28.

## Scope

This round used exactly five read-only audit agents:

1. `019f0c99-9d88-7d00-a655-9db5f5e3dcfa` audited the square
   row-submatrix lower side under independent rows with uniform directional
   small-ball bounds.
2. `019f0c99-9dcf-7d73-b64a-156e53e5cfab` audited isotropic log-concave row
   applications and recommended proving only the lower side while leaving the
   exact law open.
3. `019f0c99-9e10-7400-be7b-2d0f7b3b778d` audited smoothed deterministic row
   models and identified the need for affine, not merely centered, projection
   anti-concentration.
4. `019f0c99-9e4c-7d52-bf56-45e6d2db6d8b` audited compact Lane O summary
   guardrails and notation conflicts.
5. `019f0c99-9e8d-73e2-a8b7-45ec0e60fc20` audited phase-retrieval
   consequences and restricted them to the real critical Balan--Wang
   lower-side setting.

No terminal-launched agents, background daemons, or scheduled tasks were
created.

## Main changes

1. Added `cor:directional-row-lower`.  For independent rows satisfying
   \[
     P\{|\langle R_{m,i},u\rangle-z|\le r\}\le L_{m,i}r^{d_F}
   \]
   uniformly over deterministic unit directions, affine centers, and
   `0<r<=1`, the square lower-side budget is
   \[
     \log\binom{N_m-1}{m-1}
     +\log\sum_iL_{m,i}
     +(d_F/2)\log m .
   \]
   Summable `e^{-u_m}` gives the corresponding eventual a.s. lower bound.
2. Added `cor:logconcave-lower`: real iid isotropic log-concave rows satisfy
   the directional-density hypothesis, hence have lower-side base `h(gamma)`.
   The exact log-concave extremal law remains open.
3. Added the real critical phase-retrieval lower-side corollary
   `cor:pr-directional-lower`: at `N=2m-1`, independent real rows with
   subexponential directional budget are full spark a.s. and satisfy the
   Balan--Wang lower envelope with base `1/4`.
4. Added the compact Lane O master summary for directional anti-concentration,
   real log-concave lower side, and the real critical Balan--Wang guardrail.
5. Added the convex-geometry reference
   `BrazitikosGiannopoulosValettasVritsiou2014`.

## Verification

Standalone build:

```text
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
bibtex extremal_hard_edge
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
pdflatex -interaction=nonstopmode -halt-on-error extremal_hard_edge.tex
```

Final standalone log scan:

```text
Output written on extremal_hard_edge.pdf (45 pages, 647008 bytes).
```

Master build:

```text
pdflatex -interaction=nonstopmode -halt-on-error master.tex
pdflatex -interaction=nonstopmode -halt-on-error master.tex
```

Final master log scan:

```text
Output written on master.pdf (854 pages, 7765630 bytes).
```

`master.pdf` was copied to `~/Downloads/master.pdf`; both files
are 7765630 bytes.  The targeted log scans matched only the final output lines:
no undefined citations/references, LaTeX errors, package errors, or rerun
requests were found.
