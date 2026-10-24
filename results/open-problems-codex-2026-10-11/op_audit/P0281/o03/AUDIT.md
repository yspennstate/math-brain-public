VERDICT: PASS_WITH_GAPS

Audit date: 2026-10-12. The mathematical result stands after one small correction: ATTEMPT.md line 31 gives the wrong index in its explanation of the coordinate change. I found no substantive failure in the probability representation, midpoint inequality, or marginalization argument. This verdict does not certify novelty.

## Exactly what is claimed

ATTEMPT.md lines 7–11 and CLAIMS.jsonl claim that for every finite n >= 1, every t >= 0, and every a,b in Z^n, rate-one continuous-time TASEP started at X_i(0) = -i (rightmost particle first), with transition mass extended by zero, satisfies

    p_t(a) p_t(b) <= p_t(floor((a+b)/2)) p_t(ceil((a+b)/2)).

Floor and ceiling act coordinatewise. When the midpoint is integral, this is precisely the requested inequality with the square of the midpoint mass on the right. Thus this is an all-n, all-time answer to the finite-particle problem stipulated in the audit request, rather than a special case. The stronger rounded assertion is explicitly defined. The argument makes no claim about a real-variable extension, unequal jump rates, arbitrary initial conditions, or arbitrary linear projections.

I independently downloaded the workshop PDF. Section 3, PDF page 2, asks about the step-TASEP transition mass and defines log concavity using the midpoint inequality. The original paragraph does not explicitly specify finite n or a rounding convention; the claim answers the finite-n, integral-midpoint interpretation expressly stipulated here. I did not locate or verify the separately mentioned follow-up Q2.

## Issue requiring a small correction

**ATTEMPT.md line 31, Section 1:** “substitute k=m-i” is incorrect. For the coordinate map on line 27, the relevant index is **k=m-i+1** in the displayed raw-coordinate interlacing relation. For example, m=i=1 makes the printed substitution k=0, which is not a particle index. Naming this index correction is the only required fix.

Why it matters: the printed substitution does not establish (2). However, the coordinate map itself, the inequalities in (2), the zero initial condition, and the identification D_m=lambda_m^m are all correct. Independent substitution with the proper index verifies both inequalities. No formula, probability law, or subsequent estimate needs to change. This is an explanatory indexing error, not a counterexample to the claimed theorem.

## Independent verification of the proof

**Established inputs, lines 15–23.** I fetched the actual PDFs of Borodin–Ferrari (BF), arXiv:0804.3035, and Halikias–Klartag–Slomka (HKS), arXiv:1911.04392v4, rather than relying on the claimant's summaries. BF Section 1.1, PDF pages 3–4, specifies the packed initial array, independent rate-one clocks, blocking, and diagonal pushing. BF (2.94), (2.95), (2.101), and Proposition 2.22 give the links, row transition kernel, and Gibbs evolution used here. HKS Theorem 1.2 on PDF page 1 has exactly the four-functions floor/ceiling inequality needed at parameter 1/2; it applies on Z^r, not just the Boolean cube. These citations support the uses made of them.

**Coordinate representation and support, lines 27–38.** With the index correction above, the raw strict/weak interlacing becomes weak partition interlacing, because the one-unit coordinate shift absorbs the strict integer inequality. The initial array becomes zero. The coordinate lambda_m^m is z_1^m+m, so the TASEP displacement vector is an actual coordinate selection from the array. Nonnegativity follows from the initial condition and rightward moves. The quantities l_i=lambda_i+n-i are nonnegative and strictly decreasing. I checked the coordinate conversion in both directions independently.

**Top-row determinant, lines 40–50.** The equal-alpha alternant ratio is V(y)/V(a); the common leading confluent factors cancel. For the packed row, V(a)=product_{j=1}^{n-1} j!. The kernel in BF (2.101), after transposing the determinant if necessary, is the stated Poisson kernel. Since y_j-a_i=L_j-(i-1), extracting the column and row factors leaves monic falling-factorial polynomials. Their determinant is V(L), including cases where a kernel entry vanishes. The total time exponent is sum L_j-n(n-1)/2=|lambda|. There is no sign or factorial-shift error in (4) or (5).

**Links and full-array mass, lines 52–61.** BF's link definition on PDF pages 24 and 36 and Lemma 2.13(ii), (2.57), on PDF page 26 confirm the strict/weak support and the sign of its step-function determinant. I checked the confluent expansion in line 57: its two factors of (-1)^(m-1) cancel, leaving the positive normalized link (m-1)! V(v)/V(u). The product of links telescopes to C_n/V(y). The packed top row permits only the packed lower rows. Proposition 2.22 can therefore be used with the top level evolved to t and all lower levels sampled at the same t, yielding (3). Two Vandermondes occur in the top-row mass, and exactly one is cancelled by the links. Finite total clock rate gives nonexplosion and total probability one. The argument does not assume normalization of an unproved formal series.

**TASEP projection, line 63.** A left-edge coordinate has its own rate-one right-jump clock and is blocked exactly when its site is immediately behind the preceding edge particle. A diagonal push always increases the particle index, so an incoming push cannot reach index 1. Its generator is consequently the n-particle TASEP generator. The bounded total jump rate ensures uniqueness. This confirms that the law being marginalized is the required joint configuration law, not a top-row ensemble or PushASEP law.

**Array midpoint inequality, lines 67–92.** Every support constraint is a coordinate comparison or nonnegativity constraint, and is preserved by floor and ceiling. The factorial ratio in line 73 is correct, with the inequality in the direction required for reciprocal factorials. For each Vandermonde factor, r+s=a+b and |r-s|<=1. Hence the rounded pair is balanced, and the identity in line 84 gives rs>=ab in both parity cases. This argument correctly handles rounding differences without assuming that subtraction commutes with floor. Integer shifts commute with rounding, and the powers of t cancel because the top-row sums add. Multiplying these positive factor inequalities proves (7). Invalid endpoints give a zero left side.

**Marginalization and boundary cases, lines 96–108.** Permuting coordinates and selecting the diagonal commute with componentwise rounding. Substituting the four slices into HKS gives exactly (8). Their sums are finite because the array law is a probability measure. The alternative common-box truncation argument also works: both rounded midpoints remain in the box whenever both endpoints do. For n=1 the hidden dimension is zero and marginalization is unnecessary. Translating by the integer vector (1,...,n) preserves rounding. At t=0 the point-mass argument is valid. Thus no positive-time or dimensional boundary case is omitted.

## Independently written exact computations

I wrote and ran check_audit.py in this audit folder; I did not execute the claimant's verification scripts. All arithmetic in the following checks is integer, rational, or symbolic. Results are saved in independent_checks.json.

* Array midpoint products: 58,717 pairs, including equal endpoints, for n=1,2,3,4 with largest top coordinate bounded respectively by 12,7,4,2. Every rounded array remained legal and every inequality passed.
* Array master equation: 553 states at each of t=1/2,1,2, giving 1,659 exact identities. The generator was built separately from BF's raw-coordinate blocking and pushing rules. Outgoing moves beyond the coordinate cutoff were included; no predecessor is lost because all coordinates move only right. With the common exponential removed, the derivative equals (|lambda|/t-n) times the weight. Every identity passed.
* Edge representation: 459 exact coefficient comparisons between the array marginal and independently generated TASEP. I compared coefficients of e^(nt) p_t through degrees 12,10,8,6 for n=1,2,3,4. The TASEP coefficients come from powers of Q+nI divided by k!. Arrays with top-row sum k give exactly the coefficient of t^k, so these checks have no numerical tail error. All coefficients agreed.
* Normalization: the corresponding 40 degree coefficients of the total array weight were exactly n^k/k!, as required for exp(nt).
* Determinant identity (5): 627 exact symbolic determinant checks for n<=4, top coordinate <=5, and t=1/2,1,3/2; all passed.
* Equal-alpha links: 246 exact normalization checks for row sizes 2 through 5 and top coordinate <=4; all summed to one.
* Marginal midpoint products: 1,507 exact inequalities for the edge marginals of the four finite array boxes; all passed. These are truncated-marginal checks, not assertions that a finite box equals the full TASEP law.

These finite checks corroborate the analytic proof; they do not establish its unrestricted quantifiers by enumeration. Those quantifiers follow from the checked algebra and the established BF and HKS theorems. I did not independently rerun the claimant's Lean file or its floating-point and high-precision tail scripts. None is needed for the mathematical conclusion. In particular, ATTEMPT.md lines 117–119 and 127 correctly distinguish numerical evidence and partial formalization from a proof of the full theorem.

## Bounded independent literature search and limits

Using Python urllib only, I fetched the workshop source, BF, HKS, and Baslingker–Krishnapur–Madiman (BKM), arXiv:2412.15116. Copies and extracted text are confined to this folder. The arXiv API query `all:TASEP AND (all:concavity OR all:"log concave")` returned totalResults=0. The independent OpenAlex query `TASEP log concavity` returned HTTP 429. URLs and outcomes are recorded in fetch_log.json; the arXiv response is preserved in arxiv_search.xml. This is a bounded search, and the failed OpenAlex request is not evidence of absence.

BKM Theorem 5, PDF page 7, concerns one-dimensional marginals of Schur measures. Result 6 and Corollary 4, PDF page 9, confirm the HKS marginalization mechanism. I found no statement there settling the exact joint TASEP configuration question; a text search found no TASEP occurrence. BF and HKS supply ingredients, not an already stated solution to this question. No earlier exact solution or known counterexample was identified in the sources inspected. Novelty and exhaustive literature coverage remain unproved.

After the single index correction at ATTEMPT.md line 31, the claimed rounded-midpoint theorem, and therefore the requested finite-particle integral-midpoint log concavity, are proved using the cited established inputs. A real-variable extension, other initial conditions, and complete formal verification are not proved here.
