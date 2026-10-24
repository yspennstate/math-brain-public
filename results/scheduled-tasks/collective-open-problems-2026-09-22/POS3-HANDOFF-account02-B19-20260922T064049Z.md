# POS3 handoff — account02/B19 canonical heavy-state reciprocity

Source run: `20260922T064049Z-account02-B19-pos3-06d9849e`  
Classification: `ESSENTIAL_STEP_APPLIED`  
Parent POS3: OPEN  
Brain status: `WITHOUT_VERIFIED_BRAIN`

Canonical science commit: `b3b294ce9b76526e8a4819ff3ba006ef564dd043`  
Report: `proofnet24/collective-POS3/account02/B19/20260922T064049Z-account02-B19-pos3-06d9849e/REPORT.md`  
Verifier SHA-256: `13b1e77b3891327ee4aea1a077cde7e00d107e7d9067c3657ada6586f94d57a2`  
Output SHA-256: `03087188a963226b9e59363f38986dfd0741b8666b30dc2473c0e9371a4f9c3a`

Consumed current lead: account04/B10 r15, science commit `0c95533fce3b4870b16ede500442a0209df3d9b6`, report blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.  
Consumed named partner: account03/B10 r11, report blob `85fb81cdcbd72f87bcfca53e30f060a83770a1f6`.  
Consumed canonical-blocker dependency: account04/B19, science commit `9bdccf1abda0b25bb605c57079ed0786dbe77148`, report blob `7e142965f79f76b8a3ffb05da2c82080fbae50d2`.

New general lemma: for a heavy state `(x lessdot y; a)`, any outward `t in T_L` automatically creates the heavy state `(t lessdot a; pivot x)`, and the original `y` is a canonical `U_R` return channel. Dually any outward `u in U_R` creates `(a lessdot u; pivot y)` and the original `x` is a canonical `T_L` return channel. Hence graph-theoretic canonical-fringe acyclicity is impossible; the missing theorem must be quantitative/global.

Exact width-three connected autonomous-prime witness: the 11-element 515-extension core from the source report. Its current canonical selector states are

`S0=(5 lessdot 6; pivot 10)`, with unique heaviest canonical weight `72` on `t=1`, and

`S1=(1 lessdot 10; pivot 5)`, with unique heaviest canonical weight `105` on `u=6`.

They form the exact positive-weight greedy cycle

`S0 --72--> S1 --105--> S0`.

Both states have no strict strong-majority interior vertex in either local interval. The witness is not a POS3 counterexample: all 15 incomparable-pair probabilities were checked and five are balanced. In particular `(2,10)=49/103` is a secondary balanced cross-pair at `S1`; this shows why a proof must inspect the full canonical frontier rather than follow only the largest channel.

Next exact implication: **FRONTIER-COMPLETE QUANTITATIVE RETURN EXCLUSION** — in a minimal no-balanced width-three candidate, combine all primary canonical weights with the secondary cross-pairs used to certify outward polarity, and show every reciprocal return produces balance/span descent/width four/autonomous-or-ordinal reduction or transfers controlled conserved charge to a genuinely new frontier. Account03/B10's zero-boundary-defect theorem rules out repairing this by an additive correction to the next pair probability.
