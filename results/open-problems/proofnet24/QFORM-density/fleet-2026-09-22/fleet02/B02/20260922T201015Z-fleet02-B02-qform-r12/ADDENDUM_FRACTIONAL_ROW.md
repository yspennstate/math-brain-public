# Addendum — subcritical row trace and pair-plus-row closure

Run: `20260922T201015Z-fleet02-B02-qform-r12`.
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**.

This addendum records a second consequence of `QFORM-PHYSICAL-ROW-LP-SHEAR-v1` and consumes two fresh correction events observed after the main report was archived.

## 1. Fresh corrections consumed

1. `QFORM-SQUARE-COLLISION-ALPHA1-ENDPOINT-FALSE-v1`, brain commit `b687954d8696656f27ce85d96b376c346157b614`: one square collision does not supply the endpoint `alpha=1` Riesz energy. The argument below stays strictly subcritical at `alpha=1/4` and does not use that endpoint.
2. `QFORM-CROSS-CYCLE-ARBITRARY-SELF-CURVATURE-FALSE-v1`, brain commit `ec721c7cff0759e9daf10b251bd26c05bc2cd3c8`: three bilinear cross strengths alone do not control arbitrary self-curvature. The argument below requires an actual invertible indefinite physical principal pair and then treats the entire Schur residual through a dependence-safe fractional trace. It does not infer bounded density from a cross cycle alone.

Neither correction invalidates the main report.

## 2. A stable quarter-Riesz trace from one physical row

Let `T=aX^2+2XU+R(W)` be as in Theorem 3.1 of the main report, with `X` independent of `W`, `f_X<=1`, and the marginal density of `U` bounded by `M`. The theorem gives

`||p_T||_(3/2) <= L:=2 M^(1/3)`.                                         (2.1)

For any target level `s` and radius `rho>0`, Hölder with exponents `3/2` and `3` gives

`int_{|y-s|<=rho} |y-s|^(-1/4)p_T(y)dy
 <= L [int_{-rho}^rho |u|^(-3/4)du]^(1/3)
 =2L rho^(1/12).`                                                        (2.2)

Outside that interval the contribution is at most `rho^(-1/4)`. Therefore

`H_(1/4)(T):=sup_s E|T-s|^(-1/4)
 <= 2L rho^(1/12)+rho^(-1/4).`                                          (2.3)

Writing `z=rho^(1/12)`, the right side is `2Lz+z^(-3)`, minimized at

`z=(3/(2L))^(1/4)`.                                                       (2.4)

At this value,

`H_(1/4)(T)
 <=4 (2/3)^(3/4)L^(3/4)
 =4 (4/3)^(3/4) M^(1/4).`                                               (2.5)

Thus:

### Lemma 2.1 — `QFORM-PHYSICAL-ROW-QUARTER-RIESZ-v1`

`boxed:
 H_(1/4)(aX^2+2XU+R)
 <=4(4/3)^(3/4) M^(1/4),
`

uniformly in the scalar self-curvature `a` and arbitrary dependence between `U` and `R`.

For a physical row of a product-input quadratic form with off-diagonal coefficient norm `sigma>0`, Livshyts--Paouris--Pivovarov gives `M<=sqrt(2)/sigma`, hence

`boxed:
 H_(1/4)(T)
 <=4(4/3)^(3/4)2^(1/8)sigma^(-1/4).
`                                                                           (2.6)

## 3. New bounded-density branch: indefinite pair plus any energetic residual row

Use the source-pinned fleet02/B02 theorem `QFORM-PAIR-FRACTIONAL-TRACE-TRANSDUCER-v1` from

`yspennstate/math-open-problems@853a4e86c7ff9789891c473905eeb57b13f615ed`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260922T190827Z-fleet02-B02-40617e89/REPORT.md`.

Let the full matrix contain an invertible indefinite ORIGINAL-coordinate principal pair `B`. Put

`D=|det B|`, `kappa=sigma_min(B)`,

and let `S` be its physical Schur complement on the remaining original coordinates. The cited transducer at `alpha=1/4` gives

`||p_Q||_infinity
 <= C_pair D^(-1/4) kappa^(-1/4) H_(1/4)(Z^T S Z),`                     (3.1)

where

`C_pair=4*2^(1/4)*exp(-1+1/sqrt(2)).`                                   (3.2)

Suppose one physical row `k` of `S` has off-diagonal norm

`sigma=(sum_{l!=k}S_kl^2)^(1/2)>0`.                                    (3.3)

Write the residual in that original coordinate as

`Z^T S Z=S_kk Z_k^2+2Z_k U+R`,                                         (3.4)

where `Z_k` is independent of the remaining coordinates, `U=sum_{l!=k}S_kl Z_l`, and `R` is arbitrary. Applying (2.6) in (3.1) proves:

### Theorem 3.1 — `QFORM-INDEFINITE-PAIR-RESIDUAL-ROW-v1`

`boxed:
 ||p_Q||_infinity
 <= C_* (D kappa sigma)^(-1/4),
`

where

`C_*=16*2^(3/8)*(4/3)^(3/4)*exp(-1+1/sqrt(2))
    = [4*2^(1/4)e^(-1+1/sqrt(2))]
      [4(4/3)^(3/4)2^(1/8)]
    <19.210.`                                                            (3.5)

No nonzero scalar diagonal in the Schur residual is required. Its selected row diagonal may be zero or arbitrarily small, and all other residual curvature is unrestricted.

This strictly complements the preceding B02 theorem `QFORM-INDEFINITE-PAIR-SCHUR-PIVOT-QUARTER-v1`, which paid a nonzero residual scalar pivot by `(D kappa |d|)^(-1/4)`. The new theorem instead pays any residual row with off-diagonal energy by `(D kappa sigma)^(-1/4)` and is stable at `d=0`.

## 4. Remaining implication after this addendum

Once an outer invertible indefinite physical pair is structurally available, the analytic scalar-pivot obstruction is now reduced further: either a residual diagonal is quantitatively usable (previous B02 theorem) or a residual physical row has quantitatively usable off-diagonal norm (Theorem 3.1). The unresolved issue is again aggregate selection: the bare `s_3(A)>=1` hypothesis does not force one fixed pair with dimension-free `D*kappa`, and fresh cross-cycle corrections prohibit replacing that pair by arbitrary cross strengths without controlling self-curvature.

For the partner overlap-one near-isotropic branch, the main report's `L^3_t` credit and retained `d_i` remain the correct unresolved interface. The new alpha-one collision correction specifically rules out trying to close it by a single square-collision endpoint; a successful upgrade must spend the residual grouped-bank structure jointly.
