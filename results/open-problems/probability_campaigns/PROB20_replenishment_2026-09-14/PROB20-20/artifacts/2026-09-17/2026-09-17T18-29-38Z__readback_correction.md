# PROB20-20 exact-readback correction — 2026-09-17T18-29-38Z report

This is a notation/transport-only correction to the immutable report

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-20/runs/2026-09-17/2026-09-17T18-29-38Z__report.md`

at creation commit

`5e154390c6a4bdfed406d81f9159718b4657b44b`,

blob

`b55dfef6195d15a01499de2df8f00d923ce9e9f4`.

Exact-commit readback found four display-transport/notation defects. None changes a hypothesis, proof step, theorem, status, or frozen metric.

1. Equation (3.2) displays `\nu_r:=...` where the surrounding definition and every subsequent use intend the actual activity symbol `u_r`. The corrected opening is
   `\boxed{u_r:=...}`.
2. In Section 11, the display immediately before (11.2) reads `\nu_{j_k-d}=\exp(-2^{(j_k-d)/4})`; it should read
   `u_{j_k-d}=\exp(-2^{(j_k-d)/4})`.
3. Equation (11.3) reads `\nu_{j_k}=2^{-k}`; it should read
   `u_{j_k}=2^{-k}`.
4. Equation (8.11) lost the LaTeX `\frac` token in transport and displays `rac12`. The intended inequality is

\[
T_{n,j-1}
\le
2\eta_l+\frac12(4\varepsilon_n)^{2^{h_l}}.
\]

The proof of Lemma 8.1 immediately above already defines the coefficient as one half and derives exactly this term, and equations (8.12)--(8.14) use that intended quantity. Thus this is a rendering/escaping defect only.

The corrected mathematical claim remains Theorem 5.1: for the fixed dyadic law `w_(2^r)=u_r/2^r`, if infinitely many roots `j_l` admit barrier depths `h_l<=j_l/3` with

\[
\zeta_l:=\max_{1\le d\le h_l}2^d u_{j_l-d},
\qquad
\zeta_l^2/u_{j_l}\to0,
\qquad
\log(1/u_{j_l})=o(2^{h_l}),
\]

then for every fixed admissible `m_n/n->lambda>nu` there is a deterministic subsequence on which `Y_(1)/n -> lambda-nu` in probability and in expectation, so the restricted-class limsup metric is exactly `b(w,lambda)=lambda-nu`.

The explicit fixed spike law remains

\[
j_k=4^k,
\qquad
u_{j_k}=2^{-k},
\qquad
u_r=\exp(-2^{r/4})\quad(r\notin\{j_k\}),
\]

where both displayed `\nu` symbols in this last formula are to be read as the activity symbol `u`; in plain text: `u_(j_k)=2^-k` and `u_r=exp(-2^(r/4))` off spikes. This law has no summable nonincreasing majorant but still has `b(w,lambda)=lambda-nu` by Theorem 5.1.

Source-level status remains **PARTIAL / OPEN**. The unrestricted arbitrary-weight branch of Janson Problem 18.39 has no movement in this run.