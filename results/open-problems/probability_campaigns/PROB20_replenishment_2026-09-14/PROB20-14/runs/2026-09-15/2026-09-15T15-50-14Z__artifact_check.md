# PROB20-14 companion artifact check

**Timestamp:** 2026-09-15T15:50:14Z  
**Parent report:** `runs/2026-09-15/2026-09-15T15-47-54Z__report.md`  
**Parent commit:** `70d4eb0c633236f0a2530dafa45f3799764fafba`

Companion exact-arithmetic checker:

`probability_campaigns/PROB20_replenishment_2026-09-14/PROB20-14/artifacts/renewal_switching_identity_check.py`

Artifact commit: `4523aced3f9dbf5f372189f202ff9cbc5cf8b0e8`  
Artifact blob after SHA-specific readback: `fe0f06e3336634f859335133ac88786a14b11b0b`.

The script uses the critical finite-support law
\[
\Pr(\xi=0)=2/5,\quad \Pr(\xi=1)=1/5,\quad \Pr(\xi=2)=2/5,
\]
with `n=6`, target sum `5`, and `d=2`. It enumerates every allocation exactly using Python `Fraction` arithmetic and checks the two exchangeability formulas, equation (3.4), the summed renewal-switching identity (3.7), and the random-permutation occupation interpretation.

An execution of the same archived code in the current run returned

```text
a_n = 2412/15625
summed switching value = 1379/1206
occupation value = 1379/1206
ALL ASSERTIONS PASSED
```

This is only a finite-state algebraic consistency certificate. It is not evidence for the infinite-variance asymptotic theorem and is not independent verification.
