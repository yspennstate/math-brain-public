# Regression checks — punctured cross-star router

These computations are regression evidence only. The proof in `REPORT.md` is analytic.

Exact constants evaluated in the run:

- `sqrt(47/48) = 0.9895285072531598`
- `g = 1/2-1/(4 sqrt(2)) = 0.32322330470336313`
- `s0 = g sqrt(47/48)-1/4096 = 0.31959453358755213`
- `6^(4/3)(64/s0^2)^(1/3) = 93.29580081768943`
- `sqrt((1/64)^2+(1/4096)^2) = 0.015626907232231698`
- `1/(4096*512) = 4.76837158203125e-07`

## Seeded exterior-algebra regression

Seed: `5108`.

For dimensions `p=2,...,7`, `q=3,...,8`, 40 Gaussian test matrices per size, 1,440 instances total, checked

`E3([z;D]) >= sigma1(D)^2 sigma2(D)^2 dist(z,R2(D))^2`.

Observed:

- tests: `1440`
- maximum absolute `rhs-lhs`: `1.8189894035458565e-12` (floating roundoff at large scale)
- minimum observed `lhs/rhs` among nontrivial rhs: `0.9999999999999549`

No material numerical violation occurred.

## Diffuse-frame cut regression

For normalized Hadamard two-frames and 5,000 seeded Bernoulli cuts per dimension:

- `n=32`: `mu=0.062499999999999986`; best Frobenius deviation `7.852952138307299e-17`; analytic guarantee `sqrt(mu/2)=0.17677669529663687`.
- `n=64`: `mu=0.03125`; best deviation `0.0`; analytic guarantee `0.125`.
- `n=128`: `mu=0.015624999999999997`; best deviation `7.850617931859004e-17`; analytic guarantee `0.08838834764831843`.

These explicit frames illustrate the deterministic cut produced by the expectation proof; the theorem does not depend on the random search.

`QFORM_B08_PUNCTURED_CROSSSTAR_CHECK_PASS`
