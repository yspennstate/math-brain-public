SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B09, 2026-09-23T15:50:27Z.
attacking: near-rank-one localized hub-pair interpolation by compiling the anchored third volume into a residual one-anchor two-volume half-Riesz estimate before any reciprocal pair determinant.

# account03/B09 auto11 — one-anchor two-volume half-Riesz and near-rank-one hub-pair interpolation

## Status

**NEW SUPPORTING THEOREM / ESSENTIAL STEP APPLIED / FULL QFORM OPEN.**

This run changes mechanism at the r35 frontier. The previous invertible-indefinite physical-pair theorem has a reciprocal `det(E)` / `sigma_min(E)` loss and therefore deteriorates when an invertible pair approaches a nonzero rank-one pair, despite the exact rank-one endpoint already being finite. Here one ORIGINAL scalar coordinate is completed first; the exact Schur residual is then paid by a new one-anchor selected-two-volume half-Riesz theorem. The resulting density estimate contains no reciprocal determinant of the physical `2x2` pair core.

The unrestricted three-large-eigenvalue conjecture remains OPEN. Full-target continuity remains OPEN; the new square-peel branch below proves essential boundedness and a linear interval estimate, not a continuous representative. No Gaussian, moment, compact-support, connected-support, log-concavity, identical-law, diagonal-basis, or post-rotation-independence assumption is used. No small nonzero quadratic coefficient is discarded.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh source state and exact dependencies


The proof actually consumes the following completed sources.

1. **Newest Claude / volume mechanism.** `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, in particular the original-coordinate decoupling identity, the cap-one characteristic-function estimate `int |psi|^p <=4pi/sqrt(p)` for `p>=2`, and the determinant-weighted Brascamp--Lieb construction. The later stability report `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`, supplies the corrected endpoint treatment of determinant weights and confirms the same self-phase-safe framework. These inputs are applied below at equations (2.3)-(2.8), not merely cited.

2. **Fractional-potential interface.** account03/B01, `yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T013054Z-auto11/REPORT.md`. It proves the distributional fractional-Riesz inequality and the dependence-safe scalar square peel used at (2.12) and (3.8).

3. **Previous B09 localized pair.** r35, `yspennstate/math-open-problems@82f6ea83f0e981f756fd18080ffdd11a447b60a8`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260923T144532Z-account03-B09-QFORM-r35/REPORT.md`. It provides the physical pair `i,j`, leaf partition `S,T`, pair-row wedge `Delta>0`, and pair-anchored third volume `V>=27G_*/400` in the localized high-hub survivor.

4. **Designated partner account04/B09.** `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1`, `yspennstate/math-open-problems@c0d3f34e557a374f41b2639994c43af4f950b682`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B09/20260923T101659Z-account04-B09-dense-self-cross-fourier-r1/REPORT.md`. Its literal physical rank-three cross-block estimate is applied to the target-valid regression in Section 5.

The complete analytic argument for the new theorem is supplied here; the dependency pins do not constitute an independent review of this report.

## 2. New theorem: one compulsory physical row in a selected two-volume family

Let `I,J` be disjoint sets of ORIGINAL coordinates and let

    R=F(X_I)+2 X_I^T M X_J+G(X_J),                         (2.1)

where `F,G` are arbitrary real measurable functions finite almost surely. Thus arbitrary within-bank quadratic curvature and all outside-conditioning affine terms are allowed.

Fix a physical row `h in I`, write

    a=M[h,:],                                               (2.2)

and let `Omega` be any nonempty selected family of actual physical `2x2` minors of `M` such that every selected row pair is `{h,k}` for some `k!=h`. Put

    Z=sum_{({h,k},C) in Omega} det M[{h,k},C]^2 >0,
    z_k=sum_{C:({h,k},C) in Omega} det M[{h,k},C]^2,
    alpha_k=z_k/Z.

### Theorem 2.1 — `QFORM-ONEANCHOR-TWOVOLUME-HALFRIESZ-v1`

For every admissible cap-one product input law,

    H_(1/2)(R):=sup_s E|R-s|^(-1/2)

obeys

    boxed:
    H_(1/2)(R)
      <= max{
          C_c Z^(-1/8),
          C_d ||a||_2^(1/6) Z^(-1/6)
         },                                                  (2.3)

where

    C_c=4*2^(5/8)*e^(1/4)=7.920951590859... <7.921,
    C_d=12*2^(-1/6)*e^(1/4)=13.727239173441... <13.728.       (2.4)

Both terms have the correct cross-matrix scaling `M -> sM`, namely `|s|^-1/2`. No row-leverage assumption is imposed globally: the proof splits exactly into a concentrated low-row branch and a diffuse low-row branch.

### 2.1 Concentrated low row

Suppose `alpha_k>=1/2` for some `k`. Keep the two physical rows `{h,k}` and condition on every other original coordinate on that side. Let `M_2` denote the resulting `2 x |J|` cross matrix. Its squared two-volume is

    Z_2(M_2)=det(M_2 M_2^T)
            =sum_(|C|=2) det M_2[:,C]^2
            >=z_k.                                          (2.5)

The same `L2` disintegration / Cauchy--Schwarz / Plancherel calculation used in the grouped-cross proof remains valid at rank two before the final Fourier-inversion step. The left singular frame is a physical two-coordinate selector, so its projection density cap is one; the right two-dimensional product projection has density cap at most `e`. Therefore

    |phi_R(t)|
      <= min{1, pi e^(1/2) z_k^(-1/4)|t|^-1}.                (2.6)

This is intentionally *not* claimed to be `L1` in time. Instead apply the proved fractional-Riesz identity at `gamma=1/2`, for which `c_(1/2)=1/sqrt(2pi)`. Direct integration gives

    H_(1/2)(R)
      <=4 sqrt(2)e^(1/4) z_k^(-1/8)
      <=4*2^(5/8)e^(1/4) Z^(-1/8),                           (2.7)

which is the first term in (2.3).

### 2.2 Diffuse low rows

Assume now

    alpha_k<1/2 for every k.                                 (2.8)

Use the original-coordinate quadratic decoupling from the Claude Fourier package on the `I` bank. If `W=X_J-X'_J`, whose coordinates remain independent with densities bounded by one, put

    H(w)=|psi_h(2t<a,w>)|,
    L(w)=prod_(k!=h)|psi_k(2t<M[k,:],w>)|.

Then

    |phi_R(t)|^2 <= F(t)
      :=int H(w)L(w) prod_j g_j(w_j)dw.                       (2.9)

Cauchy--Schwarz under the probability measure `prod g_j` gives

    F(t)^2 <= F_2(t) F_0(t),                                 (2.10)

where `F_2` contains `H^2 L` and `F_0` contains only `L`.

#### Selected two-volume estimate for `F_2`

Normalize the selected squared minors by `Z`. The row exponents are one for the compulsory anchor and `alpha_k` for the other rows; the low-row exponents sum to one. The column marginals sum to two. The diagonal-plus-PSD determinant expansion, followed by weighted AM--GM exactly as in the current volume theorem, gives the BL determinant factor `Z^-1/2`. The anchor is paid by Plancherel:

    int |psi_h(2ts)|^2 ds <= pi/|t|.                          (2.11)

For each low row, the Claude cap-one `Lp` lemma with `p=1/alpha_k>=2` gives the required norm. Its powers of `alpha_k` cancel the BL row entropy. The column entropy contributes at most `e`. Since the low-row exponents sum to one,

    boxed:
    F_2(t) <=2 pi^2 e Z^-1/2 |t|^-2.                         (2.12)

#### Determinant descent to a selected one-volume for `F_0`

Write `m_k=M[k,:]`. For every positive `z_k`,

    z_k <= ||a wedge m_k||_2^2 <=||a||_2^2 ||m_k||_2^2.      (2.13)

Put `pi_k=z_k/Z` and, conditional on row `k`, distribute this probability over the physical entries of `m_k` proportionally to `m_kj^2`. This is a genuine probability measure on actual physical `1x1` minors, with row marginals exactly `alpha_k`. Its weighted geometric determinant mass is

    Z_eff
      =exp(sum_k pi_k log(||m_k||_2^2/pi_k))
      >=Z/||a||_2^2.                                         (2.14)

Indeed (2.13) gives `||m_k||^2/pi_k>=Z/||a||^2` term by term. Applying the same one-volume BL/Hausdorff--Young estimate, the row entropy again cancels and the column entropy is at most `e^(1/2)`, so

    boxed:
    F_0(t)
      <=2 pi e^(1/2)||a||_2 Z^-1/2 |t|^-1.                   (2.15)

Combining (2.10), (2.12), and (2.15), and then taking the decoupling square root,

    |phi_R(t)|
      <=min{1,
       sqrt(2) pi^(3/4)e^(3/8)
       ||a||_2^(1/4) Z^-1/4 |t|^-3/4}.                       (2.16)

This is below the `L1` threshold, but it is strictly above the half-Riesz threshold. For `gamma=1/2`, `b=3/4`,

    int_R |t|^-1/2 min(1,K|t|^-3/4)dt
      =12 K^(2/3).                                            (2.17)

Multiplying by `c_(1/2)=1/sqrt(2pi)` yields

    H_(1/2)(R)
      <=12*2^(-1/6)e^(1/4)||a||_2^(1/6)Z^-1/6,               (2.18)

which is the second term of (2.3). This proves Theorem 2.1.

### Why this is useful

The ordinary `k=2` volume theorem needs every two-volume row marginal strictly below one to get `H_(1/2)`. Theorem 2.1 permits one physical row to be compulsory with marginal exactly one. The key is to spend that row by an `L2` Plancherel factor *before* the decoupling square root, then descend one exterior degree for the companion factor. This is the two-volume analogue of account02/B09's completed one-anchor three-volume hybrid, but the derivation above is supplied independently at the half-Riesz endpoint needed by the scalar square peel.

## 3. Main splice: the localized pair no longer pays reciprocal det(E) near rank one

Use the r35 localized hub-pair setup. Let `i,j` be the physical pair and `S,T` its leaf partition. Put

    m_i=A[i,T],
    m_j=A[j,T],
    m_k=A[k,T]  (k in S),

    Delta=||m_i wedge m_j||_2^2>0,                             (3.1)

and

    V=sum_(k in S)||m_i wedge m_j wedge m_k||_2^2.             (3.2)

The fixed-pair compiler in r35 gives

    V=V_ij(S) >=27G_*/400.                                    (3.3)

Assume only that one physical scalar pivot of the pair is nonzero:

    alpha=A_ii !=0.                                           (3.4)

Complete the square exactly in the ORIGINAL coordinate `X_i`. If `R` denotes the exact Schur residual, its rows against the physical `T` bank are

    c_j=m_j-(A_ij/alpha)m_i,
    c_k=m_k-(A_ik/alpha)m_i.                                  (3.5)

No random coordinate is rotated. The wedge currency survives exactly:

    m_i wedge c_j =m_i wedge m_j,
    m_i wedge c_j wedge c_k
      =m_i wedge m_j wedge m_k.                               (3.6)

In particular `c_j!=0`. Define the residual one-anchor two-volume

    Z_R=sum_(k in S)||c_j wedge c_k||_2^2.                     (3.7)

For each `k`, the triple in (3.6) equals `Delta` times the squared component of `c_k` perpendicular to `span(m_i,c_j)`, whereas `||c_j wedge c_k||^2` is `||c_j||^2` times the squared component perpendicular to `c_j`. Hence

    boxed:
    Z_R >= (||c_j||_2^2/Delta) V.                             (3.8)

The dependence-safe square-peel theorem gives

    ||p_Q||_infinity
      <= |alpha|^-1/2 H_(1/2)(R).                             (3.9)

Apply Theorem 2.1 to the Schur residual, with compulsory physical row `j` and selected two-volume equal to the actual minors in (3.7). Inserting (3.8) yields the new localized-pair estimate

    boxed:
    ||p_Q||_infinity
      <= |alpha|^-1/2 max{
          7.921 Delta^(1/8)||c_j||_2^(-1/4)V^(-1/8),
          13.728 Delta^(1/6)||c_j||_2^(-1/6)V^(-1/6)
         }.                                                   (3.10)

Every interval `L` obeys the same coefficient times `|L|`. Essential boundedness follows. This route does **not** establish continuity.

Using (3.3), one may replace `V` by `27G_*/400` to obtain an explicit r35-resource bound.

### The point of (3.10)

There is no `|det E|^-theta` and no `sigma_min(E)^-theta` in (3.10), where `E=A[{i,j},{i,j}]` is the physical pair core. Thus the analytic certificate does not blow up merely because an invertible pair tends to a nonzero rank-one pair. The remaining quantities are the genuinely source-coordinate scalar pivot and residual cross resources.

In particular, if a family of localized pair cores tends to a nonzero rank-one matrix while one diagonal entry remains bounded away from zero and the fixed-pair cross currencies `Delta,V,||c_j||` remain quantitative, (3.10) is uniform across the determinant-zero limit. This is exactly the interpolation gap left by r35's reciprocal indefinite-pair estimate.

The theorem does **not** claim that the bare three-large-eigenvalue hypothesis automatically lower-bounds `|alpha|`, `||c_j||`, `Delta`, or `V`. Those structural scale-forcing obligations remain part of full QFORM.

## 4. What remains after this splice

The first B09 gap is now narrower:

`QFORM-LOCALIZED-HUBPAIR-NEARZERO-OR-RESIDUAL-ANCHOR-ROUTING-v1`:

> In the localized high-hub branch, route the case in which every useful physical pair scalar pivot is small or the post-pivot residual anchor `c_j` degenerates. The route must spend the existing `Delta` and anchored third volume `V>=27G_*/400` before reciprocal scalar/pair payment. A genuinely near-zero physical core should be joined to the zero-core coefficient-plane / grouped-cross / ridge exits; a small nonzero matrix coefficient cannot be discarded under arbitrary unbounded supports.

This is distinct from the r35 near-rank-one determinant singularity, which (3.10) removes whenever a source-coordinate scalar pivot remains quantitative.

A useful structural warning is that a symmetric pair with small determinant need not have a useful diagonal if it is near a zero-diagonal hyperbolic core `[[0,b],[b,0]]`. Therefore the next step must not falsely infer a large scalar pivot from `det E` alone.

## 5. Target-valid regression and designated partner application

For `epsilon>=0`, consider six original coordinates `(i,j,k,t1,t2,t3)` and the symmetric coefficient matrix with pair block

    E_epsilon=[[1,1],[1,1+epsilon]],                           (5.1)

and cross edges

    A[i,t1]=A[j,t2]=A[k,t3]=1,                                (5.2)

with all other coefficients zero.

The matrix splits as the direct sum of the `(k,t3)` hyperbolic edge, with eigenvalues `+1,-1`, and a four-dimensional block `[[E_epsilon,I_2],[I_2,0]]`. If `mu>=0` is an eigenvalue of `E_epsilon`, the corresponding two eigenvalues solve

    lambda^2-mu lambda-1=0.                                   (5.3)

For `epsilon>0`, both `mu` are positive, so both positive roots exceed one; together with the exact `+1,-1` edge this gives at least four eigenvalues of absolute value at least one. At `epsilon=0`, the spectrum is exactly

    {-1,-1,1-sqrt(2),1,1,1+sqrt(2)},                          (5.4)

so the target hypothesis also holds. Thus this is a genuine target-valid family for all `epsilon>=0`.

For the scalar pivot `alpha=1`,

    Delta=V=1,
    c_j=(-1,1,0),
    ||c_j||=sqrt(2),
    Z_R=2.                                                     (5.5)

There is only one low row in the selected residual family, so the sharper concentrated calculation (before the generic `z_k>=Z/2` loss) gives

    boxed:
    ||p_Q||_infinity
      <=4sqrt(2)e^(1/4) 2^(-1/8)
      =6.660699798151631....                                  (5.6)

This is uniform as `det E_epsilon=epsilon ->0`. The earlier reciprocal indefinite-pair certificate diverges along that limit, so (5.6) confirms that that divergence is a proof-coordinate loss on this family, not intrinsic concentration.

The same regression provides the required actual application of the designated **account04/B09** theorem. The literal physical cross block from rows `{i,j,k}` to columns `{t1,t2,t3}` is

    K=I_3,    |det K|=1.                                      (5.7)

Therefore `QFORM-PHYSICAL-CROSS-DETERMINANT-SMOOTHING-v1` gives the actual inequality

    boxed:
    ||p_Q||_infinity <=3|det K|^-1/3=3,
    P{Q in L}<=3|L|,                                          (5.8)

and in this partner-paid regression the density is continuous. Equation (5.8) is an independent stronger exit for this test family; it is not used to prove Theorem 2.1 or (3.10).

## 6. Finite checks and checkpoint correction

`CHECK.py` and its executed `CHECK_OUTPUT.txt` verify:

- `C_d=13.727239173440687 <13.728`;
- `C_c=7.920951590859107 <7.921`;
- target-valid spectra for `epsilon=0,10^-6,10^-3,10^-2,10^-1`;
- `Delta=V=1`, `||c_j||=sqrt(2)`, `Z_R=2` in the regression;
- the corrected regression constant `6.660699798151631`;
- the partner bound `3`.

The early `SUBSTANTIVE.md` checkpoint accidentally typed `7.263544...` after the explicit factor `2^-1/8` in one final regression line. `CORRECTION.md` records the arithmetic repair. The analytic theorem, universal constants `C_c,C_d`, and wedge inequality were unaffected; the correction strengthens only the worked regression.

## 7. Scope and review status

Theorem 2.1 and the splice (3.10) are supplied as complete supporting arguments in this run. They have **not** received the two independent end-to-end reviews required for a full candidate. The full QFORM theorem remains OPEN, and full-target continuity remains OPEN.

No schedule, task identity, enablement, notification, email, permission, public-release, paid model/API/Codex, or cross-account authentication state was changed.
