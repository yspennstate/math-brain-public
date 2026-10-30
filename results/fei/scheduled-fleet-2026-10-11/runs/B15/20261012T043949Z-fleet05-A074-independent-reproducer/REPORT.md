## exact target, quantifiers, hypotheses and units

Following B15 lead v2, independently reconstruct f5 with negative truth-mask4194372 and f6 with negative truth-mask1103806792023, and every Boolean truth table on uniform physical cubes n=0..4. A mask bit at little-endian assignment x means f(x)=-1; remaining outputs are+1. μ(S)=fhat(S)², B_i=H(S_i|S_-i), Inf_i=Pr(i∈S), E(f)=min over relevant i of B_i/Inf_i. Entropy is in bits. Certify f5 E>539/200 and f6 E>368/125 and independently reproduce sharp finite selection constant Kstar=4+(5/2)log2(5)-(9/2)log2(3) for n≤4. This does not certify all-dimensional aggregate erasure or full FEI.

## sources actually read, revisions and theorem locators

BOARD.md supervisor snapshot2026-10-12 04:39 UTC and own STATUS/LEARNED read at stage start. B15 STREAM_NOTES v2,2026-10-11 23:25 UTC read in full. Its explicit A074 direction supersedes our prior biased-tax NEXT. Protocol reread in full:2026-10-11-execution-v2. B15 lead CLAIMS.json in run20261011T225100Z-claude-B15-erasure-countersearch read, particularly B15-LKSTAR-FAILS-N5-N6@1 and its n4 review. A072 stage2 REPORT/CLAIMS and witness_n5/n6 JSON consulted; selected formulas were read, while complete JSONs were parsed for exact reconciliation after our fresh reconstruction. A071 stage2 REPORT read for exact-five-bit completion and scope; this stage does not rerun that census. A082 stage1 REPORT and CLAIMS read for A082-FINITE-TRUE-ERASURE@1; its affine4 claim is not reviewed here. Source receipts pin current bytes; original source versions are preserved in our local reviews. Prior-stage context-paper consultation remains context, not a mathematical premise. No other agent code is executed or imported.

## complete derivation or exact first unsupported line

Let N=2^n and A be the negative physical assignments. For every nonzero character s, sum_x χ_s(x)=0 by pairing an input with a flip in s. Hence

    W_0=N-2|A|,
    W_s=-2(|A|-2|{x∈A:popcount(x&s) odd}|), s≠0.

We implement these direct character sums by intersections with precomputed character-sign bitsets and arbitrary-precision Python bit_count. There is no butterfly transform, incremental Gray transform or imported spectrum. Character orthogonality proves this is the uniform Fourier transform with denominator N. The census checks sum W_s²=N² for every table. Witnesses additionally check the complete signed inverse at each physical assignment. Physical undirected disagreeing i-edges e_i are counted independently, giving Inf_i=2e_i/N. Every census coordinate reconciles this with sum_(s∋i)W_s²/N².

For s not containing i let p0=μ(s),p1=μ(s∪{i}),q=p0+p1. These are the exact joint spectral law of (S_i,S_-i); when q>0 the conditional law is (p0/q,p1/q). Direct conditional entropy is

    B_i=-sum_(s not containing i) sum_(j=0,1) pj log2(pj/q).

Zero masses contribute zero. For both witnesses the script constructs every nonzero joint packet as Fractions and sums this expression. Separate 60-digit mpmath evaluation uses those same exact joint probabilities as numerical evidence only. Actual physical-child tables are independently restricted from the input masks, transformed by the direct character sums, and their average squared spectra are checked to equal q packet by packet.

Rational logarithm bounds use our previous stage's independent positive series, reconstructed here without importing that implementation. If1≤x≤2 and t=1-1/x, then ln x=sum_(k≥1)t^k/k; integrating the geometric series proves the identity. Its40-term partial sum a gives a≤ln x≤a+t^41/[41(1-t)]. Range-reduce any positive rational r=2^k x with1≤x<2; divide the nonnegative numerator interval by the positive independently bounded ln2 and add k. Signed entropy weights reverse endpoints when negative. No mpmath or machine logarithm decides a sign.

For the census, write a=W_s²,b=W_(s+i)². Its conditional packet numerator is G(a,b)=(a+b)log2(a+b)-a log2(a)-b log2(b). We outward-round each rational enclosure to scale2^64, caching the possible integer packet pairs. G(a,0)=0 is exact. Let L_i=sum_(s∋i)W_s². Integer comparison Kstar_lower_scaled*L_i>sum packet_upper_scaled proves B_i<Kstar Inf_i. Every relevant coordinate is inspected; any such strict witness is enough. Unresolved ties use exact prime-log cancellation for Kstar Inf_i-B_i: factor integer log arguments and cancel rational coefficients. In each equality case, every relevant coordinate's coefficient vector vanishes, proving all those ratios equal Kstar. Irrelevant coordinates are omitted.

All truth masks from0 through2^N-1 are covered without symmetry reduction. The strict/equality classifications are recorded per mask in JSONL. The equality masks are also compared as sets with all embedded three-bit point defects and their output complements. These are exactly16 tables at n3 and64 tables at n4. A three-bit point defect has μ_empty=9/16, seven other masses1/16, Inf_i=1/4. Its conditional entropy divided by influence simplifies to Kstar, independently proving sharpness; embedding dummy coordinates preserves this ratio. The exact integer inequality2^53*5^100<3^180 proves Kstar<107/40.

Named reconstructed minima:

    E(f5)=(16/3)log2(2)-(3/8)log2(3)-(169/24)log2(13)+(89/24)log2(89),
    minimizing coordinates={0,1,3}.
    E(f6)=(16/3)log2(2)-(21/8)log2(3)+(95/24)log2(5)-(121/24)log2(11)+(65/24)log2(13),
    minimizing coordinates={0,1,2,3,4,5}.

Our direct joint-law intervals prove every coordinate exceeds the prescribed rational cutoff and Kstar; symbolic equality of ratio forms identifies ties and disjoint rational intervals establish all remaining minimum comparisons. Full spectra, edges, influences, B prime forms and minimum forms match A072. Fresh intervals also prove E(f6)>E(f5). This accepts B15's finite witness refutation at its stated scope, without changing A082's finite theorem.

The first unsupported line would be concluding that the ratios grow without bound in dimension, or that a finite uniform erasure-selection payment follows from the census. Neither inference is made. A071's five-bit upper result and A075's family bridge require their separate scoped proofs; no independent acceptance of those claims is issued here.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes execution. No symmetry; fixed dimensions; memory estimated100 MB, not measured; pilot cap55 seconds; full cap240 seconds. No job expected above300 MB, no GPU, no automatic dimension escalation. Executed from A074:

    python -X utf8 runs/20261012T043949Z-fleet05-A074-independent-reproducer/code/reproduce.py --pilot
    python -X utf8 runs/20261012T043949Z-fleet05-A074-independent-reproducer/code/reproduce.py

Pilot n0..3 and both witnesses:1607 exact assertions, zero failures,0.0262427 seconds. After the pilot, equality validation was strengthened to require symbolic equality at every relevant coordinate of an extremizer. Full run n0..4 and both witnesses:329427 exact assertions, zero failures,1.3684112 seconds. At n4:65536 tables,2 constants,65470 strict passes,64 equal; census runtime1.346160 seconds. Total census domain65814 tables,10 constants,65804 nonconstant; named witnesses are additional2 cases. No floating sign decisions.

mpmath60-digit displays begin2.695887520153100810486497662748... and2.944495303871858585073528591901...; these are numerical cross-checks, not30-digit certified enclosures. The fixed rational intervals are sufficient for the target signs; no unnecessary precision refinement is run. Each witness and each completed dimension was saved immediately; JSONL decisions stream to disk. The initial persistence validation detected Windows CRLF translation: the in-memory LF decision hash differed from saved bytes. Setting explicit LF output fixed this artifact error; one justified full replay returned the identical329427 assertions and classifications in1.1517426 seconds (n4:1.1306401 seconds), and saved-byte hashes then passed. Full n4 decision SHA256:1db27cd32b77e311f93d95f4d33fd960126dab78cacb02e3740aa19b900910b3. out/summary.json, witness_n5/n6.json and census_n*.json/JSONL contain exact endpoints, joint laws, source reconciliation and coverage counts.

## proof dependencies and changed downstream conclusions

The finite reconstruction is self-contained in truth masks, character orthogonality, entropy definitions, edge identities and the proved logarithm remainder. Source outputs are compared only after the new calculation. CLAIMS.json preserves B15-LKSTAR-FAILS-N5-N6@1 and A082-FINITE-TRUE-ERASURE@1 statements/versions/hashes and appends ACCEPT_AT_STATED_SCOPE independent review records. This creates no new broad candidate. A072's B/Inf/minimum subclaims are corroborated; its JS/decrement engine is not fully audited by this stage. A071 five-bit upper claim and all-dimensional C018/C019 remain separate obligations. Source claims are only locally reviewed, with shared registry adoption pending.

## one next mathematical action and independent reviewer

Consume A075's source-complete sparse Hamming-ball-plus-matching family formulas and reconstruct its actual physical restrictions, including any level-one collision and full terminal entropy. Certify a frozen bounded parameter list only when it tests a stated dimension-dependent payment, not a larger blind census. A085/A092 should challenge the direct-character and fixed-point/tie certificate here; A075/A072/B20 can consume the independently reconciled finite seeds.

## actual persistence receipts or precise save blocker

Saved inside the assigned A074 stage directory: REPORT, CLAIMS, PROGRESS, byte-identical PACKET_DELTA with packet_ids=[A074], FROZEN_SPEC, INDEPENDENT_REPRODUCTION.py, REPRODUCTION_REPORT.json, code and out records. Standalone reproducer is this same local implementation with root-path handling adjusted, not another independent implementation. Finalizer validates protocol field sets, unchanged source statements/hashes, decision-stream row counts and SHA256, the two-witness ordering and finite constant rational bound, and artifact sizes below20 MB. STATUS remains two lines; WORKLOG/LEARNED receive dated append entries retaining stage1 lessons. out/manifest.json pins local artifacts. Supervisor copying, remote mirror verification and review/adoption of this implementation remain pending; no external persistence is claimed.

**Universal bridge:** This stage supports the lead's erasure-selection bridge adjacent to C018 by independently accepting the two finite obstructions E(f5)>539/200 and E(f6)>368/125, while reconstructing the sharp n≤4 leaf constant and all64 four-bit extremizers through a separate direct joint-law calculation. It adds329427 exact assertions and no universal constant improvement: sup_n E*(n)<∞, or a terminal-inclusive nonreusing C019 replacement, remains unpaid. NEXT targets A075's dimension-dependent sparse-family and restriction mechanism because the unresolved issue is how erasure payment behaves through actual descendants, rather than another isolated finite maximum or replay of already accepted grids.
