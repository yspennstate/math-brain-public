SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B14, 2026-09-23T14:09:30Z.
attacking: multi-hyperplane Riesz localization — control several simultaneous reciprocal critical slopes through marginal projection caps and generalized Hölder before the physical-pair compiler.

# account03/B14 r37 — multi-hyperplane critical-budget localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T140930Z-account03-B14-QFORM-r37`  
Status: `NEW SUPPORTING LOCALIZATION THEOREM PROVED / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source boundary

The exact owner target is unchanged: for every finite `n`, every independent real input coordinates with one-dimensional probability densities satisfying `0<=f_i<=1`, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove a universal finite essential density bound for `X^T A X`, or give a valid target-level counterexample. No Gaussian, log-concave, moment, compact-support, connected-support, centering, diagonal-coordinate, or post-rotation-independence hypothesis is introduced.


The designated partner actually applied below is account04/B14 r9:

`yspennstate/math-open-problems@63ba8e0f106c3bb405f05eb99778039ff47ed47b:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T101157Z-account04-B14-continuum-perspective-rough-transfer-r9/REPORT.md`.

Its completed physical-pair theorem is used at an explicit inequality in Section 5. For an actual invertible indefinite original-coordinate pair `B`, write

`D=|det B|`, `kappa=s_min(B)`.

If an independent scalar remainder law `mu` obeys

`|hat mu(t)| <= min(1,K/|t|)`,                                  (1.1)

then account04/B14 r9 gives

`||p_Q||_infinity <= F_(D,kappa)(K)`,                           (1.2)

where

`F_(D,kappa)(K)
 := inf_(y>0) [4 sqrt(K/(kappa y)) + D^(-1/2) Omega(y)]`,        (1.3)

`c_E=1/(2 sin^2(1/2))`, and

`Omega(y)=c_E y(2+log(1/y))` for `0<y<=1`,
`Omega(y)=log y+2c_E` for `y>=1`.                               (1.4)

I also use the standard product-projection theorem already source-pinned in prior fleet work: if `Z=(Z_1,...,Z_m)` has independent cap-one densities and `b!=0`, then

`||p_(b^T Z)||_infinity <= sqrt(2)/||b||_2`.                    (1.5)

No joint-density theorem for several projections is used below.

## 2. First essential implication: several singular affine hyperplanes can be paid simultaneously

The previous account03/B14 r36 handled one singular critical factor. The present run proves that an arbitrary finite collection of possibly overlapping affine slopes can be paid with a dimension-free constant as long as the **sum of singular exponents is below the square-root critical threshold two**.

### Lemma 2.1 — one-dimensional translated Riesz bound

Let `W` have a probability density bounded by `M`. For every `0<s<1` and every `a in R`,

`E |W-a|^(-s) <= (2M)^s/(1-s)`.                                (2.1)

Proof: `P(|W-a|<r)<=min(1,2Mr)`. Layer cake for `|W-a|^{-s}` and splitting at `(2M)^s` gives

`E|W-a|^{-s}
 <= (2M)^s + 2M int_((2M)^s)^infinity u^(-1/s) du
 = (2M)^s/(1-s)`.                                               (2.2)

No support or moment input occurs.

### Lemma 2.2 — multi-hyperplane Riesz budget from marginal caps

Let `(W_1,...,W_r)` be an arbitrary jointly distributed vector; independence among the `W_j` is **not** assumed. Suppose the marginal density of `W_j` is bounded by `M_j`. Let `q_j>0` and

`q:=sum_(j=1)^r q_j < 1`.                                       (2.3)

Then, uniformly in arbitrary translations `a_j`,

`boxed:
E prod_(j=1)^r |W_j-a_j|^(-q_j)
 <= [1/(1-q)] prod_(j=1)^r (2M_j)^(q_j).
`                                                                    (2.4)

#### Proof

Set `p_j=q/q_j`. Then `p_j>1` unless there is only one term, and

`sum_j 1/p_j=sum_j q_j/q=1`,
`q_j p_j=q`.                                                     (2.5)

Generalized Hölder therefore yields

`E prod_j |W_j-a_j|^(-q_j)
 <= prod_j [E |W_j-a_j|^(-q)]^(1/p_j).`                         (2.6)

Apply Lemma 2.1 at exponent `q` to every factor:

`[E |W_j-a_j|^(-q)]^(1/p_j)
 <= [(2M_j)^q/(1-q)]^(q_j/q).`                                 (2.7)

Multiplication gives (2.4), because `sum_j q_j/q=1`. QED.

The point is that the slopes may come from the **same** outside product bank and may be maximally dependent. Only their one-dimensional marginal caps are used.

## 3. Product-bank corollary: no dimension, support, fragment, or translation tax

Let `Z=(Z_1,...,Z_m)` have independent cap-one densities. For nonzero coefficient vectors `b_1,...,b_r in R^m`, define

`W_j=b_j^T Z`, `L_j=||b_j||_2`.                                 (3.1)

By (1.5),

`M_j <= sqrt(2)/L_j`.                                           (3.2)

Hence Lemma 2.2 gives, for `q=sum q_j<1`,

`boxed:
sup_(beta_1,...,beta_r)
E prod_j |b_j^T Z+beta_j|^(-q_j)
 <= [1/(1-q)] prod_j (2^(3/2)/L_j)^(q_j).
`                                                                    (3.3)

This estimate is uniform in:

- the bank dimension `m`;
- arbitrary overlap or linear dependence among the `b_j`;
- all physical translations of every `Z_i` (absorbed into the `beta_j`);
- arbitrary distant or infinitely fragmented supports;
- unbounded supports and all moments.

Crucially, the complete product law is aggregated before any reciprocal coefficient is paid. No selected coordinate `1/|b_{j,k}|` appears.

## 4. Main new localization compiler

### Theorem 4.1 — `QFORM-MULTIHYPERPLANE-RIESZ-BUDGET-v1`

Keep the actual invertible indefinite physical pair `B` from Section 1. Let the outside original-coordinate bank `Z` consist of independent cap-one variables. Let `b_j!=0`, `L_j=||b_j||_2`, and let `beta_j in R`. Suppose that, after conditioning on `Z=z`, an independent scalar remainder law `mu_z` satisfies

`|hat mu_z(t)|
 <= min(1, K_0 prod_(j=1)^r |b_j^T z+beta_j|^(-alpha_j) / |t|)` (4.1)

for almost every `z` and every `t!=0`, where `K_0>0`, `alpha_j>0`, and

`alpha:=sum_j alpha_j < 2`.                                     (4.2)

Then the unconditional quadratic output has an essentially bounded density and

`boxed:
||p_Q||_infinity <= F_(D,kappa)(K_eff),
`                                                                    (4.3)

where

`boxed:
K_eff
 = [K_0/(1-alpha/2)^2]
   prod_(j=1)^r (2^(3/2)/L_j)^(alpha_j).
`                                                                    (4.4)

This remains uniform under arbitrary measurable translations of the remainder fibers, because those translations change only Fourier phases.

#### Proof

For fixed `z`, define

`K(z)=K_0 prod_j |b_j^T z+beta_j|^(-alpha_j).`                  (4.5)

Every affine hyperplane `{b_j^T z+beta_j=0}` has product-law probability zero because `b_j^T Z` has an absolutely continuous law. Thus `K(z)<infinity` almost surely.

From (1.2), each conditional output obeys the partner physical-pair envelope `F_(D,kappa)(K(z))`. Define

`H(zeta):=F_(D,kappa)(zeta^2), zeta>=0`.                        (4.6)

By (1.3),

`H(zeta)=inf_(y>0)[4 zeta/sqrt(kappa y)+D^(-1/2)Omega(y)]`.     (4.7)

For every fixed `y`, the bracket is affine increasing in `zeta`; an infimum of affine functions is concave, and the pointwise infimum is increasing here. Therefore conditional interval inequalities plus Jensen give

`||p_Q||_infinity
 <= E H(sqrt(K(Z)))
 <= H(E sqrt(K(Z)))
 = F_(D,kappa)((E sqrt(K(Z)))^2).`                              (4.8)

Now put `q_j=alpha_j/2`. Then `q=sum q_j=alpha/2<1`. Applying (3.3),

`E sqrt(K(Z))
 <= sqrt(K_0)/(1-alpha/2)
    prod_j (2^(3/2)/L_j)^(alpha_j/2).`                         (4.9)

Squaring (4.9) gives exactly (4.4), and substitution into (4.8) proves (4.3). QED.

### Sharp threshold of this interface

The restriction `sum alpha_j<2` is not an artifact of Hölder. If all slopes coincide, `b_j=b`, and `sum alpha_j=2`, then `sqrt(K(Z))` is proportional to `|b^T Z+beta|^{-1}`. For a cap-one law whose projection density is positive near the zero level, that expectation diverges logarithmically. This does **not** refute QFORM; it shows the square-root critical-budget compiler reaches its natural Riesz endpoint at total exponent two.

## 5. Actual designated-partner application: arbitrarily many simultaneous diffuse slopes

Let `X_1,X_2`, `V_1,...,V_r`, and `Z_1,...,Z_m` be mutually independent. Let `X_1,X_2,Z_i` have arbitrary cap-one densities. Let each `V_j` be uniform on an arbitrary interval of length one. Choose nonzero vectors `b_j in R^m`, put

`L_j=||b_j||_2`,
`G=(prod_(j=1)^r L_j)^(1/r)`,                                  (5.1)

and consider the homogeneous quadratic form

`Q=2X_1X_2 + 2 sum_(j=1)^r (b_j^T Z) V_j`.                     (5.2)

No disjointness or orthogonality of the `b_j` is assumed.

### Conditional Fourier tail

Condition on the original outside bank `Z=z` and write `s_j=b_j^Tz`. Translation of the unit interval supporting `V_j` contributes only a phase, and direct integration gives

`|hat mu_z(t)|
 = prod_j |sin(s_j t)/(s_j t)|
 <= prod_j min(1,1/(|s_j||t|)).`                               (5.3)

For numbers `u_j in[0,1]`, `prod_j u_j <= (prod_j u_j)^(1/r)`. Moreover each factor in (5.3) is at most both `1` and `1/(|s_j||t|)`. Hence

`prod_j min(1,1/(|s_j||t|))
 <= min(1, (prod_j |s_j|)^(-1/r)/|t|).`                        (5.4)

Thus (4.1) holds with

`K_0=1`, `alpha_j=1/r`, `alpha=1`.                              (5.5)

Theorem 4.1 therefore gives

`boxed:
K_eff <= 2^(7/2)/G.
`                                                                    (5.6)

For the normalized physical pair `[[0,1],[1,0]]`, `D=kappa=1`, so account04/B14 r9 is now applied at the actual inequality

`||p_Q||_infinity <= F_(1,1)(2^(7/2)/G).`                      (5.7)

When `G>=1`, monotonicity gives `F_(1,1)(2^(7/2)/G)<=F_(1,1)(2^(7/2))`. In (1.3) choose

`y=4*2^(7/2)=2^(11/2)>1`.                                      (5.8)

Then the first term is `2`, while by (1.4)

`Omega(y)=(11/2)log 2 + csc^2(1/2)`.                           (5.9)

Therefore the designated partner theorem yields the explicit dimension-free bound

`boxed:
||p_Q||_infinity
 <= 2 + (11/2)log 2 + csc^2(1/2)
 = 10.162994792419742... .
`                                                                    (5.10)

This is an equation-level application of account04/B14 r9, not a citation-only reference.

### Exact target validity

Let `R` be the `r x m` matrix whose `j`th row is `b_j^T`. The matrix of the `(V,Z)` block in (5.2) is

`[[0,R],[R^T,0]]`,                                              (5.11)

whose nonzero eigenvalues are the pairs `+sigma_k(R),-sigma_k(R)`. Since

`sigma_1(R)>=max_j ||b_j||_2 >= G`,                             (5.12)

`G>=1` implies this block contributes at least one positive and one negative eigenvalue of modulus at least one. The physical pair contributes `+1,-1`. Hence (5.2) lies inside the exact owner target (indeed it has at least four threshold eigenvalues) whenever `G>=1`.

### Diffuse stress family

For any `m` and any `r<=m`, choose mutually orthogonal vectors `b_j` with `||b_j||_2=1`, each spread uniformly across a large coordinate block; for example on disjoint blocks of size `N`, take every nonzero coefficient equal to `N^(-1/2)`. Then every individual physical coupling tends to zero as `N->infinity`, while

`G=1`,                                                          (5.13)

and the singular values of `R` are all one. The target spectrum contains the physical `+/-1` pair and `r` additional `+/-1` pairs. Bound (5.10) is unchanged in `m,r,N`.

The same theorem also permits the `b_j` to overlap or coincide completely. Its proof never assumes independence of the several slope variables `b_j^T Z`; generalized Hölder plus the one-dimensional marginal projection caps is exactly what avoids that false step.

## 6. Localization consequences

This theorem removes a new localization obstruction: **intersections of several moving critical hyperplanes do not force a worst-fiber or reciprocal-coordinate loss as long as their total square-root singular order is below two.** The correct order is:

1. keep the entire original-coordinate outside product bank intact;
2. obtain separate one-dimensional density caps for every linear slope;
3. integrate their simultaneous Riesz singularity by generalized Hölder;
4. average the resulting square-root critical budget;
5. only then invoke the physical-pair logarithmic compiler.

Arbitrary shifts are absorbed into the `beta_j`; distant fragments and unbounded support are allowed directly by the projection theorem and Lemma 2.1; no moment or tail truncation appears.

This is strictly broader than r36's codimension-one theorem because it handles any finite number of **simultaneous, potentially dependent** singular slope factors without requiring a joint projection-density bound. It is also complementary to account01/B14 r37's one-protected-slope fractional-trace localization: here several moving hyperplanes are controlled before the account04 physical-pair Fourier compiler.

## 7. What remains for the full conjecture

Full QFORM is still `OPEN / NOT PROVED / NOT DISPROVED`. The bare hypothesis `s_3(A)>=1` has not been shown to force a uniformly paid indefinite physical pair whose conditional scalar remainder possesses a critical representation of the form (4.1) with total exponent below two. The remaining structural work is to extract such a multi-slope critical budget, or reach one of the fleet's grouped-bank/volume/ridge exits, **before** reciprocal local minors or normalized thin fibers are introduced.

The present argument proves only essential boundedness in its stated branches. It does not establish a continuous density for the unrestricted target. Continuity remains a separate open requirement.

## 8. Arithmetic check

For `K=2^(7/2)` and the explicit choice `y=4K=2^(11/2)`, direct evaluation gives

`K = 11.313708498984761`,
`y = 45.254833995939045`,
`2 + log(y) + csc^2(1/2) = 10.162994792419742`.

No Monte Carlo inference is used.

## 9. Source pins and execution boundary

- Designated partner: `yspennstate/math-open-problems@63ba8e0f106c3bb405f05eb99778039ff47ed47b:proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260923T101157Z-account04-B14-continuum-perspective-rough-transfer-r9/REPORT.md`.
- Previous account03/B14 square-root-budget mechanism: `yspennstate/math-open-problems@29096949260b7ec2e9659c1379bd0a0882a37387:proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T123514Z-account03-B14-QFORM-r35/REPORT.md`.
- Previous account03/B14 codimension-one Riesz mechanism: `yspennstate/math-open-problems@0bf9b3267120208a782afde271ad0564ad52919c:proofnet24/QFORM-density/fleet-2026-09-22/account03/B14/20260923T134259Z-account03-B14-QFORM-r36/REPORT.md`.
- Execution remains `WITHOUT_VERIFIED_BRAIN`: repository retrieval/write/readback is genuine, but authenticated native receiver-memory ingestion was not observed.
- Model self-report: `GPT-5.6 Sol`.
- Configured reasoning effort: `UNKNOWN`; provider reasoning-token and provider-thinking-time counters were not exposed.
- No task/scheduler mutation, email, notification enablement, cross-account authentication, paid API/Codex action, remote workflow, installation work, or public research release was performed.
