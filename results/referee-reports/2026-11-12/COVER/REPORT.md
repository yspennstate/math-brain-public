Overall verdict: SOUND

The mathematical proof of Theorem 1 is sound. I found no counterexample, missing boundary case, incorrect sign, or unsupported equality step. I independently rebuilt the four-state polynomial and checked every coefficient of all 30 substituted polynomials, rather than accepting the supplied certificate or its reported checks. The qualification to this verdict is about the description of the auxiliary verification: the Lean files prove narrower statements than a reader might infer from the manuscript, and the random-point script is not a proof checker and has a deficient failure signal. Neither issue is a gap in the mathematical proof, because the exact certificate verifier checks the required identities and strictness conditions.

Line references below refer to PAPER.tex. I used no browsing, no other agents, and no authors' mathematical modules in my computations. All referee programs and their outputs are saved here. I did not modify PAPER.tex, code/, evidence/, or lean/.

## 1. Theorem 1, including the three-state argument — SOUND

Lines 55–60 state the correct bound, with the stated convention that the initial state is visited at time zero. Both constants are correct: 2H_2=3 and 3H_3=11/2. Equality is proved, not merely found experimentally.

The reduction to conductances at lines 71–76 is complete. For an arbitrary irreducible reversible chain, take w_xy=pi_x P_xy and h_x=pi_x P_xx. Detailed balance makes w symmetric, and q_x+h_x=pi_x. Irreducibility gives a connected positive-edge graph and q_x>0 when n>=2. Removing holding therefore produces a well-defined irreducible reversible jump chain. Conversely, any connected nonnegative conductance assignment and nonnegative holding weights define such a chain. A missing edge is represented by weight zero; completeness of the positive support is never assumed.

For three states, connectivity means at most one of a,b,c is zero, so the denominator in (three), lines 149–150, is strictly positive. I verified the numerator identity symbolically with my own integer-polynomial operations. One direct derivation is

    W E_pi C = (B_12+B_13+B_23)/(ab+bc+ca) - W,
    Q = B_12+B_13+B_23 - 4W(ab+bc+ca),
    W = 2(a+b+c).

This gives precisely the displayed Q and denominator. The decomposition at line 154 is an exact identity. Schur and AM–GM apply to nonnegative variables, including a zero edge. For the AM–GM part, a^3+b^3+c^3=3abc forces a=b=c, including the all-zero possibility; connectivity excludes that possibility. Thus equality requires a=b=c>0. Equal conductances give the loopless simple random walk on K_3.

For four states, the denominator, certificate and equality argument are checked in section 5 below. Proposition 3 makes every nonzero holding vector strictly worse than the claimed lower bound for n=3,4. Combining these arguments proves the full “if and only if” in Theorem 1. Conversely, the complete-graph walk has the claimed cover time by the geometric waiting-time computation at lines 45–47. There is no need for aperiodicity: paths, stars and other bipartite supports are included.

## 2. Lemma 2 and the alternating-sum formula — SOUND

The positive-definiteness argument at lines 78–81 is valid even with missing edges. Extend a vector on S by zero outside S. Zero Laplacian energy forces it to be constant on the entire connected graph; because S is proper it must be zero. Consequently every principal submatrix used in the argument is invertible.

In Lemma 2, lines 83–91, the first-step equation gives L_S g_S=q_S. The stationary average is q_S^T g_S/W, giving exactly q_S^T L_S^{-1}q_S/W. The zero contribution from initial states in J is correctly included by omitting them. Finite irreducible chains have finite expected hitting and cover times, so the expectations used here exist.

The inclusion-exclusion at lines 93–98 uses first hits of sets, not a presumed distribution of the last vertex. Pathwise, C=max_x T_x and min_{x in J}T_x=T_J. The max/min identity can also be obtained by integrating the inclusion-exclusion identity for the events {T_x>t}. After replacing J by its complement S, its sign is

    (-1)^(|J|+1) = (-1)^(n-|S|+1).

The J=V term is zero because the walk starts in V. J empty is absent throughout. Thus exactly the nonempty proper S occur. For n=3 the size-two terms have sign + and the singleton terms sign −. For n=4 the signs for |S|=1,2,3 are +,−,+. These are the signs used later; there is no missing factor or off-by-one step.

As the section explicitly states at lines 75–76, its q-formula is for chains without holding. With holding the corresponding formula replaces both q vectors and W by m and sum m, retaining the same L. This follows from L_S g_S=m_S. My rational checks verified both versions. The identity extends to every finite n>=2, subject to connectivity; it is not specific to three or four states.

## 3. Proposition 3 and its pointwise hypothesis — SOUND

Lines 113–117 correctly use the occupation count before the cover time, including time zero and excluding the terminal arrival. For a fixed t, a path contributes to N_xy exactly when it starts at x, ends at y, and its visited set is proper. Reversal preserves that condition. Detailed balance along a length-t path gives

    q_x Pr_x(path) = q_y Pr_y(reversed path).

Summing gives q_x N_xy=q_y N_yx. Dividing by q_x q_y proves that K_xy=N_xy/q_y is symmetric. Its entries are nonnegative because N is an occupation expectation. No positive-semidefinite assertion about K is required. Its row identity Kq=E_x C follows by counting the C occupied times t=0,...,C−1.

On adding holding, each departure from y in the jump chain takes a geometric number of actual steps of mean (q_y+h_y)/q_y. These are precisely the departures counted by N; no holding at the last new state is charged. This proves E_x C_h=(Km)_x. Averaging against the new stationary law gives m^T K m/(sum m), and expanding the symmetric quadratic form gives (holding), including its factor 2 and subtraction of c_0 sum h.

The assumptions needed are exactly the stationary bound for the jump chain and the individual bounds 2E_x C>=c_0, together with h>=0. Entrywise nonnegativity suffices for h^TKh>=0. No monotonicity of E_pi C under holding, uniform starting law, or additional bound on N is used.

The pointwise hypothesis is actually proved at lines 130–132. Every sample path needs at least n−1 moves to cover n states. Thus E_x C>=2>3/2 for n=3, and E_x C>=3>11/4 for n=4. For these cases the linear holding terms are at least sum h and (sum h)/2 respectively. Any positive holding therefore gives a strict inequality above c_0, including when the original jump chain is extremal. There is no unproved pointwise assumption in Theorem 1.

## 4. Remark 4: holding can lower the stationary cover time — SOUND

For the weights in lines 138–140, my augmented-state rational solves give

    h=(0,0,0): E_pi C = 227901/2278 = 100.04433713784022...,
    h=(0,0,1): E_pi C = 2599109/30552 = 85.07164833726107...,
    difference = -7776575/519384 < 0.

The displayed approximations 100.04 and 85.07 are correct. Here the stationary mass at state 3 changes from 1/102 to 51/152. This example is compatible with Proposition 3: both cover times remain above 3. It correctly rules out the stronger monotonicity assertion.

## 5. Proposition 5, the degree-16 identity, cone coverage and equality — SOUND

For a pair S={i,j}, the inverse of [[q_i,−w_ij],[−w_ij,q_j]] gives numerator q_i q_j(q_i+q_j+2w_ij) and denominator Delta_ij=q_i q_j−w_ij^2, exactly as at lines 165–168. Each size-three determinant is the same positive spanning-tree polynomial tau. I independently checked the four determinants and enumerated its 16 spanning trees.

The signs from section 2 give

    W E_pi C = W + A/tau - sum B_ij/Delta_ij.

Subtracting (11/2)W and multiplying by 2 tau R gives exactly F at lines 173–174; in particular the coefficient −9 is correct. Here deg A=4, deg tau=3, deg R=12 and deg B=3, so all terms have degree 16. My reconstruction has exactly 13,368 nonzero terms and 2,421 negative coefficients, agreeing with lines 177–178 and with the supplied polynomial coefficient by coefficient.

Every denominator factor is strictly positive on any connected support, even with zero edges: Delta is a size-two principal minor and tau a size-three principal minor. Thus clearing denominators preserves the inequality everywhere needed. Disconnected supports are not silently used to divide by a zero denominator.

Relabelling vertices preserves the expression F: it permutes the degree vector and principal submatrices, permutes the summands of A, leaves tau unchanged, and permutes the six Delta and B factors. This also follows from (F) on strictly positive weights and polynomial identity. My check verifies polynomial invariance under all 24 vertex permutations explicitly. The argument needs only vertex-induced edge permutations, not arbitrary permutations of six edges.

The action on edge orderings is free: a vertex permutation fixing an ordering must fix each of its six edges. The action of S_4 on these edges is faithful, so that permutation is the identity. I generated the orbits independently from all 720 permutations, rather than trusting the manifest: there are 30 disjoint orbits of size 24, and their union is all 720 orderings. The supplied representatives match these orbits. Tied weights may belong to multiple cones; at least one ordering always exists, which suffices.

On a closed ordered cone the substitution is exactly

    z_0=x_o0, z_j=x_oj−x_o(j−1) for j>=1,
    x_ok=z_0+...+z_k.

All these variables are nonnegative, including on cone intersections and coordinate boundaries. My program applied the forward substitution to the reconstructed F and compared every coefficient to each decompressed certificate. All 577,620 stored nonzero coefficients are positive integers; every omitted coefficient is zero. Therefore every G_o is nonnegative on the entire closed nonnegative orthant. This argument uses neither strictly positive z nor a limiting argument.

The strictness claims at lines 194–197 also hold:

- In each of the 30 polynomials, all five coefficients of z_0^14 z_j^2 are positive. The smallest of these 150 coefficients is 25,165,824. If every edge is positive, z_0>0. Any positive gap z_j then makes G_o>0. Hence zero requires every gap to vanish.
- If some edges vanish, let j be the first positive rank. Then z_0=...=z_(j−1)=0, z_j>0, and the positive-edge support is exactly the suffix o_j,...,o_5. For every connected suffix, I checked that the coefficient of z_j^16 is positive. There are 84 such tests; their coefficients are among {384,696,41472,106320,3008000}. This one monomial proves strict positivity regardless of which later gaps vanish.
- Conversely, the coefficient of z_0^16 is zero in every cone. Thus all equal weights make F vanish. Connectivity requires their common value to be positive.

These observations prove precisely the claimed equality set on connected supports. There is no boundary equality on a path, star, cycle, or other graph with a missing edge. Proposition 5 and (F), followed by Proposition 3, complete the four-state part of Theorem 1.

## 6. Remark 6 and what the supplied checkers establish — SOUND, with qualifications to auxiliary claims

The finite computational assertions at lines 205–212 agree with my independent computations, including the coefficient totals, 624 connected weightings in {0,1,2}^6, three holding vectors per weighting, and the two equality weightings without holding. Those two weightings represent the same transition matrix, since multiplying every conductance by a common positive constant changes no transition probability.

The actual exact proof checker is code/verify_certificate.py, read together with code/poly.py. It checks what Proposition 5 needs. Specifically, it reconstructs F from exact determinant/adjugate operations; independently builds tau from spanning trees; checks equality with the stored polynomial; verifies vertex symmetry; validates the cone coefficients; inverts the cumulative substitutions by ascending negative shears and checks the resulting polynomial identities; checks the interior and connected-boundary strictness monomials; and checks coverage of 720 edge orderings. Its inverse substitution is algebraically valid and is not a random evaluation test. My independently implemented forward-substitution audit agrees with all its reported substantive results. I did not execute the authors' programs or rely on their saved PASS records.

The roles of the other scripts are narrower. certify_cones.py starts from a stored F, so it needs a separate verification that this F is the numerator of the claimed cover-time defect. symbolic_four.py supplies a construction, and verify_certificate.py supplies another reconstruction. random_point_check.py checks only finitely many evaluations. Even exact agreement at all its points cannot prove a degree-16 polynomial identity in six variables.

There is also an actual reporting defect in random_point_check.py: lines 79–80 increment a mismatch counter but still print “ok”, and the script never asserts bad==0 or exits unsuccessfully for a mismatch. Lines 83–90 print the coverage count without asserting it is 720. **ERROR in that script's pass/fail signalling**, not in Proposition 5 or in the exact verifier. It should not be used as an exit-status-based certificate gate.

The Lean sentence at lines 213–214 needs narrower wording. On source inspection:

- P0245_N3.lean proves the bound for an explicit rational function coverTime under a>0,b>0,c>0 and nonnegative holding. It supplies first-step algebra, but does not construct a probabilistic Markov chain and identify its expected cover time in a probability formalization. Its final theorem does not include connected zero-edge boundary cases or equality characterization.
- P0245_HoldingReduction.lean proves the algebraic matrix implication assuming a symmetric entrywise nonnegative K and the two inequalities. It does not formalize the occupation-count construction, path reversal, or jump-chain waiting argument that establish these assumptions and interpretations.

These are useful partial formal checks. They do not amount to a formal proof of the entire theorem. The supplied README describes their scope more carefully than the manuscript. I inspected the source but did not recompile Lean; a pinned Mathlib project is not supplied here. The handwritten arguments and the independent certificate check already cover the omitted mathematical cases, so this scope qualification does not leave the paper's theorem unproved.

## Larger n and the statement of the open problem

**SOUND as a description of what this paper proves.** The conductance representation, positive-definite killed Laplacians, hitting formula, inclusion-exclusion identity, symmetric occupation construction, and conditional holding proposition all extend to n=5 and beyond. As a small additional check, my exact program compared the five-state augmented-state and Laplacian formulas on K_5, K_5 with holding, and a five-state path, obtaining 25/3, 13273/1380, and 37/2 respectively.

For n=5 the target is 4H_4=25/3 and the pointwise condition is E_x C>=25/6. The deterministic lower bound C>=4 falls short by 1/6. This failure is a failure of the trivial sufficient estimate, not a counterexample to the pointwise hypothesis. The manuscript does not prove that hypothesis for n=5. The holding proposition therefore remains conditional there.

The ordering-orbit count in line 221 is correct: 10!/5!=30,240, since the action on the ten labelled edges is again faithful and free on orderings. An analogous rational numerator can be formed, but this paper supplies no five-state polynomial certificate and no argument that ordered substitution must give nonnegative coefficients in that case. The four-state certificate cannot simply be reused. Lines 219–223 claim numerical evidence, not a proof for five or six states. I did not independently verify those historical numerical searches or an external claim about whether a general holding reduction is currently open.

The formulation of Open Problem 6.30 at lines 39–53 is internally unambiguous: finite irreducible reversible discrete-time chains, stationary initial law, initial state counted at time zero, holding allowed, and comparison with the loopless complete-graph walk. It matches the problem formulation supplied for this referee run. The local files contain only a citation and link to Aldous–Fill, not the original problem's text. Under the instruction prohibiting browsing I cannot certify its exact original wording or numbering, or check the historical citations. There is no visible inconsistency in the restatement; this is an attribution limit, not a mathematical gap.

## Independent programs, outputs and reproducibility

All programs are original referee implementations and import no code from code/. The exact tests use fractions.Fraction. The cone checker uses integer coefficients and exponents packed in base 32; all intermediate total degrees are at most 16, so exponent addition cannot carry between packed coordinates. Its recursive determinant expansion and bordered-determinant numerator provide a different reconstruction from the authors' adjugate implementation.

Reproduce the checks from this directory, one command at a time:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B referee_cones.py > referee_cones.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B referee_exact.py > referee_exact.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 -B referee_numeric.py > referee_numeric.log 2>&1
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -B referee_summary.py > referee_summary.log 2>&1
```

The corresponding *_results.json files retain detailed outputs. Each computation has a 280-second alarm. All four completed in under nine seconds each, with measured peak resident memory below 75 MB per process. Numerical libraries were restricted to one thread. The first two saved logs also contain a harmless “nice: setpriority: Operation not permitted” message from the attempted priority reduction; the computations themselves completed successfully.

### Exact rational checks: referee_exact.py and referee_summary.py

The first-step solver uses the augmented chain (current state, visited mask), ending immediately when the mask becomes full. It solves the visited-set blocks in descending order. A separate full augmented linear system cross-checks 57 of the cases; the full four-state transient system has 28 states. Occupation counts are computed with individual state-indicator rewards and then checked against the holding identity. A separate killed-Laplacian solve computes the alternating sum.

The main exact run reports:

```text
passed: true
random loopless weightings: 80 on 3 states, 80 on 4 states
each random weighting checked without holding and with rational holding
connected four-state grid weightings: 624
grid chains with three holding vectors each: 1872
total chains including named and random cases: 2225
full augmented-state cross-checks: 57
grid minimum: 11/2
grid equality weights: (1,1,1,1,1,1), (2,2,2,2,2,2), both without holding
seconds: 2.2361; peak RSS: 17547264 bytes
```

The grid holding vectors are (0,0,0,0), (1,0,2,3), and (0,1000,0,0). The named tests include edge weights as small as 10^-12, nearly disconnected supports, nearly isolated vertices, and holding weights as large as 10^6. Every comparison was exact. Selected unit-edge examples are:

| Chain without holding | E_i C in vertex order | E_pi C |
| --- | --- | --- |
| K_3 | (3,3,3) | 3 |
| Three-state path | (4,5,4) | 9/2 |
| K_4 | (11/2,11/2,11/2,11/2) | 11/2 |
| Four-state path | (9,11,11,9) | 31/3 |
| Four-state star, center first | (10,9,9,9) | 19/2 |
| Four-cycle | (6,6,6,6) | 6 |
| K_4 minus edge 01 | (59/10,59/10,34/5,34/5) | 161/25 |

As an additional elementary check, the star values follow from coupon collection: from its center the mean is 2(3H_3)−1=10; from a leaf it is 2(3H_2)=9. Its stationary center mass is 1/2, giving 19/2.

referee_summary.py also verifies the three-state polynomial identity and Schur decomposition coefficient by coefficient. It rounds eight numerical endpoints to rational conductances with denominator 10^9 and rechecks their cover times by exact full augmented-state solves and the alternating formula. All have strictly positive rational defect unless weights are exactly equal. The max/min identity is additionally checked exhaustively for time vectors in {0,1,2}^n for n=3,4,5.

### Complete certificate check: referee_cones.py

```text
PASS cone_00.json.gz through cone_29.json.gz, every file checked
passed: true
degree: 16
polynomial terms: 13368
negative original terms: 2421
positive substituted coefficients checked: 577620
edge orderings covered: 720
interior strictness coefficients checked: 150
connected boundary suffix tests: 84
seconds: 7.2191; peak RSS: 71401472 bytes
```

The check includes decompression, exact reconstruction, forward substitution, equality with every stored coefficient, hashes, complete orbit enumeration, and all strictness monomials. No cone was skipped. Hash agreement alone was not used as evidence of mathematical correctness.

### Numerical minimization: referee_numeric.py

I normalized the six edge weights to sum to one and used five independent log ratios. For holding searches, four additional nonnegative holding weights were optimized. The objective was computed from augmented-state first-step equations, independently of F and the certificate. Local descent used L-BFGS-B with 40 random starts without holding and 40 with holding, plus six starts on each of four boundary supports.

```text
K4 support, no holding: 40/40 successful descents
endpoint range: [5.500000000000012, 5.500000000000756]
maximum |w_e-1/6|: 2.219e-7

K4 support, holding allowed: 40/40 successful descents
endpoint range: [5.5000000000000036, 5.500000000000572]
maximum |w_e-1/6|: 1.937e-7; all endpoint holding weights: 0

boundary path, optimized weights: 10.252939685168187
boundary star, optimized weights: 9.500000000000004
boundary cycle, optimized weights: 6.000000000000002
K4 minus one edge, optimized weights: 5.931646457416247

finite-difference Hessian eigenvalues in log-ratio coordinates at K4:
[0.10620390, 0.37500019, 0.95629607, 1.62500012, 1.62500012]
seconds: 8.8419; peak RSS: 73940992 bytes
```

The search found the claimed minimizer and no competing one. These searches are not a proof of global minimality or uniqueness, and were performed on bounded numerical parameter ranges. Global uniqueness follows from the exact positivity and equality argument, not from the optimizer or the positive numerical Hessian.

## Corrections and scope clarifications

No correction to the main theorem, its formulas, or its boundary/equality proof is required.

1. **PAPER.tex, lines 213–214:** qualify the Lean claim. Suggested replacement: “Lean checks the three-state rational cover-time formula for strictly positive edge conductances and nonnegative holding, and the algebraic symmetric-matrix implication used in Proposition 3. The probabilistic occupation identity, connected zero-edge boundary cases, and equality characterization are proved above.” This resolves the ambiguity about the extent of formal verification.

2. **code/random_point_check.py, lines 79–90, relevant to PAPER.tex lines 207–210:** make failure observable: report a cone as “ok” only if all its comparisons agree, assert bad==0 at the end, and assert len(cov)==720. The current script can report a mismatch and still return exit status zero. Retain code/verify_certificate.py as the exact proof checker; random evaluations are supplementary checks.

3. **PAPER.tex, lines 41–45:** no mathematical change is indicated by the supplied text. Exact attribution to Aldous–Fill remains unverified in this run because the cited problem text is not included locally and browsing was prohibited. Supply a page or quoted problem statement if exact attribution is to be certified from a self-contained referee package.

Task: “You are refereeing a mathematical paper that has been posted.” Received 12 November 2026, approximately 19:55 Asia/Tbilisi; the supplied prompt does not record a more precise receipt time.
