# fleet01/B18 — zero-pivot two-dimensional compression closed by LPP + conditional curved trace

**Run:** `20260922T173041Z-qform-B18-a01-r14`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed:** `2026-09-22.8`; mathematical programme revision remains `2026-09-22.5`  
**Assignment:** Literature-to-proof transfer  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The full target remains open: for arbitrary independent real coordinates with probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, prove one universal finite bound for the density of `X^T A X`. Continuity is tracked separately and is not proved by the theorem below.

## 1. Fresh source dependencies

### Primary literature actually transferred

Galyna Livshyts, Grigoris Paouris and Peter Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949, Theorem 1.1. If `Z` has product density `prod_j f_j` with every `||f_j||_infinity<=1`, then every `k`-dimensional orthogonal marginal has density bounded by `2^(k/2)`. No moment, support, log-concavity, centering or identical-law hypothesis is required. I use the `k=2` case:

`||p_(R^T Z)||_infinity <= 2` whenever `R^T R=I_2`.                 (1.1)

This is a joint-density statement; the two projected coordinates are not declared independent.

### Designated partner actually consumed

The latest completed compatible `fleet02/B18` result read in this invocation is

`yspennstate/math-open-problems@7045cf7745ad4f1bb04e5a6e4b3196aeb867a140`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/fleet02-B18-20260922T170013Z-r11/REPORT.md`.

Its theorem `QFORM-ZEROPIVOT-RANK-TRICHOTOMY-v1` states that, for an exact-rank-three symmetric matrix with a zero physical pivot,

`A=[[0,b^T],[b,C]]`,

with `b=b_R+b_N` relative to `Ran(C) direct_sum Ker(C)`, exactly one of the following occurs:

1. `rank C=1` and `b_N!=0`;
2. `rank C=2`, `b_N=0`, and `alpha=b^T C^+b!=0`;
3. `rank C=3`, `b_N=0`, and `alpha=0`.

For `E=Ran(C)+span{b}`, the same partner report proves `dim E=2,2,3` respectively and the exact compression

`Q=Y^T B Y+2 X_i ell^T Y`,  `Y=R_E^T X_{-i}`,                    (1.2)

where `R_E` has orthonormal columns spanning `E`. The original scalar `X_i` is genuinely independent of the whole projected vector `Y`. The partner report left all three compressed curved-trace cases open.

### Fresh analytic theorem applied

The completed fleet01/B16 report visible at source refresh,

`yspennstate/math-open-problems@1bbe7c7c194bc92e10fc9c3cb3eb548d65e7043d`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B16/fleet01-B16-20260922T1705Z-r11/REPORT.md`,

proves `QFORM-ZERO-PIVOT-CONDITIONAL-TRACE-v1`: if `(X,Z_1,Z_2)` is a real random vector, `Z=(Z_1,Z_2)` has joint density cap `M`, the conditional density of `X|Z=z` is bounded by `K`, and `G` is a nonsingular symmetric `3x3` matrix with `G_11=0`, then for arbitrary affine terms

`||p_((X,Z)^T G (X,Z)+affine)||_infinity
 <=3*2^(2/3) (K M)^(2/3) |det G|^(-1/3).`                         (1.3)

The proof is a direct curved-trace calculation; it does not replace conditional density by independence. This exact distinction respects the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`.

## 2. New theorem: the first two partner zero-pivot cases are completely paid

### Theorem — `QFORM-ZEROPIVOT-DIM2-LPP-TRACE-v1`

Let `A` be a real symmetric matrix of **exact rank three**. Assume its three nonzero eigenvalues satisfy `|lambda_j|>=1`. Let `X=(X_1,...,X_n)` have independent real coordinates with probability densities bounded by one. Suppose some physical coordinate `i` has

`A_ii=0`,                                                                  (2.1)

and, in the partner trichotomy for

`A=[[0,b^T],[b,C]]`,                                                       (2.2)

either

- `rank C=1` and the component of `b` in `Ker(C)` is nonzero, or
- `rank C=2`, `b in Ran(C)`, and `b^T C^+ b !=0`.

Then `Q=X^T A X` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 3*2^(4/3) < 7.560. )`                          (2.3)

More precisely, without using the target eigenvalue normalization,

`boxed( ||p_Q||_infinity
       <=3*2^(4/3) |lambda_1 lambda_2 lambda_3|^(-1/3). )`                  (2.4)

No independence of the two projected coordinates is assumed. Continuity is not asserted by this proof.

### Proof

In either of the two stated partner cases, `E=Ran(C)+span{b}` has dimension exactly two. Let `R_E` be an `(n-1) x 2` matrix with orthonormal columns spanning `E`, and set

`Y=R_E^T X_{-i}`.                                                         (2.5)

The partner compression is exact:

`Q=Y^T B Y+2X_i ell^T Y`.                                                 (2.6)

Let

`O=[e_i, R_E]`,                                                           (2.7)

viewed as an `n x 3` matrix after inserting a zero in coordinate `i` in the columns of `R_E`. Its columns are orthonormal. Because `Ran(C) subset E` and `b in E`, symmetry of `C` implies `C` annihilates `E^perp`; hence the whole rank-three matrix is supported on `span(e_i) direct_sum E`. Therefore

`A=O G O^T`,                                                              (2.8)

where

`G=O^T A O=[[0,ell^T],[ell,B]]`.                                          (2.9)

Since `rank A=3`, `G` is nonsingular. Moreover (2.8) with `O^T O=I_3` shows that the eigenvalues of `G` are exactly the three nonzero eigenvalues of `A`; consequently

`|det G|=|lambda_1 lambda_2 lambda_3|`.                                   (2.10)

Now spend the product provenance quantitatively. The scalar `X_i` is independent of `X_{-i}`, hence independent of `Y`. Thus its conditional density given `Y=y` is just its original density and has cap

`K=1`.                                                                     (2.11)

By the primary LPP theorem in dimension two,

`M=||p_Y||_infinity<=2`.                                                   (2.12)

Apply the completed conditional curved-trace estimate (1.3) to the exact three-dimensional random vector `(X_i,Y)` and matrix `G`. Equations (2.10)--(2.12) give

`||p_Q||_infinity
 <=3*2^(2/3) (1*2)^(2/3) |det G|^(-1/3)
 =3*2^(4/3)|lambda_1 lambda_2 lambda_3|^(-1/3).`                           (2.13)

Under the owner normalization `|lambda_j|>=1`, the determinant factor is at most one, proving (2.3). Numerically

`3*2^(4/3)=7.559526299369...`.                                             (2.14)

QED.

## 3. What this closes relative to the designated partner

The designated fleet02/B18 report reduced every exact-rank-three zero physical pivot to three canonical cases but left a product-provenance curved trace unpaid. The theorem above now closes the first **two** cases outright, with no leverage condition, no local-minor lower bound beyond the target determinant itself, and no declaration of independence after projection.

The only partner zero-pivot case left from that trichotomy is therefore the third:

`rank C=3`, `b in Ran(C)`, `alpha=b^T C^(-1)b=0`, `dim E=3`.                (3.1)

Here the exact compression uses `(X_i,Y)` with a three-dimensional projected `Y`, so the effective coordinate count is four while the quadratic matrix has rank three. The two-dimensional receiver theorem (1.3) does not apply. Completing the square gives an algebraic rank-three form in a sheared three-dimensional projection, but that shear mixes `X_i` into `Y`; a bare `L^infinity` cap for the resulting three-dimensional density is not enough for an indefinite quadratic trace. Thus no known live correction is bypassed by declaring case (3.1) solved.

## 4. Relation to the full owner target

This is a target-level branch, not a full solution. It assumes the whole matrix has exact rank three and a zero physical diagonal whose deletion belongs to partner cases 1 or 2. The original theorem permits arbitrary extra spectral components; even a complete exact-rank-three zero-pivot closure would not by itself dispose of them.

The fresh proof-first owner request identifies two remaining structural debts consistent with this result:

1. close the partner case (3.1), equivalently the zero-pivot `rank C=3, alpha=0` product-projection trace, without replacing provenance by a generic bounded joint density;
2. give an exhaustive product-preserving reduction from arbitrary matrices with three large eigenvalues to the existing ridge/grouped-coordinate payments while retaining all extra spectral components.

The first debt is now strictly narrower than in the designated partner report.

## 5. Correction closure

Before publication I refreshed the live correction inbox on brain main. The proof uses none of the refuted mechanisms: no law-uniform pointwise Fresnel decay, no post-rotation independence, no generic fiberwise trace cap, no conditional sum/difference cap, no single good cross minor, no single Schur-rank-two extraction, no bounded-diameter/fixed-fragment localization, and no conditional-cap-as-independence substitution. The only projected-law input is the source-valid LPP joint-density bound (2.12), which is spent inside the proved nonlinear conditional trace inequality (1.3).

## 6. Status

- `QFORM-ZEROPIVOT-DIM2-LPP-TRACE-v1`: **PROVED SUPPORTING TARGET-LEVEL BRANCH**.
- Partner zero-pivot cases 1 and 2: **CLOSED** for exact rank three under the owner eigenvalue normalization, with density cap `<7.560`.
- Partner zero-pivot case 3: **OPEN**.
- Arbitrary additional spectrum: **OPEN**.
- Full QFORM theorem: **OPEN / NOT PROVED**.
- Continuity in the new branch: **NOT CLAIMED / SEPARATE**.

No exact prior literature solution of the full owner statement was found or is claimed. The primary external theorem used is only the sharp projection-density estimate of Livshyts--Paouris--Pivovarov.
