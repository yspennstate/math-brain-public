# ProofNet24 P23 — immutable readback correction / delivery receipt

**Canonical report:** `proofnet24/P23-kernel-obstruction/runs/2026-09-16/2026-09-16_10-27-33__run-report.md`  
**Creation commit:** `937ddfc477e552f945b99716c89d08879b26e0e4`  
**Verified report blob:** `b98116f7b5f3239cb4116414d5d920b03b8d8a15`

Exact-commit readback was completed through end-of-file. The report is complete and immutable.

One notation-only TeX transport defect was found in Section 7.3, equation (7.7). The archived line displays the final factor as

```text
=rac{r(r-1)}2e_2.
```

The intended and mathematically used formula is

\[
\boxed{
 e_r\le \frac{r(r-1)}2 e_2.
}
\]

The same formula already appears correctly in the executive statement, and the derivation immediately preceding equation (7.7) identifies it as the product

\[
\prod_{k=3}^r\frac{k}{k-2}=\frac{r(r-1)}2.
\]

This correction changes no theorem, constant, proof dependency, peer-audit verdict, source correction, ledger status, or next obligation. Historical immutable content is not overwritten.

Readback status: **VERIFIED WITH THE SINGLE NOTATION-ONLY CORRECTION ABOVE**.
