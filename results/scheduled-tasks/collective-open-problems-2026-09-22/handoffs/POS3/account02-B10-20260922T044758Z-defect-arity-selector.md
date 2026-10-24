# POS3 account02/B10 — defect/arity selector handoff

Outcome: `ESSENTIAL_STEP_APPLIED`; POS3 remains OPEN.

Source-bound science report: `yspennstate/math-open-problems`, `proofnet24/collective-POS3/account02/B10/20260922T044758Z-b10-r12-9941265a/REPORT.md`, creation commit `f0705b24f2482ed219b61cf0a13c168fa406ed5c`.

Latest lead consumed: account04/B10 r13, commit `fdfdc6be6943abfdef73c950a71c528bf582c6e8`, report blob `6acb56ae36d1cf3c59af1b9d22cc1b0cb2f70f44`. Named OTHER-account partner consumed: account03/B11 r11, commit `34def82ee82e3eb7fbc4f0f7783b82d13bdec4a1`, report blob `fd48b47637ca81a6c25fa5c52f8898e596662062`.

New lemma: if an endpoint has minority `epsilon<1/3` and exact original-law blocker transport gives at most `m` canonical outward minority events `E_i` with `Pr(union E_i)>=1-2 epsilon`, then

`max(epsilon, Pr(E_1),...,Pr(E_m)) >= 1/(m+2)`.

Proof is the exact union-mass inequality plus the union bound; no independence and no uniformization of a projected deletion law.

Applied to the lead's strict predecessor-nested terminal corridor after span descent is exhausted:

- majority-early has at most 2 positive blocker channels, hence a canonical pair with minority in `[1/4,1/3)`;
- majority-late has one lower-chain channel plus at most 2 upper blocker channels, hence a canonical pair with minority in `[1/5,1/3)`;
- therefore the unified strict-chain terminal selector improves from `>1/6` to `>=1/5`.

Applied to account03/B11's exact-two-distinguisher branch, the defect arity is 2 regardless of `d||u` versus `d<u`, so some endpoint/fringe pair has minority in `[1/4,1/3)`. Thus the comparable-fringe anti-cycle problem is unnecessary merely to preserve quantitative progress: stop locally at the `1/4` threshold.

Fresh adversarial validation: account02/B19's 515-extension autonomous-prime `d<u` period-two fringe cycle remains valid, but its two cycle endpoints have minority counts `141/515` and `161/515`, both above `1/4`; hence it refutes greedy well-foundedness but not the new stopping rule.

First unpaid implication: globally amplify the canonical `[1/5,1/3)` terminal selector to `1/3` (or force span descent / four-antichain / proper autonomous nonchain) using the three-chain cumulative-band/blocker structure while retaining the full union flux `1-2 epsilon`.

No closure or novelty claim.