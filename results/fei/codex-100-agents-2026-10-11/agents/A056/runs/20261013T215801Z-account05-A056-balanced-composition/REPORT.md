# A056 stage 3: common control reserve for distinct priority cores

## exact target, quantifiers, hypotheses and units

Follow the productive continuation of the adopted biased-child interface, consuming A057's newly completed one-core cap and its stated shared-control frontier. For every finite uniform controller c and two arbitrary Boolean sign branches u,v on mutually disjoint data cubes disjoint from c, price the full controller-only physical entropy path while retaining pH(u)+(1-p)H(v). Then price two priority events sharing one physical fair control bit, with disjoint private masks and distinct disjoint cores. All H and raw nonempty Hplus are in bits; all I are sign-function total flip influence. Deterministic blocks and bias endpoints are included. Hplus is not conditioned entropy or H-h2(Var).

The exact theorem, proof, scalar constants, control ownership, and first unsupported line are in PROOF.md. This continuation pays a previously unpriced distinct-core shared-control path; it is not a solution of FEI or a rediscovery of balanced substitution. Before this one focused interface extension, REVIEW_A057.md verifies A057's new cap price with a separate implementation. A056 authored its upstream biased-interface premise, so the record explicitly defers independent acceptance of the full dependency chain to A091/A090; it satisfies the verify/repair-at-cap direction without claiming an independent acceptance or opening a broad candidate.

## sources actually read, revisions and theorem locators

Read BOARD.md snapshot 2026-10-13 21:55 UTC, B12 STREAM_NOTES v2 (still 2026-10-11 23:30 UTC), own STATUS, and EXECUTION_PROTOCOL v2. The lead's requested biased split was completed in stage 2 and is not repeated; A057's stage-2 report and actual review consume it. Read A057/runs/20261012T003930Z REPORT, PROOF and CLAIMS, including its A056 v2 acceptance and its new cap claim; source-specific verdict is recorded in REVIEW_A057.md. Read A028/runs/20261012T011208Z REPORT's arbitrary-controller spectrum, semiconvex scalar price C0, disjoint budget/terminal scope and shared-control exclusion. This stage derives the same scalar constant for TWO nonconstant branches rather than assuming the one-core formula extends. Read A023/runs/20261012T010933Z REPORT's shared-core compatible event ownership and exposure restriction; our distinct-core priority partition is a different target. Read A059/runs/20261011T224320Z REPORT's no-repeated-subformula-bank control; no whole-subformula credit is reused here. Prior A056 v2 REPORT supplies the saved interface and source lineage. All actual source byte pins are saved in out/source_manifest.json. No external literature novelty or fresh full-manuscript audit is asserted.

## complete derivation or exact first unsupported line

PROOF.md gives a complete all-dimensional proof. Its reusable selector statement is: with sign controller a=1-2c, p=E c, Va=Var(a), branch means m,n, and d=(1-mn)/2, the actual controller path cost satisfies

    Pi_H=H(cu+(1-c)v)-pH(u)-(1-p)H(v)
         <=d Hplus(a)+C0 d Va,
    C0=2+2/ln2+1/(sqrt(e)ln2)<6.

The data branches can be arbitrarily biased and nonconstant. Their empty-row amplitudes collide coherently through M=p m+(1-p)n; the exact correction retains eta(M^2)-p eta(m^2)-(1-p)eta(n^2). The nonempty data rows are separated only by the physical disjointness assumption. The exact controller and terminal influence decomposition is d I(a)+p I(u)+(1-p)I(v).

This removes the apparent additional branch-bias surcharge: the same C0 as A028's constant-versus-core activation suffices for two distinct branches. The proof uses z=(m-n)^2/4<=d^2, Vu+Vv=4(d-z), semiconvexity of eta(mean^2), and an exact scalar maximization. The all-bias cases p=0,1, d=0 and z=0 require no division; their limiting formulas are direct.

For E1={s=+,A=1}, E2={s=+,B=1}, give E1 priority. With private probabilities p,q and negative core masses delta_u,delta_v, reveal s, determine A only on s=+, and determine B only on s=+,A=0. Stop at u,v, or +1. The exact four influence accounts are

    Q_s=p delta_u+(1-p)q delta_v,
    Q_A=(1/2)(delta_u+q delta_v-2delta_u q delta_v) I(1-2A),
    Q_B=(1/2)(1-p)delta_v I(1-2B),
    I_terminal=(1/2)p I(u)+(1/2)(1-p)q I(v).

The shared physical bit is charged exactly Q_s once, and the full root influence is the sum of these four accounts. Actual terminal entropy is (p/2)H(u)+((1-p)q/2)H(v), retained even for arbitrary hard cores. If each private controller has a strong certificate Hplus<=T(I-Var), the path has constant max(C0,T_A,T_B) against Q_s+Q_A+Q_B. If both cores have terminal constants L_u,L_v, the complete root cost uses max(C0,T_A,T_B,L_u,L_v). Ordinary controller certificates instead give K_A+C0 and K_B+C0. These are conditional quantified transfers, not inferred arbitrary-core certificates.

The first unsupported universal line is the nonempty signed collision when the two actual branch data cubes overlap, together with a universally admitted terminal policy. At shared data, the separate nonempty coefficients used in the selector spectrum add BEFORE squaring. Our proof does not bound that term by the same controller influence or erase H(u),H(v). The remaining problem is thus localized more sharply than a blanket ownership objection: the common control bit and mean-only collision are paid; nonempty branch collision and arbitrary terminal FEI remain unpaid.

## executed validation with domain, arithmetic, commands and outputs

out/FROZEN_SPEC.json was written before running code/check.py. The independent helper uses an integer FWHT, rational spectra, rational prime-log entropy vectors and denominator-cleared integer comparisons for signs. Physical influence is also checked by actual edge counting. It imports none of A057's code.

Pilot command: python -X utf8 code/check.py --pilot, 16 controller cases and a priority fixture; all passed in 0.0235169 seconds. Main command: python -X utf8 code/check.py. Main frozen domain: all 16 two-bit controllers times all 16^2 pairs of two-bit cores (4096 selector spectra), all 4^2 one-bit private controllers times all 16^2 two-bit-core pairs (4096 actual seven-bit priority roots), and all Boolean n=2,3 cores at r=1,2 point activations in both forward/reverse physical core orders (1088 independent cap review trees). No sampling or symmetry quotient is used. The maximum truth table has seven physical bits; no dimensions escalate.

The finite selector correction bound is checked exactly with rational constant 6. The analytic proof gives the sharper symbolic C0. The finite cap review tests bank<=5I, which is stronger than the source symbolic K>5 on this declared domain, without claiming that improved constant universally. All 4096 selector cases, 4096 priority roots and 1088 cap-review trees passed in 66.6945303 seconds, below the frozen 180-second main cap. Planned vs actually completed counts and measured runtime are distinguished in out/checks.json; no floating arithmetic is used as proof. The helper's estimated memory is 110 MB, so no >300 MB job, memok override, or heavy search is involved. The proof establishes the all-dimensional bridge separately from this finite validation.

## proof dependencies and changed downstream conclusions

The new controller/priority theorem is reconstructed from the actual Fourier spectrum and elementary convexity; it does not depend on A057's cap claim, which is verified separately. A028 supplies the scalar strategy/C0 provenance, and the complete new proof rederives it for distinct branches. A056 v2 has now been independently accepted at scope by A057 (the source review is consumed and pinned); stage-2 source files remain unchanged. A057-CAPPED-RECENTERED-ACTIVATION-TREE-BANK v1's new pricing steps are verified at its exact core-first point-mask scope, with no repair or universal-terminal acceptance. Since A056 authored its upstream premise, full-chain independent acceptance remains A091/A090's obligation. The source's statement digest is inconsistent with its actual UTF-8 text; out/source_digest_note.json records both, and our local transcription recomputes its own digest while pinning source file bytes. This is a provenance correction only, not a theorem repair. No shared registry or other agent's status is modified.

A057/A058/A060 can replace the unpriced shared-bit two-core control path by the exact account above, provided private/controller/core blocks have the stated disjointness. A028 can consume the two-branch controller transport instead of reusing a constant-leaf specialization. A095/A094 may compare this entropy-path ledger with their whole-set reference debt for shared-control events, but reference cross-entropy does not follow automatically from entropy. A059 can attach an actually certified stopping frontier with both terminal reserves preserved. No broad overlap subadditivity is assumed.

## one next mathematical action and independent reviewer

Next: remove precisely the disjointness of u,v in the paid two-branch selector, write the paired nonempty-data coefficient correction, and test a versioned price against controller influence PLUS a single owned branch/terminal reserve. Use shared-core cancellation and bent splice as mandatory controls. This addresses the one algebraic separation still used by the present proof; do not repeat the now-priced private-mask/shared-bit case. A091 is primary independent reviewer of the new selector/priority proof and A057 cap full chain; A090 alternate. A057 may consume A056's price reconstruction and exact checks, with the independence limitation intact; this stage's new theorem remains pending independent review.

## actual persistence receipts or precise save blocker

REPORT, PROOF, REVIEW_A057, CLAIMS, PROGRESS, identical PACKET_DELTA, code/check.py, frozen spec, pilot/main outputs and source manifests are saved only inside A056's assigned stage directory. Rolling STATUS/WORKLOG/LEARNED are current. out/receipts.json verifies local bytes and hashes, and out/schema_validation.json records protocol keys and claim digests. Every artifact remains below 20 MB. No shared files, other agents, brains, repositories, mail or trading trees were modified. New independent review, supervisor copying, mirror verification and downstream adoption are pending; local saving alone does not imply them.

## Universal bridge

This stage moves C019 and the lead-named common-control ownership frontier by paying the full physical control path for two distinct priority cores sharing one actual bit, using the existing scalar constant C0<6 and a single Q_s debit, while retaining both exact terminal entropies; it also verifies A057's capped one-core price while deferring independent full-chain acceptance because of the upstream authorship link. It removes the mean-only branch collision and common-control reserve from the unpaid ledger, but gives no payment for nonempty shared-data collision or arbitrary terminal H/I. NEXT removes exactly that final spectral-row separation and tests a joint collision/terminal reserve, which attacks the remaining universal transport step rather than producing another unrelated class estimate.
