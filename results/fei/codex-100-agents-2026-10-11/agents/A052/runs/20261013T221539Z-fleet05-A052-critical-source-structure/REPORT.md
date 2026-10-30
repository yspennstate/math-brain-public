# exact target, quantifiers, hypotheses and units

A052/B11 stage 20261013T221539Z-fleet05-A052-critical-source-structure. All-dimensional target: a structural restriction on least-essential-dimension fixed-K Boolean FEI violations under every proper physical cut. Entropies are in bits; K>=0. Full FEI is OPEN. Physical-descendant ratio criticality is a weaker hypothesis and is kept separate.

# sources actually read, revisions and theorem locators

Read the full execution protocol revision 2026-10-11-execution-v2, current BOARD (2026-10-13 22:15 UTC), own STATUS and preceding stage outputs, and B11 STREAM_NOTES v2 (2026-10-11 23:3xZ). The lead's old beta-composition target was completed last stage. New A051 stage3 JOINT_CHANNEL_PROOF sections1--5, REPORT, CLAIMS and NAND control are read and independently reconstructed. A018 baseline REPORT's row classification and zero-channel guard were read; A053 stage2 REPORT's continuity/individual-child scope was consulted, not adopted as a proof premise. Those report reads were partial tool views, not audits of their full proof chains. No new paper or web result is needed. Exact consulted source hashes are in out/SOURCE_MANIFEST.json.

# complete derivation or exact first unsupported line

CRITICAL_PHASE_PROOF.md gives a complete elementary proof. Zero row collision turns normalized rows into actual Boolean signs on the queried block. Minimality among all Boolean K-violators permits FEI(K) on those phases, pricing B_A<=K I_A; physical children price the terminal deficit. This rules out every isospectral proper block. The near-phase proof bounds Fourier-law TV by modulus error, applies an explicitly proved maximal-coupling entropy inequality and influence range bound, and concludes D_K<=Gamma+psi_a(eta)+Ka eta, with eta<=sqrt(C_A). The explicit small-C inequality is saved in the proof. No phase is assumed to be a physical descendant. A four-bit quadratic tensor has all physical child ratios<=2 and a zero-channel full-factor block; the weaker ratio-critical exclusion is false.

First unsupported line: a dimension-independent K and a rule selecting a proper block whose collision plus phase-error budget is below D_K(f), or directly B_A+Gamma_A<=K I_A, on every dimension-minimal K-witness. The error currently depends on a,K and can dominate the deficit. Positive collision alone is not payment.

# executed validation with domain, arithmetic, commands and outputs

Frozen specs precede both executions; estimates60MB and maximum55 seconds, no >300MB job or memok requirement. The initial spec erroneously counted 278 small tables/280 total; the corrected v2 spec states 276 small/278 total. The original is preserved, the actual domain never changed. v2 added quantitative phase-lemma tests after the first successful pilot.

    python -X utf8 runs\20261013T221539Z-fleet05-A052-critical-source-structure\code\check_phase.py

Completed final v2: 69,395 assertions, 1.443468 seconds helper runtime; all276 Boolean tables n=1,2,3, 1552 proper cuts of nonconstant tables;62 named NAND cuts;14 four-bit tensor cuts. All16 three-bit K=2 violations have every smaller child at or below K and positive collision at all96 proper cuts. Direct character sums and physical edge counts reconstruct Walsh/influence independently of A051 code. Fraction arithmetic verifies signed convolution identities and rational squared TV/modulus inequalities, avoiding square roots. Entropy signs use 40-term atanh tails with 96-bit outward rational enclosures. Every row entropy-continuity and influence-error inequality is checked exactly. No floating-point sign is accepted. The initial v1 pilot passed45,876 checks in2.401567 seconds; its stdout was returned, while CHECK.json was replaced by the successful strengthened v2 output.

NAND48.json independently matches the exact H,B,J,Gamma source vectors and truth hash; unique collision-affordable mask48 and singleton costs>3.19 are checked. Its sole nonconstant child has positive root-ratio deficit. This child prevents classifying the root as critical; it is retained throughout.

# proof dependencies and changed downstream conclusions

REVIEW_A051.md and out/REVIEW_RECORDS.json independently accept A051-JOINT-COLLISION-DESCENT@1 at its exact stated scope; no substantive repair was supplied. Global adoption is not claimed. The new phase proof rederives its needed entropy, restriction and collision facts and has no pending theorem dependency. A051's analytic review of the previous A052 collapse is now consumed from its source; no duplicate collapse search is run. The stream cap is respected by reviewing a live source-complete candidate before this narrowly scoped application. Source registry pending candidates are not silently relabelled.

Changed downstream conclusion: zero-channel arbitrary-phase obstructions are excluded specifically on dimension-minimal threshold witnesses, even though they remain valid against unconditional prescribed-block payment and against physical ratio criticality alone. This is why criticality improves the argument without reviving component pruning: all lower-dimensional Boolean phases are available only under the stronger, explicitly named minimality hypothesis. The robust bound records the exact price for leaving that zero-channel boundary.

# one next mathematical action and independent reviewer

Next: select a proper block on a dimension-minimal K-witness with sufficiently small signed collision and Boolean-phase approximation error to contradict the saved deficit bound, keeping row masses and terminal deficits. A051/A055 and B11 lead are immediate consumers; A090/A094 should independently reconstruct the norm-to-TV bound, concave entropy cap, and distinction between essential-dimension minimality and physical descendants. No outbound messages were sent.

# actual persistence receipts or precise save blocker

The four protocol files, two proof/review notes, code and exact outputs are saved in this run. PROGRESS and PACKET_DELTA are byte-identical. out/ARTIFACT_MANIFEST.json checks hashes, field sets and the20MB cap. Rolling STATUS, WORKLOG and LEARNED are updated only in A052. External mirrors, registry adoption and review of the new phase theorem are pending, not claimed.

**Universal bridge:** This stage moves C019 stopping-tree payment through B11's critical block-selection target: it independently admits the signed-collision interface, then excludes all exactly isospectral proper blocks of a least-dimensional threshold violation by paying their Boolean row phases and preserving child deficits. The quantitative advance is the explicit deficit bound Gamma+psi_a(eta)+Ka eta, checked at69,395 finite assertions; no universal constant improves. What remains is a dimension-independent selection/payment bound for the nonzero-collision remainder. NEXT targets that exact critical-source implication rather than another isolated class result, because a uniform contradiction to the minimal-witness deficit would settle full FEI.
