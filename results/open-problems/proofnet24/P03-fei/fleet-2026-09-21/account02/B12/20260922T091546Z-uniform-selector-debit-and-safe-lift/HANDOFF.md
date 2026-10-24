# B12 compact source-bound handoff

Full FEI remains **OPEN / NOT PROVED**.

## New exact universal split bound

Consume account01/B12 `20260922T090347Z-folded-js-shannon/REPORT.md` at commit `92c75e9bcd2fe9c5dc2bedc8a032b31b4afb5484`.
For any genuine Boolean restriction split with selector bias `s`, physical disagreement probability `d`, and `V_s=4s(1-s)`, the exact conditional Fourier entropy increment obeys

\[
\boxed{\Delta_i\widetilde H-dh_2(V_s)
\le h_2(d)+\frac2{\ln2}\min(d,1-d).}
\]

This is selector-bias independent and is exact-zero at both `d=0` and `d=1`. In the exact gate-defect recursion it gives

\[
D_\Gamma(G)\ge(1-s)D_0+sD_1
+(1-s)\Gamma(q_0)+s\Gamma(q_1)-\Gamma(q)
+d\Gamma(s)-h_2(d)-\frac2{\ln2}\min(d,1-d).
\]

The remaining obstruction is genuinely nonlocal: `h_2(d)/d` diverges at sparse equal-marginal disagreements, so descendant/Boolean shape slack must pay this term without reuse.

## Safe replacement seed after the exact prime falsifier

The prior `0.268204856` quadratic lift is refuted. Taking instead

\[
\Gamma^+(u)=\Gamma_0(u)+0.337u(1-u),
\qquad \Gamma^+(1/2)=6.53905,
\]

is globally monotone relative to the refuted lift because every gate defect changes by `(0.337-0.268204856)W_G` with `W_G>=0`.
For the exact 18-input prime witness (`W=1078193/4194304`), the added defect is `0.01768456523294258...`; using the certified old deficit magnitude `<0.017611420` leaves the rigorous reserve

\[
D_{\Gamma^+}>7.314523294258118\times10^{-5}.
\]

Thus all earlier positive lower-lift gate certificates survive and the first known falsifier is repaired. This is **not** a universal certificate: either amortize the binary term above for this or another finite-cap potential, or search immediately for a genuine gate/bias with base-potential requested margin `c_G>0.337`.

Scientific report and checker are in this same directory.
