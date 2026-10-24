SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T16:40:47Z.
attacking: translation-uniform low-rank receiver localization: preserve arbitrary outside affine terms and unbounded supports while coupling the partner slice-Fresnel core to a whole independent receiver bank with quadratic self-curvature.

# account03/B14 auto11 — hybrid quadratic-receiver localization

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING THEOREM / TARGET-VALID DIFFUSE FAMILY / FULL QFORM OPEN`  
**Continuity:** the theorem below proves an essentially bounded density. A continuous representative is not claimed by the abstract mixture argument; continuity remains separate.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

This run consumed the later owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` at the prepublication refresh. The already-created actual-hour login was preserved rather than overwritten. The full conjecture remains open.

## 1. Sources actually used

The designated partner theorem is account04/B14 r9:

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

On its residual-diffuse exact-null physical-core branch it proves, uniformly in the entire conditioning-generated affine vector,

    |hat mu_{l,g}(t)| <= 4 sqrt(pi) |gamma t|^(-1/2).                 (1.1)

Its translated Brascamp--Lieb step applies the newest-Claude cap-one Fourier inequality

    integral |hat f(omega)|^p d omega <= 4 pi / sqrt(p),  p>=2,      (1.2)

from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The current continuation at `c4c23b784395630c094ba299a50712209921d1ae` was read. Its new `(SP)` estimate for a hub adapted to an extra projection is explicitly OPEN and is not used below.

I also apply the current volume-stability theorem at an actual inequality in Section 6. Its source is

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

## 2. New theorem: an L^p core plus a self-curved random-slope receiver

### Theorem 2.1 — `QFORM-HYBRID-QUADRATIC-RECEIVER-LP-v1`

Let `Z=(Z_1,...,Z_m)` and `W` be disjoint ORIGINAL coordinates. Assume all of them are independent probability variables with densities at most one. Let `T_z` be a measurable conditional random variable built from further original coordinates, independent of `W` after conditioning on `Z=z`.

Fix

    4/3 < r < 2,          p=r/(r-1),

and suppose, for almost every `z`, `T_z` has a density with

    ||p_{T_z}||_p <= K_r.                                          (2.1)

Let `d,e` be real, `c in R^m`, and put

    R_0 = sqrt(d^2+||c||_2^2)>0.                                  (2.2)

For an arbitrary measurable additive shift `s(z)`, define

    Q = T_Z+s(Z)+d W^2+(2 c^T Z+e)W.                              (2.3)

Then `Q` has an essentially bounded density and

    boxed:
    ||p_Q||_infinity
      <= K_r 2^[3(r-1)/(2r)] (2-r)^(-1/r)
             R_0^[-(r-1)/r].                                     (2.4)

The constant is independent of `m`, `e`, `s`, all support locations and diameters, all fragment counts and separations, and all moments.

### Proof

Condition on `Z=z` and write

    F_z(w)=d w^2+b(z)w,       b(z)=2c^Tz+e.                       (2.5)

Let `q_z` be the density of `F_z(W)`. A nonconstant quadratic has at most two preimages away from its single critical value. The one-dimensional area formula gives

    q_z(y)=sum_{w:F_z(w)=y} f_W(w)/|2dw+b(z)|                    (2.6)

for almost every `y`. For `1<r<2`, convexity of `x^r` over a sum of at most two terms gives

    int q_z(y)^r dy
      <=2^(r-1) int f_W(w)^r |2dw+b(z)|^(1-r) dw
      <=2^(r-1) E_W |2dW+b(z)|^{-(r-1)},                          (2.7)

because `f_W<=1` implies `f_W^r<=f_W`. Hence

    ||q_z||_r
      <=2^(1-1/r)
        [E_W |2dW+b(z)|^{-(r-1)}]^(1/r).                         (2.8)

Average (2.8) over `Z`. Since `x -> x^(1/r)` is concave,

    E_Z ||q_Z||_r
      <=2^(1-1/r)
        [E_{Z,W}|2dW+2c^TZ+e|^{-(r-1)}]^(1/r).                  (2.9)

The scalar

    S=2dW+2c^TZ+e                                                   (2.10)

is a linear projection of independent cap-one original coordinates. The source-valid Rogozin--Ball projection bound yields

    ||p_S||_infinity
      <= sqrt(2)/(2R_0)
      =1/(sqrt(2)R_0).                                             (2.11)

For every probability density `p<=M`, every shift `a`, and every `0<alpha<1`, symmetric decreasing rearrangement gives the exact cap-only fractional estimate

    int |x-a|^{-alpha}p(x)dx
      <= 2^alpha M^alpha/(1-alpha).                               (2.12)

Apply (2.12) with `alpha=r-1` and `M=1/(sqrt(2)R_0)`:

    E|S|^{-(r-1)}
      <= 2^[(r-1)/2](2-r)^(-1)R_0^{-(r-1)}.                       (2.13)

Substituting (2.13) into (2.9) gives

    E_Z ||q_Z||_r
      <=2^[3(r-1)/(2r)](2-r)^(-1/r)R_0^{-(r-1)/r}.               (2.14)

For fixed `z`, `T_z` and `F_z(W)` use disjoint original-coordinate source banks and are genuinely independent. Holder convolution at conjugate exponents `p` and `r` therefore gives

    ||p_{T_z}*q_z||_infinity <= K_r ||q_z||_r.                    (2.15)

The additive shift `s(z)` does not affect this norm. Averaging (2.15) over `z` and using (2.14) proves (2.4). Tonelli/area formula also shows absolute continuity. QED.

### Why this is a localization theorem rather than a moment estimate

The singular derivative `|2dW+2c^TZ+e|^{-1}` is never paid fiberwise. The worst-fiber reciprocal can diverge when `2c^TZ+e` approaches a critical value. The proof first keeps the whole independent `(W,Z)` bank intact, lowers the singularity to the exponent `r-1<1`, and then pays the aggregate coefficient vector `(d,c)` through its Euclidean norm. This is exactly the order needed for arbitrary remote fragments and unbounded supports.

## 3. Equation-level application of account04/B14 r9

The partner slice theorem (1.1), after changing the slice coordinate from `V` to

    L=hV+q_0,

has unnormalised slice Fourier constant

    A=4 sqrt(pi)/(|h|sqrt(|gamma|)).                               (3.1)

Let `nu_l` denote the resulting unnormalised slice measure with respect to `dl`, and let `m(l)=nu_l(R)` be its mass. Then

    integral m(l) dl=1,
    |hat nu_l(t)| <= min(m(l), A|t|^(-1/2)).                      (3.2)

Consequently

    integral |hat nu_l(t)|^2 dl
      <= A|t|^(-1/2) integral m(l)dl
      = A|t|^(-1/2).                                               (3.3)

Now let the physical hub carry any real measurable phase `H(X_0)` and define

    F_t(l)=integral f_0(x) exp(itH(x)) exp(2itlx) dx.               (3.4)

Multiplication by `exp(itH(x))` is unimodular. Plancherel in the ORIGINAL hub coordinate therefore gives

    integral |F_t(l)|^2 dl
      = (pi/|t|) integral f_0(x)^2 dx
      <= pi/|t|.                                                    (3.5)

The whole-core characteristic function is the pairing of `hat nu_l(t)` with `F_t(l)`. Cauchy--Schwarz in `l`, (3.3), and (3.5) yield

    |phi_T(t)|
      <= B |t|^(-3/4),
    B=sqrt(pi A)
      =2 pi^(3/4)|h|^(-1/2)|gamma|^(-1/4).                         (3.6)

This is an equation-level use of account04/B14's completed slice inequality. The arbitrary affine vector generated by outside conditioning is already uniform in (1.1), and the newest-Claude inequality (1.2) is the equation that makes that translation uniformity possible.

For `4/3<r<2`, combine (3.6) with `|phi_T|<=1`. The crossover is `t_0=B^(4/3)`, and

    int_R |phi_T(t)|^r dt
      <=2 B^(4/3)[1+4/(3r-4)]
      = [6r/(3r-4)] B^(4/3).                                     (3.7)

Inverse Hausdorff--Young, with Fourier convention `hat f(t)=int e^{itx}f(x)dx`, gives

    ||p_T||_{r/(r-1)}
      <=(2pi)^(-1/r)[6r/(3r-4)]^(1/r) B^(4/(3r)).                (3.8)

Insert (3.8) into Theorem 2.1. The powers of `pi` cancel exactly:

    boxed:
    ||p_Q||_infinity
      <= 2^[(9r-7)/(6r)]
         [6r/((3r-4)(2-r))]^(1/r)
         |h|^[-2/(3r)] |gamma|^[-1/(3r)]
         R_0^[-(r-1)/r].                                        (3.9)

Thus account04/B14's translation-uniform half-Fresnel core can now absorb an additional receiver that has BOTH a quadratic self coefficient `d` and a driver-dependent random slope `2c^TZ+e`. The previous linear-receiver compiler did not allow the `dW^2` term.

Choosing the exact rational exponent

    r=12/7                                                        (3.10)

gives

    boxed:
    ||p_Q||_infinity
      <=2^(59/72)(63/2)^(7/12)
        |h|^(-7/18)|gamma|^(-7/36)
        (d^2+||c||_2^2)^(-5/24).                                (3.11)

At the partner normalized scale

    |h|>=2^(-1/2),  |gamma|>=1,  sqrt(d^2+||c||^2)>=1,

(3.11) is less than

    2^(73/72)(63/2)^(7/12)=15.1086429339.                         (3.12)

No tail truncation or moment enters this estimate.

## 4. Translation, fragment, and unbounded-support invariance

The scale in Theorem 2.1 is exactly `sqrt(d^2+||c||^2)`. Translate any original receiver and driver coordinates:

    W -> W+a,       Z -> Z+z_0.                                  (4.1)

The coefficients `d` and `c` do not change. Only `e`, the additive shift `s(z)`, and conditioning-generated affine terms in the core change. Theorem 2.1 is uniform in `e,s`, and account04/B14 r9 is uniform in every affine core vector. Hence arbitrary physical translations cost exactly zero.

The proof never asks where a marginal is supported. Equations (2.11)-(2.13) use only total mass one and the cap one. Thus finite, countable or arbitrarily distant fragments and unbounded support carry no diameter, separation, count or moment penalty. No normalization of thin fragments occurs.

For an independent rough-law approximation route, account04/B14's continuum compiler at `63ba8e0f106c3bb405f05eb99778039ff47ed47b` gives cap-preserving compact smooth approximants in total variation and transfers uniform interval bounds through the polynomial pushforward with the identical constant. Applying that theorem to (3.11) therefore gives a second, zero-loss route from compact smooth inputs to arbitrary cap-one product laws.

## 5. Target-valid diffuse family where self-curvature is essential

The new receiver is not merely an already-target-valid smoothing add-on. Let all variables below be independent with arbitrary cap-one densities. Put

    V=(X_1+X_2)/sqrt(2),
    Y=(X_3+X_4)/sqrt(2),
    a_m=m^(-1/2)(1,...,1),

and define

    Q_m
      =2 X_0 V +(1/2)Y^2
       +W^2+2(a_m^TZ)W.                                          (5.1)

The first five physical coordinates form an isometric exact-rank-three frame with coefficient-space matrix

    M_core=[[0,1,0],[1,0,0],[0,0,1/2]],                           (5.2)

so its nonzero eigenvalues are `1,-1,1/2`. The residual transverse row leverages are exactly `1/2`, hence the partner r9 slice theorem applies with

    h=1,   gamma=1/2.                                             (5.3)

The receiver/driver block on `span{W,a_m^TZ}` is

    [[1,1],[1,0]],                                                (5.4)

with eigenvalues

    (1+sqrt(5))/2,   (1-sqrt(5))/2.                              (5.5)

Therefore the full quadratic matrix has three eigenvalues of absolute value at least one:

    1,  -1,  (1+sqrt(5))/2.                                      (5.6)

The third target-scale eigenvalue genuinely comes from the self-curved receiver block; the partner core alone has only two eigenvalues of modulus at least one.

In (3.11), `d=1`, `||c||=||a_m||=1`, so `d^2+||c||^2=2`. Hence

    boxed:
    ||p_{Q_m}||_infinity
      <=2^(29/36)(63/2)^(7/12)
      =13.0770828465...                                          (5.7)

for every `m`. Every individual receiver-driver coefficient is `1/sqrt(m)` and tends to zero. The whole-bank bound does not pay a reciprocal coordinate coefficient and therefore remains dimension free.

This family is a genuine member of the original target for every `m`; it is not a Monte Carlo claim and no interval/extremality assumption is used.

## 6. Actual application of the newest volume-stability theorem

The current interactive theorem at

`math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

states that if an ORIGINAL-coordinate crossing block satisfies

    M=M_0+E,
    s_3(M_0)>=a,
    max_i (P_range(M_0))_ii<=1/2,
    ||E||_op<=a/16,                                                (6.1)

then, uniformly in arbitrary within-bank functions and conditioning-generated affine terms,

    ||p_C||_infinity <23/a.                                       (6.2)

Apply this to a conditional core `C_z` satisfying the same matrix gate for every realization of an outside driver bank `Z`. Add a disjoint receiver coordinate `W` exactly as in (2.3), with arbitrary `d,c,e`:

    Q=C_Z+dW^2+(2c^TZ+e)W+s(Z).                                  (6.3)

For every fixed `z`, the receiver term is independent of `C_z` and has a probability law, so convolution cannot increase an `L^infinity` norm:

    ||p_{Q|Z=z}||_infinity
      <=||p_{C_z}||_infinity
      <23/a.                                                       (6.4)

Averaging over `z` gives

    boxed: ||p_Q||_infinity <23/a.                                (6.5)

Thus the newest near-diffuse volume exit is automatically stable under this entire self-curved, random-slope, translation-unbounded receiver appendage. Equation (6.4), not a copied citation, is the actual application.

The new Theorem 2.1 matters in the complementary situation where the retained core is available only in a finite `L^p` class, as in the partner slice-Fresnel branch, and therefore ordinary `L^infinity` contraction is unavailable.

## 7. Scope and remaining full-target debt

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This run pays a precise localization interface:

- arbitrary shifts of the receiver and driver banks;
- arbitrarily distant or unbounded fragmented supports;
- no moments;
- receiver self-curvature `dW^2` and a diffuse random slope `2c^TZW` jointly;
- arbitrary driver-to-core couplings that, after conditioning on `Z`, appear only as the affine core terms already covered by account04/B14 r9.

It does **not** yet allow the receiver coordinate `W` to have additional quadratic cross-couplings directly to the unconditioned partner core. Nor does `s_3(A)>=1` by itself force a decomposition with a partner-certified slice core and a hybrid receiver scale `sqrt(d^2+||c||^2)` bounded below universally. The newest Claude `(SP)` adapted-hub estimate remains open and is not silently assumed.

The next B14-local obstruction is therefore a genuinely overlapping receiver: preserve the `L^p` core gain when the receiver's slope also depends on the same original coordinates that produce the slice core, without replacing their joint law by an arbitrary bounded projection density or a worst conditional cap.

No continuity conclusion for the full target follows from this report.

## 8. Finite checks

For the target-valid family (5.1), the receiver/driver star has nonzero spectrum `(1+-sqrt(5))/2` for every `m`. Direct numerical diagonalisation at `m=1,2,10,100` gives the same extrema `-0.6180339887...` and `1.6180339887...`. The exact constants are

    2^(59/72)(63/2)^(7/12)=13.2035844419...,
    2^(29/36)(63/2)^(7/12)=13.0770828465... .                    (8.1)

These checks only verify arithmetic/spectrum; the proof is the analytic argument above.
