# FEIB25 report

The brief is complete. FEI is not solved. The main result is a proved obstruction to the proposed level-local approach: for every fixed d≥1, A_d cannot be bounded by any dimension-independent finite linear combination of W_0,...,W_d. Adding more lower levels cannot repair L1 or L2.

The construction and all proofs are in PROOFS.md. Exact mathematical source statements and convention notes are in PAPER.md. The full data and commands are described in REPRODUCE.md.

## What is proved

Let m=2r+1, b=binom(2r,r)/4^r, and let h(z,y) equal 1 when z=1 and majority_m(y) when z=−1. Multiply h by parity on d−1 independent fresh variables. Direct Fourier expansion gives

    W_{d−1}=1/4,
    W_d=(1+m b²)/4,
    A_d=1/4+(m b²/4)log2(1+1/b²),
    I=d−1/2+m b/2.

The elementary induction 1/(4r)≤b²≤1/(r+1) gives A_d≥1/4+(1/8)log2(r+2), which diverges while all W_0,...,W_d remain bounded. This is a Boolean counterexample to every fixed lower-level-only linear bound. Its influence grows with m, so it does not contradict FEI. No claim of novelty is made.

I also proved the following elementary low-level inequalities:

    A_1 ≤ √W_0 I/ln 2,
    A_2 ≤ (I²−Σ_i Inf_i²)/ln 2 ≤ (I²−W_1)/ln 2.

The second uses |f̂(S)|≤Inf_i for i∈S, which follows from the Boolean derivative taking values in {−1,0,1}. It cannot follow from ordinary hypercontractivity alone: a normalized real degree-two polynomial with W_1=W_2=1/2 has A_2=log2((n+1)/2) and I=3/2. The quadratic I term is a real limitation; a short linear-I proof remains open here.

For arbitrary spectral probability distributions, the exact adjacent-mass Jensen bound is

    A_d ≤ dW_d log2(1+(n−d+1)W_{d−1}/(dW_d)).

Uniform mass within each adjacent level makes it an equality. This explains why probability-level reasoning alone cannot remove the dimension factor.

## Exhaustive calculations and searches

I regenerated the NPN representatives locally, rather than assuming the earlier files were exhaustive. The generator marks complete NPN orbits; a separate Burnside calculation confirms their counts. The generated files also match the earlier FEIB13 files byte for byte. Sources: npn.cpp, npn5.log, coverage_audit.json, census_summary.json.

| Variables | NPN classes | Largest L1 ratio, d≥2 |
|---:|---:|---:|
| 1 | 2 | no such level |
| 2 | 4 | 0.500000000000 |
| 3 | 14 | 0.666666666667 |
| 4 | 222 | 0.830482023722 |
| 5 | 616126 | 1.160964047444 |

At five variables the L1 maximum occurs at d=2, truth table 0x71356, where A_2=(5/16)log2(5) and 2W_2+W_1=5/8. Its twenty nonzero edge terms each have upper mass 1/64 and lower/upper ratio 4; this was independently reconstructed from the truth table. L2 with equal coefficients has the same maximum. Even denominator dW_d+Σ_{k<d}W_k reaches ratio 1.1326478511645668 (census_summary.json).

All requested A_d, dW_d and (d−1)W_{d−1} are saved for every representative in census_n*.npz, with exact integer W numerators over 4^n. The A/E arrays are binary64 evaluations of logarithms of exact dyadic masses, not symbolic exact real numbers. The truth tables permit reconstruction of every edge summand.

Beyond the census, the data contain 91 truth-table family instances: majority, tribes, address, bent, random functions, hidden-coordinate functions, and threshold/selector constructions. The largest truth-table dimension is 20, for the four-address-bit function. Search ran through n=16 with fixed seed, single/double flips and three starts for each objective. It stored 30 best-function witnesses. Its largest n=16 L1 and L2 ratios were respectively 1.7369482829826224 and 1.7375990459866377 (families.json, hill.json, hill_n*.npz). These are short-search findings, not maxima above n=5.

The ordinary disjoint-block perfect-matching K33 towers were computed by the proved spectral composition recurrence. Their sizes and ratios are:

| Tower depth | Variables | G/I, bits per influence unit | Largest L1 ratio |
|---:|---:|---:|---:|
| 1 | 9 | 1.673279240157 | 1.600200549260 |
| 2 | 81 | 2.811821689664 | 2.675423656044 |
| 3 | 729 | 3.173804996308 | 3.397527404105 |
| 4 | 6561 | 3.228290742787 | 3.891790410901 |

All these L1 maxima occur at d=2. Source: towers_decimal_50.json. These are exact algebraic recurrences evaluated numerically, not large truth-table enumerations. The initial binary64 tower file underflowed in extremely small tails and is retained only as a superseded diagnostic. The primary full tower profiles use Decimal arithmetic and preserve every level, including the smallest positive mass of approximately 3.06518639018628×10^−3950. The 40- and 50-digit calculations differ by at most 1.73513147368429×10^−37 relatively at any W/A coefficient; mass error is at most 10^−50 (tower_precision_audit.json).

Complete analytic selector-majority profiles are saved at n=1024,1025,1026. The targeted formula was checked against full truth tables through m=13. At m=65535 the parity-times-selector construction has A_2=2.9001851134665304 bits and I=103.62883419143917 (selector_majority.json). Full family/tower/search level tables are in level_profiles.csv.gz.

The tested tail-payment candidate

    A_d ≤ dW_d+(d−1)W_{d−1}+Σ_{k>d}kW_k,    d≥2,

survives every saved profile, with largest observed ratio 0.7817865759096007 at PM_K33, d=2 (numerical_summary.json). It is CHECKED NUMERICALLY, not proved. Summing it over d would count the same tail mass repeatedly. The finite tests do not establish the weakest sufficient tail weights; the proof above establishes that no lower-level-only weights suffice.

## The paper and the logarithm

I opened [arXiv:1911.10579v2](https://arxiv.org/html/1911.10579) and transcribed Theorems 1.1–1.3 and 6.6, Lemmas 2.7 and 3.5, and Corollary 6.7 in PAPER.md. The [journal page](https://link.springer.com/article/10.1007/s00039-020-00544-2) and direct PDF URL expose only subscription-preview content; I cannot compare its theorem statements or numbering with the preprint.

Theorem 1.3 includes an additive K I[F], uses natural logarithms, and concerns {0,1}-valued functions. The paper also changes its influence normalization after the introduction. PROOFS.md converts all of this explicitly to the brief's convention.

The full deduction of Σ_i E_i≤C E[|U|log2(|U|+1)] is written from Corollary 6.7, including coefficient bins, their mass bounds, entropy summation, isoperimetry, normalization conversion and Han's inequality. I have not independently reproduced the paper's entire technical induction. The log-bearing inequality is the factor δ^{-10^5 d} with δ required to be polynomially small in d. Compensating for it requires an exp(−C d log d) coefficient cutoff.

Corollary 6.7's displayed statement uses δ^{1/16}, while its proof displays δ^{1/32} at the corresponding estimate. The deduction here uses the weaker exponent, which is sufficient either way. Lemma 2.7 also has a displayed restriction-domain mismatch; its proof fixes the intended domain. Both observations are recorded without silently changing the source.

Non-Boolean adjacent-layer spectra really have edge cost of order d log d at influence of order d. I have not identified a Boolean family that saturates the global logarithmic loss, and cannot conclude that only non-Boolean spectra cause it. Individual Boolean coefficients can reach the cutoff scale without making the total bound sharp.

## Verification, resources and remaining work

The initial independent checks compared Walsh transforms with direct character sums and A_d with direct edge enumeration on 96 cases; maximum absolute discrepancy was 7.771561172376096×10^−16 (audit.json). A small biased composition checked the tower recurrence against a full truth table to 2.7755575615628914×10^−17 (tower_audit.json).

The final audit rechecked all 616368 representatives across n≤5 using truth-table pivotal influences, the two proved low-level inequalities, Han's inequality and the erasure sandwich. It found no inequality violation at tolerance 10^−11. Identity/NPN-invariance discrepancy was at most 1.1102230246251565×10^−16; all 30 hill witnesses reproduced exactly (final_audit.json). These are independent calculations by this worker, not an external referee review.

All numerical Python processes used one numerical thread and inherited nice 10. The largest measured truth-table case used 513376256 resident bytes, and the generator's visited bitset is 268435456 bytes (resources.json). The final disk record is in workspace_audit.json; the folder stays below the brief's 200 MB limit. No subagents were started; no shared files, mesh, fleet board, unrelated systems or external publishing endpoints were changed.

Brain recall helped orient the work to FLOW's erasure equivalence. The math-recall command reported that no math store was installed. Shared brain/checklist writes were deliberately omitted under the fleet's folder-only rule. This report and RESULTS.md are the handoff for the launching session.

The remaining mathematical questions are global log removal, a linear-I elementary A_2 estimate, a tail-payment rule that does not reuse mass, and Boolean sharpness of the paper's degree logarithm. The one-page assessment and the precise next lemma to try are the final section of PROOFS.md. Journal-body comparison remains inaccessible through the available view.

Task: “solve the Fourier Entropy-Influence conjecture” — the author's 9 Nov 2026, 22:20 ask; worker brief “the edge form of FEI level by level.”
