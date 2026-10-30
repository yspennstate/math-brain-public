# MOC4 fleet03/B20 — standard-channel P–R locking

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex-normal `4 x 4` Marcus–de Oliveira target  
**Worker/run:** fleet03/B20, `20260922T045352Z-b20-moc4-r11`  
**Assignment:** after compact account-local caretaking, integrate the newest cross-account candidate and directly derive its first unpaid universal step  
**Named assigned partner consumed:** fleet04/B09, `MOC4-STANDARD-CHANNEL-CEILING-v1`  
**Candidate:** `MOC4-STANDARD-PR-LOCKING-v1`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-exact target and live proof state

For spectra `a=(a_i)`, `b=(b_i)` and a unit support direction `eta`, write

\[
h(U)=\Re\!\left(\eta\det(D_a+UD_bU^*)\right),\qquad
H_\sigma=\Re\!\left(\eta\prod_i(a_i+b_{\sigma(i)})\right),
\]

and `M=max_sigma H_sigma`. MOC4 asks for `h(U)<=M` for every true `U in U(4)`, for every complex spectra including repeated and singular cases.

I use three exact inherited results.

1. Campaign lead fleet03/B07 `MOC4-V4-PAIR-GAP-CEILING-v1`: with the six Klein-four fibers, fiber means `B_rho`, `Q=max_rho B_rho`, and `Delta=M-Q`, every genuine support violation `h(U)=M+gamma`, `gamma>0`, satisfies
   \[
   k(U)\ge \gamma+\Delta. \tag{1}
   \]
2. **Assigned OTHER-account partner fleet04/B09**, run `20260922T041453Z-b09-moc4-r34`, `MOC4-STANDARD-CHANNEL-CEILING-v1`: define
   \[
   \kappa_\sigma=H_\sigma-B_{\rho_\sigma},\qquad K=\max_\sigma\kappa_\sigma.
   \]
   For any Birkhoff decomposition `P=|U|^2=sum_sigma lambda_sigma P_sigma`, the same-unitary standard channel obeys
   \[
   k(U)=\sum_\sigma\lambda_\sigma\kappa_\sigma\le K. \tag{2}
   \]
   Thus every violation already has `gamma<=r:=K-Delta`.
3. fleet03/B09 exact common-unitary compatibility: for the complementary-pair quotient `R` and oriented channel `D`,
   \[
   D=\frac14E^TPE,\qquad R\ge |D|,\qquad R\mathbf1=R^T\mathbf1=\mathbf1, \tag{3}
   \]
   and the support itself has the exact form
   \[
   h(U)=C_0+\langle C,P\rangle+\langle J,R\rangle, \tag{4}
   \]
   where, after applying the real support functional,
   \[
   C_{ip}=\Re\!\left(\eta\left[c_i b_p+a_i d_p+\frac18(EA^-)_i(EB^-)_p\right]\right),
   \]
   \[
   J_{\alpha\beta}=\frac12\Re\!\left(\eta A^+_\alpha B^+_\beta\right).
   \]

The first unpaid lead implication is the positive-reserve genuine `(P,R)` branch. This run attacks it by converting the partner's standard-channel reserve into quantitative concentration of the same `P`, then using (3) to force concentration of `R`.

## 2. New theorem — `MOC4-STANDARD-PR-LOCKING-v1`

Assume the endpoint standard values `kappa_sigma` have a **unique** maximizer `sigma_*`. Put

\[
\delta=K-\max_{\sigma\ne\sigma_*}\kappa_\sigma>0,
\qquad r=K-\Delta\ge0,
\qquad d_*=M-H_{\sigma_*}\ge0. \tag{5}
\]

Let `rho_*` be the complementary-pair permutation induced by `sigma_*`. Define the two endpoint channel reserves

\[
L_P=\max_{\sigma\in S_4}\langle C,P_\sigma\rangle-\langle C,P_{\sigma_*}\rangle, \tag{6}
\]

\[
L_R=\max_{\rho\in S_3}\langle J,R_\rho\rangle-\langle J,R_{\rho_*}\rangle, \tag{7}
\]

and

\[
L=L_P+2L_R\ge0. \tag{8}
\]

### Theorem

Every true-unitary support violation `h(U)=M+gamma`, `gamma>0`, satisfies the **strictly sharpened** ceiling

\[
\boxed{
\gamma\le\Gamma_*:=\max\left\{0,
 r-\frac\delta2,
 \frac{Lr-\delta d_*}{L+\delta}
\right\}.}
\tag{9}
\]

If `r>0`, then automatically `Gamma_*<r`; if `r=0`, the assigned partner theorem already excludes every violation. Hence on every support direction with a unique standard-channel endpoint maximizer, (9) is a strict exact improvement over the previous universal same-unitary ceiling `gamma<=K-Delta`.

### Proof

Take any Birkhoff decomposition

\[
P=\sum_\sigma\lambda_\sigma P_\sigma
\]

and let `lambda=lambda_{sigma_*}`. By (1)-(2),

\[
\gamma+\Delta\le k(U)=\sum_\sigma\lambda_\sigma\kappa_\sigma.
\]

Because every nonstar endpoint has `kappa_sigma<=K-delta`,

\[
K-k(U)\ge\delta(1-\lambda).
\]

Since `K-k(U)<=K-(gamma+Delta)=r-gamma`,

\[
\boxed{1-\lambda\le\frac{r-\gamma}{\delta}.} \tag{10}
\]

If `gamma<=r-delta/2`, the first nontrivial term in (9) already holds. It remains to treat

\[
\gamma>r-\delta/2. \tag{11}
\]

Then (10) gives `lambda>1/2`.

Write

\[
P=\lambda P_{\sigma_*}+(1-\lambda)P'. \tag{12}
\]

Because `P'` is doubly stochastic, `D'=(1/4)E^TP'E` is a convex combination of the signed standard-representation permutation matrices. At the three selected entries of the signed permutation

\[
D_*=(1/4)E^TP_{\sigma_*}E,
\]

choose signs `epsilon_alpha` so that `(D_*)_{alpha,rho_*(alpha)}=epsilon_alpha`. Every entry of `D'` lies in `[-1,1]`; therefore, from linearity of (3),

\[
\epsilon_\alpha D_{\alpha,\rho_*(\alpha)}
\ge\lambda-(1-\lambda)=2\lambda-1. \tag{13}
\]

The genuine common-unitary inequality `R>=|D|` now yields

\[
R_{\alpha,\rho_*(\alpha)}\ge2\lambda-1. \tag{14}
\]

Since `R` is doubly stochastic, subtracting `(2lambda-1)R_{rho_*}` leaves a nonnegative matrix with every row and column sum equal to `2(1-lambda)`. Hence there is a doubly stochastic `R'` such that

\[
\boxed{R=(2\lambda-1)R_{\rho_*}+2(1-\lambda)R'.} \tag{15}
\]

This is the key same-unitary locking step: large standard-channel mass on one endpoint forces the **same** complementary-pair transport toward its compatible quotient endpoint. It uses neither an arbitrary independent bistochastic pair nor a conjectural common positive lift.

Apply the exact support decomposition (4). From (12),

\[
\langle C,P\rangle-\langle C,P_{\sigma_*}\rangle
\le(1-\lambda)L_P. \tag{16}
\]

From (15),

\[
\langle J,R\rangle-\langle J,R_{\rho_*}\rangle
\le2(1-\lambda)L_R. \tag{17}
\]

At the compatible endpoint, (4) equals `H_{sigma_*}`. Thus

\[
h(U)-H_{\sigma_*}\le(1-\lambda)L. \tag{18}
\]

A violation has left side `gamma+d_*`, so by (10)

\[
\gamma+d_*\le\frac{L}{\delta}(r-\gamma). \tag{19}
\]

Rearranging gives

\[
\boxed{\gamma\le\frac{Lr-\delta d_*}{L+\delta}.} \tag{20}
\]

Combining the branch split (11) with (20) proves (9). Finally, when `r>0`, both `r-delta/2<r` and

\[
\frac{Lr-\delta d_*}{L+\delta}\le\frac{Lr}{L+\delta}<r,
\]

so `Gamma_*<r`. QED.

## 3. Exact nontrivial application

Take simple real spectra and support direction

\[
a=(0,-5,3,2),\qquad b=(-1,2,4,3),\qquad \eta=1. \tag{21}
\]

The zero spectral value is permitted by the source target; all four entries in each spectrum are distinct. Exact enumeration of the 24 endpoints and six `V_4` fibers gives

\[
M=108,\qquad \Delta=202,\qquad K=210,
\]

so the assigned-partner standard ceiling alone leaves

\[
\gamma\le r=8. \tag{22}
\]

The unique standard maximizer is `sigma_*=1432` (one-line notation), with

\[
H_{\sigma_*}=56,\qquad d_*=52.
\]

The second standard value is `413/2`, hence

\[
\delta=\frac72. \tag{23}
\]

The exact channel endpoint ranges are

\[
\langle C,P_{\sigma_*}\rangle=150=\max_\sigma\langle C,P_\sigma\rangle,
\]

\[
\langle J,R_{\rho_*}\rangle=-70,\qquad
\max_\rho\langle J,R_\rho\rangle=-10.
\]

Therefore

\[
L_P=0,\qquad L_R=60,\qquad L=120. \tag{24}
\]

The two branches in (9) are

\[
r-\frac\delta2=\frac{25}{4},
\]

and

\[
\frac{Lr-\delta d_*}{L+\delta}
=\frac{1556}{247}.
\]

Since `1556/247 > 25/4`, the new exact ceiling is

\[
\boxed{\gamma\le\frac{1556}{247}\approx6.2995951417<8.} \tag{25}
\]

For comparison, the lead's independent six-transposition pair ceiling on the same datum is `197/4`; thus (25), not the older pair roof, is the active bound here. This demonstrates a genuine quantitative reduction of the surviving true-unitary reserve, not merely a reformulation.

The companion verifier uses exact integer/Fraction arithmetic to reconstruct (21)-(25) from the spectral formulas and endpoint enumeration.

## 4. Consequences for the shared candidate

The new result directly advances `MOC4-RESIDUAL-PR-RESERVE-v1` on the entire branch where `kappa_sigma` has a unique maximizer:

- `r=0`: already safe by fleet04/B09.
- `r>0`: every positive support gap is **strictly smaller** than `r` by (9), with an explicit computable ceiling from the same spectral data.
- The proof uses the same `P=|U|^2` and its exact `D=(1/4)E^TPE`, then the genuine `R>=|D|` gate. No independent `P,R` relaxation is inserted.

A useful structural warning also falls out of the proof. If the unique `kappa` maximizer is not itself a support-maximizing endpoint, then a support-maximizing permutation supplies another `kappa>=Delta`; consequently `r>=delta`. Thus one should not expect the standard channel alone to force `lambda>1/2` at arbitrarily small gaps. The branch split in (9) is not a proof artifact; additional stationarity/odd-Weyl/spectral structure is genuinely needed near zero gap.

## 5. First remaining implication

The parent target is still open. The sharpened next obligation is:

> **`MOC4-STANDARD-FACE-LOCK-v2` (OPEN).** Extend the same-unitary reserve payment to non-unique `K_std` exposed faces and eliminate the remaining positive `Gamma_*` reserve in the unique-max branch using the existing Cartan stationarity and/or odd-Weyl square-root constraints. A valid alternative is a genuine complex-normal `4 x 4` witness with strict support gap; arbitrary bistochastic or coefficient-hull witnesses do not count.

The assigned partner's standard-channel convexity is therefore not just cited: it supplies the concentration inequality (10), which this run pushes through the exact common-unitary `P -> D -> R` chain to obtain (15) and the new target-gap ceiling (9).

## 6. Status and non-claims

- `MOC4-STANDARD-PR-LOCKING-v1`: **PROVED** under its explicitly stated unique-standard-maximizer hypothesis, for arbitrary complex spectra/support direction and true unitaries.
- Exact example (21): **verified**, improving the surviving ceiling `8 -> 1556/247`.
- Full MOC4: **OPEN / NOT PROVED / NOT DISPROVED**.
- No claim of novelty or publication readiness is made.
- No arbitrary bistochastic surrogate, benchmark gold, credential, scheduler identifier, machine-local path, unrelated private transcript, email/Drive material, public posting, paid model/API/Codex, or remote workflow was used.
