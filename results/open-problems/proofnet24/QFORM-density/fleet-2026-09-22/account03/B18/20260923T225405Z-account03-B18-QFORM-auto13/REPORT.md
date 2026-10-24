SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B18, 2026-09-23T22:54:05Z.
attacking: fresh-coordinate wedge failure via a four-source rank-three compression lemma, then transferring the product-marginal theorem to four disjoint original-coordinate banks.

# account03/B18 — four-source rank-three compression and four-bank transfer

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T225405Z-account03-B18-QFORM-auto13`.
Status: **NEW SUPPORTING IMPLICATION; FULL QFORM OPEN / NOT PROVED**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

No literature-wide novelty claim is made. This report isolates and proves a source-valid implication useful to the structural compiler.

## 1. Main deterministic-probabilistic theorem

### Theorem A — `QFORM-FOUR-SOURCE-RANK3-COMPRESSION-v1`

Let `Z_1,...,Z_4` be independent real random variables with probability densities bounded by one. Let `H=H^T` be a real symmetric `4x4` matrix of rank exactly three, and suppose its three nonzero singular values (equivalently absolute nonzero eigenvalues) are at least `s>0`. Allow any affine term `b^T Z+c`. Then

`Q=Z^T H Z+b^T Z+c`

has an essentially bounded density and

`||p_Q||_infinity < 592/s`.                                      (1.1)

The same conclusion holds conditionally inside an arbitrary ambient quadratic form whenever these four variables are retained as original coordinates and all other original coordinates are conditioned: outside quadratic/cross terms merely induce an affine term in the retained four variables.

Continuity is **not** claimed by this argument.

The proof is a one-coordinate deletion chosen from the kernel, but unlike a fixed-good-minor assertion the coordinate is selected from the exact rank-three kernel and the quantitative payment is automatic.

## 2. Sharp compression lemma

### Lemma B

Let `H=H^T` be `m x m`, `rank(H)=m-1`, and let `z` be a unit vector spanning `ker H`. Suppose every nonzero singular value of `H` is at least `s>0`. For any coordinate `j` with `z_j !=0`, let `C` be the `(m-1)x(m-1)` principal compression obtained by deleting row and column `j`. Then `C` is invertible and

`sigma_min(C) >= s z_j^2`.                                       (2.1)

The constant and exponent are sharp: equality holds for `H=s(I-zz^T)`.

### Proof

First, `C` is invertible. If `Cy=0`, embed `y` as `y_tilde` with `j`-th coordinate zero. Then `H y_tilde` is supported only in coordinate `j`, say `alpha e_j`. Because `range(H)=z^perp`,

`0=<H y_tilde,z>=alpha z_j`,

so `alpha=0`. Hence `y_tilde in ker H=span(z)`. Since `(y_tilde)_j=0` but `z_j!=0`, `y_tilde=0`, hence `y=0`.

Now take arbitrary `x in R^(m-1)` and put `y=C^{-1}x`. Embed it as `y_tilde` with zero `j`-th coordinate and write

`w=H y_tilde=alpha e_j + x_tilde`,

where `x_tilde` is the embedding of `x` with zero `j`-coordinate. Since `w perp z`,

`alpha z_j + <x_tilde,z>=0`.

By Cauchy--Schwarz,

`|alpha| <= sqrt(1-z_j^2)/|z_j| * ||x||`,

hence

`||w|| <= ||x||/|z_j|`.                                         (2.2)

Let `v=P_(z^perp)y_tilde`. Since `H` vanishes on `span(z)` and is invertible on `z^perp` with inverse norm at most `1/s`,

`||v|| <= ||w||/s <= ||x||/(s|z_j|)`.                           (2.3)

Write `y_tilde=v+t z`. The condition `(y_tilde)_j=0` gives `t=-v_j/z_j`. Since `v perp z`, decomposing `v` into its `j` coordinate and the others gives

`|v_j| <= sqrt(1-z_j^2) ||v||`.

Therefore

`||y_tilde||^2=||v||^2+t^2 <= ||v||^2/z_j^2`,

and with (2.3),

`||y||=||y_tilde|| <= ||x||/(s z_j^2)`.

Thus `||C^{-1}|| <= 1/(s z_j^2)`, proving (2.1). For `H=s(I-zz^T)`, the compression is `s(I-z_hat z_hat^T)` and its smallest eigenvalue is exactly `s z_j^2`, proving sharpness. QED.

## 3. Proof of Theorem A

Let `z` span `ker H`, `||z||=1`. Choose `j` for which `z_j^2=max_i z_i^2`. Since there are four coordinates,

`z_j^2 >= 1/4`.                                                  (3.1)

Condition on the original random variable `Z_j`. The remaining three random variables are still genuinely independent with density caps one. Their conditional quadratic matrix is exactly the principal compression `C=H_[4]\{j}`; all dependence on the conditioned value appears only in the affine term.

By Lemma B,

`sigma_min(C) >= s z_j^2 >= s/4`.                               (3.2)

Now apply the already completed three-variable cap-one all-pivot theorem `QFORM-THREE-DISJOINT-BANKS-ALLPIVOTS-v1` in its dimension-three core form: if three independent cap-one real variables have symmetric quadratic matrix with `sigma_min >= tau`, with arbitrary affine terms, then the density is bounded by `<148/tau`. Its proof is the pivot-or-indefinite-pair dichotomy using the completed orientation-free scalar-pivot half-Riesz theorem and the completed indefinite-pair logarithmic smoother.

With `tau=s/4`, every conditional law satisfies

`||p_(Q|Z_j)||_infinity < 148/(s/4)=592/s`.

Averaging the conditional densities proves (1.1).

No random spectral rotation is performed, and no bounded conditional density is substituted for independence: the retained variables are original independent coordinates.

## 4. Primary anti-concentration transfer to four disjoint banks

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949.

Their theorem applies to a product probability density `prod_i f_i(x_i)` with every one-dimensional factor bounded by one, and bounds every `k`-dimensional orthogonal marginal density by `2^(k/2)`. In particular, for every unit vector `u`,

`||p_<u,X>||_infinity <= sqrt(2)`.                               (4.1)

The hypotheses impose none of Gaussianity, log-concavity, finite moments, compact/connected support, iid laws, centering, symmetry, or smoothness.

### Corollary C — `QFORM-FOUR-DISJOINT-BANKS-RANK3-v1`

Let `I_1,...,I_4` be pairwise disjoint sets of original coordinates. For unit vectors `u_k` supported on `I_k`, define

`S_k=<u_k,X_(I_k)>`, `S=(S_1,...,S_4)`.

Suppose that after conditioning on any outside original coordinates the active bank dependence is

`Q=S^T K S + ell^T S+c`,

where `K=K^T` has rank exactly three and its three nonzero eigenvalues have modulus at least `s>0`. Then

`||p_Q||_infinity < 1184/s`.                                    (4.2)

Indeed, disjoint original-coordinate supports make the four `S_k` genuinely independent. By (4.1), `T_k=sqrt(2)S_k` are independent cap-one variables. The quadratic matrix in `T` is `K/2`, whose three nonzero singular values are at least `s/2`. Theorem A therefore gives

`592/(s/2)=1184/s`.

This is an aggregate-before-selection certificate: no individual physical coordinate or physical `3x3` minor needs to be uniformly good once four disjoint scalar banks with a rank-three effective matrix are available.

## 5. Primary quadratic-form regularity theorem: exact scope check

R. Herry, D. Malicet, G. Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488 (published in Probability Theory and Related Fields), studies quadratic forms under substantially stronger input hypotheses: iid inputs with the common law represented as a sufficiently smooth function of a Gaussian field, together with further normalization/spectral hypotheses in its main strong-density applications.

Those assumptions do **not** match the owner target, which permits arbitrary non-iid fragmented cap-one densities with no moments or smoothness. Therefore no Herry--Malicet--Poly theorem is used as a universal replacement here. The source-valid transfer in Section 4 is LPP only, followed by the proved product-preserving nonlinear receiver.

## 6. Designated account04/B18 result applied at an equation

The latest completed designated-partner report is account04/B18 `QFORM-4COORD-NULLHUB-WINDOW-EDGE-DICHOTOMY-v1`, scientific commit

`84fa5922df082f90064dea4d22a600a60e799803`,

path

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T221534Z-account04-B18-QFORM-r5/REPORT.md`.

Its exact scope is an ORIGINAL-coordinate symmetric `4x4` rank-three block `B` with a null physical hub `B_00=0`, spectral window

`s <= |mu_j| <= L`,

and a hub edge of magnitude at least `a`. It proves

`||p||_infinity <= 576^(1/3) L^(2/3)/(s a^(2/3))`.              (6.1)

Apply this literally inside Theorem A on that subbranch. We obtain the combined cap-one estimate

`||p_Q||_infinity <= min(592/s,
  576^(1/3) L^(2/3)/(s a^(2/3)))`.                              (6.2)

Thus the partner theorem is strictly stronger than the generic four-source compression bound whenever

`a/L > (576^(1/3)/592)^(3/2) = 0.0016662059524...`.             (6.3)

A concrete target-valid example is

`B=[[0,1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,0]]`.

Its spectrum is `{1,-1,1,0}`, so `s=L=a=1`. The generic Theorem A gives `<592`, while the designated partner theorem gives the actual sharper inequality

`||p_Q||_infinity <= 576^(1/3)=8.3203352922...`.                (6.4)

For Corollary C after the LPP scaling, the same partner branch applied to `K/2` gives

`||p_Q||_infinity <= 2*576^(1/3) L^(2/3)/(s a^(2/3))`,          (6.5)

so the worked bank-normalized example is bounded by `16.6406705845...`.

This is an actual use of the completed partner result, not a literature citation only.

## 7. Deterministic regression checks

A finite numerical regression (supporting check, not proof) generated 10,000 random orthogonal matrices, spectra `(lambda_1,lambda_2,lambda_3,0)` with `|lambda_i|>=1`, selected the largest kernel coordinate, and computed

`sigma_min(C)/(s z_j^2)`.

The observed minimum was `1.0000495044545215 >=1`. A separate 100-sample equality-family check with `H=s(I-zz^T)` gave ratio in `[0.9999999999999991,1.0000000000000009]`, confirming the sharp identity to floating-point tolerance. The constants `592`, `1184`, `576^(1/3)=8.320335292207616`, and the threshold in (6.3) were independently recomputed.

## 8. Correction audit and remaining implication

This argument uses none of the live-refuted interfaces:

- no law-uniform pointwise van-der-Corput decay;
- no independence after spectral rotation;
- no arbitrary-joint coarea bound;
- no positive conditional-projection-density moment;
- no conditional-cap-as-independence step;
- no naive fiber-sup integration;
- no perturbative deletion of small nonzero coefficients;
- no assertion that the bare spectral hypothesis forces a uniformly good physical minor.

The new theorem is **not** the unrestricted QFORM solution. Bare `s_3(A)>=1` does not force an exact-rank-three four-original-coordinate block, nor four disjoint scalar banks carrying the whole active rank-three matrix, and arbitrary additional spectrum remains part of the compiler problem. The known banked counterexamples to fixed-minor extraction are consistent with this statement: the corollary is invoked only after a genuine four-bank certificate exists.

Full QFORM remains `OPEN / NOT PROVED`. Full-target continuity remains open; this report proves essential boundedness only.

## 9. Source pins

Primary published anti-concentration transfer:
- Livshyts--Paouris--Pivovarov, arXiv:1507.07949 / Israel J. Math. 216 (2016).

Primary quadratic-form scope check:
- Herry--Malicet--Poly, arXiv:2303.09488 / Probability Theory and Related Fields.

Completed internal dimension-three receiver:
- `yspennstate/math-open-problems@602d508c11f3bb5848b65581a750b4497708bd5f:proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260923T112422Z-account03-B18-QFORM-r27/REPORT.md`.

Designated partner actually applied:
- `yspennstate/math-open-problems@84fa5922df082f90064dea4d22a600a60e799803:proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260923T221534Z-account04-B18-QFORM-r5/REPORT.md`.

Fresh pre-write brain head observed: `af8ae63fd29218a01ec01e42a55a079e2719c171`, OWNER CONTROL revision `2026-09-22.15`. Live correction inbox was reread at that head before this report.
