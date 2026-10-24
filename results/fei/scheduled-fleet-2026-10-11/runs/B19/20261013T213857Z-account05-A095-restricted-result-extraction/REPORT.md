# A095 stage 2: a paid block reference through a common control spine

## exact target, quantifiers, hypotheses and units

Full FEI remains OPEN. Following B19 STREAM_NOTES v2, this stage realizes a fixed normalized reference for XORs of disjoint AND/point-defect blocks, then consumes A094's requested one-coordinate-overlap objection. The extension allows an arbitrary number of unequal private blocks sharing the same conjunction of r>=1 controls. It preserves a supplied arbitrary terminal core reference explicitly.

Entropy, cross-entropy CE(P,R)=sum P log2(1/R), and KL debt are bits; scalar analytic ln uses nats. References are probability laws, fixed across spectral outputs, positive on the actual target support. Costs are ideal negative-log costs with a terminating finite reference decoder. No rounding bit is claimed paid for an optional one-symbol prefix code.

Let q be any Boolean terminal on fresh variables with normalized reference R_q and let h_j=1-2 A_(L_j) on disjoint private blocks, L_j>=1. Define g=q product_j h_j, mu=E g, p=2^-r, F=1+A_r(g-1). Empty-calibrate R_q to match (E q)^2 at empty; its CE, denoted C_q_cal, does not increase. The fixed block reference and its biased activation transfer satisfy

    CE_F <= p C_q_cal +4p sum_j I(h_j)+6rp(1-mu),
    I(F)=p[I(q)+sum_j I(h_j)+r(1-mu)].

If the supplied terminal cost obeys CE_q<=C I(q), then CE_F<=max(C,6)I(F). This conditional statement leaves arbitrary terminal entropy and debt intact. With q=1, the entire explicit shared-spine class has CE_F<=6I(F), uniformly in number of blocks, unequal widths, r and common read. With r=0 and q=1, the disjoint product reference has exact cost H(g)<4I(g). These are complete reference-cost results on specified classes; their underlying FEI conclusions overlap existing composition results, and no novelty or priority claim is made.

The full transfer is stronger than an entropy bound: for any biased Boolean g and normalized reference R, calibrate it to R0(empty)=mu^2. Then the output reference Q is normalized, its entire data debt is retained, and

    CE(P_F,Q)-H(F)=p[CE(P_g,R0)-H(g)].

No forest generator identity is asserted: this is a new explicit output reference, not an uncharged substitution into PI-J.

## sources actually read, revisions and theorem locators

Read BOARD.md supervisor snapshot 2026-10-13 21:34 UTC, B19 STREAM_NOTES v2, own STATUS/LEARNED, and all EXECUTION_PROTOCOL.json v2. The board reports A094's completed uniform-dictionary obstruction and asks A095/A008 for a one-shared-coordinate reference. The B19 lead's block-reference target is followed; a better global order is not retried.

Read A094 run 20261012T044109Z REPORT.md, AUDIT.md sections 1-7, CLAIMS.json, HASH_CONVENTIONS.json and the hash serialization locators in code/finalize.py. Read A086 run 20261011T234041Z ACTIVATION_DEBT_PROJECTION.md and A008 run 20261012T005959Z READ_ONCE_DNF.tex, especially equations (1)-(5). A094 had already supplied the disjoint occupied-block comparison; this stage consumes it and advances to biased, common-control and terminal-inclusive transfer rather than republishing it as a new FEI theorem. A008 already pays an original forest reference for read-once DNFs; this report does not conflate that OR forest with the XOR/reference used here.

Read prior A095 stage-1 claims/proofs for the candidate being refined. The earlier B19 hash diagnosis is corrected using A094's demonstrated serialization convention: hashes of canonical statement-plus-hypotheses JSON match the lead's declared hashes. No shared source needs repair. The stage-1 immutable artifacts are preserved and a source-bound correction is in out/HASH_DIAGNOSIS_CORRECTION.json. Source byte hashes and exact paths are in out/SOURCE_RECEIPTS.json. No new external literature statement is used.

## complete derivation or exact first unsupported line

DERIVATION.md supplies the complete reference construction, normalization, decoder, debt identity, six-influence scalar bound, iteration over r controls, local occupied-block cost, and conditional arbitrary-terminal application. Key steps are summarized here to make the mathematical delta explicit.

First calibrate the empty atom of a normalized core reference. By the KL chain rule, the entire decrease in CE is the Bernoulli divergence between the true and reference empty/nonempty sectors; conditional data debt is unchanged. Set R0(empty)=mu^2 and scale the remaining reference to total mass 1-mu^2. If that mass is zero, use the point mass. Calibration uses the instance's known scalar bias and fixed reference parameters, not a spectrum-dependent choice for each output.

The activation reference has vacuum mass [1-p(1-mu)]^2, each nonempty control-only subset mass p^2(1-mu)^2, and each nonempty data T with each control subset U mass p^2 R0(T). It sums to one. In the data sector a finite generator draws nonempty data from R0 conditioned on that sector and a uniform control subset; control-only and vacuum sectors are explicit. Every label, absent block, normalization and local subset is included. The actual spectrum has the identical formula with P_g(T) in place of R0(T). Expanding CE-H gives exactly p D(P_g||R0). Thus both the bias sectors and all conditional control debts are fixed, and no arbitrary terminal bill has disappeared.

For one control, put t=(1-|mu|)/2. Exact conditional erasure contributes 2t(1-t) from data plus the entropy packet on masses (1-t)^2,t^2. ln(1+x)<=x bounds this packet, and the scalar JS inequality gives JS<=2t/ln2. Optimizing the resulting one-variable upper bound proves

    H(F)-H(g)/2 <= [2+(2+exp(-1/2))/ln2]t <6t<=6 Inf_control.

The strict constant uses only ln2>2/3 and e>9/4, both proved by positive elementary series. DERIVATION reconstructs the scalar JS inequality directly; no unreviewed campaign claim is needed. Inserting the exact retained debt yields CE_F<=CE_g_cal/2+6 Inf_control. Iteration over fresh controls gives p CE_g_cal+6rp(1-mu), with precisely the same direct reference formula.

The private block reference chooses occupied blocks independently with probabilities 4*2^-L_j(1-2^-L_j), then draws a uniform nonempty local subset. Its probabilities are explicit rational functions of widths and equal the squared spectrum of the specified defect blocks by direct Fourier expansion. Occupancy labels cost sum h2(delta_j)<=2 sum I(h_j); local subset cost is <2 sum I(h_j). This proves the requested O(I) reference on the global-order obstruction with all labels retained. Uniform local subsets replace an unnecessary heavier rank law here; the conditional binomial predecessor law would also pay within-block ranks, as A008 already shows.

For q=1, sharing common controls gives

    product_j(1-2 A_r A_(L_j))=1+A_r(product_j h_j-1).

It therefore realizes a family of arbitrarily many gates sharing r physical coordinates, and CE<=6I, independently of read. For a general terminal q, product factorization before activation adds C_q_cal and the local block costs; its terminal component appears multiplied by p in the final bound. A bounded terminal reference is a hypothesis, not a consequence of this construction.

REVIEW_A094.md independently reconstructs A094-CONCRETE-ACTIVATED-DICTIONARY-DEBT-AND-RANK-BOUNDARY v1 at its full stated scope. The diagonal t=4^L,r=4L+1 retains C/I>=2^(L-2) for the uniform dictionary while H/I<4 and I tends to zero. The exact all-order rank limit follows from the equal-inclusion factorial identity, the block second moment, and size-biased Jensen with integral factorial error bounds. No substantive source repair was supplied, so this is an independent acceptance.

Queue discipline: the stage starts by consuming this independent audit dependency. Its mathematical reference application is registered as v2 of A095's existing rank/KL C020 candidate, retaining the v1 statement and adding this concrete paid application. The separate stage-1 pivotal-height candidate remains pending. No third broad universal candidate is opened, and no self-review is labeled independent acceptance.

First unsupported line: for incompatible shared control events, or an additional shared private coordinate, construct a normalized output reference and influence-pay its entire induced data/conditional-control debt while retaining the arbitrary terminal CE. The common-spine factorization cannot justify that line. General universal terminal reference construction also remains FEI-strength and unpaid.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was saved before computation. The 60-second pilot cap, 80 MB memory estimate, dimensions and parameter menus were fixed. No job above 300 MB was planned or started. No GPU, heavy/background process, external write or automatic dimension increase was used.

Command from the A095 folder:

    python -X utf8 runs/20261013T213857Z-account05-A095-restricted-result-extraction/code/check.py

PASS: 32,548 exact assertions in 16.560 seconds. Domain: all 276 labelled Boolean cores on 1..3 bits, three fixed full-support rational references and r=1..3 (2,484 cases); 27 unequal private-block tuples and r=0,1,2 (81 cases); all terminal tables on 1..2 bits with five private-block menus and r=1,2 (200 cases); and 31 exact diagonal parameter cases L=2..32 without truth tables. Maximum actual truth-table dimension is 10. Sorted block tuples use only the justified permutation of disjoint blocks; arbitrary Boolean cores use no symmetry quotient.

Integer FWHT and independently enumerated physical edges verify actual probabilities and influences. Fraction arithmetic proves normalization, calibration and spectrum identities. Exact rational linear combinations of prime logarithms prove debt, CE and scalar-decrement identities by zero coefficient vectors. Nonnegative inequalities use 40-term rational atanh-series enclosures after reduction to [1,2), with remainder at most 2 z^81/[81(1-z^2)]. Every decisive sign is rigorous; no floating entropy is accepted. Runtime is observational. The analytic derivation separately supplies all-dimensional and all-parameter proofs.

## proof dependencies and changed downstream conclusions

The transferred reference uses exact Fourier expansion and normalized KL disintegration. Its scalar payment uses a directly proved JS inequality and elementary calculus. The private-block cost uses the standard cube edge-isoperimetric variance-entropy bound (also reconstructed in prior A095/B19 level proofs). Dependencies are finite and acyclic; the previous exact rank-minus-KL equivalence is retained unchanged in v2 and supplies no universal payment premise.

A094's concrete dictionary obstruction is now independently accepted locally. A086's balanced projection is consumed at its already-reviewed scope; the present formula extends the explicit transfer to biased cores and identifies the full residual instead of inferring a universal core cost. A008's OR forest costs are not imported as XOR identities. The new application remains author-proved pending independent review. B20/A086/A008 should use the exact terminal-inclusive bound and cease control-only repairs for uniform arbitrary dictionaries. Shared indices were not modified.

The hash correction is operational only: A095's stage-1 source hash warning was a convention error, not a problem in the B19 theorem. The new correction pins both hash forms and original source bytes so B20 can retract that warning without altering history.

## one next mathematical action and independent reviewer

Next: use two private blocks and two control events with opposite literals on one shared coordinate, and compute the exact signed output spectrum and induced debt of a single normalized reference with first-exposure ownership. Retain the weighted CE_q for any arbitrary terminal and prevent double-charging the shared coordinate. The smallest case is A={z=a=+1} and B={z=-1,b=+1}. These have a common physical z but no common activating literal, so they cannot be folded into the shared-spine class by adjoining a,b to the private blocks. This removes the precise structural identity that closes this stage, rather than enlarging a settled census.

Independent reviewer: A094 for the biased transfer and common-spine application; alternate A086. The local KL identity and six-influence proof should be reconstructed before use beyond this class. Review designations are saved handoffs; no message to another agent was sent and no review completion is assumed.

## actual persistence receipts or precise save blocker

The run contains REPORT.md, CLAIMS.json, PROGRESS.json, byte-identical PACKET_DELTA.json, DERIVATION.md, REVIEW_A094.md, frozen spec, independently written checker and exact results. Source/hash-correction and persistence receipts are in out/. The rolling STATUS.md, WORKLOG.md and LEARNED.md are updated only under A095. Schemas match protocol fields; its parenthetical packet_ids documentation is interpreted as the packet_ids JSON key required by compatibility. Files are under 20 MB. Local persistence is complete; supervisor copying, mirrors and adoption remain unobserved.

## Universal bridge

This stage moves C020 whole-set witness cost by replacing the failed global-order/uniform-dictionary code with a fixed fully normalized block reference, paying the entire obstruction family below 4I and its arbitrarily high-read common-control extension below 6I, and preserving arbitrary terminal reference debt with its exact activation coefficient p. It also closes the source-bound A094 dependency without reopening settled baselines. No universal FEI constant improves: incompatible overlap transport and the terminal reference bound remain unpaid. NEXT is the shortest identified route toward full FEI because it breaks the single common-spine identity at one owned shared coordinate while testing the whole reference debt; another disjoint-block or common-control theorem would only repeat the now-paid mechanism.
