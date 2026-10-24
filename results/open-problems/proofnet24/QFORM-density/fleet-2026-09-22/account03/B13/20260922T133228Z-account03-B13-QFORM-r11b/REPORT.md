# account03/B13 — finite projective-bank rank-three theorem

**Run:** `20260922T133228Z-account03-B13-QFORM-r11b`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Extremal product laws  
**Classification:** `PROVED TARGET-LEVEL RANK-THREE SUBCLASS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full conjecture remains **OPEN / NOT PROVED**.

## 1. Exact target and first unpaid implication

The owner target is: for every dimension, every independent real coordinates with marginal densities bounded by one, and every real symmetric matrix with at least three eigenvalues of absolute value at least one, prove a universal essential-density bound for `X^T A X`, or give a valid counterexample.

The preceding B13 run proved zero-loss affine completion, median-zero purification after the exact bang-bang reduction, and refuted every universal bounded-support-diameter localization. Therefore the current structural route must be fragment-blind.

A completed peer theorem from `account02/B13` closes exact rank three when the spectral-frame rows lie in exactly three projective directions, by aggregating each direction bank before any local-minor payment. Its first residual is rank-three frames with four or more projective row directions.

This run proves a quantitative extension to **every finite number `m` of projective row directions**, with an explicit dimension-free constant depending only on `m`. In particular it closes the entire four-direction rank-three residual, including mixed signature. It also gives a sharper four-direction constant in the all-same-sign case by applying the completed four-variable same-sign theorem.

## 2. Source results actually consumed

### 2.1 Peer three-bank aggregation architecture

Consumed in full:

`yspennstate/math-open-problems@9bf04fb890e99db8ddd4e9bfd176f654bc5a82cd`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260922T125435Z-account02-B13-80c2a32d/REPORT.md`.

It proves the exact three-bank factorization and the rank-three density bound `4*pi+6*sqrt(3)<23`.

### 2.2 Three-variable affine quadratic theorem

Consumed in full:

`yspennstate/math-open-problems@289810e1f075755898f573ee5b863ad3fa9af5b8`

`qform/fleet-2026-09-22/account02/B15/20260922T110507Z-account02-B15-qform-pivot-r1/REPORT.md`.

If three independent coordinates have densities at most one and the symmetric `3 x 3` quadratic Hessian has smallest singular value `kappa>0`, then every affine tilt has output density at most

`C3/kappa`, where `C3=2*pi+3*sqrt(3)`.

### 2.3 Same-sign four-variable theorem

Consumed in full:

`yspennstate/math-open-problems@8f66972059845cb23d014fa20efee714b6655b99`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/account02-B12-20260922T1251Z-qform-additional-eigenvalue/REPORT.md`.

Together with the optimized threshold calculation in `account03/B12`, this gives the constant

`Cstar=C3+sqrt(C3^2+3*pi^2)=24.1830382899615...`

for four independent density-one coordinates whenever three eigenvalues are same-sign and have magnitude at least one, uniformly over the fourth eigenvalue and affine tilts.

### 2.4 One-dimensional product marginal theorem

As in the peer B13 proof, use the Livshyts--Paouris--Pivovarov product-marginal theorem: every normalized linear form of independent coordinates whose marginal densities are at most one has density at most `sqrt(2)`.

## 3. Exact finite-bank normal form

Let `A` have rank exactly three and write

`A=R Lambda R^T`,

where `R` is `n x 3`, `R^T R=I_3`, and `Lambda` is real symmetric invertible with

`sigma_min(Lambda)>=1`.

Assume the nonzero row vectors of `R` lie in exactly `m>=3` projective directions. Partition the active physical coordinates into disjoint nonempty banks `G_1,...,G_m`. For `i in G_k`, write

`r_i=alpha_i w_k`,

where `w_k in R^3` is a fixed nonzero representative of the bank direction. Put

`s_k=(sum_{i in G_k} alpha_i^2)^(1/2)`,

`v_k=s_k w_k`.

Define `C` as the `n x m` matrix whose `k`th column is supported on `G_k` and has entries `alpha_i/s_k`. Then the columns of `C` have disjoint supports and unit Euclidean norm, so

`C^T C=I_m`.

Let

`V=[v_1 ... v_m]`, a `3 x m` matrix.

Then

`R=C V^T`.

Using `R^T R=I_3`,

`V V^T=I_3`.                                                (3.1)

Hence `V` is a Parseval frame. Also

`A=C B C^T`, where `B=V^T Lambda V`.                         (3.2)

For the aggregate coordinates

`Y=C^T X`,

the variables `Y_1,...,Y_m` are independent because the columns of `C` use disjoint original coordinate banks. Each is a norm-one linear form, hence

`||p_{Y_k}||_infinity<=sqrt(2)`.                             (3.3)

Finally

`X^T A X=Y^T B Y`.                                          (3.4)

No rotation of the random vector has been made; independence is retained by aggregation in the original coordinate partition.

## 4. Cauchy--Binet selects a quantitatively nondegenerate aggregate triple

For a triple `S subset {1,...,m}`, let `V_S` be the `3 x 3` column submatrix. Cauchy--Binet and (3.1) give

`sum_{|S|=3} det(V_S)^2 = det(VV^T)=1`.                     (4.1)

Therefore some triple `S` satisfies

`det(V_S)^2 >= 1/binom(m,3)`.                               (4.2)

Let `T=V_S` and let the corresponding principal aggregate Hessian be

`B_S=T^T Lambda T`.                                         (4.3)

Write the singular values of `Lambda` as

`mu_1>=mu_2>=mu_3>=1`.

Because `VV^T=I_3`, `||V||=1`; hence every column submatrix satisfies `||T||<=1`. The standard singular-value ideal inequality gives, for `j=1,2`,

`s_j(T^T Lambda T)<=||T||^2 s_j(Lambda)<=mu_j`.              (4.4)

On the other hand,

`|det B_S|=|det Lambda| det(T)^2=mu_1 mu_2 mu_3 det(T)^2`.    (4.5)

Thus

`sigma_min(B_S)
 = |det B_S|/[s_1(B_S)s_2(B_S)]
 >= mu_3 det(T)^2
 >= det(T)^2
 >= 1/binom(m,3)`.                                          (4.6)

This is the decisive quantitative bridge: total Parseval determinant mass becomes one original-product aggregate triple with curvature loss only `binom(m,3)`.

## 5. Main theorem

### Theorem — `QFORM-RANK3-FINITE-PROJECTIVE-BANKS-v1`

Let `X_1,...,X_n` be independent real random variables with probability densities at most one. Let `A` be real symmetric of rank exactly three, with its three nonzero eigenvalues satisfying `|lambda|>=1`. Suppose the nonzero rows of an orthonormal spectral frame for `range(A)` lie in at most `m` projective directions, where `m>=3`.

Then `Q=X^T A X` has an essentially bounded density and

`||p_Q||_infinity <= 2 C3 binom(m,3)`,                      (5.1)

where

`C3=2*pi+3*sqrt(3)`.

#### Proof

Use Sections 3--4 and choose `S` satisfying (4.6). Condition on all aggregate variables `Y_{S^c}`. Since the aggregate variables are independent, the three coordinates `Y_S` retain their original independent marginal laws, each with density at most `sqrt(2)`.

For fixed `Y_{S^c}`, the remaining output is

`Y_S^T B_S Y_S + 2 b^T Y_S + c`,                            (5.2)

where `b,c` depend on the conditioned variables but `B_S` does not.

Set `Z=sqrt(2) Y_S`. Then the three `Z` coordinates are independent with densities at most one, and (5.2) becomes

`Z^T (B_S/2) Z + 2 (b/sqrt(2))^T Z + c`.                    (5.3)

By (4.6),

`sigma_min(B_S/2)>=1/[2 binom(m,3)]`.

The completed three-variable affine theorem therefore bounds every conditional output density by

`2 C3 binom(m,3)`.

Averaging the conditional densities over `Y_{S^c}` preserves the same bound. QED.

### Explicit constants

- `m=3`: `2 C3 = 4*pi+6*sqrt(3) = 22.9586754597...`, recovering the peer theorem.
- `m=4`: `8 C3 = 91.8347018391...`.
- `m=5`: `20 C3 = 229.586754598...`.

The theorem is dimension-free for every fixed projective-direction count and makes no support, moment, connectedness, centering, log-concavity, or sign assumption.

## 6. Four-bank branch: sharper same-sign constant

When `m=4`, the aggregate matrix `B=V^T Lambda V` is `4 x 4`, has rank three, and its three nonzero eigenvalues are exactly the eigenvalues of `Lambda`: `V^T` is an isometry from `R^3` onto the row space of `V` because `VV^T=I_3`.

If the three eigenvalues of `Lambda` have the same sign, then after scaling `Z=sqrt(2)Y`, the matrix `B/2` has three same-sign eigenvalues of magnitude at least `1/2`, and one zero eigenvalue. Applying the optimized four-variable same-sign theorem gives

`||p_Q||_infinity <= 2 Cstar`,                              (6.1)

where

`Cstar=24.1830382899615...`.

Hence

`||p_Q||_infinity <= 48.3660765799231...`                    (6.2)

for the same-sign four-bank rank-three class. The mixed-sign four-bank class is covered by the general bound `8 C3<91.835`.

This is a concrete application of completed partner mathematics to the newly enlarged aggregate geometry.

## 7. Sharpness of the determinant-selection step for four banks

The lower bound `max_S det(V_S)^2>=1/4` in (4.2) is sharp if only the Parseval identity is used. Consider the regular-tetrahedral Parseval frame

`V=(1/2) * [[ 1, 1,-1,-1],
            [ 1,-1, 1,-1],
            [ 1,-1,-1, 1]]`.

Its rows are orthonormal, so `VV^T=I_3`, and every one of the four `3 x 3` column minors has determinant squared exactly `1/4`.

Therefore any improvement to the mixed-sign four-bank constant below the present triple-selection scale must exploit more than the total Cauchy--Binet determinant mass; for example, the four-variable mixed-sign structure itself or a multi-pivot smoother.

## 8. Exact movement of the full target

Before this run, the completed aggregate theorem closed exactly three projective directions and explicitly left `>=4` directions open.

After this run:

1. **every rank-three frame with at most four projective row directions is closed**, including mixed signature;
2. more generally, every rank-three frame with a fixed finite direction count `m` has the explicit bound (5.1);
3. the all-same-sign four-direction branch has the improved bound (6.2);
4. the remaining rank-three structural gap requires **unbounded projective-direction complexity**, or a mechanism that replaces exact collinearity by a robust aggregation/diffuse alternative.

This does not control arbitrary rank greater than three, and the bound grows like `m^3`; therefore it is not the universal theorem.

A useful next implication is a product-preserving dichotomy for an arbitrary rank-three Parseval frame: either (a) finitely many exact/robust banks capture enough determinant mass to invoke this theorem, or (b) a diffuse/low-leverage theorem applies directly, with a dimension-free constant. Approximate-bank stability cannot be obtained by simply perturbing values of `X^TAX`, because the admissible one-dimensional laws have no moment or support-diameter bound.

## 9. Correction and integrity status

Consumed corrections include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`, `QFORM-TWOSHEET-XRAY-ONLY-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`, `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`, `QFORM-BOUNDED-DIAMETER-LOCALIZATION-FALSE`, and `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`.

No false pointwise oscillatory estimate, post-rotation independence, bounded-diameter localization, or single local cross-minor claim is used.

**Full QFORM status: OPEN / NOT PROVED.**  
**Continuity:** not claimed here; this report proves an essential-density bound on the stated subclasses.
