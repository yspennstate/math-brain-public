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
VERDICT: PARTIAL exact finite-box ratio criterion for cylinder convergence on Z³

The next step proposed in round 3 is complete. PROOF.md gives an exact
finite-box counterpart of the tree's survival-ratio criterion. It does not
prove that the required ratios converge at criticality on Z³, and T160
remains unresolved by this work.

For a fixed box B_m, retain the partition π of all boundary vertices and
the root induced by the interior open edges. Let h_(m,n)(π) be the
probability, over exterior edges, of a root-to-∂B_n connection after
identifying vertices according to π. The response uses the join with the
exterior connectivity partition, allowing any number of returns through
other interior components. Let π_star join every boundary vertex and the
root. Then the requested cylinder convergence is equivalent to convergence
of

    r_(m,n)(π) = h_(m,n)(π) / h_(m,n)(π_star)

for every fixed m and every realizable π.

This equivalence includes an exact finite-box law. If a_m(π) is the ordinary
product probability of π and ν_(m,π) is the interior law conditional on π,
then

    μ_n|E(B_m) = Σ_π [a_m(π) r_(m,n)(π) / Z_(m,n)] ν_(m,π),
    Z_(m,n) = Σ_π a_m(π) r_(m,n)(π).

The response at π_star is one. Its ordinary probability a_star is positive,
and a_star ≥ p^((2m+1)^3−1) by opening a fixed spanning tree. If

    D_m(n,l) = Σ_π a_m(π) |r_(m,n)(π)−r_(m,l)(π)|,

the proof gives

    D_m(n,l)/(2+1/a_star) ≤ TV(μ_n|E(B_m), μ_l|E(B_m))
                         ≤ D_m(n,l)/a_star.

The constants concern a fixed box and deteriorate as the box grows.
The argument works for every 0<p<1 and does not assume critical extinction.

One necessary correction to a simpler formulation is proved explicitly:
the root-connected boundary set alone does not determine the exterior
response. In B_1, two interiors with that same set have different responses
to ∂B_3 because an exterior path can return through another interior
component. Section 5 of PROOF.md gives integer coordinates and the positive
response-gap bound p^5(1−p)^823.

The earlier result was independently rechecked and holds. Fresh exact
population calculations and mixture identities agree with the preceding
tree proof. Its critical parameter, vertexwise critical extinction, spine
law, vanishing adjacent weight increments, and full interval of mixture
limits were also rederived analytically in LOG.md.

Reproduction commands, from this folder:

~~~sh
nice -n 15 env OMP_NUM_THREADS=1 python3 recheck.py > recheck_output.txt 2>&1
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
~~~

Both exited 0. The new audit passed 41,760 direct BFS/partition-join
configuration comparisons across 36 finite graph/parameter/target models;
756 conditional atom formulas; 504 partition-mixture/inverse checks;
36 total-variation comparisons; and 768 independent normalization stress
checks. It also checked the actual cubic coordinates, edge counts by two
methods, and explicit spanning trees. Runtime was 0.322 seconds and peak
RSS 16,613,376 bytes. The earlier-result recheck took 0.028 seconds and
14,123,008 bytes, including 64 stage certificates. These are exact finite
checks, not simulation or full-box enumeration. Scripts use the standard
library, one thread, and 120-second alarms. Their inherited nice priority
was 20; the redundant nice request warned but retained that lower priority.
Exact outputs and audit details are saved in this folder.

The five-minute literature check located no verified solution of T160.
Opened sources were Deepan Basu and Artem Sapozhnikov,
[arXiv:1603.06884](https://arxiv.org/abs/1603.06884), whose construction
assumes quasi-multiplicativity; Shirshendu Chatterjee, Pranav Chinmay,
Jack Hanson, and Philippe Sosoe,
[arXiv:2502.10882](https://arxiv.org/abs/2502.10882), using
high-dimensional two-point asymptotics; Malo Hillairet,
[arXiv:2509.18852](https://arxiv.org/abs/2509.18852), concerning the planar
setting; and Zhenhao Cai and Jian Ding,
[arXiv:2412.05709](https://arxiv.org/abs/2412.05709), concerning GFF and
loop-soup models. This was a brief check, not an exhaustive review.

What failed or remains uncertain: the root-boundary-set reduction fails
as above. No contraction across lattice annuli, quasi-multiplicativity,
or asymptotic response-ratio estimate was obtained. The finite-box
criterion is a conditioning identity, with no claim of literature novelty.
It identifies the missing input rather than supplies it.

Next worker: for a fixed m, try to control the weighted oscillation
D_m(n,l) as n,l→∞ at p_c. The corrected state space is the full realizable
interior boundary partition with its root block. Convergence of the
conditioned marked exterior partition law would suffice, but the response
criterion only requires convergence of its finitely many connectivity
functionals. Start with an actual estimate for these ratios; do not repeat
the tree classification or infer convergence from compactness.

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 Nov 2026, approximately 04:58 Asia/Tbilisi.
