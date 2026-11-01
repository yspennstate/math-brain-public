# T357: Calibration along gradient descent in Gaussian tanh random-feature classifiers

Yitzchak Shmalo, 31 October 2026

- [Read the paper](T357_Calibration_Along_Gradient_Descent.pdf).
- [Editable Markdown](T357_Calibration_Along_Gradient_Descent.md) and [generated LaTeX](T357_Calibration_Along_Gradient_Descent.tex).
- [Public Math Brain](https://github.com/yspennstate/math-brain-public) and [release index](../README.md).

This completes the catalog's explicitly permitted Gaussian tanh random-feature regime, with the paper's exact ratio and step-size conditions. The six detailed proof appendices include the later strongly overparameterized extension as Appendix F. All-time claims apply in the stated regimes, and the strict signed-overconfidence statement is an average statement at its specified scale.

Build the supplied LaTeX with `latexmk -xelatex -interaction=nonstopmode -halt-on-error T357_Calibration_Along_Gradient_Descent.tex`. To regenerate LaTeX from the Markdown source, Pandoc is optional:

```sh
pandoc T357_Calibration_Along_Gradient_Descent.md -f markdown+tex_math_single_backslash -s --include-in-header=header.tex --pdf-engine=xelatex -o T357_Calibration_Along_Gradient_Descent.tex
```
