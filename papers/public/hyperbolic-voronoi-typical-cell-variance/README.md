# The variance of the typical cell of a hyperbolic Poisson–Voronoi tessellation at low intensity

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (LaTeX source in `paper/main.tex`).

Let V_d(λ) be the variance of the volume of the typical cell of the Poisson–Voronoi tessellation of the hyperbolic
space H^d with intensity λ. D'Achille, Curien, Enriquez, Lyons and Ünel asked whether λV_d(λ) has a finite limit as
λ → 0, equal to the expected volume of C_d \ T_d(R_1), where C_d is the zero cell of the ideal Poisson–Voronoi
tessellation and T_d(R_1) the set coupled with it. We show that λV_d(λ) → ∞ for every d ≥ 2 and that the expected
volume of C_d \ T_d(R_1) is infinite, growing like θ_d log U in the window {|u| < U} of the upper half-space model,
with θ_2 = 8/π. The proof couples the typical cell inside the zero cell at positive intensity and passes to the limit
with Fatou's lemma. In the plane, numerical values of λV_2(λ) down to λ = 10^-5 fit (8/π) log(1/λ) − 6.84.

## Files

All scripts are in `code/`; each `name.py` has its output in `name_out.txt`. They need `numpy`, `scipy` and `mpmath`.

- `var.py`: the integral formula for λ²V_2(λ) of Section 6 and the hyperbolic geometry it needs, evaluated without
  cancellation.
- `var3.py`: Table 1 (λ = 100 down to 10^-5, with 12 and with 18 Gauss–Legendre nodes per piece).
  `python var3.py 100 10 1 0.1 0.01 0.001 0.0001 0.00001` (about 17 minutes).
- `geometry_check.py`: the geometry of `var.py` against the law of cosines in 60-digit arithmetic on 400 random
  triangles. `python geometry_check.py`
- `ct.py`: the closed form of I(u, v) in the plane against brute force, and the expected area of C_2 \ T_2(R_1) in the
  windows |u| < U for U = 10 to 10^8 (the remark at the end of Section 5). `python ct.py`
- `theta_check.py`: the constants M, L_d and θ_d for d = 2 to 5 against their closed forms. `python theta_check.py`
- `check_limits.py`: Monte Carlo check of the two limits of Lemma 4.1 at λ = 10^-6. `python check_limits.py`
- `mc_cell.py`: Monte Carlo of the typical cell by exact polygons in the Klein model (Table 2).
  `python mc_cell.py 0.1 20000 2` and `python mc_cell.py 0.01 20000 3`; the output of both runs is in
  `mc_cell_out.txt`.
- `mc_p.py`: Monte Carlo of p(t) at six pairs (λ, t) against the quadrature (Table 3). `python mc_p.py`

## License

MIT; see `LICENSE`.
