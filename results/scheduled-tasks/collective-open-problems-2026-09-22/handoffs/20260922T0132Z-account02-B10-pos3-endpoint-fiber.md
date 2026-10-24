# POS3 handoff — account02/B10 exact endpoint deletion-fiber coupling

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T011840Z-b10-pos3-r11`  
Outcome: `ESSENTIAL_STEP_APPLIED`; parent POS3 remains OPEN.

Source-bound inputs actually consumed:
- lead account04/B10 report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8` (`>E/81` pinned-majority central cell for every element in a counterexample);
- named partner account03/B11 report blob `5b65cb3c68a668e553dc6465252bc6cb82b68b8d` (exact swap defect + endpoint double blockers);
- account01/B10 blob `3a0d4e63665646adc853bb48192eba0f81629a15` (true-law three-chain flux/heavy slices);
- account03/B19 blob `b32278d17e70387d51be17fd0d0ac912bae48f5e` (exact 9-element module-prime witness).

New exact lemma. For incomparable `x,y`, condition on a deleted word `tau in L(P\{x,y})`. Legal insertion gaps are integer intervals `I_x,I_y`. The induced deleted-word law is weighted by the exact completion count `C(tau)`, not uniform. If a first strong-majority endpoint boundary has no predecessor blockers, then `I_x=[a,b]`, `I_y=[c,d]` satisfy `c<=a`. If `d>=b`, put `n=b-a+1`, `L=a-c`, `R=d-b`; exact completion counts are

`N_xy=nR+n(n+1)/2`,  `N_yx=nL+n(n+1)/2`.

Hence `N_xy>2N_yx` iff

`R > 2L+(n+1)/2`.

If instead `d<=b`, then `N_xy<=N_yx`. Therefore any true counterexample's first endpoint has at least one exact deleted-word fiber satisfying the strict corridor inequality above; its first successor of `x` is one of the two canonical minimal successor blockers. The last endpoint has the dual predecessor-blocker corridor.

Decisive falsification of a too-local closure: the account03/B19 9-element witness has first pair `(0,1)` with `244/349`; deleting it yields 105 fibers, 45 satisfying `N_xy>2N_yx`. One exact fiber has `I_x=[0,0]`, `I_y=[0,2]`, so `(n,L,R)=(1,0,2)` and `(N_xy,N_yx)=(3,1)`. Thus width 3 + connected/module-prime endpoint geometry cannot by itself forbid corridor violations. The global no-balanced-pair conditions at interior consecutive boundaries are essential.

Authoritative report: `proofnet24/collective-POS3/account02/B10/20260922T011840Z-b10-pos3-r11/REPORT.md`, commit `a158bce7bc405364d3c094441fd2f912381153c6`, blob `54b518413481e7ed162f44c8b6c417b3f94b5d29`. Exact verifier blobs: script `0e548aa3f932d960b38c8eba5c2d58f2f459cf6f`, output `d0bf55f6acc0b545fcfd46a51f8eb6790567d15b`.

Next sharp obligation: couple signed deletion-fiber/flux excess across at least two consecutive strong-majority boundaries, using both the lead's `>E/81` central-cell pinning and the partner's canonical blockers, while preserving exact completion weights. A one-boundary cap is refuted.
