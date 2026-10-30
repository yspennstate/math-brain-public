SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-24T08:20:47Z.
attacking: the actual-modulation pivot Fourier endpoint left by r47. First test whether averaging the exact shifted scalar Fresnel kernel before using residual phase can possibly be L1; when that fails, preserve the failure as a source-valid exact-target witness and continue the bounded-density route by a physical twist-cover conditioning receiver built from the completed fleet02/B02 theorem.

# fleet01/B02 — actual-modulation absolute-majorant obstruction and twist-cover receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **ESSENTIAL_STEP_APPLIED_WITH_COUNTEREXAMPLE / NEW BOUNDED-DENSITY RECEIVER / FULL QFORM OPEN / TARGET-WIDE FOURIER-L1 OPEN_NOT_REFUTED**  
Regularity: the twist-cover Fourier subbranch gives a continuous `C0` density; the broad twist-cover density branch gives essential boundedness only.  
Brain status: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, iid, log-concavity, post-rotation independence, or deletion of a small nonzero coefficient is used.

## 1. Fresh source boundary and designated partner

Fresh `math-research-brain/main` was resolved at startup. The effective owner control remains revision `2026-09-22.15`, QFORM-only. `AGENTS.md`, the full `scheduled_tasks/README.md`, programme `MANIFEST.json`, `CURRENT_RESEARCH.md`, `CLAIMS.json`, live `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, and `assignments/fleet01/B02.json` were read. The live corrections against law-uniform pointwise quadratic decay, arbitrary-joint coarea, conditional projection caps/moments, post-rotation independence, and absolute-value-before-cancellation shortcuts are retained.

The immediate B02 predecessor is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T072000Z-fleet01-B02-qform-auto11-r47/REPORT.md`.

On its live literal full physical cut `N=A[L,R]`, with `L union R=[n]`, the two largest squared singular values satisfy

`x1*x2 > kappa :=247/576`.                                             (1.1)

Its diagonal-pivot branch has an ORIGINAL coordinate `h` with `|A_hh|>1/228`; the residual-Schur-E2 arm is already paid, while the remaining incident/cancellation packets require a proof that keeps the overlap and both bank twists.

The newest completed designated partner available at startup is fleet02/B02 auto12,

`yspennstate/math-open-problems@19a3d60ceb5d0989aa527b32d3e76f388b9419f6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260924T060210Z-fleet02-B02-QFORM-auto12/REPORT.md`.

Two partner theorems are used below.

1. `QFORM-RANK2-ONEBANK-LINEAR-DENSITY-v1`: if a literal original-coordinate crossing `M` has top two singular values `s1>=s2>0`, arbitrary same-bank curvature is retained on one bank, and the opposite bank is exactly untwisted after conditioning other ORIGINAL coordinates, then

`||p_Q||_infinity <=2 sqrt(pi) (s1 s2)^(-1/2)`.                    (1.2)

2. `QFORM-FULL2X2-ONESIDED-TWIST-L1-v1`: for a literal invertible physical `2x2` crossing `C`, with one bank exactly untwisted and arbitrary curvature on the other,

`integral |phi_Q(t)| dt <=16 pi sqrt(60) |det C|^(-1/2)`,           (1.3)

and independently `||p_Q||_infinity<=2|det C|^(-1/2)`. The Fourier conclusion gives a continuous `C0` density.

## 2. The first essential test: can the actual pivot modulation be averaged after absolute value?

For a scalar square pivot, after completing the square one encounters the exact shifted Fresnel kernel

`G_f(t,m) := integral_R f(x) exp(i t (x+m)^2) dx`.                 (2.1)

A tempting replacement for the already-refuted worst-modulation supremum is to keep the **actual** modulation law and seek a bound

`integral_R E_M |G_f(t,M)| dt <= C`,                               (2.2)

at least when `f` and the modulation density are cap-one probabilities. The next theorem shows that (2.2) is false in the strongest elementary sense: no fragmented support is needed, and the modulation can itself be an independent connected-support cap-one variable.

### Theorem 2.1 — `QFORM-PIVOT-ABS-ACTUAL-MODULATION-L1-FALSE-v1`

Let

`f=1_[0,1]`, `M ~ Uniform[1,2]`,

and

`G(t,m)=integral_0^1 exp(i t (x+m)^2) dx`.                          (2.3)

Then for every `t>=12` and every `m in [1,2]`,

`boxed: |G(t,m)| >= 1/(24 t).`                                     (2.4)

Consequently

`boxed: integral_12^infinity E |G(t,M)| dt = infinity.`            (2.5)

Both densities in this statement are probability densities bounded by one and have connected compact support.

#### Proof

Put `y=x+m`. Twice integrating by parts, using

`d exp(i t y^2)=2 i t y exp(i t y^2) dy`,

gives

`G(t,m)
 = [exp(i t y^2)/(2 i t y)]_(m)^(m+1)
   +(1/(2 i t)) J(t,m)`,                                           (2.6)

where

`J(t,m)=integral_m^(m+1) exp(i t y^2) y^(-2) dy`

and

`J(t,m)
 = [exp(i t y^2)/(2 i t y^3)]_(m)^(m+1)
   +(3/(2 i t)) integral_m^(m+1) exp(i t y^2)y^(-4)dy`.             (2.7)

For `m in[1,2]`,

`|J(t,m)|
 <= (1/(2t))(1+1/8)+(3/(2t)) integral_1^2 y^(-4)dy
 =9/(16t)+7/(16t)
 =1/t`.                                                             (2.8)

Hence the second term in (2.6) has modulus at most `1/(2t^2)`. For the boundary term, reverse triangle inequality gives

`| [exp(i t y^2)/(2 i t y)]_m^(m+1) |
 >=(1/(2t))(1/m-1/(m+1))
 =1/(2t m(m+1))
 >=1/(12t)`.                                                        (2.9)

Thus

`|G(t,m)| >=1/(12t)-1/(2t^2) >=1/(24t)`                            (2.10)

for `t>=12`. Integrating (2.10) proves (2.5). QED.

This is stronger than the previous maximal-modulation obstruction in one important respect: the modulation here is not chosen adversarially as a function of `t`. It has one fixed, honest cap-one probability law. Therefore an integrated-Fourier proof at the pivot cannot take absolute values immediately after the scalar Fresnel integral and hope that averaging the actual modulation density alone repairs the critical `1/t` boundary tail.

## 3. Exact-target embedding: the failed majorant can diverge while the true Fourier integral is finite

The preceding obstruction is not a counterexample to the owner target and not a counterexample to target-wide Fourier `L1`. This can be seen inside an exact target matrix.

Let the four original coordinates be `(H,Y,Z1,Z2)` and set

`A = [[1,1,0,0],
      [1,1,0,0],
      [0,0,1,0],
      [0,0,0,1]]`.                                                  (3.1)

Then

`Q=(H+Y)^2+Z1^2+Z2^2`,                                              (3.2)

and

`spec(A)={2,1,1,0}`.                                                (3.3)

Thus (3.1) satisfies the exact owner spectral hypothesis. Take

`H~Uniform[0,1]`, `Y~Uniform[1,2]`, `Z1,Z2~Uniform[0,1]`,

all independent. If the `H` pivot is integrated first and absolute value is taken before averaging `Y`, the resulting majorant is exactly (2.5), hence infinite.

Nevertheless the **true** characteristic function is in `L1`. Indeed `S=H+Y` is independent of `(Z1,Z2)`, and its density is a convolution of two cap-one probability densities, hence is itself bounded by one. For any cap-one real probability density `f`, the density `g` of `W^2` obeys

`g(u)=[f(sqrt(u))+f(-sqrt(u))]/(2 sqrt(u)), u>0`,                   (3.4)

and

`||g||_(3/2) <=2`.                                                  (3.5)

To see (3.5), use `(a+b)^(3/2)<=sqrt(2)(a^(3/2)+b^(3/2))<=sqrt(2)(a+b)` and the bathtub bound

`integral f(x)|x|^(-1/2)dx <= integral_(-1/2)^(1/2)|x|^(-1/2)dx
                              =2sqrt(2)`.                           (3.6)

With the Fourier convention `hat g(t)=integral exp(i t u)g(u)du`, Riesz-Thorin/Hausdorff-Young gives

`||hat g||_3 <=(2 pi)^(1/3)||g||_(3/2)
             <=2(2 pi)^(1/3)`.                                     (3.7)

Applying (3.7) to the independent cap-one variables `S,Z1,Z2` and Holder yields

`boxed: integral_R |phi_Q(t)|dt <=16 pi.`                           (3.8)

Thus the exact same target witness has an **infinite absolute conditional-pivot majorant** but a finite true Fourier `L1` norm. The only conclusion is about proof order: the remaining curvature/residual phase must be used before the decisive absolute value.

## 4. Continue on bounded density: a physical twist-cover conditioning receiver

The failed majorant in Section 2 does not block direct bounded-density progress. The partner theorem can be extended, without changing its analytic content, to banks carrying arbitrary same-bank curvature on a physical set that can be conditioned away while a robust rank-two crossing survives.

### Definition 4.1 — physical twist cover

Split original coordinates into disjoint banks `I,J` and the remaining coordinates `W`. Write `U=X_I`, `V=X_J`, and let `D=A[J,J]` be the same-bank quadratic coefficient on `J`. A set `S subset J` is a **physical twist cover** if, with `T=J\S`,

`D[T,T]=0`.                                                         (4.1)

No coefficient touching `S` is deleted; those coordinates will be conditioned.

### Theorem 4.2 — `QFORM-TWIST-COVER-CONDITIONING-RECEIVER-v1`

Let `S` be a physical twist cover and put

`M_T=A[I,T]`.                                                        (4.2)

If the top two singular values of `M_T` satisfy

`s1(M_T)s2(M_T) >= rho>0`,                                         (4.3)

then the full ambient law has an essentially bounded density with

`boxed: ||p_Q||_infinity <=2 sqrt(pi) rho^(-1/2).`                  (4.4)

Moreover, if there are literal rows `i1,i2 in I` and literal columns `j1,j2 in T` for which

`Delta=|det A[{i1,i2},{j1,j2}]|>0`,                                (4.5)

then independently

`boxed: integral_R |phi_Q(t)|dt <=16 pi sqrt(60) Delta^(-1/2),`     (4.6)

`boxed: ||p_Q||_infinity <=2 Delta^(-1/2),`                         (4.7)

and the density is continuous and vanishes at infinity.

#### Proof

Condition on every coordinate in `W` and on `V_S`. Because `D[T,T]=0`, the remaining `V_T` variables have **no same-bank quadratic term**. All `S-T` terms become affine terms in `V_T`, all `I-S` terms are absorbed into the arbitrary function of `U`, and the literal crossing from `U` to `V_T` remains exactly `M_T`. Therefore the completed partner theorem (1.2) applies conditionally with the same deterministic constant. Mixing conditional densities proves (4.4).

For (4.6), condition further on every `U` coordinate except `i1,i2` and every `V_T` coordinate except `j1,j2`. The two surviving `V` coordinates are still exactly untwisted, while the two surviving `U` coordinates retain arbitrary quadratic/affine curvature. The crossing is the literal `2x2` matrix in (4.5). Apply the partner Fourier theorem (1.3) conditionally. Since

`|phi_Q(t)| <= E_conditioning |phi_(Q|conditioning)(t)|`,

Tonelli transfers the uniform conditional `L1` bound to the full characteristic function, proving (4.6). Fourier inversion gives the `C0` conclusion. The direct conditional height theorem gives (4.7). QED.

This theorem retains every original coefficient. It does not call a small nonzero twist zero; it conditions the physical coordinates that actually carry the twist.

## 5. Actual inequality on the live r47 crossing

The required equation-level application of fleet02/B02 is to the live full cut (1.1). There

`s1(N)s2(N)=sqrt(x1*x2)>sqrt(kappa)`, `kappa=247/576`.              (5.1)

The partner's exact-untwisted case (`S=emptyset`) gives again

`boxed: ||p_Q||_infinity
 <2 sqrt(pi) kappa^(-1/4)
 =4.380627393... .`                                                (5.2)

The twist-cover extension strictly enlarges this paid chamber. If either bank has a physical twist cover `S` whose removal leaves

`s1(M_T)s2(M_T) >= (1/2)sqrt(kappa)`,                              (5.3)

then

`boxed: ||p_Q||_infinity
 <=2 sqrt(2 pi) kappa^(-1/4)
 =6.195142671... .`                                                (5.4)

Therefore every still-unpaid **two-sided-twisted** survivor may be sharpened further: on both sides, no physical twist cover satisfying (4.1) can be conditioned away while retaining even half of the live rank-two singular-product currency. Equivalently, both bank twists are rank-two-essential at this scale. If, on an untwisted complement, a physical `2x2` minor also has `Delta` bounded below, (4.6) immediately upgrades that subbranch to genuine Fourier `L1` and continuity.

This is a bounded-density continuation after the Section 2 Fourier-majorant failure; it does not claim that every two-sided twist has such a cover.

## 6. Corrected frontier

The target-wide universal unweighted estimate

`integral_R |E exp(i t X^T A X)|dt <= C`                            (6.1)

remains `OPEN_NOT_REFUTED`. The new counterexample is to the **stronger proof criterion** obtained by taking absolute value after the scalar pivot Fresnel integral and then averaging only the actual modulation law.

The first unpaid B02 interface is now

`QFORM-PIVOT-RESIDUAL-PHASE-BEFORE-ABS-v1`:

on the r47 incident/cancellation packets, after excluding the twist-cover payments of Section 5, combine the exact residual phase with the shifted-pivot kernel **before** taking the decisive absolute value. Any successful proof must use the conserved incident `E2`/two-sided cancellation currency jointly with the pivot. The calculation in Section 3 shows that discarding the residual phase first can create a logarithmic divergence even on a benign exact-target law whose true characteristic function is uniformly integrable.

Full bounded density remains **OPEN**. Full-target continuity remains **OPEN**. The new twist-cover branches establish essential boundedness, and the physical-`2x2` subbranch establishes continuous `C0` density.

## 7. Correction audit

This run does not use:

- law-uniform pointwise van-der-Corput/Fresnel decay;
- post-rotation independence;
- arbitrary-joint coarea bounds;
- conditional projection-density caps or positive conditional-density moments;
- worst-modulation maximal estimates;
- deletion of a nonzero quadratic tail;
- Monte Carlo or interval extremality.

The obstruction uses literal cap-one connected-support input densities, and the receiver uses only conditioning on literal original coordinates.

MODEL: GPT-5.6 Sol. Configured thinking level / provider reasoning counters: UNKNOWN / not exposed.
