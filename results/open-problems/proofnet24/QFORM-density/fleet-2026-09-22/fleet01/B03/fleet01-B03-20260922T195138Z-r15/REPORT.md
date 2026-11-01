SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B03, 2026-09-22T19:51:38Z.
attacking: translation-uniform fractional-trace synthesis from the partner's affine physical-triple clamp, plus the exact exponent range of the dependence-safe square-collision time integral.

# fleet01/B03 r15 — fractional-trace synthesis after a physical pivot and all-exponent square-collision energy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Control revision consumed before publication: `2026-09-22.15`  
Assignment: Decoupled time integral  
Classification: **ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN**  
Continuity: **not proved by the new branch**  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and correction discipline

The full target remains open: for every dimension, independent real original-coordinate inputs with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal essential-density bound for `Q=X^T A X`, or give a target-valid counterexample.

No Gaussian, moment, support, log-concavity, connected-support, diagonal-basis, or post-rotation-independence assumption is used. This report does not use the refuted law-uniform pointwise Fresnel decay, the false conditional cap for a sum/difference conjugate pair, the false arbitrary-joint rank-three coarea inequality, the false positive conditional-projection-density moment, the false single-Schur-rank-two extraction, or a fixed-good-minor dichotomy.

The new step is a translation-uniform fractional-trace synthesis in original coordinates. It also determines the exact exponent range in which the B03 square-collision independent-copy energy is universally finite.

## 2. Named partner result actually consumed

The required partner is fleet02/B03. I consumed its latest complete report at

`yspennstate/math-open-problems@cdd5c5a373f3e5a9d4a38fbde390141d1d2c81d5`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260922T183916Z-fleet02-B03-QFORM-r13/REPORT.md`.

Its theorem `QFORM-AFFINE-PHYSICAL-N3-CLAMP-v1` says the following. Let three independent cap-one variables form `Y in R^3`, let `B` be a real symmetric `3x3` matrix with

`sigma_min(B)>=s>0`,

and allow arbitrary affine coefficients. Then

`||p_(Y^T B Y + ell^T Y + c)||_infinity <= C3/s`,

where

`C3 = 128*2^(1/4)`.                                                   (2.1)

The theorem is uniform in the affine term. Therefore, after conditioning all other ORIGINAL coordinates, it also applies to a physical principal triple inside an arbitrary ambient quadratic form.

I apply (2.1) below to an actual full-dimensional Schur residual and then feed its density cap into the half-Riesz time/potential transducer. This is not merely a citation.

## 3. A density cap gives the sharp fractional-potential budget

### Lemma 3.1 — bathtub fractional potential

Let `R` have probability density `g` with `0<=g<=M`. For every `0<alpha<1`,

`sup_z E |R-z|^(-alpha) <= [2^alpha/(1-alpha)] M^alpha`.             (3.1)

Proof. For fixed `z`, the kernel `|x-z|^(-alpha)` is symmetric decreasing. Among densities of mass one and cap `M`, the bathtub principle places density `M` on the centered interval of length `1/M`. Hence

`E|R-z|^(-alpha)`
` <= M int_{-1/(2M)}^(1/(2M)) |u|^(-alpha) du`
` = [2^alpha/(1-alpha)]M^alpha`.

At `alpha=1/2`,

`sup_z E|R-z|^(-1/2) <= 2 sqrt(2M)`.                                (3.2)

This elementary endpoint is the exact interface needed after one physical square pivot.

## 4. Main new synthesis: one physical pivot plus a good Schur triple

Let `A` be any real symmetric `n x n` matrix and select an ORIGINAL coordinate `i` with

`a=A_ii !=0`.

Write the physical block decomposition

`A = [[a, v^T],[v,B]]`,

and let

`S=B-vv^T/a`                                                        (4.1)

be the full Schur complement on the remaining original coordinates. Suppose there exists an ORIGINAL-coordinate triple `J` among those remaining coordinates such that

`sigma_min(S[J,J]) >= s>0`.                                         (4.2)

No condition is imposed on the other entries of `S`, on `v`, on signs, dimension, or the rest of the spectrum.

### Theorem 4.1 — `QFORM-PIVOT-SCHUR-TRIPLE-FRACTIONAL-TRACE-v1`

Under (4.1)-(4.2), for arbitrary independent cap-one original-coordinate inputs,

`boxed{ ||p_(X^T A X)||_infinity
       <= 32*2^(1/8) (|a|s)^(-1/2)
       < 34.897 (|a|s)^(-1/2). }`                                  (4.3)

This proves essential boundedness in this branch. The argument below does not by itself prove continuity.

### Proof

Let `Z=X_i` and let `W` collect all remaining original coordinates. Exact completion of the physical square gives

`Q = a [Z+a^(-1)v^T W]^2 + R(W)`,                                  (4.4)

where

`R(W)=W^T S W`.                                                     (4.5)

If the original problem includes an affine term, exactly the same computation only changes the shift in the square and adds an arbitrary affine term to `R`; the proof below is unchanged.

By (4.2), the partner theorem (2.1), applied to the residual matrix `S`, gives the ACTUAL inequality

`||p_R||_infinity <= C3/s`.                                         (4.6)

Indeed, condition on every residual coordinate outside `J`. The three coordinates in `J` remain independent with cap one, while all conditioned couplings produce only an affine term, precisely the scope covered by the partner theorem. Averaging preserves (4.6).

Conditional on `W`, the shift

`h(W)=a^(-1)v^T W`

is deterministic and `Z+h(W)` is still a translate of the original cap-one variable `Z`. The density of `a(Z+h)^2` is bounded by

`|a|^(-1/2)|y|^(-1/2)`

on the appropriate half-line. Therefore for almost every `t`,

`p_Q(t) <= |a|^(-1/2) E |t-R|^(-1/2)`.                             (4.7)

Apply (3.2) to (4.6):

`sup_t E|t-R|^(-1/2)
 <=2 sqrt(2 C3/s)`.

Since `C3=128*2^(1/4)`,

`2 sqrt(2 C3)=32*2^(1/8)`,

which proves (4.3). QED.

### Why this is not just the old good-4x4-principal-block criterion

The Schur triple can remain perfectly conditioned while the corresponding physical `4x4` principal matrix becomes arbitrarily ill-conditioned because of a large cross vector `v`. For example

`A_L = [[1,L,0,0],
        [L,L^2+1,0,0],
        [0,0,1,0],
        [0,0,0,1]]`.                                                (4.8)

Pivoting the first coordinate gives Schur complement `S=I_3`, so (4.3) gives the uniform cap

`||p_Q||_infinity <34.897`                                          (4.9)

for every `L` and every admissible product law. But the least singular value of the full `4x4` block tends to zero like `L^-2`, so a theorem paying `1/sigma_min(A_L)` deteriorates. This is the concrete gain of completing the physical square BEFORE applying the partner triple clamp.

The family (4.8) itself satisfies the target spectral premise for every `L`: it has two exact eigenvalues `1` and the `2x2` leading block has determinant one and one eigenvalue at least one. Thus there are at least three eigenvalues of modulus at least one. This is a supporting target family, not the unrestricted theorem.

## 5. New all-exponent independent-copy square-collision theorem

The preceding run proved the `alpha=1/2` square-collision energy by retaining the exact dependent product

`|(X-X')(X+X')|=|X^2-X'^2|`

before absolute-value factorization. Here I extend that estimate to its full exponent range and identify the sharp endpoint failure.

Let `X` have density cap `M`, let `X'` be an iid copy, and let `h` be arbitrary. Put

`D_h=|(X-h)^2-(X'-h)^2|`.

Translation preserves the cap, so the previous geometric section argument gives, after scaling to cap one, for `0<epsilon<=1`,

`P(D_h<=epsilon)
 <=4 sqrt(2) epsilon
   +8 epsilon log(1+1/(2 sqrt(epsilon)))`.                           (5.1)

For cap `M`, scaling `Y=M(X-h)` multiplies `D_h^(-alpha)` by `M^(2alpha)`.

For `0<alpha<1`, define

`m_alpha=2(1-alpha)`,

`J_alpha=int_0^1 r^(m_alpha-1)/(1+2r) dr`,                          (5.2)

and

`C_alpha = 1
 + [4 sqrt(2) alpha/(1-alpha)]
 + [8 alpha/(1-alpha)] [log(3/2)+J_alpha].`                         (5.3)

### Theorem 5.1 — `QFORM-SQUARE-COLLISION-RIESZ-ALL-ALPHA-v1`

For every `0<alpha<1`, every translation `h`, and every density cap `M`,

`boxed{ E D_h^(-alpha) <= C_alpha M^(2alpha). }`                    (5.4)

Proof. It suffices to take `M=1`. Layer cake gives

`E D_h^(-alpha)
 = alpha int_0^infinity epsilon^(-alpha-1)
           P(D_h<epsilon) d epsilon`.

The part `epsilon>=1` is at most one. Use (5.1) on `(0,1)`. The linear term contributes

`4 sqrt(2) alpha/(1-alpha)`.

For the logarithmic term we need

`I_alpha=int_0^1 epsilon^(-alpha)
                 log(1+1/(2sqrt(epsilon))) d epsilon`.

With `r=sqrt(epsilon)` and one integration by parts,

`I_alpha
 = [log(3/2)+J_alpha]/(1-alpha)`.                                  (5.5)

Substitution gives (5.3)-(5.4). Scaling gives the general `M` case. QED.

At `alpha=1/2`, `J_alpha=(1/2)log 3` and (5.3) becomes exactly the preceding-run constant

`C_(1/2)=1+4sqrt(2)+8[log(3/2)+(1/2)log3]`
`       =14.2950242690...`.                                         (5.6)

Thus Theorem 5.1 genuinely extends the earlier half-Riesz result rather than changing its normalization.

## 6. Exact weighted time-integral form

For

`psi_(a,h)(t)=E exp(i t a (X-h)^2)`,

independent copying gives

`|psi_(a,h)(t)|^2
 =E exp(i t a[(X-h)^2-(X'-h)^2])`.                                 (6.1)

The standard one-dimensional Riesz identity, justified by Abel regularization and (5.4), yields for every `0<alpha<1`,

`boxed{
 int_R |t|^(alpha-1)|psi_(a,h)(t)|^2 dt
 <= 2 Gamma(alpha) cos(pi alpha/2)
    C_alpha M^(2alpha)|a|^(-alpha).
}`                                                                 (6.2)

This is uniform in the translation `h`, arbitrary support fragmentation, and the input law. It is exactly an integrated independent-copy estimate; no pointwise oscillatory decay is claimed.

For `alpha=1/2`, (6.2) reduces to

`int_R |t|^(-1/2)|psi_(a,h)(t)|^2 dt
 <= sqrt(2pi) C_(1/2) M |a|^(-1/2)`,                               (6.3)

recovering the previous B03 theorem, now translation-uniform explicitly.

## 7. The exponent alpha<1 is sharp for this collision mechanism

One cannot extend (5.4) to `alpha=1` uniformly, or even for a single benign cap-one law. Let

`X ~ Uniform[-1/2,1/2]`.

On the positive square `[1/4,1/2]^2`,

`|x^2-y^2|=(x+y)|x-y| <= |x-y|`,

because `x+y<=1`. Hence

`int_[1/4,1/2]^2 |x^2-y^2|^(-1) dx dy
 >= int_[1/4,1/2]^2 |x-y|^(-1) dx dy
 = infinity`.                                                       (7.1)

Therefore

`E|X^2-X'^2|^(-1)=infinity`.                                        (7.2)

So the universal square-collision Riesz energy has the exact exponent range `0<alpha<1`; the endpoint `alpha=1` fails. Equivalently, a proof cannot obtain the missing unweighted `L^2` time integrability of a single square by simply pushing this collision identity to its endpoint. Additional independent/grouped curvature is genuinely necessary.

This is an explicit refutation of that intermediate endpoint mechanism, not a counterexample to QFORM.

## 8. What this changes and the first unpaid implication

The partner theorem plus Theorem 4.1 now pays any branch in which an original physical scalar pivot leaves a Schur residual containing a quantitatively nondegenerate original-coordinate principal triple. The bound is insensitive to arbitrary pivot-to-triple couplings before square completion; the example (4.8) shows why that is stronger than simply asking the original `4x4` principal block to be well conditioned.

The all-exponent collision theorem (5.4)-(6.2) also shows precisely what one square can supply to future time-integral splices: every fractional weight strictly below the unweighted endpoint is uniformly available, but the endpoint itself is impossible even for a uniform input.

The full theorem is still open. The first remaining implication is structural/product-preserving:

> Under only `s_3(A)>=1`, force an exhaustive universal alternative that yields either a direct ridge/cross-bank certificate, a physical pivot whose Schur residual has a good physical triple as in Theorem 4.1, or a grouped rank-one/star/hyperbolic packet whose independent coordinates can be aggregated before reciprocal local-minor payment.

The source-valid counterexamples to a universal single-Schur-rank-two extraction and to a principal-triple-or-cross-rank-three dichotomy remain binding. No such exhaustive structural implication is claimed here.

## 9. Status and provenance

New proved statements:

- `QFORM-PIVOT-SCHUR-TRIPLE-FRACTIONAL-TRACE-v1`, equation (4.3), with actual application of fleet02/B03 r13.
- `QFORM-SQUARE-COLLISION-RIESZ-ALL-ALPHA-v1`, equations (5.4) and (6.2).
- Sharp endpoint failure at `alpha=1`, equation (7.2), for this collision mechanism.

Full QFORM: **OPEN / not proved / not disproved**.  
Full-target continuous density: **OPEN**.  
Repository transport is not native learned-memory ingestion: **WITHOUT_VERIFIED_BRAIN**.

No numerical histogram or Monte Carlo evidence is used. All writes are private repository artifacts; no schedules, notifications, permissions, email, public releases, paid models, or remote workflows are changed by this report.
