# T283 work log

All new files stay in this directory. No git, uploads, messages, GPU, or external writes are authorized. Computations will use one thread, BelowNormal priority, and less than 1 GB RAM.

## 2026-11-14: orientation and literature check

Read `~/AGENTS.md`, skimmed the memory index, and inspected the recall entry point. The current session's folder-only/no-git instructions override older offload and memory-write instructions.

Used the web search tool for `arxiv 2607.20318 Mao low degree counterexample explicitness uniform sampler`, `2505.17360 low degree`, `Mao uniform low-degree sampler 2026`, and searches combining the paper number with explicitness, sampler, and November. Opened the actual arXiv pages and Mao's v2 HTML:

- Songtao Mao, *The Polynomial-Time Low-Degree Conjecture is False*, arXiv:2607.20318v2, revised 28 October 2026. https://arxiv.org/html/2607.20318v2
- Rares-Darius Buhai, Jun-Ting Hsieh, Aayush Jain, Pravesh K. Kothari, *The Quasi-Polynomial Low-Degree Conjecture is False*, arXiv:2505.17360. https://arxiv.org/abs/2505.17360

Mao Section 4 still explicitly leaves polynomial-time selection of a good evaluation seed open. Its explicit trace subspace removes the earlier subspace advice. No solution of the whole stated problem was found in this bounded search. Search results about structural repairs do not settle this question. No SOLVED_ELSEWHERE.md is warranted.

## Chosen piece (before proof work)

Prove a sharper deterministic conversion from independence of evaluation vectors to independence of graph edges in the random alternating-form construction. Mao Proposition 2.6 uses at most L/2 edges because their endpoints number at most L. Investigate whether every L-wise independent vector family actually gives uniform marginals on L-1 edges, and whether that threshold is sharp. This is a finite linear-algebra question with a complete proof and exhaustive small-instance checks available; it improves the good-seed target without claiming to remove advice.

Planned audit: derive the threshold both by the rank of an alternating form and by a direct combinatorial/linear-algebra check, then enumerate small binary vector configurations and edge parities with two independent implementations. Record any failure and retain the open status of uniform sampling.

### Literature search completed (under ten minutes)

The arXiv abstract page gives 28 October 2026 as Mao's latest revision; Section 4, Explicitness, still names polynomial-time good-seed selection as open. The searches found no later uniform-sampler resolution. The search phase ended about five minutes after the first query. This is a bounded negative search, not a proof that no unpublished advance exists.

### Initial algebraic finding

For a nonempty edge set F, let A_F be its adjacency matrix on its h incident vertices, let t=|F|, and let V contain their evaluation vectors. An identically zero edge parity is equivalent to V A_F V^T=0. If rank(A_F)=2s, its radical has dimension h-2s, so a totally isotropic row space has dimension at most h-s. If F has c connected components, rank(A_F)>=2c and t>=h-c; hence rank(V)<=h-s<=h-c<=t. A dependent edge set therefore forces a vector dependence using at most t+1 vectors. This suggests the sharp threshold L-1, rather than floor(L/2).

### Proof completed and first computation

Wrote PROOF.md. The precise result is that a nonzero vector family of finite girth g has edge-uniformity strength exactly g-2 under a uniform independent alternating form, even after vertex permutation and any resampling rate below one. A circuit supplies the obstructing star of g-1 edges. The proof also shows that mixtures over seeds cannot cancel these obstructions: all graph parity expectations are nonnegative conditional-probability averages.

Wrote verify_threshold.py, a standard-library-only program. Exact command:

```powershell
[System.Diagnostics.Process]::GetCurrentProcess().PriorityClass = 'BelowNormal'
$env:OMP_NUM_THREADS='1'
$env:OPENBLAS_NUM_THREADS='1'
$env:MKL_NUM_THREADS='1'
$env:PYTHONDONTWRITEBYTECODE='1'
python -B .\verify_threshold.py
```

First output: PASS; 5,884 vector configurations; runtime 4.097 seconds. Data written to verification.json. Every nonzero subset of F_2^K with 2<=n<=5 was checked for K<=4; nonzero multisets with 2<=n<=5 were also checked for K<=3. The vector and edge girths were computed by direct subset XOR enumeration. Independently, actual alternating matrices were exhaustively evaluated and a shortest-syndrome dynamic program found the smallest parity identically zero across all forms. Both ways agreed with the theorem on every configuration.

All nonempty labeled graphs on 2 through 6 vertices passed the load-bearing rank/component inequality (1, 7, 63, 1023, 32767 graphs). Direct enumeration with vectors (1,2,3,4) in F_2^3 gave the two-edge star Fourier coefficient 48/192=1/4 after permutation; enumerating replacements and fresh bits at resampling rate 1/2 gave 192/3072=1/16. These agree with the independent counts 6 good permutations out of 24 and the survival multiplier (1/2)^2.

Two attempted log patches failed because they targeted proof text that was not in LOG.md; no files changed in those attempts. Local memory index searches for T283/Mao/sampler-counterexample returned no matches. The general recall entry point was inspected but not executed: its default co-use logging and cache writes conflict with the folder-only restriction. No external memory files were changed.

### Independent audit additions

Added a second proof of the crucial rank bound via rank loss in the two products A V^T and V(A V^T), independent of the isotropic-quotient argument. Added closed-form combinatorial checks of every enumeration count, independent counts of the independent-vector subfamilies, and the count 168 of 5-circuits in F_2^4: there are 840 unordered bases, each extends uniquely by its sum, and each 5-circuit is counted five times. Added Windows peak-memory and priority telemetry. A second run is justified by these new audit checks.

### Final audited run and report

Re-ran the exact PowerShell command above. Exit code 0. Output: PASS; 5,884 configurations; 5.425 seconds; peak working set 25,640,960 bytes; peak private commit 17,240,064 bytes; priority class 16384 (BelowNormal); OMP_NUM_THREADS=1. The latest verification.json includes every count and the exact Fourier numerators/denominators. No mathematical check failed.

Wrote REPORT.md with verdict PROVED for the sharp threshold lemma, and explicit statement that T283's uniform polynomial-time sampler remains open. The report records the failed random-seed shortcut, assumptions on the independent alternating form, zero-vector and full-noise exceptions, literature uncertainty, exact command, and next construction target. All created artifacts remain here.
