# fleet01/B12 fixed-multiplicity audit r12

Objective: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924.

Pinned current source: yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f, improvements/interactive/20260924T145418Z-nine-400/paper.tex, blob 19fb119877426b640b2c0dae19ec2f78a399fe11, SHA-256 bf1caf6ae4b4bc33992f501c169b5dc6c795db757b0f6089eff9991391effdf3.

Historical source: commit 7c0d6e60946b19423e6400a12d34b473cf0591e2, manuscript.tex, blob 183ccd294763214e6a707e8d4749ff9a8cf7006d.

Verdict:
- historical lines 1-471 PASS; 472-475 GAP-REPAIRABLE-LOCAL; 476-790 PASS after repair;
- current nine source lines 1-597 PASS; 598-600 GAP-REPAIRABLE-LOCAL; 601-955 PASS after repair;
- FALSE: none found.

Repair: the positive and negative hyperbolic tails must choose their maximizing original coordinates separately. Equal Euclidean norms of the two exponential coefficient vectors do not imply the same physical coordinate is large in both. The two separate cutoffs obey the identical bound, so all constants are unchanged. The separately written nine-eigenvalue paper has the same wording defect and the same repair.

Current theorem after repair:
s_9(A)>=s => ||p_(X^T A X+b^T X+c)||_(infty,ess)<=400 K^2/s
under the full arbitrary-law/sign/dimension/affine hypotheses. Global continuity is not proved.

Historical verify.py is source-hash-bound. Current verify_new.py runs the stored exact/diagnostic suite but does not bind paper.tex by hash before execution; this is a reproducibility gap, not a theorem gap.

Lowest source-complete reviewed multiplicity is 8; a safe reviewed statement is ||p_Q||_(infty,ess)<2400 K^2/s. A newer constant-400 s8 construction exists but no owner release flag is self-awarded here.

The advertised five-singular-value directory still lacks the claimed main.tex/checker: UNCHECKED/PACKAGE GAP.

Fresh provenance repair: fleet03/B13 report 20260924T173304Z cites invalid SHA 8f3de08bd3d346800d3092b527faa8b8ece79c67. The matching resolving commit is 8f3de08bd3a8d68275787d05acb514eff4cfc5b8. This is a repairable provenance gap, not a mathematical counterexample.

Companion improvement proves QFORM-RANKK-TGRAPH-L1-v1, extending the B09 rank-one shared-hub Fourier receiver to arbitrary middle-crossing rank k>=1.

UNCHECKED: PDF rebuild, exhaustive novelty search, absent five-value source/checker, full s7/s6/s5/s4/s3 closure, and global continuity outside Fourier-L1 branches.
