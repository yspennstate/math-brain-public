# Law-determined norm inequalities do not imply complete mixability

Paper: [`paper/main.pdf`](paper/main.pdf) (source `paper/main.tex`).

Wang (Probab. Surv. 12, 2015, Theorem 5) showed that an n-completely mixable law satisfies a family of inequalities
between law-determined norms of the positive and negative parts of X - t and X - s, s = (n mu - t)/(n - 1), and asked
in Open Problem 4 when these inequalities are sufficient. The paper shows that for bounded laws the whole family is
equivalent to the convex order X - mu <=_cx -(n - 1)(X - mu), and gives laws that satisfy it and are not n-completely
mixable: for n = 3 the analytic density 1/10 + (27/10)(2x - 1)^2 on [0, 1], densities bounded away from zero for
n = 3 and 4, and C-infinity densities for n = 3 and 4 (the n = 4 ones not symmetric). A Bernoulli(p) law satisfies the
inequalities exactly when 1/n <= p <= 1 - 1/n.

## Contents

| Path | What it is |
|---|---|
| `code/exact_checks.py` | exact rational checks of the support gaps, the outside masses, the second-moment bounds and the convex-order certificate for H_4 (writes `data/exact_certificates.json`, `data/exact_checks.log`) |
| `code/independent_check.py` | a second program, written separately, that recomputes every certificate in the paper (writes `data/independent_check_results.json`) |
| `code/experiments.py` | discretized linear programs and rearrangement-algorithm runs used while looking for the examples (writes `data/lp_results.*`, `data/ra_results.*`) |
| `code/controls.py` | positive and negative controls for the numerical search (writes `data/controls.*`) |
| `data/environment.json` | versions and seed of the recorded run |

The recorded outputs were produced on macOS with Python 3.13, NumPy 2.2, SciPy 1.15 and SymPy 1.14. The exact checks
need only SymPy and take a few seconds:

```
python code/exact_checks.py
python code/independent_check.py
```

Run from the repository root. The numerical experiments are not needed for any proof in the paper.

## License

Text and figures CC BY 4.0; code MIT.

The paper is part of the Math Brain project: https://github.com/yspennstate/math-brain-public
