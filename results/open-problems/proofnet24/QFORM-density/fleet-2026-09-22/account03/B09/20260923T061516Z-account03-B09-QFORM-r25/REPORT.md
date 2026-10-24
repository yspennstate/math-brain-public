SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T06:15:16Z.
attacking: rank-split physical payment: close the nonzero rank-one physical two-hub core by a product-preserving random-slope/square argument, then splice it into the k=1 torsion-to-wedge branch.

# account03/B09 r25 — rank-one physical hubpair smoothing and k=1 core-rank routing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Bilinear block mechanism  
Status: **NEW SUPPORTING THEOREM / K=1 EXACT CORE-RANK ROUTING ADVANCED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains **OPEN**. This report closes the exact nonzero rank-one physical `2 x 2` core that remained after the newest k=1 torsion-to-wedge extraction. It does not prove a universal lower bound on the new transverse resource, so it does not close the quantitative near-null core regime.

No moment, compact-support, connected-support, Gaussian, log-concave, identical-law, diagonal-basis, or post-rotation-independence assumption is used. No coefficient is discarded as a small random error. All conditioning is on disjoint original-coordinate product variables.

## 1. Fresh sources and the first missing implication

Fresh owner control remained `QFORM-DENSITY-3EIG-20260922`, OWNER CONTROL revision `2026-09-22.15`. The live corrections were reread before this proof; in particular the argument does not use law-uniform pointwise Fresnel decay, arbitrary-joint coarea, conditional spectral-density suprema, or a fixed-good-minor implication.

The newest compatible B09 peer theorem actually used is account02/B09,

`QFORM-K1-TORSION-TO-PHYSICAL-WEDGE-v1`,

canonical report commit

`yspennstate/math-open-problems@ab1efb0930b7a16dc71c32530e155dd521289ab9`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B09/20260923T054256Z-account02-B09-QFORM-auto11/REPORT.md`.

In the k=1 small-disjointness branch it produces a physical leaf `i` and hub `h`, a disjoint outside bank `T`, and cross rows

`a_i=(A_ij)_(j in T)`, `b=(A_hj)_(j in T)`

such that

`Delta_i(T)=||a_i||^2||b||^2-<a_i,b>^2
 >= [eta^2(1-eta)/3] Theta^2`,                                  (1.1)

where `Theta=|det(f,Kf,q)|`. Its report pays the exact-zero physical core by the completed zero-hubpair theorem, but explicitly leaves the genuinely nonzero physical core open.

Two analytic inputs are also source-pinned:

1. account02/B05 `QFORM-RANDOM-SLOPE-HALF-RIESZ-v1` and its independent-square lift, canonical
   `yspennstate/math-open-problems@b6ded18bee0fe20353530653ce654308cac0631c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260922T225232Z-account02-B05-QFORM-37473ccc/REPORT.md`.
   If `X` is independent of an environment `E`, `||p_X||_infinity<=L_X`, the random slope `T(E)` has density cap `L_T`, and `R=K(E)+2XT(E)`, then

   `sup_q E|q-R|^(-1/2) <=4 sqrt(2 L_X L_T)`.                  (1.2)

   Adding a further independent translated square `a[S+psi]^2` gives output density at most

   `4 sqrt(2 L_X L_T) |a|^(-1/2)`.                             (1.3)

2. account02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, canonical
   `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.
   Its `k=1` consequence is: for an original-coordinate product vector `Z` and nonzero coefficient vector `w`,

   `||p_(w dot Z)||_infinity <= sqrt(e)/||w||_2`.               (1.4)

The designated `account04/B09` partner still had no current-QFORM handoff directory or completed QFORM commit in the fresh canonical searches, so no result is attributed to it. The compatible completed account02/B09 theorem above is used asynchronously at an actual inequality in Section 5.

## 2. New theorem: a nonzero rank-one physical pair is a square plus a random slope

Split the independent original coordinates as two physical coordinates `{x,y}` and an arbitrary complementary bank `K`. Write the quadratic-plus-affine polynomial as

`Q = a X^2+2bXY+cY^2
     +2X<u,Z>+2Y<v,Z>+Z^T C Z
     +2 alpha X+2 beta Y+<d,Z>+gamma`,                          (2.1)

where `C` is an arbitrary symmetric matrix and every coordinate of `(X,Y,Z)` has density at most one.

Let the physical pair core be

`E=[[a,b],[b,c]]`.                                              (2.2)

### Theorem `QFORM-RANKONE-HUBPAIR-RANDOM-SLOPE-v1`

Assume `E` has rank exactly one. If `a!=0`, define the Schur-transverse complementary row

`w=v-(b/a)u`.                                                   (2.3)

If `w!=0`, then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2) e^(1/4) (|a| ||w||_2)^(-1/2)
 <7.264 (|a| ||w||_2)^(-1/2).`                                 (2.4)

Consequently every interval `L` satisfies

`boxed:
 P{Q in L}
 <=4 sqrt(2)e^(1/4)(|a| ||w||_2)^(-1/2)|L|.`                  (2.5)

If `a=0`, rank one and nonzero imply `c!=0`; the same theorem holds after swapping `x,y`.

The complementary quadratic matrix `C`, all complementary couplings, and every affine term are arbitrary. Only essential boundedness is asserted; continuity is **not proved** here.

### Proof

Because `rank(E)=1` and `a!=0`,

`c=b^2/a`.                                                       (2.6)

Complete the square in the **original independent coordinate** `X`:

`Q = a [X+(bY+<u,Z>+alpha)/a]^2 + R(Y,Z)`,                    (2.7)

where direct expansion and (2.6) give

`R(Y,Z)=K(Z)+2Y T(Z)`,                                         (2.8)

with

`T(Z)=<w,Z> + beta-b alpha/a`,                                 (2.9)

and `K(Z)` an arbitrary quadratic-affine function of `Z`. Explicitly, every term in `C`, the Schur correction `-uu^T/a`, and the induced affine terms are absorbed into `K`; no size assumption on them is made.

Now `Y` is independent of the original-coordinate environment `Z`, with density cap `L_X=1`. By (1.4), the random slope `T(Z)` has density cap

`L_T <= sqrt(e)/||w||_2`.                                      (2.10)

Apply (1.2) to `R=K(Z)+2YT(Z)`:

`sup_q E|q-R|^(-1/2)
 <=4 sqrt(2 L_T)
 <=4 sqrt(2) e^(1/4)||w||_2^(-1/2).`                           (2.11)

Finally `X` is a further original coordinate independent of `(Y,Z)`. The square in (2.7) is precisely the translated independent-square configuration of (1.3), with coefficient `a` and a translation allowed to depend arbitrarily on `(Y,Z)`. Thus

`||p_Q||_infinity
 <=|a|^(-1/2) sup_q E|q-R|^(-1/2)`,                            (2.12)

which is (2.4). Integrating the density over an interval gives (2.5). QED.

There is no probability squaring and no square-root loss in interval length. The only singular quantity is the half-Riesz potential in (2.11), which is integrable because the **random slope itself has an original-product projection density cap**.

## 3. Coordinate-free rank-one formulation

The preceding formula has a useful invariant interpretation. Write the nonzero rank-one core as

`E=sigma r r^T`, `||r||_2=1`, `sigma!=0`,                      (3.1)

and let `n` be a unit vector orthogonal to `r`. Let

`H=[u,v]`                                                        (3.2)

be the complementary coupling matrix, whose two columns are the full rows from the pair to `K`.

Choose the physical pair coordinate `j` for which `|r_j|>=1/sqrt(2)` and complete that original coordinate. If `j=1`, then

`a=sigma r_1^2`, `b/a=r_2/r_1`,
`Hn=-r_2u+r_1v=r_1 w`.                                        (3.3)

Therefore

`|a| ||w||_2 = |sigma| |r_1| ||Hn||_2
             >= |sigma| ||Hn||_2/sqrt(2)`.                    (3.4)

The swapped case is identical. Hence:

### Corollary `QFORM-RANKONE-HUBPAIR-INVARIANT-v1`

If `E` is nonzero rank one and its internal null direction `n` couples nontrivially to the complementary original-coordinate bank, `Hn!=0`, then

`boxed:
 ||p_Q||_infinity
 <=4*2^(3/4)*e^(1/4)
   (|sigma| ||Hn||_2)^(-1/2)
 <8.638 (|sigma| ||Hn||_2)^(-1/2).`                            (3.5)

Again the same coefficient multiplies every interval length.

If `Hn=0`, then the vector supported on the physical pair with coefficients `n` is an **exact kernel vector of the full quadratic matrix**:

`A (n,0_K)^T=0`.                                               (3.6)

Thus the analytic failure of (3.5) at zero transverse coupling is an exact algebraic kernel endpoint, not an untracked logarithmic singularity.

## 4. Wedge relation for a rank-one core

Let

`Delta(H)=det(H^T H)=||u||^2||v||^2-<u,v>^2`.                 (4.1)

Orthogonally changing the two coefficient labels from the physical basis to `(r,n)` leaves this Gram determinant unchanged:

`Delta(H)
 = ||Hr||^2||Hn||^2-<Hr,Hn>^2
 <= ||Hr||^2||Hn||^2`.                                        (4.2)

Therefore, whenever `Delta(H)>0`,

`||Hn|| >= sqrt(Delta(H))/||Hr||`.                             (4.3)

In particular, a positive two-row wedge automatically rules out the exact-kernel endpoint `Hn=0`. Combining (3.5) and (4.3) gives

`boxed:
 ||p_Q||_infinity
 <=4*2^(3/4)e^(1/4)
    ||Hr||^(1/2)|sigma|^(-1/2) Delta(H)^(-1/4).`               (4.4)

This is useful precisely because the wedge can be extracted by aggregating a disjoint bank **before** selecting a physical core.

## 5. Apply the completed account02/B09 k=1 torsion result

Return to the exact k=1 mixed-hub configuration in account02/B09's theorem (1.1). Let `(i,h)` be its selected physical pair and let `H_T` be the `|T| x 2` matrix whose columns are the two actual cross rows from `(i,h)` to the disjoint outside bank `T`. Then

`Delta(H_T)=Delta_i(T)
 >= [eta^2(1-eta)/3] Theta^2`.                                 (5.1)

Assume the selected physical `2 x 2` core has rank exactly one and write it as `sigma r r^T`. Since the full complementary coupling matrix contains the rows in `T`,

`||H_full n|| >= ||H_T n||`.                                  (5.2)

Put

`M_T=||H_T r||_2`.                                             (5.3)

Because (5.1) is positive when `Theta!=0`, `M_T>0`, and (4.3) applied to `H_T` gives

`||H_full n||
 >= sqrt(Delta_i(T))/M_T
 >= eta sqrt((1-eta)/3) |Theta|/M_T`.                          (5.4)

Insert this **actual inequality** into Corollary (3.5):

`boxed:
 ||p_Q||_infinity
 <=4*2^(3/4)e^(1/4)
   eta^(-1/2)(3/(1-eta))^(1/4)
   [ M_T/(|sigma| |Theta|) ]^(1/2).`                           (5.5)

At the standard partner scale `eta=1/16`,

`boxed:
 ||p_Q||_infinity
 <46.212 [M_T/(|sigma| |Theta|)]^(1/2),`                       (5.6)

and the identical right-hand side times `|L|` bounds `P{Q in L}`.

This is the missing exact-rank-one core payment inside the partner's k=1 torsion branch. It keeps arbitrary same-bank curvature and all outside quadratic coefficients because those enter only the arbitrary `K(Z)` in Section 2 after the physical square completion.

The dependence on `M_T/(|sigma||Theta|)` is explicit and honest. Nothing here proves that this ratio is universally bounded under `s_3(A)>=1`; that quantitative scale-forcing problem is the remaining structural debt.

## 6. Exact algebraic core-rank routing for the selected k=1 pair

Once account02/B09 has produced `Delta_i(T)>0`, every exact algebraic rank/sign of the selected physical core now has an available product-preserving payment:

1. **rank 0:** the pair core is exactly zero. Account02/B09 plus `QFORM-ZERO-HUBPAIR-ARBITRARY-REMAINDER-v1` gives

   `||p_Q||_infinity
    <=2sqrt(2)3^(1/4) eta^(-1/2)(1-eta)^(-1/4)|Theta|^(-1/2)`,

   which is `<15.132 |Theta|^(-1/2)` at `eta=1/16`, with continuous density.

2. **rank 1:** Theorem 2 / Corollary 3 of this report applies. The positive wedge ensures `Hn!=0`; no exact-kernel exception survives.

3. **rank 2, definite:** condition on every complementary original coordinate. Completing the physical pair only translates its center. Since the joint density of the two original independent pair coordinates is at most one, the planar ellipse-shell computation gives directly

   `||p_Q||_infinity <= pi/sqrt(|det E|)`.                      (6.1)

   All complementary quadratic terms are a conditioned translation.

4. **rank 2, indefinite:** the source-pinned full-matrix indefinite-pair theorem in
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`
   gives, with `D=|det E|`, `kappa=sigma_min(E)` and target `s_3(A)>=1`,

   `||p_Q||_infinity
    <=3*400^(1/3) D^(-1/3) kappa^(-1/6)`.                      (6.2)

Thus the k=1 torsion branch no longer has an **unclassified exact core type**. What remains is quantitative degeneration: the rank-one resource `|sigma| ||Hn||`, the definite determinant, or the indefinite pair scales may be arbitrarily small unless the three-large-eigenvalue hypothesis is shown to force another already-paid aggregate exit.

This distinction matters: exact algebraic nonzero cores are paid; a near-zero core cannot be deleted on unbounded inputs and still requires a scale-sensitive structural argument.

## 7. Target-valid regression example

Take three independent cap-one variables and

`A=[[1,1,1],
   [1,1,-1],
   [1,-1,0]].`                                                 (7.1)

The first two physical coordinates have rank-one core

`E=[[1,1],[1,1]] = 2 r r^T`, `r=(1,1)/sqrt(2)`.              (7.2)

Its null vector is `n=(-1,1)/sqrt(2)`. The complementary coupling matrix is the single row

`H=[1,-1]`,                                                     (7.3)

so

`||Hn||=sqrt(2)`.                                              (7.4)

The characteristic polynomial factors as

`(lambda-2)(lambda^2-2)`,                                     (7.5)

so the eigenvalues are exactly

`{2,sqrt(2),-sqrt(2)}`.                                       (7.6)

This is a literal full-target matrix. Corollary (3.5) gives for every admissible product law

`||p_(X^TAX)||_infinity
 <=4*2^(3/4)e^(1/4)(2sqrt(2))^(-1/2)
 <5.137.`                                                       (7.7)

Using the physical pivot directly gives `a=1`, `w=-2` and the same number from (2.4). This is a regression check of the rank-one mechanism, not a claim that the full conjecture has reduced to three variables.

## 8. What remains

The first B09 debt is now

`QFORM-K1-NEARNULL-CORE-SCALE-FORCING-v1`:

> In the k=1 rank-split/torsion survivor, use the strict three-large-eigenvalue geometry to show that either one selected two-hub core has a universal-scale paid resource (zero-core wedge, rank-one `|sigma|||Hn||`, definite determinant, or indefinite pair condition), or route simultaneous degeneration to an existing grouped/ridge/star/finite-core exit. The proof must keep the small nonzero core exactly; it may not erase it as a random perturbation.

The unrestricted QFORM conjecture remains **OPEN**. The full-target continuous-density conclusion remains **OPEN**. This report proves essential boundedness and a direct `O(|L|)` bound on its rank-one branch; it does not establish continuity there.

## 9. Integrity / partner status

- Fresh current-QFORM searches found no completed `account04/B09` handoff directory and no `account04 B09 QFORM` mathematics commit. No designated-partner result was fabricated.
- account02/B09 commit `ab1efb0930b7a16dc71c32530e155dd521289ab9` is applied quantitatively in (5.1)--(5.6).
- account02/B05 random-slope half-Riesz and account02/B06 product-projection bounds are applied at equations (2.10)--(2.12).
- Repository retrieval is not native learned-memory ingestion. Status remains `WITHOUT_VERIFIED_BRAIN`.
- No task, schedule, notification, email, public release, paid model/API/Codex call, credential, or cross-account authentication state was changed.
