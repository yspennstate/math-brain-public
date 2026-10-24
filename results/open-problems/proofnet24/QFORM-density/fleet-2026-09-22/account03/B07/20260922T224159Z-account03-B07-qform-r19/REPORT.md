SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T22:41:59Z.
attacking: the two-star curvature survivor after the new checkerboard-wedge reduction — integrate the two physical anchors before the outside quadratic core, then isolate the genuinely tiny-nonzero-pivot remainder.

# account03/B07 r19 — coefficient-plane smoothing and a large-row tiny-pivot collar

**Run:** `20260922T224159Z-account03-B07-qform-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Fresh control at start:** `yspennstate/math-research-brain@8f4fc3081c4197ab549d4aa2b3bde859a10de324`, OWNER CONTROL revision `2026-09-22.15`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING THEOREMS / FULL TARGET OPEN`.

## 1. Exact target and corrected incoming state

The owner target is unchanged: for every dimension, independent real original coordinates with marginal probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `X^T A X`, or give a target-valid counterexample. No moment, support, Gaussian, log-concavity, connected-support, or post-rotation-independence assumption is introduced. Continuity remains a separate requested conclusion.

The live correction ledger was reread. In particular this run does **not** use a law-uniform pointwise van-der-Corput estimate, arbitrary-joint rank-three coarea, conditional-cap-as-independence, a fiber supremum, deletion of a small coefficient under unrestricted supports, or selection of one tiny coordinate minor followed by a reciprocal determinant payment.

The newest directly relevant coordinate-minor result is account02/B07:

`yspennstate/math-open-problems@a0ae0928c71cf3de71d748c416a6dceb012562b2`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260922T213439Z-account02-B07-QFORM-e7b269/REPORT.md`.

Combining the current O0 currency `E_3(B)>=1/256` with the compound-order transfer, it improves the two-sided near-coloop reserve to

`b^2 ||C||_F^2 >1/200`

or

`P:=||r||_2^2 ||c||_2^2 >1/200`.                               (1.1)

For the second alternative it puts the two physical anchors on one side of the checkerboard cut. If `u,v` are the same-side outside couplings and

`a=(u,r)`, `q=(c,v)`,

then the actual two-row checkerboard cross block is

`D=[a^T; q^T]`,                                                   (1.2)

and exactly

`E_2(D)=det(DD^T)
       =||u wedge c||^2+||r wedge v||^2+||u v^T-c r^T||_F^2`.   (1.3)

If `E_2(D)>=P/16`, its completed two-cross theorem already gives a source-valid half-Riesz payment with **arbitrary same-side curvature retained**. If `E_2(D)<P/16`, the rows are quantitatively near-collinear; this is the genuine near-leaf survivor.

The present run first proves a direct anchor-integration theorem that shows why arbitrary *outside* quadratic curvature is harmless once the two anchor coefficients retain two-dimensional area. It then splices the two-star reserve to exact-zero and discriminant scalar-pivot theorems, narrowing the remaining scalar-Schur obstruction to a large outside row with a genuinely tiny **nonzero** diagonal.

The designated `account04/B07` still has no completed current-QFORM handoff/canonical report at the fresh source check. I therefore do not fabricate one. The compatible completed account04 theorem actually used below is account04/B18's sharp one-dimensional product-projection transfer:

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B18/20260922T182500Z-account04-B18-QFORM-r2/REPORT.md`.

Its Ball--Rogozin consequence is: if `L=sum c_j X_j` is a normalized linear projection of independent cap-one original coordinates, then `||p_L||_infinity<=sqrt(2)`. This is applied to an actual half-Riesz inequality in Section 5.

## 2. A general coefficient-plane smoothing lemma

The key elementary fact is that two original scalar anchors can be integrated **before** any outside quadratic core. Let `X_1,X_2` be independent cap-one real variables. Let `Z` be any random object independent of `(X_1,X_2)`. Let

`L(Z)=(L_1(Z),L_2(Z))`

have an absolutely continuous law on `R^2` with joint density bounded by `K<infinity`, and let `H(Z)` be an arbitrary measurable real function, with no independence assumed between `H` and `L`.

Define

`R=2L_1(Z)X_1+2L_2(Z)X_2+H(Z)`.                                 (2.1)

### Theorem 2.1 — `QFORM-TWO-ANCHOR-COEFFICIENT-PLANE-v1`

The law of `R` has a bounded **continuous** density and

`boxed: ||p_R||_infinity <= 2 sqrt(K).`                          (2.2)

No regularity, moment, or support hypothesis on any input is required, and `H(Z)` may contain arbitrary quadratic curvature and arbitrary cross terms among the outside coordinates.

### Proof

Fix `Z=z` and write `ell_j=L_j(z)`. Except on a `Z`-null set, `(ell_1,ell_2)!=(0,0)` because the joint law of `L` has a density. The conditional law of

`2ell_1 X_1+2ell_2 X_2`

has a density. Its essential supremum is at most

`m(ell):=min(1/(2|ell_1|),1/(2|ell_2|))
        =1/[2 max(|ell_1|,|ell_2|)]`,                            (2.3)

with the convention `1/0=infinity`. Indeed, when both coefficients are nonzero this is the elementary convolution bound `||f*g||_infinity<=min(||f||_infinity,||g||_infinity)`; when exactly one coefficient vanishes, the nonzero scaled anchor gives the same finite value.

Put `R_L=max(|L_1|,|L_2|)`. The joint density cap gives for every `r>0`

`P(R_L<=r)<=min(1,4K r^2)`.                                     (2.4)

Layer cake now yields

`E R_L^(-1)
 =int_0^infinity P(R_L<t^(-1)) dt`
`<=int_0^(2sqrt(K)) 1 dt
   +int_(2sqrt(K))^infinity 4K t^(-2) dt`
`=4sqrt(K).`                                                     (2.5)

Averaging (2.3) therefore gives

`||p_R||_infinity<=E m(L)<=2sqrt(K)`,                            (2.6)

proving boundedness and absolute continuity.

For almost every `z`, both `ell_1` and `ell_2` are nonzero, so the conditional density is the convolution of two `L^1` densities and is continuous. Its translate by `H(z)` is also continuous. Equation (2.3) supplies the integrable dominating function `m(L(z))`; hence dominated convergence shows that the mixture density is continuous. QED.

The point is structural: **all outside curvature is inside the translation `H(Z)` and never needs to be conditioned through a rotated complement.** The only quantitative currency is the genuine two-dimensional spread of the two anchor coefficient forms.

## 3. Original-coordinate version via aggregate second compound

Let `Z=(Z_1,...,Z_m)` consist of independent cap-one original coordinates. Let

`L_1=a^T Z+alpha`, `L_2=q^T Z+beta`,

and put

`D=[a^T; q^T]`.                                                   (3.1)

Assume `rank(D)=2`. Write

`Delta_2(D)=sigma_1(D)sigma_2(D)=sqrt(det(DD^T))`.               (3.2)

The completed two-dimensional product-projection theorem gives the joint cap

`||p_(L_1,L_2)||_infinity <= 2/Delta_2(D)`.                      (3.3)

For source pinning, the same product-projection input is recorded and applied in account01/B16,

`yspennstate/math-open-problems@e8c7ac4f0294a028d4bc883d1e4bf1c805e11085`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B16/qform-b16-20260922T213856Z-r11/REPORT.md`.

Applying Theorem 2.1 gives:

### Corollary 3.1 — `QFORM-TWO-ZERO-ANCHOR-AGGREGATE-DENSITY-v1`

For

`R=2X_1(a^T Z+alpha)+2X_2(q^T Z+beta)+H(Z)`                    (3.4)

with arbitrary measurable `H(Z)`,

`boxed:
 ||p_R||_infinity
 <=2sqrt(2) Delta_2(D)^(-1/2)
 =2sqrt(2) E_2(D)^(-1/4).
`                                                                  (3.5)

The density is continuous. Consequently

`boxed:
 H_(1/2)(R):=sup_t E|R-t|^(-1/2)
 <=2^(9/4) E_2(D)^(-1/8).
`                                                                  (3.6)

Indeed any probability density bounded by `M` obeys

`sup_t E|R-t|^(-1/2)<=2sqrt(2M)`,                                (3.7)

by the same bathtub/layer-cake argument.

Equation (3.5) aggregates the whole coefficient-plane area before any reciprocal payment. No individual `2x2` minor is selected.

## 4. Actual O0 application: the zero anchor-block wedge branch is continuously paid

Return to the current B07 two-star state (1.1)-(1.3). Suppose the two anchor variables have **zero quadratic block among themselves** in the residual being estimated: both anchor diagonals are zero and their mutual coefficient is zero. No condition is imposed on the outside block; it may contain arbitrary quadratic terms inside either bank and arbitrary cross-core curvature between the banks.

Then the residual has exactly the form (3.4), with coefficient matrix equal to the checkerboard `D` from (1.2). Therefore, whenever the account02/B07 wedge gate holds,

`E_2(D)>=P/16`,                                                   (4.1)

Corollary 3.1 gives

`||p_R||_infinity
 <=2sqrt(2)(P/16)^(-1/4)
 =4sqrt(2) P^(-1/4).`                                            (4.2)

On the current O0 reserve `P>1/200`,

`boxed: ||p_R||_infinity < 4sqrt(2) 200^(1/4)
                          =21.2731835878... .`                   (4.3)

Moreover

`boxed: H_(1/2)(R)<2^(11/4) 200^(1/8)
                         =13.0455152717... .`                    (4.4)

This is a strict analytic strengthening at this exact zero-anchor-block scope: the earlier checkerboard theorem supplies a half-Riesz estimate while retaining arbitrary anchor curvature; (4.3) additionally proves a **continuous density** and shows that arbitrary curvature in the outside banks/core itself costs nothing once the two random anchor coefficients retain two-dimensional area.

The theorem does **not** delete a nonzero anchor square or a nonzero anchor-to-anchor edge. Those terms are genuinely different; a hyperbolic product can have a logarithmically unbounded density at its critical value even when its half-Riesz potential is finite.

## 5. A sharper exact-zero large-row exit using the completed account04 theorem

The two-star reserve itself forces at least one anchor to have a large total coupling to the outside coordinates, even if all individual coefficients are tiny.

In the notation (1.2), put

`beta_i=||a||_2=||(u,r)||_2`,
`beta_j=||q||_2=||(c,v)||_2`.                                   (5.1)

Then

`beta_i beta_j >= ||r||_2 ||c||_2 = sqrt(P)`,                   (5.2)

so

`boxed: max(beta_i,beta_j)>=P^(1/4)>200^(-1/4).`                (5.3)

Choose an anchor `h` attaining that maximum.

Assume now that its residual diagonal coefficient is **exactly zero**. Condition on all variables except `X_h`. The residual is affine in `X_h`:

`R=W X_h+G`,                                                     (5.4)

where `G` is arbitrary and the coefficient `W` is twice a linear form in the remaining independent original coordinates. Its coefficient Euclidean norm is at least `2 beta_h` (the possible mutual-anchor edge only makes it larger).

Here the compatible completed account04/B18 result is applied at the actual inequality. Its sharp Ball--Rogozin projection cap gives

`||p_W||_infinity <= 1/(sqrt(2) beta_h)`.                        (5.5)

For fixed `W=w`, the cap-one anchor gives

`E_(X_h)|wX_h+G-t|^(-1/2)<=2sqrt(2)|w|^(-1/2)`.                  (5.6)

For a scalar density cap `M`, the translation-uniform negative half moment is at most `2sqrt(2M)`. Averaging (5.6), using (5.5), yields the sharpened exact-zero estimate

`boxed:
 H_(1/2)(R) <=2^(11/4) beta_h^(-1/2).
`                                                                  (5.7)

Combining with (5.3),

`boxed:
 H_(1/2)(R)<2^(11/4) P^(-1/8)
          <2^(11/4)200^(1/8)
          =13.0455152717... .
`                                                                  (5.8)

This is the same numerical collar as (4.4), but it requires only **one exact-zero large-row anchor** and permits arbitrary curvature everywhere else, including a nonzero mutual anchor edge and an arbitrary square on the other anchor.

For comparison, account01/B06's earlier zero-diagonal theorem used the weaker `sqrt(e)` projection cap. Equation (5.7) is the direct `sqrt(2)` sharpening supplied by the completed account04/B18 source.

## 6. Large-row pivot collar in a scalar-Schur S0 parent

There is a second useful splice when this B07 packet sits inside the exact scalar-Schur S0 route of account02/B19. In that parent one has, for the residual symmetric matrix `S`,

`s_2(S)>=1`.                                                       (6.1)

This is the source-pinned scalar-Schur inheritance theorem in

`yspennstate/math-open-problems@fc8343c379bbddf14be670349f664f7fcb39994a`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T192830Z-account02-B19-qform-r17/REPORT.md`.

Keep the large-row anchor `h` selected by (5.3), and write `d=S_hh`.

If `d!=0`, take the further scalar Schur complement `T` after pivoting on `h`. Since `S` differs from `diag(0,T)` by a rank-one matrix, singular-value interlacing gives

`||T||_op>=s_2(S)>=1`.                                           (6.2)

Apply the completed discriminant half-Riesz theorem account01/B06,

`yspennstate/math-open-problems@c396b6e553f98ca1cd735ae10eb0e6ec24a96cc4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B06/20260922T193442Z-qform-r15-b06/REPORT.md`:

`H_(1/2)(R)<=96 |d|^(-3/8)||T||_op^(-1/8).`                     (6.3)

Thus, if

`|d|>=1/16`,                                                      (6.4)

then

`boxed: H_(1/2)(R)<=96*16^(3/8)
                         =271.5290039757... .`                  (6.5)

Together with Section 5 this proves the following source-valid collar.

### Corollary 6.1 — `QFORM-TWOSTAR-LARGE-ROW-PIVOT-COLLAR-v1`

In a scalar-Schur S0 residual with `s_2(S)>=1` and the current two-star reserve `P>1/200`, select the anchor with larger outside-row norm. Then:

1. if its diagonal is exactly zero, the residual has `H_(1/2)<13.046`;
2. if its diagonal has modulus at least `1/16`, the residual has `H_(1/2)<271.530`;
3. therefore every state escaping these two payments has a **large physical outside row**

`beta_h>200^(-1/4)`                                               (6.6)

and a genuinely tiny but nonzero diagonal

`0<|S_hh|<1/16`.                                                  (6.7)

The distinction between (6.7) and the exact-zero branch is essential. The live correction and the account01/B06 rank-one-square example show that one may not simply replace a tiny nonzero diagonal by zero under unrestricted supports.

This is the first place where the current two-star aggregate reserve and the corrected near-zero-pivot analysis meet quantitatively.

## 7. What is paid and what remains

The previous r18 report left “arbitrary same-bank curvature and the residual cross core” as part of the two-star debt. The present run separates that debt more sharply.

**Paid now:**

- If the two physical anchors are genuinely linear and their random outside coefficients have two-dimensional area, arbitrary outside quadratic curvature/cross-core terms are harmless; Theorem 2.1 and Corollary 3.1 give a bounded continuous density.
- On the current `P>1/200` wedge gate with a zero anchor block, the explicit residual bounds are (4.3)-(4.4).
- If only one selected large-row anchor has exact zero diagonal, arbitrary remaining curvature is paid by (5.8), using the completed account04/B18 projection theorem.
- In the scalar-Schur S0 parent, a quantitative nonzero diagonal `|d|>=1/16` is paid by the discriminant theorem and (6.5).

**Not paid:**

- the genuinely tiny-nonzero large-row pivot (6.6)-(6.7);
- the account02/B07 near-leaf geometry when the checkerboard coefficient area is `<P/16` and the anchor block does not fall into one of the paid exact-zero/quantitative-pivot exits;
- the sibling edge-times-bank alternative `b^2||C||_F^2>1/200`;
- O1/O2/O3 and the remaining global synthesis debts.

Accordingly the first unpaid implication for this slot becomes

`QFORM-O0-LARGE-ROW-TINY-NONZERO-PIVOT-v1` (OPEN):

> In the source-valid O0/S0 near-coloop state, after the checkerboard-wedge payment and the exact-zero/quantitative-pivot collar above, control the surviving large outside-row anchor satisfying `beta>200^(-1/4)` and `0<|d|<1/16` without treating `d` as zero. Use the discriminant and the aggregate row currency jointly, or force an already-paid pair-log, second-pivot, grouped-square, exact-cross-rank, or ridge branch.

A successful next step should keep the quadratic discriminant until after the source-product averaging. The known rank-one-square correction shows that coefficient smallness alone is not a valid perturbative argument.

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Global continuity remains open. Continuity is proved here only in Theorem 2.1 / Corollary 3.1 and their exact scope.

## 8. Exact numerical checks

The deterministic constants used above are

`2sqrt(2)*3200^(1/4)=21.273183587779954...`,

`2^(11/4)*200^(1/8)=13.045515271626478...`,

`96*16^(3/8)=271.5290039756343...`.

The layer-cake identity behind (2.5) is exactly

`2sqrt(K)+4K/(2sqrt(K))=4sqrt(K)`.

These checks are algebraic/numerical regression only; the proofs are the displayed inequalities.

**Native brain ingestion:** not verified. Repository reads/writes are not authenticated learned-memory receiver use, so this run remains `WITHOUT_VERIFIED_BRAIN`.
