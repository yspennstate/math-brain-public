# exact target, quantifiers, hypotheses and units

Verdict: ACCEPT_AT_STATED_SCOPE for A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 from run 20261011T220210Z-account05-A047-boundary-search. For every fixed finite pair of Boolean children g,h in a common orthonormal product Fourier basis with fixed interior data biases, an independent physical selector chooses h with probability p and g otherwise. Writing c=E(gh), G_T=ghat(T), H_T=hhat(T), and Z=sum_{G_T=0} H_T^2,

    lim_{p->0} (J_X-M_X)/(p log2(1/p))
       =2Z+2c-2 <= 1/2-2(c-1/2)^2 <=1/2.

Here M_X=H(S_X|S_Y), while J_X=I(X;S_Y) in the actual physical-child spectral experiment. All entropy is in bits. Equality 1/2 is attained by actual constant/quarter-defect children and by balanced children after multiplication by a fresh fair character. Disjoint child Fourier supports give M_X=J_X=h2(p) exactly at every p in (0,1).

The precise refuted statement is a universal scalar tax tau(p) with endpoint coefficient below 1/2 in J_X<=M_X+tau(p). The statement is refuted even for balanced children and a typical dictator. A047 does not refute B09's original tax, a coefficient-1/2 repair, or uniform-cube FEI. This stage adds an independent review, not a new mathematical candidate or a claim of novelty.

# sources actually read, revisions and theorem locators

Read BOARD.md at this stage's start: supervisor snapshot 2026-10-12 00:49 UTC. Read B19 STREAM_NOTES.md v2 dated 2026-10-11 23:35 UTC and A092 STATUS.md. B19 directs A092 to finish A046 then review A047's endpoint certificates. A046@1 was independently accepted in A092's previous stage; it was not replayed. A085's board status and source review record indicate prior scoped acceptance of A047 and A071; this independent reconstruction supplies the B19-directed review, and the previously pending A071 full-grid item is no longer the immediate target.

Protocol EXECUTION_PROTOCOL.json, revision 2026-10-11-execution-v2, was read in full during stage 1 and retained for this stage. The source-complete target is A047 REPORT.md, complete derivation paragraphs 1-5, BOUNDARY_ASYMPTOTICS.tex, CLAIMS.json, code/boundary.py, code/unequal.py and out/results.json/out/unequal.json. The exact target source bytes and stage board/notes are pinned in out/SOURCE_MANIFEST.json. A047's new 20261012T003641Z run was incomplete at intake and is not a dependency or acceptance target here.

The earlier B09 biased identity and A092@stage1 normalization context are retained; no Maassen-Uffink theorem, paper theorem, or unreviewed universal tax is needed for this elementary proof. The local threshold and percolation manuscripts are background already consulted in stage 1 and are not re-audited here. B19's later paper audit and B09/B10 finite-p tax announcements are context, not assumed premises.

# complete derivation or exact first unsupported line

Reconstruct the physical Boolean function directly as F(0,y)=g(y), F(1,y)=h(y). Its orthonormal selector basis consists of 1 and (X-p)/sqrt(p(1-p)). Hence each residual Fourier label T has selector-sector masses

    a_T=((1-p)G_T+pH_T)^2,
    b_T=p(1-p)(H_T-G_T)^2,
    q_T=a_T+b_T=(1-p)G_T^2+pH_T^2.

Each child law is normalized by Boolean Parseval. The physical mixture law q is exactly the residual spectral marginal, with actual branch weights 1-p,p. Therefore

    J=H(q)-(1-p)H(G^2)-pH(H^2),
    M=H((a_T,b_T)_T)-H(q).

For the finite coefficient lists, partition labels into G_T=0 and G_T!=0. On a nonzero G label, q_T and a_T converge to the positive constant G_T^2, so their entropy changes are O(p). The b mass has leading coefficient (H_T-G_T)^2 times p; if that difference is zero then b is identically zero. On a zero G label, q_T=p H_T^2, b_T=p(1-p)H_T^2, and a_T=p^2 H_T^2. Thus H(q) has p log2(1/p) coefficient Z, and H(a,b) has coefficient Z+D, where D=sum_{G_T!=0}(H_T-G_T)^2. Terms of order p^2 contribute O(p^2 log(1/p))=O(p), and the averaged fixed child entropies change only linearly. These facts prove J=Zp log2(1/p)+O_{g,h,bias}(p), M=Dp log2(1/p)+O_{g,h,bias}(p), without exchanging an infinite sum and a limit.

Parseval and correlation yield D+Z=||H-G||_2^2=2-2c, hence Z-D=2Z+2c-2. Let P_G be projection onto the nonzero labels of G. Since ||G||_2=1, c=<G,P_G H>, and Cauchy-Schwarz gives c^2<=||P_G H||_2^2=1-Z. Consequently

    2Z+2c-2 <= -2c^2+2c
       =1/2-2(c-1/2)^2 <=1/2.

Equality at the final upper bound occurs precisely when c=1/2 and P_G H=G/2. Both implications follow from equality in Cauchy-Schwarz and the completed square. The inequality itself uses only finite real unit coefficient vectors; Booleanity is needed to ensure the actual physical construction and attainability, rather than being an extra source of this upper bound.

For an explicit actual witness, take fair data bits and g=1, h=-1 only at (0,0), +1 at the other three vertices. Then c=1/2 and H=(1/2,-1/2,-1/2,-1/2) in a Walsh sign convention; Z=3/4 and D=1/4. The debt coefficient is 1/2. Multiplication of both functions by a fresh independent fair character shifts all Fourier labels bijectively, preserves the full selector ledger, and makes both children balanced. The finite balanced witness reconstructed below uses g=z and h=z except at the two vertices with y_1=y_2=0, where its sign is reversed. This gives a typical dictator and the same coefficient.

For disjoint supports, the residual label identifies which physical child generated it, giving J=h2(p). In a G-only fiber the selector spectral proportion is p; in an H-only fiber it is 1-p. Their binary entropies coincide, so M=h2(p). Equal children have M=J=0. Opposite children have J=0, M=h2(4p(1-p)); these controls check the distinction between physical and spectral selector probabilities.

The unequal-bias AND corollary is also correct at its stated scope. Starting from the four actual values (1,1,1,-1), let P(X=1)=p be fixed and P(Y=1)=q->0. The Y-present marginal mass is v=4pq(1-q); its two conditional selector masses have proportions p,1-p. The X-only, Y-absent mass is 4p(1-p)q^2=O_p(q^2). Grouping the parent law gives H(parent)=h2(v)+v h2(p)+O_p(q^2 log(1/q)). The exact child mixture identity then gives

    J-M=4p(1-p)q log2((1-p)/p)+O_p(q^2 log(1/q)).

This yields a positive leading sign for fixed p<1/2 and a negative leading sign for fixed p>1/2. It is not uniform at a simultaneous moving p,q endpoint.

No unsupported line was found in the exact A047@1 claim. The first unsupported extrapolation from this endpoint proof would be replacing its pair-dependent O(p) remainder by a dimension- and bias-independent remainder, or inferring a finite-p half-tax solely from the leading coefficient. Newer B09/B10/A096 finite-p tax sources must be reconstructed under their own versions; this endpoint review neither accepts nor rejects them. The first unpaid universal bridge remains the nonreusing payment of a complete physical tree ledger with terminal entropy.

# executed validation with domain, arithmetic, commands and outputs

SEARCH_SPEC.json was written before computation. Frozen domain: all ordered Boolean children pairs on n=0,1,2,3 uniform data bits, with no symmetry quotient; five named child pairs at p=1/8,1/64,1/1024; and five unequal-bias two-bit AND cases. There are 65,812 endpoint pairs plus 20 finite certificates. Memory estimate is 60 MB, below the memok threshold; pilot and full computation each have a 60-second hard guard. No heavy job, automatic dimension increase, GPU or background helper was used.

Executed:

    python -X utf8 runs/20261012T004903Z-account05-A092-counterexample-referee/code/review.py --pilot
    python -X utf8 runs/20261012T004903Z-account05-A092-counterexample-referee/code/review.py

Pilot PASS: 276 pairs and 20 finite certificates, 0.236 seconds arithmetic runtime. Full PASS: 65,812 pairs and 20 certificates, 0.726 seconds arithmetic runtime. Process/tool launch overhead is separate. Each n's result is saved immediately in out/CENSUS.json after the full census; finite records are saved after every case. out/RESULT.json records the final summary.

| Data bits | Ordered pairs | Positive coefficients | Zero coefficients | Maximum | Maximizers | Balanced maximum |
|---|---:|---:|---:|---|---:|---|
| 0 | 4 | 0 | 2 | 0 | 2 | none |
| 1 | 16 | 0 | 12 | 0 | 12 | 0 |
| 2 | 256 | 32 | 64 | 1/2 | 32 | 0 |
| 3 | 65,536 | 1,472 | 10,336 | 1/2 | 448 | 1/2 |

The independent census uses direct integer character sums from every original table, with an opposite truth-mask convention to A047; no spectrum is accepted as input. The direct inverse, Parseval, physical correlation and edge/spectral influence identities are checked exactly. A second recursive centered transform matches the squared spectrum of every child. Every pair checks the exact coefficient formula, Cauchy inequality, full completed-square bound, and equivalence of sharpness with the projection condition. All reported A047 counts and maxima match.

Finite source pairs are reconstructed as actual tables, with the selector appended as the last coordinate. The recursive centered transform squares coefficients and multiplies by product variances. This produces the original interleaved A047 joint law after an explicitly checked indexing permutation. M is computed by conditional spectral distributions, and J by the actual physical-selector posterior distributions; these differ in representation from A047's entropy-difference implementation. The mixture and chain-rule calculations agree in rigorous enclosures.

The certified entropy implementation is copied from A092's independent stage-1 implementation into this run as code/independent.py, with no dependency on A047 code. It normalizes x=2^k z with z in [1/2,1], and encloses -ln z using sum_{j=1}^{80}(1-z)^j/j and remainder at most (1-z)^81/[81z]. Division is between nonnegative numerator intervals and a strictly positive ln2 interval; negative entropy coefficients reverse endpoints. This is a different logarithm series from A047's atanh implementation. Exact Fraction endpoints and outward rational decimal displays are stored in out/FINITE.json and out/UNEQUAL.json. All supplied A047 M,J,debt intervals overlap the independent enclosures. Six named-pair debts and four unequal-AND debts are strictly positive; three opposite-child debts and one unequal-AND debt are strictly negative. The six equal/disjoint controls are exact zero by the analytic identities, not by declaring an interval containing zero equal to zero.

# proof dependencies and changed downstream conclusions

A047-SHARP-FIXED-CHILD-RARE-SELECTOR@1 receives an independent ACCEPT_AT_STATED_SCOPE review. No repair was supplied to that version, so A092 remains independent of its contributor. The proof uses only finite entropy expansions, Parseval, projection/Cauchy-Schwarz and the original actual Boolean tables. It does not assume a universal biased uncertainty theorem or another pending claim.

Together with A046's accepted lower-bound example, this confirms that 1/2 is the sharp fixed-child leading endpoint debt coefficient, including balanced-child realizability. The source's finite certificates and unequal-bias sign controls are independently reproduced. B09/B10 should distinguish this sharp endpoint fact from their newer finite-p envelopes and from a nonreusing global influence payment. No claim of an unbounded uniform H/I ratio is justified by any reviewed example. The independently reviewed A071 full-grid result from A085 should replace the stale pending item in A092's rolling status; it was not rerun here.

Packaging correction for B20: A047's source finalize.py hashes the statement text alone, giving a7c1f6e2b4813f92ed2d1166200b84c078aa44f1d3d124226777bf7f13e0b84f. The registry convention hashes compact sorted JSON containing both statement and hypotheses; for the unchanged A047@1 text this gives 81d834734e7315b3a311892e2384e05cd519497131ccd3ce60a01cd83546bade. This export uses the canonical hash and retains the original hash and convention inside proof_source. The mathematical statement, hypotheses and version are unchanged; no substantive repair or reviewer-independence conflict results. The original A047 and A085 files were not edited.

# one next mathematical action and independent reviewer

Next: audit A050's source-complete equal-overlapping-magnitude physical payment L<=4 Inf, then test precisely which remainder survives when inserting that scoped repair at a bad node with a prescribed terminal cost. Keep the actual selector/disagreement budget and the complete terminal entropy in one ledger. This consumes a useful new payment dependency after completing the lead-directed endpoint review, rather than seeking another endpoint witness. Independent challenge of this review: A087 or A085; original A047 has the A092 reconstruction here. Consumers: A046/A047/A049/A050/A057/A064, B09/B10/B13/B19/B20.

# actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json are saved in this assigned run, with packet_ids=[A092]. Code, frozen spec, pilot/full census, every finite certificate, source hashes, validation and artifact receipts are saved locally. STATUS.md, dated WORKLOG.md and LEARNED.md are current. code/finalize.py validates exact protocol field sets, the unchanged statement/hypotheses and canonical hash with preserved legacy source hash, report fields, progress-copy identity and the <20 MB limit, and writes out/VALIDATION.json and out/ARTIFACT_RECEIPTS.json.

Local artifact completion and the independent review verdict are established; supervisor copying, GitHub/brain mirror verification, downstream use and public release are not claimed. All writes were confined to A092. No git, external message, brain mutation, or another agent's write occurred.

Universal bridge: this stage moves C019 stopping-tree payment by independently closing the sharp fixed-child rare-selector coefficient at 1/2 and recertifying 20 actual Boolean finite controls, with 65,812 exact endpoint-pair checks supporting realizability and sharpness. It does not reduce the remaining universal payment to a bounded constant: changing-family uniformity, actual physical-budget conversion, cumulative nonreuse and terminal entropy still require their own proofs. NEXT audits a scoped physical payment at bad nodes because this is the shortest route from the now-reviewed boundary coefficient to the complete stopping-tree ledger, rather than another isolated class bound or a repeated finite witness.
