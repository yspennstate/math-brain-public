SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-22T21:54:09Z.
attacking: aggregate-before-inversion determinant transport by turning arbitrary residual cross-block rank into additional L2 oscillatory curvature while preserving original-coordinate product structure.

# account03/B16 r18 — two-bank cross-block L2 operator theorem

Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM`; full QFORM **OPEN / NOT PROVED**. The theorem below proves a new full-matrix branch and a continuous density on that branch. It does not prove continuity or the universal density bound for all target matrices.

Execution: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was genuine and source-pinned, but no authenticated native learned-memory receiver was used.

Fresh source controls before the scientific write: `yspennstate/math-research-brain@5d3501ed69da1d0b1eea3839b3350a8f0c04c11d`, OWNER CONTROL revision `2026-09-22.15`. QFORM is still the sole target. Corrections respected include: no law-uniform pointwise quadratic van der Corput; no independence after spectral rotation; no arbitrary-joint rank-three coarea bound; no positive conditional projection-height moment bridge; no scalar residual conditional-sup bridge; no receiver-only fiber supremum.

## 1. Inputs consumed

### Projection theorem used

I use the completed weighted product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` from

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `T:R^m->R^k` has full row rank and `X_1,...,X_m` are independent with densities at most one, normalizing `T` to an orthonormal-row map and applying that theorem gives

`||p_(TX)||_infinity <= exp(k/2) / sqrt(det(T T^T))`.                 (1.1)

This is an unconditional original-product projection cap. It is not a conditional fiber supremum. I use only this internally proved constant below.

### Grouped L2 precedent

Account01/B16 proved the zero-residual-cross-block case in

`yspennstate/math-open-problems@e4c589aa572f7d140c78a832af2d554eed97fde4:proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/20260922T211047Z-account01-B16-QFORM-r16/REPORT.md`.

The missing implication there is a cross-block residual `2 X_I^T C X_J`, which breaks ordinary convolution of the two three-dimensional spectral banks. The new theorem below treats a quantitatively transverse cross block exactly rather than perturbatively.

### Designated partner account04/B16 actually applied

Account04/B16 r3,

`yspennstate/math-open-problems@0f2d6290352a984c4e4ae0b024f8c27c7a2bb473:proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260922T191443Z-account04-B16-QFORM-r3/REPORT.md`,

proves for its diffuse-block source that every positive conditional projection-height moment is non-uniform: for `0<alpha<2`,

`E M_m^alpha = [m^(-alpha/2) Gamma(m+1) Gamma(2-alpha)/Gamma(m+1-alpha)]^2 ~ Gamma(2-alpha)^2 m^alpha`,

and for `alpha>=2` the moment is already infinite. In particular `E M_m=m`. Plugging this into the tempting receiver-only estimate

`||p_Q||_infinity <= C_alpha (E M_m^alpha)^(1/alpha)`                 (1.2)

forces a right side growing linearly in `m` for every `0<alpha<2`, and gives infinity for `alpha>=2`, although the same exact-rank-three family is uniformly bounded by completed product-preserving arguments. Thus (1.2) cannot be the desired universal bridge. The theorem below instead takes unconditional augmented projection densities **before** the nonlinear integration, so the partner obstruction is avoided at the inequality level rather than merely cited.

## 2. Full-matrix setup

Let `A` be any real symmetric `n x n` matrix having three chosen orthonormal eigenvectors collected in an `n x 3` matrix `U`, with corresponding invertible symmetric diagonal matrix

`Lambda=diag(lambda_1,lambda_2,lambda_3)`,  `|lambda_j|>=1`.

Write

`A = U Lambda U^T + E`.                                               (2.1)

Choose an arbitrary partition of the **original independent coordinates**

`[n]=I disjoint_union J`.                                             (2.2)

The residual cross block is

`C=E[I,J]`.

Let `r=rank C` and choose a thin singular-value decomposition

`C=L Sigma R^T`,                                                     (2.3)

where `L` and `R` have orthonormal columns and `Sigma=diag(sigma_1,...,sigma_r)>0`. Put

`k=3+r`,

`Y_I=U_I^T X_I`,       `u=Sigma^(1/2) L^T X_I`,
`Y_J=U_J^T X_J`,       `v=Sigma^(1/2) R^T X_J`.                       (2.4)

Define the augmented original-coordinate projection matrices

`T_I = [ U_I^T ; Sigma^(1/2) L^T ]`,
`T_J = [ U_J^T ; Sigma^(1/2) R^T ]`,                                 (2.5)

and their Gram matrices

`G_I=T_I T_I^T`,  `G_J=T_J T_J^T`.                                   (2.6)

The theorem applies whenever both `G_I` and `G_J` are positive definite. This condition says the residual cross singular directions and the selected three-dimensional spectral bank are quantitatively transverse inside each physical side. It does **not** assert such a partition always exists.

The within-side residual pieces

`H_I(X_I)=X_I^T E[I,I]X_I`,
`H_J(X_J)=X_J^T E[J,J]X_J`                                           (2.7)

may be arbitrary; all additional eigenvalues and signs of `A` are retained.

Because of (2.3), the exact full quadratic form is

`Q=(Y_I+Y_J)^T Lambda (Y_I+Y_J) + 2 u^T v + H_I(X_I)+H_J(X_J)`.       (2.8)

No spectral-coordinate independence has been asserted. The only independence used below is the genuine independence of the two disjoint original-coordinate groups `X_I` and `X_J`.

## 3. The new theorem

### Theorem — `QFORM-TWO-BANK-CROSSBLOCK-L2-v1`

Under (2.1)--(2.8), assume `G_I,G_J` are positive definite. Then `Q=X^T A X` has a bounded **continuous** density and

`||p_Q||_infinity
 <= [e k/(k-2)] |det Lambda|^(-1/k)
       [det G_I det G_J]^(-1/(2k))`.                                  (3.1)

Equivalently, with the homogeneous augmented determinant scale

`Omega := |det Lambda|^2 det G_I det G_J`,                            (3.2)

`||p_Q||_infinity <= [e k/(k-2)] Omega^(-1/(2k))`.                    (3.3)

Under a common scalar rescaling `A -> sA`, `Omega` scales as `|s|^(2k)`, so the right side of (3.3) has the required density scaling `|s|^(-1)`.

In particular, any branch with `Omega>=eta^(2k)` has the explicit estimate

`||p_Q||_infinity <= 3e/eta`,                                        (3.4)

since `k/(k-2)<=3` for every integer `k>=3`.

### Proof

Fix `t`. Push the law of `X_I` under the augmented map

`x -> (U_I^T x, Sigma^(1/2)L^T x)=(y,u)`

while weighting it by the unit-modulus phase `exp(i t H_I(x))`. Since `G_I>0`, the unweighted pushforward has a density `rho_I`. The weighted pushforward has a complex density `a_t(y,u)` with

`|a_t(y,u)|<=rho_I(y,u)` almost everywhere.                           (3.5)

Likewise the `J` group gives a complex density `b_t(z,v)` satisfying

`|b_t(z,v)|<=rho_J(z,v)`.                                             (3.6)

By (1.1),

`M_I:=||rho_I||_infinity <= exp(k/2)/sqrt(det G_I)`,
`M_J:=||rho_J||_infinity <= exp(k/2)/sqrt(det G_J)`.                  (3.7)

Because each weighted pushforward has total variation at most one,

`||a_t||_2<=M_I^(1/2)`,  `||b_t||_2<=M_J^(1/2)`.                     (3.8)

Using genuine independence of the original groups and (2.8),

`phi_Q(t)= integral a_t(y,u)b_t(z,v)
 exp{i t[(y+z)^T Lambda(y+z)+2u^T v]} dy du dz dv`.                   (3.9)

Set `w=(y,u) in R^k`, `q=(z,v) in R^k`, and

`D=diag(Lambda,I_r)`.                                                 (3.10)

The phase in (3.9) splits as the harmless local chirps

`t y^T Lambda y + t z^T Lambda z`

plus the full-rank cross phase

`2t w^T D q`.                                                        (3.11)

For a function `b(q)`, define

`(T_t b)(w)= integral exp{i t z^T Lambda z} exp{i 2t w^T D q} b(q)dq`,

and multiply the output by `exp{i t y^T Lambda y}`, which does not change its `L2` norm. With Fourier convention

`hat c(xi)=integral exp(i xi.q)c(q)dq`,

Plancherel gives

`||hat c||_2=(2pi)^(k/2)||c||_2`.                                    (3.12)

Since `T_t b(w)=hat c(2tD^T w)` up to a unit-modulus factor, change variables `xi=2tD^T w`. Because `det D=det Lambda`,

`||T_t b||_2^2
 =(2|t|)^(-k)|det Lambda|^(-1)||hat c||_2^2
 =(pi/|t|)^k |det Lambda|^(-1)||b||_2^2`.                             (3.13)

Hence, by Cauchy--Schwarz and (3.8), for every `t!=0`,

`|phi_Q(t)|
 <= pi^(k/2)|t|^(-k/2)|det Lambda|^(-1/2)(M_I M_J)^(1/2)`.            (3.14)

This is a **joint** oscillatory estimate. It does not claim any one-dimensional pointwise van der Corput estimate for the input laws; the decay comes from the nondegenerate `k x k` cross Fourier operator after product groups have been formed.

Let

`K=pi^(k/2)|det Lambda|^(-1/2)(M_I M_J)^(1/2)`,
`alpha=k/2>1`.                                                        (3.15)

Together with the trivial `|phi_Q(t)|<=1`,

`|phi_Q(t)|<=min(1,K|t|^(-alpha))`.                                  (3.16)

At the crossing point `T=K^(1/alpha)`, direct integration gives

`integral_R min(1,K|t|^(-alpha))dt
 = [2 alpha/(alpha-1)] K^(1/alpha)
 = [2k/(k-2)] K^(2/k)`.                                               (3.17)

Thus `phi_Q in L1(R)`. Fourier inversion gives a bounded continuous density and

`||p_Q||_infinity
 <= (1/(2pi)) [2k/(k-2)] K^(2/k)
 = [k/(k-2)] |det Lambda|^(-1/k)(M_I M_J)^(1/k)`.                     (3.18)

Substitute (3.7):

`(M_I M_J)^(1/k)
 <= e [det G_I det G_J]^(-1/(2k))`,                                  (3.19)

which is exactly (3.1). Equations (3.2)--(3.4) follow algebraically. `QED`

## 4. Exact geometric form of the augmented determinant

The theorem's invariant can be written directly in terms of the residual cross singular spaces. From (2.5),

`G_I = [[U_I^T U_I, U_I^T L Sigma^(1/2)],
        [Sigma^(1/2)L^T U_I, Sigma]]`.                                (4.1)

Taking the Schur complement of `Sigma`,

`det G_I
 = det Sigma * det[U_I^T(I-LL^T)U_I]`.                              (4.2)

Similarly,

`det G_J
 = det Sigma * det[U_J^T(I-RR^T)U_J]`.                           (4.3)

Therefore

`Omega
 = |det Lambda|^2 (det Sigma)^2
   det[U_I^T(I-LL^T)U_I]
   det[U_J^T(I-RR^T)U_J]`.                                           (4.4)

This is useful structurally. A large residual cross block is not automatically an obstruction: its singular values contribute positively through `(det Sigma)^2`. The branch fails only when the cross singular spaces consume too much of one selected three-dimensional spectral bank, or when the geometric mean of the cross singular values is too small. Those failure modes are precisely where the existing ridge, physical-pair, scalar-pivot, and low-rank bank mechanisms should be combined next.

## 5. Checks and reductions

1. **Zero residual cross block.** When `r=0`, `k=3`, `G_I=U_I^TU_I`, `G_J=U_J^TU_J`. Equation (3.18) becomes

   `||p_Q||_infinity <=3 |det Lambda|^(-1/3)(M_I M_J)^(1/3)`,

   exactly the two-full-bank specialization of account01/B16's grouped L2-Fresnel theorem before inserting a particular projection-density constant. With the internally proved weighted projection cap, this yields the valid constant `3e` times the determinant factor.

2. **One transverse residual cross direction.** For `r=1`, `k=4`, the analytic prefactor in (3.3) is `2e=5.4365636569...`. Thus one genuinely transverse cross direction improves the time-decay exponent from `3/2` to `2`; it does not merely perturb the rank-three Fresnel estimate.

3. **Higher transverse cross rank.** The prefactor `e k/(k-2)` decreases monotonically from `3e=8.1548454854...` at `k=3` toward `e`. The remaining quantitative issue is the augmented determinant, not growth of the analytic constant with cross rank.

4. **No receiver-only conditioning.** The proof never conditions on a spectral fiber and never takes a positive moment of its normalized density height, so account04/B16's exact divergence theorem does not enter as a hidden cost.

The local constant checker in this run folder verifies the time-integration coefficient `2k/(k-2)` exactly and the displayed numerical prefactors; it ends `STATUS=PASS`. It is only an algebra check, not an independent proof review.

## 6. What this pays and what remains

This theorem directly advances the full arbitrary-matrix target because `E` in (2.1) is completely arbitrary. Once a physical partition is found for which the augmented determinant `Omega` is bounded below on the natural scale, **all additional eigenvalues and cross couplings are already included** and a continuous density follows.

The first unpaid implication is now a geometric/exhaustive one rather than a new nonlinear trace inequality:

`QFORM-AUGMENTED-BANK-DICHOTOMY-v1`: from `s_3(A)>=1`, find a selected three-eigenvector frame and an original-coordinate partition such that either

(a) the augmented determinant `Omega` above has a universal lower scale and Theorem 3 applies; or
(b) a source-valid existing physical-pair/ridge/scalar-pivot/rank-one-bank branch is quantitatively forced.

A low-rank residual cross block is not itself enough: the singleton-plus-two-banks family shows why source grouping must remain available. A high-rank residual cross block is also not enough without transversality: (4.4) identifies the exact additional determinant that must be controlled.

Full QFORM therefore remains **OPEN / NOT PROVED**. This run proves essential boundedness and continuity only on the augmented-two-bank branch (3.1). No claim is made that every target matrix admits the required partition. The global continuous-density conclusion is also still open.
