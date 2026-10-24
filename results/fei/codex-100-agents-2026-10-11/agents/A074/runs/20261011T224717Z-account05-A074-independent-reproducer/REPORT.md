## exact target, quantifiers, hypotheses and units

Complete A074 independent reproduction for exactly three selected witnesses. Truth tables are little-endian binary assignments, outputs ±1, biases independent, entropy in bits, and the orthonormal basis is (x_i-p_i)/sqrt(p_i(1-p_i)). First: f=(1,1,1,-1,1,1,1,1), p=(1/8,1/8,1/2), A={2}, residual D=M_A-J_A. Second: f=(1,-1,-1,-1,-1,1,1,1), same p,A,D. Third: f=(1,1,1,-1), p=(1/8,1/4), A={0}, residual R=J_A-M_A. M is conditional spectral entropy; J is physical-child/spectral mutual information. No grid-minimality or continuum claim.

## sources actually read, revisions and theorem locators

EXECUTION_PROTOCOL.json read in full, revision 2026-10-11-execution-v2. README, CURRENT_STATUS, CLAIM_REGISTRY, OBSTRUCTION_REGISTRY, PACKET_STATUS and STREAM_NEXT_ACTIONS consulted; campaign plan B15 A074 lines978-982 supplies acceptance tests and named deliverables. BOARD read at start: supervisor 2026-10-11 22:47 UTC. B15 STREAM_NOTES.md absent at that time; we followed board handoffs A071→A074 and A073→A074 instead, without claiming to disagree with an unavailable direction.

Supplement CAMPAIGN, CLAIMS, COUNTEREXAMPLES, SEED_LEMMAS, NATIVE_MAPPING and curated sources ingested. BLOCK_RESTRICTION_IDENTITY sections1-3 read explicitly for the partial channel, conditional entropy and physical influence telescope. Canonical earlier B05/B09/B19 reports read as context. A072 REPORT gives its uniform-Walsh-to-centered expansion; A073 REPORT and three output JSONs give fixed inputs and comparison targets. A071/A073 CLAIMS@1 preserve the exact finite-grid and repaired-AND statements. Our code never imports or executes any other agent's code.

All four supplied context .txt papers read into the scoped source reader, with introductions, normalization and composition/selector locators extracted: 38pp threshold Proposition7.1, §8.2 Proposition8.6, §9.2; earlier29pp Proposition7.1; percolation30pp Theorem1.1 and §1.1, compared with31pp earlier Theorem1.1. Context results are not proof dependencies; no full scholarly audit of these papers is claimed. Byte hashes, including explicitly decoded legacy cp1252 text, are in out/source_receipts.json. Selected original-output hashes are separately in out/validation.json.

## complete derivation or exact first unsupported line

Every binary truth table has the unique multilinear interpolation f(x)=sum_T c_T prod_{i∈T}x_i. Subset Möbius inversion gives c_T=sum_{U⊆T}(-1)^{|T\U|}f(1_U). Successive differences compute these integer c_T, independently of Walsh transforms or weighted centered moments. Evaluating the polynomial at every binary input reproduces the original table exactly.

Set u_i=x_i-p_i. Expanding x_i=p_i+u_i gives b_S=sum_{T⊇S}c_T prod_{i∈T\S}p_i. Thus f=sum_S b_S prod_{i∈S}u_i and μ(S)=b_S² prod_{i∈S}p_i(1-p_i). Independence and centering prove orthogonality. We check every inverse evaluation and sum μ=1. Separately count physical disagreeing edges with product probabilities Q_i over other coordinates. Since f(1,x_-i)-f(0,x_-i) is 0 or ±2, orthogonality gives sum_{S∋i}μ(S)=4p_i(1-p_i)Q_i. We reconcile both computations; these quantities must not be confused away from uniform bias.

For each physical assignment z to A, construct its truth table afresh and apply the same polynomial routine on B=Aᶜ. Let w_z be its physical probability, μ_z its spectrum, q_t=sum_{S:S∩B=t}μ(S), and r(z,t)=w_z μ_z(t). Partial orthogonality gives q_t=sum_z r(z,t); this is checked exactly. The retained-coordinate spectral influence equals its w_z-weighted child influence, also checked.

Compute the quantities directly from the two conditional experiments:

    M=-sum_S μ(S) log2(μ(S)/q_(S∩B)),
    J=sum_(z,t) w_z μ_z(t) log2(μ_z(t)/q_t).

Zero masses are omitted. This avoids the previous parent/child entropy-combination and prime-product representations. It retains both the spectral selector and physical assignment, rather than identifying these different random variables.

Logarithms use a third representation. For 1≤x≤2 put t=1-1/x∈[0,1/2]. Integrating the geometric series yields ln x=sum_{k≥1}t^k/k. Its 40-term partial sum a obeys a≤ln x≤a+t^41/[41(1-t)], since each remaining denominator is at least41. For any positive rational r, find integer k with r=2^k x,1≤x<2; enclose log2 r=k+ln x/ln2. Both numerator bounds are nonnegative and the ln2 denominator interval positive, so division is lower/upper reversed in the denominator. Negative entropy weights reverse interval endpoints. All these operations use integers and Fraction, with no transcendental floating arithmetic.

First witness reproduces μ=(3969,7,7,49,1,7,7,49)/4096, q=(1985,7,7,49)/2048 and equally weighted children (961,7,7,49)/1024 and (1,0,0,0). The fresh rigorous interval is strictly inside (0.00256647,0.00256648); consequently D>5/2048. This name denotes the previously selected record, not an independently established global minimum.

Second witness is g(x_0,x_1)(1-2x_2). Its spectrum has deterministic selector membership and child laws both equal q=(289,343,343,49)/1024. Therefore M=J=D=0 exactly, with no approximate equality test.

AND reproduces μ=(225,7,3,21)/256, q=(29,3)/32, children (1,0) with weight7/8 and (1/4,3/4) with weight1/8. Direct channel/conditional calculations give 0.11954501<R<0.11954502, hence R>1195/10000. The tax-free arbitrary-product-bias helper is false at this scope. Full FEI is not refuted.

No differing rational quantity or unsupported line remains in these fixed calculations. The first unsupported extrapolation would be accepting every A071 grid case, its global minimum, an all-bias theorem, or dimension-independent nonreusing influence payment. We make none of those extrapolations.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json saved before running: three fixed records, no symmetry reduction, 40 log terms, estimated memory50 MB, cap55 seconds, no dimension escalation or heavy search. Executed:

    python -X utf8 runs/20261011T224717Z-account05-A074-independent-reproducer/code/reproduce.py

Final successful pilot: 232 exact assertions, 3 records, zero failures, measured Python runtime0.0189664 seconds. Source records are loaded for comparison only after the independent calculation. Signed centered coefficients, squared masses, physical pivotal probabilities, spectral influences, child weights/tables/spectra and marginals all match. Fresh intervals lie within A073's published intervals. out/*.json records exact rational endpoints and the full physical/spectral joint law.

One initial execution passed the first case's mathematical comparisons but failed saving because out/ had not yet been created; adding mkdir fixed that persistence error. The source reader first encountered a legacy non-UTF8 document; explicit cp1252 fallback completed ingestion. The first finalizer used a raw-statement digest; source A071/A073 finalizers show that statement_sha256 hashes compact sorted JSON containing both statement and hypotheses. We corrected the digest validation to that convention and preserved all source hashes. These incidents changed no mathematical result or source claim.

Standalone named deliverables INDEPENDENT_REPRODUCTION.py and REPRODUCTION_REPORT.json accompany the code entry point. The standalone script is the same local implementation with its root-path calculation adjusted; producing it is not counted as another independent calculation.

## proof dependencies and changed downstream conclusions

Only finite Boolean truth tables, elementary multilinear interpolation, product orthogonality, entropy definitions and the proved logarithm tail are proof premises. A071/A073 source outputs are comparison targets, not imported spectra or mathematical assumptions. CLAIMS.json preserves existing statement versions and hashes, adding a selected-record review to A071 and an acceptance-at-stated-scope review for the repaired AND certificate. A071's full grid remains pending review. This creates no third broad B15 candidate and supplies no new universal constant.

## one next mathematical action and independent reviewer

Consume a source-versioned singleton-tax transport candidate from A050/A057 (or a new B09 revision), and reconstruct its complete residual on an actual Boolean witness with conditional M, rare bias and terminal entropy retained. A085/A092 should inspect this separate implementation and scope-limited reviews. Do not rerun the retired baseline grid absent a concrete changed hypothesis or discrepancy.

## actual persistence receipts or precise save blocker

All assigned REPORT, CLAIMS, PROGRESS, identical PACKET_DELTA with packet_ids=[A074], named reproduction deliverables, frozen spec, code and outputs saved inside A074 only. out/manifest.json provides hashes and sizes; finalizer checks exact protocol field sets, original statement hashes, standalone equivalence, delta equality and <20 MB artifact sizes. STATUS has two lines, WORKLOG dated append, LEARNED durable record. Supervisor adoption, GitHub copy, mirror verification and independent review of this implementation remain pending; no external persistence receipt is claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment by independently certifying three fixed physical restriction ledgers: D>5/2048, D=0, and the necessary biased correction J-M>1195/10000, with a different polynomial representation, direct conditional/channel entropy and a third logarithm enclosure. It moves no universal FEI constant. Conditional M, valid bias tax, terminal entropy and a nonreusing physical influence payment remain unpaid. Applying this audited witness pipeline to the next source-versioned transport candidate is the shortest route toward the universal bridge because it tests the exact missing payment rather than producing another isolated finite-class census.
