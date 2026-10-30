# A061 stage 4: signed-child eligibility review

## exact target, quantifiers, hypotheses and units

Review A005-POINT-EDIT-CHILD-ELIGIBILITY-OBSTRUCTION@1 for finite uniform Boolean seeds with delta_C=H-CI>0, C fixed, and only relevant seed inputs. Entropy is in bits, sigma_i is average child CI-H, and average-child eligibility means sigma_i>=0. Verify its actual 12-bit obstruction at C=8/3 and erasure price 5/2. This is a repair/review stage at the two-pending-claim cap, with no third broad candidate.

## sources actually read, revisions and theorem locators

Execution protocol 2026-10-11-execution-v2 reread in full; updated BOARD dated 2026-10-14 01:30 UTC, including the new A005 handoff; B13 STREAM_NOTES v2 (still dated 2026-10-11 23:1xZ); own STATUS, rolling lessons/log, and stage-3 checker. A005 run 20261014T001325Z-fleet05-A005-noncircular-endpoint-referee: REPORT, CLAIMS, DERIVATION sections Signed-child eligibility and Corrected witness admission, and WITNESS_VALIDATION output. Byte receipts are in out/SOURCE_RECEIPTS.json. Older campaign and paper intake is inherited from earlier stages; no fresh paper/literature reading or new attribution claim.

## complete derivation or exact first unsupported line

REVIEW_PROOF.md reconstructs the physical children. Every fresh query leaves the clean padded seed on one branch and the one-vertex edited seed on the other. Their deficits converge to the seed deficit, so sigma_fresh tends to -delta_C(seed)<0. Old child slacks converge; strict positivity makes exactly the old coordinates eventually eligible. The corrected price Q_C=min_i[B_i+max(-sigma_i,0)]/d_i is preserved under admission: old prices converge and every fresh price is asymptotic to delta_C(seed)*2^(N-1). Zero-slack old seed children are handled by continuity of max for Q_C, not by an unsupported eligibility-boundary sign inference.

The exact audit q_i=max(B_i/d_i,C+(delta_C-J_i)/d_i) shows the retained deficit explicitly. The D-based analogue is max(D_i/d_i,C+delta_C/d_i). Neither expression pays the deficit from a new structural resource. First unsupported universal line: construct a selectable query or block with independently owned payment for its erasure and negative descendant slack, retaining both actual child deficits or the terminal core deficit.

The 12-bit witness has full Fourier support, max influence<1/4, positive delta_(8/3), old erasure prices>5/2 with individual child slacks zero and positive, and fresh prices<5/2 with both individual child slacks negative. Fresh corrected prices exceed 400; old corrected prices are below 3. This verifies the stated endpoint refutation. It is not a minimal violator and does not refute FEI at an unrestricted absolute constant.

## executed validation with domain, arithmetic, commands and outputs

FROZEN_SPEC.json predates every search. From this run: `python -X utf8 code/check_review.py pilot`, `... full`, `... witness`. Pilot: 6 roots/16 coordinate splits/160 assertions in 0.1213s. Full: all 22 labelled seeds in dimensions zero through two, padded by two or three bits, giving 44 roots/182 splits/1692 assertions in 0.4990s. Witness: all 4096 physical values and Walsh coefficients, all 12 coordinates and all 24 complete physical children, 185 assertions in 1.2016s. Primary total 1877; pilot separately counted. No failures. One targeted witness rerun followed addition of the useful old corrected-price<3 assertion; the earlier run is not added to totals.

Arithmetic is integer Walsh and physical edge counts, exact Fraction prime-log identities, and rational sign intervals. For log bounds reduce primes to q in [1,2), use ln(q)=2 sum z^(2k+1)/(2k+1), z=(q-1)/(q+1), 48 terms, and remainder <=2 z^97/(97(1-z^2)); divide by enclosing ln2 with correct endpoints and round outward to dyadic160. All asserted inequalities have certified strict signs. Estimated memory 65 MB, below the 300 MB trigger; no heavy job, automatic dimension escalation, background process, or GPU.

## proof dependencies and changed downstream conclusions

The reviewed A005 statement/hash is unchanged. Its new child conclusion and finite endpoint obstruction HOLDS at stated scope. The broad admission premise is A061-ARBITRARY-CORE-EDIT-ADMISSION@1, which A061 authored and which remains externally unreviewed. Accordingly this is explicitly not independent full-chain acceptance. The local CLAIMS copy records that conflict and a scoped verdict; shared sources are untouched. No substantive repair was supplied to A005. The two original pending A061 candidates remain pending; source consumption alone is not acceptance.

Downstream selection must retain signed descendant slack: the apparent price-two fresh witness becomes expensive after its actual child debt is included. Corrected-price transport does not lower any universal FEI constant. The stream lead's old point-function task was already closed; this stage consumes a new obstruction rather than repeating the census or martingale telescope.

## one next mathematical action and independent reviewer

A087/A094 should independently reconstruct the pending A061 admission/point chain and this A005 corollary. Next mathematical action: audit one source-owned selected-query negative-slack payment at a shared-controller continuation, with actual child deficits, terminal entropy and one exclusive influence account; use A064/A087's retained-boundary interfaces. This targets the unpaid universal term rather than adding another padded family.

## actual persistence receipts or precise save blocker

All four protocol files, proof, frozen spec, standalone code, three validation outputs and source receipts are saved within this run. STATUS is two lines; WORKLOG and LEARNED receive this stage's facts. PROGRESS and PACKET_DELTA are identical with packet_ids=[A061]. Finalizer checks exact field sets and the unchanged statement hash. out/PERSISTENCE_RECEIPTS.json records all local file sizes and hashes; all are below 20 MB. No shared-index, independent full-chain acceptance, supervisor mirror or remote publication receipt is claimed. No save blocker.

## Universal bridge

C019 stopping-tree payment moves by a scoped review and exact obstruction: A005's cheap admitted query fails child certification, and on its 12-bit fixture its retained descendant debt raises the corrected price above 400 while an old price stays below 3. C018 root-only erasure selection therefore cannot discard the selected child slack. No universal constant improves; the remaining bridge is an independently owned bound on the chosen negative child slack or terminal core deficit. NEXT audits that exact signed payment with A064/A087's physical continuation and exclusive budget, the shortest available route because point-edit admission and its cheap local prices are now understood and cannot themselves supply the missing universal reserve.
