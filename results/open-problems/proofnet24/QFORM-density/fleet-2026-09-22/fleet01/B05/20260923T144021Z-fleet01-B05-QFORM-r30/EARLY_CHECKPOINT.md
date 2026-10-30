# B05 r30 — early substantive checkpoint

Programme `QFORM-DENSITY-3EIG-20260922`.  Full conjecture remains OPEN.  This checkpoint attacks the first current B05 implication: uniform passage from the paid heavy physical null-pivot branch to a small nonzero physical pivot, without treating a small matrix coefficient as a small random error.

## Exact near-null normal form

Let `A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`, and suppose physical row 0 has leverage `c>1/2`. Rotate only the deterministic active basis so `r_0=sqrt(c)e_1`, and then rotate the transverse plane so

```
M = [[d,b,0],[b,alpha,delta],[0,delta,gamma]].
```

Thus `A_00=c d`. Put `rho=1-c`. Parseval gives residual orthogonal coefficient vectors `u,v,w` with `||u||^2=rho`, `||v||=||w||=1`. For `rho>0`, write `xi=u/sqrt(rho)`, `T=xi.X`, `V=v.X`, `W=w.X`. Then

```
Q = d(sqrt(c)X0+sqrt(rho)T)^2
    +2b(sqrt(c)X0+sqrt(rho)T)V
    +alpha V^2+2delta V W+gamma W^2.
```

The hub couples to the residual linear form `d sqrt(rho) T+bV`. Set

```
r = sqrt(b^2+d^2 rho),
S = (d sqrt(rho) T+bV)/r,
P = (bT-d sqrt(rho)V)/r.
```

`S,P,W` are again orthonormal residual projections.  After slicing `S=l`, the quadratic Hessian on `(P,W)` is

```
H = [[ d rho(alpha d-b^2)/r^2,   -d delta sqrt(rho)/r ],
     [ -d delta sqrt(rho)/r,      gamma                  ]].
```

A direct determinant calculation gives the exact identity

```
det H = [d rho/(b^2+d^2 rho)] det M.                    (E1)
```

Indeed `det M=gamma(d alpha-b^2)-d delta^2`.  Hence every coarea route that first slices in the hub-partner direction and then pays a reciprocal power of `|det H|` necessarily loses a reciprocal power of `|d| rho`, although the exact `d=0` endpoint is already uniformly bounded by the partner theorem.  This isolates a genuine endpoint-stability debt rather than a missing local determinant estimate.

## Nullization companion and designated-partner inequality

Define

```
M0 = M-d e1 e1^T,
Q0 = X^T R M0 R^T X,
U  = <R e1,X> = sqrt(c)X0+sqrt(rho)T.
```

Then exactly

```
Q=Q0+d U^2,                                             (E2)
```

and the physical pivot of `Q0` at coordinate 0 is zero.  By the 1-Lipschitz property of singular values,

```
s_min(M0) >= s_min(M)-|d| >= 1-|d|.                   (E3)
```

In the residual-diffuse branch `v_j^2+w_j^2<=1/2`, apply fleet02/B05's completed slice-Fresnel heavy-null theorem to `M0/(1-|d|)`.  Scaling the output density back gives the actual inequality

```
||p_Q0||_(infty,ess) < 55.776/(1-|d|),                 (E4)
```

for `|d|<1`; in particular `<111.552` for `|d|<=1/2`.  Source: `yspennstate/math-open-problems@75df8a812c96735205ee8370363808fd734e2d12`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T130427Z-fleet02-B05-QFORM-auto11/REPORT.md`.

Equation (E4) is not a bound for `Q`: the perturbation `dU^2` is dependent on `Q0`, and bounded density is not stable under an arbitrary dependent perturbation.  The exact unpaid implication is therefore an endpoint-stable, product-sensitive estimate for the rank-one square addition in (E2), not a generic perturbation lemma.

## Newest-Claude input actually used

The partner endpoint proof spends the residual product bank via the proved one-dimensional Fourier estimate `int |fhat|^p <= 4pi/sqrt(p)` for `p>=2` and translation-invariant geometric Brascamp--Lieb.  I checked that source directly at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `.../20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.  In the present reduction the same estimate remains applicable to the nullized companion because dividing `M0` by `1-|d|` changes only deterministic coefficients, not the residual product frame or its leverage condition.  Thus (E4) is a concrete current-run application of that source chain.

Next: determine whether the special correlation `U=sqrt(c)X0+sqrt(rho)T` lets one integrate the extra square jointly with the hub before paying (E1), or prove a sharp obstruction to that interface.
