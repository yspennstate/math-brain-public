# account02/B05 — aggregate 2D projection cap and hidden-leakage obstruction

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T155206Z-b05-qform-779c4c9b`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREM PROVED / MECHANISM COUNTEREXAMPLE / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval is not native learned-memory ingestion.

## 1. Exact target, corrections, and first unpaid implication attacked

The owner target remains: for every dimension, every independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid target counterexample. No moments, support bounds, spectral-coordinate independence, or sign restrictions are available.

Live corrections consumed before this report include: law-uniform pointwise quadratic-phase decay is false; unrestricted curved-fiber suprema lose dimension; spectral rotation does not preserve independence; a single physical cross minor need not be quantitatively useful; and bounded conditional-density surrogates do not replace genuine original-coordinate product provenance.

The preceding B05 run left `QFORM-POSTSCHUR-CROSS2-EXTRA-SPECTRUM-BRIDGE-v1`. The assigned partner `account03/B05`, in canonical report `yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`, sharpened the local heavy-isotropic coarea interface to `QFORM-PAIR-SECTIONAL-COAREA-v1` and isolated `QFORM-PAIR-PLUCKER-AGGREGATION-v1`: for orthonormal residual coefficient vectors `y,z`, every selected pair pays `|Delta_jk|^(-2/3)` even though `sum Delta_jk^2=1`. The present run attacks exactly whether that reciprocal pair-minor payment can be replaced by an aggregate two-dimensional projection bound.

## 2. A universal two-dimensional product-projection density cap

### Theorem `QFORM-2D-PARSEVAL-PROJECTION-CAP-v1`

Let `X_1,...,X_m` be independent real random variables with probability densities `f_j<=1`. Let `a_j in R^2` satisfy

`sum_j a_j a_j^T = I_2`.

Then

`W=sum_j a_j X_j`

has a bounded density and

`boxed( ||p_W||_infinity <= e ).`                                      (2.1)

This keeps the original independent coordinates throughout; the orthogonal transformations below act only on the two-dimensional **output** and do not assert independence after rotating the inputs.

### Proof: diffuse rows

Write every nonzero row as `a_j=sqrt(c_j) u_j`, where `||u_j||=1` and `c_j=||a_j||^2`. Then

`sum_j c_j u_j u_j^T=I_2`, hence `sum_j c_j=2`.

First suppose `c_j<=1/2` for every `j`. Put `p_j=1/c_j>=2`, `q_j=p_j/(p_j-1)`. With Fourier convention

`phi_j(s)=int exp(isx) f_j(x) dx`,

sharp Hausdorff--Young gives

`||phi_j||_(p_j)
 <= (2pi)^(1/p_j) (q_j^(1/q_j)/p_j^(1/p_j))^(1/2) ||f_j||_(q_j)`.

Since `0<=f_j<=1` and `int f_j=1`, `||f_j||_(q_j)<=1`. Raising to `p_j` and using

`(p/(p-1))^(p-1)<=e`

gives

`int |phi_j(r)|^(1/c_j) dr <= 2pi sqrt(e c_j)`.                         (2.2)

Apply the geometric rank-one Brascamp--Lieb inequality to

`F_j(s)=|phi_j(sqrt(c_j)s)|^(1/c_j)`.

Because the Brascamp--Lieb datum is exactly `sum c_j u_j u_j^T=I_2`,

`int_(R^2) prod_j |phi_j(a_j . t)| dt
 <= prod_j (int_R F_j)^(c_j)`.

By (2.2),

`int F_j = c_j^(-1/2) int |phi_j(r)|^(1/c_j) dr <=2pi sqrt(e)`.

Since `sum c_j=2`,

`||phi_W||_1 <= (2pi sqrt(e))^2=4pi^2 e`.

Fourier inversion therefore gives `||p_W||_infinity<=e`.

### Proof: one localized row

Now suppose some row has `d=||a_1||^2>1/2`. Rotate only the output plane so

`a_1=(sqrt(d),0)`, `a_k=(alpha_k,beta_k)` for `k>=2`.

The Parseval identity yields

`sum_(k>=2) beta_k^2=1`.

Set `T=sum_(k>=2) alpha_k X_k` and `Z=sum_(k>=2) beta_k X_k`. We first use the one-dimensional version of the same argument: every normalized linear form `Z` has

`||p_Z||_infinity<=sqrt(e)`.                                             (2.3)

Indeed, if all squared coefficients are at most `1/2`, the preceding Hausdorff--Young/Brascamp--Lieb calculation in dimension one gives `||phi_Z||_1<=2pi sqrt(e)`; if one squared coefficient exceeds `1/2`, convolution with the remaining independent summands gives the sharper bound `sqrt(2)<sqrt(e)`.

The rotated pair is

`W=(sqrt(d)X_1+T, Z)`.

Conditional on all variables except `X_1`, the first coordinate has density at most `d^(-1/2)`, while `X_1` is genuinely independent of `(T,Z)`. Thus as measures

`P(W in dx dz) <= d^(-1/2) dx P_Z(dz)`,

and by (2.3)

`||p_W||_infinity <= sqrt(e/d) < sqrt(2e) < e`.

This completes the proof of (2.1).

### Meaning for Pluecker aggregation

In the partner heavy-isotropic state the full residual pair

`(Y,Z)=(sum y_j X_j, sum z_j X_j)`

has orthonormal coefficient vectors `y,z`. Hence (2.1) gives

`boxed( ||p_(Y,Z)||_infinity <= e )`                                    (2.4)

with no pair selection and no factor involving `max |Delta_jk|`. Thus the regular-polygon stress frame from the partner report, where every `|Delta_jk|=O(1/m)`, does **not** make the aggregate `(Y,Z)` density large. The dimension tax in the local pair theorem comes specifically from the need to algebraically absorb the leakage variable, not from two-dimensional projection concentration.

## 3. Exact dimension-free closure of the no-leakage aggregate branch

Use the partner's exact rank-three heavy-isotropic normal form. A physical row is `sqrt(c)e` with `c>1/2` and `e^T Lambda e=0`; in the spectral basis `(e,f,g)`,

`Lambda=[[0,B,0],[B,r,s],[0,s,tau]]`,

so `B^2 |tau|=|det Lambda|>=1`. The residual Parseval coordinates satisfy

`Q=2B(sqrt(c)X_i+T)Y+A_0Y^2+tau(Z+kappa Y)^2`.

If the leakage vector is zero, equivalently `T=0`, then `U=sqrt(c)X_i` is genuinely independent of the aggregate pair `(Y,Z)`. Apply the partner theorem `QFORM-PAIR-SECTIONAL-COAREA-v1` with

`M_U=c^(-1/2)`, `M_2=e`, `a=B`, `b=tau`.

It gives

`||p_Q||_infinity
 <=3*2^(2/3)e^(2/3)c^(-1/3)(B^2|tau|)^(-1/3)
 <6 e^(2/3)
 =11.6864042463... .`                                                    (3.1)

This closes the whole no-leakage aggregate branch at once, even when every physical pair minor is `O(1/m)`. No selected pair and no unrestricted curved-fiber supremum appear.

## 4. Pair-density aggregation alone is provably insufficient once hidden leakage is arbitrary

The natural stronger shortcut would be to use only the aggregate cap (2.4) while allowing the hidden leakage `T` in the bilinear factor. That strengthening is false even with the best possible scalar/pair caps.

### Counterexample `QFORM-HIDDEN-SHIFT-PAIR-CAP-INSUFFICIENT-v1`

Let `U,V,Z` be independent `Uniform[-1/2,1/2]`, so `||p_U||_infinity=1` and `||(p_(V,Z))||_infinity=1`. Define the measurable hidden shift

`T(V,Z)=-Z^2/(2V)` for `V!=0`, and `T=0` at `V=0`.

Then

`W=2(U+T)V+Z^2=2UV` almost surely.

For `0<|w|<1/2`, the exact product-density calculation is

`p_W(w)=log(1/(2|w|))`,                                                  (4.1)

which diverges as `w->0`. Therefore there is no theorem of the form

> bounded density of `U` + bounded joint density of `(V,Z)` alone implies a bounded density for `2(U+T(V,Z))V+H(V)+b(Z+theta(V))^2`

when `T` may be an arbitrary measurable function of the pair.

This is a **mechanism counterexample, not a QFORM counterexample**: the shift `T(V,Z)=-Z^2/(2V)` need not arise as a third linear projection of an original product law. Its role is to show exactly what additional structure must be spent. In the true heavy-isotropic QFORM state, `T,Y,Z` are simultaneous linear projections of the same product measure, with coefficient vectors satisfying

`<s,y>=<s,z>=<y,z>=0`, `||s||^2=1-c`, `||y||=||z||=1`.

The next argument must use that linear-product provenance jointly with curvature; replacing it by a pair `L^infinity` cap discards essential information and is blocked by (4.1).

## 5. Exact missing factor after this run

The first unpaid implication is now

`QFORM-PAIR-PLUCKER-HIDDEN-LEAKAGE-AGGREGATION-v1`:

in the exact heavy-isotropic state, exploit the **simultaneous product-linear provenance and orthogonality** of `(T,Y,Z)` to aggregate the full Pluecker mass before reciprocal-minor payment, while retaining the bilinear shift `sqrt(c)X_i+T`. A successful proof must reduce to (3.1) when `s=0` and cannot rely merely on a joint density cap for `(Y,Z)` by the counterexample in Section 4.

This identifies a more precise missing factor than “find a large pair minor”: the missing resource is a curved-trace inequality for a three-projection product law in which the leakage projection is orthogonal, in coefficient space, to the two aggregate transverse projections. The partner's selected-pair theorem remains valid and useful because pairwise algebraic inversion makes the selected leakage an exact function of the selected `(Y,Z)` section; the obstruction is only to global aggregation without spending the third projection's provenance.

Full QFORM remains OPEN. No continuity claim is made here.

## 6. Source ledger

- Fresh brain control at start: `yspennstate/math-research-brain@49f0dab3727d1d6cf4b3e77c494fb3b92a6bea8f`, owner revision `2026-09-22.5`; later pre-write control remained the same programme/revision.
- Assigned partner actually applied: account03/B05, `QFORM-PAIR-SECTIONAL-COAREA-v1`, `yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`.
- Partner's universal rank-two half-Riesz theorem used as background boundary, not as a premise of Sections 2--4: `yspennstate/math-open-problems@bf7bff5c9b11cf495ccbcb09ef48549fd9c0d409`.
- Aggregate Pluecker collar used to interpret the residual structure: account03/B07, `yspennstate/math-open-problems@c3b0a3023962496543da62be43f07bff5ca0865b`.
- Ridge-window theorem read as current global context but not needed for the proof above: `yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`.

## 7. Arithmetic checker

The accompanying `CHECKER.py` checks the constant in (3.1), the sharp-Hausdorff--Young elementary inequality used in (2.2) on representative exponents, and the explicit growth of the density in (4.1). It is an arithmetic sanity check only; the proof above is the universal argument.
