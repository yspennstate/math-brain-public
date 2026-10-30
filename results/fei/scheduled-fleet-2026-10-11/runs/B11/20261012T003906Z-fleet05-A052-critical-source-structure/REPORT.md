# A052 / B11 stage 2: optimal recentring cannot exploit larger blocks

## exact target, quantifiers, hypotheses and units

Follow B11 STREAM_NOTES v2: replace the prior affine-pivot cost by the fully optimized conditional mismatch beta_A, then decide whether some proper block of each iterated point-defect composition satisfies U_A=H(S_A|S_Ac)+(2/ln2)beta_A<=(H/I)I_A. Entropy is in bits, f is an actual sign on a finite uniform cube, S has law fhat^2, and I_A=sum_(i in A)P(i in S). Only nonempty proper blocks with I_A>0 are admitted. Constants never enter ratios.

The frozen finite inputs are A051's 1,150 saved read-once NAND shapes on 6..9 distinct literal leaves and seven explicitly defined Hod-named six/eight-bit seeds and fresh NAND hybrids. These are a precise finite formula list, not all Boolean functions or the large recursive lower-bound family. We do not repeat A051's decrement-minimum census. The new analytic theorem proves that the optimized upper certificate's block minimum equals its singleton minimum for every binary law. Its finite decisions therefore cover all proper blocks without a new block-orbit search.

## sources actually read, revisions and theorem locators

Read STATUS.md and LEARNED.md, the updated BOARD.md snapshot 2026-10-12 00:39 UTC, and B11 STREAM_NOTES.md v2, 2026-10-11 23:3xZ. The board's B06 block/singleton comparison and B17 zero-erasure transport are relevant background; no uninspected board line is used as a proof. Read the lead's run 20261011T230100Z REPORT and CLAIMS, especially R1/R2 optimized recentring, R5 block reduction and R6 tensor scope. Reviewed the analytic interfaces independently in DEPENDENCY_REVIEW.md before adding this new candidate. R3/R4's finite scans are not proof dependencies; the source's floating computations do not provide an explicit checked global rounding bound for the whole scan.

Read A051's stage 20261011T233123Z REPORT, UNIVERSAL_DESCENT_SQUEEZE.md, COMPOSITION_CERTIFICATES.md, formula/seed definitions in descent_compositions.py and check_seeded_and_replay.py, and exact source summaries full_SUMMARY.json, SEEDED_FULL_SUMMARY.json and AGGREGATE_CERTIFICATES.json. The squeeze is independently reconstructed locally. It corrects the lead's phi/R<=1.33 experiment: revealing all but a least-influential bit already proves phi/R<=n/(n-1). This stage tests the different upper certificate and does not reinterpret that automatic ratio ceiling as payment.

The protocol remains EXECUTION_PROTOCOL.json revision 2026-10-11-execution-v2, read in full in the previous stage and used again for the exact schemas. The prior A052 REPORT and CRITICAL_SOURCE_STRUCTURE.tex supply the self-contained logarithmic Sobolev proof and the affine comparison being sharpened. No external literature theorem, A080 asymptotic certificate, or percolation result is a new premise. The named seed clauses are copied as explicit Boolean definitions from A051's pinned source, so no paper fetch or novelty assertion is needed for the finite calculation. Source hashes and locators are in out/SOURCE_MANIFEST.json, and both consumed summary hashes were frozen before computation.

## complete derivation or exact first unsupported line

SINGLETON_COLLAPSE.md and CRITICAL_SOURCE_STRUCTURE.tex give the complete proof. For every binary law define B_A=H(S_A|S_Ac), beta_A=sum_(i in A)E min(P(i in S|S_Ac),P(i notin S|S_Ac)), and U_A=B_A+kappa beta_A, kappa=2/ln2. The conditional chain rule gives B_A>=sum_A B_i. Conditional Jensen for the concave function min(q,1-q), using conditioning on all other coordinates, gives beta_A>=sum_A beta_i. Thus U_A>=sum_A U_i, and normalization by I_A yields

    min_(nonempty proper A, I_A>0) U_A/I_A
       = min_(i:I_i>0) [B_i+kappa beta_i]/I_i.              (1)

Every relevant singleton is proper when n>=2. No Booleanity, extremality or optimizer existence is used in (1). For Boolean physical children, the independently reconstructed lead lemma gives J_A<=kappa beta_A. The criticality comparison enters only at L_A>=R I_A, or L_A>=KI_A+D_K for a dimension-critical K-witness. This restates the prior pivot obstruction with the optimal predictor. A larger block cannot rescue the U certificate if all singletons fail. The information-cap repair B_A+min(|A|,kappa beta_A) also collapses to singletons, by min(sum a_i,sum b_i)>=sum min(a_i,b_i).

There is an exact all-dimensional mechanism obstruction. For F_m=product_j (-1)^(x_j y_j), m>=2, the squared spectrum is uniform, so H=2m and I=m. Every block has B_A=|A|, beta_A=|A|/2, and I_A=|A|/2. Consequently U_A/I_A=2+kappa>R=2, and the capped version equals 4. Yet the actual decrement is L_A=2 times the number of touched pairs, and J_A is the number of pairs touched once. Revealing a whole pair has J_A=0 and L_A/I_A=2. All physical restrictions have ratio<=2, so this is genuinely non-strict physical-descendant ratio-critical; it is neither tensor-indecomposable nor dimension-minimal. The same certificate failure with strict actual descent holds for disjoint tensor powers of a two-bit quadratic factor times a three-bit point defect: the root ratio is between 2 and 3, each singleton certificate is at least 2+kappa>4, and querying the low-ratio full factor improves the remaining child. These are bounded-ratio route obstructions, not FEI disproofs or high-threshold critical obstructions.

Exact decisions on the saved NAND family are:

| dimension | formulas | U certificate passes | fails every block | failures with independently rechecked strict actual descent |
|---|---:|---:|---:|---:|
| 6 | 33 | 8 | 25 | 8 |
| 7 | 90 | 20 | 70 | 37 |
| 8 | 261 | 60 | 201 | 102 |
| 9 | 766 | 177 | 589 | 332 |
| total | 1150 | 265 | 885 | 479 |

All seven separate seed/hybrid controls fail U_A<=R I_A; four nevertheless have directly rechecked strict actual descent. The latter is a constructive witness statement, independent of whether A051's chosen blocks are global decrement minimizers. We verify those blocks directly from truth tables. For NAND case 0006, a six-bit formula, R is between 2.40 and 2.41, min U_i/I_i exceeds 3.57, yet block mask 48 has L_A/I_A<2.30. Its actual joint channel and exact symbolic costs are in out/CHANNEL_REPRODUCTION.json. For Hod_g3, the certified displayed values are R approximately 2.414979, minimum U_i/I_i approximately 2.688444, and the actual singleton decrement approximately 2.348682. Displays summarize rational endpoint certificates, not floating signs.

First unsupported line: infer a fixed absolute K paying B_A+J_A on arbitrary dimension-critical witnesses, or the full terminal-inclusive stopping-tree cost. The finite census does not do this. Even a universal bound for the optimized U minimum would be a singleton erasure route; optimizing larger blocks in this same surrogate cannot create an additional payment. The all-dimensional counterexamples reject the own-ratio certificate and its elementary information-cap repair, not every larger fixed universal K or every joint-channel/critical-only mechanism.

## executed validation with domain, arithmetic, commands and outputs

Before computation, froze out/FROZEN_PILOT.json, FROZEN_FULL.json and FROZEN_REPRODUCTION.json, specifying helper version, actual Boolean family, dimension domain, counts, symmetry, arithmetic, memory and time. The two census specs also pin source summary hashes. Memory estimates were 70 MB and 30 MB, below the 300 MB memok gate; peak RAM was not measured. One substantive job ran at a time. No GPU, automatic dimension increase, persistent background process, other-folder write, git or external message was used.

Commands from A052:

    python -X utf8 runs\20261012T003906Z-fleet05-A052-critical-source-structure\code\recentred_census.py freeze
    python -X utf8 runs\20261012T003906Z-fleet05-A052-critical-source-structure\code\recentred_census.py pilot
    python -X utf8 runs\20261012T003906Z-fleet05-A052-critical-source-structure\code\recentred_census.py full
    python -X utf8 runs\20261012T003906Z-fleet05-A052-critical-source-structure\code\reproduce_channel.py

The first pilot correctly failed its final frozen-count assertion because the six/eight-variable seeds were labelled g6/g8 instead of source g3/g4; the seed-name filter omitted them. No mathematical sign failed. out/PILOT_FAILURE.json preserves this failure and repair. After correcting names, pilot PASS: four cases, 924 assertions, 0.153369 seconds helper runtime, below 55 seconds. Full census PASS: 1,157 cases, 68,806 assertions, 36.048827 seconds, below 600 seconds. Separate physical/direct-Walsh channel replay PASS: five cases, 1,881 completed assertions, 0.062800 seconds in its first run and 0.066212 seconds after its metadata repair, below 55 seconds. The save writer caught that the first replay's file counted assertions before its final output-size check while stdout counted afterward; out/SAVE_FAILURE.json preserves that mismatch. The same frozen replay was rerun with consistent completed-count metadata. No mathematical inequality, family or precision changed. Times are rounded displays of measured helper metadata; command startup time is separate. Full plus replay total is 70,687 exact assertions; pilot is additional.

For each actual truth table, integer Walsh squares sum exactly to N^2. Spectrum influence agrees with counted physical boundary edges; root entropy vectors and truth-table hashes agree exactly with the frozen sources. Natural-unit entropy has numerator N^2 ln(N^2)-sum w_s^2 ln(w_s^2), represented by integer prime-log coefficients. Marginal packet sums compute B_i; beta_i is the exact sum of packet minima. The tested sign is

    I_i_num H_num - I_num B_i_num - 2 beta_i_num I_num.

All coefficients and constants are integers. Its sign is checked with rational logarithm intervals. Range reduction uses ln p=k ln2+ln(p/2^k); the positive atanh series has 40 terms and a proved tail at most 2z^81/[81(1-z^2)], z<=1/3. Each log interval is rounded outward to a 96-bit dyadic interval. Signed expressions reverse endpoints for negative coefficients, and signed ratios use all four division corners. No floating sign decision is made. Equal minima are recognized by exact symbolic coefficients and constants. The precision is fixed, not silently escalated.

Every singleton's actual physical-child entropy is independently reconstructed; the channel upper bound is checked against that value. One named proper block from A051's summary is directly recomputed for every case, so all 479 positive actual-descent statements are new physical witnesses. The pilot additionally checks every proper block of its two NAND cases and both six-bit seeds for entropy/mismatch superadditivity and the actual channel bound. The separate replay uses direct character sums for roots and children, compares them with FWHT, and exhausts all proper blocks of the two quadratic tensors and the five-bit strict tensor example. It shares the proved rational-log enclosure and is not represented as an independent logarithm implementation or external review. Per-case certificates are saved immediately in out/cases; summaries and the channel replay are also saved. All files are below 20 MB.

## proof dependencies and changed downstream conclusions

The distributional singleton-collapse theorem is self-contained and has no FEI or pending-claim premise. Its application to an actual physical upper bound uses CLAUDE-B11-R1@1, reconstructed independently with the prior self-contained logarithmic Sobolev proof. Criticality uses CLAUDE-B11-R2@1/A051's earlier deficit identity; these are reviewed locally in DEPENDENCY_REVIEW.md. The A051 squeeze is separately accepted at its stated analytic scope. R5 is reconstructed; R6's meaningful full-factor clause is reconstructed with a one-bit empty-block definition caveat. No source finite scan is silently promoted to exact certification, no reviewer repair is supplied, and shared claim/status files remain untouched.

The new result changes the stream's next mechanism. The fully optimized pivot recentring is stronger than the prior affine predictor but its normalized block minimum is exactly singleton. Thus a lead-directed search for a larger block passing the same U bound is now closed analytically. The 885 failures and 479 constructive false negatives show the gap explicitly on the requested compositions. The exact tensor formulas isolate channel cancellation, rather than component pruning, as the missing behavior. A053's near-tensor continuity and A018/A019's signed/isospectral channel identities are the relevant next dependencies; their own class theorems are not repeated or assumed without reading. The surviving universal target must estimate actual joint J_A or pay a complete tree with terminal entropy.

## one next mathematical action and independent reviewer

Next: derive a joint-channel estimate that recognizes coherent isospectral/full-factor cancellation and is not superadditive under block assembly. Start with the saved six-bit case 0006 and its strict-descending block mask 48; preserve B_A, exact J_A and the averaged child deficits rather than replacing them by beta_A. Consume A053's near-tensor remainder and A018/A019's source-bound channel identity when available. A090 should reconstruct the conditional-Jensen collapse and the tensor obstruction; A094 should independently reproduce the finite signs and criticality scope. The lead and A051/A054/A055 are the primary consumers.

## actual persistence receipts or precise save blocker

Saved only in this A052 run: REPORT.md, CLAIMS.json, PROGRESS.json, PACKET_DELTA.json, CRITICAL_SOURCE_STRUCTURE.tex, SINGLETON_COLLAPSE.md, DEPENDENCY_REVIEW.md, frozen specs, preserved pilot failure, scripts, all 1,157 per-case certificates, summaries, channel replay, witness summary, source manifest and out/RECEIPTS.json. STATUS.md, WORKLOG.md and LEARNED.md are updated. The save writer checks exact protocol fields, passing outputs, file-size limits, byte-identical packet delta and SHA256 receipts. No source tree or other agent folder was modified. Supervisor copy/mirror, shared-index adoption and independent review of this new bundle remain pending; local persistence does not imply them.

## Universal bridge

This stage moves C018/C019 by closing a specific proposed selection mechanism: the best recentred logarithmic-Sobolev block certificate equals the best singleton certificate exactly, even after clipping by the physical block's information ceiling. On the requested 1,150 compositions it certifies 265 and misses 479 explicitly affordable actual blocks among its 885 failures; exact tensor families exhibit the same lost joint-channel cancellation in all dimensions. This is a rigorous scope obstruction and a sharper critical-source interface, not a universal influence payment. The unpaid target is a fixed-K bound on the actual joint decrement or a nonreusing stopping tree with terminal entropy retained. NEXT targets the exact cancellation visible in a saved strict-descent block because it changes the failed additive mechanism at its first unsupported line, whereas a larger isolated formula census or a larger-block search using the same U bound cannot advance full FEI.
