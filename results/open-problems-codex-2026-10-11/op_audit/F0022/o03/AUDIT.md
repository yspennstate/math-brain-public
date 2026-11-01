VERDICT: PASS (correct and complete)

Independent audit of F0022, 2026-10-12. This verdict accepts the explicitly scoped counterexample to the literal printed formula. It does not certify a solution of the intended singular-part problem.

Claim and match to the question

I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md without modifying the claimant's directory. The main claim (ATTEMPT.md lines 11–19; CLAIMS.jsonl entry 1) is that independent triangular-lattice site percolation satisfies κ(p) ≥ p(1−p)^6, so κ(p) cannot behave as |p−1/2|^{4/3+o(1)} on either side of criticality. The claimant expressly limits SOLVED to a counterexample to the printed statement and excludes the Taylor-subtracted singular remainder (lines 33, 48–52, 74). This refutes the supplied statement rather than proving its requested positive assertion; the audit instructions permit checking counterexamples.

I independently downloaded https://arxiv.org/pdf/1107.0158 and extracted PDF page 44. It specifies site percolation on the triangular lattice and prints κ(p)=E_p(|C|^{-1}), the power 2+α+o(1), and α=−2/3. Question 1 states no subtraction. Thus the printed power is 4/3, confirming ATTEMPT.md lines 3–7. Interpreting it as a statement about a singular contribution changes the mathematical assertion. The claimant does not claim to settle that interpretation.

Proof checked independently

1. Convention, lines 11 and 19. Assigning zero to empty and infinite occupied clusters makes X a measurable, nonnegative variable bounded by one and agrees with the usual occupied-cluster count per site. The source does not spell out the empty-cluster convention. This does not rescue its literal formula: conditioning on occupation gives the lower bound (1−p)^6, and the origin's color cluster also retains the isolated-open contribution. The convention is explicit rather than silently exploited.

2. Local event, lines 13–15. The triangular lattice has six distinct neighbors. Requiring the origin open and all six neighbors closed fixes seven independent Bernoulli variables, with probability p(1−p)^6. No exterior configuration can connect the origin to another occupied vertex. On this event X=1; elsewhere X≥0. The lower bound therefore holds for every p∈[0,1] in the infinite lattice. No arm estimate or finite-volume approximation is needed.

3. Limit and quantifiers, line 17. On [1/4,3/4], all seven factors are at least 1/4, giving 1/16384. More sharply, p(1−p)^6 tends to 1/128 from either side of 1/2, yielding liminf κ(p)≥1/128. If ε(p)→0, eventually 4/3+ε(p)≥2/3. For 0<|p−1/2|<1 the proposed power is then at most |p−1/2|^{2/3}, tending to zero. Bounded prefactors do not affect this contradiction. The argument concerns the approach to criticality, not merely the value at criticality, and has the required two-sided quantifiers.

4. Continuity, lines 23–29. For a connected finite rooted set S, C(0)=S requires S open and its external vertex boundary closed, giving the displayed product probability. Every rooted connected set of size at most M lies in the finite graph-distance ball of radius M−1. There are therefore finitely many terms and κ_M is a polynomial. On every configuration the discarded reciprocal is at most 1/(M+1); empty and infinite clusters contribute zero. The expectation estimate is uniform in p, including endpoints. The epsilon proof correctly uses two approximation errors and one polynomial-continuity error. Hence κ is continuous on [0,1] and κ(p)→κ(1/2)>0. This proof is complete and stronger than needed for the counterexample.

5. Conditional calculus lemma, lines 38–46. I independently rederived the integral Taylor remainder. For 0<η<2/3, b=−1/3−η>−1, so the bound on the third derivative is absolutely integrable near zero. The fundamental theorem away from zero, continuity of f'' at zero, and two integrations give R(h)=(1/2)∫_0^h(h−t)^2 f'''(t)dt for sufficiently small positive h. Absolute integrability justifies the integrations. The coefficient is exactly 1/[(b+1)(b+2)(b+3)], so the asserted upper bound follows. Application to κ requires the regularity and derivative hypotheses; lines 48–52 explicitly leave those external inputs and the lower remainder bound outside the proof. This lemma establishes no unconditional remainder law for κ.

Exact computational checks

I independently enumerated all 128 assignments of seven Bernoulli variables at p=0, 1/4, 49/100, 1/2, 51/100, 3/4, 1 using Python Fraction arithmetic. The probabilities sum to one, and the isolated-open assignment has exactly probability p(1−p)^6. At criticality it is exactly 1/128.

I separately generated all rooted connected triangular-lattice sets through size five by adjoining boundary vertices and deduplicating. The spanning-tree non-root leaf-removal argument in line 57 proves completeness of this construction. Counts were 1, 6, 33, 176, 930. Exact contributions at p=1/2 were 1/128, 3/1024, 13/8192, 65/65536, 357/524288, summing to 7341/524288, agreeing with line 57. SymPy also verified that the difference between the expanded integral coefficient and the asserted rational coefficient is identically zero. Results are saved in independent_checks.json in this audit folder.

I read Singleton.lean and lean_check.txt, referenced at line 58. The file contains the three asserted rational-arithmetic lemmas using norm_num, with no sorry or native_decide. Their arithmetic was independently checked here. I did not rerun Lean or independently authenticate the historical execution log. The probability proof does not depend on that execution claim.

Literature search and scope issues

I used direct Python HTTP requests for two arXiv API searches, with 30 and 40 returned entries, screening titles and abstracts. I independently downloaded the source, Zhang's manuscript, and Mertens–Jensen–Ziff. OpenAlex returned HTTP 429. Search terms, limits, and failures are recorded in search_log.txt; raw arXiv responses, downloaded PDFs, and extracted pages are retained locally. This bounded search does not certify the modern openness of a corrected formulation.

Zhang, arXiv:math/0301160v6, PDF page 5, states an upper bound |κ'''(p)|≤|p−p_c|^{−1/3+o(1)} and an existential sequence of lower bounds, as quoted in LITERATURE.md. Pages 2–3 identify κ with the reciprocal occupied-cluster expectation. A subsequential lower bound on |κ'''| supplies neither a uniform lower bound on the Taylor remainder nor cancellation control under integration. ATTEMPT.md lines 52 and 69 correctly retain this gap. I checked the theorem statement and relevant definitions, not Zhang's full proof. Remark 2 also contains the quoted inability to prove the lower bound for any sequence; this does not strengthen the theorem to a uniform lower bound.

Mertens–Jensen–Ziff, arXiv:1602.00644v2, PDF page 2, equation (2), separates a constant, linear, and quadratic background from A_±|p−p_c|^{2−α}, with α=−2/3. This supports the distinction in ATTEMPT.md lines 33 and 68 and the conventional 8/3 singular power. Its series, simulation, and enumeration work is not used as a rigorous proof of the corrected remainder law. The bounded search located no theorem settling that exact law. The literal lower bound has no novelty claim. The claimant's report of an earlier repository observation was not needed or independently investigated here.

Issues found and disposition

No failed mathematical step or required repair was found in the literal counterexample, continuity proof, or conditional lemma. The material scope limitation is at ATTEMPT.md lines 33, 48–52, 68, and 74: this work refutes an un-subtracted vanishing law and leaves the intended nonanalytic remainder law unresolved. Calling it a solution of the intended critical singularity problem would be unjustified. The claimant already states this limitation in STATUS.md and ATTEMPT.md, so it is not a gap in the actual accepted claim.

What is proved: the printed asymptotic for κ itself is false; κ is continuous and strictly positive at criticality under the stated convention; the conditional calculus estimate and the finite exact computations hold. What is not proved: the full two-sided logarithmic 8/3 law for the Taylor-subtracted remainder or an exhaustive current literature-status assertion. That remainder law remains a conjecture in this submission.
