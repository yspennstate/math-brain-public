# fleet01/B06 — weighted curved-fiber aggregation through Plücker marginals

**Run:** `20260922T130334Z-qform-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREM_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/use occurred, but no native learned-memory ingestion was verified.

## 0. Exact target and correction discipline

The full target remains: for every finite `n`, independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite constant, or give a valid counterexample. No moment, support, log-concavity, Gaussianity, diagonal-basis independence, or sign hypothesis is added.

This report consumes the live corrections `QFORM-POINTWISE-DECAY-FALSE`, `QFORM-FIBER-SUP-DIMENSION-LOSS`, `QFORM-NO-INDEPENDENCE-AFTER-ROTATION`, `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, and `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`. The argument below uses none of the refuted statements. It does not condition on a rotated coordinate and does not replace a curved fiber by an unrestricted fiber supremum.

The designated partner result actually used is fleet02/B06, run `b06-20260922T113045Z-d47192d10a82`, canonical report `yspennstate/math-open-problems@6902eb62f21a7c833ca27dcca69f34d50e711a7d:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`. Its theorem `QFORM-SAMESIGN-DETERMINANT-MASS-v1` gives, for an orthonormal two-frame `R=[r s]`, the Plücker weights

`w_ij=(r_i s_j-r_j s_i)^2`,   `sum_{i<j} w_ij=1`.

The new argument turns that determinant-mass probability measure into dimension-free product smoothing rather than trying to select one large physical minor.

## 1. Compact conditional end-to-end argument and first unpaid implication

Among any three large eigenvalues of `A`, two have the same sign. Choose such a pair `(lambda_1,r),(lambda_2,s)` and write

`P(X)=lambda_1 <r,X>^2 + lambda_2 <s,X>^2`,

`A = lambda_1 rr^T + lambda_2 ss^T + B`, with `Br=Bs=0`.

The theorem proved below gives the completely rotation-robust bound

`||p_P||_infinity <= pi e / sqrt(|lambda_1 lambda_2|) <= pi e`

for every allowed product input law. Thus delocalization of the same-sign spectral plane is no longer an obstruction for the pure same-sign component: even the Hadamard family from the partner report is controlled uniformly although every physical pair minor is tiny.

If `P(X)` were independent of `X^T B X`, convolution would immediately give the same bound for `Q`. In the actual theorem these two terms are generally dependent because an orthogonal spectral decomposition does not preserve independence of the projected coordinates. Therefore the first essential remaining implication on this route is now sharply isolated:

> **QFORM-ORTHOGONAL-CORRELATED-ADDITION-v1 (OPEN).** Under the original product law, with `r,s` orthonormal, `lambda_1 lambda_2>0`, `|lambda_i|>=1`, `Br=Bs=0`, and `B` having at least one eigenvalue of magnitude at least one, prove a universal density bound for
> `lambda_1<r,X>^2+lambda_2<s,X>^2+X^T B X`.

The present report proves the exact weighted curved-fiber input needed before that correlation step. It does not claim the full target or continuity for the full target.

## 2. A sharp one-dimensional Fourier input with the correct leverage scaling

Use Fourier convention

`hat f(t)=int_R exp(i t x) f(x) dx`.

Let `f` be a probability density with `0<=f<=1`. For `0<c<=1/2`, put `q=1/c` and `p=1/(1-c)`, so `1/p+1/q=1` and `1<=p<=2<=q`. Sharp Hausdorff--Young gives

`||hat f||_q <= (2pi)^(1/q) [ p^(1/p) / q^(1/q) ]^(1/2) ||f||_p`.

Since `int f=1` and `f<=1`, `||f||_p<=1`. Raising to the `q`-th power yields the exact estimate

`int_R |hat f(t)|^(1/c) dt`
` <= 2pi sqrt(c) (1-c)^(-(1-c)/(2c)).`                                         (2.1)

The factor `sqrt(c)` is crucial: after the physical coefficient rescaling below it exactly cancels the Jacobian `c^(-1/2)`. A plain Plancherel interpolation bound would miss this cancellation and reintroduce a dimension-dependent entropy factor.

## 3. One-dimensional projection lemma

### Lemma 3.1 — `QFORM-1D-PROJECTION-SQRT-E-v1`

Let `Z=sum_i a_i X_i`, where the `X_i` are independent with densities at most one and `sum_i a_i^2=1`. Then `Z` has a density and

`||p_Z||_infinity <= sqrt(e)`.

### Proof

Write `d_i=a_i^2` and omit zero coefficients.

If some `d_k>1/2`, condition on all variables except `X_k`. Translation does not change an `L^infinity` density norm and scaling gives conditional density at most `1/|a_k|<sqrt(2)<sqrt(e)`. Averaging preserves the bound.

Assume now every `d_i<=1/2`. The characteristic function is

`Phi(t)=prod_i hat f_i(a_i t)`.

Apply Holder with exponents `1/d_i`. By (2.1),

`int |Phi(t)| dt`
` <= prod_i [ |a_i|^(-1) int |hat f_i(s)|^(1/d_i) ds ]^(d_i)`
` <= 2pi prod_i (1-d_i)^(-(1-d_i)/2).`

For `0<=d<1`,

`-(1-d) log(1-d) <= d`.

Therefore

`log prod_i (1-d_i)^(-(1-d_i)/2) <= (1/2) sum_i d_i = 1/2`.

Thus `int |Phi|<=2pi sqrt(e)`, and Fourier inversion gives `||p_Z||_infinity<=sqrt(e)`.  QED.

No continuity statement is needed in the heavy-coordinate branch; the conclusion used later is only the essential density bound.

## 4. Partner Plücker mass becomes the exact leverage marginal

Let `R=[r s]` have orthonormal columns and row vectors `u_i=(r_i,s_i)`. Define

`c_i=||u_i||_2^2=r_i^2+s_i^2`.

The partner result provides `w_ij=det(u_i,u_j)^2` and `sum_{i<j}w_ij=1`. The following marginal identity is new in this report and is the point where the partner theorem is used quantitatively:

### Lemma 4.1 — `QFORM-PLUCKER-MARGINAL-v1`

For every physical coordinate `i`,

`sum_{j:j!=i} w_ij = c_i`.                                                   (4.1)

Consequently, if an unordered physical pair is sampled with probability `w_ij`, the probability that coordinate `i` is one of its two endpoints is exactly `c_i`; equivalently, a uniformly selected endpoint has law `c_i/2`.

### Proof

Expand and use orthonormality of `r,s`:

`sum_j (r_i s_j-s_i r_j)^2`
`=r_i^2 sum_j s_j^2+s_i^2 sum_j r_j^2-2r_i s_i sum_j r_j s_j`
`=r_i^2+s_i^2=c_i`.

The `j=i` term is zero. QED.

Thus the determinant-mass probability measure of fleet02/B06 is not merely normalized: its vertex marginals are exactly the row leverages of the same-sign spectral plane.

## 5. Dimension-free two-dimensional projection density

### Theorem 5.1 — `QFORM-WEIGHTED-2D-PROJECTION-v1`

Let `R` be any real `n x 2` matrix with `R^T R=I_2`, and let

`Y=R^T X in R^2`

for independent real `X_i` with densities at most one. Then `Y` has an essentially bounded density `g` satisfying

`||g||_infinity <= e`.                                                        (5.1)

In the diffuse case `max_i c_i<=1/2`, one has the sharper determinant-mass/leverage formula

`||g||_infinity`
` <= B(c):=prod_i (1-c_i)^(-(1-c_i)/2)`
` =prod_i (1-sum_{j!=i}w_ij)^(-(1-sum_{j!=i}w_ij)/2)`
` <= e`.                                                                       (5.2)

If one leverage is larger than `1/2`, then

`||g||_infinity <= sqrt(e/c_*) < sqrt(2e) < e`,                               (5.3)

where `c_*=max_i c_i`.

### Proof: diffuse case

For each `c_i>0`, write `u_i=sqrt(c_i) v_i` with `||v_i||=1`. Since `R^TR=I_2`,

`sum_i c_i v_i v_i^T=I_2`,   `sum_i c_i=2`.

The characteristic function of `Y` is

`hat mu(xi)=prod_i hat f_i(u_i dot xi)`.

Set

`h_i(t)=|hat f_i(sqrt(c_i)t)|^(1/c_i)`.

The rank-one geometric Brascamp--Lieb inequality for the isotropic datum `(v_i,c_i)` gives

`int_{R^2} |hat mu(xi)| dxi`
`=int prod_i h_i(v_i dot xi)^(c_i) dxi`
`<=prod_i (int_R h_i)^(c_i)`.

By (2.1),

`int h_i = c_i^(-1/2) int |hat f_i(s)|^(1/c_i) ds`
`<=2pi (1-c_i)^(-(1-c_i)/(2c_i)).`

Hence

`int_{R^2}|hat mu| <= (2pi)^2 B(c)`.

As above, `-(1-c)log(1-c)<=c`, so

`log B(c)<= (1/2)sum_i c_i=1`, hence `B(c)<=e`. Fourier inversion in `R^2` gives (5.2), and in fact gives a bounded continuous density in this diffuse subcase.

### Proof: one heavy leverage

There can be at most one `c_i>1/2`. Relabel it `i=1` and rotate the two-dimensional target plane so

`u_1=(sqrt(c),0)`, `c=c_1>1/2`.

For `i>=2`, write `u_i=(alpha_i,beta_i)`. Isotropy implies

`sum_{i>=2} beta_i^2=1`.

Let

`W_1=sum_{i>=2}alpha_i X_i`,  `W_2=sum_{i>=2}beta_i X_i`.

Then `Y=(sqrt(c)X_1+W_1,W_2)`, and `X_1` is independent of `W=(W_1,W_2)`. Lemma 3.1 gives `W_2` a density `h_2` with `||h_2||_infinity<=sqrt(e)`.

For every Borel `E subset R^2`, conditioning on `W` and using `f_1<=1`,

`P(Y in E)`
`=E_W int f_1(x) 1_E(sqrt(c)x+W_1,W_2) dx`
`<=c^(-1/2) E_W int_R 1_E(y_1,W_2) dy_1`
`<=sqrt(e/c) |E|`.

Thus `Y` has density at most `sqrt(e/c)<sqrt(2e)<e`. QED.

### Interpretation in the partner determinant-mass language

Equation (4.1) says that the diffuse/heavy dichotomy in Theorem 5.1 is exactly a dichotomy for the partner's Plücker determinant-mass graph:

- diffuse: no coordinate is incident to more than half of the total determinant mass;
- heavy: one coordinate carries more than half of the total determinant mass and can be paid directly by one original-coordinate density cap, while the transverse direction is paid by Lemma 3.1.

This is the weighted replacement for selecting one large physical pair. No individual `w_ij` needs to be bounded below.

## 6. Curved ellipse consequence

### Theorem 6.1 — `QFORM-WEIGHTED-ELLIPSE-AGGREGATION-v1`

Let `r,s` be arbitrary orthonormal vectors in `R^n`, let `lambda_1 lambda_2>0`, and let `X_i` be independent with densities `<=1`. Then

`P=lambda_1<r,X>^2+lambda_2<s,X>^2`

has an essentially bounded density satisfying

`||p_P||_infinity <= pi e / sqrt(|lambda_1 lambda_2|)`.                       (6.1)

In particular, if `|lambda_1|,|lambda_2|>=1`, then `||p_P||_infinity<=pi e`.

### Proof

Let `Y=(<r,X>,<s,X>)`. By Theorem 5.1 its density is at most `e`. Reflect the output if both eigenvalues are negative, so assume `a=lambda_1>0`, `b=lambda_2>0`.

For any interval `I`,

`P(aY_1^2+bY_2^2 in I)`
`<= e * Leb{y in R^2: a y_1^2+b y_2^2 in I}`.

With `z_1=sqrt(a)y_1`, `z_2=sqrt(b)y_2`, the latter area is

`(1/sqrt(ab)) Leb{z: |z|^2 in I}`
`<= (pi/sqrt(ab)) |I|`,

because `Leb{z: |z|^2 in [u,u+h]}<=pi h` for every real interval. Therefore the distribution function is Lipschitz with constant `pi e/sqrt(ab)`, which is equivalent to an essentially bounded density satisfying (6.1). QED.

This proof retains the whole ellipse shell after first performing a dimension-free weighted product aggregation. It never takes the supremum of the original `n`-dimensional product density along spectral fibers.

## 7. Stress test: the partner Hadamard delocalized family

For the partner's positive two-dimensional Hadamard spectral component, each row has

`c_i=2/n`.

Every nonzero pair Plücker weight is of order `n^-2`, so any method selecting one physical pair loses with dimension. The new weighted theorem instead gives

`B_n=(1-2/n)^(-n(1-2/n)/2) < e`,

and hence the pure same-sign spectral quadratic has density at most `pi B_n`, uniformly in `n`. This is exactly the delocalized regime that defeated the finite-coordinate localization strategy.

Thus the conserved determinant mass is genuinely spent: its marginals feed the Brascamp--Lieb exponents, and sharp Hausdorff--Young cancels the corresponding physical-coordinate scaling.

## 8. What is proved, what remains open, and regularity

**PROVED SUPPORTING:**

1. `QFORM-PLUCKER-MARGINAL-v1`, equation (4.1), converting the partner pair-mass measure to exact leverage marginals.
2. `QFORM-1D-PROJECTION-SQRT-E-v1`.
3. `QFORM-WEIGHTED-2D-PROJECTION-v1`, a dimension-free `e` bound for every two-dimensional orthogonal projection of the allowed product laws, with the explicit Plücker-marginal formula (5.2).
4. `QFORM-WEIGHTED-ELLIPSE-AGGREGATION-v1`, the universal `pi e` density bound for an arbitrary rotated same-sign rank-two spectral quadratic component.

**NOT PROVED:** the full quadratic-form conjecture. The remaining spectral quadratic is correlated with the same-sign component under a general product law. Neither a marginal density bound nor a generic X-ray bound can be substituted for the missing correlated trace estimate.

**CONTINUITY:** this report proves essential boundedness for the supporting rank-two component, not the owner's separate full-target continuous-density conclusion. The rank-two same-sign law itself need not have a density continuous across its spectral edge, so no continuity claim is made here.

## 9. Next exact derivation

Attack `QFORM-ORTHOGONAL-CORRELATED-ADDITION-v1` without conditioning on rotated variables. The most direct formulation is to keep the partner Plücker weights inside the full small-ball integral and show that the orthogonal remainder cannot align with the ellipse shell simultaneously across the determinant-mass distribution. A valid closure would replace the marginal estimate (6.1) by a weighted curved-trace estimate for the joint spectral projection. Any attempted proof must survive the flat Hadamard/Walsh frames and the two-sheet X-ray-only counterexample already in the correction inbox.
