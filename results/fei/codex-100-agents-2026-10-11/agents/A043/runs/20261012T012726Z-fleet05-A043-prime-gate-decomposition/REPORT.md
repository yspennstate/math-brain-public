# A043 stage 2: certified biased-prime grid and a missed prime endpoint

## exact target, quantifiers, hypotheses and units

The B09 lead assigned the largest corrected ratio Hplus_mu(g)/delta_mu(g), delta=I_mu-Var_mu, over essential primes of arity at most four under product biases, starting with a discovery grid and then exact certification. This stage closes one explicitly finite grid and a nonbinary boundary obstruction; it does not close the supremum over all interior product laws. Constants and literals have zero deficit and are outside the ratio domain. Entropy is in bits; influence is spectral influence in the normalized product basis.

For every essential prime g of arity n=2,3,4 and every independent bias vector with coordinates in {1/4,1/2,3/4}, the exact largest ratio is

    M_grid = 26-12 log2(3).

It is attained by sign OR_2 at probabilities (1/4,1/4), up to the input/output symmetries of the grid. A canonical table encodes +1 at assignments 1,2,3 and -1 at assignment 0: mask 14. The exact certificate encloses M_grid between 29278127/4194304 and 14639065/2097152. It certifies all 4,639,338 labeled prime/bias cases through an exact quotient of 458,356 representatives. The n=3 and n=4 grid maxima are rigorously below the binary winner; their discovered values are approximately 5.45473576 and 6.37956699. Those last decimals are discovery summaries, not all-bias bounds.

On a fixed three-input prime, majority_3, the interior path with probabilities (1-q^3,q,q) satisfies

    lim_{q->0} Hplus_mu(majority_3)/delta_mu(majority_3)=2+4/ln(2).

At q=1/8 its ratio lies in [73411827299/10000000000,734118273/100000000], hence exceeds 7. This disproves a hypothetical all-bias bound Hplus<=7 delta even when restricted to nonbinary primes of arity three or four. It is a finite strong-helper counterexample, not a disproof of ordinary uniform FEI or an unbounded ratio family. The curve is bounded in the displayed limit. Full FEI remains OPEN.

## sources actually read, revisions and theorem locators

At the start of this stage read BOARD.md, own STATUS.md and LEARNED.md, and claude/B09/STREAM_NOTES.md v2, dated 2026-10-11 23:33 UTC. The notes explicitly assign the n<=4 prime/bias grid to A043, prohibit repeating the one-bit tax, and state the B09 pending-review cap. This is the requested finite verification and endpoint scope repair, not a new broad universal conjecture. The speculative approximation direction mentioned before the notes returned was not pursued; no result is claimed for it.

EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2 was read in full again. Stage 1 REPORT.md, PRIME_GATE_DEFINITION.tex, PRIME_ENDPOINT_IMPLICATION.md and main_census.json supply the precise class, two-row criterion and normalization. The updated board shows A091/A093 review of the earlier biased-block core, A042's binary endpoint work, and A044's common-mean addressing result. A042's stage-2 REPORT.md was read as available and cross-checked for the binary endpoint and scope; it partially reconstructs A043's prior analytic reduction, without accepting the bundled census. No A042 proof or unseen review record is a premise here. A044's original report path was inspected; its addressing theorem is not a dependency.

The original 38-page threshold paper Section 6.1 defines Hplus_mu and delta; Section 7 Proposition 7.1 gives the composition identities already reconstructed in stage 1. Those source bytes and locators remain pinned in that stage's out/source_manifest.json; no composition theorem is re-proved or claimed as new here. This stage's out/source_receipts.json pins the current protocol, board, lead notes, prior proof and relevant files actually loaded for the handoff.

## complete derivation or exact first unsupported line

### Exact domain and symmetry

Encode assignments by an integer x, with input bits Yi=(x>>i)&1 and signs Xi=2Yi-1. A table mask has bit x equal to 1 exactly when g(x)=+1. Output negation preserves every squared coefficient and the corrected ratio, so retain only masks with g(0)=-1. Input reflection Yi->1-Yi, together with p_i->1-p_i, changes signs of selected normalized characters but preserves all squared masses and input variances. It also preserves the cofactor-row prime property. Since every table of the prime family is included, biases 3/4 may therefore be represented by 1/4; keep {1/4,1/2} in each coordinate. No variable-permutation quotient or unverified orbit list is used.

The exact vectorized cofactor criterion removes all nonessential functions and then every proper block with at most two distinct rows. It returns 5,52,28620 output-negation representatives of primes on n=2,3,4, respectively, agreeing with the stage-1 exhaustive tuple census. The checked family covers 5*4+52*8+28620*16=458356 representative gate/bias pairs. Restoring all labeled tables and grid biases gives 10*9+104*27+57240*81=4639338 cases. Reflection need not act freely; this is a surjective maximum-preserving representation, not an orbit-count assertion.

### Rational biased Fourier spectra

For a reduced bias vector let b coordinates have probability 1/4 and u=n-b have probability 1/2. D=4^b 2^u is a power of two. On a biased coordinate use integer probability weight 1 for Y=1 and 3 for Y=0, and centered numerator t=4Y-1=2X+1. Its normalized character is t/sqrt(3). On a uniform coordinate use probability weight 1 and character X. Let W(x) be the product of the integer probability weights. For a Fourier set S define the exact integer moment

    N_S = sum_x g(x) W(x)
          product_{i in S, biased}(4Y_i-1)
          product_{i in S, uniform}(2Y_i-1).

If k=|S intersect biased|, the squared coefficient is P_S=N_S^2/(D^2 3^k), while sigma_S^2=(3/4)^k. Thus

    log2(sigma_S^2/P_S)
       =2 log2 D-2k+2k log2 3-2 log2 |N_S|.

Zero N_S contributes zero. Put L=D^2 3^b and w_S=N_S^2 3^(b-k). All cases verify sum_S w_S=L exactly and have positive deficit numerator d=sum_{S nonempty}(|S|-1)w_S. The corrected ratio equals the corrected logarithmic numerator divided by d; the common L cancels.

The Boolean coefficient bound gives |N_S|<=D(3/2)^k<=1296 throughout this domain. A finite table of outward logarithm intervals therefore suffices. Neither irrational basis factors nor floating Fourier coefficients are used to prove signs.

### Certified logarithms and arithmetic bounds

For x in [1,2], z=(x-1)/(x+1) is in [0,1/3]. Use

    ln x = 2 sum_{j=0}^{31} z^(2j+1)/(2j+1) + R,
    0<=R<=2 z^65/[65(1-z^2)].

Version 2 encloses every power and product by floor/ceiling operations on integers scaled by Q=2^80. Squaring the nonnegative z interval and repeatedly multiplying it gives lower and upper bounds on each odd power; dividing by the positive odd denominator and rounding outward preserves bounds on the partial sum. The added upper tail is the exact integer ceiling of Q*2*9/(65*8*3^65). At x=1 the exact interval is [0,0]. These are rational interval operations, not floating approximations.

Normalize each integer a as a/2^floor(log2 a), apply the displayed logarithm series, divide its interval by the positive similarly obtained ln(2) interval, and add the integer part. Round outward at scale s=2^24. The saved table has width at most one integer unit for every a=1,...,1296. Use the upper log(3) and lower log(|N_S|) for the entropy upper bound, and the opposite endpoints for the lower bound. Parseval, positive deficit and both maximum comparisons are checked on every representative. A floating quotient may select an index for a per-bias maximum, but all comparisons against that index are subsequently verified by arbitrary-integer cross-products, so a wrong candidate could not pass the certificate.

The moments have absolute value at most 1296; powers and products used to form w_S fit in signed 64-bit arithmetic. L<=256^2*3^4=5308416. Verified Parseval bounds the sum of all weights by L, and the absolute logarithm bracket by 50s, so the entropy sum has absolute value at most 50sL<2^63. Ratio cross-products may exceed 64 bits and explicitly use Python arbitrary integers through object arrays. Final reported interval ratios use Fraction. This avoids silent integer overflow as well as numerical underflow.

### Exact winner

The winner's spectrum has empty mass 1/64, singleton masses 27/64 and 27/64, and pair mass 9/64. Its deficit is 9/64. Therefore

    Hplus=(27/32)log2(16/9)+9/32,
    Hplus/delta=26-12log2(3).

Every n=3 and n=4 per-bias upper certificate is strictly below the winner's exact lower enclosure. The final small checker independently compares all other 19 binary representatives with that lower enclosure. The canonical winner alone remains. This closes the exact grid maximum, rather than just bounding a discovered witness.

### Nonbinary boundary and the unsupported extension

MAJORITY_BOUNDARY.md gives the complete prime test, normalized derivative coefficients, rational spectrum and Taylor expansion for probabilities (1-q^3,q,q). In particular delta=4q^2+O(q^3) and Hplus=(8+16/ln(2))q^2+O(q^3); the other terms are O(q^4), O(q^5), or O(q^5 log(1/q)). The ratio limit is consequently 2+4/ln(2). All bias coordinates stay interior for q>0. The twelve dyadic points q=2^-k, k=1,...,12, independently reconstruct the spectrum from all eight physical assignments and check the closed masses exactly.

The first unsupported line toward the lead's full target would be extending this finite grid upper bound, or its winner, to arbitrary interior biases. That extension is false for the bound 7: the saved majority point at q=1/8 is already above 7. The continuous supremum on ternary/quaternary primes is not determined here, nor is a finite arity-uniform prime constant paid. No divergent family was found or proved; the displayed sequence has a finite proved limit. Its lower bound does not assert that the continuous supremum equals that limit.

## executed validation with domain, arithmetic, commands and outputs

All frozen specifications precede their computations and are saved in out/FROZEN_SPEC.json, FROZEN_CERTIFICATE_SPEC.json, FROZEN_CERTIFICATE_SPEC_V2.json, FROZEN_WINNER_SPEC.json and FROZEN_BOUNDARY_SPEC.json. Memory estimates are 20-80 MB, so no >300 MB job or memok invocation was needed. No GPU, dimension escalation or persistent background process was used.

Commands from this run directory:

    python -X utf8 code/biased_grid.py pilot
    python -X utf8 code/biased_grid.py main
    python -X utf8 code/certify_grid.py
    python -X utf8 code/verify_winner.py
    python -X utf8 code/certify_boundary.py

The pilot covers 436 representatives on n=2,3. Main discovery completed all 458356 representatives in 1.1958252000622451 computation seconds. It is evidence only. The initial Fraction-heavy logarithm implementation hit the 50-second cap; no all-grid certificate was inferred from that attempt. During the implementation repair an indentation error was caught and fixed before a certificate ran. Final certificate v2 completed all 28 bias vectors and all 458356 representatives in 2.3398401000304148 computation seconds. It verifies Parseval and positive deficit once each per case and two exact interval maximum comparisons per case, totaling 1,833,424 per-case checks, in addition to logarithm-table and classification checks. out/grid_certificate.json is complete and out/log_intervals.json saves the rational log table.

The exact winner checker passed 44 checks and saved out/exact_winner.json. The independent physical majority reconstruction passed 190 checks over twelve dyadic cases in 0.22530539997387677 computation seconds; out/boundary_certificate.json encloses every ratio by rational endpoints with decimal denominator 10^10. At k=12 the interval is [38850376613/5000000000,77700753227/10000000000]. This approaches the analytically proved limit but is not used to infer it.

All jobs stayed in the frozen dimensions and terminated. Startup/tool-host latency is separate from the computation seconds reported by the scripts. The certificate is an exhaustive finite result plus an analytic boundary proof, not evidence of independent reviewer acceptance. The new vectorized prime classifier agrees with the earlier distinct implementation; the boundary spectra are separately reconstructed by direct Fraction expectations rather than trusting the closed derivative formulas.

## proof dependencies and changed downstream conclusions

The prime definition and two-row criterion are the source-complete A043-DISJOINT-PRIME-ENDPOINT@1 analytic interface, with the previous exact counts as a cross-check. Elementary product Fourier normalization, integer arithmetic and the explicitly proved logarithm remainder complete the finite certificate. The majority prime test and boundary expansion are independently written in this run, so no A042 sharp-constant proof, B09 sharp-tax claim, or unreviewed addressing theorem is a prerequisite. No one-bit tax or AND endpoint theorem is recomputed.

The stage adds a finite-domain verification and a boundary guard for the already open all-prime endpoint. A042's binary endpoint cannot be discarded when looking only at nonbinary primes: a genuine ternary prime approaches the same lower constant. A044/A045 must retain highly unequal physical biases in any proposed prime or tax transport. A091/A090 receive exact finite coverage, an overflow-safe interval certificate, and the actual Boolean witness separating finite grid from all biases. The new result is bundled into one finite-verification claim and does not open another broad universal candidate while B09 is above the review cap.

## one next mathematical action and independent reviewer

Next action: classify the mixed-rate endpoint expansions of the finitely many ternary prime symmetry classes and identify any coefficient exceeding 2+4/ln(2), retaining the actual variance deficit. The majority path already shows why checking only moderate grid biases is insufficient, while an endpoint expansion can rule out or certify whole parameter regimes without a larger truth-table census. A091 is the primary independent reviewer, with A090 alternate; they should reconstruct the weighted-moment certificate and majority asymptotic using separate code or a separate coefficient representation. No message was sent and no other agent's folder was modified.

## actual persistence receipts or precise save blocker

The run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, the full boundary proof, five frozen specifications, code and complete exact outputs. Rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only under A043. out/schema_check.json checks the exact protocol field sets and packet-delta identity; out/receipts.json records local sizes and SHA256 hashes. No file exceeds 20 MB. Supervisor copy, remote-mirror verification, independent review and downstream mathematical use remain pending. No git, shared-index edit, brain write or unauthorized filesystem mutation occurred.

**Universal bridge:** This stage moves the B09 lead's all-prime corrected product-FEI+ target by certifying the complete n<=4 grid maximum 26-12log2(3) and proving that a genuine three-input prime approaches the larger lower constant 2+4/ln(2) on a mixed-rate boundary path. It bounds a finite domain and rules out a tempting constant-7 extension, but pays none of C018/C019/C020/C024's universal residuals and proves no finite all-arity prime constant. The remaining gap is the continuous prime ratio, especially unequal endpoint rates and then growing arity. NEXT targets analytic mixed-rate regimes of ternary prime classes because the concrete off-grid prime witness exposes exactly that unpaid term; another balanced composition identity or larger moderate grid would not resolve it.
