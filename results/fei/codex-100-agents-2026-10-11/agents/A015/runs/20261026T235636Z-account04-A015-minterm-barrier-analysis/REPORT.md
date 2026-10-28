## exact target, quantifiers, hypotheses and units

C020 original whole-set source cost. For EVERY nonconstant monotone Boolean g on a finite uniform s-cube, construct actual positive-anchor CNFs F_L, L>=1, each displayed clause prime and irredundant with one relevant positive private bit, such that H(F_L)/I(F_L)->H(g)/I(g). Entropy and reference costs are in bits; influence is physical uniform-cube total influence. The resulting class has EXACTLY the same supremum H/I as all monotone Boolean functions. This is a reduction, not a solution of monotone or full FEI. Independently review the whole stated A007 signed-core universality theorem and A008 conditional finite extraction theorem.

## sources actually read, revisions and theorem locators

Read machine AGENTS.md, EXECUTION_PROTOCOL revision2026-10-11-execution-v2 in full, own STATUS/LEARNED and previous REPORT, B03 STREAM_NOTES v2, and BOARD written2026-10-26 23:52UTC. Rechecked BOARD through2026-10-27 00:13UTC; A010's newer imbalance result does not supersede the target here. Campaign README/CURRENT_STATUS, registry A015/B03/C020 passages, plan A015 acceptance contract, supplemental campaign/claim/counterexample/seed/mapping files and source inventory were consulted as context. Read A007 CORE_EMBEDDING.md and A008 PROOF_AND_REVIEW.md in full, their exact claims, and their reports. A006's latest REPORT is context only; its bundle is NOT independently accepted here. The previous A015 CORE_FUSION/positive-majority results are already accepted by A007 and are not re-proved.

The four paper text versions were checked at their abstracts and relevant theorem locators, including threshold Proposition8.6 and percolation Theorem1.1. These .txt inputs are cp1252, not UTF8; the first strict UTF8 decode rejected one, then explicit source encoding was used. No paper theorem is a premise of the new reduction. No literature-priority assertion. One math-brain search and one mistake-recall query provide leads, not proof dependencies. out/SOURCE_RECEIPTS.json pins the sources; mutable board hashes refer to the final observation, not the initial snapshot.

## complete derivation or exact first unsupported line

POSITIVE_CORE.md gives the complete proof. Represent g as a positive CNF and let b(z) be its number of false anchors. Repeat every anchor L times, each with a distinct private bit. Conditional success is a(z)=2^(-Lb(z)); it equals one at true cores and at most epsilon=2^-L at false cores. With q=Pr[g=-1] and t anchors,

    I_private=2L E[b epsilon^b]<=2Lqepsilon,
    I_core=sum_i E|a(z)-a(z xor e_i)|,
    |I(F_L)-I(g)|<=2q(s+L)epsilon.

The core formula uses actual nested conjunction events on the SAME private cube, a consequence of positive anchors. It fails for incomparable signed anchors; the source A007 formula correctly retains disagreement on those edges. The scalar b/2^(b-1)<=1 removes dependence on the number of anchors from the influence error.

The signed Walsh coefficient for a nonempty private target is twice the core Fourier coefficient of epsilon^b times its actual group-incidence indicator. Parseval gives exact private mass M=4E[a(1-a)]<=4qepsilon. Collapse the private sector to one cemetery atom. The resulting FINITE core law converges to g's spectrum, and the lost conditional entropy is at most M(s+tL), which tends to zero for EACH fixed g and fixed anchor list. This pays the growing private dimension rather than applying continuity on a growing alphabet. Thus both H and I converge, and nonconstancy gives I(g)>0 before dividing. Every F_L is monotone, proving equality of the two supremum ratios.

An explicit finite entropy error for L>=3 is h2(4epsilon)+4epsilon s+4qepsilon(s+tL). Its proof bounds the total variation of the collapsed core law by4epsilon and gives the finite-alphabet coupling entropy argument. No assumed FEI estimate enters this error bound.

This positive embedding is NOT A007's common-scaling construction: already for AND2 the singleton core amplitude ratio is1-epsilon^2 and the pair ratio is(1-epsilon)^2. Accordingly the exact signed-point reference-extraction identity cannot simply be transplanted. The new theorem concerns entropy/influence limits; it does not assert a finite arbitrary-reference extraction, a free wrapper, or an adaptive-history reset.

REVIEW_SIGNED.md independently reconstructs both source claims at unchanged hashes. The A007 whole theorem HOLDS, including actual false/false core edges, the complete private entropy tail, prime-clause scope, negative conditioning normalizer and finite2K extraction. A008's oriented finite(1+delta) extraction HOLDS, including q<=1/2,2q<=I, denominator(1-epsilon)^2,K>=0, and the ceiling bound. No substantive repair is supplied. Their universal original source is still unpaid.

The FIRST UNSUPPORTED universal line remains: construct a fixed, complete, influence-paid original reference for an arbitrary interacting core. Positivity alone leaves the whole monotone problem, while signed anchors leave the full Boolean problem. The present proof does not identify those two open problems with one another.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json precedes both executions. `python -X utf8 code/check.py --pilot` passes571 assertions on10 positive lifts and32 scalar pairs in0.0383s. `python -X utf8 code/check.py` passes73492 assertions in1.0993s:69 positive lifts from ALL23 labelled nonconstant monotone cores on s<=3 with L1,2,3;286 signed-core source-review lifts;576 fixed A008 scalar pairs s1..64,delta=2^-j,j0..8. Maximum positive physical dimension12, signed10. No symmetry quotient or dimension escalation. Pilot overlaps main and is not added to73492.

New helper, no source executable imported. Literal physical truth tables, integer Walsh transforms and independent physical bit-flip counts check every predicted coefficient and influence; fractions check sector masses, relevance, total variation and all error bounds. Rational logarithm intervals use range reduction, the positive atanh series through degree35 and remainder <=2t^37/[37(1-t^2)], t<=1/3; division by a positive ln2 interval is outward. Entropy comparisons never use floating signs. Floats record elapsed runtime only. AND2 rejects common-scaling transplantation; equal-probability independent signed groups reject the nested-edge shortcut. All b1..128 scalar boundary checks pass; the all-b induction is given analytically.

One bounded core-only Lean check of `a015_linear_le_pow` attempts the scalar n+1<=2^n with explicit target, reviewed source hash, compiler hash and local receipt directory. It reaches RUNTIME_UNVERIFIED at45.619s with no compiler result. No formal target, axiom audit or Lean certification is claimed; a timed-out check neither proves nor disproves the statement. The main mathematical rung is AUTHOR PROOF WITH EXACT FINITE CHECKS, independent-agent review pending. The source reviews are independent mathematical reconstructions, not kernel checks.

Python jobs estimate90MB and finish far below55s. Core-only Lean avoids Mathlib and is bounded45s; no heavy search, >300MB planned job, GPU, remote compute, detached worker, new window or automatic enlargement is used. Governor initially reports ok, CPU82%,available memory9606MB, but only4.3GB free on C:. No shared work is stopped or load-shed. The bounded Lean check expires within its own runtime limit.

## proof dependencies and changed downstream conclusions

The positive-anchor theorem depends only on its direct clause construction, physical nested-event counting, signed Walsh/Parseval identities, finite-alphabet entropy and the proved scalar induction. It does NOT depend on A007/A008 or any FEI hypothesis. The source reviews are separate acyclic outputs, copied at unchanged statement hashes with A015 review records. A007's acceptance of A015's previous theorem is consumed as prior acceptance, never described as independent acceptance by A015 of its own theorem. Only one new unreviewed candidate is created.

The new theorem fills the exact scope left open in A007: all-positive CORE anchors retain the full MONOTONE supremum. It does not enlarge A007's signed-core theorem to a false same-scaling statement. Supplied full-reference pricing would give the corresponding entropy inequality; nonempty suppliers keep their wrapper. Prior history-transfer results remain conditional and retain the same old source and debits.

## one next mathematical action and independent reviewer

A007/A008/A086/A094: reconstruct POSITIVE_CORE.md, especially the nested-event edge identity, growing-private entropy tail and non-affine AND2 control. The shortest next mathematical action is a core-sensitive ORIGINAL source law for nonfactorable interacting anchors, with a strict structural hypothesis that does not merely assume a monotone core has cheap entropy. Test any proposed geometry compression on the canonical positive CNF of an arbitrary monotone core and on the previous amplified-majority family; retain signed fusion, normalization, old debits and BOTH full terminals. No further bounded-core enumeration is proposed.

## actual persistence receipts or precise save blocker

Four protocol files, both proofs/reviews, frozen spec, code and exact outputs are written only in A015's designated unique run. code/persist.py validates exact JSON field sets, unchanged source statements, hashes, case counts, file sizes and readback; out/PERSISTENCE.json records actual landed receipts. A007 hashes statement text; A008 hashes canonical JSON of statement plus hypotheses. The first validator incorrectly assumed the same recipe for both, then used each source's documented recipe and passed without changing either source hash. PACKET_DELTA equals PROGRESS and packet_ids=[A015]. STATUS has two lines; WORKLOG/LEARNED are updated. No remote mirror/adoption, git, mail, shared research index or brain write is claimed. Supervisor owns copying. Checklist completion command subsequently returned exit0 (shared-ledger reread not claimed). The initial working update failed with `RuntimeError('checklist lock held too long')`; no lock is removed. Wake flagged stale personal-context notes, reported immediately and excluded as mathematical premises. Formal verification is unresolved as stated above; research artifact persistence has no blocker.

## Universal bridge

C020 whole-set witness cost advances by two complete source reviews and by a precise all-positive scope reduction: even with irredundant prime clauses and relevant single-bit private blocks, the growing positive-anchor class retains EXACTLY the full monotone H/I supremum. Its physical influence error is <=2q(s+L)2^-L, independent of anchor count, and its growing private entropy tail is explicitly paid. What remains is an ORIGINAL core-sensitive source bound, and the positive embedding lacks the common amplitude scaling needed for A007's exact finite extraction. NEXT targets that missing compression rather than positivity or another fixed-core class, since those shortcuts retain an entire open FEI problem. Full FEI remains OPEN.
