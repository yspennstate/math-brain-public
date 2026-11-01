# QFORM B03 — fractional pair-collision and dyadic half-Riesz criteria

Run: `20260922T155848Z-fleet03-B03-QFORM-r15`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Initial control head observed: `7f9a0b35e1d4fe278d1291f8bc0a9bb2f53ab6d0`; pre-publication control head observed: `521cf8717db5349bf94ddcf200e4d91f0a742e7d`  
Assignment: `Decoupled time integral`  
Execution status: `WITHOUT_VERIFIED_BRAIN`  
Outcome: `PROVED_SUPPORTING_THEOREM + SHARP ENDPOINT OBSTRUCTION / FULL_TARGET_OPEN`.

## 1. Exact target and corrections retained

The owner target remains: for every dimension, independent real original-coordinate variables with densities at most one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample. Continuity is a separate desired conclusion.

This report never rotates the random vector and never asserts that the sum and difference of one independent-copy coordinate pair are independent. It does not use the refuted law-uniform pointwise quadratic-phase decay, the refuted conditional cap after `U=X+X', V=X-X'`, a fixed local cross-minor extraction, or absolute Fourier `L^1` as a necessary condition.

## 2. Physical pivot and the exact square-smoothing inequality

Fix an original physical coordinate `Z=X_0` with `d=A_00 != 0`, and write the remaining original coordinates as `W`. Completing the square gives

    Q = d (Z+h(W))^2 + R(W),

where `Z` is independent of `W`, its density is at most one, and no independence is assumed between `h(W)` and `R(W)`.

For every fixed `W=w`, the map `z -> d(z+h(w))^2+R(w)` has at most two inverse branches. Since the density of `Z` is at most one, its conditional pushforward density is bounded by

    |d|^(-1/2) |y-R(w)|^(-1/2)

(on the appropriate one-sided set; dropping that indicator only enlarges the bound). Averaging over `W` gives the basic transducer

    p_Q(y) <= |d|^(-1/2) E |y-R|^(-1/2).              (2.1)

This is valid with arbitrary dependence between the random shift `h` and the residual `R`.

## 3. Independent-copy identity with the pair dependence kept intact

Let

    eta(t)=E exp(i t R),

and let `R'` be an independent copy. Then

    psi(t)=E exp(i t(R-R'))=|eta(t)|^2 >= 0.          (3.1)

When `R(W)=W^T S W` and `W'` is an independent copy, put coordinatewise

    U_j=W_j+W'_j,   V_j=W_j-W'_j.

Then exactly

    R(W)-R(W') = U^T S V.                              (3.2)

For each original coordinate pair the joint density is

    g_j(u,v)=1/2 f_j((u+v)/2) f_j((u-v)/2).           (3.3)

The pairs `(U_j,V_j)` are independent across `j`, but `U_j` and `V_j` inside one pair generally are not independent. Hence

    psi(t)=int exp(i t u^T S v) prod_j g_j(u_j,v_j) du dv,   (3.4)

and every estimate below treats this as the exact pair law. No conditional density cap for `U_j|V_j` or `V_j|U_j` is used.

## 4. New fractional pair-collision criterion

### Theorem 4.1 (`QFORM-FRACTIONAL-PAIRCOLLISION-v1`)

Assume the physical-pivot representation (2.1). Fix `alpha` with

    1/2 <= alpha < 1,

and define the fractional independent-copy collision integral

    S_alpha = int_R psi(t)^alpha dt
            = int_R |eta(t)|^(2 alpha) dt.             (4.1)

If `S_alpha<infinity`, then `Q` has an essentially bounded density and

    ||p_Q||_infinity
      <= [2/sqrt(pi(1-alpha))] |d|^(-1/2) S_alpha^(1/2).     (4.2)

No continuity claim is made in this theorem.

### Proof

Put `r=2 alpha`, so `1<=r<2`, and `p=r/(r-1)` (with `p=infinity` when `r=1`). From `eta in L^r`, the converse Hausdorff--Young statement for a finite measure gives a density `g` of `R` with

    ||g||_p <= (2 pi)^(-1/r) ||eta||_r.                (4.3)

For completeness, this can be justified by Gaussian mollification: the mollified residual measures have Fourier transforms `eta(t)e^{-eps t^2}`, Hausdorff--Young gives a uniform `L^p` bound, and weak compactness (weak-* at `p=infinity`) identifies the limiting measure with an `L^p` density.

For any `a>0`, split the half-Riesz potential at distance `a`. Holder on the near part and probability mass on the far part give

    int |y-s|^(-1/2) g(s) ds
      <= K_r ||g||_p a^(1/r-1/2) + a^(-1/2),          (4.4)

where

    K_r = [2/(1-r/2)]^(1/r).                           (4.5)

Choose

    a=(K_r ||g||_p)^(-r).

The two terms in (4.4) are then equal, so

    sup_y int |y-s|^(-1/2)g(s)ds
      <= 2 (K_r ||g||_p)^(r/2).                        (4.6)

Using (4.3),

    K_r^(r/2) (2pi)^(-1/2)
      = [2/(1-r/2)]^(1/2) (2pi)^(-1/2),

and since `r/2=alpha`, (4.6) becomes

    sup_y E|y-R|^(-1/2)
      <= [2/sqrt(pi(1-alpha))] S_alpha^(1/2).          (4.7)

Combining with (2.1) proves (4.2).

### Useful special case

At `alpha=3/4`,

    ||p_Q||_infinity
      <= (4/sqrt(pi)) |d|^(-1/2)
         [int_R psi(t)^(3/4) dt]^(1/2).                (4.8)

Equivalently, if the residual density satisfies `g in L^3`, direct use of (4.4) with `p=3` gives

    ||p_Q||_infinity
      <= 4 sqrt(2) |d|^(-1/2) ||g||_3^(3/4).          (4.9)

Thus a finite three-copy residual collision density (`int g^3`) is enough after one physical square pivot. This replaces the previous all-order collision requirement on this branch by a finite-order criterion.

## 5. A dyadic decoupled-time criterion using only pair-collision energies

The Fourier transform of `|x|^(-1/2)` under the convention used here is

    sqrt(2 pi) |t|^(-1/2).

After standard Gaussian regularization and monotone/weak limiting, (2.1) therefore gives the sufficient estimate

    ||p_Q||_infinity
      <= |d|^(-1/2) / sqrt(2 pi)
         int_R |t|^(-1/2) |eta(t)| dt.                (5.1)

Fix `tau>0` and define dyadic pair-collision shell energies

    E_k(tau)=int_{tau 2^k <= |t| < tau 2^(k+1)} psi(t) dt.  (5.2)

On `|t|<=tau`, use `|eta|<=1`; on each shell apply Cauchy--Schwarz before losing the independent-copy information. This yields

    ||p_Q||_infinity
      <= |d|^(-1/2) [
          2 sqrt(2/pi) sqrt(tau)
          + (1/sqrt(pi)) sum_{k>=0} E_k(tau)^(1/2)
        ].                                               (5.3)

Hence the summability condition

    sum_k E_k(tau)^(1/2) < infinity                     (5.4)

is another explicit decoupled-time route to a linear small-ball estimate. It is an `ell^1` square-root shell condition, stronger than merely knowing total collision energy `sum_k E_k<infinity`; the next section shows that this distinction is real.

## 6. Decisive endpoint obstruction: total pair-collision energy alone is insufficient

This section constructs a source-valid rank-two control showing that the endpoint `alpha=1` cannot replace `alpha<1` in Theorem 4.1. It is **not** a counterexample to the full owner conjecture, because the matrix has only two large eigenvalues, precisely the known sharp indefinite obstruction.

Define a density on the positive real line by

    f_X(x)=1/log(1/x),                  0<x<e^(-2),
           1,                           2<x<2+(1-m),
           0,                           otherwise,       (6.1)

where

    m=int_0^{e^(-2)} dx/log(1/x).

Because `log(1/x)>=2` on the first interval,

    m <= e^(-2)/2 < 1,

so (6.1) is a probability density and `0<=f_X<=1`.

Let `S=X^2`. On `0<s<e^(-4)`, its density is exactly

    g_S(s)=1/[sqrt(s) log(1/s)].                        (6.2)

Indeed `f_X(sqrt(s))=2/log(1/s)` and the square-map Jacobian is `1/(2sqrt(s))`. Therefore

    int_0^{e^(-4)} g_S(s)^2 ds
      = int_0^{e^(-4)} ds/[s log(1/s)^2]
      = int_4^infinity du/u^2
      = 1/4.                                            (6.3)

The remote component `X in (2,3)` contributes a bounded compactly supported square density, hence `g_S in L^2`. Put `R=-S`. Then `R` also has an `L^2` density, so Plancherel gives

    int_R psi(t) dt = int_R |eta_R(t)|^2 dt < infinity. (6.4)

Thus the ordinary two-copy total collision energy is finite.

Now let `Z` be independent Uniform`(0,1)` and set

    Q=Z^2-X^2.                                          (6.5)

This is the diagonal matrix `diag(1,-1)`, with exactly two eigenvalues of modulus one. The density of `Z^2` is `k(u)=1/(2sqrt(u))` for `0<u<1`, and for `0<y<e^(-4)/2`, using `s in [y,e^(-4)]`,

    p_Q(y)
      = int_0^infinity k(y+s) g_S(s) ds
      >= (1/(2sqrt(2))) int_y^{e^(-4)} ds/[s log(1/s)]
      = (1/(2sqrt(2))) [log log(1/y)-log 4].           (6.6)

The right side tends to infinity as `y downarrow 0`. Hence

    ||p_Q||_infinity = infinity                        (6.7)

although the independent-copy residual collision integral (6.4) is finite.

Consequences:

1. A bound using only `int psi`, equivalently only residual `L^2`, cannot be the missing general decoupled-time theorem.
2. The exponent gap `alpha<1` in Theorem 4.1 is substantive, not an artifact of the proof.
3. The dyadic criterion (5.4) correctly asks for distribution of collision energy across scales, not only its total.
4. This reproduces the required two-opposite-sign control without invoking the false pointwise decay route.

## 7. Applying completed fleet04 mathematics to an actual inequality

The designated partner is `fleet04/B03`. A fresh scan found no completed current-QFORM handoff for that exact slot, so no partner result is fabricated.

A compatible completed fleet04 Fourier-pathway theorem **is** available: `fleet04/B01`, `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1`, canonical source

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

It proves, for a law `mu`,

    ||p_mu||_infinity = sup_{T>0,y} D_T mu(y)          (7.1)

whenever the density is bounded, where `D_T` is the signed triangular Fejer average, and for an interval `I` of length `ell` centered at `y`,

    mu(I) <= (pi ell/s_0) D_{2/ell}mu(y),
    s_0=4 sin(1/2)^2.                                  (7.2)

Apply (7.1) to the new Theorem 4.1. If `S_alpha<infinity`, then the actual signed-time estimate is

    sup_{T,y} D_T law(Q)(y)
      <= [2/sqrt(pi(1-alpha))] |d|^(-1/2) S_alpha^(1/2).   (7.3)

Substituting (7.3) into the fleet04/B01 interval inequality (7.2) gives

    P(Q in I)
      <= [2 sqrt(pi)/(s_0 sqrt(1-alpha))]
         |d|^(-1/2) S_alpha^(1/2) |I|.                 (7.4)

This is an explicit **linear** small-ball estimate obtained from the independent-copy time integral while preserving the exact sum/difference pair dependence. Of course once (4.2) is known, the sharper direct bound `P(Q in I)<=||p_Q||_infinity |I|` also holds; (7.4) is recorded because it directly instantiates the compatible fleet04 signed-time interface.

## 8. Relation to existing same-team results

The current fleet03/B01 Schur-cross-volume theorem supplies a branchwise pointwise residual estimate `|eta_R(t)|<=min(1,K/|t|)` after an admissible physical pivot. Such an estimate implies `S_alpha<infinity` for every `alpha>1/2`; therefore Theorem 4.1 is compatible with that completed branch. The new content here is the general pair-collision criterion, the purely dyadic pair-energy criterion, and the exact endpoint obstruction showing why total `L^2` collision information alone cannot close the assignment.

The current fleet01/B03 packet-gluing theorem gives another finite-collision route when two conditionally independent physical packets exist. Theorem 4.1 differs in allowing an arbitrary correlated square shift `h(W)` and residual `R(W)` and requiring only the fractional collision integral of the residual after one original-coordinate pivot.

## 9. What remains unpaid for the full three-eigenvalue theorem

The full QFORM conjecture remains OPEN. The first target-level missing implication is now precise:

> From only `#{j: |lambda_j(A)|>=1}>=3`, force a product-preserving branch in original coordinates that either already falls under a completed ridge/bank/cross theorem, or produces a physical pivot with a dimension-free bound on `S_alpha` for some fixed `alpha<1` (equivalently, a dimension-free dyadic bound of the form (5.4)).

The known singleton-plus-two-banks and local-cross-rank-three falsifier families show that this cannot be reduced to one uniformly good fixed minor or one rank-three cross cut. The endpoint construction in Section 6 additionally shows that merely proving finite residual `L^2` after a pivot is not enough.

Continuity is **not proved** by Theorem 4.1 or the dyadic criterion. Essential boundedness is proved on the stated branches; continuity needs an additional regularity argument such as local-uniform convergence of the signed Fejer averages.

## 10. Verification and scope

A finite arithmetic checker in `check.py` validates the displayed constants and the exact endpoint integral identities; its saved output is `check.txt` and ends `QFORM_PAIRCOLLISION_BESOV_CHECK_PASS`. These finite checks are diagnostic only; the analytic proof is Sections 2--7.

Changed-file scope is only this run's mathematical report/check files plus its own run/checkin/handoff/memory/receipt/finish records. No credentials, scheduler IDs, unrelated private data, machine paths, signed URLs, email, Drive material, public release, paid API/model action, or cross-account native action are included.
