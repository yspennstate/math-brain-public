SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T23:49:26Z.
attacking: the principal-minimal base-subcritical non-Fresnel threshold-transfer gate by sign-resolved Schur inertia; convert the third threshold crossing into an exact normalized carrier and pay the source-valid three-Fresnel subbranch.

# fleet02/B19 auto11b — threshold-normalized Schur carrier at the principal-minimal endpoint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL STEP APPLIED / FIRST GAP SHARPENED / FULL QFORM OPEN**  
Continuity: **not claimed for the full target**.

## 1. Target and fresh source boundary

The target remains: independent original real coordinates `X_i`, each with a probability density bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of `A` with modulus at least one. Prove one universal essential density bound for `X^T A X`, or give a valid counterexample. No moments, support bounds, log-concavity, iid hypothesis, diagonal-basis assumption, or independence after spectral rotation is used.


The designated partner actually used is fleet03/B19 r43:

`yspennstate/math-open-problems@39db1d98a37e71ccc28619a59bc53b79d1be8408`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T220120Z-fleet03-B19-QFORM-r43/REPORT.md`.

Its theorem `QFORM-PRINCIPAL-MINIMAL-INDUCTIVE-REDUCTION-v1` reduces the affine interval-density theorem, with no constant loss, to matrices that are principal-minimal at threshold one. Thus after conditioning any proper ORIGINAL-coordinate bank whose complement already carries three target-scale modes, only the following irreducible state remains:

`N_A(1)>=3`, every proper physical principal block has `N<=2`, and in the finite-core cut `H disjoint_union L` the exact base `D=A[L,L]` satisfies `N_D(1)<=2`.

The same report proves that a principal-minimal full matrix has exactly three threshold-large eigenvalues, or four with mixed signs. This run attacks the stated base-subcritical threshold-transfer debt without discarding any retained coefficient tail.

The owner-required frozen source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Its proved Theorem F is applied in Section 6 below at a real density inequality.

## 2. Sign-specific threshold counts

For a real symmetric matrix `M` and `sigma in {+1,-1}`, define

`p_sigma(M) := #{lambda(sigma M) >= 1}`,

counting multiplicity. Thus

`N_M(1)=p_+(M)+p_-(M)`.

Split the actual coefficient matrix in ORIGINAL coordinates as

`A = [[B,C],[C^T,D]]`,

where `B=A[H,H]`, `D=A[L,L]`, and `C=A[H,L]`.

In a principal-minimal base-subcritical state,

`N_A(1)>=3 > N_D(1)`.

Therefore at least one sign `sigma` satisfies the exact count surplus

`p_sigma(A) > p_sigma(D)`.                                      (2.1)

No perturbation, genericity, or strict-threshold assumption is hidden here; eigenvalues exactly equal to `+1` or `-1` are counted.

## 3. Main theorem — threshold-normalized physical carrier

### Theorem `QFORM-PRINCIPALMINIMAL-THRESHOLD-NORMALIZED-CARRIER-v1`

Let

`A=[[B,C],[C^T,D]]`

be any finite real symmetric block matrix and fix a sign `sigma` such that (2.1) holds. For `0<gamma<=1`, if

`lambda_max(sigma B) <= 1-gamma`,                              (3.1)

then

`|| C P_< (I-sigma D)^(-1/2) ||_op^2 >= gamma`,                (3.2)

where `P_<` is the spectral projection of `sigma D` onto `(-infinity,1)`, and the inverse square root is taken only on that subspace. Equivalently,

`lambda_max( C P_< (I-sigma D)^(-1) P_< C^T ) >= gamma`.       (3.3)

This statement is deterministic coefficient geometry. It does not rotate random variables or assert independence of spectral coordinates.

### Proof

Put `D_sigma=sigma D`. Because the spectra are finite, there is `epsilon_0>0` such that for every `0<epsilon<epsilon_0`, with

`t=1-epsilon`,

no eigenvalue of either `sigma A` or `D_sigma` lies strictly between `t` and `1`. Exact threshold eigenvalues equal to one are above `t`. Hence

`n_+(sigma A-tI)=p_sigma(A)`,
`n_+(D_sigma-tI)=p_sigma(D)`.                                  (3.4)

Choose such an `epsilon` with `t` not an eigenvalue of `D_sigma`. Haynsworth inertia additivity applied to the lower-right block gives

`n_+(sigma A-tI)
 = n_+(D_sigma-tI)+n_+(S_t)`,                                  (3.5)

where

`S_t = sigma B-tI-C(D_sigma-tI)^(-1)C^T`
`    = sigma B-tI+C(tI-D_sigma)^(-1)C^T`.                       (3.6)

By (2.1), (3.4), and (3.5), `S_t` has a positive eigenvalue. From (3.1),

`sigma B-tI <= -(gamma-epsilon)I`,                              (3.7)

so

`lambda_max(C(tI-D_sigma)^(-1)C^T) > gamma-epsilon`.            (3.8)

Write the spectral resolution `D_sigma v_j=mu_j v_j`. Then

`C(tI-D_sigma)^(-1)C^T
 = sum_(mu_j<t) (Cv_j)(Cv_j)^T/(t-mu_j)
   -sum_(mu_j>t) (Cv_j)(Cv_j)^T/(mu_j-t)`.                      (3.9)

The second sum is positive semidefinite and is subtracted. Therefore the first sum alone has top eigenvalue `>gamma-epsilon`. For all sufficiently small `epsilon` its index set is exactly `{mu_j<1}`. Let `epsilon downarrow 0`. The first sum converges in operator norm to

`C P_< (I-D_sigma)^(-1) P_< C^T`,                              (3.10)

which proves (3.3), hence (3.2). QED.

### Exact-threshold point

No separate continuity-in-coefficients or continuity-in-law step is used. Eigenvalues `mu_j=1` of `sigma D` occur in the negative resolvent part for `t<1`; dropping that negative part is legitimate. The limit uses only a finite-dimensional matrix resolvent on the strictly subthreshold spectral subspace.

## 4. Quadratic threshold-transfer law

Let

`c=||C||_op`,
`delta_sigma := min{1-mu : mu in spec(sigma D), mu<1}`.          (4.1)

The set in (4.1) is nonempty whenever the carrier alternative (3.2) holds. On the subthreshold space,

`(I-sigma D)^(-1) <= delta_sigma^(-1) I`,

so (3.3) gives

`gamma <= ||C P_< (I-sigma D)^(-1)P_< C^T||_op
       <= c^2/delta_sigma`.                                     (4.2)

Hence

`boxed: delta_sigma <= c^2/gamma.`                              (4.3)

This is the quantitative threshold-transfer statement missing from the previous assembly. It says that, unless the physical hub block itself approaches the relevant sign threshold, a vanishing physical carrier can only create the extra target eigenvalue by coupling to a base eigenmode whose signed threshold deficit is at most quadratic in the carrier norm.

For the universal choice `gamma=1/2`, every base-subcritical principal-minimal survivor has, for at least one sign `sigma`, the exhaustive dichotomy

`lambda_max(sigma B) >= 1/2`,                                   (4.4)

or

`|| C P_< (I-sigma D)^(-1/2)||_op >= 1/sqrt(2)`                 (4.5)

and simultaneously there is `mu_*<1` in `spec(sigma D)` with

`1-mu_* <= 2 ||C||_op^2`.                                      (4.6)

Thus the former vague phrase “near-threshold base plus vanishing carrier” is replaced by an exact normalized coefficient currency. A receiver that is uniform in (4.5), rather than in `||C||` or in `1-mu_*` separately, has the correct scale.

A stronger parameter-free version is also immediate. If

`b_sigma=lambda_max(sigma B)<1`,

then choose `gamma=1-b_sigma` and obtain

`|| C P_< (I-sigma D)^(-1/2)||_op^2 >= 1-b_sigma`,              (4.7)

`delta_sigma <= ||C||_op^2/(1-b_sigma)`.                        (4.8)

## 5. Sharpness on a target-valid principal-minimal family

The preceding B19 run constructed the exact family on three disjoint original-coordinate ray banks plus one physical hub,

`A_delta = u_+u_+^T-u_-u_-^T+(1-delta)vv^T
           +sqrt(delta)(e_h v^T+v e_h^T)`,                      (5.1)

with `0<delta<=1/2`. Its nonzero spectrum is

`{1,1,-1,-delta}`.                                              (5.2)

For the cut `H={h}`, `L=H^c`,

`B=0`,
`D` has nonzero spectrum `{1,-1,1-delta}`,
`||C||_op^2=delta`.                                             (5.3)

For `sigma=+1`,

`p_+(A_delta)=2 > 1=p_+(D)`,                                   (5.4)

and the only coupled strictly subthreshold positive-side mode is `v`, with gap `delta` and coupling norm squared `delta`. Therefore

`C P_< (I-D)^(-1)P_< C^T = [delta/delta]=[1]`.                 (5.5)

So Theorem 3 is attained exactly at `gamma=1`, and the quadratic relation (4.3) is attained with equality:

`delta_sigma = ||C||_op^2`.                                    (5.6)

This proves that the normalized denominator is not an artifact of the proof and that no replacement of (4.3) by a scale `o(||C||^2)` can hold universally, even inside principal-minimal target-valid matrices.

The deterministic checker accompanying this report verifies 20,027 random qualifying sign instances of Theorem 3 with no violation and checks (5.2)-(5.6) at `delta=1/2,1/10,1/100,1/10000`. It terminates

`QFORM_B19_THRESHOLD_NORMALIZED_CARRIER_CHECK_PASS`.

The numerical check is not used in the proof.

## 6. Frozen-source Theorem F pays the source-valid near-threshold packet

Now apply an actual completed result from the owner-required frozen source `e5f71d79...`.

Theorem F there says: if on some ORIGINAL-coordinate source bank `I`

`A[I,I]=sum_(k=1)^3 lambda_k v_kv_k^T + Delta_I`,                (6.1)

with `Delta_I` physical diagonal, source Gram

`G_I=sum_(i in I) rho_i rho_i^T`,
`rho_i=((v_1)_i,(v_2)_i,(v_3)_i)`,                              (6.2)

and every normalized leverage `rho_i^T G_I^(-1)rho_i<=1/2`, then all outside blocks, couplings and affine terms may be arbitrary and

`||p_Q||_infinity <= 12 (|lambda_1 lambda_2 lambda_3| det G_I)^(-1/3)`. (6.3)

Consequently the threshold-transfer branch is completely paid whenever the two already-available base modes together with the transferred near-threshold mode form such a source-valid three-Fresnel packet with

`|lambda_1|,|lambda_2|>=1`, `|lambda_3|>=1/2`, `det G_I>=g_0>0`,

because then

`boxed: ||p_Q||_infinity <= 12 (2/g_0)^(1/3).`                  (6.4)

For the sharp family (5.1), take `I=U_+ union U_- union V`. The three frame columns are orthonormal on disjoint original-coordinate supports, so `G_I=I_3`; spreading each ray over at least two coordinates makes every leverage at most `1/2`. With coefficients `1,-1,1-delta` and `delta<=1/2`, (6.3) gives the real full-law inequality

`||p_(Q_delta)||_infinity
 <= 12(1-delta)^(-1/3)
 <= 12*2^(1/3)
 =15.1190525987...`.                                            (6.5)

The hub coupling `sqrt(delta)(e_hv^T+v e_h^T)` is retained in the arbitrary outside/cross residual exactly as permitted by Theorem F. Thus the family saturating the new threshold-normalized matrix currency is uniformly easy probabilistically. The unresolved issue is not the vanishing collar itself; it is manufacturing or replacing the source-valid Fresnel packet for a general rough base.

## 7. Source-pinned conditional proof graph after this run

A compact essential-density graph is now:

1. **Principal-minimal descent — PAID.** Fleet03/B19 r43: if any proper physical principal block has three threshold-large eigenvalues, condition its complement and descend with no constant loss. Hence irreducible targets have `N_A(1)=3`, or mixed-sign `4`.
2. **Previously certified nondegenerate exits — PAID at their exact scopes.** Physical scalar/pair/triple receivers, D/D'/D5 and later physical-volume receivers, Fresnel/H, ridge/window, projected crossing, grouped square/hyperbola and latent common-plane payments remain available with their original hypotheses. No one-good-minor converse is assumed.
3. **Finite-core retained-error reduction — PAID structurally.** The r39 compiler quoted by the designated partner leaves a physical cut `H|L`, `|H|<=124`, an exact untouched base `D=A[L,L]`, a rank-at-most-six carrier and a genuine retained operator tail; no coefficient tail may be discarded probabilistically.
4. **Base already target-large — PAID by Step 1.** If `N_D(1)>=3`, condition `H` and descend.
5. **Base-subcritical threshold transfer — NEWLY PAID STRUCTURALLY.** If `N_D(1)<=2`, choose a sign with `p_sigma(A)>p_sigma(D)`. Either the same-sign hub block has eigenvalue at least `1/2`, or the exact normalized carrier (4.5) is at least `1/sqrt(2)` and a base mode lies within `2||C||_op^2` of that signed threshold.
6. **Source-valid transferred Fresnel packet — PAID ANALYTICALLY.** If the two prior modes and the transferred near-threshold mode satisfy the original-bank rank-three-plus-diagonal/leverage gate of frozen-source Theorem F, (6.4) gives a universal density bound; the sharp vanishing-collar family is in this paid chamber.
7. **FIRST REMAINING GATE.** `QFORM-THRESHOLD-NORMALIZED-CARRIER-NONFRESNEL-ROUGH-RECEIVER-v1`: under the exact original-coordinate product law, spend

   `|| C P_< (I-sigma D)^(-1/2)||_op >= 1/sqrt(2)`

   jointly with `N_D(1)<=2`, while allowing arbitrary non-diagonal same-bank curvature, arbitrary subthreshold spectrum (including many modes arbitrarily close to `+/-1`), the retained nonzero finite-core error, arbitrary signs, and arbitrary fragmented/unbounded cap-one laws; or descend to an already-paid physical-volume/Fresnel/ridge/grouped branch.

The parallel hub-self branch `lambda_max(sigma B)>=1/2` remains explicit. It cannot be silently called a good physical pivot: the finite `H` block may have its spectral mass spread over many original coordinates and local scalar/pair/triple pivots can still be tiny.

## 8. Corrections and nonclaims

This proof uses none of the refuted interfaces: no arbitrary-joint coarea bound, no positive moment of a worst conditional projection density, no law-uniform pointwise quadratic-phase decay, no spectral-fiber supremum, no independence after rotation, no universally good single physical minor, and no deletion of a small nonzero coefficient matrix on unbounded inputs.

The theorem is a deterministic structural reduction plus a scoped analytic payment. It does not prove the full unrestricted QFORM theorem, does not prove global continuity, and has not received the two independent end-to-end reviews required for a full candidate.
