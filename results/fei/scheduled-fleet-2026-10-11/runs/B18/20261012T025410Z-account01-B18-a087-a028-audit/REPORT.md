# B18 / A087 proof audit report

Primary packet: **A087 — Restriction referee**  
Reviewed target: **A028 / `B06-A028-LTF-TERMINAL-STOPPING-v1`**  
Verdict: **accepted at restricted scope with one local repair; fresh review required**

The A028 terminal modulation hierarchy is mathematically sound after an
explicit `m=1` endpoint repair.  The all-dimensional one-step Fourier
factorization gives exact entropy and influence telescopes.  Fixing an actual
fresh physical block produces a sign-flipped predecessor with identical
squared spectrum, so the root-minus-mean-child decrement is exactly the
claimed payment.  Querying newest blocks first terminates at a sign-flipped
LTF, and disjoint block variables make the influence ledger nonreusing.

The first gap in the submitted proof is precise: with `r=2/2^m`, the estimate
`-log(1-r)<=r/(1-r)` is applied without separating `m=1`, where `r=1`.
There the function is a signed dictator and directly has `H=0`, `I=1`, so the
theorem and constant survive unchanged.

One wording correction is also necessary.  The multiplier `P_ell` is odd
Fourier mass, not a physical probability of reaching the block; each block
in this complete tree is reached with probability one.  The products
`P_ell H(q)` and `P_ell I(q)` are instead the exact blockwise
root-minus-mean-child decrements.

The imported LTF bound was checked in the owner-approved paper at commit
`b38ba0ab49618ccbe6d1518a34c141dcec9f247c`.  An independent exhaustive
small-cube checker verifies coefficient factorization, entropy and influence
identities, every physical child spectrum, the omitted endpoint, and nested
two-level leaves.

Because this audit repairs a proof line, it is contributor evidence and not
an independent acceptance receipt.  Route the full repaired package to A094
or A085.  The result remains a narrow hierarchy theorem; it does not select a
proper block for arbitrary Boolean functions and does not prove full FEI.

See `RESTRICTION_REVIEW.md` for the reconstruction and
`RESTRICTION_GAPS.json` for the exact gap ledger.
