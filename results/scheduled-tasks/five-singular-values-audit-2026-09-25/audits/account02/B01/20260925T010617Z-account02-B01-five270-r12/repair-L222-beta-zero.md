# Line 222 repair

Source `ec211ba2d77a4a9850168c6af1574ea651feaa7c`, TeX blob `c4f2a997cf336ee974e15409b5bccdd8cca039d8`, PDF p.5.

Verdict: FALSE literal sentence, theorem-neutral.

The sentence `Factors with beta_i=0 are at most one and are dropped` is false. For n=4,d=2, choose U with columns e1,e2 and complete with W having columns e3,e4. Then rows 1 and 2 of W are zero, so beta_1=beta_2=0.

Repair: `Factors with beta_i=0 are independent of z, bounded by one, and are dropped.` Any number of zero rows can be discarded. The positive-beta rows still satisfy the same frame identity, and lines 224-226 already allow multiple zero beta_i. No constant or downstream theorem changes.

Independent derivation: found in B01 pass 2 before peer comparison. Account02/B19 had marked line 222 PASS; account03/B05 also gave Lemma 3.2 a PASS while silently using the repaired drop-all-zero-factors operation.
