# Substantive checkpoint — fixed-tent exact sharp normal form

Status: proved supporting reduction; full QFORM remains OPEN.

Let `s(A)=s_3(A)` and `Q=X^TAX`. Define the triangular probability kernel

`tau(u)=(1-|u|)_+`, so `tau>=0`, `int tau=1`, `||tau||_infinity=1`, and `Lip(tau)=1`.

For a probability law `mu` on R define

`D_infinity(mu)=inf{D: mu(E)<=D |E| for every Borel E}`,

allowing `+infinity`. This equals the essential `L^infinity` norm of the density when finite.

Define the two sharp target constants

`C_dens = sup_target s(A) D_infinity(mu_Q)`

and

`C_tent = sup_target sup_y s(A) E tau(Q-y)`.

## Exact equality

`C_tent <= C_dens` because `mu<=D dx` implies `tau*mu<=D int tau=D`.

Conversely assume `C_tent<infinity`, fix one target instance and put `s=s(A)>=1`. For every `0<r<=s`, the scaled matrix `A/r` is still a target matrix, with `s(A/r)=s/r` and output `Q/r`. Hence for every `t`,

`(s/r) E tau((Q-t)/r) <= C_tent`.

With `tau_r(u)=r^(-1) tau(u/r)`, this is

`(tau_r*mu_Q)(t) <= C_tent/s`.

For every nonnegative `phi in C_c(R)`, the approximate-identity property gives

`int phi dmu_Q = lim_(r->0) int phi(t) (tau_r*mu_Q)(t) dt <= (C_tent/s) int phi dt`.

Thus `mu_Q <= (C_tent/s) dx`, so `s D_infinity(mu_Q)<=C_tent`. Taking the target supremum proves

`C_dens = C_tent` (as extended real numbers).

This proves the central universal density theorem is *exactly equivalent* to a universal bound on one fixed positive, compactly supported, 1-Lipschitz test kernel. Raw density continuity is not used.

## Weak-law stability at the fixed scale

With the bounded-Lipschitz metric

`d_BL(mu,nu)=sup{|int f d(mu-nu)|: ||f||_infinity<=1, Lip(f)<=1}`,

every translate `tau(. - y)` is an admissible test. Therefore

`sup_y |(tau*mu)(y)-(tau*nu)(y)| <= d_BL(mu,nu)`.

Hence weak convergence of probability laws on R implies uniform convergence of the fixed-tent profiles. This is exactly the stability unavailable for normalized intervals whose widths shrink simultaneously with the approximating source.

## Application of completed fleet02/B15 result

Source applied: `yspennstate/math-open-problems@46c33d97490f78f8c3de0435f63d573958d81180`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260923T130525Z-fleet02-B15-qform-auto11/REPORT.md`.

For an invertible indefinite original-coordinate physical 3x3 block `B`, let `kappa=sigma_min(B)` and `G_B` be its majority/one-sheet event after conditioning on all outside original coordinates and completing the square. The partner proves the majority output submeasure satisfies

`mu_B^+(I) <= C_B |I|`, with `C_B <= pi sqrt(2)/kappa`,

uniformly in the outside affine translation. Thus directly for the fixed tent,

`E[tau(Q-y) 1_{G_B}] <= C_B <= pi sqrt(2)/kappa`,

and therefore

`s(A) E tau(Q-y) <= pi sqrt(2) s(A)/kappa + s(A) E[tau(Q-y) 1_{G_B^c}]`.

If `kappa>=c s(A)`, the entire majority contribution costs at most `pi sqrt(2)/c`; only the product-sensitive minority/two-sheet tent term remains. This uses original-coordinate conditioning only and makes no rotated-independence or projection-only assumption.
