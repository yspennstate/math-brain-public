VERDICT: PASS

# Independent hostile audit of G0002

Date: 2026-10-11. Read-only claimant folder: `~/brain_workers/TRIO_1011/op/G0002`. I read STATUS.md, ATTEMPT.md, CLAIMS.jsonl, and LITERATURE.md. All audit writes are confined to this audit folder. No claimant code was executed, no built-in web search was used, and no image tools were used.

## Exact claim and scope

ATTEMPT.md, sections 1 and 7, claims a **refutation** of Conjecture 53.1, for both objectives. At the particular integer dimension n=10^14, every increasing global maximizer of either phi_2 or phi_{2\1} violates at least one of the two proposed inclusions. It does not claim a positive proof of the conjecture, identify the maximizing family, or materialize a gigantic truth table. A finite existential counterexample suffices to refute the universal conjecture.

The argument constructs a finite distribution of increasing CNF events with r=10^6 samples per clause and M=2^r independent clauses. It proves that some fixed event has normalized phi_{2\1} at least n/259200, whereas every event satisfying both proposed inclusions has either normalized objective at most 10 sqrt(n). Since phi_2 dominates phi_{2\1}, this separates both global maxima from all events in the band.

This answers the source's conjecture with the correct quantifiers. Finiteness guarantees existence of a global maximizer; neither construction nor identification of that maximizer is necessary.

## Definition and source issues

1. **Task shorthand differs from the source; the claimant's correction is justified.** ATTEMPT.md section 1 sums over w in A, rather than all configurations. I independently downloaded the 708-page source from https://arxiv.org/pdf/2608.23661 and inspected pages 269, 373, 391, 394, 398, and 453. Formulas (51.1), (52.1), and the restatement on page 398 explicitly use sums over omega in A. Conjecture 53.1 is on PDF page 398, not the supplied locator 407. Thus the proof addresses the source problem; an independently defined objective summing over the whole cube is not the objective being certified here.

2. **Literal definition versus tables is a real source inconsistency, not a gap in this refutation.** ATTEMPT.md section 1 correctly notes that (49.1) constrains the coordinates deleted before testing pivotality, but does not constrain the tested coordinate to be initially occupied. For OR on two coordinates, direct application gives phi_2=6, whereas source Table 5 gives 4. The latter corresponds to restricting counted pivots to occupied coordinates. The lower bound uses only occupied pivotal witnesses and the upper bound uses the total coordinate count n, so the proof applies to both readings without relying on the tables.

3. **Minor citation typo.** ATTEMPT.md section 1 refers to P^+ “from (39.2).” The pivotal definition is **Definition 39.2**, on page 269; equation (39.2), on page 268, is a derivative identity. This is a locator issue only and has no mathematical consequence.

No substantive failing step or missing hypothesis was found.

## Step-by-step mathematical verification

**Section 2, (B1)-(B3): band bound.** Put n=2d. If |w|>=d+3, deleting up to one occupied coordinate and then setting any tested coordinate to zero still leaves at least d+1 coordinates occupied. Every such configuration belongs to A, so no second positive pivot can exist. Configurations counted in A have size at least d-2. There are therefore at most five contributing levels, d-2 through d+2. Each has at most binom(2d,d) configurations and each contributes at most n coordinates. This proves (B1) under both pivotal readings. The central-binomial ratio is (2d+1)/(2d+2), and the squared induction inequality has exact slack 3d+2. Consequently b_d<=1/sqrt(d+1)<=2/sqrt(n), proving the common bound 10 sqrt(n). I also checked the squared binomial inequality exactly for d=0,...,1000 and directly checked pivotal support for every monotone band family at n=2 and n=4 (5 and 114 families respectively).

**Section 3, construction and (E1)-(E4).** Every CNF event is increasing, including clauses with repeated samples. For fixed support size s, a clause fails with probability q_0=z^r, where z=1-s/n. Conditioning on all clauses succeeding factors into independent single-clause success conditioning. The geometric-series estimate in (E1) follows from binom(k,j)<=k^j. Bernoulli's inequality gives the lower bound in (E2), since r(2/h)=1/5. The stronger base in (E3) satisfies r(2/h+2/n)=1/5+1/(5h)<1/4. These yield Mq_0<=2 and q_0<=1/2. Integrating 1/(1-u)<=2 proves log(1-u)>=-2u; hence success probability is at least e^-4>1/81. The elementary e<3 argument is valid. All central-range conditions hold at the stated integers, including (s-1)/n>=1/3.

**Section 4, (G1): pivotal certificate.** First pivots are precisely coordinates that are the sole distinct positive coordinate of at least one clause. This definition includes repeated occurrences. A selected edge clause has two positive sample positions with distinct values i,j. If neither endpoint is a first pivot, deleting j alone preserves every clause, but deleting i and j kills the selected clause. Thus i is pivotal after deleting j and was not first-order initially. Covered vertices outside bad-edge endpoints therefore belong to P_2^+ minus P_1^+. The union of endpoints of B bad edge instances has size at most 2B; multiplicity does not invalidate the inequality. My independent enumeration of all 729 clause arrays with n=3,r=2,M=3 checked the direct literal pivotal definition against this certificate on all 2640 successful array/support pairs. Every check passed.

**Section 5, (C1)-(C3): coverage.** Choosing two positive positions, assigning i to one and one of s-1 other coordinates to the other, gives a_i=r(r-1)(s-1)z^(r-2)/n^2. The position cases are disjoint. Conditional edge-incidence probability is t_i=a_i/(1-q_0). Multiplication by M=2^r produces the factor 4 in (C2). The lower bound is (8/15)r^2/n>=r^2/(2n); the upper bound is (32/3)r^2/n<1 because r^2/n=1/100. Conditional clause independence permits the first two inclusion-exclusion terms. They imply coverage probability at least Mt_i/2>=r^2/(4n). Summing over s>=n/3 gives r^2/12. No independence between vertex indicators is required.

**Section 6, (D1)-(D3): contamination.** The exact singleton-at-i probability is (z+1/n)^r-z^r, and its derivative/geometric bound includes every positive repetition. Singleton events for different i are disjoint. The exact edge probability is binom(r,2)s(s-1)z^(r-2)/n^2. Independent single-clause enumeration for n=2,...,5, r=2,...,4, and every s=1,...,n confirmed both identities and the incidence identity (C1), using rational arithmetic. Conditioning costs at most a factor two. The bounds MQ_S<6r and MQ_E<4r^2 follow with the stated constants. An edge clause cannot itself be a singleton clause; each other conditioned clause has singleton probability Q_S/s at a specified endpoint by symmetry. A union bound gives E(B | success)<=144r^3/n. No unjustified independence of singleton and edge indicators is asserted. Subtracting twice this quantity proves (D3), since n>=6912r. Its exact slack after weakening to r^2/24 is 124991360000/3>0.

**Section 7, (R1) and extremal conclusion.** A uniform support has size variance n/4, so Chebyshev gives central-range probability at least 3/4 when h^2=n. For every central fixed support, multiply the success bound 1/81 by the conditional pivotal lower bound r^2/24; contributions elsewhere are nonnegative. Finite averaging gives normalized expected phi_{2\1} at least r^2/2592=n/259200. Thus some fixed increasing event achieves this lower bound. The exact comparison is

    r^2/2592 = 31250000000/81,
    10 sqrt(n) = 100000000,
    difference = 23150000000/81 > 0.

These values were independently checked with Python Fraction. Maximization of either objective then gives at least this value, while every band event satisfies the smaller upper bound. This proves the asserted failure for every global maximizer of both objectives at the stated dimension. All spaces and sums are finite; no limiting approximation or asymptotic error remains.

## Literature check and limits

I fetched the source abstract and PDF afresh, using Python urllib only. The freshly fetched PDF's relevant pages matched the cached PDF when independently extracted with PyMuPDF. The source's Section 62 already gives the random-CNF lead; page 453 states a probability lower bound of linear scale, while the displayed Proposition 62.1 lacks the corresponding 2^n normalization factor. I do not certify its proof or count that printed proposition as an exact prior resolution. The claimant supplies its own finite proof of the needed stronger normalized lower bound, including phi_{2\1}.

A fresh arXiv API search for “second order” and “pivotal,” first ten results, returned unrelated papers; titles and identifiers were inspected. A fresh OpenAlex query for “second order pivotal Cerf” returned HTTP 429. This is a bounded literature check, not evidence of exhaustive novelty. Nothing retrieved contradicts the independently checked argument.

Reproducible independent checks are in `independent_check.py`, `band_check.py`, and `source_check.py` in this folder; each completed with exit code 0. The source PDF and successful HTTP responses are also retained here. I did not rerun the claimant's Lean certificate and do not rely on its claimed formalization. The proof certified here is the complete finite mathematical argument in ATTEMPT.md, supported by independently written exact computations. It is not a fully machine-formalized theorem and does not determine the smallest counterexample dimension or an explicit maximizing truth table.
