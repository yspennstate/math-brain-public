# A047 stage 2: exact real supremum and certified Boolean separation

## exact target, quantifiers, hypotheses and units

Follow B10 lead v2's A047 direction. For an independent selector X of bias p and two real L2-unit children G,H in a common orthonormal product basis, let M=H(S_X|S_Y), J=H(S_Y)-(1-p)H(G^2)-pH(H^2). Entropy is in bits. Compute the sharp real supremum of J-M at every fixed interior p, and compare it to the Boolean supremum over all ordered children on at most three UNIFORM residual data bits at p=1/8,1/4,3/8. Arbitrarily biased residual measures are not included in this finite census.

The real supremum equals tau*(p)=h2(p)-min_t[h2(sin^2 t)+h2(sin^2(t-b))], sin^2 b=p. The lower convex envelope at abscissa p equals that minimum exactly. Two residual Fourier labels suffice for attainment, hence one uniform residual bit suffices for REAL children. The finite Boolean suprema are exactly the witness prime-log expressions in out/CENSUS.json. Strict gaps to certified real witnesses are established at all three requested biases.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-12 00:32 UTC, B10 STREAM_NOTES.md v2 2026-10-11 23:31Z, own STATUS/LEARNED, and the complete execution protocol revision 2026-10-11-execution-v2. Read the lead's original REPORT and CLAIMS in claude/B10/runs/20261011T230400Z-claude-B10-onebit-half-tax, especially exact angle reduction and A047 next target. Read A085 original REPORT/CLAIMS, run 20261011T231324Z-account05-A085-certificate-adversary, which independently accepts A047@1 at fixed-child scope and warns against moving-bias remainders. Source bytes and hashes are recorded in out/SOURCE_RECEIPTS.json.

The board shows A046 reviewing the lead half-tax bound, A048 assigned tree payment, A049 assigned block additivity, and A050 scoped repair. Those tasks are not repeated here. The prior packet's missing lead notes now exist. The lead's analytic half-tax lemmas, interval boxes and multi-bit additivity claim are not proof dependencies of the new real-attainment theorem or census; this stage re-derives the exact angle ledger and does not attempt to certify tau*<=Delta/2.

## complete derivation or exact first unsupported line

Full proof is in DERIVATION.md. For q_T=(1-p)G_T^2+pH_T^2, set (sqrt(1-p)G_T,sqrt(p)H_T)=sqrt(q_T)(cos t_T,sin t_T). Normalization gives sum q_T=1 and sum q_T sin^2 t_T=p. Exact parent masses yield

    J-M=h2(p)-sum_T q_T F_p(t_T),
    F_p(t)=h2(sin^2 t)+h2(sin^2(t-b)).

Conversely every finite angle mixture satisfying these two constraints defines unit real children. Thus the sharp real supremum is h2(p) minus the lower convex envelope of (sin^2 t,F_p(t)) at p. Let m=min F_p and t0 minimize it. F_p(0)=h2(p), while F_p(t0)>=h2(x), x=sin^2 t0. For 0<p<1/2 this excludes p<x<1-p. Complement t0 by pi/2 if necessary to arrange x<=p. Its orthogonal companion has abscissa 1-x and the same F_p=m. Weights (1-x-p)/(1-2x) and (p-x)/(1-2x) are nonnegative, average the abscissae to p, and average F_p to m. This proves exact attainment with two labels. Child exchange covers p>1/2; at p=1/2 a complementary equal-weight pair, or a single minimizer with abscissa 1/2, works. Explicit normalized coefficient vectors are given in DERIVATION.md. Their inverse transforms are real and need not be Boolean.

Real lower witnesses use rational x=sin^2 t<=p and the same complementary mixture. Their second measurement probability is y=p+(1-2p)x-2sqrt(p(1-p)x(1-x)), so the attained debt is h2(p)-h2(x)-h2(y). Rational square-root enclosures and monotonicity of h2 on [0,1/2] certify these witnesses without a numerical optimizer or an unproved minimizer formula.

For Boolean children use all sign tables and integer Walsh coefficients. Each pair's exact debt is a sum over fibers of 2eta(q)-eta(a)-eta(b)-(1-p)eta(G^2)-p eta(H^2), with eta(s)=-s log2 s and exact parent masses a=((1-p)G+pH)^2,b=p(1-p)(H-G)^2,q=a+b. Rational log intervals certify every pair, then maximum lower/upper endpoints enclose the finite supremum. Every interval-overlapping candidate has the same exact rational prime-log vector as the witness; all excluded candidates have certified smaller debt. Thus the reported candidate counts are exact maximizing-pair counts, not floating ties. This settles the finite domain without extrapolating to more bits.

First unsupported line: a dimension-independent Boolean improvement below tau*(p), or any deduction that these small uniform-data gaps persist for arbitrarily many residual bits or moving product biases. Neither the exact real supremum nor the finite Boolean census pays the C019 expected path tax, conditional M term or terminal entropy. The trigonometric minimum's full numerical value is not computed by this stage; certified witness lower bounds suffice for the strict comparisons.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded all computation. Pilot: 828 ordered pair-bias cases on n=0,1,2, compute runtime 1.274 seconds. Full frozen domain: 197,436 ordered pair-bias cases on n=0,1,2,3, with no symmetry reduction. Initial full run took 1.713 seconds. A targeted equality-certificate extension rechecked the same domain in 2.196 seconds, adding exact symbolic ties; it did not increase dimension or precision. An initial pilot coding error shadowed the parser object with an integer interval endpoint; it exited before a saved row and supplied no result. The error and repair are recorded in out/PILOT_FAILURE.txt.

| p | Exact Boolean maximum, decimal display | Max pairs on n=3 | Attaining typical/rare children | Real lower witness x | Certified gap greater than |
|---|---:|---:|---|---|---:|
| 1/8 | 0.11954501602442495 | 448 | constant / quarter defect | 1/32 | 0.012463 |
| 1/4 | 0.08272815130664832 | 448 | constant / quarter defect | 1/16 | 0.019324 |
| 3/8 | 0.010176855194269169 | 128 | constant / one-point defect on 3 bits | 1/256 | 0.007873 |

The n=2 maximum at p=3/8 is 0.009440472829260055 (32 maximizing pairs), so the three-bit point defect supplies a genuine increase. The n=2 maxima at the other two p match n=3. For n<=1, the exact maximum is zero. All numerical entries above are displays of rationally certified quantities; out/CENSUS.json contains exact interval endpoints, prime-log expressions, child truth masks/tables, integer Walsh vectors, parent spectrum, exact excluded-candidate separation and real witnesses.

At the positive finite maxima, the typical child is -1. For p=1/8,1/4 the rare child is +1 at data points 0,1 and -1 elsewhere: integer Walsh (-4,0,4,0,4,0,4,0). For p=3/8 it is +1 at point 0 only: integer Walsh (-6,2,2,2,2,2,2,2). The typical child Walsh is (-8,0,0,0,0,0,0,0). This explicitly verifies actual Boolean realizability; output negation converts them to the usual positive typical child convention.

Forty-term rational atanh intervals after range reduction r in [1,2) have proved tail <=2z^81/(81(1-z^2)). Entropy contributions are rounded outwards to a common 2^-100 lattice. All maximum comparisons are integer operations, and square roots use proved rational enclosures at scale 2^-140. Symbolic equalities factor rational probabilities into primes with rational coefficients; no approximate log equality is accepted. Direct character-sum Walsh, inverse Walsh, Parseval, physical edge influences, and physical/spectral selector influence agree exactly. Powers-of-two logs and zero masses are checked.

Commands from this run: `python -X utf8 code/census.py --max-n 2`, then `python -X utf8 code/census.py --max-n 3`; `python -X utf8 code/summarize.py` displays witnesses. The full equality replay returns PASS. Memory estimate is under 100 MB (one temporary 65,536-score list, cached fiber types, 256 child spectra); peak RSS was not measured. No >300 MB job, GPU, background helper, git, brain write or external mutation was used.

## proof dependencies and changed downstream conclusions

The exact angle reduction is re-derived algebraically and the envelope-attainment proof uses only continuity, elementary binary-entropy monotonicity, complementary-angle symmetry and unit-vector normalization. No unreviewed lead half-tax bound or block-additivity theorem is assumed. A047@1 has independent acceptance recorded in A085's original review; it is context, not a premise for the new finite-p theorem. The real relaxation is now proved sharp at every p despite its normalization constraint. Any further uniform singleton improvement must use Boolean realizability, not just L2 normalization. The finite census supplies explicit amounts of extra Boolean credit at three biases, but those amounts cannot yet be spent at arbitrary tree nodes.

## one next mathematical action and independent reviewer

Derive the equality-defect identity tau*(p)-(J-M)=sum q_T(F_p(t_T)-min F_p) for actual stopping-tree child pairs, and test whether a Boolean f^2=1 constraint prices that nonnegative reserve in the same single-use path-entropy ledger as A048/A050. This can support the live C019 tax payment without another dimension escalation. A092 is primary independent reviewer; A087 alternate. A085 can reconstruct the finite maxima via a different centered parent transform. A048/A050 receive the exact real-attainment obstruction and finite Boolean fixtures through these saved artifacts; no messages or completed downstream use are claimed.

## actual persistence receipts or precise save blocker

REPORT, CLAIMS, PROGRESS and byte-identical PACKET_DELTA, DERIVATION, frozen specification, scripts, pilot failure/receipts, full output, exact endpoint and symbolic certificates are saved in this run. STATUS has two lines; WORKLOG is appended and LEARNED receives the real-attainment and scope lessons. The finalizer validates exact protocol keys, report elements and file-size limits and writes SHA256 receipts. There is no save blocker. Independent review, supervisor copy, brain/GitHub ingestion and mirror verification remain pending.

## Universal bridge

This stage moves the B10 sharp-tax interface for C019 stopping-tree payment by proving that the lead's tau*(p) is the exact real normalized-child supremum, with the normalization constraint attained on only two labels, and by certifying strict Boolean savings in the entire n<=3 uniform-data domain at three biases. The remaining universal gap is payment of the expected sharp tax plus conditional labels and terminal entropy using nonreused physical influence or C024 path-entropy reserves; finite Boolean savings are not a universal substitute. NEXT studies the exact nonnegative uncertainty defect in actual tree child pairs, because that is the reserve the stopping-tree ledger would have to use, rather than enlarging an isolated finite census.
