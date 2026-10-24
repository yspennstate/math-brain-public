# MOC4 account02/B09 — quantitative external-spinor separation and exact closure of the previous complex transport datum

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Run:** `20260922T054507Z-account02-B09-MOC4-r16`  
**Role:** geometric/polarization support mechanism for complex-normal `4 x 4` MOC4  
**Outcome:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact current state consumed

The latest complete campaign-lead version available in the canonical archive is account03/B07 run `20260922T043708Z-account03-B07-MOC4-r11`, report blob `c286ea3e5ec5a72902fbff82e94db343f2bbc543`, theorem `MOC4-TRANSPOSE-SUBGROUP-CUBATURE-v1`. It gives exact true-unitary subgroup roofs and leaves a positive-reserve maximizer-local problem after the subgroup, pair, `P-R-D`, stationarity and Hessian constraints.

A later OTHER-account result used directly is account03/B09 run `20260922T051640Z-account03-B09-moc4-external-facets`, report blob `51b400736746d39fceb646d41b0566212cb492d8`, theorem `MOC4-SAXL-EXTERNAL-FACET-CLOSURE-v1`. Using Drury's normalized positive-Saxl dual description, it identifies the finite outer base as 24 Weyl evaluation vertices plus 48 non-Weyl external vertices. In the complementary-minor coordinates, each external vertex is

\[
P^{\rm ext}_{\tau}=\frac13(J_4-P_\tau),\qquad
D^{\rm ext}_{\tau}=\frac14E^TP^{\rm ext}_{\tau}E,
\]
\[
R^{\rm ext}_{\tau,\rho'}
=\frac13R_{\rho_\tau}+\frac23R_{\rho'},
\]
where `rho'` is one of the two derangements of the pair-class permutation `rho_tau`. Its external functional is

\[
e_{\tau,\rho'}(f)
=\frac23\{B_{\rho_\tau}(f)+B_{\rho'}(f)\}-\frac13 f(\tau).
\tag{1}
\]
That worker also used the exact gaugewise spinor identity `det N=0` to show that every one of the 48 external vertices is individually non-genuine: in 12 even-even gauges exactly one of the six determinant monomials is nonzero.

A second compatible OTHER-account result, account04/B09 `MOC4-CONTINUOUS-BIORIENTATION-STATIONARITY-v1`, supplies the full twelve-equation first-order `Spin(6)` stationarity system and confirms that the residual must be handled on the genuine common-unitary orbit, not by independent minor masses. The fresh account03/B20 `MOC4-STANDARD-DEFECT-LP-DUAL-v1` further sharpens this worker's preceding standard-transport route. I use these results as constraints on the remaining branch rather than duplicating them.

The new work below makes the account03/B09 external-vertex exclusion **quantitative**, using the actual complex determinant phases, and then applies its finite external criterion to close exactly the genuinely-complex datum from this worker's preceding run.

## 2. Gauge notation

For an exterior-square point, write the usual nonnegative channel masses

\[
q^+=\frac12(R+D),\qquad q^-=\frac12(R-D).
\]
For an even-even gauge `(r,c)`, let `q^{r,c}` be the `3 x 3` matrix whose entries select `q^+` or `q^-` according to the gauge parity. At a genuine spinor point there is a complex `3 x 3` anti-linear matrix `N_{r,c}` satisfying

\[
q^{r,c}_{ij}=|(N_{r,c})_{ij}|^2,
\qquad \det N_{r,c}=0.
\tag{2}
\]
Thus the six determinant-monomial magnitudes are

\[
w_\pi=\prod_i |(N_{r,c})_{i,\pi(i)}|
=\sqrt{\prod_iq^{r,c}_{i,\pi(i)}}.
\tag{3}
\]
Equation (2), with complex phases retained, implies the necessary polygon inequality that no one `w_pi` can exceed the sum of the other five.

## 3. New theorem — `MOC4-EXTERNAL-SPINOR-SEPARATION-v1`

Fix any one of the 48 external vertices `e`. In each of the 12 singleton gauges identified by account03/B09, the external gauge matrix `q_0` has entries only in `{0,1/3}`. Exactly one perfect matching `pi_0` has positive product,

\[
\prod_i(q_0)_{i,\pi_0(i)}=\frac1{27},
\tag{4}
\]
and, among the other five perfect matchings, the numbers of zero entries are exactly

\[
1,2,2,2,3.
\tag{5}
\]
The companion exact verifier checks (4)-(5) for all `48 x 12=576` singleton gauges.

### Theorem

For every genuine `Lambda^2 SU(4)` point and every singleton gauge of `e`,

\[
\boxed{\|q^{r,c}-q_0^{r,c}\|_\infty>\frac1{25}.}
\tag{6}
\]

### Proof

Put `delta=||q-q_0||_infty` and suppose `delta<=1/25`. The distinguished determinant monomial obeys

\[
w_{\pi_0}\ge(1/3-\delta)^{3/2}.
\tag{7}
\]
For an alternative perfect matching containing `z` zero entries of `q_0`, every formerly zero factor is at most `delta`, while every formerly `1/3` factor is at most `1/3+delta`. Using the exact zero-count multiset (5), the sum of the other five determinant-monomial magnitudes is at most

\[
\sqrt\delta(1/3+\delta)
+3\delta\sqrt{1/3+\delta}
+\delta^{3/2}.
\tag{8}
\]
The left side of (7) decreases with `delta`, while (8) increases. At `delta=1/25`, after multiplying by `375`, strict dominance is exactly

\[
110\sqrt{22/75}>31+45\sqrt{28/75}.
\tag{9}
\]
Both sides are positive. Squaring once reduces (9) to

\[
\frac{5497}{3}>2790\sqrt{28/75},
\]
and squaring again leaves the exact positive rational margin

\[
\frac{4062433}{9}>0.
\tag{10}
\]
Hence `w_{pi_0}` is strictly larger than the sum of the other five magnitudes. That contradicts `det N=0`, because the six complex determinant terms cannot cancel. Therefore (6) holds. No phase is discarded: the only inequality is the necessary complex polygon inequality for the exact determinant cancellation. QED.

This theorem is singular-safe and spectrum-independent. It concerns only the exact spinor realization of the common unitary, so repeated spectra or a singular matrix sum do not create an exception.

## 4. Quantitative outer-polytope consequence

The same exact verifier checks that, in every even-even gauge, every one of the 72 normalized-Saxl outer vertices has all `q` coordinates in `[0,1]`.

Let a genuine normalized-Saxl functional have any outer-polytope decomposition

\[
\ell_U=\sum_{v\in V_{72}}\lambda_vv,
\qquad \lambda_v\ge0,\quad\sum_v\lambda_v=1.
\tag{11}
\]
Fix an external vertex `e` and one of its singleton gauges. Gaugewise `q` is linear on this finite coordinate model, so

\[
\|q(\ell_U)-q(e)\|_\infty
\le\sum_{v\ne e}\lambda_v\|q(v)-q(e)\|_\infty
\le1-\lambda_e.
\]
Combining with (6) gives the strict barycentric cap

\[
\boxed{\lambda_e<\frac{24}{25}}
\tag{12}
\]
for **every** external vertex `e` in **every** outer decomposition of a genuine point.

Consequently, if one external vertex `e` is the unique maximizer of a support datum over all 72 outer vertices, with value `E`, and `L_2` is the second-largest outer value, then every true unitary obeys the strictly improved external roof

\[
\boxed{
h(U)<\frac{24}{25}E+\frac1{25}L_2
=E-\frac{E-L_2}{25}.}
\tag{13}
\]
This is a genuine phase-sensitive improvement over the raw Drury/Saxl outer roof `h<=E`. It does **not** by itself prove the target when an active external face remains above the Weyl maximum `M`, because the required repair mass could in principle sit on other high outer vertices. That unpaid coupling is isolated below.

## 5. Decisive exact application: the preceding complex transport datum is now fully closed

This worker's preceding run used the genuinely-complex datum

\[
a=(-6i,5i,3+5i,1),
\quad b=(7+4i,1+7i,1-5i,-3),
\quad\eta=-1+2i.
\tag{14}
\]
It had endpoint maximum `M=7470`; the prior standard-Hamming/Cartan mechanism only proved a positive-gap cutoff `<180`. During this invocation, account03/B20 independently sharpened that route to `<174` via `MOC4-STANDARD-DEFECT-LP-DUAL-v1`.

Applying instead account03/B09's complete 48-external criterion to exactly (14), the new exact application checker obtains

\[
\boxed{\max_{\sigma\in S_4}H_\sigma=7470,}
\]
\[
\boxed{\max_{e\in\mathcal E_{48}}e(H)=\frac{8414}{3},}
\]
so the external margin is

\[
\boxed{7470-\frac{8414}{3}=\frac{13996}{3}>0.}
\tag{15}
\]
Therefore the Drury/Saxl 72-vertex outer theorem immediately gives

\[
\boxed{h_\eta(U)\le7470\quad\text{for every true }U\in U(4).}
\tag{16}
\]
Thus the entire support direction (14) is now **closed exactly**, superseding both `<180` and `<174` as bounds for this particular datum. This does not weaken the transport/LP theorems; it shows that the newer external-facet mechanism is strictly stronger on this example.

## 6. Compact conditional end-to-end argument and first unpaid implication

Assume MOC4 fails for some spectra and support direction. Compactness gives a genuine global maximizing unitary with positive support gap over the 24 Weyl endpoints.

1. If every one of the 48 external values is at most the Weyl maximum `M`, account03/B09's finite outer criterion closes that support direction immediately.
2. Hence a counterexample direction must have a nonempty **active external set** `F={e:e(H)>M}`.
3. The campaign lead's subgroup-cubature roofs, the bidirectional pair roofs, account03/B20's exact defect-LP filter when its unique-standard hypothesis applies, and the exact `Spin(6)` stationarity equations all remain necessary for the same true maximizer.
4. The present theorem adds a phase-sensitive quantitative obstruction: for every active external vertex `e`, every outer decomposition of the genuine point has `lambda_e<24/25`; in each of its 12 singleton gauges the common-unitary channel must move by more than `1/25` in `q_infinity` from the external corner.
5. Therefore the remaining issue is no longer individual exclusion of the 48 corners. It is simultaneous payment across an **active external face**.

The first essential missing implication is:

> **`MOC4-EXTERNAL-FACE-MULTI-PAYMENT-v1` (OPEN).**  
> For every structured spectral support datum with at least one external value above `M`, combine the simultaneous gaugewise equations `det N_{r,c}=0`, the quantitative separation (6), the exact `P-R-D` relations, and the current subgroup/stationarity filters to show that the repair mass forced away from the active external vertices necessarily lands on outer vertices with enough support loss to bring the genuine support to at most `M`; or construct an actual complex-normal spectral datum and one true unitary violating that conclusion.

A free symmetric matrix, independent gauge decomposition, arbitrary bistochastic surrogate, or isolated normalized-Saxl point is not a source-valid refutation. The active-face coupling must come from one common unitary.

## 7. Verification and non-claims

`verify_external_spinor_separation.py` uses only the Python standard library and exact `Fraction` arithmetic. It checks all 48 external vertices, all 576 singleton gauges, the universal zero-count pattern `(0,1,2,2,2,3)`, the 72-vertex gauge coordinate range `[0,1]`, and the two exact rational squaring margins proving the `1/25` separation certificate.

`verify_transport_datum_external_closure.py` uses exact Gaussian-integer arithmetic for (14), enumerates all 24 Weyl and 48 external values, and verifies (15)-(16).

Full MOC4 remains open. No arbitrary bistochastic surrogate, benchmark material, held-out answer, credential, scheduler identifier, machine path, unrelated private transcript, email/Drive material, paid model/API/Codex call, remote workflow, permission bypass, or public release was used.
