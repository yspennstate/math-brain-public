# MOC4 fleet04/B07 r12 FINAL — exact UF counterexample; parity-endpoint note corrected by concurrent peer state

**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Campaign:** MOC4, complex normal 4-by-4 Marcus–de Oliveira target  
**Worker:** fleet04/B07  
**Assignment:** representation-theoretic / exterior-algebra attack on the shared mixed-minor constraint  
**Final outcome:** `CANDIDATE_REFUTED` — an exact counterexample refutes the spectral-only upper-Drury-facet shortcut `MOC4-UPPER-DRURY-FACET-FAN-v1/(UF)`. Full MOC4 remains OPEN.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

This file is the final run report. It preserves, but corrects, the earlier same-run `REPORT.md`: after that file was committed, two concurrent exact peer reports became visible on the shared branch. Those reports show that the earlier report's proposed surviving `MOC4-PARITY-ENDPOINT-v2` is not a valid remaining proof route. The one-parameter Birkhoff algebra in that earlier report is correct, but the logical role assigned to its *minimum*-penalty endpoint is superseded. No result below relies on the superseded claim.

## 1. Exact live source state consumed

The target is

\[
\det(A+B)\in\operatorname{conv}\left\{v_\sigma:=\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}
\]

for every complex normal `4 x 4` pair, including repeated spectra and singular cases.

The source-exact chain used in this final report is:

1. **Team lead fleet03/B07, `MOC4-PARITY-SLACK-v1`, run `20260922T012650Z-fleet03-B07-MOC4-r12`, report commit `24b17ab66521620fd857d7b9ec24bc6c1eca3bb5`.** It gives the exact standard-representation support inequality
   \[
   \langle D,K\rangle+\frac12\langle R,X\rangle
   \le \max_{\rho\in S_3}\left(F_\rho(K)+\frac12x_\rho\right),
   \tag{SR}
   \]
   with `F_rho=A_rho-2m_rho` from the four even sign patterns in each `S_4 -> S_3` fiber.
2. **fleet01/B07, `20260922T013731Z-b07-moc4-r11b`, report commit `a0fac94c9342ee4a2c18ed94f7fe770bdf0b12df`.** This exact later peer result refutes the universal existential parity-slack gate on a generic true-unitary structured datum and proves the exact `X`-aware support-gap identity
   \[
   \boxed{
   M-\left(\langle D,K\rangle+\frac12\langle R,X\rangle\right)
   =\mathcal S-2\sum_\rho\lambda_\rho m_\rho+\sum_\rho\lambda_\rho g_\rho,
   }
   \tag{GAP}
   \]
   for every Birkhoff decomposition of `R`.
3. **Named OTHER-account partner fleet01/B08, newest compatible report `20260922T013942Z-b08-moc4-r11`, report commit `1204bdd4463fa137bcfb1d53c3b5ce9702930924`.** It shows the lead's convex-roof simplification is controlled by the **maximum**, not minimum, parity penalty over the one-dimensional Birkhoff fiber, and gives a genuine structured true-unitary counterexample to that corrected unconditional scalar roof. It leaves the stationarity-conditioned roof `MOC4-STATIONARY-ROOF-v1` as one possible narrower route.
4. **fleet01/B07, `MOC4-MIXED-ASSIGNMENT-v1`, report commit `2bc09bcf24348893b74ddf06addf605b6392ad90`.** This is the exact exterior-power/mixed-minor reduction and the identity making `D` a linear image of `P=|U|^2`.
5. **fleet04/B09, `MOC4-PR-JOINT-LIFT-v1 = REFUTED`.** Its exact rational orthogonal witness proves that an unrestricted positive common `(P,R)` permutation lift is false; structured support coefficients must be retained.
6. **S. W. Drury,** *The external vertices conjecture in case n=4*, Electronic Journal of Linear Algebra 11 (2004), 180–191, DOI `10.13001/1081-3810.1131`. This proves a weakened n=4 result, not full MOC4.

## 2. New exact result of this run: `(UF)` is false

The earlier named partner report `MOC4-UPPER-DRURY-FACET-FAN-v1` proposed the universal spectral implication

\[
 u(\operatorname{Re}(\eta v))\le\max_\sigma\operatorname{Re}(\eta v_\sigma),
 \tag{UF}
\]

for the nontrivial Drury facet orbit, with representative

\[
3u(f)=f(3214)+f(4132)+f(3421)+f(2341)-f(3241).
\tag{1}
\]

Take

\[
\begin{aligned}
a&=\frac1{100}(-1+76i,\ 91-158i,\ 1+50i,\ 161+192i),\\
b&=\frac1{100}(-24+48i,\ -69-103i,\ 174+159i,\ 197-193i)
\end{aligned}
\tag{2}
\]

and the support functional

\[
L(z)=-3\operatorname{Re}z-\operatorname{Im}z
=\operatorname{Re}((-3+i)z).
\tag{3}
\]

Exact rational-Gaussian enumeration of all 24 values

\[
v_\sigma=\prod_i(a_i+b_{\sigma(i)})
\]

gives the **unique** support maximizer `sigma=2341` and

\[
M=\max_\sigma L(v_\sigma)=\frac{942601979}{25000000}.
\tag{4}
\]

For the Drury representative (1),

\[
u(v)=
-\frac{3545069333}{300000000}
-i\frac{241749543}{100000000},
\tag{5}
\]

so

\[
L(u(v))=\frac{946704719}{25000000}
\tag{6}
\]

and therefore

\[
\boxed{
L(u(v))-M=\frac{205137}{1250000}>0.
}
\tag{7}
\]

This is a source-valid exact counterexample to `(UF)`. It is **not** a counterexample to MOC4: `(UF)` is a stronger spectral-only sufficient statement, independent of any chosen unitary determinant value. The exact verifier `verify_uf_and_s3.py` and recorded output `VERIFICATION.txt` independently enumerate the 24 products with Python standard-library `Fraction` arithmetic.

### What this rules out

A proof cannot finish MOC4 merely by showing every spectral support deficit belongs to Drury's positive subset-event cone through the universal upper-facet inequality `(UF)`. Some support functions violate that facet inequality before any unitary information enters. Thus the surviving proof must use the actual same-unitary exterior/minor compatibility encoded in `(D,R,K,X)` or an equivalent unitary-dependent mechanism.

## 3. Correction to the earlier same-run parity-endpoint note

The earlier same-run `REPORT.md` independently rederived that every Birkhoff decomposition of a `3 x 3` doubly stochastic `R` is a one-parameter line segment. In the permutation order

\[
123,231,312,132,213,321,
\]

every decomposition is

\[
\lambda=(x,\ R_{12}-R_{33}+x,\ R_{13}-R_{22}+x,\ R_{11}-x,\ R_{33}-x,\ R_{22}-x)
\tag{8}
\]

with

\[
L_R=\max(0,R_{33}-R_{12},R_{22}-R_{13})
\le x\le
U_R=\min(R_{11},R_{22},R_{33}).
\tag{9}
\]

That algebra is correct and is equivalent, by double stochasticity, to the concurrently posted fleet01/B07/fleet01/B08 parameterizations.

However, the earlier report then treated the **minimum** weighted parity penalty as if proving its payment would close the lead's convex-roof route. The newest partner report shows this is not the correct roof quantifier. Since

\[
\sum_\rho\lambda_\rho F_\rho(K)
=\langle R,|K|\rangle-2\sum_\rho\lambda_\rho m_\rho(K),
\tag{10}
\]

minimizing the `F`-cost means **maximizing** the parity penalty. Hence the true scalar roof is

\[
\Psi_K(R)=\langle R,|K|\rangle
-2\max\{M_K(L_R),M_K(U_R)\},
\tag{11}
\]

not the minimum-endpoint expression used by the superseded same-run note.

Moreover, the newest fleet01/B08 exact witness shows even this corrected unconditional roof can fail on generic structured true-unitary data while the actual MOC4 support inequality has large positive slack. Fleet01/B07 independently shows that even the weaker existential parity-slack sufficient gate itself can fail, with the missing payment supplied by the actual structured `X`-dependent support gaps in `(GAP)`.

Therefore:

- the earlier same-run endpoint derivation is retained only as an independent algebraic rederivation of the `S_3` Birkhoff line;
- `MOC4-PARITY-ENDPOINT-v2` is **withdrawn** as a proposed surviving route;
- no novelty/progress credit is claimed for that endpoint parameterization after the concurrent peer artifacts became visible.

## 4. Current compact conditional end-to-end argument

The latest source-valid route is now:

1. Reduce MOC4 exactly to `(SR)` using the exterior-power expansion and the Hadamard standard representation.
2. Do **not** replace `(SR)` by an unrestricted common positive lift: fleet04/B09 refutes that.
3. Do **not** replace `(SR)` by the spectral-only universal Drury upper-facet condition `(UF)`: equation (7) refutes that.
4. Do **not** discard the structured `X` geometry through the unconditional scalar parity roof: fleet01/B07 and the newest fleet01/B08 exact witnesses refute those simplifications.
5. In the generic residual core, a hypothetical target-level support maximizer must also satisfy the inherited row/column pair-stationarity conditions. Thus one currently viable first implication is the newest partner's

   **`MOC4-STATIONARY-ROOF-v1`**: under all twelve exact pair-polarization north-pole conditions for the same true unitary and support direction, prove the corrected maximum-penalty roof, or produce a pair-stationary counterexample and retain the full `X`-dependent six-fiber inequality.

6. Independently, fleet01/B07's exact identity `(GAP)` shows the more faithful target is **`MOC4-SUPPORT-GAP-RESCUE-v1`**: in the positive-deficit regime, the structured `X`-dependent fiber gaps must pay the parity deficit. Any next exterior/representation proof should attack this coupled statement rather than another `X`-free positivity surrogate.

This run does not prove either remaining implication. It contributes the exact exclusion (7), which removes the competing spectral-only Drury-facet mechanism and forces the shared effort back to genuinely unitary-dependent mixed-minor structure.

## 5. Boundary scope and status

The exact counterexample (2) has distinct spectra; no singular/repeated-spectrum claim is needed for the refutation. The parent MOC4 statement remains open and still includes all singular and repeated cases. The campaign's inherited boundary reductions remain separate and are not re-proved here.

No target-level counterexample was produced. No full proof candidate is claimed. No benchmark work, gold material, credentials, private unrelated data, paid/remote compute, public posting, email, Drive, or remote workflow dispatch was used.

## 6. Verification artifacts

- `verify_uf_and_s3.py`, creation commit `9cef5ea97e007820721f6e9ac158e12ecc878447`.
- `VERIFICATION.txt`, creation commit `32e4902f06097b125ea84bd097b0803e61b3dd31`.
- earlier same-run `REPORT.md`, commit `b7ddf7aea27cb0f5175dd19016b37cd96782ccd6`, retained as history and superseded by this final report where they conflict.

**Final classification:** `CANDIDATE_REFUTED` for `MOC4-UPPER-DRURY-FACET-FAN-v1/(UF)`; parent MOC4 remains OPEN.
