# PROB20-20 raw-commit readback clarification — 2026-09-17T18-29-38Z report

This clarification supersedes the *diagnosis of transport defects* in the sibling `2026-09-17T18-29-38Z__readback_correction.md`; it does **not** supersede or mutate the immutable research report.

After comparing the connector's serialized `fetch_file` string with the raw creation-commit diff at

`5e154390c6a4bdfed406d81f9159718b4657b44b`,

I found that three apparent `\nu...` defects and the apparent `rac12` defect were artifacts of interpreting JSON/string escape boundaries rather than defects in the stored Git blob. The raw commit diff is authoritative here.

Specifically, the stored report already has these intended expressions correctly:

- equation (3.2) begins with the actual activity `u_r:=...`;
- Section 11 has `u_{j_k-d}=exp(-2^{(j_k-d)/4})`;
- equation (11.3) has `u_{j_k}=2^{-k}`;
- equation (8.11) has the correct term `\frac12(4\varepsilon_n)^{2^{h_l}}`.

There is one genuine notation omission visible in the raw report near equation (4.1): after `\qquad` the stored text has the scalar `u<\infty`, where the intended statement is Janson's boundary mean

\[
\nu<\infty.
\]

This omission is redundant with the immediately following assumption `sum_r u_r<infinity`, with Theorem 5.1's explicit conclusion `0<nu<infinity`, and with the proved identity

\[
\nu=\frac{\sum_r u_r}{1+\sum_r u_r/2^r}.
\]

Thus it changes no hypothesis or proof step: in the general dyadic law (4.1), read the final scalar condition as `nu<infinity`, not `u<infinity`.

The mathematical claim remains exactly Theorem 5.1 and Corollary 11.1 of the immutable report. In particular, the fixed sparse-spike law with `j_k=4^k`, root activities `u_(j_k)=2^-k`, and trough activities `u_r=exp(-2^(r/4))` admits no summable nonincreasing majorant, yet for every fixed admissible `m_n/n->lambda>nu` it has a deterministic subsequence with `Y_(1)/n -> lambda-nu` in probability and expectation; hence its restricted frozen metric is `b(w,lambda)=lambda-nu`.

Source status remains **PARTIAL / OPEN** and the unrestricted arbitrary-weight branch of Janson Problem 18.39 has no movement.