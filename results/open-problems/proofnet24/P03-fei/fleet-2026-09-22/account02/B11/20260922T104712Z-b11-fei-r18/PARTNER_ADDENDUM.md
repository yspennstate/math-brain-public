# Partner integration addendum — nonrobust common-source frontier

**Run:** `20260922T104712Z-b11-fei-r18`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PARTNER_RESULT_APPLIED / FULL_FEI_OPEN`

This immutable addendum records a compatible assigned-partner result that appeared after the primary `REPORT.md` and its first handoff had already been committed. It supersedes only the report's statement that no current-FEI `account03/B11` artifact was yet available. The q/(8r) entropy theorems themselves are unchanged.

## 1. Assigned partner result now consumed

Repository `yspennstate/math-open-problems`, commit

`32e98f96b54e9c0e8bdee8f7ac49cba9aca0fe46`,

path

`proofnet24/P03-fei/fleet-2026-09-22/account03/B11/20260922T105133Z-account03-B11-fei/REPORT.md`.

The exact expression applied here is partner equation (5.5). For any family `N` of centered derivative rows on an `F/J`-critical core with `rho>4`, define

\[
L_N:=\sum_{i\in N}q_i\log_2\frac1{q_i},
\]

and let

\[
Z_N:=\sum_{i\in N}Z_i,
\qquad
Z_i:=\sum_{j\ne i}\zeta_{ij},
\qquad
\zeta_{ij}:=p_{ij}-c_{i\leftarrow j}-c_{j\leftarrow i}\ge0.
\]

Then account03/B11 proves

\[
\boxed{
Z_N>
2L_N-\frac7{22}
[\mathcal P-\operatorname{DTC}(X)].
}
\tag{P.1}
\]

This is source-valid common-source structure: `p_ij=p_ji` follows from Boolean two-face parity, and `zeta_ij` measures support boundary invisible to both physical singleton posterior crossings. No independent arbitrary-row model is substituted.

## 2. Direct application after the q/(8r) physical compiler

Run the primary report's adaptive physical compiler, removing every encountered maximum row for which there is a codimension-`r` subcube proxy with

\[
e\le\frac{2^{-r}}{8r}
\]

and `I_Z<=rq_i`. At any centered critical leaf where this paid mechanism stalls, let `N` be any chosen family of remaining rows, in particular all rows in the residual nonrobust family.

Put

\[
B:=\mathcal P-\operatorname{DTC}(X)\ge0.
\]

Equation (P.1) immediately gives the sharper residual dichotomy

\[
\boxed{
L_N\le\frac7{22}B
\quad\text{or}\quad
Z_N>L_N.
}
\tag{P.2}
\]

Indeed, if the first alternative fails, then (P.1) yields

\[
Z_N>2L_N-\frac7{22}B>L_N.
\]

The first branch is already dimension-free in the existing phase bank:

\[
L_N\le\frac7{22}B
\le\frac7{22}\mathcal P
\le\frac7{11\ln2}\,\mathcal J.
\tag{P.3}
\]

Therefore the logarithmic rare-row load at a stalled leaf is either already phase-paid, or a nonnegative **common-source invisible-boundary bank** `Z_N` dominates that entire logarithmic load.

This is a genuine application of the assigned partner's completed result; it replaces the primary report's formerly generic request for a nonrobust-row dichotomy.

## 3. Revised first unpaid implication

After this partner integration, the first unpaid implication is narrower:

> **COMMON-SOURCE `Z` PAYMENT / RENORMALIZATION.** On a stalled centered `rho>4` critical leaf in the branch `Z_N>L_N`, convert the symmetric two-face common-source mass `Z_N` (or the partner's stronger `xi_ij=zeta_ij+4o_ij` bank) into a realizable physical entropy decrement / terminal contradiction without asserting raw `U_4=O(J)` and without erasing the tensor-orientation baseline.

The partner further proves the exact pairwise decomposition

\[
\frac{\omega_{i\leftarrow j}+\omega_{j\leftarrow i}}2
=\xi_{ij}:=\zeta_{ij}+4o_{ij}\ge0,
\]

and shows that the old hidden bank differs from its symmetric `xi` bank only by an already-visible crossing correction. This structural identity is compatible with the present full-refund compiler, but no payment of the symmetric bank is claimed here.

Full uniform-cube FEI remains **OPEN / NOT PROVED**.
