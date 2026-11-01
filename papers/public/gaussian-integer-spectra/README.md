# Gaussian-integer spectra of random sign matrices

Yitzchak Shmalo, 13 October 2026

[Paper (PDF)](paper.pdf) · [LaTeX source](main.tex)

Paper on the probability that every eigenvalue of an $n\times n$ matrix with independent, uniformly random $\pm1$ entries is a Gaussian integer. Vu conjectured that this probability is $2^{-(1+o(1))n^2}$ (Conjecture 9.5 in *Recent progress in combinatorial random matrix theory*).

Repository: https://github.com/yspennstate/gaussian-integer-spectra

## Main result

For every $n\geq1$, the paper constructs a family $\mathcal F_n$ of sign matrices whose eigenvalues lie in $\mathbb Z[i]$, with

$$
|\mathcal F_n|=2^{\lceil n^2/2\rceil}3^{\lfloor n/2\rfloor}.
$$

Consequently,

$$
\Pr\bigl(\operatorname{Spec}(M_n)\subseteq\mathbb Z[i]\bigr)
\geq3^{\lfloor n/2\rfloor}2^{-\lfloor n^2/2\rfloor}.
$$

The bound contradicts Conjecture 9.5. A matching upper bound remains open. The matrices have independent sign entries in the probability model; the result does not settle the adjacent conjecture for symmetric sign matrices.

The manuscript also counts the ordinary-integer subfamily: it comprises two thirds of the constructed family in even dimensions and the entire family in odd dimensions.

## Files

| File | Contents |
| --- | --- |
| `main.tex` | Complete LaTeX source, using the AMS article class |
| `paper.pdf` | Compiled seven-page manuscript |
| `verify_construction.py` | Self-contained Python exact-arithmetic verification |
| `verification_results.json` | Executed verification results, including the script hash |
| `SHA256SUMS.txt` | SHA-256 checksums of the package contents |

## Build

A standard TeX Live installation with the AMS classes, Latin Modern, microtype, mathtools, enumitem, geometry, booktabs, and hyperref is sufficient.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build produces `main.pdf`; `paper.pdf` is the supplied compiled copy.

## Reproduce the finite checks

The verification uses only the Python standard library.

```sh
python3 verify_construction.py --output verification_results.json
```

The script enumerates every matrix in the constructed families for dimensions 1 through 4. It checks that the matrices are distinct, computes their characteristic polynomials directly by the Leibniz formula, and compares them with the factors prescribed by the proof. Integer pairs represent Gaussian integers; no floating-point eigenvalue computation is used.

| Dimension | Constructed matrices | Ordinary-integer spectra | Exact polynomial comparisons |
| --- | ---: | ---: | ---: |
| 1 | 2 | 2 | 2 |
| 2 | 12 | 8 | 12 |
| 3 | 96 | 96 | 96 |
| 4 | 2304 | 1536 | 2304 |
| Total | 2414 | 1642 | 2414 |

All 2,414 comparisons agree. The manuscript gives the proof for arbitrary dimension.

## References

- Van H. Vu, *Recent progress in combinatorial random matrix theory*, Probability Surveys 18 (2021), 179–200, Conjecture 9.5. [DOI](https://doi.org/10.1214/20-PS346), [arXiv](https://arxiv.org/abs/2005.02797).
- Sean Eberhard, *The characteristic polynomial of a random matrix*, Combinatorica 42 (2022), 491–527. [DOI](https://doi.org/10.1007/s00493-020-4657-0), [arXiv](https://arxiv.org/abs/2008.01223).
