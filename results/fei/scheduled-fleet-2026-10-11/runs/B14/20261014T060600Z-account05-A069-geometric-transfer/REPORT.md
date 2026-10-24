# A069 stage5: exposed cancellation with an inherited core reference

## exact target, quantifiers, hypotheses and units

For every m>=1, disjoint uniform control bits c,u, an m-bit Z and nonempty Y, choose four arbitrary Boolean Y cores h_cu. Let G select these cores, q1 flip {c=c*,u=u*}, q2 flip {c=c*,Z=z*}, source g=q1G and sequential edit mask q=q1q2. The final F=q2G has one fully exposed canceled private event and arbitrary nonfactorizing core branches. Given ONE positive normalized reference R_Y shared by all four cores, retain B=average C_R(h_cu), exactly the average reference cost of all actual final terminals. Construct ONE normalized final reference Q with

    H(F)<=C_Q(F)<=B+2I_Y(F)+4I_{c,u}(F)+(4+log2(20/7))I_Z(F).

The last coefficient is <28/5. If every C_R(h)<=K I(h), obtain H(F)<=max(K+2,4+log2(20/7))I(F). The paid common reference is a hypothesis, not implied by four separate entropy bounds. All quantities are bits, I is physical pivotal influence. A degenerate q2=1 output is also included. An actual Y query admits an exact inherited-reference decrement and signed physical ledger, not an unproved local price. Full FEI OPEN.

## sources actually read, revisions and theorem locators

BOARD snapshot2026-10-14 06:02; B14 STREAM_NOTES v2,2026-10-11 23:25; own STATUS; EXECUTION_PROTOCOL 2026-10-11-execution-v2. The lead's original tree-code examples were completed earlier. Dispatch consumes new A070 review/objection: run20261014T034205Z DERIVATION Sections1-5 and CLAIMS independently accepts own stage4, proves partial privacy, and refutes finite ancestral-bill transfer at complete exposure. A067 run20261014T044841Z DERIVATION Sections1-5 and CLAIMS independently accepts that A070 claim and constructs a no-cap four-controller-state reference; its universal Boolean flag lemma is reproduced here. A088 run20261014T053751Z CLAIMS records independent acceptance of A067 and a post-core conditional flag obstruction. These sources are pinned in out/SOURCE_MANIFEST.json. We do not repeat the accepted partial-privacy theorem or the controller-state census.

## complete derivation or exact first unsupported line

DERIVATION.md supplies the entire proof, equations(1)-(11). Exactly cancel q1 before selecting the final output reference. The original and final core marginals coincide, so the same inherited R_Y preserves both core entropy and complete core KL; all four actual terminal bills remain in B. Nonempty control Fourier sets split into three visible singleton cells and two cells with nonempty Z and fixed u-membership. Equation(4) gives equal squared row amplitudes throughout each tail cell for arbitrary unequal cores. This directly proves the abstract encoding property, without geometric estimates.

Use normalized label weights1/4,1/4,1/16,7/20,7/80, uniform inside each cell. The singleton label costs are exactly twice degree. Both tail cells have the same residual log2(20/7) after their u-label cost is absorbed by degree. Their size cost is at most twice mean degree. Only the tail residual spends I_Z. The final empty/nonempty flag is paid once by the reviewed universal Boolean bound h2(alpha)<=2I(F). The resulting complete joint law R_Y times this control law pays the full reference cost, including its empty atom; no channel is silently dropped because the common core-reference mixture cost is explicitly in B.

For three core bits, one normalized hierarchy law with Kraft sum13/16 pays Maj3,y0,-y0,-Maj3 at K=3; these four branches are not all scalar multiples of one core. Thus this nonfactorizing family has H<(28/5)I for every control width and fixed event assignment. This is a derived family certificate, not a priority claim against other known small-selector classes.

One actual Y query carries R_Y by frequency marginalization, common to all four cores and both physical children. Complete reference decrement equals conditional core-reference cost plus the actual binary flag Jensen-Shannon refund. The exact K-ledger retains both child costs and K Inf_i minus that decrement. No local positivity or same-constant payment is inferred.

No unsupported line remains in the scoped theorem. The first unsupported universal line is paying the retained2I_Y or the signed query conversion from a genuinely UNUSED common-reference child surplus. Separate terminal entropy certificates do not supply such a common reference. Arbitrary source dependence on Z breaks five-cell flatness; recognition of this cancellation normal form for arbitrary Boolean functions is unproved. C019 physical ownership is not established.

## executed validation with domain, arithmetic, commands and outputs

All searches were frozen before execution. V1 caught an author checker error in the first fixture: the unnormalized Walsh multiplier implementing the correct normalized coefficient formula was2^(k+1), whereas it must be N*2^-m/2^(k+1)=2. The failed helper is preserved as code/check_v1.py; out/PILOT_V1.json records zero completed cases and the failing40th assertion. No mathematical formula changed. code/freeze_repair.py wrote the unchanged domain/resource limits with helper version2 before rerunning.

Completed main domain: m=1,2,3; all256 ordered quadruples of one-bit Boolean cores; precisely256 frozen quadruples of two-bit cores (not16^4); all four c*,u* assignments; reflected canonical z*. Add256 degenerate outputs and three explicit witnesses. Coordinate reflection on Z preserves the source, cells, code, and influence. PASS:6403 cases,463814 exact assertions,10.8619843s. Checks cover direct Boolean cancellation, physical influence, inherited core marginal, per-row flatness, explicit signed Fourier phase, normalized complete product reference including endpoints, integer cardinality/degree bounds, and the rational coefficient comparison20^5<2^8*7^5. A070's t5 witness gives I(g)=21/16,I(q)=37/32,I(F)=1/2 and ancestral ratio369/8>26; no positive ancestral conversion is assumed. The nonfactorizing example's common normalized core law and all K3 bills are checked exactly.

Separate frozen history domain:256 prescribed two-bit core quadruples, one private Z bit, actual query Y0, both actual physical children, inherited R_Y=(1,2,3,4)/10 and common marginal(3,7)/10. PASS:256 cases,2817 exact assertions,0.587872s. Rational spectra/influences and exact prime-log coefficient maps certify the full parent/child reference identity and signed K6 ledger, with no floating logarithm sign decisions. All256 decrements are symbolically nonzero; no claim is made that6Inf_i minus the decrement is nonnegative.

Commands from A069:

    python -X utf8 runs/20261014T060600Z-account05-A069-geometric-transfer/code/freeze_repair.py
    python -X utf8 runs/20261014T060600Z-account05-A069-geometric-transfer/code/check.py
    python -X utf8 runs/20261014T060600Z-account05-A069-geometric-transfer/code/history.py
    python -X utf8 runs/20261014T060600Z-account05-A069-geometric-transfer/code/finalize.py

Main/history memory estimates64/32MB, not observed peaks; both55s caps and pilot60s rule respected. No heavy job, automatic dimension escalation, GPU or background process. No job expected above300MB, so memok gate was not triggered. Entropy flag signs and all-dimensional bounds are proved analytically; finite checks do not claim all-dimensional exhaustiveness.

## proof dependencies and changed downstream conclusions

A067-BOOLEAN-FLAG-FOUR-BRANCH-FINAL-REFERENCE@1, hash92eacd157bc8b527dc2e8d38d2bdb5be1dfbf179105280ad82707f5c587c1948, is used ONLY for its universal Boolean flag fragment, independently accepted at full stated scope by A088. The flag proof is reproduced without importing controller/terminal hypotheses. All new five-cell/cardinality/core-preservation and history calculations are derived here.

Own A069-SOURCE-BLIND-SHARED-EDGE-TRANSFER@1 was independently accepted by A070 without repair; acceptance receipts are saved. A070-PARTIAL-PRIVACY-TRANSFER-AND-EXPOSED-EVENT-BOUNDARY@1 is independently accepted by A067; we consume its full-exposure objection instead of trying to bound its ancestral bill again. The new final reference handles its factorizable cancellation and a genuine four-core nonfactorizing perturbation with the original common core reference retained. It does not repair arbitrary private-source transfer, general conditional flag price, or unused child slack. The new narrow transfer/history lemma is author-proved; independent review pending. No previous claim is refuted or overwritten, and no registry adoption or external copy is asserted.

## one next mathematical action and independent reviewer

At one actual Y query, calculate the signed K Inf_i-Delta C_Q from equation(11) and identify a once-owned unused surplus in the SAME common core reference, retaining both actual child terminals and the unchanged five-cell label law. Start with the certified nonfactorizing Maj3/literal branches; do not renew the global2I flag reserve at a child. A070 should reconstruct the cancellation/reference and core-query ledger; A088/A094 should challenge the slack owner and its compatibility with the post-core flag obstruction. This is a source-bound handoff, not an external message.

## actual persistence receipts or precise save blocker

The four protocol files, derivation, frozen specifications, original failed checker, repaired code, exact outputs and local receipts are written only inside this run. STATUS has exactly two lines; WORKLOG is appended and LEARNED updated. code/finalize.py checks the exact protocol schemas, canonical statement hash, report headings and identical PROGRESS/PACKET_DELTA, then hashes every run artifact and rolling file in out/RECEIPTS.json. Local persistence is complete when its PASS output is read. New independent review, supervisor copy, registry adoption and mirrors remain unverified. No save blocker.

## Universal bridge

This stage moves C020 by replacing a fully exposed canceled-event ancestral bill with one complete final five-cell law: full cost is bounded by the unchanged actual terminal reference B plus2I_Y+4I_{c,u}+(4+log2(20/7))I_Z, the last coefficient below28/5. C024 additionally gains an exact carry of that SAME core reference through one physical Y query with both child bills and its signed conversion retained. The universal unused-child-surplus payment of2I_Y and K Inf_i-Delta C_Q, and arbitrary Z-dependent row references, remain open. NEXT targets precisely that signed query bank under the inherited reference, the shortest route because another cancellation family would not resolve the now-explicit universal surplus line.
