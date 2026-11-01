SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T21:24:59Z.
attacking: QFORM-ZEROPIVOT-NEARRANK1-INTEGRATED-CHIRP-BRIDGE-v1 — determine whether the exact-rank-one three-bank tensor Fourier gain survives a genuinely nonzero cross-Schur tail without deleting it; if not, isolate the exact pointwise obstruction and route the live V1 mass through D'/D5 or a genuinely integrated-in-time mechanism.

# Early checkpoint — nonzero-tail chirp operator is pointwise critical

Programme: `QFORM-DENSITY-3EIG-20260922`. Full unrestricted QFORM remains OPEN. Target-wide universal unweighted Fourier-L1 remains OPEN / not refuted.

## Sources consumed

- Required base Fourier package at `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.
- Reviewed q-dependent sharp-HY refinement and its D'/D5 consequences from the existing QFORM source chain.
- Current grouped crossing theorem `NEW_PROJECTED_CROSSING.md` at release commit `d2f970d33fa7084f8de55412189402ac609e4da6`; it retains arbitrary same-bank phases but still degenerates with the small projected crossing direction.
- Immediate same-slot exact-rank-one tensor theorem in `20260923T200844Z-fleet02-B02-qform-auto11/REPORT.md` and positive-tail physical compound checkpoint in `20260923T204251Z-fleet02-B02-qform-auto11-r2/EARLY.md`.
- Newest designated partner fleet03/B02 r39, `QFORM-V1-GLOBAL-THREEBANK-COMPILER-v1`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T210023Z-fleet03-B02-qform-r39/REPORT.md`.

No pointwise scalar Fresnel decay, post-rotation independence, conditional-density cap, or deletion of a nonzero matrix tail is used.

## 1. The exact perturbation operator

The exact-rank-one shared-hub proof reduces the star sector to

`(T_0 f)(y)=int k_t(alpha y+beta z) f(z) dz`,

where

`k_t(s)=hat g(2ts)`, `0<=g<=1`, `int g=1`,

and `g` is the physical hub density after an affine modulation of modulus one. A genuinely nonzero cross-Schur coefficient `delta` inserts the bilinear phase

`(T_delta f)(y)=int k_t(alpha y+beta z) exp(i 2t delta yz) f(z) dz`.       (1.1)

Assume `alpha beta delta t !=0` and set

`mu=2t delta/(alpha beta)`.                                             (1.2)

Scale `x=alpha y`, reflect/scale `w=-beta z`, and use

`-mu xw =-(mu/2)x^2-(mu/2)w^2+(mu/2)(x-w)^2`.                         (1.3)

The outer two factors are unitary chirp multipliers. Therefore `T_delta` is unitarily equivalent, up to the exact Jacobian factor `|alpha beta|^{-1/2}`, to convolution by

`h_(mu,t)(s)=k_t(s) exp(i mu s^2/2)`.                                  (1.4)

With the angular Fourier convention `hat f(xi)=int exp(i xi x)f(x)dx`, the L2 operator norm is exactly

`boxed:
 ||T_delta||_(2->2)
 = |alpha beta|^(-1/2)
   || hat( k_t(.) exp(i mu (.)^2/2) ) ||_infinity.`                    (1.5)

This identity keeps the full nonzero tail. No approximation has been made.

## 2. Singular discontinuity at delta=0

At `delta=0`, Fourier scaling gives

`hat k_t(xi)= (pi/|t|) g(-xi/(2t))`,                                  (2.1)

hence the exact-rank-one estimate

`boxed:
 ||T_0||_(2->2)
 <= pi |t|^(-1)|alpha beta|^(-1/2).`                                  (2.2)

For `delta!=0`, Fresnel integration in `s` instead gives

`hat h_(mu,t)(xi)
 = sqrt(2pi/|mu|) exp(i theta(xi,t))
   int g(h)
      exp(-i (xi+2th)^2/(2mu)) dh`,                                   (2.3)

where the prefactor phase has modulus one. Since `int g=1`, (1.5) and (1.2) imply the law-uniform bound

`boxed:
 ||T_delta||_(2->2)
 <= sqrt(pi/(|t delta|)),     delta!=0.`                               (2.4)

Thus the extra star-sector power drops from `|t|^-1` at the exact algebraic endpoint to only `|t|^-1/2` under an arbitrarily small nonzero cross-Schur perturbation.

The loss in (2.4) is not an artefact of the estimate when one insists on a law-uniform pointwise operator norm. For any fixed nonzero `t,delta` and any epsilon>0, the quadratic phase in the last integral of (2.3) has infinitely many level windows on which its argument lies within epsilon of one fixed phase. The total Lebesgue measure of these windows is infinite (their lengths are comparable to `n^-1/2` along the quadratic levels). Select a measurable subset `E` of total measure one from their union and take `g=1_E`. Then `g` is an admissible cap-one probability density and the modulus of the last integral is at least `cos(epsilon)`. Hence (2.4) is sharp up to an arbitrarily small multiplicative loss at each fixed point `(t,delta)`.

This does NOT provide one fixed density saturating all `t`; therefore it is not a counterexample to integrated Fourier-L1. It is a precise obstruction to any proof that first takes the law-uniform pointwise norm in (1.5) and only then integrates in `t`.

## 3. Why the naive perturbation of the three-bank tensor proof becomes exactly critical

The transverse factor retained by the exact-rank-one tensor theorem is a genuine scalar bilinear transform

`(S_sigma f)(y2)=int exp(i2t sigma y2 z2)f(z2)dz2`,

whose exact L2 norm is

`||S_sigma||_(2->2)=sqrt(pi/(|t sigma|)).`                             (3.1)

Tensoring (2.4) with (3.1) gives only

`boxed:
 ||T_delta tensor S_sigma||_(2->2)
 <= pi |t|^(-1)|delta sigma|^(-1/2).`                                 (3.2)

The exponent is exactly the nonintegrable `|t|^-1` endpoint. At `delta=0`, (2.2) times (3.1) gives the integrable `|t|^-3/2` envelope proved in the preceding B02 report. Consequently the known exact-rank-one tensor proof cannot be continued uniformly through a nonzero tail by a pointwise operator-norm perturbation. The next proof must integrate in time before taking the worst modulation/frequency, or spend an independent physical volume resource.

## 4. Latest partner r39 applied to the live V1 heavy-hub branch

Partner r39 proves that an actual original-coordinate three-bank partition satisfies

`W >= (16/3125) V1`,                                                   (4.1)

where `W=sum_h D_h` is the overlap-one third-minor mass surviving the partition. On its heavy-hub alternative, some physical `h` obeys

`D_h>=W/2 >= (8/3125)V1`.                                              (4.2)

At the exact zero-pivot endpoint `A_hh=0`, the local exterior identity is

`D_h=T_h=||c_h||^2||r_h||^2||P_(c_h^perp)N P_(r_h^perp)||_F^2`.        (4.3)

Thus the previous exact-rank-one tensor theorem gives an actual new global V1 inequality on the subbranch `rank N=1`:

`boxed:
 ||p_Q||_infinity
 <=3*2^(2/3) T_h^(-1/6)
 <=12.875614 V1^(-1/6).`                                               (4.4)

For a genuinely positive transverse tail with stable-rank parameter `1<rho<=2` and `b=min(||c_h||^2,||r_h||^2)/||C_h||_F^2`, the physical append-one-row/column identities from the immediately preceding B02 checkpoint give a literal physical cross block `M_*` with

`E3(M_*) >= ((rho-1)/(rho^2 b)) T_h`.                                 (4.5)

Applying the marginal-free D' / physical-E3 Fourier theorem to (4.5), then (4.2), yields

`boxed:
 ||p_Q||_infinity
 <=27.970099 [b rho^2/(rho-1)]^(1/6) V1^(-1/6),`                       (4.6)

with a genuine unweighted Fourier-L1 estimate on this positive-tail branch. The reviewed D5 exit remains, on the same literal physical blocks,

`boxed:
 ||p_Q||_infinity
 <=(5e/sqrt(2)) [M E4(C_h)]^(-1/10)`                                 (4.7)

whenever `E4(C_h)>0`.

Equations (4.4)-(4.7) are an equation-level use of the newest designated partner result, not citation-only reuse. They also make the exact gap explicit: (4.4) is finite at rank one, while the D'/E3 coefficient in (4.6) blows like `(rho-1)^(-1/6)` as `rho downarrow1`, and D5 can vanish identically on a rank-two transverse model.

## 5. Next exact debt

The first unpaid implication is now

`QFORM-ZEROPIVOT-NEARRANK1-INTEGRATED-CHIRP-BRIDGE-v1`:

for the actual three-bank kernel (1.1) coupled to the transverse bilinear factor, obtain an estimate that integrates in `t` before taking the worst modulation/frequency and remains uniform as `delta->0`, using the original cap-one product law; or route the same heavy/diffuse V1 resource through a separate paid physical-volume mechanism. A pointwise operator-norm interpolation between (2.2) and (2.4) is now ruled out as a uniform strategy.

Full QFORM and target-wide universal unweighted Fourier-L1 remain OPEN. The obstruction above concerns one proof mechanism only and is not a target counterexample.