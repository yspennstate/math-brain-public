# Extreme singular values of Gaussian submatrices and the adversarial geometry of deep networks

Manuscript source and numerics for the paper connecting the singular-value theory of
coordinate-optimized Gaussian submatrices to adversarial examples in deep networks.

## Building

From `paper/`:

```
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

The bibliography is written directly in the source (`bibliography.tex`), so there is no BibTeX step.
The document is split into `sec_*.tex` (body) and `app_*.tex` (appendices), included from `main.tex`.

## Contents

- `main.tex` — preamble, abstract, introduction, and includes.
- `sec_notation.tex`, `sec_rmt.tex` — notation, the constants, and the random-matrix results.
- `sec_networks.tex` ... `sec_trained.tex` — the network theory.
- `sec_numerics.tex`, `sec_discussion.tex` — verification and discussion.
- `app_twosided.tex` — full proof of the two-sided single-layer rate `2H(alpha)/d_F`.
- `app_product.tex` — the product bracket `[2H/d_F, (k+1)H/d_F]` and the sharp value.
- `app_brackets.tex` — operator-norm brackets, the order-statistic law, the convex-hull reduction.
- `app_netlemmas.tex` — the uniform gain, gradient, and stability lemmas.

## Numerics

In `../numerics/`:

- `verify_product_rate.py` — small-N exhaustive and cascade computation of the product least-singular-value
  rate; confirms `(k+1)H(alpha)/d_F` and the depth-2/depth-1 rate ratio `1.5`.
- `verify_constants.py` — checks the deterministic constants `kappa`, `kcheck`, `alpha*`, `s*`.
- `RESULTS.md` — recorded output.

Both scripts use `numpy` (and `scipy` for the constants).
