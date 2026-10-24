# R28 verification - moving-excess finite budget and Lane O guardrails

Date: 2026-06-28.

## Scope

This round used exactly five read-only audit agents:

1. `019f0c89-83dc-7353-b307-0758c77042e6` audited the rectangular
   moving-excess finite-budget lower side and identified the safe insertion
   point after the proportional-excess density-rate proof.
2. `019f0c89-b4dc-7b31-bf57-e40a583106a6` audited entrywise smoothing-profile
   refinements and recommended leaving the stronger profile averaging problem
   for a later round.
3. `019f0c89-e214-7682-93db-8066c585181b` audited the fixed-`k`
   Laguerre finite-`m` constants and recommended explicit nonnegative
   polynomial-loss constants.
4. `019f0c89-f811-7812-8f3b-268479a99fc3` audited phase-retrieval
   consequences and found no convention-safe theorem to promote this round.
5. `019f0c8a-0e63-77a0-a3fb-1cab8238e0f5` audited Lane O consistency after
   the finite-budget/a.s. upgrades.

No terminal-launched agents, background daemons, or scheduled tasks were
created.

## Main changes

1. Added `rect:moving-excess-finite-budget`.  For arbitrary
   `m <= ell_m <= N_m`, scalar density bound `K_m`, and
   `p_m = ell_m-m+1`, `q_m = d_F p_m`, the finite lower-side budget is
   \[
     B_m = 1 \vee \left[
       \binom{N_m}{\ell_m}mK_m^{p_m}
       \binom{\ell_m}{p_m}^{d_F/2}v_{q_m}m^{q_m/2}
     \right].
   \]
   Therefore
   \[
     P\left\{M_m^{(\ell)} \le
       \exp[-(\log B_m+u_m)/(d_Fp_m)]\right\}\le e^{-u_m}.
   \]
   If `sum_m e^{-u_m}<infty`, the corresponding lower bound holds
   eventually almost surely.
2. The proof keeps the exact unit-ball volume, coordinate-minor, row-set, and
   density factors.  It is a lower-side finite-budget statement only: no
   Wishart-edge law, upper side, or exact exponential base is asserted.
3. Clarified the fixed-`k` Laguerre finite-`m` constants as
   `C_{F,k} >= 1` and `B_{F,k} >= 0`.
4. Tightened Lane O finite-budget Borel-Cantelli guardrails in the master:
   deterministic families, deterministic budgets, and no independence inside
   the tested family.
5. Fixed compact Lane O notation for fixed-excess entrywise budgets,
   two-sided heterogeneous sums, and the generic `4m-4` complex
   phase-retrieval threshold.

## Verification

Standalone build final log scan:

```text
Output written on extremal_hard_edge.pdf (42 pages, 630691 bytes).
```

Master build final log scan:

```text
Output written on master.pdf (854 pages, 7762588 bytes).
```

`master.pdf` was copied to `~/Downloads/master.pdf`; both files
are 7762588 bytes.  The targeted log scans matched only the final output lines:
no undefined citations/references, LaTeX errors, package errors, or rerun
requests were found.
