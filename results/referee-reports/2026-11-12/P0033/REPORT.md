# Referee report on PAPER.tex

**Overall verdict: SOUND.** I found no mathematical gap or counterexample in the supplied construction, including its two-component ergodic decomposition. This verdict concerns the proof in this source. Exact source attributions, historical priority, and the author's unavailable computational artifacts remain unverified.

The audit used no browsing, outside agents, author programs, or external writes. PAPER.tex was left unchanged. Locations below are physical source lines. Detailed verdicts were recorded in the requested order in [LOG.md](LOG.md). All numerical work is independent code in [audit.py](audit.py).

## Verdict table

Every mathematical statement and proof step below is CORRECT. The external-source limitations following the table are not being passed off as verified mathematical or historical facts.

| Statement or step | Verdict | Reason |
|---|---|---|
| Abstract, line 32 | CORRECT | Its mathematical claims follow from the proved theorem; positivity is a separate assumption. |
| Tree/flow definitions, line 38 | CORRECT | Nonnegative mass starts at one and is conserved; finite trees cannot support it. |
| Flow consistency display, lines 40–43 | CORRECT | Normalize the restriction at a positive-flow child. |
| Equivariance, line 44 | CORRECT | The required symmetry is explicitly included and later proved. |
| Chain display, lines 45–47 | CORRECT | First-step mass selects the descendant tree. |
| Stationarity/invariance/ergodicity, line 48 | CORRECT | These are the standard stationary Markov-chain notions. |
| Question and positive-child distinction, lines 50–56 | CORRECT | The construction legitimately uses zero weights; exact book wording is not source-verified. |
| n-ray comparison, line 56 | CORRECT | Conditional n-ray laws are stationary on a proper subset; details below. |
| [thm:main](i), line 61 | CORRECT | The selected tree has conditional law GW_r; average the two colours. |
| [thm:main](ii), line 62 | CORRECT | Selected children preserve the binary root colour. |
| [thm:main](iii), line 63 | CORRECT | Two independent same-colour children force every invariant indicator to be constant within that colour. |
| Equivalent measures and labelled-tree discussion, line 67 | CORRECT | Absolute continuity transfers null exceptions; the witness event itself is isomorphism-invariant. |
| Fixed points and description, line 69 | CORRECT | F(x)-x=x(1-x)(1-2x)/5. |
| Ulam–Harris and branching laws, line 73 | CORRECT | Existence of a word depends only on strict ancestors, independently of its descendant offspring. |
| T_23 closed and full measure, line 75 | CORRECT | Violating a degree condition is visible at a finite depth. |
| AND/OR display, lines 76–78 | CORRECT | These are the independent Bernoulli success probabilities. |
| Definition of q_n, line 79 | CORRECT | Finite leaf randomization gives a deterministic finite-truncation function. |
| [lem:q](a), line 83 | CORRECT | Disjoint child descendant sets give the recursion. |
| Proof (a), line 94 | CORRECT | Independence, induction, and symmetric f_k give every stated property. |
| [lem:q](b), line 84 | CORRECT | The bounded truncation-adapted process is a martingale. |
| Phi multi-affine, line 96 | CORRECT | Each boundary Bernoulli variable occurs in a disjoint branch. |
| Boundary g_v laws, line 96 | CORRECT | They are independently 1/4 or 7/8 with mean 1/2. |
| Conditional expectation, line 96 | CORRECT | E[Phi(g) given F_n]=Phi(Eg)=q_n. |
| [lem:q](c), lines 85–89 | CORRECT | Pair enumeration gives the recursion and geometric upper bound. |
| Two-colouring disagreement, line 98 | CORRECT | Conditional independence given T gives 2q_n(1-q_n). |
| Pair-law display, lines 99–101 | CORRECT | Both marginals are fair, which determines all four masses from d_n. |
| Independent child pairs, line 102 | CORRECT | GW branching and independent boundary randomness give product pair laws. |
| AND disagreement display, lines 103–105 | CORRECT | d-d²/2. |
| OR disagreement display, lines 106–109 | CORRECT | (3d-3d²+d³)/4; one phrase omits “is 0.” |
| [eq:rec], lines 86–88 and averaging line 110 | CORRECT | Weighted sum is d(3-d)²/10. |
| Averaged pair-law closure, implicit in lines 98–110 | CORRECT | Marginals return to 1/2 after mixing over K, not conditional on K. |
| Contraction display/proof, lines 111–114 | CORRECT | The difference from 0.9d is d²(6-d)/10, nonnegative on [0,1]. |
| E, G, C definition, line 117 | CORRECT | G requires binary limits at every descendant, including the root. |
| [lem:colour](a), line 121 | CORRECT | Countable Borel conditions, invariant finite approximations, and subtree closure. |
| Borel/continuity argument, line 128 | CORRECT | Fixed-word presence is clopen; the descendant map is continuous on that domain. |
| [lem:colour](b), line 122 | CORRECT | GW(G)=1 and the binary limit has expectation 1/2. |
| Martingale convergence and summability, line 130 | CORRECT | Bounded martingale convergence and Tonelli; the sum bound is 5/2. |
| Countably many descendants, line 130 | CORRECT | Each present descendant has conditional law GW; take a countable union of null events. |
| Bounded-convergence probability, line 130 | CORRECT | E C=lim E q_n=1/2. |
| [lem:colour](c) and proof, lines 123 and 132 | CORRECT | Polynomial continuity passes the recursion to every t in G, including binary endpoints. |
| Nonempty S, line 137 | CORRECT | In all four cases some child has its parent's colour. |
| Fallback on all infinite trees, line 137 | CORRECT | At least one child has infinite descendants, even in trees with finite branches. |
| Product flow display, lines 138–140 | CORRECT | Local probability vectors give conservation at positive-flow vertices and zero elsewhere. |
| Positive-flow descendant is infinite, line 141 | CORRECT | Induction ensures every needed local vector is defined. |
| Flow consistency proof, line 141 | CORRECT | Identical products of local factors apply after rerooting, including entry from outside G into G. |
| Equivariance proof, line 141 | CORRECT | Isomorphisms preserve G, C, and infinite child subtrees. |
| Borel proof, line 141 | CORRECT | Infinite-descendant tests are Borel and coordinates are finite path products. |
| [eq:kernel], lines 142–144 | CORRECT | First-step weights are uniform on S(t). |
| B, G_0, conditional measures, line 146 | CORRECT | B and G_0 partition the full-measure set G. |
| [lem:cond], line 149 | CORRECT | Each ordered child colour vector has mass p_k 2^(-k). |
| Conditional product-law proof, line 153 | CORRECT | Conditioning independent trees separately preserves independence. |
| Theorem (i) setup, line 157 | CORRECT | Root colour and selected count are functions of (K,c). |
| Conditional expectation display, lines 158–160 | CORRECT | Each of the N selected children has law GW_r and their average has that expectation. |
| [eq:statr], lines 161–165 | CORRECT | Condition on root colour, then average the two conditional stationary laws. |
| Theorem (ii), line 167 | CORRECT | Colour preservation gives invariance and equivalence gives intermediate mass. |
| Theorem (iii), A' reduction, line 169 | CORRECT | Transitions stay in G'_r; intersecting A with it preserves the invariant-set relation. |
| Agreement along selected children, line 169 | CORRECT | A positive weighted average of indicators equal to 0 or 1 forces agreement of every indicator. |
| Conditioning on D, line 169 | CORRECT | D has conditional mass 3/10 for either colour; both child trees are independently GW_r. |
| Alpha display, lines 170–172 | CORRECT | alpha² and 1-(1-alpha)² equal the same conditional parent probability. |
| Alpha is 0 or 1, line 173 | CORRECT | 2alpha(1-alpha)=0; no unproved tail or regeneration step is used. |
| Four invariant sets, line 173 | CORRECT | Each of the two ergodic conditional laws assigns invariant sets mass 0 or 1. |
| [rem:positive], line 179 | CORRECT | Mixed children have probability (3/5)(1/2)+(2/5)(3/4)=3/5. |
| [rem:general], line 183 | CORRECT | Finite conservative colour rules give the same conditional-law stationarity argument. |
| [rem:jps], interpretation uniqueness, line 187 | CORRECT | The stated uniqueness is for this fixed point; the supplied construction proves existence independently of JPS. |
| [rem:jps], pivot criterion applied here, line 187 | CORRECT | Both the subcritical pivot tree and existence are independently established here; the general cited theorem's exact hypotheses remain source-unverified. |
| Pivotal-vertex definition and configurations, line 187 | CORRECT | Flipping a pivotal child changes its parent; such a child has the parent's colour here. |
| Pivot mean matrix, line 187 | CORRECT | diag(9/10,9/10), hence subcritical. |
| Agreement with disagreement slope, line 187 | CORRECT | The derivative at zero is 9/10. |
| Endogeny and pair-map assertions, line 187 | CORRECT | The binary variable is tree-measurable; the pair map has no positive fixed point in [0,1]. |
| Last remark, line 191 | CORRECT | The old invariant supports leave positive GW mass uncovered; these binary supports do not. |
| Computations: exact values, atom counts, early martingale tests, line 196 | CORRECT | Independent exact enumeration and moment calculations reproduce them. |
| Computations: conditional child colours given truncations, line 196 | CORRECT | Uniform integrability gives E[C given T\|n]=q_n; separate child truncations preserve independence. |

The CORRECT verdicts for mathematical consequences associated with cited works do not certify exact theorem numbering or quotations. The claimed author code, Lean checks, and depth-80 population simulation are unavailable here and receive no independent verification verdict. They are not premises of the proof.

## The load-bearing arguments

The martingale does not follow from an identity map on arbitrary colour probabilities. Indeed

\[
F(x)=\tfrac35x^2+\tfrac25(1-(1-x)^3),\qquad
F(x)-x=\tfrac15x(1-x)(1-2x).
\]

For example F(1/4)=43/160, not 1/4. What is true is that the fresh generation-n parameters g_v are independently 1/4 or 7/8, with mean exactly 1/2. The already-exposed root formula Phi is affine separately in each leaf parameter. Thus

\[
\mathbb E[q_{n+1}(T)\mid T|n]
=\mathbb E[\Phi((g_v)_v)\mid T|n]
=\Phi((1/2)_v)=q_n(T).
\]

For two independently randomized boundaries on the same tree, each child pair has law

\[
P(10)=P(01)=d/2,\qquad P(00)=P(11)=(1-d)/2.
\]

The AND disagreement is d-d²/2; the OR disagreement is (3d-3d²+d³)/4. Their offspring-weighted average is d(3-d)²/10. The pair-law family closes after this averaging, because the averaged single-coordinate mean is 1/2. Martingale convergence gives a limit Q. Bounded convergence gives E[2Q(1-Q)]=lim d_n=0, hence Q is binary. The source's stronger summability argument is also valid.

Uniqueness at this fixed point can also be proved without JPS. For any other tree-measurable interpretation D with P(D=1)=1/2, condition on T|n. Its descendant colours at generation n are independent fair bits because the descendant trees are independently GW. Propagating them upward gives E[D(T) given T|n]=q_n(T). Since the increasing truncation sigma-fields generate the full tree, these conditional expectations converge to D(T). Therefore D=C almost surely. This does not assert uniqueness of interpretations with different marginal laws.

The strongest possible objection to part (iii) would be loss of independence when conditioning on the parent. The chosen event D avoids that problem. It specifies K=2 and *both* child colours equal to r, so the two child trees remain independent GW_r. Any invariant indicator must agree on these two selected children, by strict positivity of their weights. If alpha is its GW_r probability, then under D

\[
0=P(\text{child indicators disagree}\mid D)=2\alpha(1-\alpha).
\]

That proves ergodicity directly. The paper's displayed argument is equivalent. It never assumes P(T in A' given D)=alpha; that would have been unjustified.

The fallback outside G is complete. At each visited vertex it computes a fresh local vector, choosing infinite child subtrees outside G and matching-colour subtrees inside G. Normalizing the restriction of the resulting product flow gives exactly the flow generated afresh from that child. Entering G from its complement causes no inconsistency.

## Exact calculations

Commands, run from this directory:

```sh
nice -n 10 python3 audit.py exact
python3 audit.py pivot
```

The attempted niceness adjustment was denied by the environment; the exact computation itself completed in 0.043 seconds. It did not require sustained compute. The program has 240-second CPU and wall limits. All subsequent invocations use a single Python process.

| n | Atoms | E q_n | E q_n² | d_n |
| --- | --- | --- | --- | --- |
| 0 | 1 | 1/2 | 1/4 | 0.5 |
| 1 | 2 | 1/2 | 11/32 | 0.3125 |
| 2 | 7 | 1/2 | 6343/16384 | 0.2257080078125 |
| 3 | 85 | 1/2 | 4542519076759/10995116277760 | 0.173720593397047 |
| 4 | not enumerated | 1/2 | 1430971267076077464029059548743167053319/3323069989462289682259517650700861440000 | 0.138765495993887 |

In particular,

\[
d_3=\frac{955039062121}{5497558138880},\qquad
d_4=\frac{230563727655067377100699276607263666681}{1661534994731144841129758825350430720000}.
\]

The source's d_1=5/16, d_2=1849/8192, and d_4 rounded to 0.13877 are all correct. The independent exact laws give the stated 2, 7, 85 atoms. Exact probability masses are listed below and in q1_law.tsv, q2_law.tsv, q3_law.tsv. The q_4 second moment was propagated from the exact q_3 law, rather than inferred solely from the disagreement recurrence:

\[
\mathbb E q_{n+1}^2
=\tfrac35 m_2^2+\tfrac25\bigl[1-2(1-m_1)^3+(1-2m_1+m_2)^3\bigr],
\quad m_j=\mathbb E q_n^j.
\]

This independently reproduces d_4. Exact conditional expectation tests also pass on all 1, 2, 12 truncations of depths 0, 1, 2. Pair identities were checked at four exact distinct rational d values; because both sides are polynomials of degree at most three, those checks establish the polynomial identities.

Exact law of q_1:

| q | Probability |
| --- | --- |
| 1/4 | 3/5 |
| 7/8 | 2/5 |

Exact law of q_2:

| q | Probability |
| --- | --- |
| 1/16 | 27/125 |
| 7/32 | 36/125 |
| 37/64 | 54/625 |
| 49/64 | 12/125 |
| 119/128 | 108/625 |
| 253/256 | 72/625 |
| 511/512 | 16/625 |

## Stationarity in the four cases

Write N for the number of children with the root's colour r. The following masses are conditional on r alone; they include the probability of the indicated K. They are not additionally conditioned on K.

| Root r | Parent K | Ordered child colours | N | Probability under GW_r | Selected subtree law |
|---|---|---|---|---|---|
| 1 | 2 | 11 | 2 | 3/10 | GW_1 |
| 1 | 3 | 001, 010, 100 | 1 | 3/10 total | GW_1 |
| 1 | 3 | 011, 101, 110 | 2 | 3/10 total | GW_1 |
| 1 | 3 | 111 | 3 | 1/10 | GW_1 |
| 0 | 2 | 01, 10 | 1 | 3/5 total | GW_0 |
| 0 | 2 | 00 | 2 | 3/10 | GW_0 |
| 0 | 3 | 000 | 3 | 1/10 | GW_0 |

For a fixed degree/colour vector producing r, the selected child has law GW_r regardless of N. Summing these masses yields stationarity of each GW_r, and their fair mixture is GW. It would be incorrect to claim the selected tree has unconditional law GW separately for each *parent* degree: conditional on K=2 its law is (1/4)GW_1+(3/4)GW_0, while conditional on K=3 it is (7/8)GW_1+(1/8)GW_0. Their offspring-weighted mixture is GW. The source uses the correct conditioning.

## Pivot calculations and the other remarks

| Parent colour | Configuration | Conditional probability | Pivotal children | Contribution to same-colour mean |
|---|---|---|---|---|
| 1 | K=2, 11 | 3/10 | Both | 6/10 |
| 1 | K=3, exactly one 1 | 3/10 | The unique 1 | 3/10 |
| 1 | K=3, at least two 1s | 4/10 | None | 0 |
| 0 | K=2, 01 or 10 | 3/5 | The unique 0 | 3/5 |
| 0 | K=2, 00 | 3/10 | None | 0 |
| 0 | K=3, 000 | 1/10 | All three | 3/10 |

There are no opposite-colour pivotal children. In colour order (0,1),

\[
M=\begin{pmatrix}9/10&0\\0&9/10\end{pmatrix},\qquad \rho(M)=9/10<1.
\]

This is a **subcritical** pivot tree. Independently, F'(1/2)=9/10 and the derivative at zero of the disagreement update is 9/10. Also d_(n+1)/d_n=(3-d_n)²/10 tends to 9/10. These three computations agree; the geometric bound is not an equality at finite depth. Mixed children occur with probability (3/5)(1/2)+(2/5)(3/4)=3/5, exactly as stated.

The general finite-colour remark is sound: conditioning on individual child colours preserves product conditional laws, and a parent colour occurring among the children ensures a unit flow. Under the standing nontrivial branching assumption even the component-ergodicity argument generalizes: condition on k>=2 children all having the same positive-probability colour, for any k with p_k>0.

For the n-ray comparison, an n-ray must start at the root. Set a_n=GW(A_n). Then a_n=(1/2)[1-(1-a_n)^n]. The positive solution for n=3 is (3-sqrt(5))/2; for n=4 it is positive and less than 1/2. A_3 and A_4 are disjoint because their roots have different degrees, and their union has probability less than one. Uniform selection among children extending an n-ray leaves the conditional law GW_(A_n) stationary. Thus the old mixture has the described absolute-continuity failure. This mathematical verification does not certify the exercise's precise wording from an unavailable edition.

## Independent depth-12 experiment

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py simulate
python3 audit.py stationarity
```

The simulation generated 4,096 independent actual GW trees with offspring mean 2.4, seed 17182026, in batches of 16. For each tree it evaluated q_0 through q_12 on that same tree by propagating boundary probabilities 1/2. It did not recycle samples through population dynamics. The hard node cap would abort instead of rejecting a tree, so it introduced no selection bias; the cap was never approached.

The run took 5.74 seconds, processed 258,225,346 vertices in total, and had at most 1,242,925 vertices resident in one batch. Peak process RSS was 253,902,848 bytes (242.1 MiB), below 1 GB. Computations used one numerical-library thread. Raw root probabilities are saved in simulated_root_q.npy; summary statistics are in simulation_results.json.

| n | Mean q | Theory d_n | Estimated d_n | SE of estimate | q <= 0.1 | q >= 0.9 |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.500000 | 0.50000000 | 0.50000000 | 0.00000000 | 0.000% | 0.000% |
| 1 | 0.510468 | 0.31250000 | 0.30988312 | 0.00120381 | 0.000% | 0.000% |
| 2 | 0.510726 | 0.22570801 | 0.22447903 | 0.00231705 | 20.532% | 32.764% |
| 3 | 0.510795 | 0.17372059 | 0.17237496 | 0.00252864 | 27.319% | 33.960% |
| 4 | 0.512563 | 0.13876550 | 0.13778210 | 0.00252883 | 31.909% | 36.890% |
| 5 | 0.510577 | 0.11360263 | 0.11131480 | 0.00243252 | 35.156% | 39.551% |
| 6 | 0.510009 | 0.09464565 | 0.09241803 | 0.00233130 | 37.939% | 41.162% |
| 7 | 0.509492 | 0.07989118 | 0.07819451 | 0.00222711 | 39.551% | 42.944% |
| 8 | 0.509239 | 0.06812350 | 0.06606291 | 0.00209795 | 41.284% | 43.774% |
| 9 | 0.508973 | 0.05855827 | 0.05678930 | 0.00198918 | 42.285% | 44.897% |
| 10 | 0.508816 | 0.05066508 | 0.04873517 | 0.00187433 | 43.213% | 45.825% |
| 11 | 0.509373 | 0.04407141 | 0.04245512 | 0.00176672 | 44.312% | 46.167% |
| 12 | 0.510193 | 0.03850746 | 0.03572028 | 0.00163376 | 44.775% | 47.144% |

“SE” is the across-tree sample standard error. At depth 12 the disagreement error is -1.71 SE; the largest absolute standardized disagreement error over all depths is about 2.174 at depth 1. These depths share trees and are correlated. No anomalous discrepancy is evident. The mean root probability at depth 12 is 0.51019 with SE 0.00753, consistent with 1/2.

The combined fraction in [0,0.1] or [0.9,1] grows from 53.30% at depth 2 to 91.92% at depth 12. At depth 12 the fractions below and above 1/2 are 49.15% and 50.85%. The near-endpoint bins need not already each contain 1/2 at finite depth; the proof gives those exact limiting masses. Floating-point arithmetic may round extremely small probabilities to endpoints, so the experiment uses 0.1-wide bins and does not interpret exact numerical zeros or ones as finite-depth binary colours.

The exact enumeration then checked the *next tree's own* degree and ordered child-colour vector. It enumerated root local types, independent conditional child local types, and uniform same-colour selection; it did not simply plug the desired marginal into an average. Results:

| Root colour | Next degree | Next child colours | Target probability | Next probability | Difference |
| --- | --- | --- | --- | --- | --- |
| 0 | 2 | 00 | 3/10 | 3/10 | 0 |
| 0 | 2 | 01 | 3/10 | 3/10 | 0 |
| 0 | 2 | 10 | 3/10 | 3/10 | 0 |
| 0 | 3 | 000 | 1/10 | 1/10 | 0 |
| 1 | 2 | 11 | 3/10 | 3/10 | 0 |
| 1 | 3 | 001 | 1/10 | 1/10 | 0 |
| 1 | 3 | 010 | 1/10 | 1/10 | 0 |
| 1 | 3 | 011 | 1/10 | 1/10 | 0 |
| 1 | 3 | 100 | 1/10 | 1/10 | 0 |
| 1 | 3 | 101 | 1/10 | 1/10 | 0 |
| 1 | 3 | 110 | 1/10 | 1/10 | 0 |
| 1 | 3 | 111 | 1/10 | 1/10 | 0 |

Every omitted pattern has probability zero under the respective conditional law. All rational differences are exactly zero. Averaging the two conditional tables gives probability 3/20 for each degree-2 vector and 1/20 for each degree-3 vector, the unconditional GW local law. This checks the requested finite local marginal; full Borel stationarity is proved by [lem:cond] and the conditional-expectation argument.

## Typos, unclear wording, and presentation issues noticed

1. Line 106: “the OR of one coordinate with probability 1/8” omits **“is 0”**. The intended assertion is P(OR=0)=1/8, not P(OR=1)=1/8. The displayed computation uses the correct event.
2. Lines 56 and 191: define an “n-ray” explicitly as a ray **starting at the root**. If “contains” meant a ray beginning anywhere below it, the stationary-support discussion would describe different events.
3. Line 141: the Borel claim cites only [lem:colour](a). Add the elementary Borel test for an infinite descendant subtree to cover the fallback as well. The existing claim is correct, but the supporting sentence is compressed.
4. Line 187: make the pivotal configuration “two children of colour 1, both pivotal” explicitly `(K=2,c=11)`. It is not the OR configuration with two 1 children, which has no pivotal children.
5. Line 187: “unique” is correctly qualified by “corresponds to its fixed point Bernoulli(1/2)”; retain that qualification. The constant all-zero and all-one interpretations also exist at other fixed points. A casual abridgment to “the unique interpretation” would be false.
6. Line 196: “checks that GW(C=1)=1/2” should distinguish a finite computation of E q_n=1/2 from the theorem's limiting assertion, which is justified by bounded convergence. A finite run alone cannot certify an infinite-tree event's exact probability.
7. Lines 196 and 220: “No data were used” is ambiguous beside reported simulated samples and generated computation outputs. “No external datasets were used; computational outputs are available ...” would be more precise.
8. Lines 26 and 251: the manuscript date is 13 October 2026, while the referenced Math Brain paper path names 24 October 2026. This may reflect a later revision with unchanged date; clarify the version date rather than treating this as a mathematical error.
9. Line 224: the bibliography width argument is `{9}`, but there are eleven entries. Use `{99}` to allow space for two-digit numerical labels; actual typeset spacing was not checked by compilation.

I noticed no additional typographical error in the mathematical formulas. None of the listed issues changes the theorem.

## What could not be checked; attribution and novelty

- No book or cited article was supplied. I cannot certify exact wording or numbering of Proposition 17.17, Question 17.18, Exercise 17.22, the cited path-shift corollary, or the specified August 2026 edition. The flow-rule definition and the question's separate positivity distinction agree with my recollection. I know no remembered extra positivity requirement that invalidates this construction, and its all-infinite-tree extension is explicitly complete.
- I recognize Johnson–Podder–Skerman's interpretation/pivot-tree framework and the subcritical-or-critical two-state criterion from memory. I cannot independently certify the precise general hypotheses or theorem numbers. Their claimed interpretation uniqueness is consistent with uniqueness for a fixed distribution, not across different fixed points. Bounded offspring here satisfies finite moment restrictions. The paper's own argument proves the needed existence without invoking that criterion.
- I recognize the Aldous–Bandyopadhyay endogeny/bivariate framework and Holroyd–Martin win/loss recursion. Exact source descriptions and the Rousselin bibliographic statement remain unverified. None is needed for the self-contained proof.
- Author checks.py, Bounds.lean, Lean/Mathlib versions, the 400,000-sample depth-80 run, and the random depth-3 author checks are not supplied and were not accessed. I independently reproduced the identities, early exact laws, pivot means, and the requested local stationarity calculation, not the claimed execution history.
- Funding, affiliations, AI-work chronology, links, publication status, and priority are outside what can be verified from this source alone.
- I have **no reliable independent memory of a prior solution of this precise question**, nor of this exact AND/OR invariant-event application to a flow rule. I therefore neither identify a prior solution nor certify novelty. General tree automata and endogenous recursive colourings are established frameworks; the precise flow-rule application requires a literature check to settle priority. No speculative reference is supplied.

The proof's central claims survive independent rederivation: tree-measurable binary colouring, a globally defined equivariant flow rule, exact GW stationarity, an invariant half-mass event, and ergodicity of each colour-conditioned chain.

## Appendix: full exact law of q_3

| q_3 | Exact probability |
| --- | --- |
| 1/256 | 2187/78125 |
| 7/512 | 5832/78125 |
| 37/1024 | 8748/390625 |
| 49/1024 | 5832/78125 |
| 119/2048 | 17496/390625 |
| 253/4096 | 11664/390625 |
| 511/8192 | 2592/390625 |
| 259/2048 | 11664/390625 |
| 343/2048 | 2592/78125 |
| 721/4096 | 39366/9765625 |
| 833/4096 | 23328/390625 |
| 1771/8192 | 15552/390625 |
| 3577/16384 | 3456/390625 |
| 2567/8192 | 157464/9765625 |
| 1369/4096 | 8748/1953125 |
| 7009/16384 | 209952/9765625 |
| 1813/4096 | 3888/390625 |
| 17143/32768 | 93312/9765625 |
| 4403/8192 | 34992/1953125 |
| 9361/16384 | 23328/1953125 |
| 18907/32768 | 5184/1953125 |
| 2401/4096 | 432/78125 |
| 10309/16384 | 236196/48828125 |
| 22643/32768 | 629856/48828125 |
| 5831/8192 | 7776/390625 |
| 48661/65536 | 419904/48828125 |
| 12397/16384 | 5184/390625 |
| 25039/32768 | 1152/390625 |
| 13009/16384 | 52488/9765625 |
| 27143/32768 | 139968/9765625 |
| 54601/65536 | 472392/244140625 |
| 56161/65536 | 93312/9765625 |
| 112847/131072 | 629856/244140625 |
| 14161/16384 | 34992/1953125 |
| 59461/65536 | 209952/48828125 |
| 30107/32768 | 46656/1953125 |
| 120947/131072 | 279936/48828125 |
| 242461/262144 | 314928/1220703125 |
| 60809/65536 | 10368/1953125 |
| 30743/32768 | 472392/48828125 |
| 62161/65536 | 1376352/48828125 |
| 125447/131072 | 995328/48828125 |
| 251209/262144 | 209952/244140625 |
| 127427/131072 | 1889568/244140625 |
| 64009/65536 | 15552/1953125 |
| 256069/262144 | 2752704/244140625 |
| 129047/131072 | 419904/48828125 |
| 129283/131072 | 6912/1953125 |
| 258769/262144 | 577152/48828125 |
| 517727/524288 | 1889568/1220703125 |
| 64861/65536 | 314928/48828125 |
| 129947/131072 | 839808/48828125 |
| 260269/262144 | 559872/48828125 |
| 520643/524288 | 839808/244140625 |
| 260929/262144 | 629856/48828125 |
| 261121/262144 | 768/1953125 |
| 522263/524288 | 186624/9765625 |
| 261469/262144 | 279936/48828125 |
| 523163/524288 | 373248/48828125 |
| 1046389/1048576 | 5038848/1220703125 |
| 130847/131072 | 69984/48828125 |
| 261769/262144 | 186624/48828125 |
| 523663/524288 | 124416/48828125 |
| 1047361/1048576 | 279936/48828125 |
| 523883/524288 | 559872/48828125 |
| 1047901/1048576 | 808704/48828125 |
| 524063/524288 | 62208/48828125 |
| 1048201/1048576 | 82944/48828125 |
| 2096423/2097152 | 7838208/1220703125 |
| 2096747/2097152 | 248832/48828125 |
| 1048441/1048576 | 279936/48828125 |
| 2096927/2097152 | 387072/48828125 |
| 4194061/4194304 | 7838208/1220703125 |
| 4194169/4194304 | 124416/48828125 |
| 2097107/2097152 | 373248/244140625 |
| 4194229/4194304 | 497664/244140625 |
| 8388527/8388608 | 5225472/1220703125 |
| 8388563/8388608 | 165888/244140625 |
| 4194289/4194304 | 41472/244140625 |
| 8388583/8388608 | 55296/244140625 |
| 16777189/16777216 | 2322432/1220703125 |
| 16777201/16777216 | 18432/244140625 |
| 33554423/33554432 | 663552/1220703125 |
| 67108861/67108864 | 110592/1220703125 |
| 134217727/134217728 | 8192/1220703125 |

Task: “Be a hard, independent referee” — 12 November 2026, 04:51 +04 (launch log; Asia/Tbilisi).
