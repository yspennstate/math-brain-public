SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B18, 2026-09-23T18:55:27Z.
attacking: literature-to-proof transfer for a four-coordinate exact-rank-three null-hub core; convert fleet02/B18's planar-twist receiver into a physical cofactor/range-leverage inequality and lift it through original-coordinate conditioning.

# fleet01/B18 r36 — null-hub cofactor transfer

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`; current owner-control revision `2026-09-22.15`.

Status: **PROVED SUPPORTING TARGET-LEVEL IMPLICATION / DESIGNATED PARTNER APPLIED. Full unrestricted QFORM remains OPEN. Continuity is not claimed for the new branch.**

Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh sources and live corrections

Fresh control was read from `yspennstate/math-research-brain` main, initially at `f2a078a553ec43666e2080b751d723eaa5c80760`; before the substantive write main had advanced to `e6f57f046e91b82e284b0489665fbd6768fa0000`, with the same latest owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. Fresh mathematics was read from `yspennstate/math-open-problems` master at `8f2bb69d550ede6f508d421e478cea807a04c192` before the proof work.

I consumed the live corrections, in particular: no arbitrary-joint coarea cap; no conditional-cap-as-independence; no independence after spectral rotation; no uniform pointwise quadratic-phase decay; no universal fixed good minor; and no deletion of a small quadratic term for arbitrary rough unbounded-support laws. None is used below.

The designated partner input is fleet02/B18 commit

`2d20f8bbcbffd1dfc98d85a976237eebe74e5510`

at

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B18/b18-20260923T180826Z-cd3f2e4b/REPORT.md`,

blob `19c616347e55fd234739845868c80720d0cdf69a`.

Its theorem `QFORM-NULLHUB-PLANAR-TWIST-CLOSURE-v1` says that in the exact null-hub normal form

`Q=2(X_0+ell·X_L)(g·X_L)+d(beta·X_L)^2`,

with `||beta||=1`, `beta·g=0`, `gamma=||g||>0`, if for a physical leaf `i`

`q_i=beta_i^2+(g_i/gamma)^2<1`

and the residual twist `ell_{-i}` lies in `span{g_{-i},beta_{-i}}`, then

`||p_Q||_infinity <= [192/(|d| gamma^2(1-q_i))]^(1/3)`.       (1.1)

The proof conditions only an ORIGINAL coordinate, leaves the hub genuinely independent of the residual product block, and permits dependence between the two residual orthogonal projections. The theorem is uniform in the deterministic shifts produced by that conditioning.

## 2. New theorem: `QFORM-4COORD-NULLHUB-COFACTOR-v1`

Let `B` be a real symmetric `4×4` matrix of rank exactly three, indexed by four ORIGINAL coordinates `{0,1,2,3}`. Assume

`B_00=0`,

and let its three nonzero eigenvalues satisfy

`|mu_1|,|mu_2|,|mu_3| >= s>0`.                                  (2.1)

Let `z` be a unit vector spanning `ker B`, and define the range leverage of the physical hub coordinate

`h = ||P_range(B)e_0||^2 = 1-z_0^2`.                             (2.2)

If `h>0`, then for arbitrary independent original-coordinate inputs with densities at most one, and for arbitrary affine terms,

`boxed: ||p_(X^T B X+b^T X+c)||_infinity
        <= 576^(1/3) s^(-1) h^(-1/3).`                           (2.3)

Numerically `576^(1/3)=8.320335292207616...`.

Moreover, if `B` occurs as an ORIGINAL-coordinate principal block of an arbitrary larger symmetric matrix `A`, then after conditioning every coordinate outside this four-set, the same bound (2.3) applies uniformly to the conditional quadratic-plus-affine polynomial. Averaging therefore gives the same essential-density bound for the full ambient form.

This is a supporting theorem. The factor `h^(-1/3)` is not uniformly bounded under the bare full-QFORM hypothesis, so (2.3) is not a proof of the unrestricted conjecture.

## 3. Algebraic normal form

Write the hub decomposition

`B = [[0,g^T],[g,C]]`,                                            (3.1)

where `g in R^3`. Since `h>0`, `e_0` is not in the kernel, hence `g!=0`. Put `gamma=||g||` and `u=g/gamma`.

Let `P=I-u u^T` on the three-dimensional leaf space. Since `rank B=3`, the two-dimensional compression `PCP|_(u^perp)` has rank exactly one. Indeed its rank cannot be two because then the full matrix would be nonsingular; and if it were zero, in the basis `(e_0,u,u^perp)` the three rows belonging to `e_0` and the two transverse leaf directions would all be supported only in the `u` column and hence span at most one dimension, forcing `rank B<=2`.

Therefore there are a unit `beta in u^perp` and `d!=0` such that

`PCP = d beta beta^T`.                                            (3.2)

The remainder `C-d beta beta^T` has zero `u^perp×u^perp` block, so for some `ell in R^3`

`C = g ell^T + ell g^T + d beta beta^T`.                          (3.3)

Thus the associated quadratic form is precisely the designated partner's normal form.

## 4. Exact physical cofactor identity

Delete leaf `i` and let `{j,k}={1,2,3}\{i}`. The physical principal `3×3` block on `{0,j,k}` is

`[[0,G^T],[G, G E^T+E G^T+d Bv Bv^T]]`,                          (4.1)

where `G=(g_j,g_k)`, `E=(ell_j,ell_k)` and `Bv=(beta_j,beta_k)`.

A direct determinant expansion gives the twist-free identity

`det B_{[4]\{i}} = -d (g_j beta_k-g_k beta_j)^2`.                 (4.2)

All `ell` terms cancel exactly. Since `u=g/gamma` and `(u,beta)` is an orthonormal pair in `R^3`, if `e` is the unit vector orthogonal to their span then

`(g_j beta_k-g_k beta_j)^2 = gamma^2 e_i^2`.                      (4.3)

The partner quantity is

`q_i=u_i^2+beta_i^2=1-e_i^2`,                                    (4.4)

so

`boxed: |det B_{[4]\{i}}| = |d| gamma^2(1-q_i).`                 (4.5)

Consequently, whenever this cofactor is nonzero, `q_i<1`. After conditioning the physical leaf `i`, the two remaining leaf coordinates form a two-dimensional space, so the residual twist is AUTOMATICALLY in `span{g_{-i},beta_{-i}}`: nonzero (4.5) says those two vectors are linearly independent. Hence fleet02/B18 applies and (1.1) becomes the physical-coordinate statement

`boxed: ||p_Q||_infinity <= 192^(1/3)|det B_{[4]\{i}}|^(-1/3).`  (4.6)

This is the promised partner-to-actual-inequality transfer.

Arbitrary affine terms cause no problem in this conditioning proof. A hub-linear term is absorbed into the deterministic shift of the factor `L+a`; any residual two-coordinate linear term is absorbed into the square centre and the one-variable remainder after completing the transverse square. No rotated variable is declared independent.

## 5. Adjugate summation supplies a cofactor

Because `B` has rank three and unit kernel vector `z`, spectral decomposition gives the exact adjugate identity

`adj(B) = (mu_1 mu_2 mu_3) z z^T`.                                (5.1)

Therefore every principal cofactor satisfies

`|det B_{[4]\{i}}|=|mu_1 mu_2 mu_3| z_i^2`.                      (5.2)

Sum only the three cofactors that retain the hub:

`sum_{i=1}^3 |det B_{[4]\{i}}|
 = |mu_1 mu_2 mu_3| (z_1^2+z_2^2+z_3^2)
 = |mu_1 mu_2 mu_3| h
 >= s^3 h`.                                                        (5.3)

Hence one leaf `i` obeys

`|det B_{[4]\{i}}| >= s^3 h/3`.                                  (5.4)

Substitution in (4.6) yields

`||p_Q||_infinity
 <= 192^(1/3)(s^3 h/3)^(-1/3)
 = 576^(1/3) s^(-1)h^(-1/3)`,                                    (5.5)

which proves (2.3).

A useful corollary is the uniform subbranch

`h>=eta >0  =>  ||p_Q||_infinity <= 8.321 eta^(-1/3)/s`.          (5.6)

In the leakage-free case `h=1` this gives `8.321/s`. A separately completed pure-hub theorem in the current owner handoff is sharper in its own exact geometry (`<5.361/s`); (5.5) is useful because it is expressed only through the physical four-coordinate block and its range leverage, and it identifies exactly where the cofactor mechanism loses mass.

## 6. Ambient lift

Suppose this `B=A[I,I]` is an original-coordinate principal block of a larger matrix. Condition on all `X_{I^c}=y`. Then

`Q_y(X_I)=X_I^T B X_I+b(y)^T X_I+c(y)`.                           (6.1)

The four retained variables remain independent with their original density caps. Section 4 shows that the partner proof is uniform in the affine vector `b(y)`. Thus for every Borel set `E`

`P(Q in E | X_{I^c}=y) <= C |E|`,

with `C=576^(1/3)s^(-1)h^(-1/3)` independent of `y`. Averaging proves

`P(Q in E)<=C|E|`,                                                  (6.2)

hence the full ambient law has an essentially bounded density with the same bound.

No statement is made about additional eigenvalues of the ambient matrix beyond the existence of this qualifying principal core.

## 7. Primary-literature hypothesis audit

Primary source checked: G. Livshyts, G. Paouris, P. Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), arXiv:1507.07949. Their theorem assumes exactly a product density `prod f_i` with each one-dimensional `||f_i||_infinity<=1` and proves every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. It needs no moments, iid hypothesis, bounded support, log-concavity, centering, symmetry, or smoothness. This is the projection theorem used in the source-valid hub receiver; in the conditioned two-leaf step here the retained source variables are still original independent coordinates, so the product hypothesis is genuinely present.

I also checked Herry--Malicet--Poly, *Regularity of laws via Dirichlet forms -- Application to quadratic forms in independent and identically distributed random variables*, arXiv:2303.09488 / PTRF. Their setting requires iid inputs whose common law is representable as a sufficiently smooth function of a Gaussian field and their main regularity regimes impose additional normalization/spectral assumptions. It therefore does not directly cover the owner's arbitrary non-iid rough cap-one inputs.

No exact published theorem closing all owner quantifiers was found in this targeted source check. This is only a hypothesis comparison; no novelty claim is made.

## 8. What this removes and what remains

The four-coordinate exact-rank-three null-hub core is now paid whenever the hub has a quantitative amount `h` of range leverage. The partner theorem plus adjugate identity replaces a coordinate-by-coordinate search by the deterministic total cofactor currency `s^3 h`.

The precise local failure of this argument is `h -> 0`: the physical hub approaches the one-dimensional kernel, and all three hub-containing principal cofactors can vanish proportionally to `h`. The bare three-large-eigenvalue hypothesis does not by itself forbid this in an arbitrary chosen four-coordinate core. The full target therefore still needs a structural step that either selects a null/small-diagonal hub with `h>=eta`, or routes the low-`h` state into a different paid cross-volume/ridge/grouped-source branch. Additional ambient spectrum must also be handled by such a selection, not discarded perturbatively.

Continuity is tracked separately: this report establishes essential boundedness on (2.3)'s branch. I do not promote a continuous representative from the partner theorem.
