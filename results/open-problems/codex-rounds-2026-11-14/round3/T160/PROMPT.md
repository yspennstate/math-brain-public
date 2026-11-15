# Open problem T160: Existence of Kesten's incipient infinite cluster in three dimensions

Statement: For critical Bernoulli bond percolation on Z³, with B_n = [−n, n]³, the conditional laws P_{p_c}( · | 0 ↔ ∂B_n) converge as n → ∞, on events that depend on finitely many edges, to a limiting law: the incipient infinite cluster.

Caveat: Kesten defined the incipient infinite cluster in the plane both by this limit and as the limit of P_p( · | 0 ↔ ∞) as p ↓ p_c, and proved that the two limits exist and agree. If θ(p_c) > 0 on Z³ the limit above exists trivially and equals P_{p_c}( · | 0 ↔ ∞); the content of the question is the case θ(p_c) = 0, which is itself open (T001). The three-dimensional critical exponents are T087, and random walk on the planar incipient cluster is T102.

Source: H. Kesten, The incipient infinite cluster in two-dimensional percolation, Probab. Theory Related Fields 73 (1986) 369–394; D. Basu and A. Sapozhnikov, Kesten's incipient infinite cluster and quasi-multiplicativity of crossing probabilities, arXiv:1603.06884

Where it stands (checked by us, Nov 2026): Known in two dimensions (Kesten 1986; further constructions by Járai, Ann. Probab. 31 (2003); a short quantitative construction by Hillairet, arXiv:2509.18852) and in high dimensions through the lace expansion (van der Hofstad–Járai, J. Stat. Phys. 114 (2004); Heydenreich–van der Hofstad–Hulshof, J. Stat. Phys. 155 (2014), arXiv:1108.4325; Chatterjee–Chinmay–Hanson–Sosoe, arXiv:2502.10882; a bi-infinite version by Cabezas–Fribergh–Heydenreich–Járai, arXiv:2506.06559). Basu–Sapozhnikov (arXiv:1603.06884) prove existence on slabs Z² × {0, …, k}^{d−2}, and on any bounded-degree graph with at most one infinite cluster, which holds on Z³, on which crossing probabilities are quasi-multiplicative; they expect quasi-multiplicativity on Z^d for d < 6, but it is not proved for Z³. Analogues are known for the FK–Ising model on Z^d, d ≥ 3 (Panis, arXiv:2406.15243) and for the metric-graph Gaussian free field (Cai–Ding, arXiv:2412.05709). Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T160 (read it,
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
VERDICT: PARTIAL explicit degree-three critical tree with nonconvergent radius-conditioned laws

An explicit nontransitive tree T of maximum degree three has been constructed with p_c(T)=1/2 and no infinite open cluster at criticality. Nevertheless, conditioning on connection from its root to graph-distance spheres fails to converge on one fixed edge event. At radii N_k+1, where N_k=2^(k^2+10), that edge's conditional opening probability tends to 1/2 along odd k and to 1 along even k. The complete proof is in PROOF.md.

This is a counterexample to an extinction-only general argument, not a counterexample on Z^3 or a proof of T160. The tree lacks transitivity and fails uniqueness of the infinite cluster above criticality. The result supplies an explicit obstruction that a proposed general construction must exclude. No claim of literature novelty is made.

The mechanism is alternating survival probabilities in two branches. At selected depths their suppressed-level counts differ by k. Independently derived bounds give weaker-branch/stronger-branch survival ratio at most 16*2^(−k). The actual critical parameter and critical extinction at every vertex are proved, rather than assumed.

Verification command, run from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py > audit_output.txt 2>&1
```

The run exited 0. It passed 378 exact forward-distribution/backward-recursion comparisons at p=1/3,1/2,2/3; 378 second-moment checks; 126 reciprocal-identity checks; and 16 fixed-edge formulas by exhaustive enumeration of 33,856 configurations. It also checked 32 stage certificates. The data are in stage_certificates.csv. These are bounds derived from the proof, not simulated probabilities. Exact output is in audit_output.txt and copied into LOG.md. Runtime was 0.270 seconds, peak RSS 15,663,104 bytes, one thread. The inherited nice priority was 20; the redundant `nice -n 15` emitted a priority warning and the process retained priority 20.

The proof was checked a second way: its lower survival bound follows both from a second moment and a reciprocal recursion; its upper bound follows both from a plateau union bound and the reciprocal recursion. The root-edge formula was checked against full configuration enumeration, including the case where the unsuccessful branch edge remains open. The graph-distance radius offset and the first stage were checked explicitly.

The literature check ended within four minutes of session start. No verified new solution of the three-dimensional Bernoulli IIC limit was located. Opened sources include:

- Deepan Basu and Artem Sapozhnikov, *Kesten’s incipient infinite cluster and quasi-multiplicativity of crossing probabilities*, [arXiv:1603.06884](https://arxiv.org/abs/1603.06884). Their theorem requires uniqueness and quasi-multiplicativity; the latter is not established here for Z^3.
- Shirshendu Chatterjee, Pranav Chinmay, Jack Hanson, and Philippe Sosoe, *Robust construction of the incipient infinite cluster in high dimensional critical percolation*, [arXiv:2502.10882](https://arxiv.org/abs/2502.10882). Its input is high-dimensional two-point asymptotics; it does not establish the Z^3 statement.
- Malo Hillairet, *Short, Quantitative Construction of the IIC in Planar Percolation*, [arXiv:2509.18852](https://arxiv.org/abs/2509.18852), version 3 dated 28 May 2026. This is a planar construction.
- Raphaël Cerf, *θ(p_c, Z^d)=0?*, [arXiv:2608.23661](https://arxiv.org/abs/2608.23661). Its abstract concerns Bernoulli site percolation and a finite-cluster-tail alternative, not the bond IIC limit.

Search results also included secondary claims about T001. Those were not verified or used, and the present result does not depend on the truth of critical extinction on Z^3. No SOLVED_ELSEWHERE.md was created because no verified solution or substantial new advance of T160 itself was found. This was a short search, not an exhaustive literature review.

What failed or remains uncertain: there is no lattice ratio limit, improved Z^3 bound, or proof of the IIC limit here. The tree obstruction does not apply to the full Basu–Sapozhnikov assumptions. Its novelty was not established.

Next worker: use this example as a test for any proposed compactness/uniqueness proof. Identify a quantitative consequence of transitivity and lattice geometry that prevents alternating dominance of long connections. Establishing such a control on Z^3, rather than only critical extinction or existence of subsequential limits, is the unresolved step. Do not spend time simulating the exponentially large tree; its obstruction is already proved analytically.

Task: “push this problem forward by one checkable piece” — received 14 Nov 2026, approximately 22:02 Asia/Tbilisi.
