# Open problem T142: The variance of the longest common subsequence of two random words (Waterman's conjecture)

Statement: Let L_n be the length of a longest common subsequence of two independent uniformly random binary words of length n. Then Var(L_n) is of order n: there are constants 0 < c < C with c n ≤ Var(L_n) ≤ C n for all large n.

Caveat: E L_n / n converges to the Chvátal–Sankoff constant γ_2 ≈ 0.812, whose exact value is unknown; Steele's guess γ_2 = 2/(1 + √2) is ruled out by Lueker's bounds (J. ACM 2009). The upper bound is elementary, so the conjecture is the matching lower bound.

Source: V. Chvátal and D. Sankoff, Longest common subsequences of two random sequences, J. Appl. Probab. 12 (1975); M. S. Waterman, Estimating statistical significance of sequence alignments, Philos. Trans. R. Soc. Lond. B 344 (1994) 383–390

Where it stands (checked by us, Nov 2026): Steele (1986) proved Var(L_n) ≤ n with the Efron–Stein inequality; Chvátal and Sankoff had conjectured a variance of order o(n^{2/3}), which Waterman's simulations contradict. A linear lower bound is proved when one letter has very small probability (Lember–Matzinger, Ann. Probab. 37 (2009)) and in other strongly biased models (Houdré–Ma, High Dimensional Probability VII, Progr. Probab. 71 (2016)). Houdré and Işlak (arXiv:1408.1559) prove a central limit theorem for L_n assuming a lower bound of the right order on the variance, so the conjecture would also give the fluctuations. Houdré and Liu (arXiv:1812.09552) prove the linear order when one word omits a letter of the alphabet. Amsalu, Hauser and Matzinger (arXiv:1211.5489) show that the linear order follows once gamma(S) - gamma(S - epsilon T) > 0 for the scoring function T induced by changing one letter into another, and verify this by simulation at a stated confidence level for binary words with letter probabilities 0.2 and 0.8; for equiprobable letters the difference vanishes by symmetry, so the criterion says nothing there. Open for uniform binary words.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T142 (read it,
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
VERDICT: PARTIAL Var(L_n) <= n/4 and a quadratic route to the missing lower bound

No resolution of the fair binary variance problem was found in the bounded
literature search. The conjectured linear lower bound remains unproved here.

The completed piece is a Fourier decomposition that retains information after
fair-letter symmetry cancels every linear coefficient. `PROOF.md` proves, for
every n, Var(L_n) <= n/4: global complementation removes odd degrees, so the
usual cube energy controls twice the variance. The constant is attained at
n=1. This improves the constant in the upper bound stated in the brief; no
claim is made that the observation is new in the literature.

Writing W_k for the squared Walsh mass at degree k gives the exact identities

    Var(L_n) = W_2 + W_4 + ... + W_{2n},
    W_2 = 2 sum_{i<j} (E[L_n (-1)^(X_i+X_j)])^2
          + sum_{i,j} (E[L_n (-1)^(X_i+Y_j)])^2.

Thus W_2 >= cn would suffice. A simpler sufficient target is

    Var(L_n) >= F_n'(0)^2 / (2(n-1)),  n >= 2,

where F_n(theta) is the expected LCS of independent stationary symmetric
Markov words with probability (1+theta)/2 of repeating the previous letter.
The proof differentiates only a finite polynomial. A uniform estimate
|F_n'(0)| >= delta n would settle the lower bound, but is not proved.

Exhaustive integer data cover every ordered word pair for n=1..12: 22,369,620
pairs per enumeration method. At n=12 the exact values are

| Quantity | Exact value | Decimal |
| --- | --- | --- |
| Var(L_12) | 5658830720631 / 4398046511104 | 1.2866691397 |
| W_2 | 1165932541151 / 1099511627776 | 1.0604094688 |
| W_2 / Var(L_12) | 4663730164604 / 5658830720631 | 0.8241508529 |
| F_12'(0) | -1933745 / 1048576 | -1.8441629410 |
| Markov derivative lower bound | 339942702275 / 2199023255552 | 0.1545880433 |

Reproduce from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 reproduce.py
```

The underlying commands are

```sh
OMP_NUM_THREADS=1 nice -n 15 clang -std=c11 -O3 -Wall -Wextra -Wconversion exact_lcs.c -o exact_lcs
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs bits 12 > results_bits.jsonl 2> run_bits.txt
OMP_NUM_THREADS=1 nice -n 15 ./exact_lcs dp 12 > results_dp.jsonl 2> run_dp.txt
OMP_NUM_THREADS=1 nice -n 15 python3 audit.py > audit.txt
```

The two LCS algorithms agree, and all assertions and exact rational audits
pass. A third method uses literal subsequence-set intersections and direct
Walsh sums through n=5. Histogram moments, centered moments, Parseval, direct
flip edges, odd-degree cancellation, quadratic coefficients, and direct
adjacent covariances provide further checks. `DATA.md` defines every field;
`LOG.md` records commands, outputs, and limitations. Runs are sequential and
single-threaded. The executable verifies inherited nice >=15; on this machine
it was 20. Peak resident memory was below 100 MB.

What failed: symmetry eliminates the individual-letter covariances, and neither
the quadratic mass nor the Markov derivative has been bounded below uniformly
in n. The observed |F_n'(0)|/n decreases from n=4 to n=12. These finite data do
not distinguish a positive limiting slope from zero. There is no fitted
exponent and no asymptotic claim based on the computations. An unsupported
macOS address-space cap was removed before enumeration; allocation sizes are
bounded explicitly by n<=12.

Next work should target a rigorous lower estimate on the adjacent covariances
or another family of quadratic coefficients. The full degree-two coefficient
tables are saved for that purpose. Proving only monotonicity of a limiting
Markov LCS constant would not by itself give the finite-n derivative bound;
that passage needs separate justification.

Primary literature actually opened during the search:

- Jüri Lember and Heinrich Matzinger, *Standard deviation of the longest common
  subsequence*, [arXiv:0907.5137](https://arxiv.org/abs/0907.5137), Ann. Probab.
  37 (2009), 1192–1235: sufficiently biased Bernoulli words.
- Christian Houdré and Ümit Işlak, *A Central Limit Theorem for the Length of
  the Longest Common Subsequences in Random Words*,
  [arXiv:1408.1559v6](https://arxiv.org/abs/1408.1559v6), EJP 28 (2023), paper 3:
  a CLT conditional on a variance lower bound.
- Saba Amsalu, Raphael Hauser and Heinrich Matzinger, *A Monte Carlo Approach
  to the Fluctuation Problem in Optimal Alignments of Random Strings*,
  [arXiv:1211.5489](https://arxiv.org/abs/1211.5489): its abstract explicitly
  excludes a resolution of the equiprobable binary case by that method.
- Christian Houdré and Qingqing Liu, *On the Variance of the Length of the
  Longest Common Subsequences in Random Words With an Omitted Letter*,
  [arXiv:1812.09552](https://arxiv.org/abs/1812.09552): different alphabets for
  the two words.

Task: “push this problem forward by one checkable piece” — 14 November 2026,
approximately 22:02 Asia/Tbilisi.
