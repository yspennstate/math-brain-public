VERDICT: PROVED online clique barrier with bounded final late admissions and arbitrary intermediate revisions

The earlier bounded-deletion result holds: its reduction was independently re-derived and its computation rerun unchanged. The new result follows the earlier report's proposed next step, allowing late admission and readmission. It loses the number of final late vertices from the clique target, with no guessing factor for those vertices. Full proof: [PROOF.md](PROOF.md). This is a deduction from an existing theorem; priority in the wider literature is not established.

The algorithm may replace its clique by any clique among inspected vertices after each inspection round, using the same information model as before. Write J for its final clique, E for its exceptional-query union, P for vertices accepted immediately after their own inspection round, D for inspection rounds of vertices in P\J, and R=J\P. Intermediate deletions and readmissions are unrestricted. Put L=log₂n−1. For every fixed η>0, sufficiently large n, and integer 0≤r≤n,

\[
\Pr\{|J|-|R|\ge(1+\eta)L,\ |D|\le r,
 |E\cap\tbinom J2|\le c_\eta L^2\}
\le\min\left\{1,\left(\sum_{j=0}^r\binom nj\right)2^{-\xi_\eta L^2}\right\},
\quad c_\eta=\frac{\min\{\eta^2,1\}}8,\quad
\xi_\eta=\frac{\min\{\eta^2,1\}}{64}.
\]

For the target (1+ε)log₂n, choose any fixed 0≤β<ε and η=ε−β. Allow |R|≤βlog₂n and |D|≤a log₂n with 0≤a<ξ_η. Under the displayed exceptional-query cap, success has probability at most 2^(−(ξ_η−a−o(1))(log₂n)²). Thus a positive multiple of log n final late admissions is allowed. The query cap must be evaluated at η and may decrease when the allowed late-admission coefficient β increases.

For an explicit choice, let h=min{ε²/4,1}. The caps |R|≤floor(εlog₂n/2), |D|≤floor(hlog₂n/128), and |E∩binom(J,2)|≤hL²/8 give success probability at most 2^(−(h/128−o(1))(log₂n)²). No running-time assumption is needed. Counts D and R measure final disagreement with inspection-time decisions, so the theorem also permits arbitrarily many temporary revisions that do not increase those counts.

The proof guesses D, simulates the complete revising algorithm privately, and builds a separate irrevocable output. On the correct guess that output equals J∩P. Clique and query-budget guards make every wrong guess satisfy the source theorem. A uniformly random guess gives a second derivation of the same multiplicative loss.

Validation commands, all exited 0:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r3/briefs/T068/verify_reduction.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_revision.py
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_counts.py
```

The earlier script reproduced all its recorded counts. The independent revision implementation checked all 23,112 legal clique trajectories across every graph on 1–4 vertices, plus adaptive policies and exceptional queries. In total: 24,808 original runs, 468,796 guarded runs, and 26,405 correct-guess/budget events. Every such event preserved the transcript and produced J∩P. All three guards were exercised. A second enumeration, summing compatible graphs over schedules, reproduced the totals. Exact fractions and independent logarithmic calculations checked the constants and exponents. New scripts ran in 3.709 seconds and 0.001 seconds, respectively, at nice 20 and one thread, with peak RSS below 16 MB. Full output: [LOG.md](LOG.md).

The literature check closed within one minute and found no solution of the unrestricted problem. The source remains David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2). The opened related October induced-matching and November worst-case clique papers do not state a solution to this problem; references and the scope of the bounded search are in LOG.md.

What fails or remains uncertain: removing the |R| loss is invalid for this reduction. Rejecting all vertices until the final update and then choosing a maximum clique has zero exceptional queries and D=∅, but nearly its entire output lies in R. Neither large deletion-disagreement budgets nor unrestricted final late-admission budgets are controlled here. The full OGP source proof remains external. Finite tests audit the reduction, not the asymptotic theorem. The launcher issued a setpriority warning; each computation verified actual inherited nice 20 before proceeding. No substantive verification failed; two illustrative audit fixtures were strengthened during readback.

Next worker: reduce the entropy cost of guessing D when the admissible inspection-time decision vectors have additional structure. For example, a family of at most N possible D sets replaces Σ_{j≤r}binom(n,j) by N in the same guarded reduction. A less immediate next step is a direct stopping-time argument controlling final disagreement, which might improve the deletion coefficient without paying r log₂n. Neither improvement is established here.

Task: “take the NEXT checkable step on this problem, building on that work.” — T068, 15 November 2026, 04:33:47 Asia/Tbilisi (first recorded clock).
