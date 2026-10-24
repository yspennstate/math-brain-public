# Phi-mixing implies interlaced rho-mixing for Markov chains

Yitzchak Shmalo — Einstein Institute of Mathematics, The Hebrew University of Jerusalem.
Manuscript dated 18 September 2026. Compiled length: 11 pages.

## Build and supplementary checks

Compile main.tex twice with pdfLaTeX, or upload main.tex to Overleaf. All references are embedded in the TeX file. No external bibliography or figures are required.

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python check.py > checks.json
```

The optional checker needs Python 3.10+ and NumPy. The source ZIP delivered to the author includes checks.json from a successful run on 18 September 2026. Exact rational checks cover the six-state identities. Floating-point diagnostics cover 200 random finite channels, path norms for 2–30 blocks and the binary-chain covariance formulas. These checks are supplementary and do not prove the general theorem.

## Scope and source provenance

This manuscript consolidates the Bradley Question 5 research in the parent GitHub package: main.tex, sdpi_sharpening_2026-09-17.tex, arcsine_tensorization_and_binary_sharpness_2026-09-17.tex, square_root_sharpness_family_2026-09-18.tex and version_safe_prefix_interface_2026-09-18.tex. The rewrite includes a self-contained finite-channel contraction proof and a fixed countable-state reset-chain example proving sharpness of the exponential-rate loss.

The main statement is the implication phi-mixing => rho-star-mixing for standard-Borel Markov chains, including time-inhomogeneous nonstationary chains, with rho-star(n) <= min(1, 2 sqrt(2 phi(n))) and a stronger arcsine bound. The optimal universal leading constant is not claimed.

The proof uses existing tensorization theorems of Peyre, whose exact minimal-prefix conditional hypotheses are stated and verified. Bradley's question and those tensorization inputs were checked against the primary sources. No assertion of an exhaustive publication-priority search is made.

The repository contains earlier distinct-track R01 and P26 audit passes for the source-level implication. These are internal project audit records, not independent human peer review. They must not be represented as two new end-to-end audits of this entire expanded manuscript or its new reset-chain section. This package is a preprint for the author's review.

## Repository

main.tex was created at commit ce7525469761be756f5aef8b44eda8d6a321ee59, blob 5ba0a05b9e8751ca0db06af9439238b2aa9b78ba. Its SHA-256 is 15bf2ea2534ec0dc708b4ee6b972e06b32e7867529209d59418a1341c16e2c43. The delivered PDF and source ZIP use that exact TeX source. check.py has Git blob SHA 8e2a1c919e2ef0c3e478516ef96e90ae6a7f83bd.

This new Bradley manuscript is not asserted to be posted on ResearchGate. For the owner's previously posted papers, see [the ResearchGate full-text catalog](../../../../publications/researchgate/README.md).
