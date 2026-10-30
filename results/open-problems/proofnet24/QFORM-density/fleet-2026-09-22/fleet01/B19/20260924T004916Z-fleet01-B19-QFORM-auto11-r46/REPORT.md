SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-24T00:49:16Z.
attacking: the threshold-normalized non-Fresnel carrier; convert the normalized Schur currency into a literal original-coordinate source/receiver alternative and pay one branch with a completed peer theorem.

# fleet01/B19 r46 — multiplicity threshold transfer and diffuse-base payment

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Universal proof assembly / SYNTHESIS  
Status: **ESSENTIAL STEP APPLIED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full-target continuity: **OPEN**.

## 1. Scope and source boundary

The target remains the unrestricted statement: independent real original-coordinate variables `X_i`, each with probability density bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No moment, support, iid, log-concavity, smoothness, or sign assumption is made. No spectral rotation of the product law is used.


The designated partner mathematics actually used is fleet02/B19 auto11b, canonical source

`yspennstate/math-open-problems@da594097550f0b88ea54c6989b252ae347a2d2f3`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T234926Z-fleet02-B19-QFORM-auto11b/REPORT.md`.

Its theorem `QFORM-PRINCIPALMINIMAL-THRESHOLD-NORMALIZED-CARRIER-v1` proves, for a physical block split

`A=[[B,C],[C^T,D]]`,

that if one signed threshold count increases from `D` to `A` and `lambda_max(sigma B)<=1-gamma`, then

`|| C P_< (I-sigma D)^(-1/2)||_op^2 >= gamma`.                 (1.1)

The partner also identifies the first rough unresolved interface as spending this normalized carrier without assuming a source-valid three-Fresnel packet.

The second completed input used at an actual density inequality is the ridge-window theorem, source

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,

`proofnet24/QFORM-density/interactive/20260922T151048Z-ridge-window/REPORT.md`,

and its strengthened window frontier in fleet01/B08 r30. The theorem works on literal original-coordinate cross blocks, retains arbitrary self blocks, outside coordinates and couplings, permits arbitrary coordinate-separable terms, and yields a continuous `C_0` density.

Current corrections were preserved. In particular, nothing below uses law-uniform pointwise Fresnel decay, arbitrary-joint coarea, positive conditional projection-density moments, a fiber supremum, one-good-minor inversion, independence after rotation, or deletion of a small coefficient tail.

## 2. Signed threshold notation

For `sigma in {+1,-1}` define

`p_sigma(M)=#{lambda(sigma M)>=1}`,

counting multiplicity. For the physical principal block `D`, Cauchy interlacing gives

`p_sigma(A)>=p_sigma(D)`.

Put

`k_sigma=p_sigma(A)-p_sigma(D)>=0`.                                (2.1)

The partner theorem handles the case `k_sigma>=1`. The first new step is to retain the entire multiplicity `k_sigma`.

## 3. Main deterministic theorem: multiplicity threshold-normalized carrier

### Theorem `QFORM-THRESHOLD-CARRIER-MULTIPLICITY-TRANSFER-v1`

Let

`A=[[B,C],[C^T,D]]`

be a finite real symmetric matrix in original coordinates. Fix `sigma in {+1,-1}` and write `k=k_sigma`. Assume `k>=1` and, for some `0<gamma<=1`,

`lambda_max(sigma B)<=1-gamma`.                                   (3.1)

Let `P_<` denote the spectral projection of `sigma D` onto `(-infinity,1)`. Then

`boxed:
 lambda_k( C P_< (I-sigma D)^(-1) P_< C^T ) >= gamma.`          (3.2)

Here eigenvalues of the positive semidefinite matrix in (3.2) are in decreasing order. Equivalently, the normalized carrier

`W_sigma=C P_< (I-sigma D)^(-1/2)`

has at least `k` singular values at least `sqrt(gamma)`.

### Proof

Choose `epsilon>0` small enough that `t=1-epsilon` lies outside both spectra and no eigenvalue of `sigma A` or `sigma D` lies strictly between `t` and `1`. Then

`n_+(sigma A-tI)=p_sigma(A)`,
`n_+(sigma D-tI)=p_sigma(D)`.                                    (3.3)

Haynsworth inertia additivity, applied to the lower-right block, gives

`n_+(S_t)=k`,                                                     (3.4)

where

`S_t=sigma B-tI+C(tI-sigma D)^(-1)C^T`.                         (3.5)

Resolve the last term spectrally. If `sigma D v_j=mu_j v_j`, write

`P_t=sum_(mu_j<t) (Cv_j)(Cv_j)^T/(t-mu_j)`,
`N_t=sum_(mu_j>t) (Cv_j)(Cv_j)^T/(mu_j-t)`.

Then `P_t,N_t>=0` and

`S_t=sigma B-tI+P_t-N_t
    <=-(gamma-epsilon)I+P_t`,                                   (3.6)

using (3.1). Since (3.4) says the `k`-th largest eigenvalue of `S_t` is strictly positive, Loewner monotonicity and (3.6) imply

`lambda_k(P_t)>gamma-epsilon`.                                  (3.7)

For all sufficiently small `epsilon`, the positive-resolvent index set is exactly `{mu_j<1}`. Let `epsilon downarrow0`. The finite-dimensional matrices `P_t` converge in operator norm to

`C P_< (I-sigma D)^(-1) P_< C^T`,

and (3.2) follows. Exact eigenvalues `mu_j=1` remain in the negative-resolvent part for `t<1`; no genericity assumption or threshold perturbation is used. QED.

This strictly strengthens the partner's equation (1.1) from the largest normalized carrier direction to every signed threshold-count surplus direction.

## 4. Quadratic near-threshold multiplicity transfer

Put

`c=||C||_op`.

For `Delta>0`, split the strictly subthreshold spectral space of `sigma D` into

`E_near={1-Delta<=mu<1}`,
`E_far={mu<1-Delta}`.

Correspondingly write the carrier Gram matrix in (3.2) as

`M=M_near+M_far`.

On the far space the inverse gap is at most `1/Delta`, hence

`0<=M_far
 <=Delta^(-1) C P_far C^T
 <=(c^2/Delta) I`.                                                (4.1)

Take

`Delta=2c^2/gamma`.                                                (4.2)

Then (3.2), (4.1), and Weyl's inequality give

`lambda_k(M_near)>=gamma-c^2/Delta=gamma/2`.                      (4.3)

Therefore `rank(M_near)>=k`; in particular `sigma D` has at least `k` eigenvalues in the literal interval

`[1-2c^2/gamma,1)`.                                               (4.4)

Thus the count surplus does not merely create one unspecified near-threshold base mode. Every missing signed target mode is transferred into a base mode at a gap quadratic in the physical carrier norm.

### Both-sign corollary

Assume

`||B||_op<=1/2`.                                                   (4.5)

Then (3.1) holds for both signs with `gamma=1/2`. Suppose also

`c=||C||_op<=1/8`.                                                 (4.6)

Now `Delta=4c^2<=1/16`, so the positive- and negative-side near-threshold intervals are disjoint. Applying (4.4) for `sigma=+1` and `sigma=-1` and adding the exact threshold modes already present in `D`, we obtain

`#{lambda(D): |lambda(D)|>=1-4c^2}
 >= p_+(D)+p_-(D)+k_++k_-
 = p_+(A)+p_-(A)
 = N_A(1).`                                                        (4.7)

Hence every target matrix with `N_A(1)>=3` satisfying (4.5)-(4.6) has

`boxed:
 N_D(15/16)>=3.`                                                   (4.8)

This is sign-free, includes repeated and exact-threshold eigenvalues, and never rotates the input variables.

## 5. Actual analytic payment of the diffuse base

The new deterministic transfer is useful because the completed ridge-window theorem can now be applied to the **physical base block `D` at a fixed absolute scale**.

Let

`L0=15/16`,
`P_D=1_{|D|>=L0/39}`.

Assume the transferred base is physically diffuse at this window:

`max_{i in L} (P_D)_{ii} <=1/32`.                                (5.1)

Apply the completed spectral-window frontier with

`ell=1/32`, `tau=1/39`, `q=1`, `r=1/2`.

Its frame parameter is

`delta_w=1/2-sqrt(2ell)-ell=7/32`,
`sigma_w=delta_w-tau=241/1248`.                                  (5.2)

The two admissibility inequalities are, numerically and strictly,

`(sqrt(ell/delta_w)+tau/(r sigma_w))^2
 =0.41412396097991355 <1/2=q/2`,                                 (5.3)

`3/(1+r^2)=12/5>2`.                                               (5.4)

Because (4.8) supplies three eigenvalues of `D` of modulus at least `L0`, the theorem constructs a literal partition of the **original leaf coordinates** and applies the ridge Fourier estimate to the corresponding actual cross block. The hub bank `H`, every other self block and coupling, all signs, all smaller eigenvalues, and every induced affine term remain unrestricted by that theorem. Therefore it controls the original full ambient quadratic form, not a rotated or tail-truncated surrogate.

The resulting bound is

`||p_Q||_infinity
 <= 6 sqrt(2e)/(sigma_w L0)
 =77.27513199092344... <77.276.`                                  (5.5)

Moreover this paid branch has a continuous density vanishing at infinity.

This is an actual equation-level use of a completed peer theorem. It pays the low-hub/low-carrier part of the partner's normalized-threshold branch whenever the transferred base window is diffuse.

## 6. What failure of the diffuse payment now means physically

If (5.1) fails, there is an original leaf coordinate `i` with `(P_D)_{ii}>1/32`. The spectral theorem immediately gives

`||D e_i||_2^2
 >=(L0/39)^2 (P_D)_{ii}
 >(L0/(39 sqrt(32)))^2`,

hence

`boxed:
 ||D e_i||_2 > rho L0,
 rho=1/(156 sqrt(2)),
 rho L0=0.00424943979078454... .}`                               (6.1)

The completed signed-Schur heavy-row split of fleet03/B12 can then be invoked without changing coordinates. Either

`|D_ii| >= (rho L0)/2`,                                           (6.2)

or

`||D[L\{i},i]||_2 > (sqrt(3)/2) rho L0
 =0.00368012281067184... .`                                      (6.3)

Thus the rough non-Fresnel residue is no longer merely the spectral object `(I-sigma D)^(-1/2)`. In the low-hub/low-carrier chamber it is either already continuously paid by (5.5), or it exposes a fixed-scale **literal physical base row**.

In the currently recorded finite-core compiler, `|H|<=124`. Consequently the two hypotheses deliberately excluded above are also physical packets:

- `||B||_op>1/2` implies some hub row of `B` has Euclidean norm `>1/(2 sqrt(124))=0.0449013...`;
- `||C||_op>1/8` implies some literal hub-to-base star has Euclidean norm `>1/(8 sqrt(124))=0.0112253...`.

Therefore, after the partner threshold-transfer reduction, all failure of the new continuous diffuse payment is localized into a fixed-scale physical hub row, hub-to-base star, or base heavy row. No reciprocal tiny spectral gap remains in this residual statement.

## 7. Updated compact conditional proof assembly

A correction-safe proof graph can now be stated as follows.

1. **Principal-minimal descent.** The completed fleet03/B19 reduction descends, with no density-constant loss, whenever a proper original-coordinate principal block already carries three threshold-large modes. Work can therefore be restricted to the principal-minimal endpoint.
2. **Previously certified exits.** Physical scalar/pair/triple, D/D5/physical-`E_3`, Fresnel, ridge/window, grouped-square, hyperbola, and common-plane payments remain usable only under their exact recorded hypotheses.
3. **Base-subcritical threshold transfer.** The designated partner fleet02/B19 proves the normalized carrier. The present theorem upgrades it to the exact multiplicity transfer (3.2)-(4.4).
4. **Low-hub/low-carrier chamber.** If `||B||<=1/2` and `||C||<=1/8`, the untouched physical base has at least three modes at scale `15/16`, equation (4.8).
5. **Diffuse transferred base — PAID.** If its `L0/39` spectral window has leverage at most `1/32`, the completed ridge-window theorem gives the full-law continuous bound `<77.276`, equation (5.5).
6. **FIRST REMAINING LOCAL GATE.** If the base window is not diffuse, equation (6.1) gives a literal fixed-scale heavy row. Together with the two large-hub alternatives, the next obligation is

   `QFORM-THRESHOLD-TRANSFER-PHYSICAL-HEAVYROW-STAR-CLOSURE-v1`:

   spend one of the fixed original-coordinate packets in Section 6 jointly with the remaining signed threshold information, without reciprocal payment of a single tiny coefficient/minor and without replacing correlated conditional laws by independent ones.

The fresh localized pair-star compiler of fleet03/B19 r45 is compatible with this next gate: strong shared physical edges are already paid, while weak pairs funnel to disjoint `E_2`, two-star, or giant near-rank-one crossing packets. This does not yet show that every heavy row produced by (6.1) enters one of those paid/localized configurations; that splice remains to be proved.

## 8. Corrections and edge cases

- All signs are treated by `sigma=+/-1`; no same-sign spectral pair is assumed.
- Degenerate/repeated eigenvalues and eigenvalues exactly at `+1` or `-1` are handled by the one-sided `t=1-epsilon` inertia limit.
- If `C=0` and some `k_sigma>0` while (3.1) holds, (3.2) is impossible; thus the theorem correctly rules out that geometry rather than dividing by zero.
- The positive and negative near-threshold packets are counted separately only after `Delta<1`; in the quantitative corollary `Delta<=1/16`, so they cannot overlap.
- The low spectral tail of `D` is never deleted. The ridge theorem acts on the actual cross block after the physical partition and explicitly retains arbitrary smaller spectrum and outside couplings.
- No bounded support or moment is assumed for any `X_i`.
- Essential boundedness and continuity are kept separate. Equation (5.5) is a `C_0` branch. The unrestricted theorem and unrestricted continuity remain open.

## 9. Numerical diagnostic

The accompanying deterministic checker sampled 5,000 random finite block matrices. Among 636 signed instances with positive threshold-count surplus and admissible hub gap, there were zero violations of (3.2) and zero violations of the near-threshold multiplicity conclusion. The minimum observed numerical margin in (3.2) was positive. This is only a regression check; Sections 3-5 are the proof.

## 10. Status

This run does **not** claim the full theorem. It removes a genuine part of the partner's first rough normalized-carrier debt:

`normalized threshold carrier`
`=> multiplicity-preserving O(||C||^2) transfer to the untouched physical base`
`=> fixed scale 15/16 when ||B||<=1/2 and ||C||<=1/8`
`=> continuous full-law density <77.276 in the diffuse-base window`
`=> otherwise a fixed-scale original-coordinate heavy row/star packet.`

The next proof should attack the final heavy-row/star closure directly, rather than return to a reciprocal near-threshold denominator.
