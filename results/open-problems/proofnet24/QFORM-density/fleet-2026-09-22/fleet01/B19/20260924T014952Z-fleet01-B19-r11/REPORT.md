SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-24T01:49:52Z.
attacking: the diffuse-D2 punctured common-plane residual from fleet02/B19 — prove a rank-two diagonal-distance inequality that survives arbitrary small nonseparable residual E, then feed it into the physical-pair small-ball receiver without deleting E.

# fleet01/B19 — punctured common-plane residual receiver

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T014952Z-fleet01-B19-r11`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: **not claimed for the new pair-log branch**; the positive physical-E3 exits cited below have continuous `C_0` densities. Full-target continuity remains open.

All random coordinates below are literal ORIGINAL product coordinates. No post-rotation independence, moment bound, support bound, iid assumption, log-concavity, arbitrary-joint coarea estimate, conditional projection-height moment, law-uniform pointwise Fresnel decay, one-good-minor shortcut, or probabilistic deletion of a nonzero coefficient matrix is used.

## 1. Fresh proof graph and source-pinned inputs

The current owner target remains: independent real coordinates with one-dimensional densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. The programme claim is still open.

The exact completed sources consumed in this run are:

1. **Principal-minimal same-constant descent**, fleet03/B19 r43,
   `yspennstate/math-open-problems@ef38106705da5fab5a2fb6dbdd64745206580f62`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T220120Z-fleet03-B19-QFORM-r43/REPORT.md`.
   It proves that the full affine interval theorem reduces without constant loss to ORIGINAL-coordinate principal-minimal matrices. Such matrices have exactly three threshold-large eigenvalues or four with mixed signs. No coefficient tail is deleted.

2. **Restored physical D2 currency**, fleet02/B20,
   `yspennstate/math-open-problems@405fc21676782cde5254f7a7b9709f06e188a672`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260923T225733Z-fleet02-B20-QFORM-auto11/REPORT.md`.
   In the finite-core survivor there is a literal physical hub pair `T` and light bank `L`, with

   `M=A[T,L]`, `G=MM^T`, `S=sqrt(det G)>S0:=1/(480 sqrt(7626))=2.3856699607287348e-5`,

   and leverage `ell_j=m_j^T G^(-1)m_j`. Its diffuse D2 branch is `max_j ell_j<=3/4`; the complementary branch is a literal physical volume-coloop.

3. **Designated partner fleet02/B19**, latest completed aggregate-E3/common-plane-rigidity run,
   `yspennstate/math-open-problems@5633a44f2d0dfefe54240878bc9deb46d315109c`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/fleet02-B19-20260923T231057Z-auto11/REPORT.md`.
   It proves the exact local E3 identity and an aggregate random-cut lift. Writing

   `Zagg=sum_j S^2(1-ell_j)d_j^2`,

   if `Zagg>=2^-60`, one literal physical cross cut has `E3>=2^-64`, and the completed marginal-free E3 theorem gives

   `||p_Q||_infinity <13741`,

   with a continuous `C_0` density. If `Zagg<2^-60` and `max ell_j<=3/4`, the partner proves a **retained**, not deleted, residual representation

   `A[L,L]=Delta+M^T K M+E`,                                      (1.1)

   where `Delta` is diagonal in the original light coordinates, `K=K^T` is `2x2`, `E=E^T`, and

   `||E||op <=2 sqrt(26) sqrt(Zagg)/S
             < epsilon0:=0.00039811307176481383`.                  (1.2)

   The exact-coloop counterexample in the same report shows why the diffuse assumption is essential.

4. **Arbitrary-rank quarter-power small ball / full-matrix physical-pair theorem**,
   `yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.
   For any nonzero symmetric `R0`, arbitrary affine terms, and independent cap-one coordinates,

   `sup_s P(|Y^T R0 Y+linear-s|<rho)
       <=min(1,5(rho/||R0||op)^(1/4))`.                            (1.3)

5. **Physical indefinite-pair logarithmic envelope**,
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   If a literal independent coordinate pair has invertible indefinite coefficient matrix `B`, with

   `D_B=|det B|`, `kappa=sigma_min(B)`,                             (1.4)

   and completion leaves a remainder random variable `R`, then for every `r>0`

   `p_Q(t)<=2sqrt(2)/r
      +D_B^(-1/2) E log_+(2r^2/(kappa |t-R|))`.                    (1.5)

The last two sources allow arbitrary signs, all extra spectrum, arbitrary affine terms, and arbitrary independent cap-one input laws. They prove essential boundedness, not continuity.

## 2. The first missing inequality: a rank-two common-plane matrix cannot be hidden by a physical diagonal

The partner's representation (1.1) gives exactly the geometry for which the older rank-one diagonal witness should be replaced by a rank-two statement.

Let `V` be a real `r x m` matrix satisfying

`V V^T=I_r`,                                                        (2.1)

and let its physical columns be `v_i`, with

`||v_i||^2<=alpha<1`.                                               (2.2)

Let `T=T^T` be a nonzero `r x r` matrix of rank `r0`, and let `Delta` be an arbitrary real diagonal `m x m` matrix.

### Lemma 2.1 — `QFORM-RANKR-DIAGONAL-DISTANCE-LEVERAGE-v1`

One has

`boxed:
 ||Delta+V^T T V||op
 >= (1-alpha)/(2 r0) tr|T|
 >= (1-alpha)/(2 r0) ||T||op.`                                    (2.3)

For the live rank-at-most-two state this implies the uniform bound

`boxed:
 ||Delta+V^T T V||op >= (1-alpha)||T||op/4.`                       (2.4)

This includes positive definite, negative definite, indefinite, rank-one, repeated-eigenvalue, and singular `T` (with `r0=rank T` for `T!=0`).

### Proof

Let

`P=sgn(T)`                                                         (2.5)

on the support of `T`, with zero on `ker T`. Put

`U=V^T P V`,
`H=U-diag(U)`.                                                      (2.6)

Then `H` has zero diagonal, so

`tr(H Delta)=0`.                                                    (2.7)

Because `V V^T=I_r`, the nonzero singular values of `V^T P V` are the nonzero singular values of `P`, hence

`||U||_* = r0`.                                                     (2.8)

Moreover

`||diag U||_*
 =sum_i |v_i^T P v_i|
 <=sum_i v_i^T |P| v_i
 =tr(|P| V V^T)
 =r0`.                                                             (2.9)

Thus

`||H||_*<=2r0`.                                                     (2.10)

Now pair `H` with the common-plane matrix. The full, non-diagonalized trace is

`tr(U V^T T V)
 =tr(P V V^T T V V^T)
 =tr(P T)
 =tr|T|`.                                                          (2.11)

For the removed diagonal part, using `|v_i^T P v_i|<=||v_i||^2<=alpha` and `|v_i^T T v_i|<=v_i^T |T|v_i`,

`|tr(diag(U) V^T T V)|
 <=alpha sum_i v_i^T |T|v_i
 =alpha tr|T|`.                                                     (2.12)

Therefore

`|tr(H(Delta+V^T T V))|
 =|tr(H V^T T V)|
 >=(1-alpha)tr|T|`.                                                (2.13)

Operator/nuclear duality and (2.10) give (2.3). QED.

The point is that this is a coefficient identity in the **original physical light coordinates**. The spectral sign matrix `P` is used only as a deterministic trace witness. No rotated random coordinate is introduced.

## 3. Robust version: retain the partner's nonzero residual exactly

Now include an arbitrary real symmetric error matrix `E`, with

`epsilon=||E||op`.                                                  (3.1)

By Weyl / the triangle inequality and Lemma 2.1,

`boxed:
 ||Delta+V^T T V+E||op
 >= (1-alpha)||T||op/4-epsilon.`                                  (3.2)

This is the first essential inequality attacked in this run. It is deliberately a lower bound on the **actual completed remainder matrix**, not an assertion that `X^T E X` is probabilistically small.

## 4. Apply the partner common-plane state to an actual density inequality

Work in the fleet02/B19 diffuse D2 branch (1.1)-(1.2). Condition only on all original hub variables in `H\T`. The two coordinates indexed by `T` and every light coordinate remain independent with their original density caps. The conditioned variables enter only through affine/constant terms.

Let

`B=A[T,T]`.                                                        (4.1)

Assume first that `B` is invertible indefinite. Completing these two literal coordinates leaves on the untouched light bank the exact quadratic matrix

`R0
 =Delta+M^T(K-B^(-1))M+E`.                                      (4.2)

Normalize the physical two-frame by

`V=G^(-1/2)M`, so `V V^T=I_2`,                                   (4.3)

and define the normalized mismatch

`T0=G^(1/2)(K-B^(-1))G^(1/2)`,
`mu=||T0||op`.                                                     (4.4)

Then

`M^T(K-B^(-1))M=V^T T0 V`,                                       (4.5)

while `||v_i||^2=ell_i<=3/4`. Hence Lemma 2.1 and (3.2) give

`boxed:
 ||R0||op >= mu/16-epsilon.`                                      (4.6)

No sign restriction on `T0` is needed. If `T0` has rank one, (2.3) actually gives `mu/8` before subtracting `epsilon`; the uniform `mu/16` is chosen to cover rank two and all degeneracies with one formula.

Define

`delta:=mu/16-epsilon`.                                            (4.7)

Whenever `delta>0`, apply the completed arbitrary-rank theorem (1.3) to the **actual** matrix `R0`, obtaining for every affine term

`sup_s P(|R-s|<rho)
 <=5 (rho/delta)^(1/4)`.                                           (4.8)

This is a direct application of completed peer mathematics to a new equation supplied by the designated partner; the residual `E` remains inside `R0` throughout.

## 5. Feed (4.8) into the physical-pair logarithmic transducer

From (1.5), with `a=2r^2/kappa`, layer cake gives

`E log_+(a/|t-R|)
 =int_0^infinity P(|t-R|<a e^(-v)) dv
 <=20 delta^(-1/4) a^(1/4)`.                                     (5.1)

Therefore

`p_Q(t)
 <=2sqrt(2) r^(-1)
   +20*2^(1/4) D_B^(-1/2) kappa^(-1/4) delta^(-1/4) r^(1/2)`.     (5.2)

For `A/r+B sqrt(r)`, the exact minimum is

`3(A B^2/4)^(1/3)`.                                                (5.3)

Substituting into (5.2) gives the new receiver

### Theorem 5.1 — `QFORM-DIFFUSE-D2-PUNCTURED-MISMATCH-RECEIVER-v1`

Under the partner diffuse D2 representation (1.1), after conditioning `H\T`, if the physical pair `B=A[T,T]` is invertible indefinite and

`delta=mu/16-||E||op>0`,                                          (5.4)

then the full ambient quadratic form has an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity
 <=3*400^(1/3) (D_B^2 kappa delta)^(-1/6).`                        (5.5)

Every same-bank coefficient, the full nonzero residual `E`, all outside couplings, all affine terms, arbitrary additional spectrum, every sign pattern and every arbitrary independent cap-one law are retained. Continuity is not asserted by this pair-log proof.

The statement survives the rank-two-to-rank-one degeneration of `T0`; only the true near-latent scale `mu comparable to ||E||op` remains outside it.

## 6. Quantitative live consequence at the partner scale

In the partner's unpaid aggregate-E3 branch,

`alpha<=3/4`,
`epsilon<epsilon0=0.00039811307176481383`.                          (6.1)

If

`mu>=32 epsilon`,                                                  (6.2)

then (4.6) gives

`delta>=mu/32`.                                                     (6.3)

Hence Theorem 5.1 yields

`boxed:
 ||p_Q||_infinity
 <=3*400^(1/3)*32^(1/6)
   (D_B^2 kappa mu)^(-1/6)
 <39.385188 (D_B^2 kappa mu)^(-1/6).`                              (6.4)

In particular, if also

`D_B^2 kappa mu >=2^-60`,                                         (6.5)

then

`boxed: ||p_Q||_infinity <40331.`                                 (6.6)

Thus every **unpaid** diffuse-D2 punctured common-plane state with an invertible indefinite physical hub pair must satisfy at least one of the two explicit collars

`boxed:
 mu<32 epsilon <=0.012739618296474043,`                            (6.7)

or

`boxed:
 D_B^2 kappa mu<2^-60.`                                           (6.8)

Using the partner's exact retained-error estimate rather than the numerical cap, the near-latent collar can be written invariantly as

`boxed:
 mu <64 sqrt(26) sqrt(Zagg)/S.`                                   (6.9)

This is the main structural gain of the run: the entire punctured common-plane chamber away from a quantitatively near-latent mismatch and away from a genuinely weak physical-pair/mismatch product is paid. The residual is never set to zero.

## 7. Definite, singular, coloop and exact/near-latent endpoints

The signs of the physical pair are not hidden in Theorem 5.1.

* If `B` is definite and invertible, the completed pair source gives the direct conditional ellipse bound

  `||p_Q||_infinity <=pi/sqrt(|det B|)`,                           (7.1)

  so any fixed lower bound on `|det B|` pays that branch. A nearly singular definite pair remains a weak-pair collar.

* If `B` is singular, pair inversion is not used. This remains a separate structural branch.

* If some light leverage exceeds `3/4`, the designated partner explicitly keeps a physical D2-coloop branch. The partner's exact-coloop construction shows that it cannot be folded into the common-plane formula merely from `Zagg=0`.

* If `T0=0` exactly, then `mu=0` and Theorem 5.1 deliberately says nothing: after pair completion the light quadratic matrix is `Delta+E`. This is the retained-residual version of the exact latent cancellation center.

* More generally (6.7)/(6.9) is the true punctured near-latent collar. Since arbitrary cap-one laws can be unbounded and have no moments, the small coefficient residual `E` cannot be deleted as a random perturbation.

## 8. Compact conditional proof assembly after this run

The current full-proof graph can be stated without pretending that the final splice is done.

1. By fleet03/B19 r43, it suffices with no constant loss to prove the affine interval theorem for principal-minimal matrices; only three threshold-large eigenvalues or four mixed-sign threshold-large eigenvalues remain.
2. The existing finite-core compilers either pay already-certified determinant/ridge/volume branches or restore a literal physical D2 pair `T,L` with `S>S0`.
3. Fleet02/B19 converts total transverse self-curvature into aggregate physical `E3`. If `Zagg>=2^-60`, the full law is paid by `<13741` and is `C_0`.
4. If `Zagg<2^-60` and `max ell_j<=3/4`, the partner produces the retained representation `Delta+M^T K M+E` with (1.2). This run now pays every invertible-indefinite-pair state satisfying (6.2)-(6.5), uniformly through rank-one mismatch degeneration.
5. What remains locally is therefore sharply named rather than amorphous: the physical D2-coloop branch; singular/quantitatively weak physical hub pairs; and the near-latent retained-residual collar (6.9), including its exact center. Other global branches already separated by the finite-core compiler, such as the threshold-transfer physical-heavy-row/star closure, must still be spliced into one of these paid mechanisms.

Accordingly the first unresolved implication after this theorem is

`QFORM-DIFFUSE-D2-NEARLATENT-OR-WEAKPAIR-COUPLED-PAYMENT-v1`:

> in the principal-minimal finite-core state, spend jointly the robust two-volume `S>S0`, a diffuse physical two-frame `max ell_j<=3/4`, and either `mu<64 sqrt(26) sqrt(Zagg)/S` with the retained nonzero `E`, or `D_B^2 kappa mu<2^-60`, without dividing by one tiny physical coefficient and without deleting the coefficient residual.

The coloop branch remains a parallel explicit obligation.

## 9. Verification notes

The deterministic proof of Lemma 2.1 is trace/nuclear-norm algebra and does not depend on computation. As a regression check, `5000` random Parseval two-frames, arbitrary symmetric `2x2 T`, and arbitrary diagonals produced no violation of (2.4); an additional `5000` random trials with an arbitrary symmetric residual scaled below half of the deterministic margin produced no violation of (3.2). These checks are not evidence for the full theorem.

Numerically,

`3*400^(1/3)*32^(1/6)=39.38518727672824`,

`39.38518727672824*2^10=40330.43177136972`,

`32*epsilon0=0.012739618296474043`.

## 10. Status

This run proves a new supporting theorem and applies the designated partner's completed mathematics at an actual density inequality. It does **not** prove or disprove the unrestricted conjecture. The full target and global continuity remain open. Execution remains `WITHOUT_VERIFIED_BRAIN`.