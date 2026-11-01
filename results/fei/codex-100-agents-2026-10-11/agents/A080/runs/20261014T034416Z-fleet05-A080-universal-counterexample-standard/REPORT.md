# A080 stage4: one budget for arbitrarily repeated escape/return cycles

## exact target, quantifiers, hypotheses and units

Audit the previously unpriced repeated-excursion mechanism: matched common-policy h steps interleaved with full one-flip J=-h(x xor1) rare-escape episodes. h is negative at binary indices{0,1,2,4,8,16,32,6,17,40}, zero encoding sign+1. Every seed is an actual nonconstant finite Boolean function on the uniform physical cube; every substitution uses six identical disjoint copies and retains all coordinates. A common step uses minority-negative inputs up to7/32 and their common complement otherwise. Escape starts only at minority<=1/16 and ends when that bias first exceeds1/16; a terminal partial episode is allowed. All entropies are bits. Prove a dimension- and cycle-count-independent UPPER correction with complete starting H/I retained. Full FEI is OPEN.

## sources actually read, revisions and theorem locators

Read full EXECUTION_PROTOCOL.json revision2026-10-11-execution-v2; BOARD.md supervisor snapshot2026-10-14 03:35 UTC, including the initially truncated middle read separately; B16 STREAM_NOTES.md v2 unchanged2026-10-11 23:25Z; own STATUS.md. The lead baseline standard and sandwich review are finished and not repeated. Read A07420261014T030615Z REPORT/CLAIMS: scope-preserving independent acceptance of our prior g3 obstruction,503 exact checks. That acceptance is consumed unchanged in this CLAIMS.json.

Read A07220261014T020611Z PROOF/CLAIMS: one-flip mean map, unequal outer pivotal directions, exact entropy ledger and repeated-excursion warning. Read A07520261014T005346Z PROOF portions on localization and retained rare-tail entropy; A08420261014T030826Z PROOF portions on fixed-policy payment and the cycle gap; A08920261014T030932Z REPORT/CLAIMS: reciprocal-influence moderate payment and C<342p^2 rare envelope. Their relevant identities/envelopes are independently reconstructed below; no full new acceptance of the A072 erasure-loss theorem or the entire A075/A084/A089 claims is asserted. out/SOURCES.json fingerprints consulted local sources. Earlier campaign and manuscript readings remain retained context; no new literature review or brain query was needed.

## complete derivation or exact first unsupported line

PROOF.md supplies the complete all-dimensional argument. The new potential is mu=Var(g)/I(g). Exact composition gives R_next-R=C/(QI), with R=H/I, C=H_p(outer)-Qh2(Var(g)); the entire terminal H(g) remains. Biased spectral first moment Q*Var(g) dominates output variance, so J steps never increase mu. For common h, the degree-six polynomial P=4-28p+109p^2-152p^3+100p^4-32p^5+4p^6 controls2Qv-3Var_p(h). A16-box exact Bernstein positivity certificate on the full interval[0,1] gives mu_next<=2mu/3 at every common step, under either common sign and every actual core dimension.

For the prescribed common policy, the signed full entropy correction costs at most8mu per step. Moderate cases use actual pivotal lower bounds and spectral marginal subadditivity; the rare case reconstructs C<342p^2 by canceling the complete Qh2(v), giving C/(Qv)<76/15<8. For a full one-flip escape, the bias increases between3p and4p. Unequal direction entropy is bounded using min(q_j,1-q_j)<=5p and Q>=11/4. Reverse geometric bias summation shows the ENTIRE episode costs at most(225/44)mu_start. This sharpens the scale of payment needed for repeated accounting, without claiming a sharper erasure-loss bound.

At most one escape episode can occur after any given count of common steps, because every completed episode exits the rare band. Every terminal partial episode is paid too. Hence sum of common-step mu and sum of episode-start mu are each at most3mu_seed. Telescoping all signed corrections proves

`H(F)/I(F) <= H(g)/I(g) + (1731/44)*Var(g)/I(g) < H(g)/I(g)+40`.

This holds for EVERY finite depth and arbitrarily many eligible escape/return cycles, independent of core dimension and starting rarity. A fixed finite seed under this named strategy cannot produce an unbounded-H/I disproof. Tensor powers retain the seed ratio and make Var/I smaller; dummy coordinates and output complements preserve the bound. A starting family already having unbounded H/I is not excluded or manufactured by this theorem.

First unsupported universal line: bound the retained arbitrary rare core's full conditional erasure/entropy cost from a noncircular physical budget, or supply a different actual operation with a proved divergent H/I ledger. No absolute FEI constant, selectable-erasure bound, shared-data transfer, arbitrary mixed block signs, or physical stopping-tree payment follows from this composition theorem.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes the pilot and full check. Pilot PASS8388 assertions in1.1042seconds:16 polynomial boxes,4 scalar profiles and2 actual12-bit compositions. Full PASS115869 assertions in5.6993seconds: the same16 boxes,13 frozen exact scalar profiles (including the actual g3 bias) and all28 compositions of14 nonconstant two-bit cores under both actual gates. Integer Walsh checks every one of114688 parent coefficients against the hierarchical product formula; direct physical edges check all336 parent coordinate influences. Complete entropy identities are analytically proved and validated by independently evaluated enclosing intervals, rather than float equality.

SYMBOLIC_SPEC.json precedes a second exact representation: reconstruct both output-probability polynomials and all12 directional pivotal polynomials from integer vertex/edge counts, with no coordinate symmetry quotient. PASS23 assertions in0.00205seconds. These global polynomial identities and Bernstein coefficients supply exact continuum certificates; the finite bias fixtures only supplement them.

Commands from A080:

`python -X utf8 runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard/code/check.py --pilot`

`python -X utf8 runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard/code/check.py`

`python -X utf8 runs/20261014T034416Z-fleet05-A080-universal-counterexample-standard/code/symbolic.py`

Arithmetic is integer/Fraction throughout. Logarithms use32 positive atanh terms after power-of-two range reduction, proved tail2z^65/[65(1-z^2)], outward2^-128 argument brackets, certified ln2 division and2^-80 output rounding. No float selects a certificate sign. out/BERNSTEIN.json, PROFILES.json, PHYSICAL.json, SYMBOLIC.json and VALIDATION.json save exact outputs; profiles are checkpointed immediately after each completed case. Frozen estimate100MB, pilot cap60seconds/full180seconds; all successful runtimes satisfy the budgets. Serial jobs only, no expected>300MB job or memok override, no GPU/detached process, no automatic bias/depth escalation. Peak memory was not measured. No failed mathematical check occurred.

## proof dependencies and changed downstream conclusions

The proof reconstructs its complete chain from actual gate vertex/edge polynomials, orthogonal biased expansion, Shannon chain rule, a scalar entropy inequality, the exact Bernstein certificate and geometric summation. Pending universal source claims are not premises. A074's independent acceptance of A080@1 is recorded as a consumed review, preserving the exact statement/hash and source proof; the new repeated-excursion theorem is author-proved and awaits independent reconstruction.

A072/A075/A084/A089 can now retire the specifically named repeated one-flip/common-policy entropy-growth frontier, including unrestricted numbers of excursions. Their scoped single-escape and fixed-policy proofs remain intact. The new variance/influence potential pays the cycles from one budget, rather than summing a fresh absolute allowance per visit. This result does not resolve the hard rare-core supremum in A075's localization, and those arbitrary terminal cores must not be dropped. It also does not justify one-shot erasure monotonicity, already refuted by the reviewed g3 fixture.

## one next mathematical action and independent reviewer

Independently reconstruct A075 rare/small-influence erasure-supremum localization, then audit its retained rare-core conditional-erasure target on the accepted g3 fixture; require a noncircular core payment or an actual unbounded rare-core family, rather than another escape/return growth search.

A072/A089/A075 should independently reconstruct the episode-scale bound and event-count/geometric argument; A074/A092 should challenge the Bernstein contraction certificate, all six unequal J directions and retention of complete terminal entropy. Source-bound next consumers are recorded locally; no messages or other agents' files were written. The lead baseline direction is completed; new dependency dispatch is followed without mathematical disagreement.

## actual persistence receipts or precise save blocker

REPORT.md, CLAIMS.json, PROGRESS.json and identical PACKET_DELTA.json, full proof, frozen specs, exact checkers and outputs are saved in this run. STATUS.md remains exactly two lines; WORKLOG.md and LEARNED.md are updated. out/PERSISTENCE_RECEIPTS.json binds artifact and rolling file sizes/SHA256 and excludes its own circular hash. All files are below20MB. Local save is complete; independent review of the new theorem, shared registry adoption, supervisor copying, mirror verification and downstream mathematical use remain separate and unverified. No shared tree, brain, git repository or other agent folder was modified.

**Universal bridge:** This stage moves B16's actual-counterexample standard and the signed composition bridge adjacent to C018/C019 by closing the previously unpaid arbitrarily repeated one-flip escape/common-policy return mechanism: its total H/I increase is at most(1731/44)Var(seed)/I(seed), hence below40, with every terminal core entropy retained. It improves no universal FEI constant and claims no physical restriction-tree payment. The exact remaining bridge is the arbitrary localized rare-core erasure/entropy cost or a new operation outside this now-bounded strategy. NEXT reviews and attacks that retained universal rare-core target, because a depth or sign search inside the closed excursion mechanism can no longer produce the needed unbounded ratio.
