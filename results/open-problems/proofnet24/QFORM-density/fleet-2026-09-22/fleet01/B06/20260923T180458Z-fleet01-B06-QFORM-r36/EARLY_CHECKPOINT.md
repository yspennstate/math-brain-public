SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B06, 2026-09-23T18:04:58.766711Z.
attacking: the curved-section replacement behind (CS) — retain the parabola exactly, integrate the singular Fresnel weight against product Fourier volume before any fiber supremum, and splice diffuse-frame and disjoint-bank regimes.

# Early substantive calculation — weighted curved-section Brascamp–Lieb

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T180458Z-fleet01-B06-QFORM-r36`  
Status: `SUPPORTING_ANALYTIC_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture is **not** proved here. This checkpoint attacks the current source's curved-section statement `(CS)` in a quantitative product-preserving regime. No support, moment, log-concavity, iid, spectral-coordinate independence, or pointwise quadratic-phase decay assumption is used.

## 1. Scalar Fourier input

For a cap-one probability density `f` on `R`, write

`psi(z)=int f(x) exp(i z x) dx`.

Use the source-valid sharp integral estimate

`int_R |psi(z)|^p dz <= 4 pi / sqrt(p),   p>=2`.                 (1.1)

The only other analytic input is geometric Brascamp--Lieb. If vectors `r_i in R^d` satisfy

`sum_i r_i r_i^T = I_d`,                                             (1.2)

and `ell_i=|r_i|^2<=1/2`, then for arbitrary shifts `c_i`,

`int_{R^d} prod_i |psi_i(<r_i,z>+c_i)| dz <= (4 pi)^d`.         (1.3)

Indeed write `r_i=sqrt(ell_i)e_i`, use BL with weights `ell_i`, and set
`G_i(s)=|psi_i(sqrt(ell_i)s+c_i)|^(1/ell_i)`. Then

`int G_i = ell_i^(-1/2) int |psi_i|^(1/ell_i)
          <= ell_i^(-1/2) 4pi sqrt(ell_i)=4pi`,

because `1/ell_i>=2`; zero rows are omitted. This proof is translation-uniform.

We will also use the elementary interpolation identity: if `H>=0`, `||H||_infinity<=M`, and `int H<=N`, then

`int_R |t|^(-1/2) H(t) dt <= 4 sqrt(MN)`.                        (1.4)

Proof: split at `R>0`; the inner part is at most `4M sqrt(R)` and the outer part at most `N/sqrt(R)`. Optimize at `sqrt(R)=sqrt(N)/(2sqrt(M))`.

## 2. One-output curved marginal

### Theorem 2.1 — `QFORM-DIFFUSE-PARABOLIC-P2-v1`

Let `X_1,...,X_n` be independent with densities at most one. Let `u,v in R^n` be orthonormal and assume

`u_i^2+v_i^2 <= 1/2` for every `i`.                               (2.1)

Put `U=<u,X>`, `V=<v,X>`. For every `c!=0` and every `v_0 in R`,

`F=U+c(V-v_0)^2`                                                  (2.2)

has a continuous density vanishing at infinity and

`boxed: ||p_F||_infinity <= 8 / sqrt(|c|).`                       (2.3)

#### Proof

For `t!=0`, Fresnel linearization gives

`|phi_F(t)| <= (4pi |ct|)^(-1/2) H(t)`,                           (2.4)

where

`H(t)=int_R prod_i |psi_i(t u_i + xi v_i)| dxi`.                 (2.5)

(The translation `v_0` contributes only a unimodular factor.)

For fixed `t`, apply (1.3) in the one-dimensional `v` frame; since `v_i^2<=1/2`,

`H(t)<=4pi`.                                                       (2.6)

Integrating in `t` and `xi`, apply (1.3) to the two-dimensional frame `(u_i,v_i)`:

`int_R H(t) dt <= (4pi)^2`.                                      (2.7)

Equations (1.4), (2.6), (2.7) give

`int |t|^(-1/2) H(t) dt <=32 pi^(3/2)`.                          (2.8)

Therefore

`int |phi_F(t)| dt <=16 pi / sqrt(|c|)`.                          (2.9)

Fourier inversion divides by `2pi`, proving (2.3), and the `L^1` characteristic function gives a continuous `C_0` representative. QED.

The point is that the curvature singularity `|t|^{-1/2}` is averaged against the **same product Fourier volume** before any supremum over a spectral fiber.

## 3. The two-output parabola section

The current Claude continuation isolates the curved-section map

`L=<w,X>,   Y=lambda (V-v_0)^2 + beta B`,                         (3.1)

where `w,v,b` are orthonormal, `V=<v,X>`, `B=<b,X>`. The desired `(CS)` estimate is an off-fold joint-density bound of order `1/(|lambda|r)`.

### Theorem 3.1 — `QFORM-DIFFUSE-CURVED-SECTION-BL-v1`

Assume

`w_i^2+v_i^2+b_i^2 <=1/2` for every `i`,                          (3.2)

and `lambda beta !=0`. Then `(L,Y)` has a continuous joint density vanishing at infinity and

`boxed: ||p_(L,Y)||_infinity <= 16 / sqrt(|lambda beta|).`        (3.3)

Consequently the subprobability pushforward restricted to

`|V-v_0|>r`                                                        (3.4)

has density at most the same quantity; in particular, whenever

`|beta| >= |lambda| r^2`,                                         (3.5)

it obeys the exact `(CS)` scaling

`boxed: ||p_(L,Y; |V-v_0|>r)||_infinity <=16/(|lambda|r).}`       (3.6)

#### Proof

Let

`Phi(s,t)=E exp{i[sL+tY]}`.                                       (3.7)

Fresnel linearization of the square gives

`|Phi(s,t)| <= (4pi |lambda t|)^(-1/2)
               int_R prod_i |psi_i(s w_i + xi v_i + t beta b_i)| dxi`. (3.8)

Set `tau=beta t` and

`H(tau)=int_{R^2} prod_i |psi_i(s w_i + xi v_i + tau b_i)| ds dxi`.    (3.9)

For fixed `tau`, (1.3) for the two-dimensional frame `(w,v)` gives

`H(tau)<= (4pi)^2`;                                                (3.10)

integrating over `tau`, (1.3) for the three-dimensional orthonormal frame `(w,v,b)` gives

`int H(tau) dtau <= (4pi)^3`.                                     (3.11)

Hence (1.4) yields

`int |tau|^(-1/2)H(tau) dtau <=4 sqrt((4pi)^2(4pi)^3)
                                =128 pi^(5/2)`.                    (3.12)

Using `|t|^(-1/2)dt=|beta|^(-1/2)|tau|^(-1/2)dtau`, (3.8) implies

`int_{R^2}|Phi(s,t)| ds dt <=64 pi^2 / sqrt(|lambda beta|)`.      (3.13)

Two-dimensional Fourier inversion divides by `(2pi)^2=4pi^2`, proving (3.3). Restriction to (3.4) only decreases the pushforward measure, so its density is bounded by (3.3). Under (3.5), `sqrt(|lambda beta|)>=|lambda|r`, giving (3.6). QED.

This closes the high-linear-transverse-coefficient side of `(CS)` in the fully diffuse three-frame regime. It does **not** close the complementary `|beta|<|lambda|r^2` regime: a small coefficient cannot be discarded because the rough input law may have unbounded support.

## 4. Designated partner fleet02/B06 applied: exact three-bank endpoint

Use the completed fleet02/B06 theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` (canonical source `math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`). Suppose now that `w,v,b` are supported on three pairwise disjoint original-coordinate banks `S,T,R`. Then `L,V,B` are independent, and the partner theorem gives at the actual inequalities

`||p_L||_infinity <= sqrt(e),
 ||p_V||_infinity <= sqrt(e),
 ||p_B||_infinity <= sqrt(e).`                                   (4.1)

On the off-fold set `|V-v_0|>r`, the subprobability density of

`Z=lambda(V-v_0)^2`                                               (4.2)

has at most two inverse branches, each with Jacobian at least `2|lambda|r`, so

`||p_(Z;off)||_infinity <= sqrt(e)/(|lambda|r)`.                  (4.3)

Since `B` is independent of `V`, convolution with `beta B` cannot raise this supremum, and since `L` is independent of both,

`boxed: ||p_(L,Y; |V-v_0|>r)||_infinity <= e/(|lambda|r).}`       (4.4)

Thus `(CS)` holds with constant `e` on the exact three-bank ray endpoint, for every `beta` including `beta=0`, arbitrary fragmented cap-one laws, and no support or moment restriction. Equation (4.1) is the required actual use of the designated partner result.

## 5. What remains

The two new endpoints are complementary but do not yet prove `(CS)` in full:

* diffuse three-frame leverage plus `|beta|>=|lambda|r^2` is paid by (3.6);
* exact disjoint-bank geometry is paid for every `beta` by (4.4).

The first unpaid implication is therefore

`QFORM-CURVED-SECTION-SMALL-BETA-OVERLAPPING-v1`:

> Under the diffuse leverage gate (3.2), prove the off-fold bound `C/(|lambda|r)` uniformly when `|beta|<|lambda|r^2`, without treating `beta B` as a small random error and without replacing the curved section by its fiberwise supremum; or prove a quantitative structural splice that routes this regime to a grouped-bank receiver before reciprocal Jacobian payment.

This is precisely the region in which the source maximal-functional route loses dimension. The new proof shows why the **large** transverse slope does not lose dimension: the singular Fresnel weight is integrated against a three-dimensional product Fourier volume.

Full unrestricted QFORM status: **OPEN**. Full-target continuity status: **OPEN**.