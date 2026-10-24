# PROB20-20 — immutable readback correction for 2026-09-17T22-30-00Z report

This note corrects two notation/domain details in the immutable report

`runs/2026-09-17/2026-09-17T22-30-00Z__report.md`

created at commit `867becf728bc7add0c989ef359cdae040bc68a66`.

Neither correction changes the proposition, its proof, the frozen metric, the PARTIAL/OPEN status, or the recovery/rotation state.

## 1. Tail-record convention in Proposition 4.1

The phrase “strict record-minimum indices of `q_r`” is to be read **after a finite tail start**.

Because

\[
\sum_r u_r<\infty,
\]

we have `u_r -> 0`. Hence there exists a deterministic `R_0` such that `0<u_r<1` for every `r>=R_0`, and therefore

\[
a_r=-\log u_r>0,
\qquad
q_r=a_r/2^r>0
\]

on that tail.

Choose `j_0>=R_0`, then let

\[
j_0<j_1<j_2<\cdots
\]

be the successive strict record minima **relative to the tail `r>=R_0`**. Since

\[
\liminf_{r\to\infty}q_r=0,
\]

there are infinitely many such tail records and

\[
s_k=q_{j_k}\downarrow0.
\]

Also `j_k->infinity` and `u_{j_k}->0`, so

\[
A_k=2^{j_k}s_k=-\log u_{j_k}\to\infty.
\]

With this tail-record convention, equations (4.10)--(4.17) in the immutable report are unchanged verbatim. A finite prefix of the weight law has no role in the asymptotic statement.

## 2. Typo in equation (4.4)

The displayed equivalence in (4.4) should read

\[
\boxed{u_r^{\,2^{j-r}}\asymp u_j,}
\]

not `nu_r^{2^{j-r}}`. The symbol `nu_r` was a typesetting typo; only the already-defined activity sequence `u_r` is meant.

## Status impact

- unrestricted Janson Problem 18.39: **PARTIAL / OPEN**;
- frozen unrestricted metric: **UNKNOWN/UNMEASURED -> UNKNOWN/UNMEASURED, no movement**;
- supported unchanged count: `3 -> 4`;
- recovery state: **STUCK RECOVERY 2/2 consumed**;
- no closure claim;
- no source/literature/scheduler statement changes.
