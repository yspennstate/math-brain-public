VERDICT: PASS

Independent audit, 2026-10-11. The claimed counterexample is correct and complete for the general question. No mathematical defect or required fix was found. References below are to the claimant's ATTEMPT.md, numbered as read during this audit.

## Claim and scope

The claim is that on the free group F_32, the minimum number L of unmatched letters in a noncrossing inverse-letter matching defines a conjugation-invariant norm. Consequently d(g,h)=L(g^-1 h) is a genuine bi-invariant metric. For the symmetric probability measure uniform on the 64 generators and inverse generators, its first moment is one and its expected drift exists and lies in [1/4,1]. This disproves the assertion that every symmetric measured group with an integrable bi-invariant (semi-)metric has zero drift.

I independently fetched https://arxiv.org/pdf/1406.0763 and extracted its text. PDF page 25, Problem 4, asks exactly the general question quoted in ATTEMPT.md line 3. PDF page 1 defines a measured group to be countable with semigroup-generating measure support, symmetry by invariance under inversion, and drift by the limit of expected distance divided by n. Neither passage requires properness, finite metric balls, or a special group. F_32 is countable; the specified support generates it as a semigroup. A single counterexample therefore answers the general question as stated. The source's separate suggestion concerning stable commutator length on [F_2,F_2] is a test case, not an additional hypothesis.

The counterexample does not resolve that stable commutator length test case. It also does not determine the exact drift, prove novelty, or certify an earlier published solution. The claimant explicitly observes these limitations at lines 28 and 55.

## Step-by-step mathematical checks

1. **Definition and free-reduction invariance, lines 7–9 and 32.** I checked both inequalities under insertion/deletion of adjacent inverse letters. Inserting the adjacent pair extends any old matching without changing its cost. For deletion: an internal pair is removed; two unmatched endpoints reduce the cost by two; one external partner becomes unmatched with net unchanged cost; two external partners are reconnected with net unchanged cost. Their letters are inverse because the deleted letters are inverse. In the last case noncrossing permits only disjoint old intervals on opposite sides, or nested old intervals on the same side, together with reflections. A pair crossing the new interval would necessarily cross an old interval. Adjacency is essential here, and the proof uses it correctly. Thus the function descends to free-group elements. I found no missing endpoint configuration in line 32.

2. **Subadditivity, inversion, and conjugation, line 11.** Concatenated matchings are noncrossing and their costs add. Word reversal and letter inversion give a cost-preserving bijection of matchings. Pairing the entire conjugating word with its inverse creates nested outer arcs that surround every matching of the middle word. This proves L(ugu^-1)<=L(g). Applying the same inequality with u^-1 gives the reverse inequality because free-reduction invariance has already been established. These arguments hold for arbitrary words and conjugators.

3. **Nondegeneracy and metric axioms, line 13.** In a perfect matching, every endpoint inside an arc must have its partner inside the same arc. A shortest arc is therefore adjacent, allowing induction by free cancellation. Hence L(g)=0 implies g=e; the converse follows from reduction invariance. Inversion yields symmetry of d; L(g^-1 k)<=L(g^-1 h)+L(h^-1 k) yields its triangle inequality. Left translations cancel in g^-1 h, while right translations conjugate that element. Thus d is indeed a genuine bi-invariant metric. Every supported increment has norm one, so integrability and the stated first moment follow exactly.

4. **Probability model and counting, lines 17–19.** The proof uses the unreduced word of independent increments. For a fixed positional matching with m disjoint pairs, the inverse-letter events involve disjoint random variables and have joint probability 64^-m. No independence between different matching events is needed. Choosing k unmatched positions and contracting them leaves a perfect noncrossing matching on n-k=2m ordered positions, so the count is binom(n,k) C_m. Unmatched positions inside arcs are allowed and included. Noncrossing makes the parenthesis encoding injective, giving C_m<=4^m. These counts and probabilities are correct.

5. **Union bound and exponent, lines 21–26.** The event L(X_n)<=n/4 supplies at least one matching with k<=floor(n/4) unmatched positions and k congruent to n modulo 2. For each permitted k, m=(n-k)/2>=3n/8. Therefore the claimed sum is at most 2^n 16^(-3n/8)=2^(-n/2). The sum must retain the parity convention stated at line 21; I read lines 23–24 with that convention. Integer rounding only strengthens the estimate. Nonnegativity then gives E[L(X_n)]/n >= (1/4)(1-2^(-n/2)) for n>=1. This is a valid lower bound even though the complementary event has a strict inequality.

6. **Existence and positivity of drift, line 26.** The expected norms a_n are finite, bounded by n, and satisfy a_(n+m)<=a_n+a_m by splitting the product into increment blocks and using subadditivity. Fekete's lemma supplies the expected-distance limit; the preceding lower bounds force it to be at least 1/4, and L(X_n)<=n supplies the upper bound one. This is precisely the source's definition, so no almost-sure theorem is needed to answer the question. The additional Kingman statement is also valid: the block-norm process is stationary and subadditive over the ergodic iid shift, with finite integrable bounds. Its deterministic limit is the same expected drift. The exponential tail is summable, so the separately stated Borel–Cantelli conclusion is valid as well.

## Independent exact computations

I wrote and ran independent_checks.py in this audit folder; all assertions passed. Its results are saved in independent_checks.json. I did not execute or copy the claimant's check.py.

- Enumerated all positional noncrossing partial matchings at lengths 2 through 12 and checked every adjacent-position deletion surgery: 258,372 instances, including 64,152 two-external-partner configurations. Each resulting matching remained noncrossing, used distinct endpoints, and had cost no larger than before deletion. The four case counts are recorded in the JSON.
- Verified the exact binom(n,k) C_((n-k)/2) positional counts against the enumerations for every k at those lengths.
- Computed the matching norm independently by interval recursion for all 87,381 words over two generators and inverses at lengths zero through eight. Reduction invariance, inversion symmetry, and nondegeneracy all passed.
- Used a separate exhaustive deletion oracle on 5,461 words through length six: examine every retained subsequence and freely reduce it, minimizing the deleted-letter count when the subsequence is trivial. Its answers agreed with the matching recursion. This provides a check independent of the recursion itself.
- Checked subadditivity and conjugation invariance on all 7,225 pairs of words of lengths at most three.
- For every n from 1 through 200, calculated both the Catalan union-bound sum and the coarser sum using exact rational arithmetic, with the parity restriction. Verified the first is at most the second and the square of the second is at most 2^-n. No floating-point approximation was used in these assertions.

These finite computations support the arbitrary-length argument; they do not substitute for it. The computational claims at lines 43–45 are consistent with my independently obtained counts. I read ExponentCheck.lean and lean_check.txt read-only. The two displayed arithmetic lemmas at line 47 follow directly from 4k<=k+2m, hence 3k<=2m and 3n=3k+6m<=8m. I did not rerun Lean or independently certify the historical execution log. Full formalization is neither claimed nor necessary for the proof audited here.

## Bounded independent literature search

I used Python HTTP requests only, with URLs and outcomes recorded in research_log.json. The source PDF and the cited background paper were fetched anew and saved in this folder. No built-in web search was used.

The arXiv API searches were:

- (all:"cancellation norm" OR all:"cancelation norm" OR all:"spelling length") AND (all:"random" OR all:"drift"), capped at 30: one unrelated precipitation-model result; its abstract does not address this problem.
- (all:"bi-invariant" OR all:"conjugation-invariant") AND all:"drift", capped at 30: no entries.

OpenAlex searches for "cancellation norm random walk drift" and "Five remarks about random walks on groups" both returned HTTP 429. Thus this search cannot support an exhaustive literature or novelty conclusion.

I inspected Brandenbursky, Gal, Kędra, and Marcinkowski, *The cancelation norm and the geometry of biinvariant word metrics*, https://arxiv.org/pdf/1310.2921, v3 (2 April 2023). Proposition 2.A on PDF page 7 identifies cancellation norm with the bi-invariant word norm; Theorem 1.C on PDF page 3 gives an algorithm on free groups. The paper contains no occurrences of "random" or "drift" in its extracted text and I found no theorem resolving this random-walk question there. Its incomplete older proof of Proposition 2.E and Section 6 erratum are explicitly flagged. The claimant's free-group reduction argument is independent of that incomplete proof, and I verified it directly above. This paper is background, not a basis for a SOLVED_IN_LITERATURE verdict.

## Issues and final assessment

No proof issue requiring a fix was found. Lines 3 and 28 correctly state the scope: a finite-first-moment bi-invariant metric with strictly positive drift disproves the universal zero-drift assertion. The bounded, partly rate-limited literature search leaves publication priority unverified, which the claimant does not assert. The stable commutator length example remains unresolved by this work. Neither limitation weakens the proved counterexample to Problem 4 as stated.
