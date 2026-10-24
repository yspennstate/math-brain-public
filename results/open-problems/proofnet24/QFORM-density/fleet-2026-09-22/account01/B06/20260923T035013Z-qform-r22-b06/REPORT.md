SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B06, 2026-09-23T03:50:13.900976Z.
attacking: the one-sided zero-diagonal overlap survivor by replacing conditional fiber suprema with an exact section-mass/section-height functional, and testing whether the available product-projection caps actually control that functional.

# account01/B06 r22 — weighted section functional and a provenance barrier

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Curved fiber integration  
**Run:** `20260923T035013Z-qform-r22-b06`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / PROOF_INTERFACE_REFUTED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Target, fresh controls, and mathematical scope

The target is unchanged. For every dimension, independent real original coordinates `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^T A X` has a density with one universal finite essential supremum, or give a valid counterexample. Continuity is a separate requested conclusion and is not proved here.

Fresh control at the start of this run was `yspennstate/math-research-brain@0de28be725f2b0b14daa210b4df494d9ea356a78`. OWNER CONTROL remains revision `2026-09-22.15`, QFORM is the sole research target, and the live `CURRENT_RESEARCH.md`, `CLAIMS.json`, `CORRECTION_INBOX.json`, `MEMORY_PROTOCOL.md`, `scheduled_tasks/fleet.json`, `scheduled_tasks/roles.json`, `scheduled_tasks/PROTOCOL.md`, and the account01/B06 assignment were reread. In particular, the full conjecture is still OPEN and the following false interfaces are not used: law-uniform pointwise quadratic-phase decay, independence after spectral rotation, arbitrary-joint rank-three coarea, positive moments of worst conditional projection caps, unrestricted fiber suprema, perturbative deletion of a small nonzero quadratic tail, or selection of one uniformly good physical minor from aggregate minor mass.

The immediate predecessor is account01/B06 r21, which proved the two-bank curved square-hyperbola estimate and reduced the exact-rank-three zero-diagonal Schur endpoint to the one-sided state

`kappa<1/3`, `x^2<1/6`, `y^2>1/2`,                                  (0.1)

with notation from r20/r21. The first unpaid implication was to consume the `>1/2` one-L/two-R Pluecker packet without replacing the original product law by an arbitrary projected joint density.

The designated partner result used below is account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical proof

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For an orthonormal `k`-dimensional projection of an original cap-one product law it gives an `L^infinity` density cap at most `exp(k/2)`. I apply this at an actual inequality in Section 4.

I also read the newest completed account02/B06 result

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260923T025657Z-adca02bb41f7/REPORT.md`,

which proves `QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1`. Section 2 below isolates the exact weighted functional behind that theorem and shows precisely which part must remain product-specific.

## 1. A one-dimensional unnormalised bathtub lemma

Let `nu` be a finite absolutely continuous measure on `R`, with density `h` satisfying

`0<=h<=H`, `int h = m`.

For the one-sided kernel `k(s)=s^(-1/2) 1_{s>0}`, rearrangement gives, uniformly in `t`,

`int h(z) k(t-z) dz <= H int_0^(m/H) s^(-1/2) ds = 2 sqrt(Hm)`.       (1.1)

The statement is also valid when `H=0` or `m=0`, by the zero convention. This is the correct replacement for a conditional fiber supremum: both the section height `H` and the actual section mass `m` survive until after the singular kernel is integrated.

## 2. Main positive result: an exact weighted section functional

### Theorem 2.1 — `QFORM-CHAIN-WEIGHTED-SECTION-FUNCTIONAL-v1`

Let `X` be independent of a pair `(Y,Z)`. Assume only that `X` has a probability density bounded by one and `(Y,Z)` has a joint probability density `g`. For a.e. `y`, set

`m(y)=int_R g(y,z) dz`,                                               (2.1)

`H(y)=ess sup_z g(y,z)`.                                              (2.2)

Let `a,d` be nonzero, and for arbitrary real `b,c,r,s,u,v` define

`Q = a X^2 + 2bXY + cY^2 + 2dYZ + rX + sY + uZ + v`.                (2.3)

Put

`y_0=-u/(2d)`                                                        (2.4)

and define the curved section functional

`J_(y_0)(g)
 := int_R sqrt(H(y)m(y)) |y-y_0|^(-1/2) dy`.                         (2.5)

Whenever this quantity is finite, `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= sqrt(2) J_(y_0)(g) / sqrt(|ad|).`                                (2.6)

No conditional probability density is normalized in the proof; the unnormalised section mass is part of the estimate.

### Proof

Fix `y` outside a null set. Completing the square in the genuinely independent original scalar `X` gives

`a X^2+(2by+r)X
 =a(X+eta(y))^2+c_0(y)`.                                             (2.7)

For either sign of `a`, the density kernel of the translated square is bounded by

`|a|^(-1/2) q^(-1/2) 1_{q>0}`                                       (2.8)

on the appropriate one-sided translated coordinate. The unnormalised `z`-section `g(y,z)dz` has mass `m(y)` and cap `H(y)`. Under the linear map

`z -> (2dy+u)z`,                                                      (2.9)

it has the same mass and cap

`H(y)/|2dy+u|`.                                                       (2.10)

Apply (1.1) to the convolution with the square kernel. The contribution of this fixed `y` to the output density is therefore at most

`2 |a|^(-1/2)
 sqrt( H(y)m(y) / |2dy+u| )`.                                        (2.11)

The unique `y` for which `2dy+u=0` is irrelevant to the Lebesgue integral. Integrating (2.11) in `y` and using

`|2dy+u|^(-1/2)
 =(2|d|)^(-1/2)|y-y_0|^(-1/2)`                                      (2.12)

gives exactly (2.6). QED.

### Corollary 2.2 — exact recovery of the partner physical-chain theorem

Assume in addition that the `Y` marginal has density cap `L` and that for a.e. `y` the conditional density of `Z|Y=y` is capped by `K`. Then

`H(y)<=K m(y)`,                                                       (2.13)

hence

`J_(y_0)(g)
 <=sqrt(K) int m(y)|y-y_0|^(-1/2)dy
 <=2 sqrt(2KL)`,                                                      (2.14)

where the last step is the symmetric one-dimensional bathtub bound for a probability density capped by `L`. Therefore (2.6) becomes

`boxed:
 ||p_Q||_infinity <=4 sqrt(LK)/sqrt(|ad|).`                           (2.15)

This is exactly the constant and scope of the completed account02/B06 `QFORM-PHYSICAL-CHAIN-WEIGHTED-FIBER-v1`. The point of Theorem 2.1 is that it displays the more primitive quantity: a proof does not need a uniform conditional cap if it can control the weighted product `sqrt(Hm)` after aggregation.

## 3. A sharp route obstruction: joint cap plus middle marginal cap is still insufficient

The natural next shortcut would be to combine the partner's two-dimensional projection-density theorem with a scalar marginal-density theorem and infer that `J_(y_0)` is universally bounded. This is false for arbitrary dependent pairs, even for the exact target-signature matrix `diag(1) direct_sum [[0,1],[1,0]]`.

### Proposition 3.1 — `QFORM-JOINT-PLUS-MIDDLE-MARGINAL-CHAIN-FALSE-v1`

There exist a pair `(Y,Z)` with

`||p_(Y,Z)||_infinity<=1`,                                           (3.1)

`||p_Y||_infinity<=1`,                                               (3.2)

and an independent `X~Uniform[0,1]`, such that

`Q=X^2+2YZ`                                                          (3.3)

has an unbounded density. The symmetric quadratic matrix in (3.3) has eigenvalues `{1,1,-1}`. This is **not** a counterexample to QFORM because `Y,Z` are dependent. It is a counterexample to compressing the product-projection provenance to the two caps (3.1)-(3.2).

### Construction and proof

Let

`S=sum_(n=21)^infinity n^(-2)`,
`p_k=1/[S(k+20)^2]`, `k>=1`.                                         (3.4)

Then `sum p_k=1`, the sequence decreases, and

`p_1<=1/21<1/10`,                                                     (3.5)

because `S>=int_21^infinity x^(-2)dx=1/21`. Moreover

`sum_k sqrt(p_k)=infinity`.                                          (3.6)

Set

`R_k=3^k`, `I_k=[R_k,2R_k]`, `s_k=p_k/R_k`,                          (3.7)

and let `(Y,Z)` have joint density one on the disjoint set

`E= union_(k>=1) I_k x [-s_k,0]`.                                    (3.8)

The total area is

`sum_k |I_k| s_k = sum_k R_k (p_k/R_k)=1`,                           (3.9)

so this is a probability density with joint cap one. Its `Y` marginal equals `s_k` on `I_k` and zero elsewhere, so

`||p_Y||_infinity <= sup_k p_k/R_k <1`.                              (3.10)

Now condition on `(Y,Z)=(y,z)`. For `t>=0`, the positive root of

`X^2=t-2yz`                                                          (3.11)

contributes conditional density

`[2 sqrt(t-2yz)]^(-1)`                                               (3.12)

whenever `0<=t-2yz<=1`.

Fix `N` and `0<=t<=p_N`. For every `k<=N` and every `(y,z)` in the `k`th block,

`0<=-2yz<=4R_k s_k=4p_k`,                                            (3.13)

and because `p_N<=p_k<=p_1<1/10`,

`t-2yz<=p_k+4p_k=5p_k<1`.                                            (3.14)

Thus the whole `k`th block contributes, and (3.12) is at least

`1/[2 sqrt(5p_k)]`.                                                   (3.15)

Since the block has area `p_k`,

`p_Q(t)
 >= (1/(2sqrt(5))) sum_(k<=N) sqrt(p_k)`                              (3.16)

for every `t in [0,p_N]`, an interval of positive length. By (3.6) the right side tends to infinity with `N`. Hence

`ess sup p_Q=infinity`.                                               (3.17)

QED.

### Exact relation to the new functional

For this example, `H(y)=1` and `m(y)=s_k` on `I_k`. At the critical point `y_0=0`, the `k`th contribution to (2.5) is

`int_(R_k)^(2R_k) sqrt(p_k/R_k) y^(-1/2)dy
 =2(sqrt(2)-1)sqrt(p_k)`.                                             (3.18)

Therefore `J_0(g)=infinity` for exactly the same `sum sqrt(p_k)` reason. The section functional detects the obstruction that the two global caps completely miss.

This proposition strengthens the provenance warning in the newest account02/B06 report: not only can a joint pair cap fail when the middle marginal is large; **even a uniform joint cap and a uniform middle marginal cap together do not control the non-null curved chain**. What matters is how much conditional section height is carried at each middle-coordinate location, weighted before the singular fiber is paid.

## 4. Actual application of the designated account02/B06 product theorem in the one-sided survivor

Return to the exact rank-three zero-diagonal Schur geometry from r20/r21. We have orthonormal spectral-frame columns

`F=[w,u,v]`,                                                         (4.1)

with `u` supported on the physical bank `L`, `v` supported on the disjoint bank `R`, and

`x=||w_L||`, `y=||w_R||`, `kappa=||w_{ {i} union K }||^2`,
`x^2+y^2+kappa=1`.                                                    (4.2)

The one-sided survivor satisfies (0.1), in particular `y>1/sqrt(2)`. Because `w_R dot v=0`,

`q_R=w_R/y`                                                          (4.3)

is a unit vector orthogonal to `v`, both supported on `R`. Put

`V=v^T X_R`, `P_R=q_R^T X_R`.                                       (4.4)

The `n x2` coefficient matrix with columns `v,q_R` has orthonormal columns. Applying the designated partner theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` with `k=2` gives the **actual inequality**

`boxed:
 ||p_(V,P_R)||_infinity <= e.`                                       (4.5)

The same theorem at `k=1` gives

`boxed:
 ||p_V||_infinity<=sqrt(e),
 ||p_(P_R)||_infinity<=sqrt(e).`                                     (4.6)

Now decompose the physical pivot vector on the right bank as

`h_R=beta v+k_R`, `k_R=rho w_R=m_R q_R`, `m_R=rho y`.                 (4.7)

The exact shear

`Z_R=beta V+m_R P_R`                                                  (4.8)

has Jacobian `m_R` in the pair `(V,P_R)`. Therefore (4.5) yields

`boxed:
 ||p_(V,Z_R)||_infinity <= e/m_R.`                                   (4.9)

Because `y>1/sqrt(2)`,

`m_R>rho/sqrt(2)`.                                                    (4.10)

Equations (4.5)-(4.10) are a genuine use of the completed partner theorem on the live one-sided branch.

However, Proposition 3.1 shows why these inequalities alone are not the missing proof. A global two-dimensional cap such as (4.9), even together with a scalar marginal cap such as (4.6), does not control the weighted singular section functional needed when a non-null square and a hyperbolic middle coordinate are coupled. We must use that `(V,P_R)` is not an arbitrary dependent pair: it is an **orthogonal projection of an original product law**.

## 5. New exact structural identity: the hard state already has a dimension-free bank cover

The one-sided survivor is also not missing spectral coverage. Its problem is purely how to pay that coverage without summing physical-coordinate fiber costs.

For a physical row `j`, write

`f_j=(w_j,u_j,v_j) in R^3`.                                          (5.1)

Since `u` is supported on `L`, `v` on `R`, `w_L dot u=0`, and `w_R dot v=0`, the aggregate row Grams are exactly

`G_L=sum_(j in L) f_j f_j^T = diag(x^2,1,0)`,                         (5.2)

`G_R=sum_(j in R) f_j f_j^T = diag(y^2,0,1)`,                         (5.3)

`G_0=sum_(j in {i} union K) f_j f_j^T = diag(kappa,0,0)`.             (5.4)

The sum is `I_3`, as it must be. In particular,

`G_L+G_R=diag(1-kappa,1,1)`.                                         (5.5)

Hence, in the hard branch `kappa<1/3`, the two hyperbolic banks alone satisfy the dimension-free frame-cover inequality

`boxed:
 (1/(1-kappa))(G_L+G_R) >= I_3,
 1/(1-kappa)<3/2.`                                                    (5.6)

Call this `QFORM-ZERODIAG-HYPERBOLIC-BANK-GRAM-COVER-v1`.

The determinant of the two-dimensional `R`-bank Gram on the `(w,v)` plane is `y^2`; by Cauchy--Binet this is exactly the aggregate two-row wedge mass in that bank. Wedging with the `u` direction on `L` recovers the r21 identity that the one-L/two-R Pluecker packet has total mass `y^2>1/2`.

Thus the remaining difficulty is **not** finding a good spectral cover or a good right-bank plane. Both exist with universal constants. The missing implication is a bankwise curved-coarea inequality that pays (5.6) through the original product law before splitting it into coordinate fibers.

## 6. What changed, and the first unpaid implication

This run narrows the one-sided debt in two ways.

1. `QFORM-CHAIN-WEIGHTED-SECTION-FUNCTIONAL-v1` gives the exact weighted substitute for the singular conditional fiber supremum. The sufficient quantity is

   `J_c(g)=int sqrt(H(y)m(y)) |y-c|^(-1/2)dy`,                        (6.1)

   not a worst conditional cap.

2. `QFORM-JOINT-PLUS-MIDDLE-MARGINAL-CHAIN-FALSE-v1` proves that the currently available generic planar projection cap plus scalar marginal cap cannot by themselves bound (6.1). The repair must use product-projection provenance at the level of the weighted sections themselves.

3. In the live one-sided Schur survivor, the designated partner theorem gives the concrete right-bank projection bounds (4.5)-(4.10), while the exact Gram identity (5.6) shows that `L union R` already gives a universal spectral cover.

The first unpaid implication is therefore

`QFORM-PRODUCT-PROJECTION-WEIGHTED-SECTION-v1`:

> Let `(Y,Z)` be a two-dimensional orthogonal projection of independent cap-one coordinates (allow the affine shear/scaling actually generated by square completion). Prove a dimension-free estimate for the particular weighted section functional needed in (2.5), or produce a source-valid product-projection counterexample. The estimate must be stable under the bankwise coefficients in (4.7)-(4.10) and must be used before any physical-coordinate supremum is taken.

A successful theorem of this type would plug directly into the one-sided branch because `y^2>1/2` makes the right projection uniformly nondegenerate and (5.6) supplies a dimension-free two-bank frame cover. A failure would identify a genuinely product-derived obstruction rather than the arbitrary dependent-pair obstruction of Proposition 3.1.

The full arbitrary-dimensional QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED. No target counterexample is produced here. The separate continuous-density conclusion remains unproved.
