B08 r13 source-pinned audit handoff.

Source commit: ec211ba2d77a4a9850168c6af1574ea651feaa7c
short.tex blob: c4f2a997cf336ee974e15409b5bccdd8cca039d8

Reviewed: lines 163-173, 177-240, 243-269, 271-391.

New local defect: line 222 falsely says beta_i=0 factors are at most one. Counterexample n=3,d=2,U=(e1,e2),W=e3 gives beta1=beta2=0. Safe repair: drop the count claim; every zero-beta factor is <=1 and may be dropped. Constants unchanged.

C02 reproduced: lines 319-322 need Jensen |E F|^2 <= E|F|^2 before (4.5). Lemma 4.3 then checks through Step 5.

No theorem-level contradiction found in reviewed range. Full manuscript pass incomplete; earliest unchecked line 1.