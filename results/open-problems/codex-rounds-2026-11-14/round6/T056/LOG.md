# T056 work log

Task: “take the NEXT checkable step on this problem, building on that work.” First explicit clock read: 15 November 2026, 10:12:17 Asia/Tbilisi (06:12:17 UTC); work began a few minutes earlier, and exact prompt-arrival time is unavailable.

## 1. Orientation and bounded literature check

Read the startup memory index, brain navigation index and compute_state.json. State: warn, owner_away_open, CPU saturated. The task-specific instruction to write only in this folder overrides global routines that write mesh, checklist or brain state elsewhere; none was run. No subagents, git, background processes or external mutations.

Inventoried all four earlier folders with rg --files and ls -la. Read their REPORT.md and LOG.md, the original SOLVED_ELSEWHERE.md, and the PROOF.md files of rounds 3, 4 and 5. The original folder has no PROOF.md. No earlier folder contains mathematical scripts. Large combined reads were truncated, so the affected files were read again separately; the transfer proof's middle portion will receive a final separate read. Earlier folders remain untouched.

Shell reads after the initial inventory used OMP_NUM_THREADS=1 nice -n 15. The sandbox prints `nice: setpriority: Operation not permitted`; requested priority was not established. No numerical workload will be run. All commands so far were immediate text reads.

The web literature search took under five minutes. Queries: `"fixed price" group "2026" Gaboriau` and `"A group without fixed price"`. No newer established general resolution was located beyond the manuscript already reported. This bounded check is not exhaustive. The previous manuscript's remaining dependency is being audited, rather than treating its title as proof. No new SOLVED_ELSEWHERE.md is warranted.

Primary sources opened: OpenAI, *A group without fixed price* (5 October 2026), build/paper.tex, build/planar.tex and build/rank-surgery.tex. Base URL: https://github.com/openai/math/blob/main/preprints/A-group-without-fixed-price-October-5-2026/ . The title page confirms author and date; no arXiv identifier verified. Web opening of rank-surgery.tex failed with a cache miss; the read-only GitHub connector successfully opened it. A mistaken URL-only call to github_fetch_file failed schema validation and made no write. Read-only GitHub fetch supplied the full planar source as well.

## 2. Independent recheck of round 5

Re-derived its main model-existence claim from the random-permutation count. The triangular change of basis has inverse b_i=a^-1 u_(i-1)^-1 u_i, so the u_i for i>0 may indeed receive independent uniform permutations. A failing s-row set T fits inside C of size 96s containing T. Counting (T,C) gives binom(n,s)binom(n-s,95s), and independent image containment contributes [binom(96s,s)/binom(n,s)]^99. Bounding these factors gives [K(s/n)^3]^s with K=e^96*96^99/95^95: 99 image constraints minus 1+95 set choices leaves exponent 3. Sum by taking out K*s^3/n^3 and bounding the remaining base by q=K*alpha^3<1/2. The resulting cubic series at q=1/2 is 52. Independently, differentiating sum s^2 q^s=q(1+q)/(1-q)^3 gives (1+4q+q^2)/(1-q)^4, again 52 at 1/2.

For a reduced word of length L, until the first repeated vertex each next positive or inverse permutation entry is unexposed: a previously exposed entry at the newest vertex would require immediate free cancellation. At step t, at most t visited targets among at least n-t+1 choices gives total at most L(L+1)/(2(n-L+1)). Closure requires a repeat. This checks the word estimate without assuming independent starting vertices.

For two distinct rows with two common distinct columns, eliminate the second row to get the fixed-word certificate u_i u_k^-1 u_l u_j^-1. Its triviality would imply equality of u_i u_k^-1 and u_j u_l^-1. The ordered-pair map is injective for unequal indices, including index zero (single positive/negative words), contradicting distinct shared columns. Repetitions within one row have length-two certificates. There are at most Q=100*99+100^4 nonidentity certificates of length at most four. The word bound gives E b <=10Q*n/(n-3). Markov and the expansion union bound make every finite list of freeness and small-bad-row constraints simultaneously attainable for sufficiently large n. A diagonal choice gives the claimed sequence. The earlier result holds. No script existed to rerun.

## 3. One extension chosen before its proof

Audit the coefficient-sensitive planar word lemma, the principal unverified input named by round 5. This is one self-contained piece of the rank dependency; the complete deterministic rank theorem remains a subsequent task. The proof will include the finite filling over arbitrary H, connectivity, dipole removal, exact coefficient-gap equality and the planar corner count.

There is a candidate strengthening worth checking within this same lemma: the graph on inner relator disks is bipartite, because every relator has only positive exterior letters and an arc joins opposite signs. Thus an inner-only face cannot be triangular. Try corner weights 1/2, 1/2, 1 in place of 1/3, 1/2, 1. If valid, this would allow m(r)>=4 and give two matching intervals of length at least m(r)-2. This improvement is provisional until the face walks, bridges, outer loops and coefficient equations are checked in full.

## 4. The strengthened count and its topology

The candidate count works symbolically. Give zero to outer and bigon corners. At other inner corners give 1 if both adjacent edges lead to O, and 1/2 otherwise. Inner-only face walks have even length at least four by bipartiteness and exclusion of inner bigons; their weight is ell/2 <= ell-2. A face with one occurrence of O has weight (ell-1)/2 <= ell-2 for ell>=3. With at least two O occurrences there are at most ell-2 inner corners, each at most one. Euler therefore gives sum_inner(2-c(v))>=2.

A vertex without an O-edge has c=m/2>=2 when m>=4. At any positive vertex, every gap between consecutive O-edges that is not a bigon costs at least one. A gap containing h>=1 inner edges costs 1+(h-1)/2=(h+1)/2. Positivity forces exactly one nonbigon gap, with h<=2, unless all gaps are bigons. Thus a positive vertex supplies a consecutive match with at least m-2 exterior letters and contributes at most one. All-bigon rotation gives a full cyclic match. Otherwise the total contribution forces two distinct positive vertices, whose outer endpoints are disjoint.

Rechecked the construction of the graph from a least-relator expression, with finite true H-relations witnessing all fillings. A component not containing O can be enclosed by a track-avoiding curve representing an element of H killed in D; injectivity removes the enclosed relator disks, contradicting minimality. The same least-number choice excludes dipoles of the same relator: their boundary loops based on the constant common-letter track are actual inverses, even with noncommuting coefficients. Inner loops are forbidden by sign, and different relators have at most one joining edge. These facts imply both simplicity of the inner graph and its bipartiteness.

Face equations are obtained by collapsing exterior circles to the basepoint and evaluating in H. A bigon between inner letters u,v and outer letters u,v has coefficient equation A*B^-1=1, hence A=B in H. No conjugating factor survives: the two tracks are constant and the cut-circle pieces collapse to the same basepoint. Closed tracks inside the face do not change this equation. This addresses the main coefficient-sensitive issue named by round 5.

Read the previously truncated middle of round 4's transfer proof separately with `OMP_NUM_THREADS=1 nice -n 15 sed -n '175,245p' .../PROOF.md`; no missing condition changes the recheck or chosen scope. No numerical program was run.

## 5. Proof saved; attempt to increase the bound fails

Saved PROOF.md with a full proof of the strengthened lemma, including all face types and the coefficient-sensitive topology. An adversarial four-relator example shows that the loss of two is necessary, even for every common exterior length m>=4. Take H=1, shared generators a,b,c,d, and disjoint positive private words A_i of length m-2, with no repeated letters. The relators are adA_0, A_1ab, cbA_2, A_3cd. Pairwise overlaps are exactly a,b,c,d around the four-cycle. W=A_0 A_1^-1 A_2 A_3^-1 is cyclically reduced but trivial in the quotient, since its substituted value is d^-1 a^-1 a b b^-1 c^-1 c d=1. Each relator has only m-2 of its letters anywhere in W, so no interval can match m-1. W has length 4(m-2)>m, so there is no full match. Thus the new m-2 constant is best possible under these hypotheses, not merely an improvement of a slack estimate.

Checked the example a second way at m=4 using A_i=p_i q_i: all eight private letters in W are distinct; every relator has only two private letters, so three-letter matching is impossible by support alone. The quotient identities for A_i were also solved separately from each of the four positive relations to confirm the order and inverse signs.

Other adversarial checks: m=4 inner vertices without outer edges have contribution zero (which is sufficient); h=3 internal edges in the exceptional gap also gives contribution zero and is not selected. Face walks containing repeated vertices and bridges are covered by incidence multiplicity. Outer loops are covered by their number of O-corners. Constant tracks ensure no coefficient conjugator is lost. Finite true H-relations can always be enlarged during a replacement without changing minimality in L. A torsion example with H=C_2 and gap spellings s and s^3 checks the exact intended coefficient conclusion. None invalidates the strengthened lemma.

## 6. Final readback and scope audit

Commands:

```
OMP_NUM_THREADS=1 nice -n 15 cat PROOF.md
OMP_NUM_THREADS=1 nice -n 15 cat LOG.md REPORT.md
OMP_NUM_THREADS=1 nice -n 15 /usr/bin/wc -l LOG.md PROOF.md REPORT.md
OMP_NUM_THREADS=1 nice -n 15 rg -n 'm.r.-2|m.r.-3|m>=|m-1|m-2|89|91|11|20|VERDICT|Task:|q_1|A_1|h.3' PROOF.md REPORT.md LOG.md
OMP_NUM_THREADS=1 nice -n 15 rg --files ~/codex_op_1114/briefs/T056 ~/codex_op_1114r3/briefs/T056 ~/codex_op_1114r4/briefs/T056 ~/codex_op_1114r5/briefs/T056
```

All completed with exit zero and the nice permission warning. Readback counts before this entry: LOG.md 49, PROOF.md 179, REPORT.md 21. The final complete earlier-file inventory confirms that no mathematical scripts were omitted. Corrected an awkward sentence in the explicit m=4 example before final readback; the equations were unchanged.

Checked all six numbered equations in PROOF.md, the order of all four substitutions in the sharpness example, and the precise alternative in the lemma. The downstream discussion now explicitly distinguishes full cyclic matching from the two-interval alternative. The conditional numbers are 91-2=89, 100-89=11, and 31-11=20; equivalently 31-100+91-2=20. They are not used to claim a rank theorem in this session.

REPORT.md starts with the required PROVED verdict and records the sharper lemma, sharpness example, earlier-result recheck, commands, failures, limitations and next task. Only LOG.md, PROOF.md and REPORT.md were created here. No numerical computation was run. The completed piece is the planar matching lemma; shortest-loop reduction, seam extraction and rank surgery remain for the next worker.
