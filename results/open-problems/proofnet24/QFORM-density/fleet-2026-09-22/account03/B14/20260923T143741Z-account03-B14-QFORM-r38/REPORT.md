SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T14:37:41Z.
attacking: whole-support chirp localization for the new affine slice-Fresnel branch, with an arbitrary hub self-phase and no tail, support, moment, or fragment payment.

# account03/B14 r38 — chirp-stable slice localization and the exact endpoint barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: translations and localization  
Status: **NEW SUPPORTING ANALYTIC THEOREM / PARTNER RESULT APPLIED / ENDPOINT OBSTRUCTION IDENTIFIED / FULL QFORM OPEN**  
Continuity: **not proved here**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted quadratic-form conjecture remains OPEN. This report does not claim a universal `L^infinity` density bound. It proves a new whole-support compiler that is completely insensitive to an arbitrary one-variable hub phase, including an arbitrarily small or large quadratic pivot, and applies it to account04/B14's newest affine slice-Fresnel estimate. The result gives a pivot-uniform `L^2` density on that branch without truncating, fragmenting, centering, or imposing moments. An explicit compact product example then shows why the partner's `1/2`-Hölder slice estimate, by itself, cannot be promoted to `L^infinity` after an arbitrary hub self-phase: one must retain additional phase/determinant structure.

## 1. Fresh source and exact partner input

Fresh `math-research-brain` main was read before this work at

`54a02a82ba1de885cf0ddf5ff8911ba5a2e3b73c`.

OWNER CONTROL remains revision `2026-09-22.15`; QFORM is the sole research target and no B14 stop/pause was present. The current state still marks the full conjecture OPEN and continuity OPEN. The live corrections were reread; in particular this run does not use law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea, post-rotation independence, bounded-diameter localization, or a conditional projection-density moment.

The designated partner result actually used below is account04/B14 r9,

`QFORM-AFFINE-SLICE-FRESNEL-BL-v1`,

source

`yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T141430Z-account04-B14-affine-slice-fresnel-r9/REPORT.md`.

In its heavy physical exact-null residual-diffuse normal form,

`Q_0 = 2 X_0 (h V + q_0) + Y_g`,

with `h=b sqrt(c)`, account04/B14 proves for the unnormalised slice law `mu_{v,g}` of `Y_g` on `V=v`

`|hat(mu_{v,g})(t)| <= 4 sqrt(pi) |gamma t|^(-1/2)`             (1.1)

for almost every `v`, uniformly in all affine leakage, translations, supports, tails, ambient dimension, and the slice location. This is their equation (3.6). Their final null-hub receiver gives an `L^infinity` density when the hub self-phase is exactly absent. The local obstruction they record is a nonzero near-null physical pivot.

The present report uses the stronger Fourier form (1.1), not merely the interval corollary.

## 2. Abstract chirp-stable slice compiler

Let `X` be independent of a pair `(L,Y)`. Assume `X` has a probability density `f` with `0<=f<=1`. Assume the law of `(L,Y)` admits the Lebesgue disintegration

`P{L in dl, Y in dy} = nu_l(dy) dl`,                             (2.1)

where each `nu_l` is a finite positive measure and

`int_R nu_l(R) dl = 1`.                                        (2.2)

Let `H:R->R` be any measurable real function finite almost surely. No boundedness, growth, moment, or regularity condition is imposed on `H`.

Assume that for some `A>0`, for every `t!=0`,

`ess sup_l |hat(nu_l)(t)| <= A |t|^(-1/2)`.                    (2.3)

Define

`T = H(X) + 2 X L + Y`.                                        (2.4)

### Theorem `QFORM-CHIRP-SLICE-L2-COMPILER-v1`

For every `t!=0`,

`boxed:
|phi_T(t)| <= K |t|^(-3/4),
K = sqrt(pi A).`                                                (2.5)

Consequently `T` has an `L^2` density and

`boxed:
||p_T||_2 <= sqrt(3/pi) K^(2/3).`                              (2.6)

In particular, both conclusions are completely independent of the one-variable phase `H`. Thus an arbitrary term `aX^2+rX+s`, with `a` arbitrarily close to zero or arbitrarily large, costs nothing in this `L^2` compiler.

### Proof

For fixed `t!=0`, put

`G_t(l) = int_R f(x) exp(i t H(x)) exp(2 i t l x) dx`.          (2.7)

This is the Fourier transform, evaluated at frequency `2tl`, of the function

`g_t(x)=f(x) exp(i t H(x))`.

Multiplication by the chirp `exp(i t H(x))` is unimodular. With Fourier convention `hat g(xi)=int g(x)e^{i xi x}dx`, Plancherel gives the exact identity

`int_R |G_t(l)|^2 dl
 = (1/(2|t|)) int_R |hat(g_t)(xi)|^2 dxi
 = (pi/|t|) int_R f(x)^2 dx
 <= pi/|t|,`                                                    (2.8)

because `f^2<=f` and `int f=1`.

Write

`A_t(l)=hat(nu_l)(t)`.

Positivity of `nu_l` gives

`|A_t(l)| <= nu_l(R)`,                                         (2.9)

hence by (2.2)

`||A_t||_1 <= 1`.                                              (2.10)

Combining (2.3) and (2.10),

`||A_t||_2^2 <= ||A_t||_infinity ||A_t||_1
 <= A |t|^(-1/2).`                                             (2.11)

Independence of `X` from `(L,Y)`, followed by the disintegration (2.1), gives the exact characteristic-function identity

`phi_T(t)=int_R G_t(l) A_t(l) dl`.                              (2.12)

Cauchy-Schwarz, (2.8), and (2.11) yield

`|phi_T(t)|
 <= (pi/|t|)^(1/2) (A |t|^(-1/2))^(1/2)
 = sqrt(pi A) |t|^(-3/4),`                                     (2.13)

which is (2.5).

Together with the trivial `|phi_T(t)|<=1`, set `t_0=K^(4/3)`. Then

`int_R |phi_T(t)|^2 dt
 <= 2 [ t_0 + K^2 int_(t_0)^infinity t^(-3/2) dt ]
 = 6 K^(4/3).`                                                  (2.14)

Thus `phi_T in L^2`. By Plancherel and uniqueness of Fourier transforms of finite measures, `T` has an `L^2` density and

`||p_T||_2^2
 = (1/(2pi)) ||phi_T||_2^2
 <= (3/pi) K^(4/3),`                                           (2.15)

which proves (2.6). QED.

### Localization content

The proof never truncates `X`, never chooses a support center, and never normalizes fragments. An arbitrary shift of `X` is absorbed into `H` and the linear coefficient, while the identity (2.8) is unchanged. Arbitrarily distant or countably fragmented support is therefore paid with exactly zero support/tail/moment tax. This is the relevant B14 feature: the potentially dangerous self-quadratic pivot is treated as a unimodular chirp on the whole original law rather than as a small random error.

## 3. Equation-level application of account04/B14 r9

Return to the partner normal form and now add an **arbitrary one-variable hub phase**:

`Q_H = H_0(X_0) + 2 X_0 (hV+q_0) + Y_g`,                       (3.1)

where `H_0` is any measurable real function. This includes, in particular,

`H_0(x)=a x^2+r x+s`                                            (3.2)

with no restriction on `a,r,s`.

Set

`L=hV+q_0`.

If `nu_l` denotes the unnormalised law of `Y_g` on `L=l`, the change of slice coordinate gives

`nu_l = |h|^(-1) mu_{(l-q_0)/h,g}`.                            (3.3)

Applying the partner inequality (1.1) to this **actual slice measure** gives

`ess sup_l |hat(nu_l)(t)|
 <= [4 sqrt(pi)/( |h| sqrt(|gamma|) )] |t|^(-1/2).`             (3.4)

Thus Theorem 2 applies with

`A = 4 sqrt(pi)/( |h| sqrt(|gamma|) )`                          (3.5)

and therefore

`boxed:
|phi_(Q_H)(t)|
 <= [2 pi^(3/4)/(sqrt(|h|) |gamma|^(1/4))] |t|^(-3/4).`         (3.6)

Writing

`K_* = 2 pi^(3/4)/(sqrt(|h|) |gamma|^(1/4)),`                  (3.7)

we obtain the whole-support quantitative conclusion

`boxed:
||p_(Q_H)||_2
 <= sqrt(3/pi) K_*^(2/3).`                                     (3.8)

This is a genuine use of account04/B14 r9 at an equation: its slice-Fresnel bound (3.6 in their report) is substituted into the exact Plancherel compiler above.

At the partner's unit active scale, `|b|>=1`, `c>1/2`, `|gamma|>=1`, so `|h|=|b|sqrt(c)>1/sqrt(2)`. Hence

`K_* < 2 pi^(3/4) 2^(1/4) = 5.6124165822...`                   (3.9)

and

`boxed:
||p_(Q_H)||_2 < 3.0862.`                                       (3.10)

The coefficient of `X_0^2` can tend to zero through arbitrary nonzero values without changing (3.6)-(3.10). No support radius appears, so there is no hidden `|a|R^2` truncation error.

Scope warning: (3.8) is an `L^2` density estimate, not the target `L^infinity` estimate. Moreover, an arbitrary physical rank-one perturbation of the exact-null normal form need not remain an exact-rank-three matrix. The statement here is therefore a supporting analytic theorem, not a solution of the partner's entire near-null structural branch.

## 4. The half-Hölder slice data alone cannot yield L-infinity after a hub chirp

The loss from the partner's null-hub `L^infinity` theorem to the chirp-stable `L^2` theorem is not merely an artifact of Cauchy-Schwarz. The following compact product example shows that **uniform `1/2`-Hölder slice control alone is insufficient** once a quadratic hub self-phase is admitted.

Let `X,L,W` be independent `Uniform[-1/2,1/2]` variables and define

`Y=L^2-W^2`.                                                    (4.1)

For fixed `l`, the unnormalised slice law of `Y` is the translate of `-W^2`. For every interval `I` of length `epsilon`,

`nu_l(I) <= 2 sqrt(epsilon)`.                                  (4.2)

Indeed `W^2` has density `s^(-1/2)` on `(0,1/4)`, and the mass of any interval of length `epsilon` is at most its mass adjacent to zero, namely `2sqrt(epsilon)`.

Now take

`T=X^2+2XL+Y=(X+L)^2-W^2`.                                    (4.3)

Put `U=X+L`. Then `U` and `W` are independent and

`p_U(u)=1-|u|` for `|u|<=1`.                                   (4.4)

For `0<s<1/4`, the density of `U^2` is

`p_(U^2)(s)=(1-sqrt(s))/sqrt(s) >= (1/2)s^(-1/2),`             (4.5)

whereas

`p_(W^2)(s)=s^(-1/2)`.                                         (4.6)

Therefore the density of `U^2-W^2` at zero has the lower bound

`int_0^(1/4) p_(U^2)(s) p_(W^2)(s) ds
 >= (1/2) int_0^(1/4) ds/s
 = infinity.`                                                   (4.7)

So the output density is logarithmically unbounded at zero despite the uniform slice estimate (4.2), compact supports, and cap-one independent source variables.

The same slices also have the standard Fresnel modulus bound `|hat(nu_l)(t)| <= C min(1,|t|^(-1/2))` for a universal finite `C`; the phase factor `e^{it l^2}` does not change the modulus. Thus a proof of the near-null `L^infinity` branch cannot use only the magnitude information contained in the partner's slice `|t|^(-1/2)` estimate. It must retain an additional determinant/transversality relation between the hub quadratic curvature and the moving slice phase, or a stronger product-preserving joint estimate.

This example is **not** a counterexample to QFORM: the matrix of (4.3) on `(X,L,W)` is

`[[1,1,0],[1,1,0],[0,0,-1]]`,                                  (4.8)

whose nonzero eigenvalues are `2,-1`; it has only two eigenvalues of modulus at least one. It refutes only the proposed *interface* “half-Hölder slice control plus arbitrary hub chirp implies bounded density.”

## 5. What this changes in the proof search

The partner's latest exact-null theorem should not be extended to a nonzero pivot by truncating the hub, calling `aX_0^2` a small error, or using only the slice half-Hölder constant. Those approaches either introduce a forbidden support scale or are defeated by Section 4.

The positive replacement is precise:

1. an arbitrary hub self-phase is completely free at the `L^2` level by whole-law Plancherel;
2. the remaining target-level gap is now to gain **any additional quarter-power of integrable time decay** from the determinant/transversality relation that is absent in the rank-two endpoint example (4.8), while preserving the product structure;
3. equivalently, one may seek a joint slice-energy/phase estimate stronger than the magnitude-only pair `(||hat nu_.(t)||_1, ||hat nu_.(t)||_infinity)` used in Section 2.

This is a narrower obstruction than “unbounded support makes a small pivot unusable”: unbounded support itself is no longer the issue for the hub phase. The issue is the endpoint correlation between the quadratic hub critical curve and the slice phase.

## 6. Full-target status

The exact owner target remains OPEN / not proved / not disproved. The new result proves absolute continuity with an `L^2` density for the stated chirped heavy-null slice-Fresnel family, but does not prove an essentially bounded density there for arbitrary `H_0`, and does not prove continuity. No claim is made beyond that scope.
