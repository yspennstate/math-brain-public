VERDICT: PASS (correct and complete)

Audit date: 2026-10-12. This verdict applies to the claimant's explicitly limited counterexample to the literal printed formula. It does not certify a solution of the intended singular-part problem. No failing mathematical step or necessary repair was found in the counterexample.

## Exact claim and match to the stated question

STATUS.md and CLAIMS.jsonl define SOLVED as disproving the printed assertion, not proving a critical singularity exponent. ATTEMPT.md lines 11–19 claim that, for independent site percolation on the full triangular lattice, with reciprocal cluster size defined as zero for a closed origin or an infinite open cluster,

κ(p) ≥ p(1−p)^6,

so liminf as p approaches 1/2 from either side is at least 1/128. Consequently κ(p) cannot equal, be asymptotic to a positive constant times, or be bounded above by a bounded multiple of |p−1/2|^(4/3+o(1)). This is a counterexample in precisely the stated model, uniformly for all nearby parameters, rather than an observation only at the critical point.

I independently downloaded https://arxiv.org/pdf/1107.0158 (HTTP 200, 50 pages). PDF page 44, Section 5, Question 1 indeed prints κ(p)=E_p(|C|^(−1)) and |1/2−p|^(2+α+o(1)), α=−2/3. The immediately preceding heading specifies triangular-lattice site percolation. There is no Taylor subtraction in this question. Thus the counterexample answers the literal assertion supplied for this audit by proving it false. Reading “behaves like” as shorthand for an unstated singular component changes the mathematical claim; under that interpretation this result would not solve the problem.

## Independent proof checks

1. **ATTEMPT.md lines 11–15: convention, isolation, and lower bound.** The triangular lattice has six distinct nearest neighbors. The cylinder event consisting of one occupied origin and six vacant neighbors has probability p(1−p)^6 by independence. On this event no occupied path can take its first step, irrespective of the configuration outside these seven sites. The open cluster therefore has size exactly one, its reciprocal is one, and all other contributions are nonnegative. The lower bound follows without any finite-volume approximation or assumption about infinite clusters. Conditioning on an occupied origin gives the claimed alternative bound (1−p)^6 for p>0; using clusters of the origin's color also retains the unconditional singleton lower bound.

2. **Lines 17–19: limits and quantifiers.** On [1/4,3/4] each of the seven factors is at least 1/4, giving 1/16384. The sharper bound tends to (1/2)^7=1/128. For ε(p)→0, 4/3+ε(p) is eventually at least 2/3, so for 0<r<1 the proposed power is at most r^(2/3)→0. The positive lower bound contradicts it on both sides. Changing only the definition at p=1/2 cannot remove this contradiction.

3. **Lines 23–29: continuity.** For a finite connected set S containing the origin, C(0)=S is equivalent to occupation of S and vacancy of its external vertex boundary. This gives exactly p^|S|(1−p)^|∂S|. A connected rooted set of size at most M lies in the finite radius-(M−1) graph ball, so the displayed sum has finitely many terms and is a polynomial. The omitted finite-cluster reciprocals are at most 1/(M+1); empty and infinite clusters contribute zero. This proves the claimed uniform error, including p=0 and p=1, and hence continuity. The explicit epsilon argument also checks. This proof establishes continuity, not differentiability or the singular exponent.

4. **Lines 38–46: conditional calculus lemma.** Fix η in (0,2/3), and restrict h to the sufficiently small positive range where the assumed derivative bound holds. The exponent b=−1/3−η exceeds −1, making f''' absolutely integrable near zero. Applying the fundamental theorem on [δ,u] and using continuity of f'' at zero justifies δ→0. Two further integrations, with absolute integrability justifying Fubini, give the remainder (1/2)∫_0^h(h−t)^2 f'''(t)dt. Expansion of the square gives coefficient (1/2)[1/(b+1)−2/(b+2)+1/(b+3)] = 1/[(b+1)(b+2)(b+3)]. Its denominator is positive throughout the stated η range. The upper bound and its exponent 8/3−η are correct. Reflecting the parameter handles the left side, conditional on the same hypotheses there.

5. **Lines 56–58: computational claims.** I wrote and ran a separate script rather than trusting the claimant's code. Exact rational enumeration of all 128 seven-site states at p=0, 1/4, 49/100, 1/2, 51/100, 3/4, 1 reproduces normalization and the singleton probability. Independent rooted connected-set generation with the triangular adjacency ±(1,0), ±(0,1), ±(1,1) gives counts 1, 6, 33, 176, 930 and respective critical contributions 1/128, 3/1024, 13/8192, 65/65536, 357/524288. The sum is 7341/524288. Generation is exhaustive by removing a non-root leaf of a spanning tree to obtain a connected predecessor. SymPy independently simplifies the integral coefficient difference to exactly zero. I checked the rational exponent and singleton arithmetic directly; I did not rerun Lean and do not certify the reported Lean execution or imports. Formal verification is unnecessary for the independently checked elementary argument.

## Literature checks and scope issues

I independently downloaded Zhang's https://arxiv.org/pdf/math/0301160 (HTTP 200, 38 pages) and Mertens–Jensen–Ziff's https://arxiv.org/pdf/1602.00644 (HTTP 200, 8 pages).

Zhang's theorem on PDF page 5 states an upper bound |κ'''(p)|≤|p−p_c|^(−1/3+o(1)) and a lower bound along an existential sequence ε_n↓0. It is a theorem about a third derivative, not the vanishing of κ itself or a full all-small-h Taylor remainder law. The page's Remark 2 also states inability to prove the lower bound for an arbitrary sequence. I verified these statements, not the complete 38-page proof, and the literal counterexample does not depend on that paper.

Mertens–Jensen–Ziff equation (2), PDF page 2, separates an analytic background A_0+B_0(p−p_c)+C_0(p−p_c)^2 from a singular term A_±|p−p_c|^(2−α), with α=−2/3. Its abstract describes series analysis, simulations and exact enumeration. It does not supply a rigorous theorem establishing the complete corrected law with the required quantifiers.

Fresh arXiv API searches returned HTTP 200: a 40-result recent search for percolation with free energy/cluster number/cluster density, and a 30-result targeted search for percolation with singularity/number of clusters. I screened the returned titles and abstracts. The targeted search recovered Zhang, Mertens–Jensen–Ziff, and Hongler–Smirnov's critical rectangle observable; the latter concerns boundary separation at criticality rather than near-critical mean clusters per site. The recent search also returned fixed-width bond-percolation strips and nonamenable-graph differentiability, which do not settle this model and question. OpenAlex returned HTTP 429 for the fresh search. No exhaustive or current-openness conclusion follows from this bounded search.

The material scope limitations are already acknowledged in ATTEMPT.md:

- **Lines 33, 48–52, 68–74:** the full background-subtracted 8/3 law remains unproved here. The derivative lemma yields only an upper bound conditional on regularity and external estimates. A subsequential lower bound on an absolute third derivative supplies neither uniform lower control for a Taylor remainder nor control of cancellation. The conjecture in CLAIMS.jsonl must remain a conjecture.
- **Lines 58 and 66:** the reported Lean verification checks algebra only; it must not be described as formal verification of percolation or the continuity theorem. The text presently makes that distinction.
- **Lines 69–70:** this is neither an exhaustive literature-status determination nor a novelty claim. I have not independently verified the historical repository comparisons, and they are not needed for the mathematical conclusion.

These are boundaries of the result, not gaps invalidating the stated counterexample. An unqualified claim that the intended singularity problem has been solved would fail this audit; the actual STATUS.md explicitly excludes it.

## Evidence retained

All audit writes are inside this folder. independent_checks.py and independent_checks.json record the independent exact calculations. source.pdf/source.txt, zhang.pdf/zhang.txt and mertens.pdf/mertens.txt record fresh primary-source downloads and extraction. literature_checks.json records URLs, statuses, extracts and search results; arxiv_targeted.response and arxiv_targeted.json retain the targeted response. The claimant's files were read only.

What is proved: the literal printed positive-power law for κ itself is false; κ is continuous with a positive critical value; the stated conditional calculus lemma is valid. What is not proved: the intended background-subtracted singularity law or a complete contemporary literature classification.
