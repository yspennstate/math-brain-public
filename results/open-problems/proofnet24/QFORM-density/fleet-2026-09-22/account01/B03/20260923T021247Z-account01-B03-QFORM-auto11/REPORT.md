SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T02:12:47Z.
attacking: rank-one product channel plus two aggregate square channels: a product-preserving L2-L4-L4 time splice, followed by the exact independent-copy half-Riesz energy.

# account01/B03 — product + two-square Fourier splice

Run: `20260923T021247Z-account01-B03-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control observed before publication: revision `2026-09-22.15`  
Assignment: decoupled time integral  
Status: `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Exact scope and source pins

The full target remains open: for arbitrary dimension, arbitrary independent real coordinates with one-dimensional densities bounded by one, and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal density cap for `X^T A X`, or give a valid target-level counterexample. Continuity is a separately desired conclusion.

Fresh control was resolved from `yspennstate/math-research-brain` main before publication; OWNER CONTROL remained revision `2026-09-22.15` and QFORM remained the sole research target. The live correction inbox was reread. In particular, no law-uniform pointwise quadratic-phase decay, no independence after spectral rotation, no conditional cap for conjugate sum/difference variables, no arbitrary-joint rank-three coarea lemma, and no fixed-good-minor structural assertion is used below.

The designated partner result actually used in an equation is account02/B03 run `20260922T150949Z-account02-B03-QFORM-r11`, canonical commit

`yspennstate/math-open-problems@f40d5d4f5013b0a6af275a19aa3dc0fa2d76c347`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T150949Z-account02-B03-QFORM-r11/REPORT.md`.

For independent cap-one real `U,V`, that report proves

`||p_(UV)||_2^2 <= 3 sqrt(3)`                                                (1.1)

and, separately, `||p_(UV)||_3 <= 2 sqrt(3)`. The present run uses (1.1) at the Fourier-Plancherel level. Its proof is product-preserving and its independent-copy interpretation does not condition a difference on its dependent conjugate sum.

A second completed source used only in the concrete bank example is account02/B04 commit

`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T181702Z-dac07509/REPORT.md`,

which records the one-dimensional product-projection cap

`||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`                                  (1.2)

for a linear projection of an original-coordinate product bank.

## 2. A translated square in `L^(4/3)`

The first input needed for the time splice is elementary and completely translation-uniform.

### Lemma 2.1 — square density `L^p` bound

Let `Y` have a probability density bounded by `M`, let `b` be arbitrary, let `lambda != 0`, and put

`S=lambda (Y-b)^2`.

For every `1<p<2`,

`||p_S||_p <= [2^(p-1)/(2-p)]^(1/p)
               M^(2-2/p) |lambda|^(-1+1/p).`                                (2.1)

In particular, at `p=4/3`,

`boxed( ||p_S||_(4/3)
        <= (3^(3/4)/sqrt(2)) M^(1/2)|lambda|^(-1/4). )`                       (2.2)

#### Proof

It is enough to take `lambda>0`; reflection of the output handles the other sign. For `r>0`, set

`F(r)=f_Y(b+r)+f_Y(b-r)`.

Then `0<=F<=2M` and

`int_0^infinity F(r) dr = 1`.                                                (2.3)

At `z=lambda r^2`, the pushforward density is

`p_S(z)=F(r)/(2 lambda r)`.

Therefore

`int |p_S(z)|^p dz
 =2^(1-p) lambda^(1-p)
   int_0^infinity F(r)^p r^(1-p) dr`.                                       (2.4)

The weight `r^(1-p)` is decreasing and locally integrable because `p<2`. Under the two constraints in (2.3), the bathtub/rearrangement principle maximizes the last integral by

`F=2M 1_[0,1/(2M)]`.

Hence

`int F(r)^p r^(1-p)dr
 <=(2M)^p [1/(2M)]^(2-p)/(2-p)
 =(2M)^(2p-2)/(2-p)`.                                                        (2.5)

Substitution in (2.4) gives (2.1). At `p=4/3`,

`[2^(1/3)/(2/3)]^(3/4)=3^(3/4)/sqrt(2)`,

which is (2.2). QED.

### Corollary 2.2 — square characteristic function in `L^4`

With the Fourier convention

`phi_S(t)=E exp(itS)`,                                                        (2.6)

Hausdorff-Young by interpolation between `L^1 -> L^infinity` and Plancherel gives

`||phi_S||_4 <= (2pi)^(1/4)||p_S||_(4/3)`.

Consequently

`boxed( ||phi_S||_4
 <= [6^(3/4) pi^(1/4)/2]
    M^(1/2)|lambda|^(-1/4). )`                                               (2.7)

No support, moment, regularity, connectedness, or log-concavity assumption appears.

## 3. Partner theorem gives the product channel in `L^2_t`

Let `A,B` be independent with density caps `M_A,M_B`, allow arbitrary deterministic translations `alpha,beta`, and let

`P=kappa(A+alpha)(B+beta)`, `kappa!=0`.

Scale

`U=M_A(A+alpha)`, `V=M_B(B+beta)`.

Then `U,V` are independent with densities at most one, and

`P=[kappa/(M_A M_B)]UV`.

Applying the designated account02/B03 result (1.1),

`||p_P||_2^2
 <=3 sqrt(3) |kappa|^(-1) M_A M_B`.                                        (3.1)

Plancherel gives the literal integrated time estimate

`boxed( ||phi_P||_2
 <= sqrt(6 pi sqrt(3))
    |kappa|^(-1/2)(M_A M_B)^(1/2). )`                                        (3.2)

Equivalently,

`|phi_P(t)|^2=E exp(it(P-P'))`,                                               (3.3)

and (3.2) is the finite two-copy collision integral. Nothing in (3.1)-(3.3) asserts independence of `A-A'` from `A+A'`, or of the analogous pair for `B`; the partner theorem retains the product source before the Plancherel payment.

## 4. New `L^2-L^4-L^4` Fourier splice

The next theorem is the main result of this run.

### Theorem 4.1 — `QFORM-PRODUCT-TWO-SQUARE-FOURIER-SPLICE-v1`

Let `A,B,C,D` be mutually independent real random variables with probability-density caps

`M_A,M_B,M_C,M_D`,

and let `W` be arbitrary outside data independent of those four variables. Let `alpha,beta,gamma,delta,R` be arbitrary measurable real functions of `W`. Let `kappa,lambda,mu` be nonzero real constants. Define

`T = kappa(A+alpha(W))(B+beta(W))
     +lambda(C+gamma(W))^2
     +mu(D+delta(W))^2
     +R(W).`                                                                 (4.1)

Then the characteristic function of `T` belongs to `L^1(R)` and

`boxed(
 int_R |phi_T(t)| dt
 <= 9*3^(1/4)*pi
    |kappa|^(-1/2)|lambda mu|^(-1/4)
    (M_A M_B M_C M_D)^(1/2).
 )`                                                                          (4.2)

Therefore `T` has a bounded continuous density and

`boxed(
 ||p_T||_infinity
 <= (9/2) 3^(1/4)
    |kappa|^(-1/2)|lambda mu|^(-1/4)
    (M_A M_B M_C M_D)^(1/2).
 )`                                                                          (4.3)

Numerically, the universal scalar constant in (4.3) is

`(9/2)3^(1/4)=5.922333058286216...`.                                         (4.4)

In particular every interval `I` satisfies the genuine linear small-ball estimate

`P(T in I) <= [(9/2)3^(1/4)
               |kappa|^(-1/2)|lambda mu|^(-1/4)
               (M_A M_B M_C M_D)^(1/2)] |I|`.                               (4.5)

#### Proof

Condition on `W=w`. The four active scalar sources remain mutually independent. Write the three conditional channels as

`P_w=kappa(A+alpha(w))(B+beta(w))`,

`S_w=lambda(C+gamma(w))^2`,

`Z_w=mu(D+delta(w))^2`.

Their conditional characteristic functions factor:

`phi_(T|w)(t)=e^(itR(w)) phi_(P_w)(t) phi_(S_w)(t) phi_(Z_w)(t)`.             (4.6)

The translated product estimate (3.2) is uniform in `w`. The square estimate (2.7) is also uniform in its translation. Therefore Holder in time with exponents `2,4,4` gives

`int |phi_(T|w)(t)|dt
 <= ||phi_(P_w)||_2 ||phi_(S_w)||_4 ||phi_(Z_w)||_4`.                         (4.7)

The constants multiply exactly as follows:

`sqrt(6 pi sqrt(3))
 * [(2pi)^(1/4)3^(3/4)/sqrt(2)]^2
 = 9*3^(1/4)*pi`.                                                            (4.8)

Thus (4.2) holds conditionally, uniformly in `w`. Unconditionally,

`|phi_T(t)|
 = |E_W phi_(T|W)(t)|
 <= E_W |phi_(T|W)(t)|`,                                                     (4.9)

so Tonelli and (4.7) give the same bound (4.2). Fourier inversion now supplies a bounded continuous density with

`||p_T||_infinity <= (2pi)^(-1)||phi_T||_1`,

which is precisely (4.3). Integrating that density over an interval gives (4.5). QED.

### Why this is a dependence-safe decoupled-time estimate

The only two-copy step is the product-channel `L^2_t` payment (3.2), sourced from the designated partner's exact collision theorem. The two square channels are paid in `L^4_t` through one-copy Hausdorff-Young. At no point do we write a conditional density for `X-X'` given `X+X'`. The complete time integral is performed before any physical coefficient is selected from a distributed bank.

This is qualitatively different from the refuted finite-coordinate Tonelli/Holder closure that separately normalizes every sum/difference slice: here the partner collision theorem has already aggregated the entire product channel into its physical scalar law, and the two independent square channels supply the remaining Fourier exponents globally.

## 5. Exact independent-copy half-Riesz energy for the new packet

The assignment also asks to retain the exact `|phi|^2` identity in an integrated estimate. Theorem 4.1 gives one immediately with a sharp elementary bathtub constant.

Let

`K=(9/2)3^(1/4)
   |kappa|^(-1/2)|lambda mu|^(-1/4)
   (M_A M_B M_C M_D)^(1/2)`.                                                 (5.1)

Then `||p_T||_infinity<=K`. For an independent copy `T'`, the difference density is

`p_(T-T')=p_T * tilde(p_T)`,

so

`||p_(T-T')||_infinity<=K`.                                                  (5.2)

Among probability densities bounded by `K`, the decreasing kernel `|x|^(-1/2)` is maximized by the centered bathtub `K 1_{|x|<=1/(2K)}`. Hence

`E |T-T'|^(-1/2) <= 2 sqrt(2K)`.                                             (5.3)

The exact one-dimensional Riesz identity is

`int_R |t|^(-1/2)|phi_T(t)|^2 dt
 =sqrt(2pi) E|T-T'|^(-1/2)`.                                                 (5.4)

Combining (5.1)-(5.4),

`boxed(
 int_R |t|^(-1/2)|phi_T(t)|^2 dt
 <= 6 sqrt(2pi) 3^(1/8)
    |kappa|^(-1/4)|lambda mu|^(-1/8)
    (M_A M_B M_C M_D)^(1/4).
 )`                                                                          (5.5)

The scalar constant in (5.5) is

`6 sqrt(2pi)3^(1/8)=17.2536642035361...`.                                    (5.6)

Equation (5.4) is literally the independent-copy identity at the requested fractional time weight. It keeps the law of `T-T'` intact; no dependent sum/difference pair is conditionally separated.

The logical direction should be kept clear. The linear small-ball bound is proved directly by the `L^1_t` estimate (4.2). Equation (5.5) is a compatible collision-energy certificate, not a claim that a negative-weight `L^2_t` integral alone implies an `L^infinity` density bound for an arbitrary law.

## 6. Aggregate target-family application: one star plus two square banks

The theorem pays a family in which every individual physical coefficient tends to zero, so selecting one local entry before aggregation loses the useful scale.

For `m>=2`, use four disjoint original-coordinate groups:

- one hub coordinate `X_0`;
- a bank `I` of `m` coordinates and `u=m^(-1/2)(1,...,1)`;
- a bank `J` of `m` coordinates and `v=m^(-1/2)(1,...,1)`;
- a bank `K` of `m` coordinates and `w=m^(-1/2)(1,...,1)`.

Set

`U=u^T X_I`, `V=v^T X_J`, `W0=w^T X_K`,

and consider

`Q_m = 2 a X_0 U + b V^2 + c W0^2`.                                         (6.1)

The corresponding symmetric matrix is the direct sum of the star block

`[[0, a u^T],[a u,0]]`

and the rank-one square blocks `b vv^T`, `c ww^T`. Its nonzero spectrum is exactly

`{+|a|,-|a|,b,c}`.                                                           (6.2)

Thus taking, for example,

`a=1`, `b=1`, `c=1/2`                                                        (6.3)

gives exactly three eigenvalues of modulus at least one and one additional eigenvalue of modulus `1/2`. This is a genuine instance of the full target with arbitrary extra smaller spectrum.

Every physical star coefficient is `a/sqrt(m)` and every entry in the two square banks is respectively `b/m` and `c/m`; hence all fixed local coefficients and fixed local minors collapse as `m` grows. The natural aggregate variables do not collapse.

By the completed projection theorem (1.2),

`||p_U||_infinity,
 ||p_V||_infinity,
 ||p_W0||_infinity <= sqrt(2)`.                                              (6.4)

Apply Theorem 4.1 to

`A=X_0`, `B=U`, `C=V`, `D=W0`,

with

`kappa=2a`, `lambda=b`, `mu=c`.

The cap factors and the coefficient `2` simplify to

`boxed(
 ||p_(Q_m)||_infinity
 <= (9/2)6^(1/4)
    |a|^(-1/2)|bc|^(-1/4).
 )`                                                                          (6.5)

This is uniform in `m`. At the exact-three-large choice (6.3),

`boxed( ||p_(Q_m)||_infinity
        <= (9/2)12^(1/4)
        = 8.375443731918896... . )`                                          (6.6)

Moreover `p_(Q_m)` is continuous. The corresponding weighted independent-copy energy obeys

`int |t|^(-1/2)|phi_(Q_m)(t)|^2 dt
 <=6 sqrt(2pi)3^(1/8) 2^(1/8)
   |a|^(-1/4)|bc|^(-1/8)`,                                                   (6.7)

and is likewise dimension-free.

This family is not claimed to be the remaining worst case. Its role is structural: one rank-one mixed star together with two independent aggregate square channels has a complete product-preserving Fourier closure even though no individual active physical coefficient remains at constant scale.

## 7. What this adds relative to the latest partner result

The latest account02/B03 run (`20260923T012658Z-account02-B03-QFORM-auto11`) pays a **rank-two** cross packet plus one aggregate square channel. The present theorem pays the complementary Fourier geometry

`rank-one product channel + two aggregate square channels`.

The two mechanisms use different exponent budgets:

- partner latest: a two-volume residual pays most of the half-Riesz endpoint and one square supplies the missing direction;
- present run: the partner's earlier exact product collision gives `L^2_t`, while two squares each give `L^4_t`, and `1/2+1/4+1/4=1` closes Fourier inversion exactly.

This is a literal analytic manifestation of the three-direction threshold in a nonseparable product-preserving packet.

## 8. First unpaid implication

The full QFORM theorem is still open. The first missing step is structural:

> Starting only from `s_3(A)>=1`, prove a dimension-free product-coordinate decomposition that yields either (i) an already-paid three-or-higher cross-volume/ridge packet, (ii) the partner's rank-two-cross plus aggregate-square packet, (iii) the present rank-one-product plus two-square packet, or (iv) another grouped packet that pays genuinely entangled in-bank quadratic curvature without selecting a tiny local minor first.

The known singleton-plus-two-banks and Walsh families show why a proof cannot simply demand one uniformly good fixed physical minor. The new result removes the Fourier obstruction once a rank-one mixed channel and two transverse square channels can be isolated on disjoint original-coordinate banks; it does **not** prove that the bare spectral hypothesis always supplies that decomposition.

## 9. Continuity and integrity statement

For Theorem 4.1 and the family (6.1), continuity **is proved**, because the full characteristic function belongs to `L^1`. For the unrestricted conjecture, both the universal density bound and the continuous-density conclusion remain open.

No Gaussianity, moment condition, compact or connected support, log-concavity, spectral-coordinate independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, conditional conjugate-pair density cap, or fixed-good-minor premise is used. Signs of `kappa,lambda,mu` are arbitrary. Outside data may cause arbitrary translations of all four active scalar channels and an arbitrary additive remainder, provided the four active sources remain on disjoint independent original-coordinate groups and the displayed quadratic coefficients are the fixed ones in (4.1).
