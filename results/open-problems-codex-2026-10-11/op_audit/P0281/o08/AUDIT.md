VERDICT: PASS (correct and complete)

Independent audit of P0281, 2026-10-12. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl and LITERATURE.md in the claimant's directory, as well as PROOF.md and the relevant verification records. All audit downloads, scripts and outputs are in this audit directory. The claimant's directory was read only.

## Exact claim and scope

ATTEMPT.md lines 7–11 and CLAIMS.jsonl entry 1 assert that, for rate-one continuous-time TASEP with every finite n >= 1, initially X_i(0) = -i in right-to-left order, every t >= 0 and every a,b in Z^n,

    p_t(a)p_t(b) <= p_t(floor((a+b)/2))p_t(ceil((a+b)/2)),

with componentwise rounding and mass zero outside the support. At an integral midpoint this is exactly p_t(a)p_t(b) <= p_t((a+b)/2)^2. Thus the claim answers the finite-particle, integral-midpoint problem stipulated in the audit request. It additionally proves a precisely defined stronger rounded-midpoint assertion; it does not assert a real-variable extension.

I independently downloaded the workshop PDF and checked Section 3 on PDF page 2. Its question concerns step TASEP and the midpoint inequality; it does not itself specify finite n or rounding. The claimant explicitly acknowledges this distinction. The result is complete for the problem as stipulated here, without an implicit claim about a density on infinite configurations, arbitrary initial data, or unequal particle rates. A common positive rate can be absorbed into time.

## Issue found

ATTEMPT.md line 31 has an editorial indexing error: to derive (2) with the displayed lambda index i from z_k^{m+1} < z_k^m <= z_{k+1}^{m+1}, the substitution is k = m-i+1, not k = m-i. The latter produces the same interlacing relation with lambda index i+1 and, if applied over the intended full range without relabeling, includes an invalid k=0. Name the correct substitution there. The definition on line 27, the displayed inequalities on line 29, the edge identification D_m = lambda_m^m, and all subsequent arguments are correct. This typo does not leave a mathematical gap: direct substitution into the displayed definition establishes the asserted relation.

I found no failed inequality, incorrect stochastic identification, missing substantive hypothesis, or quantifier restriction that invalidates the result.

## Proof checked against independently fetched sources

**Array process and projection, lines 15, 27–31 and 63.** In the independently fetched Borodin–Ferrari paper, arXiv:0804.3035, PDF pages 3–4 and 36–38, the initial array is z_k^m = k-m-1, the blocking condition is z_k^m = z_k^{m-1}-1, and pushing follows (k,m) to (k+1,m+1). Therefore the k=1 edge is never pushed, has its own independent rate-one jump attempts, and is blocked precisely by the particle immediately to its right. Its initial positions are -m. This is the finite TASEP generator, rather than the pushing process on the other edge. The coordinate transformation yields zero initial partitions, nonnegative interlacing arrays, and D_m = X_m+m = lambda_m^m. The projection is a selection of coordinates, which is crucial later.

**Top row and links, lines 33–61.** I checked BF equation (2.101), Proposition 2.22, definition (2.94), the matrices on PDF page 24, and Lemma 2.13(ii), equation (2.57), on page 26. The equal-alpha limit of the alternant ratio is V(y)/V(a), with V(a) = product_{j=1}^{n-1} j!. The transpose convention for the Poisson determinant is immaterial. Factoring its columns and rows gives the falling-factorial determinant, hence

    det[q_t(y_j-a_i)] = e^(-nt)t^(sum L_j-n(n-1)/2)V(L)/product L_j!,

where L_j = y_j+n. The zero entries when L_j < i-1 agree with the polynomial falling factorial, so no division by a negative factorial is being performed.

The equal-alpha links are (m-1)! V(v)/V(u) on u_i < v_i <= u_{i+1}. BF's step determinant has sign (-1)^(m-1); the normalization product contributes the matching sign. I independently checked the stated cancellation in the confluent limit. Multiplying the links telescopes to C_n/V(y). The packed initial top row forces the unique packed lower rows, so the initial-law hypothesis of Proposition 2.22 holds. Choosing its top-row interval [0,t] and subsequent intervals of length zero supplies the simultaneous-time array law. The resulting full-array mass has one Vandermonde factor, exactly as in (3), rather than the two factors in the top-row mass. Finite total clock rate establishes nonexplosion and the probability-law interpretation. Thus the summability used later is justified.

**Array inequality, lines 67–92.** I re-derived each factor inequality. Interlacing and nonnegativity are coordinate comparisons, preserved by both componentwise floor and ceiling. For the factorial factor, the product formula in line 73 is correct and proves r!s! <= a!b!. Integer shifts commute with rounding. For a Vandermonde difference, rounding subtraction cannot simply be interchanged, but the argument actually used is valid: r+s=a+b and |r-s|<=1. The identity rs-ab=((a-b)^2-(r-s)^2)/4, together with parity, proves ab<=rs. Positivity of the differences follows from the partition order and the shift j-i. The time factors cancel because the two rounded top-row sums have the same total as the endpoints. Invalid endpoints give zero on the left, so the extension to all integer arrays is valid.

**Marginalization, lines 96–108.** I independently downloaded arXiv:1911.04392v4. HKS Theorem 1.2 on PDF page 1 is exactly the four-function sum inequality quoted in the attempt, in arbitrary lattice dimension, with componentwise floor and ceiling. At parameter 1/2, the four slices defined in lines 98–100 satisfy its premise for every pair of hidden-coordinate vectors. It therefore proves (8) for the entire joint TASEP vector, not merely individual one-dimensional marginals. Coordinate permutation commutes with rounding. The common-box truncation argument is valid if desired; its support is closed under the two midpoint operations. The n=1 case needs no sum theorem. Translation back to X and the separate point-mass argument at t=0 are correct.

These checks establish the proof using BF and HKS as published theorem inputs. No step requires a conjectural preservation principle for arbitrary linear projections.

## Independent computations

I wrote new audit programs rather than executing the claimant's programs. The computations corroborate the general proof; they are not substitutes for it.

- `identities_audit.py` / `identity_results.json`: exact rational checks of 381 Poisson/falling-factorial determinants at t=3/2, with n=1 through 5; 372 interlacing-link normalizations by explicit summation; 2,601 factorial balancing pairs; and 26,244 difference-balancing cases including signed coordinates and integer shifts. Every check passed.
- `check_audit.py` / `check_results.json`: exhaustive exact rational array midpoint checks on (n, top-coordinate cap) = (1,8), (2,7), (3,4), (4,2), (5,1). There are respectively 9, 120, 294, 126 and 32 arrays, and 59,199 unordered endpoint pairs in total, including equal endpoints. Every rounded array remained legal and every inequality held. The n=2 and n=3 sets contain the claimant's respective cap-6 and cap-3 sets; the n=4 set is the same cap-2 set.
- In the same script I independently constructed the push/block generator on these 581 arrays and checked the exact coefficient identities in the forward equation for e^(-nt)c(A)t^|A^n|. For incoming transitions preserving the top-row sum, the coefficient is (q(A)-n)c(A); for transitions increasing that sum by one, it is |A^n|c(A). All identities passed. Outgoing boundary transitions were included in q(A); incoming transitions cannot originate beyond the coordinate cap because coordinates only increase. This is an additional check of the proposed law, independent of its determinant derivation.
- Independent 65-digit TASEP uniformization at n=3,t=1/2, through 130 terms, was compared with explicit array marginal sums through top coordinate 40 for all six states in ATTEMPT.md line 127. Relative discrepancies range from about 3.4e-61 to 3.3e-56, reproducing the reported scale and probabilities. These computations remain numerical, not interval certificates.
- `tail_audit.py` / `tail_results.json`: independent 85-digit uniformization through 140 terms reproduces all three tail ratios in line 117 and CLAIMS.jsonl entry 3: 1.03439448732283665, 1.08311332726795745, and 1.13923160896743232. The corresponding analytic absolute Poisson-tail bounds are approximately 7.72e-161, 5.04e-178 and 7.14e-137. Coordinate caps cannot lose paths returning to any tested target, since coordinates never decrease. Floating-point arithmetic is still not interval-certified. These are compelling checks, correctly described by the claimant as numerical evidence.

I inspected Midpoint.lean and lean_check_2.txt. The file contains the three stated integer lemmas, and the recorded output lists no sorryAx. I did not independently rerun Lean and do not treat that log as independent formal certification. Neither the claimant nor this audit has formalized the full stochastic proof. The published-theorem-and-algebra proof above stands independently of the Lean artifact. I did not re-evaluate every raw double-precision search output; those outputs are not used as proof.

## Fresh bounded literature check

`fetch_audit.py` and `fetch_results.json` record independent downloads of BF, HKS, the workshop source and Baslingker–Krishnapur–Madiman, arXiv:2412.15116. I checked the latter's Theorem 5 on PDF page 7 and Result 6 / Corollary 4 on page 9. Its quoted Schur theorem concerns one-dimensional marginals; its coordinate-marginalization result supports the method but is not an explicit theorem on the TASEP configuration vector.

A fresh arXiv API search for `all:TASEP AND (all:concavity OR all:"log-concave")` returned zero records, saved in `arxiv.response`. A fresh OpenAlex search for `TASEP log concavity` returned HTTP 429, recorded explicitly. I found no earlier exact-target theorem or known counterexample in the inspected material. This limited search does not establish novelty or absence of other literature. The verdict concerns mathematical correctness and completeness for the stipulated problem, not certified priority.

The all-n, all-time integral-midpoint assertion, and the explicitly defined stronger rounded-midpoint assertion, are proved by the submitted argument using the verified published inputs. No substantive repair is needed.
