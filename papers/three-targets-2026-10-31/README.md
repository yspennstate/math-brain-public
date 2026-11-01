# Three completed research targets: T067, T228 and T357

Yitzchak Shmalo, 31 October 2026

These three papers record **targets solved in their stated mathematical scope** in the [public Math Brain repository](https://github.com/yspennstate/math-brain-public). Each paper contains complete proofs and cites both this repository and its own public archive. The status is based on internal mathematical review and the checks described below; external peer review and exclusive publication priority have not been established.

## Papers and solved scope

| Target | Paper | Scope of the completed result |
|---|---|---|
| T067 | [A three-state posterior cone and reconstruction on finite-mean Galton-Watson trees](T067/T067_Finite_Mean_Reconstruction.pdf) | The ferromagnetic three-state reconstruction threshold on an observed iid Galton-Watson tree with arbitrary finite-mean offspring and (0<\lambda<1): reconstruction exactly when (d\lambda^2>1), including nonreconstruction at equality. The four-state conclusion is a credited consequence of an earlier cone. |
| T228 | [Exact power tails and moment growth for a contractive nonlinear SGD model](T228/T228_Nonlinear_SGD_Power_Tails.pdf) | An explicit scalar nonlinear Gaussian regression model: average contraction, a unique stationary law, a strictly positive exact power tail with exponent between one and two, and critical/supercritical moment-growth statements on the stated parameter rectangle. |
| T357 | [Calibration along gradient descent in Gaussian tanh random-feature classifiers](T357/T357_Calibration_Along_Gradient_Descent.pdf) | The catalog's permitted Gaussian random-feature regime: exact conditional calibration and population-risk limits at fixed finite training times, with all-positive-stopping-time conclusions under explicit sample-rich or strongly overparameterized conditions. |

**Download the complete [public source and verification archive](Three_Papers_Public_Source_and_Verification.zip).** Browse individual sources and supplements in [T067](T067/), [T228](T228/), and [T357](T357/).

## Interpretation and prior work

T067 addresses the three-state case of Formentin and Kulske's published general-offspring conjecture, including its critical boundary. Earlier regular/Poisson reconstruction theorems and the four-state cone retain their attribution. The arbitrary finite-mean three-state cone and extension are the contribution developed in this paper.

T228 completes a concrete-model target by applying established implicit-renewal and iterated-map theory. The critical-moment formula has earlier affine and Lipschitz-system antecedents; the manuscript now cites Buraczewski, Damek and Zienkiewicz, *On the Kesten-Goldie constant* (2016), separately from the four-author paper on perpetuity exceedance times. No general theorem for arbitrary nonlinear neural-network losses is claimed.

T357 treats ordinary output-weight gradient descent with fixed tanh features, Gaussian inputs and a logistic single-index teacher. Prior random-feature calibration and logistic overconfidence results are credited. Its all-time conclusions have stated aspect-ratio and step-size conditions; the paper does not settle calibration for every architecture, feature-learning procedure or scaling.

These are completed mathematical targets with exact hypotheses, not an assertion that three unrestricted famous conjectures have received external certification. The machine-readable [completion record](https://github.com/yspennstate/math-brain-public/blob/main/results/completed-targets/2026-10-31.json) preserves that distinction.

## Verification for this release

- **T067:** a fresh independent Python expansion checked all 80,532 coefficient positions, found zero negative coefficients, and passed 16 exact rational identity checks. Both regenerated coefficient tables are byte-identical to the delivered tables. See the [receipt](T067/computation/publication_verification_receipt.json) and [run log](T067/computation/publication_q3_run.log).
- **T228:** ten exact rational checks passed, including the contraction bound (0.99010707), its positive margin and the multiplier's second-moment bounds. See the [checker](T228/verify_arithmetic.py) and [result](T228/verification_result.json).
- **T357:** the final manuscript includes the strongly overparameterized extension as Theorem D and Appendix F. A targeted review checked its scope, the scalar overconfidence argument and the later extension. The earlier simulations are not proof premises and were not rerun for this release.

The prior four-state traversal records are retained as historical records; their full C++ traversals were not rerun for this release. None of these checks is a proof-assistant formalization or an external referee report.

## Reproduce

From this directory, build all three PDFs with:

```sh
python3 build_papers.py
```

This requires TeX Live, `latexmk`, `pdflatex` and `xelatex`. T357's generated LaTeX is included, so Pandoc is optional. To rerun the exact arithmetic:

```sh
python3 T067/computation/verify_q3_python.py
python3 T228/verify_arithmetic.py
```

See [T067's supplement](T067/SUPPLEMENT.md) for the additional inherited C++ checks. [MANIFEST.json](MANIFEST.json) gives hashes and byte lengths for the release files; [PROVENANCE.md](PROVENANCE.md) records contribution history and the changes in this public edition. Original project contributions use the repository's [MIT license](https://github.com/yspennstate/math-brain-public/blob/main/LICENSE); the imported four-state material retains its [Apache 2.0 license](T067/computation/published_q4/LICENSE) and [attribution](T067/THIRD_PARTY_NOTICES.md).
