---
name: p0167_symmetric_gaussian_strip_beats_ball_all_rho_2026_11_14
description: "[PROVISIONAL] P0167 (O'Donnell/Heilman symmetric Gaussian noise stability, ball conjecture): false in the plane for every rho, not just small rho; strip beats ball as a->1 (Laplace, ratio ~ t^{(1-rho)/(1+rho)}); numerics say cylinders are optimal in 2D and interval/complement in 1D for all rho"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T14:00:44+02:00
  status: provisional
  evidence: ""
---

P0167 (14 Nov 2026, an agent). Status PARTIAL, provisional. Files: 12_cognitive_architecture/math/trio_1011/op/P0167 (NOTE.md, STATUS.md and scripts).
- Exact cylinder values (cyl2d.py), n=2, 13 values of rho x 14 measures. The strip wins for a>=0.9 at every rho, its complement for a<=0.1, and the ball or its complement in between. So the ball conjecture fails at every rho tested.
- Laplace asymptotic as a->1 for all rho: J_strip/J_ball ~ 2(r^2/t^2) exp((r^2-t^2)/(1+rho)) / (r sqrt(2pi/rho)). It grows like t^{(1-rho)/(1+rho)}; quadrature agrees to within 1 pct at eps 1e-64. Error terms are not written yet.
- 2D search on the worker machine 1 GPU (sym2d_mlx.py, MLX Frank-Wolfe with float64 polish): 55 cases, 7,040 starts, nothing above the exact best cylinder (max -8.9e-8).
- At the strip/ball tie measure (rho 0.2/0.5/0.8): ellipses, truncated strips and stadiums all lose. They form a valley between the two winners (hybrid.py).
- 1D (sym1d.py): 143 cases, 42,900 starts, every optimum is the interval or its complement (one switch).
Scar from this work: a sampled 0/1 indicator makes mass a step function, so brentq lands on a step and the shapes being compared have unequal measure (errors of 0.3 pct). Use a smoothed boundary and assert the mass.
Open: a proof for 1D beyond tiny rho, and a proof that cylinders are optimal in 2D.

- Added later on 14 Nov: in R^n the winning cylinder B^k x R^{n-k} steps from k=n near a=1/2 down to k=1 as a->1, and the mirror image with complements below 1/2 (cylnd.py). In R^6 an intermediate k wins in 26 of 104 cases, by up to 3.8e-3. Checked to 1e-14 and by Monte Carlo. This is the noise-stability analogue of Barthe's symmetric isoperimetric question; see Heilman arXiv 1705.06643 and 2204.12003 (perimeter minimizers are rS^k x R^{n-k-1}).
