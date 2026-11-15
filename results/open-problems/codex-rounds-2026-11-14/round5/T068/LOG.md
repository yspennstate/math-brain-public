# T068 working log

Task: “take the NEXT checkable step on this problem, building on that work.” First recorded clock: 15 November 2026, 07:56:03 Asia/Tbilisi (03:56:03 UTC).

## Orientation and bounded literature check

Read the three earlier REPORT.md and LOG.md files, the round-3 and round-4 PROOF.md files, startup memory, brain navigation index, and compute governor state. The initial folder has no PROOF.md or scripts; its SOLVED_ELSEWHERE.md will also be read. Read the earlier Python scripts before executing them. Long combined tool outputs truncated, so any truncated script sections are being read separately. All earlier folders remain read-only. The current folder-only instruction overrides the general requests for global checklist, mesh and brain writes, including recall commands that can refresh an index outside this folder. No git or subagents.

Governor: status warn, mode owner_away_open, CPU saturated, 63 percent free memory. Only tiny, sequential, standard-library verification is planned. Commands use OMP_NUM_THREADS=1 and nice -n 15; the launcher reports a setpriority warning. Actual inherited priority will be checked by every verification script.

Web search queries: “Karp random graph clique log n polynomial algorithm 2026 2025 online Gamarnik Kızıldağ Warnke”; “2504.11450 clique online”. Opened https://arxiv.org/abs/2504.11450 and https://arxiv.org/html/2504.11450v2 : David Gamarnik, Eren C. Kızıldağ, Lutz Warnke, *Optimal Hardness of Online Algorithms for Large Independent Sets*, latest listed version v2, 30 January 2026. Also opened https://arxiv.org/abs/2610.40369 : Abhishek Dhawan, Eren C. Kızıldağ, Neeladri Maitra, Cheng Mao, Timothy L. H. Wee, *Half-Optimal Induced Matchings in Random Graphs: Online and Low-Degree Algorithms*; and https://arxiv.org/abs/2605.03893 : David Gamarnik, Miklós Z. Rácz, Gabe Schoenbach, *Optimal Hardness of Online Algorithms for Large Common Induced Subgraphs*. Their stated results concern different optimization problems. No solution of unrestricted Karp clique search found. Search closed after these calls, within five minutes; this bounded search is not an absence certificate. No SOLVED_ELSEWHERE.md warranted.

## Independent re-derivation of the round-4 claim

The main claim holds on re-derivation. For a fixed deletion-round guess T, preserve B's private state separately from the irrevocable clique K. Guard both growth of the exceptional-query union and growth of K, and guard clique membership. Every guess therefore meets the external theorem on every graph. On a successful run, T=D gives K_t=(J∩P)∩V_t: v_t∈P is determined by C_t at its own inspection, and an inspection-time positive outside J is exactly a round in D. All query and clique guards pass because K⊆J and the simulated queries form a subset of E. Thus the correct simulation equals J∩P at the end even with arbitrary temporary revisions. The union bound costs Σ_{j≤r} binom(n,j). Complementation gives L=log₂n−1, c=min(η²,1)/8, ξ=c/8, and success bound 2^(−ξL²). The original OGP theorem remains external.

## Chosen extension, before implementation

Replace inspection-round guessing by a fixed family of binary words on inspection-time positive decisions, stopping once k final-core vertices have been retained. On the correct word, the first k final-core positives are retained and earlier positives absent from J are skipped. There are at most r skipped positives before the kth retained one. Words with k ones, at most r zeros, and last symbol one number Σ_{d=0}^r binom(k+d−1,d)=binom(k+r,r). This may replace the old factor Σ_{j≤r} binom(n,j) without restricting the family of D sets. Keep all three guards for wrong words and halt the simulation once the word is exhausted. Target k=ceil((1+η)L). Planned consequence: polynomially many final deletion disagreements, r≤n^a with a<ξ/(1+η), still yield a vanishing 2^(−Ω((log n)²)) success bound. This is the one chosen extension. It needs a full prefix invariant, a count checked two ways, and adversarial tests of early stopping and wrong words.


## Earlier computation rerun and source checked

Command: `OMP_NUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T068/verify_revision.py`, exit 0. Output reproduced all earlier totals: 23,112 exhaustive trajectories on 75 graphs; combined 24,808 original runs, 468,796 guarded runs, 26,405 correct-guess events; guards budget_reject=9,593, clique_reject=56,599, query_stop=2,804. Arithmetic outputs reproduced log2M=8191 and exponent=-8185.000976562 at x=4096, and log2M=32763.415037499 and exponent=-32756.585939063 at x=8192. Actual nice=20; elapsed=4.825s; peak_RSS=15,253,504 bytes. Thus the re-derivation and unchanged computation both support the round-4 result.

Opened the source HTML at Definition 2.1 and Theorem 2.2 again, retaining condition (1) and the explicit c and ξ. This was proof-source reading after the search closed. Ordinary and exceptional stages match the simulations; repeated pairs in S_t are counted in its union. Read the first folder's SOLVED_ELSEWHERE.md and the round-4 audit_counts.py in full, and separately read the tail of verify_revision.py after combined output truncation.

Wrote PROOF.md with the word-family reduction, its exact binomial cost, polynomial disagreement consequence, and a second Bernoulli-thinning derivation of the leading exponent. Key change: stop the private simulation immediately after consuming the final word symbol. Correct-word transcript preservation is claimed only through the kth final-core vertex. It need not hold through B's final update. One attempted no-op append patch failed to match its context and changed no file; subsequent log appends use a direct append.


## Verification script saved and running

Created verify_words.py as a separate set-based implementation with a graph-query oracle. It re-executes the policy from its known-answer dictionary for each word, enforces all guards, and checks correct-word transcript equality only through its stopping round. Planned exhaustive coverage: all legal clique trajectories on every graph on 1–4 vertices, all k=1,…,n, every word with at most min(n,2) zeros; adaptive policies additionally exercise exceptional queries and budgets 0,1,3. Longer words that cannot finish within n inspections are included too. Counts will be recomputed independently by summing schedules before compatible graphs.

Arithmetic checks independently enumerate all binary words for 42 (k,r) pairs, check Pascal counts, and compare exact integer binomial coefficients with a logarithmic product. A separate Bernoulli cost checks the asymptotic coefficient. Explicit constants for ε=1, β=1/2 are c=1/32, ξ=1/256, a=1/768, and ξ−a(1+η)=1/512. Large-n examples use x=7680,15360,23040 and exact integer r=n^(1/768)=2^10,2^20,2^30. No random-graph sampling is used to claim the asymptotic result.

Command started: `OMP_NUM_THREADS=1 nice -n 15 python3 -B verify_words.py > verification_output.txt 2>&1`. Output is saved in this folder. CPU limit 180s; actual priority and peak RSS are checked inside the script.


## Verification passed; adversarial fixtures added

The first verify_words.py run exited 0 in 9.398s with peak RSS 18,644,992 bytes, actual nice 20. It checked 865,050 guarded runs, 20,832 correct-word events, and all three guards. A targeted fixture was then added because the all-trajectory sample had no case with more than r total disagreements but at most r disagreements before the kth core vertex. The new fixture has n=7, core={0,1}, four final deletion disagreements after round 2, and correct word 11 with no zeros. A second fixture rejects everything until final maximum-clique selection, checking that its core has size one and the R loss remains essential.

Reran the same command after adding only those fixtures. Final complete output:

```text
nice: setpriority: Operation not permitted
nice=20; OMP_NUM_THREADS=1; CPU limit=180s
Exact word-family cases=42
epsilon=1; beta=1/2; eta=1/2; c=1/32; xi=1/256; a=1/768; coefficient=1/512
x=7680; k=11519; r=1024; old_explicit_r=15; log2N=5110.385320166; thinning_cost=5116.649753004; log2_bound=-225229.618586084; leading=-115200.000000000
x=15360; k=23039; r=1048576; old_explicit_r=30; log2N=160495.839408687; thinning_cost=160504.395379587; log2_bound=-760984.164497563; leading=-460800.000000000
x=23040; k=34559; r=1073741824; old_explicit_r=45; log2N=565581.808605731; thinning_cost=565590.672720984; log2_bound=-1507838.195300519; leading=-1036800.000000000
Prefix fixture: core=2; total_D=4; guessed_zeros=0; stopping_round=2
Late-admission fixture: final=7; core=1; D=0; R=6; E=0
All-trajectory audit: {'correct_events': 18750, 'deletions_after_stop': 3000, 'early_stops': 11255, 'exhaustive_graphs': 75, 'exhaustive_trajectories': 23112, 'guarded_runs': 780594, 'late_and_deleted': 3066, 'original_runs': 23112, 'prefix_only_events': 0}
Combined audit: {'correct_events': 20832, 'deletions_after_stop': 3190, 'early_stops': 12507, 'exhaustive_graphs': 75, 'exhaustive_trajectories': 23112, 'guarded_runs': 865050, 'late_and_deleted': 3242, 'original_runs': 24000, 'prefix_only_events': 0}
Guard coverage: {'budget_reject': 6355, 'clique_reject': 83589, 'query_stop': 1286, 'word_stop': 79607}
Independent totals: trajectories=23112; original=24000; guarded=865050
PASS; elapsed=11.043s; peak_RSS=19480576 bytes
```

The independent schedule-first enumeration reproduces the 23,112 legal trajectories and the combined 24,000 original and 865,050 guarded runs. The exact binomial values agree with a separate sum of logarithms; Bernoulli thinning independently verifies the leading coefficient 1/512. The targeted fixtures do not contribute to the main enumeration counts. All computations are standard-library only, single-threaded, under 1 GB, and under 20 minutes. The launcher warning persists, but the actual inherited nice value is 20.


## Self-audit and report saved

Audited the word family at r=0 (only k ones), k=1 (up to r zeros then one), and word lengths greater than n (legal fixed strategies that may not finish). Guards count the union of exceptional requests even when edges were previously known. B's independent seed is shared with each simulated strategy; the word family is fixed independently of graph and seed. Wrong word symbols are consumed even when their acceptance test fails; the algorithm then stops at word exhaustion, and its output still meets the source theorem. On the correct word every acceptance guard passes because its output is contained in the fixed final clique J.

The induction preserves only a prefix transcript: asking it to preserve the complete trace would require guessing all later disagreements and would lose the improvement. The kth core vertex exists on the event, and its word has at most |D| zeros. Query guards occur before irreversible requests, including the stopping round's requests. Later B queries do not occur in the stopped simulator. Removing either budget guard is unsupported and is explicitly excluded. A vertex accepted at inspection, deleted, then readmitted belongs to the core if finally retained, irrespective of its intermediate absence.

Rechecked the exponent independently: log2 binom(k+r,k)≤k log2(e(k+r)/k), with k=(1+η)x+O(1). At r≤n^a this is at most a(1+η)x²+o(x²); the source cost is ξ(x−1)²=ξx²+O(x). The Bernoulli factor p^(−k)(1−p)^(−r), p=k/(k+r), reproduces that leading cost. For r=O(x), binom(k+r,r)≤2^(k+r) gives only O(x) log-cost. Exact fractions confirm h/64−[h/(128(1+ε/2))](1+ε/2)=h/128. For ε=1: h=1/4, c=1/32, ξ=1/256, a=1/768, remaining coefficient=1/512. The ceil inequality k≤(1+η)x−η justifies the target conversion; no rounding of a negative threshold is used because n is sufficiently large.

Saved REPORT.md with the required PROVED verdict, exact bound, comparison with the preceding report, commands and outputs, uncertainties, and next-step suggestions. No general solution or literature priority is claimed. No file outside this task folder was changed, and no git, external write, global coordination mutation, or subagent was used.


## Final readback

Read the full PROOF.md and REPORT.md from disk. Rechecked the three membership cases in the correct-word induction, event-level quantifiers, the stopping rule after failed wrong-word acceptance, and the late-loss and polynomial-budget conversions. Added the explicit source-density inequalities n≥2d and n≥2^d and the derivative calculation for the Bernoulli optimum. These are proof explanations, with no code or theorem change. All numerical and finite checks already passed; no repeated testing was needed. Final artifact check confirms the exact verdict line and all five authored files. The final verification run exited 0. This completes the chosen extension.
