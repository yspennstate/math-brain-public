## exact target, quantifiers, hypotheses and units

For every r>=1 and widths w_j>=1, let U=product_j OR(X_j), with disjoint private blocks X_j of widths w_j, T=z OR U on one shared coordinate z, and f=2T-1. Put epsilon_j=2^(-w_j), a=product_j(1-epsilon_j), J=a sum_j w_j epsilon_j/(1-epsilon_j). Then physical I(f)=1-a+J. Let Q be the normalized A006 anchored clause-mask union law on supports {z} union X_j, with t_j=epsilon_j/2, empty mass 1-t_j and each nonempty mask mass t_j^2/(1-t_j). The fixed normalized reference R=(delta_{ {z}}+Q)/2 satisfies sum_{A nonempty} hat(f)(A)^2 log2(1/R(A)) <=(29/2) I(f); the standard empty/nonempty wrapper costs at most (33/2) I(f). For all w_j=2 and r>=4, the unaugmented Q instead has nonempty cross-entropy divided by I(f)>3(r-1)/224, although H(f)<6 I(f).

Uniform physical cube; all private X_j are mutually disjoint and disjoint from the one shared coordinate z.
Representation, z and widths are public before the spectral set is sampled; R is fixed for the whole spectral set.
Entropy and logarithmic code costs use base 2. Claims concern logarithmic cost with standard asymptotic arithmetic coding, not an uncharged integral prefix length.

The universal target H(f)<=C I(f) for every Boolean f remains OPEN. The divergence concerns a specific reference, not a Boolean FEI counterexample.

## sources actually read, revisions and theorem locators

Read the current BOARD.md, B02 STREAM_NOTES.md and own STATUS.md, plus protocol and campaign context. This stage reconstructs A006-NORMALIZED-SHARED-TAG-PUSHFORWARD-AND-PAID-CLAUSE-CODE@1, SHARED_TAG.md (20261023T112840Z), and A015-ONCE-TAGGED-JOINT-DICTIONARY-REFERENCE@1, JOINT_DICTIONARY_CODE.md (20261023T110145Z), in full. See REVIEW_SOURCES.md and out/SOURCE_RECEIPTS.json for source-bound reviews and exact byte hashes. A010 latest bounded-mixture extension was read as context. Earlier-stage paper/campaign baseline reads are inherited, not represented as fresh full-paper reads. B02 lead notes are the old v2 instructions; current board supplies the newer dependency. Protocol campaign-end metadata is superseded by the user deadline 2026-10-23 14:49 UTC.

## complete derivation or exact first unsupported line

Complete derivation: COMMON_ANCHOR.md. Actual local-mask tuples and anchors are pushed forward to physical unions; the posterior counts both allocations and anchors. No independent clone substitutes for z. Write rho=sum epsilon_j/2. For private nonempty B meeting L blocks, Q(B)=(L/rho) product_active c_j product_inactive(1-t_j), and Q(B+z)>=(2^L-1)Q(B). For widths two, Q({z})=(1/7)(25/28)^(r-1), P({z})=(1-a)^2>1/4 and I<2, giving cost/I>3(r-1)/224. The true entropy stays below 6I.

The repaired fixed reference R=(delta_{ {z}}+Q)/2 pays its global branch once. The core coordinate is public in the supplied representation; for r>=2 it is the unique total intersection. All tuple unions yielding the same final output are summed. Gate names, attachments and subset choices are supplied by the actual anchor/mask sampling law; there is no free output-dependent root or terminal choice. The bound -log R(B),-log R(B+z)<=1+log_+rho+sum_active(2w_j+2)+3rho is averaged using exact physical private-pair mass 2a(1-a) and occupation mass 2a epsilon_j. This yields C_R<=(1-a)+(29/2)J<=(29/2)I, then full wrapper <=(33/2)I. See the proof for every inequality and the prefix-length convention.

First unsupported universal line: arbitrary intersecting-core libraries admit fixed paid selectors and occupation/attachment charges bounded by one absolute multiple of the same physical influence account. This is not proved here.

## executed validation with domain, arithmetic, commands and outputs

Frozen SPEC.json and REVIEW_SPEC.json preceded their searches. Commands: python -X utf8 code/check.py pilot; python -X utf8 code/check.py full; python -X utf8 code/check.py review_pilot; python -X utf8 code/check.py review. All paths relative to this run. Nonpilot outputs PASS: full 15,419 assertions in 1.7264959 seconds; review 2,211 assertions in 15.5384552 seconds, total 17,630. Pilots separately PASS 260 and 155; they are not added to that total.

Full domain: all 39 width lists of lengths 1..3 with widths 1..3, 61 scalar r=4..64 equal-width cases, and direct Boolean tables at r=4,5,6 widths two. An integer weighted physical-union DP is compared with explicit actual-anchor enumeration, physical edge influence and integer FWHT spectra. Source review: 29 paired disjoint width lists, all 196 ordered pairs of nonconstant two-bit indicators using two reference choices, and 115 local-mask count/moment cases. Physical occupation identities and complete expected reference costs are verified. All signs use exact rational arithmetic and certified 16-term atanh logarithm enclosures with a proved tail, outward rounded to 40-bit dyadics; floating values record runtimes only. LOG_CERTIFICATE.md supplies the interval proof.

Resource estimates <=110 MB; all jobs under 60 seconds and no job expected over 300 MB, so no >300 MB job was started. The governor snapshot inspected was stale and supplies no current capacity claim. No other process was stopped or restarted; no running research job remains.

## proof dependencies and changed downstream conclusions

A006 normalized pushforward is accepted independently; its complete disjoint paired-clause cost is also accepted at <155I/24<7I. This does not assert the overlap claim refuted by the new example. A015 generic independent-indicator composition identity and once-tagged mixed-width dictionary bounds (<8I nonempty, <9I full) are accepted at their stated independent-support scope; they are not a logical premise for the new physical-overlap bound. New claim hash/version and source-specific hash conventions are preserved in CLAIMS.json. New theorem is a local proof with exact verification and has no independent acceptance yet.

The old w/2592 fixed-two-polarity obstruction and this new 3(r-1)/224 obstruction concern different references and families; neither revises the other. The older central 251I/5 result is unchanged. The negative control I=5/4 versus clone surrogate 3/2 is respected. No downstream source index or other agent file was changed.

## one next mathematical action and independent reviewer

Test the first nonnested interacting-core pattern using a fixed core-augmented physical-union dictionary; charge selector priors and true occupation to ONE physical influence account. Independent review requested from A006/A015. This addresses the actual universal allocation/selector bottleneck rather than proving another calibration class.

## actual persistence receipts or precise save blocker

All results and exact outputs are saved locally in this immutable stage directory; out/PERSISTENCE.json lists artifact byte counts and SHA256 hashes, with a read-back verification. CLAIMS.json and progress schemas are checked against EXECUTION_PROTOCOL.json; PROGRESS.json and PACKET_DELTA.json are identical and packet_ids=[A008]. STATUS.md, WORKLOG.md and LEARNED.md are updated. No GitHub mirror, brain ingest or downstream adoption receipt is claimed; supervisor transfer remains external to this stage. Brain self-care is degraded/unverified: personal model, state-of-mind and dream sources were stale at wake (98.7h, 83.3h, 34h); personal/dream freshness remains affected. No save blocker.

## Universal bridge

C020 whole-set witness cost moves from a disjoint-support normalized dictionary to a complete common-anchor physical-overlap obstruction and repair: the default law has unbounded cost/I, while a single fixed core branch pays at most 29I/2 nonempty (33I/2 full), with all allocation and final-output multiplicities charged. What remains is a uniform paid selector/occupation theorem for arbitrary interacting cores from one physical influence account. Testing the first nonnested core pattern is the shortest next route toward full FEI because it probes that missing universal interface directly; the known FEI behavior of this formula family is only a calibration, not the claimed advance.
