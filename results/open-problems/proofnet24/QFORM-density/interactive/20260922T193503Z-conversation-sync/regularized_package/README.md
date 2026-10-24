# Quadratic-form research: regularized determinant proof and checks

This bundle contains a complete supporting analytic argument. It is **not a proof of the unrestricted three-large-eigenvalue conjecture**. Independent end-to-end reviews of this new argument were requested from two existing scheduled workers.

Start with `REPORT.md`. Its Section 7 proves a uniform density bound below 27 when the whole range of the quadratic matrix has maximum coordinate leverage at most 1/32. This extra hypothesis is explicit and is not automatic. All additional nonzero eigenvalues may be arbitrarily small and of either sign. Earlier sections give more general cross-block characteristic-function bounds.

The full proof is committed in the private research archive at:

- Repository: `yspennstate/math-open-problems`
- Report commit: `a302aab3477c64757b511e80d3907f982e04873a`
- Report path: `proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`
- Check sources/results are present by commit `93e0c195c0755797fab94e19763f8df4175ecbe3`.

Run the finite sanity checks with Python 3.10+ and numpy, scipy, sympy installed:

```sh
python check_algebra.py
python paving_checks.py
```

The tests exercise algebra and listed finite examples only. They do not prove the universal analytic inequalities, establish the MSS partition theorem, or certify the unrestricted conjecture. `REPORT.md` states and cites the classical inputs and gives the complete argument for its actual scope.

The earlier separable-phase theorem has received one passing scoped review from account02/B08. That review is not a review of the new determinant argument.
