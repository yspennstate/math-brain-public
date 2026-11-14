# Slabs are more noise stable than balls at large Gaussian measure, for every correlation

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Among symmetric subsets of R^n of prescribed Gaussian measure, which one maximizes the probability that two
ρ-correlated standard Gaussian vectors both lie in the set? A centred ball or its complement was suggested, and Heilman
showed that this fails in the plane to second order at ρ = 0. We show that it fails for every ρ in (0,1) and every
n ≥ 2: at measure close to 1 the slab {|x_1| ≤ t} is strictly more noise stable than every cylinder B^k × R^(n-k)
with k ≥ 2 and every cylinder complement, and at measure close to 0 the complement of the slab wins. Computations in
dimensions one, two and six are consistent with cylinders and their complements being the optimal sets.

## Files

All scripts are in `code/`; each `name.py` has its output in `name_out.txt` (for `sym2d_mlx.py` the output is
`sym2d_out.txt`). They need `numpy` and `scipy`; `sym2d_mlx.py` also needs `mlx` (Apple silicon).

- `cyl2d.py`: exact noise stability of the ball, the slab and their complements in R^2 on a (ρ, a) grid (Table 1 and
  the margins quoted with it). `python cyl2d.py`
- `tail_check.py`: the joint exceedances of the slab and the ball in R^2 as the measure tends to 1, against the Laplace
  prediction of Remark 3.4. `python tail_check.py`
- `slab_vs_ball.py`: the same in R^2 and R^3 down to ε = 1e-32, with the explicit bounds of Lemmas 3.1 and 3.2 printed
  beside the exact values. `python slab_vs_ball.py`
- `cylnd.py`, `cylnd_check.py`: cylinders B^k × R^(n-k) and their complements in R^6, and cross-checks against
  `cyl2d.py`, node doubling and Monte Carlo. `python cylnd.py`, `python cylnd_check.py`
- `hybrid.py`: shapes between the slab and the ball at the measure where the two tie. `python hybrid.py 0.5 400`
- `sym1d.py`: search over symmetric subsets of R. `python sym1d.py`
- `sym2d_mlx.py`: search over symmetric subsets of R^2 on a 256 × 256 grid from 7,040 random starts; every reported
  value is recomputed in double precision. It reads `exact_cyl.json`, the exact cylinder values. `python sym2d_mlx.py`

`cyl2d.py`, `tail_check.py`, `cylnd.py` and `cylnd_check.py` each run in under four minutes on a laptop.

## License

MIT; see `LICENSE`.
