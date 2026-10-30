# r19 addendum — balanced all-cross-minor L1 compiler

**New stronger result:** `QFORM-BALANCED-CROSSMINOR-ENTROPY-L1-v1`.  
**Status:** supporting theorem proved; full QFORM remains OPEN.  
**Relation to the main report:** this strictly strengthens the fixed-three-column packet result by aggregating simultaneously over **all** physical row triples and **all** physical column triples of an arbitrary original-coordinate cross block before any reciprocal minor is paid.

## 1. Setup

Let `I,J,K` be disjoint banks of ORIGINAL coordinates. Condition on `K`. Put

`B=A[I,J] in R^(m x n)`.

No rank-exactness is assumed, only `rank(B)>=3`. As in the main report, after conditioning the form is

`Q=q_I(X)+q_J(Y)+2 X^T B Y+c`,

where `q_I,q_J` may be arbitrary measurable real self phases arising from all within-bank quadratic and affine terms.

One Cauchy--Schwarz step in the `X` probability measure gives, with `Y'` an independent copy and `D=Y-Y'`,

`|phi_(Q|K)(t)|^2
 <= E_D prod_(i in I)|hat f_i(2t [BD]_i)|.`                         (1.1)

The coordinates `D_j` are independent with difference densities

`g_j=f_j*tilde f_j`, `0<=g_j<=1`, `int g_j=1`.                      (1.2)

Write `b_i^T` for the rows of `B` and

`h_i(s)=|hat f_i(s)|`.

Then the right side of (1.1) is the graph integral

`I(a)=int_(R^n) prod_j g_j(x_j) prod_i h_i(a b_i^T x) dx`,

with `a=2t`.                                                        (1.3)

## 2. Canonical three-minor law

Define the total squared physical `3x3` cross-minor mass

`W_3(B)=sum_(|R|=|S|=3) det(B_[R,S])^2
      =e_3(B^T B)=e_3(BB^T).`                                      (2.1)

Assume `W_3(B)>0`. On nonzero minor pairs `(R,S)` define the canonical probability law

`w_(R,S)=det(B_[R,S])^2/W_3(B)`.                                    (2.2)

Let `mu` be any probability law absolutely continuous with respect to `w`. Put

`p_i=P_mu(i in R)`, `s_j=P_mu(j in S)`, `q_j=1-s_j`.                (2.3)

Then

`sum_i p_i=3`, `sum_j s_j=3`, `sum_j q_j=n-3`.                      (2.4)

Assume only the **row balance gate**

`p_i<=1/2 for every i`.                                             (2.5)

There is no column-leverage gate.

Let

`D_mu=D(mu||w)`.                                                     (2.6)

## 3. Entropy graph-Brascamp--Lieb lemma

### Lemma 3.1

Under (2.5), for every real `a!=0`,

`I(a)
 <= |a|^(-3) W_3(B)^(-1/2) exp(D_mu/2)
    (2pi)^3 exp(3)
    2^(-3/2).`                                                       (3.1)

### Proof

If `q_j=0`, drop the factor `g_j<=1`; if `p_i=0`, drop `h_i<=1`. For positive exponents write the integrand in rank-one Brascamp--Lieb form using

`F_j=g_j^(1/q_j)`, `H_i=h_i^(1/p_i)`,                              (3.2)

with linear forms `e_j^T x` and `a b_i^T x`, carrying exponents `q_j` and `p_i`, respectively.

The rank-one Gaussian variational formula gives

`BL^2
 =sup_(r_j,u_i>0)
   [prod_j r_j^(q_j) prod_i u_i^(p_i)]
   /det(sum_j q_j r_j e_j e_j^T
       +sum_i p_i u_i a^2 b_i b_i^T).`                              (3.3)

Set `y_j=q_j r_j`, `z_i=p_i u_i`. The numerator is

`prod_j y_j^(q_j) prod_i z_i^(p_i)
 *prod_j q_j^(-q_j) prod_i p_i^(-p_i).`                             (3.4)

For the denominator use the exact Cauchy--Binet expansion

`det(D_y+a^2 B^T D_z B)
 =sum_(r>=0) sum_(|R|=|S|=r)
   a^(2r) det(B_[R,S])^2
   prod_(j notin S)y_j prod_(i in R)z_i.`                           (3.5)

Keep only the nonnegative `r=3` terms and apply weighted AM--GM with weights `mu_(R,S)`. Since the inclusion marginals are (2.3),

`det(D_y+a^2 B^T D_z B)
 >= |a|^6 W_3(B) exp(-D_mu)
    prod_j y_j^(q_j) prod_i z_i^(p_i).`                             (3.6)

Therefore

`BL
 <= |a|^(-3) W_3(B)^(-1/2) exp(D_mu/2)
    prod_j q_j^(-q_j/2) prod_i p_i^(-p_i/2).`                       (3.7)

For the difference densities, sharp Young in exactly the scalar form already proved in the regularized-determinant source gives, for `0<q<=1`,

`||g_j||_(1/q)
 <=2^q q^(q/2)(1+q)^(-(1+q)/2).`                                   (3.8)

For `p_i<=1/2`, sharp Hausdorff--Young gives

`||h_i||_(1/p_i)
 <=(2pi)^p_i p_i^(p_i/2)
   (1-p_i)^(-(1-p_i)/2).`                                           (3.9)

The `q_j` and `p_i` powers cancel those in (3.7). Put

`G(q)=2^q(1+q)^(-(1+q)/2)`.

The concavity estimate from the same regularized-determinant source is

`log G(q)<=((1-log2)/2)(1-q)`.                                     (3.10)

Because `sum_j(1-q_j)=sum_j s_j=3`,

`prod_j G(q_j)<=exp(3(1-log2)/2).`                                 (3.11)

Also `-(1-p)log(1-p)<=p`, so using `sum_i p_i=3`,

`prod_i (1-p_i)^(-(1-p_i)/2)<=e^(3/2)`,                            (3.12)

and `prod_i(2pi)^p_i=(2pi)^3`. Combining (3.7)--(3.12) proves

`I(a)
 <= |a|^(-3)W_3(B)^(-1/2)exp(D_mu/2)
    (2pi)^3 e^3 2^(-3/2)`,

which is (3.1). QED.

No conditional density cap, post-rotation independence, moment, support, or scalar pointwise Fresnel estimate was used.

## 4. Integrated Fourier consequence

Apply Lemma 3.1 to (1.1) with `a=2t`. Since `(2pi)^3/2^3=pi^3`,

`|phi_Q(t)|^2
 <= pi^3 e^3 2^(-3/2)
    exp(D_mu/2)W_3(B)^(-1/2)|t|^(-3).`                              (4.1)

Therefore

`boxed(
 |phi_Q(t)|
 <=min{1,
   pi^(3/2)e^(3/2)2^(-3/4)
   exp(D_mu/4)W_3(B)^(-1/4)|t|^(-3/2)}.
)`                                                                  (4.2)

This is an actual unweighted-`L1` tail. Integrating the envelope at its exact crossover gives

`boxed(
 ||phi_Q||_1
 <=(6pi e/sqrt(2)) exp(D_mu/6)W_3(B)^(-1/6).
)`                                                                  (4.3)

Hence `Q` has a bounded **continuous** density with

`boxed(
 ||p_Q||_infinity
 <=(3e/sqrt(2)) exp(D_mu/6)W_3(B)^(-1/6).
)`                                                                  (4.4)

Numerically `3e/sqrt(2)=5.766...`.

The bound is uniform in all conditioned outside original coordinates, so (4.2)--(4.4) hold for the full ambient form after averaging.

## 5. Automatic row-balance from disjoint minor mass

Let `(R,S)` and `(R',S')` be iid from the canonical minor law `w`. Define

`delta_row=P(R cap R'=empty)`.                                      (5.1)

If `delta_row>0`, condition the pair on row-disjointness and let `mu` be the first marginal. Symmetry gives

`p_i=P(i in R | R cap R'=empty)<=1/2`.                              (5.2)

If

`r_(R,S)=P(R' cap R=empty | R,S)`,

then

`mu_(R,S)=w_(R,S) r_(R,S)/delta_row`,                               (5.3)

and `r_(R,S)<=1`, so

`D(mu||w)<=log(1/delta_row)`.                                       (5.4)

Thus (4.4) gives the source-free-looking aggregate corollary

`boxed(
 ||p_Q||_infinity
 <=(3e/sqrt(2))
   delta_row^(-1/6) W_3(B)^(-1/6).
)`                                                                  (5.5)

The density is continuous.

There is a transpose version obtained by applying the initial Cauchy--Schwarz step on the other bank; it uses `delta_col=P(S cap S'=empty)` instead. Hence **either** substantial row-disjoint or column-disjoint determinant mass pays the whole arbitrary-self-curvature cross block.

## 6. Why this is stronger than selecting a three-column packet

The main report fixed a physical three-column bank before applying Pluecker entropy. Formula (5.5) instead uses

`W_3(B)=sum_(R,S)det(B_[R,S])^2`

across all physical row and column triples simultaneously. The reciprocal is paid only after this full Cauchy--Binet aggregation. Thus the newest live correction against selecting one tiny local minor is respected more directly.

If `delta_row` and `delta_col` are both small, the canonical determinant mass is forced into highly intersecting row and column triple families. That is now the sharpened structural residue: convert simultaneous small disjointness on the two compound-coordinate sides into one of the already-paid finite-core / hub / pair / grouped-ridge exits, without destroying product provenance.

## 7. Designated partner overlap

The fleet04/B02 zero-diagonal physical-triple theorem remains compatible with this stronger tail. Its global `L2` Fourier credit

`int|phi_Q|^2<=6pi 2^(2/3)|det P|^(-1/3)`

can be interpolated exactly as in the main report with the tail constant in (4.2). This produces another valid overlap inequality; the main scientific advance of this addendum is (4.4)--(5.5), which no longer fixes a column triple.

## 8. Status

`ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

The target-wide `int|phi_Q|` estimate is still not proved from `s_3(A)>=1` alone, because the spectral hypothesis has not yet been converted into a universal lower bound for `delta_row W_3(B)` or its transpose over some product-preserving cut. But a large class of high-cardinality cross configurations is now paid by a single integrated estimate with arbitrary same-bank curvature.
