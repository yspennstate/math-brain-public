VERDICT: PROVED sharper clique barrier with polynomial deletion disagreements and bounded exceptional queries

The round-5 result holds: its reduction was independently re-derived, and its unchanged verification reproduced every count. The new result replaces the external dense-graph probability bound with a direct weighted exposure argument. It increases the permissible deletion power by a factor 24 at the preceding exceptional-query allowance for 0<eta<=1, and includes the critical endpoint. The unrestricted Karp problem remains open. The complete proof is in [PROOF.md](PROOF.md).

Use the round-5 model and notation: J is the final clique, P records membership immediately after each vertex's own inspection, R=J minus P, D=P minus J (identified with inspection rounds in the earlier reports), and E is the exceptional-query union. For any integers 1<=k<=n, 0<=s<k, r>=0, and real q>=0, put ell=k-s. The new finite bound is

\[
\Pr\{|J|-|R|\ge k,\ |D|\le r,
         |E\cap\operatorname{pairs}(J)|\le q\}
\le \min\left\{1,
 \binom{k+r}{k}\binom n\ell
 2^{q-s\ell-\binom\ell2}\right\}.
\]

It is uniform over adaptive inspection orders, exceptional-query choices and independent seeds, with arbitrary temporary revisions and no running-time hypothesis. All caps are joint-event conditions.

For x=log2 n, fixed eta>0 and 0<=c<eta^2/2, set

\[
a_* =\frac{\eta^2/2-c}{1+\eta}.
\]

At core target (1+eta)x, exceptional cap cx^2 and |D|<=floor(n^a), each fixed 0<=a<a_* gives probability at most

\[
2^{-(\eta^2/2-c-a(1+\eta)-o(1))x^2}.
\]

At a=a_*, the retained factorial terms still give

\[
2^{-(1+2\eta)x\log_2 x+O(x)}.
\]

The original target (1+epsilon)x with |R|<=beta x uses eta=epsilon-beta, exactly as before. Arbitrary final late admissions remain uncontrolled.

The preceding exceptional cap min{eta^2,1}(x-1)^2/8 is covered by c=min{eta^2,1}/8. For 0<eta<=1 the new endpoint is 3eta^2/[8(1+eta)], compared with the preceding strict ceiling eta^2/[64(1+eta)], a factor 24. For example, epsilon=eta=1/2 and R empty permit

\[
|D|\le\lfloor n^{1/16}\rfloor,\qquad
|E\cap\operatorname{pairs}(J)|\le(x-1)^2/32,
\]

with probability at most 2^(-2x log2 x+O(x)); previously a<1/384 was required. Choosing a=1/32 instead leaves quadratic probability coefficient 3/64. At zero exceptional budget inside J, the corresponding endpoint is 1/12; queries outside J are still allowed.

The key new inequality is elementary. Before an irrevocable algorithm inspects its next vertex, let b be the number of edges to its retained clique already exceptionally exposed. Conditional acceptance probability is at most 2^(-(|K|-b)). Multiplying by 2^(-b) restores a bound 2^(-|K|). Each charged pair has a unique later-inspected endpoint, so the total charge is bounded by the queried-pair count inside the final output. After hitting size s, a union over the times of the next ell acceptances gives the finite source bound. Combining it with the old word family gives the displayed result. Since this source bound itself controls a joint budget event, wrong words no longer require the two query-budget guards; the clique guard remains. The proof retains early stopping at the kth core vertex.

As an independent check, the genuinely no-query irrevocable tail is exactly optimized by greedy. Its geometric waiting times give

\[
\log_2\Pr\{\text{greedy size}\ge\lceil(1+\eta)x\rceil\}
=-\eta^2x^2/2-\eta x\log_2x+O(x).
\]

Thus its quadratic source coefficient cannot be increased uniformly. This does not prove optimality of the deletion power or of the exceptional-query tradeoff.

Validation commands, all exited 0:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T068/verify_words.py > prior_verification_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_noquery.py > verification_output.txt 2>&1
OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_queries.py > query_verification_output.txt 2>&1
```

The prior audit reproduced 865,050 guarded runs and 20,832 correct-word events. New no-query checks compared exact forward recurrences, independent geometric convolutions and backward Bellman recurrences; checked 11,480 finite upper bounds; and enumerated 8,792 source and 8,792 revising policy runs on every graph of orders 1 through 5. The independent query-aware audit checked 43,960 source and 43,960 revising runs, 10,640 source joint bounds, 21,280 revision joint bounds, and 1,772 conditional weighted-tuple inequalities grouped by complete hitting history. Exact binomial integers, logarithmic products and natural-log calculations independently checked the endpoint constants. Detailed commands and outputs are in [LOG.md](LOG.md) and the three output files. All runs were single-threaded, actual nice 20, below 19 MB peak RSS, and below ten seconds.

The bounded literature check found no general solution. The model reference remains David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, [arXiv:2504.11450v2](https://arxiv.org/html/2504.11450v2), Definition 2.1. The new dense-graph inequality does not invoke its OGP theorem. Virginia Vassilevska Williams, Or Zamir, *The k-Clique hypothesis is dead, for good*, [arXiv:2611.09764](https://arxiv.org/abs/2611.09764), was also opened; its stated worst-case exponent remains proportional to k. Priority for the new weighted bound and reduction combination has not been established.

What failed or remains uncertain: no substantive check failed. An unweighted fresh-row argument fails with future information: on five vertices, full-information maximum-clique selection finds a triangle with probability 159/256, compared with greedy's 55/128. The weighted argument accounts for this through charged output pairs. Choosing a maximum clique only after all inspections still defeats any conclusion with unrestricted R. The linear cost q and the word entropy cost may be improvable; no matching revising algorithm or optimal disagreement threshold is proved. The launcher printed a setpriority warning, but every script verified actual nice 20 before computation.

Next worker: improve the advice entropy cost or obtain a direct stopping-time estimate for revising algorithms; the no-query irrevocable source coefficient is already sharp. Compare the bound with a concrete construction that marks an initial candidate set positive at inspection, chooses a seed clique within it, then extends greedily. Track D and R exactly to obtain an algorithmic benchmark for the deletion-power gap. The weighted proof may also support refined charges instead of paying a full factor 2 per pre-exposed pair, but no such improvement is established here.

Task: “take the NEXT checkable step on this problem, building on that work.” — T068, 15 November 2026, 10:23:14 Asia/Tbilisi (first recorded shell clock).
