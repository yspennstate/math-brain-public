# Diffuse two-light Fourier receiver with arbitrary source-local potentials

**Status:** proved scoped analytic theorem. It gives a product-compatible affine-null bridge for a separable light square and hub cross, and allows arbitrary diagonal quadratic perturbations. It does not handle a mixed light term such as beta L^2 or 2epsilon LP when L and P each use multiple original inputs. The unrestricted QFORM theorem remains open.

Let H and X_1,...,X_m be independent real random variables, each with probability density at most one. Let L=ell·X and V=v·X, where ell,v are orthonormal vectors in R^m and every physical row leverage ell_i^2+v_i^2 is at most 1/2. Let tau,lambda be nonzero real numbers. Let R_H and R_i be arbitrary measurable real functions for which the displayed random variable is finite almost surely. Define

Q=2tau H L + lambda V^2 + R_H(H) + sum_i R_i(X_i).

Then Q has a bounded continuous density and

||p_Q||_infinity <= 3 e^(2/3) / (|tau| sqrt(|lambda|))^(2/3).    (1)

For tau=lambda=1 this is less than 5.85. In particular the theorem permits every original-coordinate affine term, any hub self-square aH^2, and any original-coordinate diagonal quadratic sum_i d_i X_i^2, with **no dependence** on their coefficients.

## Fourier proof

Use the convention hat f(xi)=int exp(-i xi x)f(x)dx. The already proved diffuse two-frame Fourier certificate states that for every choice of separate measurable phases |omega_i(x)|<=1,

int_R² | E_X [prod_i omega_i(X_i) exp(i yL+i zV)] | dy dz
 <= K_2 := (2pi sqrt(e))².                                      (2)

This is the geometric Brascamp–Lieb plus sharp scalar Hausdorff–Young estimate for an orthonormal two-frame whose physical row leverages are at most 1/2. A proof with the precise constant is in [the diffuse Wiener provenance report](https://github.com/yspennstate/math-open-problems/blob/1fcdb431e3fbe3cd369593c599f86d5bc1dd6102/proofnet24/QFORM-density/interactive/20260923T194039Z-diffuse-wiener-provenance/REPORT.md). In particular, (2) is uniform over the t-dependent phases omega_i(x)=exp(itR_i(x)).

Let phi_Q(t)=E exp(itQ). For t≠0 put
F_t(y,z)=E_X exp(i yL+i zV+it sum_i R_i(X_i)).
Equation (2) gives ||F_t||_L1(R²)<=K_2. The one-dimensional Fresnel identity for exp(it lambda V²), first with a Gaussian damping factor and then by dominated convergence using F_t∈L1, yields

phi_Q(t)=c_(t,lambda) int_R dz exp(-iz²/(4t lambda))
                    int_R dh f_H(h) exp(itR_H(h)) F_t(2tau t h,z),

where |c_(t,lambda)|=1/(2sqrt(pi |t lambda|)).
The Gaussian-damped identity has a kernel of modulus at most 1/(2sqrt(pi |t lambda|)), so the limit and the following estimate are justified without any moments or smoothness. Since f_H<=1, change variables y=2tau t h and take absolute values:

|phi_Q(t)|
 <= [1/(2sqrt(pi |t lambda|))] [1/(2|tau t|)] ||F_t||_1
 <= [pi^(3/2)e/(|tau|sqrt(|lambda|))] |t|^(-3/2).                (3)

Also |phi_Q(t)|<=1. Write C=pi^(3/2)e/(|tau|sqrt(|lambda|)). Fourier inversion applies because min(1,C|t|^(-3/2)) is integrable, giving a bounded continuous output density. Direct integration at the crossover |t|=C^(2/3) gives

||p_Q||_infinity
 <= (1/(2pi)) int_R min(1,C|t|^(-3/2))dt
 = (3/pi) C^(2/3)
 = 3e^(2/3) / (|tau|sqrt(|lambda|))^(2/3).

This proves (1).

## Scope and boundary

The source-local terms may have any size and sign because their Fourier phases factor across the **original independent coordinates**. The hub phase is similarly harmless after taking its absolute value. No moment, support, continuity, or bounded-variation hypothesis is used.

The assumption on full two-frame row leverage is substantive. The proof uses (2), which fails for some high-leverage frames. Such finite-heavy configurations may instead admit physical-coordinate or planar-bank receivers.

A nonseparable term beta L², 2epsilon LP, or a general additional quadratic tail creates cross-coordinate Fourier phases and invalidates (2). A separate product-compatible receiver is still needed there, particularly at negative targets. This theorem is not the full RMT/QFORM proof.
