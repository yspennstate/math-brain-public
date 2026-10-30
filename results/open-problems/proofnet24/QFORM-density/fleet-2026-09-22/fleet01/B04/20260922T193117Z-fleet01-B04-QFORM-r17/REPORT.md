SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B04, 2026-09-22T19:31:17Z.
attacking: weighted product-space aggregation of many disjoint hyperbolic pairs, replacing payment by the two largest edges with an exact second-elementary-symmetric currency.

# fleet01/B04 — weighted hyperbolic matching aggregation by Laplace rearrangement

**Run:** `20260922T193117Z-fleet01-B04-QFORM-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh prepublication owner control:** revision `2026-09-22.15`; QFORM remains the sole research target  
**Assignment:** Product Fourier rearrangement  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Conditional end-to-end placement

The full target remains open: for every dimension, every independent product input with one-dimensional densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove a universal finite essential-supremum bound for the density of `X^T A X`, or give a valid counterexample. Full-target continuity is separately open.

The immediately preceding B04 mechanism paid an exact induced matching of two zero-diagonal hyperbolic edges by an `L^2 * L^2 -> L^infinity` convolution, with coefficient `K_2=5.194878...`. Its unresolved quantitative issue was that a diffuse zero-diagonal bank can have no individually large edge even though the total matching currency is order one. The present run changes the analytic mechanism: condition on one side of an entire matching, apply the product-projection density theorem once, and estimate the resulting reciprocal Euclidean norm by a Laplace transform plus one-dimensional decreasing rearrangement. The result depends on the aggregate

`E_2(c)=e_2(c_1^2,...,c_m^2)=sum_{i<j} c_i^2 c_j^2`

rather than on a selected pair of largest coefficients.

The first unpaid implication after this report is therefore structural rather than analytic: in the unresolved zero/near-zero diagonal bank, force a dimension-free amount of `E_2` on an induced/product-preserving hyperbolic matching, or route failure to the already-paid triangle/color/ridge/square/grouped-coordinate branches. The live corrections forbid replacing this by a universally good single physical minor or one Schur extraction.

## 2. Source-pinned partner result and corrections

The designated OTHER-account partner result actually applied is fleet02/B04 `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1`, complete at

`yspennstate/math-open-problems@4bea103ece44732c1c7c31368fec4e33b35e1fdd`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T174702Z-r15/REPORT.md`.

For an original-coordinate hyperbolic pair over an arbitrary residual,

`Q=2cYZ+2Y L_1(W)+2Z L_2(W)+R(W)`,
`H=R-2L_1L_2/c`,

it proves that a residual density cap `||p_H||_infinity<=B` implies

`||p_Q||_infinity <= |c|^(-1)+4B`.                          (2.1)

I apply (2.1) in Section 7 to the new matching estimate, giving a new explicit nested-packet inequality.

I also use the standard product-projection estimate recorded and used in the completed fleet02/B04 star-bank report

`yspennstate/math-open-problems@2ac6c31f920852005f11947f020bb4642af38d27`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B04/B04-20260922T171934Z-r11/REPORT.md`:
if `Z_j` are independent with densities at most one and `a` is a real coefficient vector, then the density of `sum a_j Z_j` is bounded by

`||p||_infinity <= sqrt(2)/||a||_2`.                         (2.2)

The proof below does not use law-uniform pointwise quadratic-phase decay, independence after spectral rotation, the refuted arbitrary-joint coarea bound, a universal positive conditional-projection-density moment, a universally good principal minor, or a forced one-Schur rank-two extraction. All probabilistic conditioning is on disjoint original coordinate blocks.

## 3. A sharp-enough one-dimensional Gaussian rearrangement lemma

### Lemma 3.1

Let `X` have a probability density `f` with `0<=f<=1`. Then for every `u>=0`,

`E exp(-u X^2) <= I(u) <= (1+u/6)^(-1/2)`,                  (3.1)

where

`I(u)=int_{-1/2}^{1/2} exp(-u x^2) dx`.

#### Proof

The first inequality is the one-dimensional bathtub/decreasing-rearrangement principle: among all densities with mass one and cap one, the integral of the symmetric decreasing function `exp(-u x^2)` is maximized by the indicator of the centered interval of length one.

For the second inequality put

`J(u)=int_{-1/2}^{1/2} x^2 exp(-u x^2) dx=-I'(u)`.

Integrating the derivative of `x exp(-u x^2)` gives the exact identity

`I(u)-2u J(u)=exp(-u/4)`.                                    (3.2)

Also, because `1/4-x^2>=0` on the interval and `e^y>=1+y`,

`exp(u/4) I(u)
 =int_{-1/2}^{1/2} exp(u(1/4-x^2)) dx
 >=1+u int_{-1/2}^{1/2}(1/4-x^2)dx
 =1+u/6`.                                                     (3.3)

Hence

`exp(-u/4)/I(u) <= (1+u/6)^(-1)`.                            (3.4)

Using (3.2), for `u>0`,

`J(u)/I(u)
 =[1-exp(-u/4)/I(u)]/(2u)
 >=1/[2(u+6)]`.                                               (3.5)

Therefore

`d/du [log I(u)+(1/2)log(1+u/6)]
 =-J(u)/I(u)+1/[2(u+6)] <=0`.                                (3.6)

The bracket is zero at `u=0`, so (3.1) follows. QED.

The constant six is tangent-correct at the origin because `E_{[-1/2,1/2]} X^2=1/12`.

## 4. Reciprocal Euclidean norm of a weighted product vector

Let `U_1,...,U_m` be independent cap-one variables and let `c_1,...,c_m` be real. Put

`R=(sum_k c_k^2 U_k^2)^(1/2)`

and assume

`E_2:=sum_{i<j} c_i^2 c_j^2>0`.                              (4.1)

### Lemma 4.1 — aggregate negative moment

`E R^(-1) <= C_R E_2^(-1/4)`,                               (4.2)

where

`C_R=sqrt(3/2) Gamma(1/4)^2/pi
    =5.124575629524625...`.                                  (4.3)

#### Proof

The event `R=0` has probability zero because at least two coefficients are nonzero and all inputs are absolutely continuous. Use

`r^(-1)=pi^(-1/2) int_0^infinity s^(-1/2) exp(-s r^2) ds`.    (4.4)

Tonelli, independence and Lemma 3.1 give

`E exp(-sR^2)
 =prod_k E exp(-s c_k^2 U_k^2)
 <=prod_k (1+s c_k^2/6)^(-1/2)`.                             (4.5)

Expanding the nonnegative product polynomial and retaining only its constant and second elementary-symmetric terms,

`prod_k (1+s c_k^2/6)
 >=1+(E_2/36)s^2`.                                           (4.6)

Thus

`E R^(-1)
 <=pi^(-1/2) int_0^infinity
    s^(-1/2)(1+(E_2/36)s^2)^(-1/2) ds`.                      (4.7)

With `t=(E_2/36)s^2`,

`(4.7)=pi^(-1/2) sqrt(3/2) E_2^(-1/4)
       B(1/4,1/4)`
`=sqrt(3/2) Gamma(1/4)^2/pi * E_2^(-1/4)`,                  (4.8)

which proves the claim. QED.

The point of (4.6) is that no individual edge is selected. A bank of `m` edges of size `m^(-1/2)` has `E_2=(m-1)/(2m)`, so the right side remains uniformly bounded as `m` grows.

## 5. Main theorem — `QFORM-HYPERBOLIC-MATCHING-E2-v1`

Let

`U_1,V_1,...,U_m,V_m,W_1,...,W_r`

be independent real variables with densities bounded by one. Let at least two `c_k` be nonzero. Let `L_k(W),M_k(W)` be arbitrary real linear forms of the disjoint outside block `W`, and let `R_0(W)` be an arbitrary quadratic-plus-linear function of `W`. Assume that among the selected `2m` physical coordinates the quadratic form has exactly the matching edges `U_k V_k`: namely no selected diagonal terms and no selected-selected cross terms other than the displayed pairs. Define

`Q= sum_{k=1}^m [2c_k U_kV_k
                 +2U_k L_k(W)+2V_k M_k(W)] +R_0(W)`.        (5.1)

Set

`E_2=sum_{i<j}c_i^2 c_j^2`.                                 (5.2)

Then `Q` has a **continuous** density and

`boxed: ||p_Q||_infinity
 <= C_match E_2^(-1/4)`,                                    (5.3)

with

`C_match=sqrt(3) Gamma(1/4)^2/(2pi)
        =3.623622178340184...`.                              (5.4)

#### Proof

Condition on `W=w`. Complete each selected pair exactly:

`2c_k U_kV_k+2U_k L_k(w)+2V_k M_k(w)
 =2c_k (U_k+M_k(w)/c_k)(V_k+L_k(w)/c_k)
  -2L_k(w)M_k(w)/c_k`.                                      (5.5)

The shifted `U_k,V_k` remain mutually independent cap-one variables. Absorb the last terms in (5.5) and `R_0(w)` into a deterministic translation. It therefore suffices to bound

`S=2 sum_k c_k U_kV_k`.                                     (5.6)

Condition now on `U=(U_1,...,U_m)`. By the product-projection estimate (2.2), the conditional density of the linear combination of the independent `V_k` has cap

`||p_{S|U}||_infinity
 <= sqrt(2)/[2(sqrt(sum_k c_k^2U_k^2))]
 =1/(sqrt(2)R)`.                                             (5.7)

Average (5.7) and apply Lemma 4.1:

`||p_S||_infinity
 <=(1/sqrt(2)) E R^(-1)
 <=sqrt(3)Gamma(1/4)^2/(2pi) E_2^(-1/4)`.                   (5.8)

This is uniform in `w`, so averaging the conditional densities gives the same bound for `Q`.

For continuity, each nonzero single-pair product has an `L^1` density. Since at least two pair coefficients are nonzero, after conditioning on `W=w` the random part is a convolution of at least two `L^1` densities, hence has a continuous representative. The representatives are uniformly bounded by (5.3). If `t_n->t`, dominated convergence in `w` applied to the translated conditional densities gives `p_Q(t_n)->p_Q(t)`. Thus the averaged density is continuous. QED.

### Two-edge endpoint

For exactly two nonzero coefficients, `E_2=c_1^2c_2^2`, so

`||p_Q||_infinity
 <=3.623622178340184/sqrt(|c_1c_2|)`.                        (5.9)

This strictly improves the preceding B04 `L^2` convolution coefficient `5.194878272562849` on the same two-pair scope.

### Diffuse matching endpoint

For `c_k=m^(-1/2)`,

`E_2=(m-1)/(2m)`

and hence

`||p_Q||_infinity
 <=C_match (2m/(m-1))^(1/4)
 ->4.309237276563806...`.                                    (5.10)

Thus an arbitrarily large number of individually tiny exact hyperbolic edges is paid at constant cost without selecting one edge first.

## 6. Genuinely rotated indefinite target instance

Take five independent cap-one variables in the order `(U_1,V_1,U_2,V_2,W)` and

`A=[[0,1,0,0,0.30],
    [1,0,0,0,-0.20],
    [0,0,0,1,0.25],
    [0,0,1,0,0.15],
    [0.30,-0.20,0.25,0.15,2.00]]`.                          (6.1)

This is not diagonal in the independent coordinates; every selected matching coordinate is coupled to the outside coordinate. Its eigenvalues are

`(-1.04330866..., -1, 0.92556572..., 1, 2.11774294...)`,     (6.2)

so at least three eigenvalues have modulus at least one. The selected two matching coefficients are `c_1=c_2=1`, hence `E_2=1`. Theorem 5.1 proves, for **every** allowed choice of the five independent input laws,

`boxed: ||p_{X^TAX}||_infinity <=3.623622178340184...`.      (6.3)

Moreover the density is continuous. This is a target-valid rotated indefinite example, not a diagonal-basis calculation and not a numerical density histogram.

## 7. Direct application of the designated fleet02/B04 result

Now take one further original-coordinate hyperbolic pair with coefficient `c_0!=0` and arbitrary cross shifts into a residual `H` that itself has the exact matching structure of Theorem 5.1, with coefficients `d_1,...,d_m` and

`E_2(d)=sum_{i<j}d_i^2d_j^2>0`.

Theorem 5.1 supplies the actual residual density inequality

`B=||p_H||_infinity
 <=C_match E_2(d)^(-1/4)`.                                  (7.1)

Apply fleet02/B04 `QFORM-HYPERBOLIC-PAIR-DENSITY-TRANSFER-v1`, equation (2.1), at its exact hypotheses. One gets

`boxed: ||p_Q||_infinity
 <=|c_0|^(-1)
   +4 C_match E_2(d)^(-1/4)`                                (7.2)

or numerically

`||p_Q||_infinity
 <=|c_0|^(-1)+14.494488713360736 E_2(d)^(-1/4)`.             (7.3)

This is a literal use of a completed OTHER-account result in a new inequality. It is useful when the outer pair has arbitrary residual-dependent translations that are most naturally removed by the partner completion. When all pairs lie in one exact matching packet, Theorem 5.1 is sharper because it aggregates them simultaneously.

## 8. What this pays and what it does not

The theorem closes the analytic smoothing problem for an exact zero-diagonal **induced weighted matching** using the aggregate second elementary symmetric weight. It therefore repairs an important weakness of the preceding two-pair theorem: a diffuse matching no longer requires locating two individually macroscopic edges.

It does **not** establish that the bare three-large-eigenvalue hypothesis forces such an exact matching with `E_2>=c>0`. It also does not permit dropping small nonzero diagonal curvature on the selected vertices: without moment or support assumptions, a small coefficient multiplying an unbounded random square is not a perturbative error. Inter-pair selected-coordinate edges likewise require a different packet theorem or routing argument.

The first remaining B04 implication is therefore

`QFORM-WEIGHTED-MATCHING-OR-CURVATURE-ROUTING-v1`:
from the current aggregate-before-inversion residual, prove that either an original-coordinate zero-diagonal induced matching carries a universal amount of `E_2`, or the failure quantitatively forces one of the already completed triangle, colored-star, square-pivot, ridge-window, or grouped-curvature branches. This must be a global weighted statement; current corrections rule out selecting one universally good local triple or one universally good Schur cut.

The full QFORM conjecture remains open. No full-solution or novelty claim is made. The branch theorem (5.3) proves continuity; full-target continuity is still open.

## 9. Finite calculation and privacy/provenance note

The accompanying checker evaluates the exact constants in (5.4), (5.10), the eigenvalues/determinant of (6.1), and sample values of the scalar inequality in Lemma 3.1. Those computations are sanity checks, not substitutes for the analytic proof.

This report contains only authorized mathematics and repository source pins. No credentials, scheduler identifiers, machine paths, unrelated private data, benchmark material, email, external workflow output, or public-release action is included. No scheduler, notification, email, Drive, permission, paid-model/API, or remote-workflow mutation was made.
