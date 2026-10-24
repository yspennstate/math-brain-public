Model requested: GPT-6 maximum. Actual runtime: GPT-5.6 Sol; reasoning level UNVERIFIED, so GPT-6/maximum is not claimed.

# R11 / I0054 idea before code — shuffled microblock paintboxes

Methods for this run: **#7 TAKE THE LIMIT, #22 READ THE FAILURES, #28 REPLACE FOR ALL WITH FOR TYPICAL.** These differ from the preceding #6/#12/#29 triple.

The preceding C078 shuffled sticky-Markov construction shows that a strong local dependence field can still give CTCS when a random ambient permutation makes every fixed visible set typically sample locations farther apart than the correlation length. The next route is to remove the Markov chain entirely and make the dependence combinatorial and perfectly rigid inside deterministic microblocks.

For each N choose a deterministic partition of the ambient positions [N] into consecutive blocks of sizes s_{N,1},...,s_{N,r_N}. Let b_N=max_r s_{N,r}. At every harmonic-grid proposal x_j=j/N, draw a fresh uniform permutation sigma of [N], then give every microblock an independent Bernoulli(x_j) color and color label ell by the color of the microblock containing sigma^{-1}(ell). Use the usual harmonic proposal clock lambda_{N,j}=N/[2j(N-j)]. Every proposal redraws both sigma and all microblock colors.

The key exact collision parameter is

    kappa_N = [sum_r s_{N,r}(s_{N,r}-1)]/[N(N-1)].

For a fixed visible set of m labels, the probability that any two visible labels land in the same microblock is at most C(m,2) kappa_N. Conditional on no collision, their colors are exactly iid Bernoulli(x_j). For any specified nontrivial unordered split A|B, both the iid split probability and the microblock split probability are bounded by 2 x_j(1-x_j); hence the singular harmonic weight cancels rather than introducing H_N. This should give the uniform generator estimate

    |q_N^micro(A|B)-q_N^iid(A|B)| <= C(m,2) kappa_N (N-1)/N.

For two visible labels the formula is exact:

    q_N^micro(1|1)=((N-1)/N)(1-kappa_N).

Therefore kappa_N -> 0 is both necessary and sufficient for convergence of every fixed restriction generator to CTCS. For deterministic partitions, kappa_N -> 0 is equivalent to b_N/N -> 0, since

    (b_N/N)^2 <= sum_r s_{N,r}^2/N^2 <= b_N/N,

up to the negligible 1/N corrections connecting sum s_r^2 and kappa_N.

Concrete candidate C079: b_N=max(1,floor(sqrt(N))) with consecutive blocks of size b_N except the last. This has b_N/N -> 0 but has perfect within-block dependence at every proposal.

At N=4, b_4=2, so the random permutation induces a uniform perfect matching into two size-2 microblocks. A nontrivial split is necessarily 2|2. For each specified balanced split, exact rate should be 1/4; every specified 1|3 rate is 0. Thus the root topology is balanced with probability 1, versus CTCS(4) balanced probability 3/11. This is invariant under leaf relabeling and positive global time rescaling, so it is a finite non-equivalence witness.

If the exact checks confirm these formulas, this yields a genuinely different class C079 and a general theorem U059 (sharp shuffled-microblock compiler). The external/campaign status must remain PARTIAL until the canonical admission and two independent audits exist.