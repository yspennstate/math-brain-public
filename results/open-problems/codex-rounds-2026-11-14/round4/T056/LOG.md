# T056 work log

Task: “take the NEXT checkable step on this problem, building on that work.” Work began 15 November 2026, 00:27 UTC (04:27 Asia/Tbilisi); exact prompt-arrival time unavailable.

## 1. Orientation and literature check

Read the startup memory index and compute state, and inventoried both earlier folders with `rg --files`. The first folder has REPORT.md, LOG.md and SOLVED_ELSEWHERE.md but no PROOF.md or scripts. The round-3 folder has REPORT.md, LOG.md and PROOF.md but no scripts. Reading the earlier material is underway. No subagents or git are used. The task-specific prohibition on writes outside this folder precludes brain recall logging, mesh registration and global checklist updates; these were not run.

Read-only shell commands use `OMP_NUM_THREADS=1 nice -n 15`; `nice` reports `setpriority: Operation not permitted` but the reads complete. No numerical workload has been launched. Compute state: `warn`, `owner_away_open`, CPU saturation reported. Only small text operations are planned.

Web search began at about 00:28 UTC. Queries: `"fixed price" group "2026" Gaboriau`, `"A group without fixed price"`, `"fixed price" "November" "2026" group counterexample`, and `"A group without fixed price" error review correction`. These returned the already-known OpenAI manuscript and no newly established resolution. Opened Ali Khezeli's arXiv page https://arxiv.org/abs/2509.08325 (v4, 4 January 2026), confirming the title and author. This product theorem is not a resolution for all groups. The search portion is now closed, within five minutes. No new SOLVED_ELSEWHERE.md is warranted by this search.

Opened OpenAI, *A group without fixed price* (5 October 2026), through the read-only GitHub connector:
https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/build/finite-models.tex
The file contains Proposition `models:transfer`, the next step named by round 3. A reported counterexample is already known to the previous workers; its remaining proof is the subject of this audit, not an established solution inferred from a title.

## 2. Earlier result independently rechecked

Finished reading both earlier REPORT.md and LOG.md files, the original SOLVED_ELSEWHERE.md and all of round 3's PROOF.md. No scripts were present. Opened the manuscript's compression.tex and deployment.tex as well. A guessed actions.tex path returned 404; the directory listing identifies group-actions.tex as the correct file. Source blobs for compression and deployment agree with those recorded by round 3. finite-models.tex has blob `00ce9e11dab55f6e572b69b4a28f437d8d7cfefc`.

Re-derived the deployment bound through a separate cost ledger. Write m for the mass after subdivision and c for the original graphing cost. Subdivision adds exactly m-1. At one compression, deleting one parent edge for each finite supplied class outside the retained complete set saves the transversal mass k(S;Z minus Y). The retained finite-class transversal lies in a T-complete set of mass at most k(T)+e, so the saving is at least k(S)-k(T)-e. Pushing residual edges must be split at both endpoints; on every such piece it preserves measure and hence its cost. Summing savings gives at least m-k(S_n)-sum e, so the remaining cost is at most c-1+k(S_n)+sum e. This also follows by inductively preserving C_n-k(S_n) <= c-1+sum_{j<n}e_j; the sign and constant agree.

Checked the logical part separately: the alternating process keeps both factor relations increasing, their join full, and their intersection with the J-relation equal to the limiting supplied relation. A shortest alternating path outside J cannot have total displacement in J, by amalgam normal form and freeness. Thus that limiting relation is all of R_J on the enlarged space. Infinite J forces reciprocal class sizes to zero on this fixed finite-measure space. At each finite stage, projection by source/target sheets preserves indexed cost, and the same normal-form argument recovers R_A after supplying R_J. This yields d_X <= c-1+o(1), and then Cost(R_Gamma) >= 1+d_X. No flaw found in the earlier claim.

Independent finite-class check: merging a p-point supplied class and a q-point supplied class, with common atom mass t, decreases component mass from 2t to t and needs exactly one edge of cost t, regardless of p,q. A forest merging h such classes saves (h-1)t. This confirms the component correction without counting subdivision sheets. Infinite classes contribute zero component mass. Finite J would prevent the vanishing step, as the earlier proof correctly notes.

## 3. Chosen extension (before proof work)

Audit only Proposition `models:transfer`: prove d_X >= limsup rk(D_V)/|V| for asymptotically free finite exact A-sets. This is the next step requested by round 3 and is logically independent of the remaining rank/planar argument. The deliverable will include an explicit finite-model error bound, so both the limit order and the exceptional-source contribution can be checked. The construction of expanding finite models and the deterministic rank estimate are outside this session's chosen piece.

## 4. Transfer proof saved

Opened paper.tex to confirm author OpenAI and date 5 October 2026, and group-actions.tex to confirm the words u_i,w,J and the action convention. These are source reads, not further literature searches. Wrote PROOF.md with a full proof of transfer and the finite estimate

```
rk(D_V)/|V| <= C(E) + p + sum_l (1+m_l) Delta_l + (r+1) beta_V(F).
```

Here p is the uncovered measure after selecting finitely many path types, Delta_l is the symmetric-difference error of the l-th paid domain, m_l counts its occurrences, r is the number of selected paid indices, and beta_V(F) is the fraction of sources where the coordinate map F -> V has a collision. The group-label cocycle, its triviality on J, inverse-domain source, exact equivariance, and the generation of every x_v are all proved explicitly. The selected labels and support F are fixed before passing to k. Taking p=epsilon and weighted cylinder error < epsilon gives C(E)+2 epsilon in the limit; this is just a tighter account of a vanishing error than the source's C(E)+3 epsilon, not a new positive cost gap.

All four questioned steps hold on this audit. For an inverse step after prefix h the list entry is at vh g_l^{-1}. Finite configurations need not belong to the original conull free set: cylinder predicates are defined on the full product, and their formal path labels remain exactly a. Exactness gives xi_{vq}=xi_v q. Repeated path vertices and stabilizers do not alter the cocycle identity. The generating-list inequality holds for every labeling, so expectation suffices without concentration.

One patch attempting to append to this log used a partial-line context and was rejected; PROOF.md had already been saved successfully. The append is corrected here. No mathematical computation or external write occurred.

## 5. Attempts to break the proof

Re-derived the weighted error in two ways: the symmetric-difference union bound for path predicates, and the L1 difference of the total paid-count-plus-failure functions W,W'. Both give p+sum(1+m_l)Delta_l. Re-derived the exceptional-source coefficient both by summing r+1 local-law errors and by splitting sources into good/bad, with the bad count bounded pointwise by r+1. Both give (r+1)beta, with no stochastic independence across sources.

An explicit inverse example uses g=b_1 a^{-1}, then the formal path g^{-1},b_1 has product a. The correct list entry comes from y=vg^{-1}: theta(y,g)=x_v^{-1}. Its inverse is x_v. This independently checks both the inverse-domain origin and multiplication order. Rechecked generation in the subgroup generated by the list, not merely its normal closure: induction over path prefixes uses only multiplication of listed factors and inverses, never conjugation by arbitrary elements.

For the trivial one-point action the presentation is C_100, although all endpoints coincide; this checks why the cocycle must retain labels. The number 100 is checked both by the 0,...,99 row indices and by counting 99 a's in u_99 plus the final a in w. The presentation maps onto Z/100 and is generated by an element of order dividing 100, so the group has exactly order 100. Its constant configurations violate the product law at any two distinct coordinates, giving beta=1; omitting the collision error would be unjustified. The theorem excludes this sequence through (3).

Checked the remaining boundary cases: nonfree finite configurations, configurations outside the original free conull subset, nontransitive actions, overlapping domains, repeated steps, repeated list entries, no paid indices, and coordinate support of size zero or one. None invalidates the selected estimate. Added the elementary conull-freeness argument and specified nonempty V to make all denominators explicit. No positive rank lower bound, expansion theorem, or planar estimate has been verified in this session.

Read PROOF.md and LOG.md back from disk with `OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'cat PROOF.md; cat LOG.md; wc -l PROOF.md LOG.md'`. Exit 0; line counts before the latest amendments were PROOF.md 291 and LOG.md 46. The nice warning persists. All reads were small and immediate; no numerical script was needed.

## 6. Final report and audit (00:33 UTC)

Saved REPORT.md with first line `VERDICT: PARTIAL proof audit of the Bernoulli-to-finite-model transfer inequality`. It states what is newly checked, the earlier-result recheck, the finite error bound, failed access/patch attempts, compute limitation, and remaining dependencies. Read it back using

```
OMP_NUM_THREADS=1 nice -n 15 /bin/zsh -c 'cat REPORT.md; wc -l LOG.md PROOF.md REPORT.md; rg -n "\\\\tag|VERDICT|Task:|beta|rank|Next worker" REPORT.md PROOF.md'
```

Exit 0. Counts before this final log append: LOG.md 59, PROOF.md 291, REPORT.md 34. The output confirmed the verdict, all twelve numbered equations, the explicit finite correction, and the task/time line. The report's uncertainty sentence was then simplified without changing its substance. Rechecked the direction of the infimum and limsup: each fixed admissible graphing bounds the limsup from above, hence taking its cost infimum gives d_X >= limsup. Combining with deployment gives only a conditional route to a positive gap.

All deliverables are in this folder. No outside files were edited. Next checkable dependency is the finite-model existence proposition `models:sequence`; deterministic rank and planar estimates follow it. Work on the chosen transfer piece is complete.




