# Ballisticity for positive excited random walks without bounded cookie stacks

Yitzchak Shmalo — 13 October 2026

[Paper (PDF)](paper.pdf) · [LaTeX source](main.tex)

This paper proves the zero-speed/positive-speed criterion at expected total
drift two for a one-dimensional nearest-neighbour excited random walk in an
IID positive cookie environment satisfying weak ellipticity. It permits
arbitrary dependence within a stack and infinitely many non-neutral cookies
at a site. The critical case is proved by a branching-chain comparison and
a direct downcrossing argument.

Repository: https://github.com/yspennstate/positive-cookie-ballisticity

## Files

- `paper.pdf`: the manuscript.
- `main.tex`: the complete LaTeX source, including the bibliography.
- `SHA256SUMS.txt`: checksums of the published files.

## Build

With a standard TeX Live installation and latexmk:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

This produces `main.pdf`; `paper.pdf` is the supplied compiled copy.
The source uses the AMS article class, Latin Modern, microtype, amsmath,
amssymb, amsthm, mathtools, geometry, and hyperref. No external bibliography
file, figures, datasets, or custom style files are required.

The manuscript contains the author's funding statement and competing-interest and AI-use declarations.
