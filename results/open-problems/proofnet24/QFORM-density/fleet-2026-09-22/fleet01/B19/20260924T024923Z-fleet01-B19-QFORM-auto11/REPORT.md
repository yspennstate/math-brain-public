SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B19, 2026-09-24T02:49:23Z.
attacking: the fixed-E2 finite-localized survivor — pull the active localized vector back through the orthogonal peel to the original rank-42 carrier so the tiny original residual is retained, then convert that finite localization into a literal physical threshold-normalized row using fleet02/B19.

# fleet01/B19 — pullback of the active carrier and physical threshold-normalized row

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T024923Z-fleet01-B19-QFORM-auto11`  
Status: **ESSENTIAL_STEP_APPLIED / FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: **WITHOUT_VERIFIED_BRAIN**.  
Continuity: asserted only on the cited physical-Fourier exits. The new deterministic reductions do not by themselves prove full-target continuity.

All coordinates that are conditioned or singled out below are literal ORIGINAL product coordinates. Spectral projections occur only in deterministic coefficient inequalities. No post-rotation independence, moment or support bound, iid/log-concavity, arbitrary-joint coarea estimate, law-uniform pointwise phase decay, one-good-minor inference, or probabilistic deletion of a nonzero coefficient tail is used.

## 1. Fresh source graph actually used

1. **Same-constant principal-minimal descent**, fleet03/B19 r43:
   `yspennstate/math-open-problems@ef38106705da5fab5a2fb6dbdd64745206580f62`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B19/20260923T220120Z-fleet03-B19-QFORM-r43/REPORT.md`.
   It reduces the affine interval theorem, without constant loss, to ORIGINAL-coordinate principal-minimal matrices. Hence every proper physical principal block of an irreducible target has at most two eigenvalues of modulus at least one. A principal-minimal full matrix has exactly three target-large eigenvalues, or four with mixed signs.

2. **Full-cut E2 to finite carrier**, fleet01/B02 r43, available at immutable source
   `yspennstate/math-open-problems@f423fb15e023ae33ee864e6d2468da782c8afd99`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B02/20260924T022016Z-fleet01-B02-qform-auto11-r43/REPORT.md`.
   Apart from its paid physical-E3 / coordinate-core branches and the already-tracked giant near-rank-one branch, it produces the exact ORIGINAL-coordinate decomposition
   \[
      A=D_0+R_0+E_0,                                               \tag{1.1}
   \]
   with
   \[
      \|D_0\|_{op}<\frac18,\quad \operatorname{rank}R_0\le42,
   \]
   \[
      s_3(R_0)>\gamma_0:=0.8749992111292801,
      \qquad \|E_0\|_F<\epsilon_0:=7.888707199262311\cdot10^{-7}. \tag{1.2}
   \]
   The tail `E_0` is retained exactly.

3. **Active localized peeling**, fleet02/B20, source containing the completed report
   `yspennstate/math-open-problems@f423fb15e023ae33ee864e6d2468da782c8afd99`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B20/20260924T022856Z-fleet02-B20-QFORM-auto11/REPORT.md`.
   Starting from (1.1), it either pays a physical-E3 branch by `||p_Q||_infinity<479.633` with continuous `C_0` density, or after orthogonal low-action peels finds a localized carrier vector with action at least `1/64`. Its published endpoint moves the peeled increments into a larger retained tail. Section 2 below shows that this enlargement is unnecessary for the localization certificate.

4. **Designated partner fleet02/B19 — threshold-normalized carrier**, source pin
   `yspennstate/math-open-problems@da594097550f0b88ea54c6989b252ae347a2d2f3`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260923T234926Z-fleet02-B19-QFORM-auto11b/REPORT.md`.
   For a physical block decomposition
   \[
      A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
   \]
   a sign `sigma in {+1,-1}` with `p_sigma(A)>p_sigma(D)`, and
   `lambda_max(sigma B)<=1-gamma`, it proves
   \[
      \left\|C P_< (I-\sigma D)^{-1/2}\right\|_{op}^2\ge\gamma,   \tag{1.3}
   \]
   where `P_<` is the spectral projection of `sigma D` onto `(-infinity,1)`. Exact threshold eigenvalues, repeated eigenvalues, both signs and singular blocks are included. This is coefficient geometry only.

5. **Newest designated-partner update**, fleet02/B19 r11,
   `yspennstate/math-open-problems@4ad9d206dba1b22fd917280717c24f4e1dd6ea09`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B19/20260924T021245Z-fleet02-B19-QFORM-r11/REPORT.md`.
   It introduces no correction to (1.3). It sharpens the parallel two-star branch: after its physical-E3/D5 exits, the bilateral transverse rank-one defects satisfy
   \[
      \eta_L\eta_R<3/512,                                         \tag{1.4}
   \]
   and distinct anchors also satisfy the bordered tradeoff described in that report. This is incorporated in the conditional proof graph in Section 5.

## 2. First new theorem: pull an active peeled vector back to the original tiny-tail carrier

The fleet02/B20 peel uses one fixed original carrier isometry. Write
\[
   R_0=V_0K_0V_0^T,\qquad V_0^TV_0=I.
\]
At successive stages there are nested coefficient subspaces
\[
   W_0\supset W_1\supset\cdots\supset W_m
\]
and orthogonal projections `P_j` onto `W_j`, with retained carrier matrices obtained by compression. Equivalently, after identifying every `W_j` inside `W_0`,
\[
   K_j=P_jK_0P_j.                                                   \tag{2.1}
\]
The B20 stopping alternative supplies a unit `u in W_m` and a literal physical set `H` with
\[
   |H|\le16\,\operatorname{rank}(R_m)^2\le28224,                  \tag{2.2}
\]
\[
   \|(V_0u)_H\|_2^2>\frac12,                                      \tag{2.3}
\]
\[
   \|K_mu\|_2\ge\frac1{64}.                                      \tag{2.4}
\]

### Theorem 2.1 — `QFORM-ACTIVELOCALIZED-PEEL-PULLBACK-v1`

In the non-Fourier branch of the B20 peel, the **original** carrier in (1.1) already has the same active localization certificate:
\[
   \boxed{\|(V_0u)_H\|_2^2>1/2,\qquad |H|\le28224,\qquad
          \|K_0u\|_2\ge1/64.}                                    \tag{2.5}
\]
Consequently one may keep the original bounds (1.2); there is no need to replace `E_0` by the much larger accumulated peel tail in order to record the active localized direction.

### Proof

Since `u in W_m`, `P_mu=u`. From (2.1),
\[
   K_mu=P_mK_0P_mu=P_mK_0u.
\]
Orthogonal projection is a contraction, hence
\[
   \|K_0u\|_2\ge\|P_mK_0u\|_2=\|K_mu\|_2\ge1/64.                 \tag{2.6}
\]
The physical carrier vector is exactly the same `V_0u` at every stage because the B20 compression changes only the coefficient operator on the fixed carrier range; therefore (2.2)-(2.3) are unchanged. QED.

This is a deterministic pullback. None of the peeled coefficient increments is deleted from the random quadratic form: we simply return to the exact identity (1.1), for which those increments were still part of `R_0`.

### Scaled-back fixed-E2 consequence

The current B20 fixed-positive-E2 compiler globally rescales by
\[
   \Lambda=16.405318852237478.                                    \tag{2.7}
\]
Applying Theorem 2.1 before scaling back shows that its finite-active-localized original-scale endpoint can be sharpened to the exact decomposition
\[
   A=\widehat D+\widehat R+\widehat E,                             \tag{2.8}
\]
with
\[
   \operatorname{rank}\widehat R\le42,
   \quad \|\widehat D\|_{op}<0.007619480067767874,                \tag{2.9}
\]
\[
   s_3(\widehat R)>0.05333631238809731,
   \quad \|\widehat E\|_F<4.808627781218889\cdot10^{-8},          \tag{2.10}
\]
and an `H,u` satisfying
\[
  |H|\le28224,\qquad \|(Vu)_H\|_2^2>1/2,
  \qquad \|\widehat K u\|_2\ge0.0009524350084709843.            \tag{2.11}
\]
Compared with the published scaled-back B20 certificate, the active branch therefore retains the original tiny residual and the larger original carrier `s_3` floor.

## 3. Apply fleet02/B19 to an actual physical block

Now pass to the principal-minimal problem using fleet03/B19 r43. Let `H` be the nonempty literal physical set from (2.5) and put `L=H^c`, `m=|H|<=28224`. Write the **actual** matrix in original coordinates as
\[
   A=\begin{pmatrix}B&C\\C^T&D\end{pmatrix},
   \quad B=A[H,H],\quad C=A[H,L],\quad D=A[L,L].                  \tag{3.1}
\]
If `L` already carries three target-scale eigenvalues, the same-constant principal-block descent pays this dimension. Hence in the irreducible state
\[
   N_D(1)\le2.                                                     \tag{3.2}
\]
Since `N_A(1)>=3`, there is a sign `sigma` such that
\[
   p_\sigma(A)>p_\sigma(D).                                       \tag{3.3}
\]

If
\[
   \|B\|_{op}>1/2,                                                 \tag{3.4}
\]
we record the fixed-scale finite physical hub and do not claim it paid here. Assume instead `||B||op<=1/2`. Then
\[
   \lambda_{max}(\sigma B)\le1/2=1-\gamma,
   \qquad \gamma=1/2.                                             \tag{3.5}
\]
The designated fleet02/B19 theorem (1.3) applies **directly** to (3.1):
\[
  \boxed{\left\|C P_< (I-\sigma D)^{-1/2}\right\|_{op}^2\ge1/2.}\tag{3.6}
\]
Set
\[
   M=C P_< (I-\sigma D)^{-1/2}.
\]
Then `||M||_F^2>=||M||op^2>=1/2`. Since `M` has exactly `m` physical rows, one literal coordinate `i in H` satisfies
\[
  \boxed{\|e_i^T M\|_2^2\ge\frac1{2m}\ge\frac1{56448}.}          \tag{3.7}
\]
In particular
\[
  \|e_i^TM\|_2\ge1/\sqrt{56448}=0.004208968935634212\ldots.      \tag{3.8}
\]
This is already a product-preserving localization of the partner's normalized carrier: the source coordinate `i` is a genuine original independent coordinate. The spectral basis on `L` is used only to measure the deterministic coefficient energy in (3.7).

### Theorem 3.1 — `QFORM-FINITELOCALIZED-THRESHOLD-NORMALIZED-PHYSICAL-ROW-v1`

For every principal-minimal target and every nonempty physical set `H` with `m=|H|<=28224`, one of the following holds:

1. `||A[H,H]||op>1/2`; or
2. there are a sign `sigma` and a literal `i in H` satisfying (3.7).

All threshold degeneracies and both signatures are included.

The theorem is independent of the magnitudes of the subthreshold spectral gaps. In particular it does not reciprocate one small ordinary coefficient.

## 4. Split the normalized physical row into an ordinary star or a near-threshold packet

Let `c_i=e_i^TC` and spectrally resolve `sigma D`. In the row from (3.7),
\[
   \sum_{\mu<1}\frac{|\langle c_i,v_\mu\rangle|^2}{1-\mu}
       \ge\frac1{2m}.                                             \tag{4.1}
\]
Fix the universal gap `delta=1/16`. Separate the strictly subthreshold modes into
\[
   \mathcal N=\{\mu:15/16<\mu<1\},
   \qquad \mathcal F=\{\mu:\mu\le15/16\}.                       \tag{4.2}
\]
On the far set,
\[
   \sum_{\mu\in\mathcal F}\frac{|\langle c_i,v_\mu\rangle|^2}{1-\mu}
      \le16\|c_i\|_2^2.                                          \tag{4.3}
\]
Therefore either
\[
   \|c_i\|_2^2\ge\frac1{64m},                                    \tag{4.4}
\]
which is the literal physical star
\[
   \boxed{\|A[i,L]\|_2\ge\frac1{8\sqrt m}
          \ge\frac1{8\sqrt{28224}}
          =0.000744047619047619\ldots,}                           \tag{4.5}
\]
or else (4.3) is `<1/(4m)` and the near-threshold modes carry
\[
   \boxed{
   \sum_{15/16<\mu<1}
       \frac{|\langle c_i,v_\mu\rangle|^2}{1-\mu}
       >\frac1{4m}\ge\frac1{112896}
       =8.857709750566894\cdot10^{-6}.
   }                                                               \tag{4.6}
\]

Equation (4.6) is the exact normalized currency left by a vanishing ordinary star: as its physical coefficients shrink, they must aim at signed base modes proportionally closer to the threshold. Repeated eigenvalues cause no issue. Modes exactly at `mu=1` are excluded exactly as in the partner theorem and are already counted on the threshold side of `p_sigma(D)`.

### Corollary 4.2 — sharpened active-localized endpoint

Combining Theorem 2.1 with Theorem 3.1, every finite-active-localized survivor of the current fixed-E2 compiler, after principal-minimal descent, lies in the exhaustive physical alternative
\[
\boxed{
\begin{array}{ll}
\text{(HUB)} & \|A[H,H]\|_{op}>1/2,\quad |H|\le28224;\\[2mm]
\text{(STAR)} & \exists i\in H:\ \|A[i,H^c]\|_2\ge0.000744047619\ldots;\\[2mm]
\text{(NTR)} & \exists i,\sigma:\
\sum_{15/16<\mu<1}\frac{|\langle A[i,H^c],v_\mu\rangle|^2}{1-\mu}
\ge1/112896.
\end{array}}
\tag{4.7}
\]
The exact tiny retained tail (2.10) remains in `A`; it is not set to zero.

## 5. Compact conditional proof assembly after this step

The current source-pinned assembly can be stated compactly.

1. By fleet03/B19 r43, it is enough, with no density-constant loss, to prove the affine interval theorem for principal-minimal matrices. Arbitrary extra target-scale spectrum is removed by conditioning ORIGINAL coordinates, not by perturbation.
2. The existing physical-E3/D5, ridge/window, scalar/pair, coordinate-core and Fresnel receivers pay their certified nondegenerate branches with all same-bank curvature and outside couplings retained.
3. The current full-cut E2 compiler (fleet01/B02 r43 plus fleet02/B20) sends its finite-carrier branch either to a continuous physical-E3 payment, the separately tracked giant-near-rank-one collar, or the active localization (2.5). Theorem 2.1 shows that this active state already lives in the original tiny-tail carrier rather than only in the enlarged peeled-tail representation.
4. The active-localized state is now reduced by (4.7) to a finite physical hub, a fixed ordinary star, or one literal-coordinate normalized near-threshold row packet. This is a strictly sharper interface than “finite localized carrier”.
5. The newest fleet02/B19 r11 independently sharpens the parallel two-star/common-hub path: after its physical-E3/D5 exits, the two opposite rank-one defects obey `eta_L eta_R<3/512`; for distinct anchors the bordered-E3 tradeoff further leaves only its stated weak-edge/E2 or small double-transverse alternatives. Thus no robust two-sided transverse two-star packet remains unclassified.

Accordingly the first local receiver needed on the active-carrier spine is now

`QFORM-PHYSICAL-NORMALIZED-ROW-OR-FINITEHUB-PAYMENT-v1`:

> Under the original cap-one product law and principal-minimal spectral hypothesis, pay one of (HUB), (STAR), or (NTR) in (4.7), jointly with the surviving two target-scale resources, without paying a reciprocal single coefficient or declaring the spectral coordinates independent.

The parallel latest-partner debt is its same-hub one-sided moving-ridge / distinct-anchor weak-edge-E2 branch, and the giant near-rank-one collar remains separately tracked. A full candidate proof does not yet exist.

## 6. Scope and regularity

The new pullback and normalized-row theorems are deterministic coefficient statements and therefore cover arbitrary signs, repeated eigenvalues, exact threshold degeneracies, singular finite blocks and arbitrary independent input densities bounded by one. They introduce no regularity claim for the output law by themselves. The cited physical-E3 Fourier branches have continuous `C_0` densities; the unrestricted continuous-density conclusion remains OPEN.

**Full QFORM status: OPEN / NOT PROVED / NOT DISPROVED.**
