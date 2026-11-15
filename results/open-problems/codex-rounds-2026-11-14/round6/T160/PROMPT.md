# Open problem T160: Existence of Kesten's incipient infinite cluster in three dimensions

Statement: For critical Bernoulli bond percolation on Z³, with B_n = [−n, n]³, the conditional laws P_{p_c}( · | 0 ↔ ∂B_n) converge as n → ∞, on events that depend on finitely many edges, to a limiting law: the incipient infinite cluster.

Caveat: Kesten defined the incipient infinite cluster in the plane both by this limit and as the limit of P_p( · | 0 ↔ ∞) as p ↓ p_c, and proved that the two limits exist and agree. If θ(p_c) > 0 on Z³ the limit above exists trivially and equals P_{p_c}( · | 0 ↔ ∞); the content of the question is the case θ(p_c) = 0, which is itself open (T001). The three-dimensional critical exponents are T087, and random walk on the planar incipient cluster is T102.

Source: H. Kesten, The incipient infinite cluster in two-dimensional percolation, Probab. Theory Related Fields 73 (1986) 369–394; D. Basu and A. Sapozhnikov, Kesten's incipient infinite cluster and quasi-multiplicativity of crossing probabilities, arXiv:1603.06884

Where it stands (checked by us, Nov 2026): Known in two dimensions (Kesten 1986; further constructions by Járai, Ann. Probab. 31 (2003); a short quantitative construction by Hillairet, arXiv:2509.18852) and in high dimensions through the lace expansion (van der Hofstad–Járai, J. Stat. Phys. 114 (2004); Heydenreich–van der Hofstad–Hulshof, J. Stat. Phys. 155 (2014), arXiv:1108.4325; Chatterjee–Chinmay–Hanson–Sosoe, arXiv:2502.10882; a bi-infinite version by Cabezas–Fribergh–Heydenreich–Járai, arXiv:2506.06559). Basu–Sapozhnikov (arXiv:1603.06884) prove existence on slabs Z² × {0, …, k}^{d−2}, and on any bounded-degree graph with at most one infinite cluster, which holds on Z³, on which crossing probabilities are quasi-multiplicative; they expect quasi-multiplicativity on Z^d for d < 6, but it is not proved for Z³. Analogues are known for the FK–Ising model on Z^d, d ≥ 3 (Panis, arXiv:2406.15243) and for the metric-graph Gaussian free field (Cai–Ding, arXiv:2412.05709). Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T160 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T160 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T160 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T160 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.




----- earlier REPORT.md -----
VERDICT: PARTIAL uniform BK localization estimate for the finite-box exterior response on Z³

The round-4 criterion holds. This session adds a quantitative estimate for
its exterior partition state, under the extinction premise relevant to T160.
It does not prove existence of the three-dimensional IIC.

Fix m<R<n. In the unwired open graph E(B_R) minus E(B_m), let N_(m,R)
count components meeting both ∂B_m and ∂B_R. Write H_(m,j) for the exterior
connection from ∂B_m to ∂B_j and b_(m,j)=P_p(H_(m,j)). PROOF.md proves

    P_p(N_(m,R) >= k | H_(m,n)) <= b_(m,R)^(k-1),   k >= 1.

The constant is one. The proof constructs disjoint open witnesses for one
connection to ∂B_n and k−1 connections to ∂B_R, then applies BK. It allows
components to merge beyond B_R and does not apply BK directly to the
nonmonotone component-count event.

When N_(m,R)=1, the full marked exterior partition at radius n is determined
by the configuration through radius R: retain its entire partition of ∂B_m
and mark its unique component reaching ∂B_R. Extending that rule arbitrarily
to the exceptional configurations defines L_(m,R). Simultaneously for all
realizable interior partitions π, the earlier normalized responses satisfy

    |r_(m,n)(π) − E_p[K_m(π,L_(m,R)) | H_(m,n)]| <= b_(m,R).

The corresponding normalized interior laws differ by at most b_(m,R)/a_star
in total variation, with the same fixed-box constant a_star as round 4.
These errors are uniform over n>R. If θ(p)=0, then

    b_(m,R) <= (24m²+2) P_p(0 ↔ ∂B_(R−m)) → 0.

As a consequence, assuming θ(p_c)=0, every subsequential cylinder limit
has a unique infinite open cluster containing the root, and that cluster
has one end. This does not select a unique limiting law. No literature
novelty is claimed for this application of BK.

The remaining oscillation now has the explicit bound

    D_m(n,l) <= 2 b_(m,R)
               + TV(Law(L_(m,R) | H_(m,n)),
                    Law(L_(m,R) | H_(m,l))).

The last term remains uncontrolled. Local measurability of L_(m,R) does
not make its law under distant survival independent of n. Dropping that
conditioning, discarding finite return components, or inferring convergence
from the one-endedness conclusion would leave a gap.

All three earlier folders were read and left unchanged. The main round-4
claim was rederived from conditional atom probabilities and independently
checked by 9,216 full-connectivity/contraction comparisons, 144 atom laws,
108 partition inversions and 9 two-sided TV comparisons. Its cubic return
witness and closed-edge exponent 823 also hold.

Reproduction commands, run in this folder:

~~~sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 independent.py > independent_output.txt 2>&1
~~~

Every command exited 0. The new audit enumerated 2,560 configurations on
six finite graphs, checking 1,572 disjoint-path inclusions, 874 exact
one-active-component reconstructions, 69 tail bounds, 240 response
approximations and 36 normalization bounds. Cases include outer mergers,
returns, cycles and multiple targets. A separate bitset-closure calculation
reproduced all 90 exact probability values in certificates.csv. These are
finite checks, not simulation or enumeration of full cubic boxes.

All runs used the standard library, one thread, a 120-second alarm and
inherited nice priority 20. The redundant nice request warned and retained
that lower scheduling priority. Each final run took under 0.1 seconds and
used under 17 MB peak RSS. Commands, exact output and adversarial checks
are recorded in LOG.md.

The initial literature check found no verified resolution of T160. Opened
sources still distinguish the conditional Bernoulli construction of
Deepan Basu and Artem Sapozhnikov,
[arXiv:1603.06884](https://arxiv.org/abs/1603.06884), from high-dimensional,
planar and GFF results. In particular, Remark 1.2 of Jian Ding and Zhenhao
Cai's [October 2026 paper](https://doi.org/10.1007/s00220-026-05772-5)
explicitly assumes Bernoulli quasi-multiplicativity. All opened sources
are listed in LOG.md. No SOLVED_ELSEWHERE.md is warranted.

Next worker: seek a bound on the conditional-law distance in the displayed
oscillation estimate, or on its finitely many K_m functionals. It would
suffice to make its limsup as n,l→∞ arbitrarily small by choosing large R.
This requires an input beyond extinction, such as a usable comparison of
far-survival weights for the local states. Do not repeat the tree
classification or treat the finite verification as evidence of that input.

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 08:31 Asia/Tbilisi.
