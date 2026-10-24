# account02/B18 — zero-pivot two-bank transfer and isotropic shear ledger

**Run:** `20260922T221352Z-account02-B18-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Status:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Full target and first unpaid implication

The full target remains: for arbitrary independent real coordinates `X_j` with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a single dimension-independent finite bound for the density of `X^T A X`, or give a valid counterexample. No moment, support, centering, log-concavity, smoothness, or independence-after-rotation assumption is introduced here.

This run attacks the exact-rank-three zero-pivot branch isolated in the earlier account02/B18 theorem `QFORM-ZEROPIVOT-RANK-TRICHOTOMY-v1`. The first unpaid implication at entry was the curved trace of a low-dimensional product projection. The newest completed designated-partner result account03/B18 r18 is applied below to close two of the three zero-pivot rank cases with an explicit universal constant.

## 2. Source-matching literature transfer

### 2.1 Livshyts--Paouris--Pivovarov

Primary source: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949.

Exact source scope used here: if `Z=(Z_1,...,Z_m)` has product density `prod f_j` with `||f_j||_infinity<=1` and `E` is a `k`-dimensional subspace, then the density of the orthogonal marginal onto `E` is bounded by `2^(k/2)`. No moments, bounded support, identical laws, symmetry, log-concavity, or smoothness are assumed.

Thus every two-dimensional orthogonal marginal of an original-coordinate product source has joint density cap `2`. This is a joint-density statement only; it does not make the two projected coordinates independent.

### 2.2 Completed designated partner account03/B18 r18

Source-pinned partner handoff: `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/account03/B18/20260922T215805Z-account03-B18-QFORM-r18.md`. Canonical mathematics: `yspennstate/math-open-problems@aa1419c6f3f8559d7eef2030de7275e2d65e6567`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/20260922T215805Z-account03-B18-QFORM-r18/REPORT.md`.

The partner exposes the dependence-safe zero-pivot bound used here. If a scalar `U` is independent of a two-dimensional vector `V`, the scalar density cap is `N`, the pair density cap is `M`, and `H=sup_t E|U-t|^(-1/2)`, then for a nonsingular symmetric `3x3` zero-pivot core `K` the completed zero-pivot argument gives

`||p_Q||_infinity <= 3 N^(1/3) (M H)^(2/3) |det K|^(-1/3)`.

For a physical scalar coordinate with density cap one, `N=1`. Moreover the elementary bathtub bound gives

`H <= integral_{-1/2}^{1/2} |x|^(-1/2) dx = 2 sqrt(2)`.

For a two-dimensional orthogonal product marginal LPP gives `M<=2`. Therefore this particular specialization costs

`3 (4 sqrt(2))^(2/3) = 6*2^(2/3) = 9.52440631180919...`.

This specialization is slightly sharper than treating the physical scalar as a generic linear bank, because its original density cap is exactly one rather than the generic LPP scalar cap `sqrt(2)`.

## 3. Previous exact algebra used as premise

Canonical earlier account02/B18 report: `yspennstate/math-open-problems@a6fb901fe3ca122be86cfff6d2ce6e6d683255d7`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/account02-B18-20260922T170013Z-r11/REPORT.md`.

Let `A` be real symmetric of exact rank three and choose a physical coordinate `i` with `A_ii=0`. After moving `i` first write

`A = [[0,b^T],[b,C]]`.

Let `R=Ran C`, `N=Ker C`, decompose `b=b_R+b_N`, and, when `b_N=0`, put `alpha=b^T C^+ b`. The bordered-rank identity proved there is

`rank A = rank C + 2` if `b_N != 0`,

and

`rank A = rank C + 1_{alpha != 0}` if `b_N=0`.

Since `rank A=3`, exactly three cases occur:

1. `rank C=1`, `b_N !=0`;
2. `rank C=2`, `b_N=0`, `alpha!=0`;
3. `rank C=3`, `b_N=0`, `alpha=0`.

With `E=Ran C + span{b}`, cases 1 and 2 have `dim E=2`, while case 3 has `dim E=3`.

## 4. New theorem: the first two zero-pivot cases are uniformly closed

### Theorem — `QFORM-ZEROPIVOT-NONISOTROPIC-CLOSURE-v1`

Let `A` be a real symmetric exact-rank-three target matrix: its three nonzero eigenvalues satisfy `|lambda_j(A)|>=1`. Assume there is a physical coordinate `i` with `A_ii=0`, and write `A=[[0,b^T],[b,C]]`. If the bordered-rank trichotomy is in case 1 or case 2 above (equivalently `dim(Ran C+span b)=2`), then for every independent cap-one product input `X`, the law of `X^T A X` has a continuous density satisfying

`boxed: ||p_(X^T A X)||_infinity <= 6*2^(2/3) < 9.525.`

#### Proof

Let `E=Ran C+span b`, so `dim E=2`. Choose an orthonormal basis `v,w` of `E` in the residual physical coordinate space and define

`U=X_i`, `V=<v,X_{-i}>`, `W=<w,X_{-i}>`.

Because `U` uses the original coordinate `i` and `(V,W)` uses only the complementary original coordinates, `U` is genuinely independent of the whole pair `(V,W)`. No independence between `V` and `W` is claimed.

Let `P:R^3 -> R^n` be the isometry whose columns are `e_i,(0,v),(0,w)`. Since `C` is symmetric with range contained in `E`, `E^perp` is contained in `Ker C`; also `b in E`. Hence `A` annihilates the orthogonal complement of `span(e_i) direct_sum E`, and

`A = P K P^T`

for the exact active matrix `K=P^T A P`. Its `(1,1)` entry is zero. Since `rank A=3` and the active space is three-dimensional, `K` is nonsingular. Moreover the nonzero spectrum of `A` is exactly the spectrum of `K`, so

`|det K| = product_{j=1}^3 |lambda_j(A)| >=1`.

The quadratic form is exactly

`X^T A X = (U,V,W)^T K (U,V,W)`.

The physical scalar `U` has density cap `N=1` and, by the bathtub principle,

`sup_t E|U-t|^(-1/2) <=2sqrt(2)`.

By LPP the joint density of the orthogonal pair `(V,W)` is at most `M=2`. Applying the completed account03/B18 r18 dependence-safe zero-pivot inequality gives

`||p_Q||_infinity <= 3 * 1^(1/3) * (2*2sqrt(2))^(2/3) * |det K|^(-1/3)`

`<= 6*2^(2/3)`.

The partner theorem also supplies continuity in this no-outside three-variable representation. QED.

### Scope

This is a genuine target-level branch: arbitrary admissible one-dimensional input laws and arbitrary ambient physical dimension are allowed, and the projected pair may be dependent. It is not the unrestricted target because it assumes global exact rank three, an actual zero physical pivot, and excludes the third Schur-isotropic trichotomy case.

## 5. The only surviving exact-rank-three zero-pivot case

The remaining case is

`rank C=3`, `b in Ran C`, `b^T C^(-1)b=0`.

Here `C` is invertible on the three-dimensional active residual space. Put

`u=C^(-1)b`.

Then `u^T C u=0`, and for the three-dimensional residual orthogonal projection `Y` the quadratic form completes exactly as

`Q = Y^T C Y + 2 X_i b^T Y`

`  = (Y+u X_i)^T C (Y+u X_i)`.

This gives two exact identities which sharpen the remaining interface.

### Lemma — `QFORM-ISOTROPIC-SHEAR-LEDGER-v1`

Let `W=Y+uX_i`. Then:

1. `W` is a three-dimensional linear image of the original cap-one product law with coefficient Gram matrix `I+uu^T`;
2. LPP plus the determinant change of variables gives

   `||p_W||_infinity <= 2sqrt(2) / sqrt(1+||u||^2)`;

3. the product of the three nonzero eigenvalues of `A` satisfies the exact pseudodeterminant identity

   `pdet(A) = det(C) (1+||u||^2)`.

#### Proof

In active coordinates the matrix is

`A_active = [[0,u^T C],[C u,C]] = L^T C L`,

where `L=[u,I_3]` is the `3x4` matrix. The coefficient map taking the active physical input to `W` is exactly `L`; hence

`L L^T=I+uu^T`.

Whitening `L` gives a `3x4` matrix with orthonormal rows, so the LPP three-dimensional marginal bound followed by the determinant change of variables yields item 2.

For item 3, the nonzero eigenvalues of `L^T C L` equal those of `(L L^T)C` by the standard `AB/BA` nonzero-spectrum identity. Therefore

`pdet(A)=det((I+uu^T)C)=det(C)det(I+uu^T)=det(C)(1+||u||^2)`.

QED.

Since the target normalization gives `|pdet(A)|>=1`, the scaling-covariant combination cancels exactly:

`||p_W||_infinity^(2/3) |det C|^(-1/3)
 <= 2 |pdet(A)|^(-1/3) <=2`.

This is mathematically important but is **not** a closure: the live correction `QFORM-JOINT-DENSITY-COAREA-23-FALSE-v1` proves that a bound of the form `K ||rho||_infinity^(2/3)|det C|^(-1/3)` is false for an arbitrary dependent three-dimensional density `rho`. The cancellation above can be used only if one proves such a trace inequality for the much narrower class of actual linear images of cap-one product laws, retaining their provenance.

Equivalently, after whitening `W`, the remaining case is exactly a three-dimensional orthogonal projection of a cap-one product law evaluated by a symmetric `3x3` form whose eigenvalues are the three nonzero eigenvalues of `A`. Thus the surviving zero-pivot obstruction is not a hidden rotation-independent problem; it is the exact projected-product rank-three core.

## 6. Literature audit and non-transfers

The LPP theorem transfers exactly because it is formulated for arbitrary cap-one product marginals. It supplies only density caps of linear projections; it does not control a curved quadratic trace by itself.

The newest account03/B18 r18 also source-checks Juškevičius--Lee (arXiv:1503.09190) and Chasapis--König--Tkocz (arXiv:2011.12251) to obtain translation-uniform negative half-moments for one-dimensional aggregate banks. Their hypotheses match such linear banks, and no moment/support assumptions are added. In the theorem above the physical singleton admits the sharper direct half-Riesz constant `2sqrt(2)`, so importing the looser generic-bank constant would only weaken the numerical bound.

No theorem located in this run source-matches the final three-dimensional projected-product quadratic trace. In particular, the corrected arbitrary-joint coarea statement cannot be used, and no independence of projected coordinates is inferred from an orthogonal rotation.

## 7. What changed and exact next implication

Before this run, all three zero-pivot trichotomy cases were part of `QFORM-PROJECTION-PROVENANCE-TRACE-v1`. After applying the newest completed designated-partner zero-pivot packet, cases 1 and 2 are closed with a continuous density bound `<9.525`.

The exact remaining branch is now only the Schur-isotropic case 3. Its cleanest unpaid implication is:

**`QFORM-PRODUCT-PROJECTION-QUADRATIC-TRACE-v1`.** If `Z=S X` with `S S^T=I_3` and `X` has independent cap-one coordinates, and `D=D^T` has all three eigenvalues of modulus at least one, prove

`||p_(Z^T D Z)||_infinity <= C`

for a universal constant, or give a counterexample realized by such an actual product projection.

This is exactly the rank-three projected-product core, not the false arbitrary-joint version. A proof of this implication closes the surviving exact-rank-three zero-pivot branch. The arbitrary-extra-spectrum target still needs the owner-prioritized exhaustive product-preserving reduction to this or another already-paid branch.

## 8. Source pins and correction status

- Fresh control observed for publication work: brain main in the current revision-.15 control epoch; programme revision remains `2026-09-22.5` and full target remains open.
- Earlier zero-pivot trichotomy/compression: `yspennstate/math-open-problems@a6fb901fe3ca122be86cfff6d2ce6e6d683255d7`, path pinned above.
- Completed designated partner account03/B18 r18: `yspennstate/math-open-problems@aa1419c6f3f8559d7eef2030de7275e2d65e6567`.
- LPP primary source: arXiv:1507.07949.
- Juškevičius--Lee: arXiv:1503.09190; Chasapis--König--Tkocz: arXiv:2011.12251, used through the partner source audit only where their hypotheses match.
- Live corrections explicitly respected: arbitrary-joint coarea false; conditional projection positive moments false; no independence after rotation; conditional cap is not independence; fixed-minor/cross-rank dichotomies false.

Manual changed-file review found only mathematical text, public source identifiers, logical fleet labels, and repository-relative paths; no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark material, or public-release action are present.
