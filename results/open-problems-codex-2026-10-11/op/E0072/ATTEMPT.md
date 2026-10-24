# E0072: cancellation norm counterexample

2026-10-11. Exact source statement, verified in Michael Björklund, Five remarks about random walks on groups, arXiv:1406.0763v2 (7 July 2014), Problem 4, PDF page 25: "Let (G, µ) be a symmetric measured group and suppose there exists a bi-invariant (conjugation-invariant) and µ-integrable (semi-)metric d on G. Is ℓ_d(µ) = 0?" Page 1 defines a measured group to be countable with a probability measure whose support generates the group as a semigroup, symmetry as µ(g)=µ(g^-1), and drift as lim_n (1/n) integral d(g,e) dµ^{*n}(g). No properness or finite-ball condition is imposed. The counterexample below meets precisely these hypotheses.

## Construction and complete mathematical proof

Let G be the free group on 32 generators. Let A be its 64 letters (generators and inverses), and let mu be uniform on A. For a word w of length n, a matching is a collection of disjoint pairs of positions (i,j), i<j, with inverse letters at paired positions. Require noncrossing: no two pairs have endpoints i<k<j<l. Define L(w) as the minimum number of unpaired positions over these matchings.

First L is invariant under free reduction. Insert an adjacent inverse pair at positions i,i+1. Any matching on the shorter word extends by pairing these two positions; hence insertion cannot increase L. Conversely take any matching on the longer word. If the two positions are paired together, remove their pair. If both are unpaired, remove them, decreasing the cost by two. If exactly one is paired to an external position, remove its pair and leave that external position unpaired: the cost is unchanged, since the removed inverse pair previously contained one unpaired position. If both are paired externally, remove their two pairs and pair their former partners together. Those partners carry inverse letters. This surgery is noncrossing: if the partners are on opposite sides of the adjacent positions, the old pairs occupy disjoint intervals and the new pair surrounds their intervening region; an existing pair crossing the new interval would have crossed one of the old intervals. If both partners are on the same side, the old pairs are nested, and the new interval lies between their outer endpoints; again any crossing of the new interval would cross one old pair. The mirrored order gives the same argument. Thus the cost never increases upon deletion. The two inequalities prove invariance. Since free reduction gives unique representatives in a free group, L defines a function on G.

Concatenating two matchings proves L(gh)<=L(g)+L(h). Reversing a word and inverting each letter preserves matchings, so L(g^-1)=L(g). For words u,w, pair each position of u with its mirror inverse position in u^-1, around a matching of w. This gives L(uwu^-1)<=L(w). Apply this inequality to u^-1 and uwu^-1 for the reverse inequality: L(ugu^-1)=L(g).

If a word has a perfect noncrossing inverse matching, it represents the identity. Indeed choose a matched pair with minimal interval; every position strictly inside it must be matched inside it (otherwise a crossing occurs), so minimality implies this pair is adjacent. Delete that inverse pair and induct. Conversely an identity word freely reduces to empty, whose L is zero; reduction invariance gives L=0. Thus d(g,h)=L(g^-1 h) is a genuine metric: positivity follows from the preceding argument, symmetry from inverse invariance, triangle inequality from subadditivity, left invariance directly, and right invariance from conjugation invariance. Each letter has L=1, so its mu first moment is exactly one. The measure is symmetric, finitely supported, and generates G.

## Positive drift

Let W_n be the raw word of n independent uniform letters; X_n its element of G. A matching leaving k positions unpaired has m=(n-k)/2 pairs. For a fixed such positional matching, the probability that all its pairs carry inverse letters is 64^-m: pairs use disjoint independent letters, each pair matching with probability 1/64. There are binom(n,k) C_m such noncrossing positional matchings, where C_m is the Catalan number. To see the count, choose the unpaired positions, then use the order-preserving bijection of the remaining positions with 2m positions; perfect noncrossing matchings of these are counted by C_m. The standard first-pair decomposition gives the Catalan recursion and C_m=binom(2m,m)/(m+1)<=4^m.

For completeness, the only counting estimate needed, C_m<=4^m, also follows directly by encoding every matched left endpoint as an opening parenthesis and every right endpoint as a closing parenthesis. Noncrossing ensures that every closing endpoint pairs with the most recent unpaired opening endpoint, so the parenthesis string determines the matching. There are at most 2^{2m}=4^m binary strings. This avoids needing the closed Catalan formula.

Union bound, including only k with correct parity, gives

P(L(X_n)<=n/4) <= sum_{0<=k<=n/4} binom(n,k) (4/64)^((n-k)/2)
 <= 2^n 16^(-3n/8) = 2^(-n/2).

Here n-k>=3n/4; extending the sum of binomial coefficients to all k gives 2^n. Therefore E L(X_n)/n >= (1/4)(1-2^(-n/2)). Expectations are subadditive by independent increments and the norm triangle inequality, so Fekete's lemma proves that delta=lim E L(X_n)/n exists and delta>=1/4. Also delta<=1. If drift is defined almost surely, Kingman's subadditive ergodic theorem applied to L of increment blocks gives the deterministic same limit; bounded increments supply integrability. Independently, summability of the displayed probability and Borel--Cantelli give liminf L(X_n)/n>=1/4 almost surely.

Thus the source's exact mathematical question has a negative answer on F_32. This is a complete counterexample proof. It does not answer the proposed stable-commutator-length test case, and it does not establish literature novelty.

## Hostile-referee checks

1. Crucial point: invariance under deletion of an adjacent inverse pair; all four matching configurations are explicitly treated above. Additional endpoint verification for the two-external-partner case: after reflection if necessary, either p<i<j<q with old pairs (p,i),(j,q), or p<q<i<j with old pairs (p,j),(q,i). In the first configuration, every remaining position inside (p,q) lies inside one old interval, because i,j are adjacent; a pair crossing (p,q) would cross that old interval. In the second configuration, for a position r in (p,q), a partner s<p or s>j crosses (p,j), while a partner q<s<i crosses (q,i); there are no positions between i,j, and i,j,p,q are already occupied. Thus no existing pair crosses the replacement (p,q). The mirrored configuration is identical. This closes the planar surgery proof without relying on a diagram.
2. Conjugation is handled by nested outer pairs, so no bound on the conjugating word is used.
3. The metric is nondegenerate, not merely a semimetric, and the first moment is finite.
4. The random word is not conditioned to be reduced. Independence in the probability estimate therefore holds exactly; free reduction invariance connects it to X_n.
5. Matchings can overlap as events; the argument uses a union bound and never assumes event independence. Independence is used only for distinct pairs within one positional matching.
6. Catalan counting permits unpaired positions inside arcs; selecting the unpaired set correctly includes these matchings.
7. No interchange of an unbounded limit and expectation is used. Fekete suffices for expected drift.
8. Exact source hypotheses were verified from PDF pages 1 and 25. Later-literature searches are documented separately, with API rate limits recorded. No claim of SOLVED_IN_LITERATURE or novelty is made.

## Executed finite checks and formalization scope

check.py computes L exactly by interval dynamic programming: either leave the first letter unmatched (cost 1), or pair it with each later inverse letter and add the optimal costs of the interior and exterior subwords. Noncrossing is exactly what makes those two subproblems independent. This recurrence considers every legal first-letter configuration, and induction on word length proves its correctness.

Executed output in finite_checks.json: 87,381 words over an alphabet of four letters, lengths zero through eight, checked for reduction invariance, nondegeneracy, and inverse symmetry; 7,225 pairs of words of lengths at most three checked for subadditivity and conjugation invariance. All assertions passed, runtime 0.731 seconds. The cache holds at most 100,000 entries. These checks support the full arbitrary-word proof and are not substituted for it.

ExponentCheck.lean formalizes the arithmetic implication k+2m=n and 4k<=n imply 3n<=8m used in the squared exponential probability estimate. It uses omega, with no sorry or native_decide. Executed from ~/lean_verify with command `lake env lean ~/brain_workers/TRIO_1011/op/E0072/ExponentCheck.lean`; after a 136-second shared-slot wait, it completed with exit code 0 and no Lean diagnostics. The arithmetic lemmas are kernel-checked. Only this arithmetic step is formalized; the metric and probability proof are written mathematics, not a full Lean development. Execution evidence is recorded in lean_check.txt.

## Research brain and previous work

The prescribed topic/mistakes recall and the named cancelation-norm math-store recall returned mostly off-topic cards, not a resolution. A follow-up author query likewise returned off-topic cards. Intake probability_1000_intake_E_20260908 records E0072-A001 (2026-09-08) as attempted_unsolved and discusses a quasimorphism/scl approach. Its assertion that symmetry and subadditivity imply monotonicity of expected norm was not used and is not established there. Its assertion that a general conjugation-invariant norm is a quasimorphism-type object was likewise not used. The present construction avoids any exchange of a supremum with a drift limit. Read-only git ls-tree of origin/master in math-open-problems found no path containing E0072 or five_remarks; no working tree was touched.

## Remaining gap

None for the general question: the verified source hypotheses are met and the drift is strictly positive. The source's suggested scl case remains untouched. Literature coverage is bounded and partly rate-limited, so novelty is not asserted.
