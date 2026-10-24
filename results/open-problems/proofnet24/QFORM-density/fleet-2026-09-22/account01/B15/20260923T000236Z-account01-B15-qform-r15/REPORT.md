SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B15, 2026-09-23T00:02:36Z.

attacking: target-level regularity — compress the newest no-pivot reduction to one fixed compact positive output kernel, while keeping rough original-coordinate product laws and separating continuity from the universal height estimate.

# account01/B15 r15 — an exact single-scale compact-tent normal form for the no-pivot gap

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Owner control consumed:** revision `2026-09-22.15`  
**Assignment:** Absolute continuity and regularity  
**Status:** `ESSENTIAL_STEP_APPLIED / EXACT_SINGLE_SCALE_N3_NORMAL_FORM`; full unrestricted QFORM remains **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and newest live reduction

For independent real coordinates `X_i` with probability densities `0<=f_i<=1`, and real symmetric `A`, write

`Q_A=X^T A X`,

and let

`s=s_3(A)`

be the third largest eigenvalue modulus. The owner target is one absolute finite `C` such that

`||p_{Q_A}||_infinity <= C`

whenever `s>=1`.

The newest owner-required synthesis is the no-pivot reduction at

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`.

For any fixed `tau in (0,1]`, it isolates N3: prove a universal density bound `C_0` for all target matrices satisfying

`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau` for all `i!=j`.

That completed synthesis proves that N3 implies the full conjecture with

`C_full <= tau^(-1/2) max{1+2 exp(pi) C_0, 1+3 K_tau}`,

`K_tau=(2/sqrt(tau))[6.2+log_+(16 sqrt(tau))]`.                 (1.1)

N3 itself remains unproved. The purpose of this report is to replace N3 by an exactly equivalent **one-output-scale, positive, compactly supported integral inequality** on original-coordinate extreme product laws. No output desmoothing modulus is required.

## 2. Completed assigned-partner results actually applied

Two completed `account02/B15` results are used at equations below.

### 2.1 Fixed-matrix bounded continuous density

Canonical source:

`yspennstate/math-open-problems@4b2e6a36bcffeb767998c43d27cee1d8f5eaa07e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T150242Z-account02-B15-qform-r3/REPORT.md`.

It proves that for every fixed symmetric `A` of rank at least three and arbitrary independent cap-one input densities, `Q_A` has a bounded continuous density. In fact it gives a matrix-dependent physical-principal-block certificate. Thus every target instance has a canonical `p_A in C_0(R)` and an attained maximum. The matrix-dependent bound is **not** the desired universal bound.

I use this theorem only in the exact limiting identity (4.4) below; it is not used as a source of a universal constant.

### 2.2 Exact Choquet product-indicator representation

Canonical source:

`yspennstate/math-open-problems@b1d930ff0fbc625393aebcd4a59f9ba1ead465ed`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T130201Z-account02-B15-qform-r2/REPORT.md`.

For every one-dimensional admissible density `f`, there is an exact probability mixture of densities `1_E` with `|E|=1`. Taking the representing measures independently yields an exact mixture of product-indicator input laws. I apply it directly in (5.1), to the actual positive tent functional.

The same partner report proves that there is no law-uniform continuity modulus even for fixed `A=I_3` on finite-fragment extreme laws. Therefore no step below may rely on equicontinuity or uniform desmoothing.

## 3. Scale-free version of the newest no-pivot class

For fixed `tau in (0,1]`, define the **scale-free no-pivot class** `N_tau^sc` to consist of target matrices `A` with `s=s_3(A)>=1` and

`|A_ii| < tau s`                                                   (3.1)

for every `i`, and

`|A_ii A_jj-A_ij^2| < tau s^2`                                   (3.2)

for every `i!=j`.

These inequalities are homogeneous under `A -> cA`: `s_3(cA)=c s_3(A)`, diagonal entries scale by `c`, and `2x2` principal determinants scale by `c^2`.

Let `C_N3(tau)` denote the sharp constant for Claude's absolute-threshold N3 class, allowing `+infinity`. Let

`C_sc(tau)
 = sup_{A in N_tau^sc, f} s_3(A) ||p_{Q_A}||_infinity`.            (3.3)

### Proposition 3.1 — exact homogeneous normalization

`C_N3(tau)=C_sc(tau)`, and both equal the sharp constant on the slice

`s_3(A)=1`, `|A_ii|<tau`, `|A_iiA_jj-A_ij^2|<tau`.               (3.4)

**Proof.** Let `s=s_3(A)` and put `B=A/s`. Then

`Q_A=s Q_B`,

so

`p_A(t)=s^(-1)p_B(t/s)`, hence

`s ||p_A||_infinity=||p_B||_infinity`.                            (3.5)

If `A` is in the scale-free class, (3.1)-(3.2) imply that `B` satisfies (3.4). Conversely every matrix in (3.4) is itself in the scale-free class.

Now suppose `A` is in Claude's absolute N3 class, so `s>=1`, `|A_ii|<tau`, and `|det A_{ij}|<tau`. Then `B=A/s` satisfies (3.4), and

`||p_A||_infinity=s^(-1)||p_B||_infinity<=||p_B||_infinity`.      (3.6)

Thus the absolute N3 supremum cannot exceed the normalized supremum; the reverse inequality is immediate because the normalized slice is contained in N3. This proves all equalities. QED.

The point of (3.1)-(3.2) is not to enlarge the hard problem: after the natural `s_3` weight, it is exactly the same sharp N3 constant, but the class is now genuinely scale invariant.

## 4. One fixed compact tent contains the entire N3 density problem

Define the fixed tent

`T(u)=(1-|u|)_+`.                                                 (4.1)

It is nonnegative, compactly supported, bounded by one, and

`int_R T(u)du=1`.                                                 (4.2)

Define

`C_tent(tau)
 = sup_{A in N_tau^sc, f, y in R}
     s_3(A) E T(Q_A-y)`.                                         (4.3)

### Theorem 4.1 — exact single-scale normal form

`C_tent(tau)=C_sc(tau)=C_N3(tau)`.                               (4.4)

In particular the entire remaining no-pivot density problem is equivalent, with **zero constant loss**, to bounding one fixed output-scale expectation. There is no auxiliary radius `epsilon` left.

**Proof: upper bound.** For every fixed target instance the partner theorem gives a bounded density `p_A`. From (4.2),

`E T(Q_A-y)
 = integral T(u-y) p_A(u)du
 <= ||p_A||_infinity`.                                           (4.5)

Multiplying by `s=s_3(A)` and taking the scale-free supremum yields

`C_tent(tau)<=C_sc(tau)`.                                        (4.6)

**Proof: reverse bound.** It is enough by Proposition 3.1 to take a normalized matrix `B` satisfying (3.4), with `s_3(B)=1`. By the assigned partner's fixed-matrix theorem, `Q_B` has a continuous density `p_B in C_0(R)`. Let `t_*` attain its maximum:

`p_B(t_*)=||p_B||_infinity`.                                     (4.7)

For every `c>=1`, put `A_c=cB`. The scale-free no-pivot inequalities are preserved exactly, and `s_3(A_c)=c`. Taking the center `y_c=c t_*`, the quantity in (4.3) is

`c E T(cQ_B-c t_*)
 = integral c T(c(u-t_*)) p_B(u)du`.                             (4.8)

The kernels

`K_c(v)=c T(cv)`                                                  (4.9)

form a compactly supported probability approximate identity. Since `p_B` is continuous at `t_*`,

`lim_{c->infinity} c E T(cQ_B-c t_*)
 =p_B(t_*)=||p_B||_infinity`.                                    (4.10)

Therefore `C_tent(tau)>=||p_B||_infinity` for every normalized N3 instance. Taking the supremum and using Proposition 3.1 gives the reverse inequality. QED.

### Why continuity is still logically separate

Continuity is used above only to make (4.10) a pointwise limit at the actual maximizer. For the central essential-supremum statement it is unnecessary: an approximate identity converges at Lebesgue points, and points with values arbitrarily close to the essential supremum suffice. Thus Theorem 4.1 does not turn continuity into a hidden quantitative hypothesis.

Conversely the partner's no-common-modulus construction shows why (4.10) must be applied **instance by instance** after scaling. There is no claim that `K_c*p_A -> p_A` uniformly over all target laws.

## 5. Exact reduction to compact finite-fragment extreme sources

The fixed tent is especially useful because it is a bounded positive functional of the original product law.

Let `f=(f_1,...,f_n)` be arbitrary admissible marginals. Apply the assigned partner's exact Choquet theorem independently to the coordinates. If `Pi` is the resulting product mixing measure on measure-one sets `E=(E_1,...,E_n)`, then for every fixed `A,y`,

`E_f T(Q_A-y)
 = integral E_E T(Q_A-y) dPi(E)`.                                (5.1)

This is the promised direct use of a completed partner result in an actual target inequality. In particular,

`s E_f T(Q_A-y)
 <= sup_{|E_i|=1} s integral_{E_1 x ... x E_n}
                  T(x^T A x-y) dx`.                             (5.2)

The reverse inequality is trivial because indicator laws are admissible. Hence the sharp constant in (4.3) is unchanged by restricting all marginals to measure-one indicators.

We may further restrict to **bounded finite unions of intervals**, still with no loss and with no uniform bound on the number of components. Indeed, for a measure-one measurable set `E`, Lebesgue regularity gives finite unions of bounded intervals `F_m` of exact measure one with

`|E triangle F_m| ->0`.                                         (5.3)

For product indicators of mass one, telescoping gives

`|| prod_i 1_{E_i} - prod_i 1_{F_i} ||_{L^1(R^n)}
 <= sum_i |E_i triangle F_i|`.                                  (5.4)

Since `0<=T<=1`,

`|E_E T(Q_A-y)-E_F T(Q_A-y)|
 <= sum_i |E_i triangle F_i|`.                                  (5.5)

For a fixed matrix the multiplier `s` is finite, so the right side can be made arbitrarily small compared with any prescribed error after multiplying by `s`. Thus

`boxed:
 C_N3(tau)
 = sup s integral_{E_1 x ... x E_n}
       (1-|x^T A x-y|)_+ dx,`                                   (5.6)

where the supremum is over

- `s=s_3(A)>=1`;
- `|A_ii|<tau s` for every `i`;
- `|A_ii A_jj-A_ij^2|<tau s^2` for every `i!=j`;
- arbitrary dimension and center `y`;
- each `E_i` a bounded finite union of intervals with `|E_i|=1`.

Equation (5.6) is an exact sharp-constant identity, not an approximation theorem with a hidden support radius or fragment-count parameter.

The existing correction that no uniform fragment-count bound exists is respected: the number and separation of components of `E_i` remain unrestricted.

## 6. Direct application to the newest Claude reduction

Assume one can prove the following **single-scale finite-fragment inequality** for some finite `C_0`:

`boxed:
 s_3(A) integral_{E_1 x ... x E_n}
 (1-|x^T A x-y|)_+ dx <= C_0`                                  (6.1)

for every scale-free no-pivot instance listed after (5.6).

By Theorem 4.1 and Section 5, (6.1) gives Claude N3 with **the same constant `C_0`** for every arbitrary cap-one product law. Therefore the completed newest synthesis applies and yields the full target bound (1.1):

`boxed:
 C_full <= tau^(-1/2)
 max{1+2 exp(pi) C_0,
     1+3(2/sqrt(tau))[6.2+log_+(16sqrt(tau))]}.`                (6.2)

No separate proof for Gaussian marginals is needed in the padding stage of the Claude reduction: (5.1) has already transferred (6.1) from extreme inputs to **all** cap-one marginals with the identical constant, including the auxiliary Gaussian density `exp(-pi x^2)` used there.

For the convenient choice `tau=1`, the remaining mathematical target becomes simply

`sup s_3(A) integral_{prod E_i}(1-|x^T A x-y|)_+ dx < infinity`, (6.3)

under

`|A_ii|<s_3(A)`,
`|A_ii A_jj-A_ij^2|<s_3(A)^2`,                                  (6.4)

and finite-fragment measure-one `E_i`. If (6.3) holds with constant `C_0`, then

`C_full <= max{1+2e^pi C_0, 1+6[6.2+log16]}`                    (6.5)

(the second displayed term is approximately `54.84`).

This is now a **one-scale geometric integral problem**: the output window is fixed (`|Q-y|<1` through the tent), the spectral scale is carried explicitly by `s_3(A)`, and all source complexity is a finite union of original-coordinate boxes with no cap loss.

## 7. Relation to the earlier multiscale tent theorem

The completed account03/B15 r20 theorem at

`yspennstate/math-open-problems@626e33966e69eda517dd09776028cbd80bd5d372`

shows for any probability law `mu`

`||p_mu||_infinity
 = sup_{epsilon>0,y} epsilon^(-2)
   E(epsilon-|Z-y|)_+`.                                        (7.1)

The new point here is not (7.1). It is that **after passing to the homogeneous scale-free N3 class, all epsilon are redundant**. Scaling the matrix itself converts the sharp N3 constant into the single fixed tent (4.3), while keeping the no-pivot hypotheses invariant in the normalized form (3.1)-(3.2). This interfaces directly with the newest Claude reduction.

That distinction matters because a proof of (6.1) can work at one physical output scale and need not produce a family of estimates uniform in an extra smoothing parameter.

## 8. Absolute continuity / boundedness / continuity ledger

The exact logical status is now:

1. **Absolute continuity:** already holds for any nonzero quadratic under any absolutely continuous joint input law; no three-large-eigenvalue assumption is needed.
2. **Fixed-matrix finite boundedness:** every rank-at-least-three target has a finite matrix-dependent density bound.
3. **Fixed-matrix continuity:** by the completed `account02/B15` theorem, every rank-at-least-three product target has a density in `C_0(R)`.
4. **Universal height:** still open. It is exactly the finite supremum in (5.6), and by the newest Claude reduction proving that supremum finite closes the full conjecture.
5. **Uniform raw regularity:** not available and not needed. The assigned partner has target-valid families excluding a common continuity modulus; its later r21 report excludes uniform positive Besov/Sobolev/BV control even on fixed `I_3` smooth-source families.

Thus the regularity problem and the central universal-height problem are cleanly separated. The one remaining B15-compatible quantitative object is the positive compact tent integral (5.6), not a raw-density modulus or an `L^1` Fourier norm.

## 9. Corrections preserved

This argument uses:

- no law-uniform pointwise quadratic Fourier decay;
- no independence after spectral rotation;
- no arbitrary-joint coarea estimate;
- no projection-only shortcut;
- no worst conditional-density supremum;
- no uniformly conditioned physical minor;
- no bounded support diameter and no bounded fragment count.

Every probabilistic mixture is in the **original independent coordinates**. The only scaling is the scalar multiplication `A -> cA`, which preserves the spectral directions and the homogeneous no-pivot ratios exactly.

## 10. First unpaid implication

The full theorem is not claimed. The first unpaid statement can now be written with no smoothing parameter and no general densities:

> For one fixed `tau in (0,1]`, prove a finite universal `C_0` such that (6.1) holds for all dimensions, all scale-free no-pivot symmetric matrices, all centers, and all product sets whose one-dimensional factors are bounded finite unions of intervals of measure one.

This is equivalent to N3 and, through the completed newest synthesis, sufficient for the full QFORM conjecture.

The natural next mathematics is therefore to apply the no-pivot inequalities directly inside this positive fixed-window integral before any reciprocal local-minor or conditional `L^infinity` payment. The integrand is bounded, compactly supported in the **output value**, and preserves all original-coordinate packing information.

**FULL-PROBLEM CHANGE:** `OPEN -> OPEN`.  
**NEW EXACT REDUCTION:** multiscale N3 / arbitrary source laws -> one fixed compact tent on the scale-free no-pivot finite-fragment extreme class, with zero constant loss before the already-proved Claude transfer.
