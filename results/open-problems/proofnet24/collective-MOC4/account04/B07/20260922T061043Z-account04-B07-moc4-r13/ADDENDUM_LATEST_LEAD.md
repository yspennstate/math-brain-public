# Addendum — latest lead saturation theorem supersedes the one-flat residual

**Run:** `20260922T061043Z-account04-B07-moc4-r13`  
**Status:** `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN**.

After the immutable main report was written, the team lead published a newer complete result:

- account03/B07, run `20260922T060726Z-account03-B07-MOC4-r11`, report blob `c8911d75149115eb15810e4f8fac624cfc5e34f5`;
- theorem `MOC4-SPIN4-SATURATION-TO-ZERO-FACE-v1`.

That theorem is stronger than the residual named in section 8 of the immutable report. At a genuine global support maximizer, saturation of **any one** complementary-pair mixed-Hessian gate, `T=|C|`, gives a genuine coordinate `SU(2)` orbit on which the support is exactly flat and therefore an equal-support unitary with a zero entry. Hence `MOC4-ONE-FLAT-SPINOR-PROPAGATION-v1` is no longer the first target-level missing implication and should not be pursued as a separate closure problem.

The spinor results of the main report remain valid and useful on the surviving strictly curved branch. In particular, for every row pair
\[
\left(
\left|\sum_\beta (X_{\alpha\beta}-X_{\gamma\beta})m_{\alpha\beta}n_{\alpha\beta}\right|
+
\left|\sum_\beta (X_{\alpha\beta}-X_{\gamma\beta})m_{\gamma\beta}n_{\gamma\beta}\right|
\right)^2
\le T_{\alpha\gamma}^2-C_{\alpha\gamma}^2.
\]
Thus the lead's strict-interior branch has a quantitative spinor interpretation: its positive Hessian reserve bounds the two weighted orientation-mixing moments on the same true exterior-square point. When the affine row matrix `L_alpha` is invertible, the main report further gives
\[
\sum_\beta\min\{|m_{\alpha\beta}|^2,|n_{\alpha\beta}|^2\}
\le \sqrt3\,\|L_\alpha^{-1}\|_2
\sqrt{r_{\alpha\gamma}+r_{\alpha\delta}},
\qquad r_{\alpha\gamma}=T_{\alpha\gamma}^2-C_{\alpha\gamma}^2.
\]
The zero-reserve endpoint is rigorously block-safe by `MOC4-PURE-BLOCK-SPINOR-RIGIDITY-v1`.

Accordingly the first essential implication for this B07 exterior-algebra lane is now:

> **`MOC4-STRICT-SPINOR-RESERVE-PAYMENT-v1` (OPEN).** On a genuine positive-gap global maximizer with no zero entry, all left/right complementary-pair gates are strictly curved by the new lead theorem. Use the exact spinor moment inequalities above, full first-order stationarity, and the same-unitary `P/R/D` identities to turn the available positive reserves into enough support payment to rule out the gap. The affine-degenerate coefficient branch must be handled rather than assumed away.

The lead simultaneously reduces any saturated branch to the separate zero-face obligation `ZF`. This addendum therefore preserves the main report's new identities and rigidity theorem but updates its target-facing residual to the newest complete team state.

The assigned OTHER-account result used in this run remains account01/B08 `20260922T060423Z-account01-B08-MOC4-r11`, `MOC4-PR-JOINT-LIFT-FACET-v1`: its dense exact true-unitary counterexample forbids replacing the strict-reserve problem by a universal positive same-unitary common-compound lift.
