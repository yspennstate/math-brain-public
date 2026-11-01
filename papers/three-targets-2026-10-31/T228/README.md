# T228: Exact power tails and moment growth for a contractive nonlinear SGD model

Yitzchak Shmalo, 31 October 2026

- [Read the paper](T228_Nonlinear_SGD_Power_Tails.pdf).
- [Editable LaTeX](T228_Nonlinear_SGD_Power_Tails.tex).
- [Exact arithmetic checker](verify_arithmetic.py) and [result](verification_result.json).
- [Public Math Brain](https://github.com/yspennstate/math-brain-public) and [release index](../README.md).

The concrete nonlinear-model target is solved in the paper's stated parameter rectangle. The activation is the identity plus a bounded smooth perturbation, not a bounded activation. The stationary law has a strictly positive exact power tail with exponent between one and two. The moment theorem includes every fixed teacher in the stated interval. Established renewal theory and prior moment results retain their attribution.

Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error T228_Nonlinear_SGD_Power_Tails.tex`. Reproduce the rational arithmetic with `python3 verify_arithmetic.py`. The arithmetic check is not a substitute for the analytic proof or external review.
