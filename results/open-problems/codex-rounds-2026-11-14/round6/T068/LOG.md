# T068 working log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded shell clock: 15 November 2026, 10:23:14 Asia/Tbilisi. Work began shortly before that clock.

## Orientation and bounded literature check

Read startup memory and compute state (warn, owner_away_open, CPU saturated). No heavy computation is planned. The specific folder-only rule overrides the earlier global mesh/checklist/brain mutation requirements; no such command, git command, or subagent is used. Brain recall is skipped because earlier logs record that it auto-refreshes shared state outside this folder. All prior folders are read-only.

Initial file search was too broad and produced truncated output; subsequent reads are scoped. Read the first session REPORT.md, LOG.md and SOLVED_ELSEWHERE.md (no PROOF.md or scripts exist there), round-3 and round-4 reports, logs, proofs and scripts, and round-5 proof and log. Re-reading truncated script sections separately before any execution.

Web search queries: `Karp random graph clique log n polynomial algorithm 2025 2026 open problem`; `"Optimal Hardness of Online Algorithms for Large Independent Sets"`. Opened https://arxiv.org/html/2504.11450v2 (David Gamarnik, Eren C. Kızıldağ, Lutz Warnke), https://arxiv.org/abs/2611.09764 (Virginia Vassilevska Williams, Or Zamir, *The k-Clique hypothesis is dead, for good*), and https://randomstrasse101.math.ethz.ch/posts/clique-low-degree/ (Anastasia Kireeva, June 2026 open-problem discussion, not used as a theorem). No general solution found. The worst-case algorithm's exponent remains proportional to k, so its displayed bound does not resolve logarithmic clique search in polynomial time. Literature search closed within five minutes. The no-query extension below will not require an external asymptotic theorem.

## Re-derivation of the round-5 claim

The word reduction holds on independent inspection. Fixing a binary word before graph exposure defines a legal irrevocable strategy. The pre-query budget guard and acceptance budget guard jointly keep its queried output pairs below the source cap, including wrong words; the clique guard ensures a clique. On a successful B trajectory, record one at each final-core positive and zero at each other positive through the kth core vertex. It ends in one, has k ones and at most r zeros. Every accepted vertex on this correct word lies in J, so all guards pass and the private transcript matches B until that stopping round. No later transcript match is needed. Counting nonnegative zero gaps with total at most r gives binom(k+r,r), independently agreeing with the sum over last-one word lengths. At r=n^a and k=(1+eta)log2(n)+O(1), its log cost is a(1+eta)(log2 n)^2+o((log n)^2). The source exponent and the preceding explicit constants therefore hold. An unchanged rerun will also be saved here.

## Chosen extension, before doing it

Sharpen the permissible power a in the special case with no exceptional queries (E empty), as suggested by round 5. Prove a direct sharp tail for irrevocable online clique growth, replacing the external probability exponent min(eta^2,1)/64 by eta^2/2. Then combine with the existing word reduction. The intended exponent is eta^2/2-a(1+eta). This is one extension of the previous bound, restricted to E empty; late-admission loss will remain explicit. The direct argument must handle adaptive inspection order and decisions using all previously inspected edges. Verification will compare the claimed tail to exact finite recurrences and brute-force graph policies, and independently audit the exponent.

## Earlier computation rerun — holds

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r5/briefs/T068/verify_words.py > prior_verification_output.txt 2>&1`, exit 0. All recorded combinatorial totals reproduced: 23,112 legal trajectories, 24,000 original runs, 865,050 guarded runs, 20,832 correct-word/budget events. Guard counts agree exactly (6,355 budget rejections, 83,589 clique rejections, 1,286 query stops, 79,607 word stops). PASS; elapsed 9.040s; peak RSS 18,808,832 bytes; actual nice 20. The unchanged output is saved in this folder. Thus both the independent proof check and rerun support the round-5 result. All previously truncated script sections have now been read separately.

## Direct tail derivation

With genuinely no exceptional queries (not merely zero queried pairs inside J), the row exposed at each chosen vertex is fresh conditionally on the past, even with adaptive order. If an irrevocable strategy has m retained vertices, compatibility has conditional probability 2^(-m), and acceptance probability is at most that. After first reaching s retained vertices, union over the times of its next ell=k-s acceptances. Each fixed time tuple costs at most the product over i=0,...,ell-1 of 2^(-(s+i)), so the conditional tail is at most binom(n,ell) 2^(-s ell-ell(ell-1)/2). This holds after every hitting-time transcript; average over that transcript. Choose s=floor(log2 n). For k=ceil((1+eta)log2 n), the logarithm is -eta^2(log2 n)^2/2-eta log2 n log2 log2 n+O(log n). The first-order coefficient is sharp for greedy: independent geometric waiting times and an equal-time-block event give a matching lower exponent up to O(log n log log n).

Combining with the round-5 word factor gives exponent eta^2/2-a(1+eta), so a<eta^2/[2(1+eta)] is permitted. At the endpoint a=eta^2/[2(1+eta)], keeping both factorial terms yields the stronger residual log bound -(1+2eta)log2 n log2 log2 n+O(log n), still tending to minus infinity. This endpoint was not needed in the initial plan, but follows from the same calculation and will be audited with exact binomial arithmetic. This is still the single no-exceptional-query extension.

## Proof saved

Created PROOF.md with the finite hitting-time bound, the word reduction specialized to genuinely no exceptional queries, the quadratic exponent, its endpoint, and an independent greedy waiting-time argument. The finite estimate is uniform over every permitted transcript and seed. A separate Bellman induction proves that greedy maximizes the finite irrevocable tail: its probability can replace the elementary finite bound in the reduction. This identifies the actual source limitation and does not claim that the disagreement exponent is optimal.

For eta=1/2 and no final late admissions, the new endpoint is a*=1/12, compared with the previous strict ceiling 1/384. At that endpoint the bound is 2^(-2x log2 x+O(x)), x=log2 n. Choosing a=1/24 instead gives quadratic coefficient 1/16. The endpoint coefficient 2 comes from two factorials: (1+eta)x log2 x in the word count and eta x log2 x in the acceptance-time count. Omitting either would give an incorrect endpoint calculation.

Next verification is a new standard-library script, independent of the old simulator: exact pure-birth probabilities versus geometric convolution, all graph inputs for small adaptive policies, aggregate joint-event checks for revising policies, large-integer binomial bounds at the endpoint, and a deliberately illegal look-ahead policy to show why fresh-row independence is essential.

## New verification passed

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_noquery.py > verification_output.txt 2>&1`, exit 0. Complete substantive output:

```text
nice: setpriority: Operation not permitted
nice=20; OMP_NUM_THREADS=1; CPU limit=120s
Exact source checks: upper_bounds=11480; geometric_convolutions=100; block_lower_bounds=820; Bellman_steps=288
All graph inputs n=1..5: source_runs=8792; revision_runs=8792; joint_bounds=560; greedy_exact_matches=30; correct_word_prefixes=13338; mixed_core_D_R=265
Failure fixture with full future information: n=5, k=3; maximum-clique success=159/256; legal greedy success=55/128
Late-admission fixture: complete graph n=7; final=7; core=1; D=0; R=6
Exact constants: eta=1/2; critical_a=1/12; previous_strict_ceiling=1/384; power_ratio=32; interior_a=1/24; interior_coefficient=1/16; endpoint_second_coefficient=2
x=120; k=180; r=2^10; log2_words=727.788983239; log2_source=-2042.132930370; log2_joint_bound=-1314.343947132; endpoint_ratio=1.585788290; factorial_upper=-1284.648641446; geometric_upper=-2055.851014315; block_lower=-2423.954157454
x=240; k=360; r=2^20; log2_words=4656.820484689; log2_source=-7800.483661798; log2_joint_bound=-3143.663177109; endpoint_ratio=1.656605263; factorial_upper=-3133.222085515; geometric_upper=-7819.609638194; block_lower=-8550.957196330
x=480; k=720; r=2^40; log2_words=22998.534358832; log2_source=-30236.686627431; log2_joint_bound=-7238.152268599; endpoint_ratio=1.693013261; factorial_upper=-7226.800732370; geometric_upper=-30262.219995356; block_lower=-31718.471420986
x=960; k=1440; r=2^80; log2_words=102162.640642063; log2_source=-118548.593310096; log2_joint_bound=-16385.952668033; endpoint_ratio=1.722912001; factorial_upper=-16373.601466100; geometric_upper=-118581.533819085; block_lower=-121486.008017202
PASS; elapsed=0.448s; peak_RSS=15106048 bytes
```

Exact source laws were computed by forward pure-birth transitions, independently by convolution of geometric waits, and independently by backward Bellman recursion. Every finite hitting-time upper bound for 1<=n<=40 and 0<=s<k<=n was checked. Greedy graph enumeration agrees exactly with the source recurrence for both inspection rules. Four irrevocable and four revising policies, each with two inspection rules, were checked on every graph of orders 1 through 5: 1+2+8+64+1024=1,099 graphs, times 8 policies gives 8,792 runs in each class. There are 8*sum(n*(n+1),n=1..5)=560 revising joint-event comparisons and 2*sum(n,n=1..5)=30 exact greedy matches. The 13,338 correct-word prefix checks and 265 mixed core/D/R runs exercise the final-disagreement definitions.

The endpoint uses exact large-integer binomials versus independently summed logarithmic products; a direct factorial upper bound equals its separately expanded formula, and natural logarithms recover the same combined probability exponent. A different geometric Chernoff bound verifies the source tail's scale, while time-block events give lower bounds. These checks audit identities and finite policies; they do not use finite enumeration as a substitute for the written general proof. Actual nice=20 satisfies the requested priority despite the launcher's warning; peak memory about 15.1 MB, standard library only, one thread.

## Refinement of the same chosen extension: charge exposed edges

The no-query result and all its checks passed. Before finalizing, the direct tail suggests a weighted version that could preserve the preceding report's exceptional-query allowance. This refines the same chosen extension (a sharper source probability exponent and permissible deletion power), rather than starting a different problem.

For an irrevocable output K, before inspecting v let b be the number of its pairs to K already exceptionally exposed. Conditional acceptance probability is at most 2^(-(|K|-b)); hence the conditional mean of 1_accept*2^(-b) is at most 2^(-|K|). Each such b is predictable before the ordinary row, even when the vertex choice is adaptive. Over the ell accepted vertices after hitting s, the charged pairs are distinct and all lie in the exceptional-query union inside the final output, so their total is at most q on the budget event. Iterating the weighted conditional inequality for each specified acceptance-time tuple should give the finite joint-event source bound min(1,binom(n,ell)*2^(q-s*ell-binomial(ell,2))). Importantly, this is a joint-event bound for any irrevocable algorithm, and does not require its budget cap on other runs.

If verified, the resulting revision bound is the old word factor times this new finite source bound. At q<=c*x^2, the critical deletion exponent becomes (eta^2/2-c)/(1+eta), provided c<eta^2/2; the endpoint still has -(1+2eta)x log2 x+O(x). For the preceding source allowance c=min(eta^2,1)/8 and eta<=1, this increases the strict critical power by a factor 24, while retaining that allowance. At eta=1/2, c=1/32 gives the endpoint 1/16 instead of the old strict ceiling 1/384. Next: write the weighted induction carefully and test it against genuinely adaptive query policies. No claim of this refinement is made until those checks finish.

## Weighted refinement proved and verified

Updated PROOF.md to the general exceptional-query model. The central conditional inequality is E[1_accept*2^(-b_t)|past]<=2^(-|K|), with b_t determined before exposing the current row. In the specified-next-acceptance-time induction, the previous weight and all intervening-rejection indicators are measurable before the next row. Apply the conditional inequality and then drop the intervening-rejection indicator. Charged pairs at different acceptances are distinct because they have different later-inspected endpoints; all remain in the irrevocable final output. On the good-budget event their total charge is <=q, so the probability of that event can be bounded by 2^q times the weighted moment. This does not condition the graph product law on the budget event.

This proves a source joint-event estimate for every irrevocable algorithm, even one violating the cap on other runs. Consequently the word reduction only needs its clique guard: query-budget guards can be omitted in this new proof, because wrong words are handled by their own joint output-budget events. On the correct word the prefix output is a subset of J and the queried union is a subset of E, so it falls in that event. Early stopping remains part of the reduction.

Created an independent query-aware oracle and verification script. Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_queries.py > query_verification_output.txt 2>&1`, exit 0. Complete output:

```text
nice: setpriority: Operation not permitted
nice=20; OMP_NUM_THREADS=1; CPU limit=120s
Exact queried-policy audit: source_runs=43960; revision_runs=43960; source_joint_bounds=10640; revision_joint_bounds=21280; conditional_weighted_tuples=1772; nonzero_charge_runs=22320; full_query_successes=2797
Query-budget constants: eta=1/2; c=1/32; critical_a=1/16; old_strict_ceiling=1/384; ratio=24; half_critical_a=1/32; remaining_coefficient=3/64
Queried endpoint: x=128; k=192; r=2^8; q=512; log2_bound=-1363.328318290; factorial_upper=-1283.970724636; endpoint_ratio=1.521571784
Queried endpoint: x=256; k=384; r=2^16; q=2048; log2_bound=-3398.786883567; factorial_upper=-3386.729148467; endpoint_ratio=1.659563908
Queried endpoint: x=512; k=768; r=2^32; q=8192; log2_bound=-7815.375983042; factorial_upper=-7803.931280560; endpoint_ratio=1.696045135
Queried endpoint: x=1024; k=1536; r=2^64; q=32768; log2_bound=-17668.307247832; factorial_upper=-17655.862957367; endpoint_ratio=1.725420630
PASS; elapsed=3.823s; peak_RSS=15613952 bytes
```

Coverage: every graph of orders 1 through 5, four policies, five query modes, two inspection rules gives 1,099*4*5*2=43,960 source and separately 43,960 revising runs. Query modes include no queries, the entire graph in the first exceptional stage, a future vertex's entire star, an adaptive unknown pair, and edges from a retained clique to future vertices. Adaptive vertex selection uses the known positive and negative edges to the retained set. Every source run checks the charge sum against the actual exceptional union inside its final output. A further 1,772 checks group all graph inputs by complete history at the hitting time and verify the conditional weighted tuple inequality itself, exactly over rational probabilities. Aggregate joint-event inequalities were checked for all k, q, s in the source cases and all k, q, r in revising cases. The 22,320 positive-charge runs and 2,797 full-query successes exercise the cases where unweighted no-query reasoning is insufficient.

Endpoint arithmetic uses the larger q=x^2/32 cap, so it also covers the previous (x-1)^2/32 allowance. Exact large-integer binomials, independent logarithmic products, the expanded factorial bound, and natural-log conversion agree. The new critical exponent 1/16 is exactly 24 times the previous strict ceiling 1/384; its half choice 1/32 leaves coefficient 3/64. All substantive mathematical checks passed. The no-query result remains as the c=0 specialization, strengthened further to allow exceptional queries outside J; greedy's exact optimality is stated only in the genuinely no-query model.

## Report saved and self-audit

Saved REPORT.md with the required PROVED verdict. The final result retains exceptional queries; the earlier no-query-only choice in this chronological log was strengthened by the same direct-tail calculation, not left as the final scope. The main improvement at the prior query allowance is a factor 24 in the critical power, with the endpoint included; the c=0 specialization gives factor 32. Neither factor is presented as an optimal algorithmic threshold.

Re-derived the load-bearing constants by exact fractions and by the expanded exponent: eta=1/2, gamma=3/2, c=1/32, source coefficient eta^2/2-c=3/32, critical a=(3/32)/(3/2)=1/16, half-critical a=1/32, remaining coefficient 3/32-(1/32)*(3/2)=3/64. The earlier ceiling is (1/256)/(3/2)=1/384; (1/16)/(1/384)=24. At the endpoint the x^2 terms cancel exactly, leaving -(gamma+eta)x log2 x=-2x log2 x plus O(x). For c=0 the same calculation gives a=1/12, which was separately audited before the weighted refinement.

Checked the proof's difficult cases: revealed zero edges make acceptance impossible; exceptional sets may repeat ordinarily known pairs, which can enlarge the budget but cannot invalidate the upper bound; current-round exceptional requests occur after the ordinary row and therefore cannot change which edges were fresh at its start; all previously exposed current-to-clique pairs were necessarily exceptional because the current vertex is uninspected. Each charged pair persists in the irrevocable output and is counted once by its later endpoint. The budget event is used only to compare nonnegative weighted indicators, never to assert conditional independence after conditioning on future success. Hitting-time histories include all previous exceptional answers. Wrong words are legal regardless of their budget because the source theorem is a joint-event estimate. This is the precise reason the old budget guards can be removed in this new argument.

Also checked r=0, k=1, s=0, fractional q (the event could equivalently use floor(q)), s=k-1, n not a power of two, independent random seeds, failed clique checks under wrong words, and arbitrarily many temporary changes. The O(1) floor/ceiling errors contribute O(x), including at the endpoint, and cannot change the x log x coefficient. Late-admission loss is still explicit. All substantive checks passed; no files outside the task folder were changed and no git, external writes or subagents were used.

## Final readback — 10:47 Asia/Tbilisi

Read the complete final PROOF.md and REPORT.md from disk and rechecked the round-4 and round-5 report comparisons. Confirmed the exact verdict line, all eight authored artifacts, unchanged prior counts, and both new PASS outputs. The final finite theorem includes q in the exponent, its source estimate is a joint event, and the zero-query optimality assertion is confined to Section 5's no-exceptional-query model. No stale no-query restriction remains in the main theorem. The first recorded task clock is retained explicitly instead of inventing an exact receipt time. All required work for this extension is complete; no further tests were needed after the substantive checks passed.
