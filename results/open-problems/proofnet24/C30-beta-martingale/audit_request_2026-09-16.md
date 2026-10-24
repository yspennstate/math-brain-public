# C30 audit request — beta-splitting growth martingale package

Requested independent reviewers under `operations/FLEET_2026-09-16.md`:

1. P26 (fleet independent audit), and
2. C29 (directed registry-cycle auditor for C30).

This is a claim-scoped audit request, not a claim that Open Problem 13 is closed.

## Claims to audit

1. **Growth hit kernel.** For each clade edge `C` in `CTCS(n)`,
   `p_T(C)=(|C|/n) exp(-sum_{A strict ancestor C} ell_A/|A|) b_T(C)`,
   with `b_T(C)=1-exp(-ell_C/|C|)` for non-singletons and `b_T(C)=1` for terminal singleton rays, is the exact conditional probability that the next growth insertion hits `C`.
2. **Clade-count increment.** For every `r>=2`,
   `d_r(T,C)=1_{|C|+1=r} + #{A strict ancestor C: |A|=r-1} - #{A strict ancestor C: |A|=r}`
   equals `N_r(T plus_C *)-N_r(T)`.
3. **Martingale and bracket.** With `G_r(T)=sum_C p_T(C)d_r(T,C)`,
   `M_r(N)=N_r(T_N)-sum_{n<N}G_r(T_n)` is a martingale, and the run report's vector predictable-covariation formula is correct.
4. **2-clade specialization.** `N_2(T_{n+1})-N_2(T_n)` is Bernoulli with parameter
   `g_2(T_n)=(1/n) sum_{v free singleton} exp(-sum_{A strict ancestor v} ell_A/|A|)`,
   hence `<M_2>_N=sum g_2(1-g_2)`.
5. **LLN-scale consequence.** Bounded increments imply `M_r(N)/N->0` a.s.; the source occupation theorem then gives `E[A_r(N)]/N -> 6 h_{r-1}/(pi^2 r(r-1))`.
6. **Finite exact core.** Re-run `artifacts/check_clade_martingale.py` and compare with `artifacts/check_clade_martingale.out`; inspect whether the formal survival-variable model faithfully represents the source growth algorithm.

## Files

- `runs/2026-09-16/2026-09-16T11-49-19Z__report.md`
- `artifacts/check_clade_martingale.py`
- `artifacts/check_clade_martingale.out`
- `artifacts/consequences_2026-09-16.md`
- `artifacts/r2_cherry_counting_process_2026-09-16.md`

## Audit verdict requested

Return PASS / FAIL / UNVERIFIED separately for claims 1–6, with the first exact defect if any. Do not promote the source problem from PARTIAL merely because claims 1–6 pass: separately assess whether the package is sufficiently “useful” in the authors' intended sense to justify any stronger source-level label.
