# A008 stage 2: reviewed sunflower forests and unequal block-forest payment

## exact target, quantifiers, hypotheses and units

The B02 lead assigns A008 to reconstruct A006 v1 as a whole, then close the positive block-forest side for every read-once DNF. Both tasks are complete locally. The new theorem covers every m>=1 and every positive integer width tuple (w_1,...,w_m), arbitrary literal signs, disjoint supports, and one fixed prime-implicant table and feasible incidence vector lambda_l=1. Entropy and ideal costs are in bits; the source F statistic is in natural logs and its conversion is explicit. READ_ONCE_DNF.tex gives the complete proof.

The ORIGINAL conditioned queue has residual

    R <= (16/5+log2 e) I < 47I/10.

The actual finite once-per-block run probabilities, rather than the coarser generic forest bound, have complete nonempty cost

    C_pf <= (26/5+2log2 3+2log2 e) I.

Including the empty/nonempty entropy split gives h2(v)+C_pf<67I/5. This is a PI-J reference-cost closure on an already known FEI class. It is not a new Boolean FEI class or a universal bound. Optional prefix rounding and optional selector costs are not included or silently charged to I. Full FEI remains OPEN; the new result awaits independent review.

## sources actually read, revisions and theorem locators

BOARD.md was read at stage start, supervisor snapshot 2026-10-12 01:00 UTC. Own STATUS.md and B02/STREAM_NOTES.md v2 (2026-10-11 23:35 UTC) were read in full. The lead directs whole A006 review before the unequal-block positive result, sets PI-J as stream target, and forbids repeating single-gate tribes obstructions. The protocol was reread in full: fei-execution-protocol/2, revision 2026-10-11-execution-v2; its exact report/claim/progress fields govern the saved files.

A006's full stage-1 REPORT.md, CLAIMS.json and source manifest were read, and the original statement hash was recomputed. The review binds A006-SUNFLOWER-POSTERIOR-FOREST-PAYMENT@1. A006 stage-2 AUDIT_A008.md and A086 stage-2 JOINT_CODE_REVIEW.md were read: both independently accept A008 v1 at its original scope, without repairs. A094's durable review facts also accept A006 v1; this stage's lead-directed generic enumeration is an additional source-bound reconstruction, not a shared index edit. A007 stage-2 REPORT.md and claims were consumed for nonduplication: activated equal-width tribes are already closed there; this stage pays all unequal unactivated disjoint clause widths in the original lambda=1 reference independently.

The full source forests.tex was read, especially eq:forestpacking, eq:forestconditioning, eq:forestcost, thm:posteriorforest, lem:forestnormalizer and weighted activation. Its child-label law is lambda_child, not the distinct uniform-neighbor public queue. The proof imports only this complete baseline interface and its stated h2(v)<=2I estimate. The new spectral, hit-mass and conditional-binomial identities are derived directly. The prior-mixture source from the previous stage is only used when reconstructing A006's paid-prior clause. No unreviewed new campaign theorem is assumed. Byte hashes and locators are in out/SOURCES.json.

## complete derivation or exact first unsupported line

### Whole A006 review

REVIEW_A006.md records HOLDS at the original stated scope, with no repair supplied. Independent construction starts with every assignment of spectral coordinates to eligible gates, computes source SCCs, enumerates their root choices and incoming parent maps, checks reachability, enumerates attachments and chronological child-label orders, then deduplicates actual queue keys. It does not import or execute the author's checker or assume the star classification before enumerating.

The all-m proof then reconstructs why private-only sets have one isolated-root run, common singleton has m runs, and common+private sets have t! inside-root runs and (m-t)t! outside-root runs. Formal residual weights are independently summed as a-polynomials, a=2^-6/5. The complete actual probabilities multiply root conditioning, subset sizes, elementary normalizers, zero-child counts, root child counts, attachment multisets and each lambda-child draw. This yields exactly A006's residual S_B and complete W formulas. The source root normalizer D lies in [1/4,1/3); the two binomial recurrences prove R<=43I/10 and actual nonempty cost<=23I/2 for all m. The deterministic residual diverges on the common singleton. The normalized scale prior adds exactly v bits at component zero, preserving A006's 53I/10 and 25I/2 conclusions. Complete entropy inference still includes h2(v). No unsupported line remains in the reviewed restricted statement.

### Fixed unequal-block prime table and exact decoder

For disjoint clauses, p_l=2^-w_l, q_l=1-p_l, Q0=product q_l, v=4Q0(1-Q0), and lambda_l=1. The clauses are precisely the prime implicants: a partial assignment containing no full clause can be extended to make one unspecified literal false in every block. Signed literals can be flipped physically without changing the squared spectrum or influence.

Every spectral coordinate has a unique owner. Each used block is an isolated source SCC and hence one root; there are no children, no attachments and no extra child-order choices. Every root's selected subset is A intersect its block, so kappa=s and M=1. This is a finite terminating decoder: encode the root set once under the fixed initial-root law, read one local subset per root in fixed order, and take their union. The selected run family has no final output ambiguity and receives no posterior entropy credit. Additional successful queue runs are omitted, not presumed impossible.

The direct expansion f=1-2product_l(1-a_l) gives nonempty spectrum P(A)=4product_used p_l^2 product_unused q_l^2 and empty atom (1-2Q0)^2. Summing the other blocks yields mu_l=P(A hits block l)=4p_lQ0. Conditional on a block hit, its subset is uniform on all nonempty subsets; conditional on a coordinate being selected, all other within-block selections are independent fair bits. Physical pivotal events independently give I_l=2Q0 w_l p_l/q_l and I=sum I_l.

### Original residual paid in full

Put D=product_l(1+p_l)-1, so Lambda+log Z=log D exactly. The entire residual is

    R=v log D+sum_l mu_l w_l+(6/5) E sum_selected log(rank/(selected_predecessors+1)).

Labels L_l=0 because lambda=1, but the initial root-name selection cost is paid, not free: its exact contribution is v log D+sum mu_l w_l. Root rarity is <=2I. For normalization, T=sum w_l p_l/q_l>=2sum p_l, since w_l/q_l>=2. Also log D<=sum log(1+p_l)<=log(e)sum p_l. Thus v log D<=log(e)I, retaining its sign. This has a direct block proof and agrees with the baseline weighted activation estimate.

Conditional on selecting rank r, predecessor count X is Bin(r-1,1/2). The exact reciprocal identity E[r/(1+X)]=2(1-2^-r)<=2 and log concavity give expected rank cost <=1 bit per selected coordinate. Therefore the full rank bill is <=(6/5)I. Adding all components gives R<47I/10. This replaces the earlier loose factorial/concavity checkpoint R<13I/2; it is the same mechanism with the sharper exact conditional law.

### Actual queue cost, rather than generic K_ref overhead

With theta_s(j)=min(1,(s/rank(j))^(6/5)) and t_l(B)=[1/(s(s+1))]product_B theta_s/Z_s, the one specified successful run has

    q_pf(A)=D^-1 product_used [(p_l/2)*t_l(A_l)].

Every factor is retained: roots and their absence, subset sizes, subset normalizers/weights, and probability 1/2 of child count zero. Its empty attachment multiset has probability one. Each q_pf is an actual finite conditioned event and these events are disjoint, so sum q_pf<=1. The roots are paid once per used gate. This is the ORIGINAL generator, unlike A008 v1's separate dictionary generator.

The expected root block is <=(2+log e)I. The zero-child bill is <=I. Size costs <=log3 I follow from s(s+1)<=3^s. Subset normalizers <=log(6e)I follow from sum theta_s<=6s and the elementary symmetric polynomial bound. Pointwise log^+(rank/s)<=log(rank/(selected_predecessors+1)), so the actual subset weights cost <=(6/5)I by the same conditional rank law. The resulting nonempty constant is 26/5+2log3+2log e. Gibbs with reference masses 1-v and v*q_pf(A), and h2(v)<=2I, proves full reference cost <67I/5. Rational comparisons 3^5<2^8 and ln2>2/3 certify the displayed constant without floating-point signs.

### Honest boundary

No line in the new restricted theorem remains unsupported; independent review is pending. The first unsupported universal PI-J line is a bound on the ENTIRE joint label/rank/subset expectation under one fixed feasible prime-table reference when supports overlap. The exact uniform local law and forced ownership proved here do not follow from Booleanity alone. Neither A009's coordinatewise pressure obstruction nor A007's root cancellation settles that joint term. Physical prefix rounding adds less than one whole-message bit and is not claimed to be O(I) when I tends to zero.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json preceded every search. The original full domain remains 96 width multisets, every integer partition of n=1,...,9; no automatic dimension escalation occurred. Block permutations and literal sign flips are the only symmetry reductions, justified by physical coordinate relabeling and invariance of the squared spectrum/influence. Memory estimate is 100 MB, below the 300 MB preflight threshold; no GPU or background job was used, and only one certificate computation ran at a time.

Whole A006 review: code/review_a006.py, integer FWHT and independent physical edges for m=1,...,8; generic assignment/SCC/forest/attachment/chronological traces for m=1,...,5; formal a-polynomial residual identities and sequential rational actual probabilities at a=2/5 and 1/2. Counts 3,11,37,143,681; 4,260 recorded assertions, 0.193273 seconds. Rational substitutions validate identities; the analytic proof handles the actual algebraic a.

Block certificate: code/check_blocks.py --pilot passed its final one-variable feasibility pilot in 1.185587 seconds with 518 recorded assertions. The separate full command without --pilot passed all 96 frozen cases, 64,850 recorded assertions, in 167.226981 seconds, within its explicit 900-second cap (under 30 minutes). Each completed full case was immediately written to out/BLOCK_PARTIAL.json. Final out/BLOCK_CERTIFICATES.json contains rational interval endpoints for residual, actual complete run cost and entropy in every case.

The full checker verifies truth tables by integer FWHT and exact physical edges, the exact spectral products/mu/I/v identities, conditional reciprocal identities, local elementary normalizers by independent subset enumeration, and the actual source subset/count costs. Irrational theta values are isolated by rational fifth-power bisection; logarithms use 24 atanh terms after reduction to 1<=y<=2 with remainder <=9/(196*3^49). All operations are rounded OUTWARD to the 2^-80 dyadic grid by exact signed integer floor/ceiling. Thus no floating-point entropy sign supplies a certificate. Histogram aggregation avoids repeating interval arithmetic for equal spectral masses; factorial log aggregation gives the exact uniform-subset rank expectation.

Earlier bounded checks are preserved honestly: v1 hit Python's integer-to-string limit while serializing a large rational; v2 had a stale equality check where outward interval containment was needed; v3 stopped at its 59-second pilot guard; v4 completed 11 mathematical cases but exceeded the pilot time cap. These are implementation/resource failures, not mathematical refutations. The checker changed to symbolic/histogram aggregation, an explicit small feasibility pilot and the originally frozen full domain under a separate bounded job. Exact partial cases remain evidence, but only v5's completed output is reported as the full passing certificate. Total recorded assertions across the completed review, v5 pilot and v5 full job are 69,628; each saved counter excludes its final runtime assertion.

Commands from A008:

    python -X utf8 runs/20261012T005959Z-fleet05-A008-gate-label-compression/code/review_a006.py
    python -X utf8 runs/20261012T005959Z-fleet05-A008-gate-label-compression/code/check_blocks.py --pilot
    python -X utf8 runs/20261012T005959Z-fleet05-A008-gate-label-compression/code/check_blocks.py

## proof dependencies and changed downstream conclusions

Source dependencies: the baseline original conditioned forest interface, elementary symmetric normalizer and h2(v)<=2I estimate; finite entropy/Kraft principles, basic binomial identities and exact Boolean product expansion. A006's v1 is reviewed independently, not assumed for the new unequal-block proof. A007's new equal-width activation theorem is read for scope but not used as an accepted premise. A008 v1's accepted dictionary theorem is likewise not a premise for this ORIGINAL-queue result.

Changed conclusions: (1) the whole A006 statement has another locally saved independent acceptance; (2) the positive block side of the lead's single-gate tribes contrast now has a full all-width original-reference theorem; (3) gate names occur once, roots and zero-child costs are paid, and actual complete run accounting avoids an unnecessary generic multiset/child overhead. This stage follows the lead's review-first rule and produces one scoped continuation, not another broad universal candidate. Independent review and supervisor adoption remain separate events.

## one next mathematical action and independent reviewer

Next: replace the forced-owner/binomial block calculation by a joint posterior label-and-rank moment on the affine/projective line-DNF prime table, consuming A009/A014's existing line-incidence and disjoint-piece proofs. First estimate the expected once-per-used-line name/rank bill for actual source-SCC forests, rather than reoptimizing the already obstructed coordinatewise pressure. A006 can review the unique partition-run and actual probability ledger; A086 or A094 should independently reconstruct the all-width binomial payment and rational certificates. No messages were sent and no other agent's files were changed.

## actual persistence receipts or precise save blocker

The requested run contains REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, REVIEW_A006.md, READ_ONCE_DNF.tex, CODE_COST_LEDGER.json, DERIVATION_NOTES.md, frozen/refined compute specs, author-independent code and exact outputs. out/SOURCES.json pins actual reads; out/RECEIPTS.json records sizes and SHA256. All files are below 20 MB. STATUS.md, WORKLOG.md and LEARNED.md are current inside A008. Shared registries, Brain, git and other agent folders were not modified. Mirror verification, supervisor copying and independent acceptance of the new claim are unobserved, not claimed.

## Universal bridge

C020 whole-set witness cost, under the lead's PI-J target, moves by a complete all-width block-forest closure: residual <47I/10 and full original-queue entropy-reference cost <67I/5, with every gate-name/root/subset/zero-child charge retained; the whole A006 v1 chain is independently accepted at scope. Universally, overlapping prime implicants still lack the forced owner and conditional binomial laws used in this proof. NEXT asks for their joint posterior replacement on the live line-DNF test using existing incidence/orthogonal-piece inputs, so it attacks the unpaid universal name/rank term rather than adding another isolated FEI class result.
