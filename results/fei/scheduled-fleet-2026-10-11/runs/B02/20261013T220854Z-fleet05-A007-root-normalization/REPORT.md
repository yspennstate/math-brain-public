# A007 stage 3: actual root lift and paid activation ranks

## exact target, quantifiers, hypotheses and units

Bridge C020 / PI-J (the B02 lead target). For every nonconstant finite Boolean g=2B-1 represented by all signed prime conjunctions, fix positive feasible lambda and one full physical support order per gate. For every r>=1, activate through a fresh common positive conjunction: F=2A_r B-1, p=2^-r. Fix beta in (0,1] with beta sum lambda<=1 and use the exact activated prime table, lambda'=beta lambda and core-first orders. All references are chosen globally, before the Fourier set. Costs are bits; gamma=6/5; F rank discrepancies use natural logarithms only in the source notation. This stage proves an exact actual-event mass lift and a quantitative payment of all new physical rank and extra empty-core rarity. It does not prove generic activation FEI closure or universal PI-J.

With R_g,R_F the complete optimized surrogate residuals (including v log D but excluding h2(v) and K_ref I), and Psi the explicit signed joint functional in LIFT.md, the result is

    R_F <= p R_g + (7/2)p I(g) + [6/5+log2(e)/4]I_core(F) + Psi.

I_core(F)=2rp E B. The still-unpaid Psi retains gate scaling, congestion, root-removal credit and entropy of added actual events. No negative normalizer is discarded.

## sources actually read, revisions and theorem locators

Read BOARD.md at stage start and reread its 2026-10-13 22:15 UTC snapshot, B02 STREAM_NOTES.md v2 (2026-10-11 23:35 UTC), and own STATUS/LEARNED/WORKLOG. Read execution protocol revision 2026-10-11-execution-v2 in full. Read A006 stage-3 REPORT, CLAIMS and FOREST_MOMENTS.md, all determinant/moment clauses; read A009 stage-2 REPORT, its affine-prime full residual and linear-hypergraph transfer (T); read A086 stage-2 review records relevant to prior A007 acceptance. Reread forests.tex actual queue definition, source-SCC partition forests, eq:forestcost, eq:forestconditioning and thm:posteriorforest. Source hashes are in out/SOURCES.json. Prior-stage public-paper baseline remains inherited, not claimed as newly reread.

The lead's original review-A009/activated-tribes assignment was completed in stage 2. A009 has now paid the affine-plane whole-set residual at its stated q>=16 scope, so the previous coordinatewise affine pressure is not a PI-J obstruction and repeating that family would duplicate work. A006 supplies a new exact mass dependency. This stage reviews that entire dependency before continuing the existing root-normalization packet. It does not claim the stream-wide review cap has disappeared or open another broad FEI candidate; its narrow continuation leaves the same C020/PI-J gap explicit.

## complete derivation or exact first unsupported line

The complete analytic proof is LIFT.md. For each base actual forest and selected nonempty core U, choose an old root to own U; preserve every data assignment, edge attachment and within-coordinate child sequence, and connect all other former roots through selected core coordinates. Deleting core-attached edges and replaying the old fixed queue order recovers the unique base event. Therefore the construction counts distinct actual generator events. Its added multiplicity is (c-1)! binom(|U|+c-2,c-1), rather than |U|^(c-1).

The selected mass is p S(T)G_U(T). For empty selected core this equals the full partition-forest mass by a bijection; for nonempty selected core it is a lower bound on full mass. For core-only sets, summing one-gate outcomes gives p beta a 2^(-C_U). Keeping log D'=Lambda'+log Z' yields exact normalizer log[D'/(pD)] and the signed bound <=log beta only after the identity is tested. The core-only rare-root/name block cancels to delta' in [0,p beta a log e].

The quantitative refinement bounds private rank shift pointwise by gamma |T|log(r/|U|), then averages over the binomial selected core. The exact reciprocal-binomial identity removes any log r loss, paying all new private ranks by 3p I(g). Extra empty-core roots cost <=p I(g)/2. Core ranks across both data and core-only sectors total <=(6/5)I_core(F); core-only normalization costs <=(log e/4)I_core(F). The remaining signed Psi is defined with the SAME base posterior, preserving congestion and scale labels rather than optimizing those pieces separately.

The first unsupported line is Psi<=K I(F), with a dimension-independent K, for suitable globally fixed feasible weights on arbitrary overlapping signed prime tables. A paid base R_g alone does not supply it. It is not part of the claimed theorem. REVIEW_A006.md independently reconstructs the whole determinant-moment claim, including actual chronology, rational bounds, SCC factorization boundary and positive-mass sharpness, with no repair. Its local acceptance does not imply an all-dimensional influence bound.

## executed validation with domain, arithmetic, commands and outputs

Frozen specs FROZEN_SPEC.json and REVIEW_SPEC.json were saved before their jobs. Pilot: all four nonconstant labelled monotone n=2 prime tables, r=1, completed in 0.014 seconds with 247 assertions after correcting a Walsh sign convention in the first attempt (out/PILOT_REPAIR.md). No mathematical statement was altered. Main domain: all 22 labelled nonconstant monotone prime tables at n=2,3, each r=1,2,3, all covered nonempty data sets and eligible ownership assignments. No symmetry reduction, random search or automatic dimension increase. Main completed in 0.186 seconds: 27,571 assertions; 66 activated truth tables, 123 assignments, 127 root minors/base events, 2,036 lifted events and 396 core-only events.

Arithmetic is integer truth tables/FWHT, exact rational influence/normalizers, integer sparse determinant polynomials, explicit parent/attachment/child-sequence enumeration, and formal weights z^gamma with rational z. Irrational structural weights were never rounded or called rational. The quantitative rank inequalities and reciprocal-binomial identities are tested rationally in the same fixed domain. The all-r extension is the analytic proof, not an extrapolation of the finite run.

Targeted independent review checks forced sunflowers e=1,...,5, all 81 K4 full-set assignments, and all eight heterogeneous {01,12,023} full-set assignments: 1,137 assertions; 164 minors, 374 actual events, 64 nontrivial factorial moments and five sharp positive-Fourier-mass examples. Its observed runtime was 0.043 seconds. The frozen heterogeneous pre-count was mistakenly four; actual count is 2*2*2*1=8 and no domain changed, as recorded in REVIEW_CHECK.json. Aggregate successful full checks: 28,708 assertions. These counts exclude earlier pilot assertions and the superseded pre-refinement main output.

Reproduction commands, from this run directory:

    python -X utf8 code/check_lift.py --pilot --out out/PILOT.json
    python -X utf8 code/check_lift.py --out out/EXACT_CHECK.json
    python -X utf8 code/check_review.py
    python -X utf8 code/finalize.py

Both jobs were estimated below 100 MB, so the >300 MB memok trigger did not apply. One job ran at a time, each below the frozen 60-second limit. No GPU, git, network messaging, brain mutation or shared-file write was used. Memory estimate is not a measured peak.

## proof dependencies and changed downstream conclusions

A006-ACTUAL-FOREST-DETERMINANT-MOMENT-BOUNDS v1 is independently accepted here at its unchanged exact statement and hash. The review reconstructs all clauses and supplies no repair; A007 is an independent reviewer rather than contributor to that source version. Its use in this stage computes the correct base posterior mass; the activation injection, binomial rank payment and signed normalizer derivation are separately proved. The original forests.tex source is hash-pinned. A009's new affine theorem is context for dispatch only, not an unreviewed proof premise.

New claim A007-ACTUAL-DATA-WITNESS-ROOT-LIFT v1 is author-proved/exactly-checked and pending A086/A094 review. The stage removes the rank-shift and extra empty-core rare-root debt from the generic activation gap and identifies Psi as the remaining joint payment. It does not refute any Boolean FEI claim, promise generic closure, equate B mass with exact queue probabilities, or assert free selection among reference scales.

## one next mathematical action and independent reviewer

Pay Psi by spreading selected core ownership across the existing used data gates, retaining an invertible actual-trace map and using the accepted determinant moment masses for the resulting posterior. This directly addresses the remaining congestion/scale-label debt at arbitrary overlap. A086 or A094 should reconstruct LIFT.md as a whole, especially recovery of old roots, repeated-slot multiplicity, the rank-stripped posterior and every signed normalizer. A006/A008 can use the explicit J functional; A015 can use the root-conditioned activation interface. No external message was sent.

## actual persistence receipts or precise save blocker

All run artifacts are written only under A007's authorized stage directory; STATUS.md is current and WORKLOG.md/LEARNED.md appended. out/RECEIPTS.json records SHA256 and sizes of run artifacts and rolling files. code/finalize.py verifies exact protocol fields, matching PROGRESS/PACKET_DELTA, preserved reviewed statement/hash, the 20 MB file cap and on-disk receipt hashes. Local persistence is complete. Supervisor GitHub/brain copying is not performed or verified here. No save blocker.

## Universal bridge

This stage moves C020 whole-set witness cost / the lead's PI-J target by supplying an invertible generic actual-forest activation lift, exact rising-factorial event credit and signed nonempty-root normalization, then paying all added physical rank and core-empty rarity by (7/2)p I(g) and core rank/normalization by [6/5+log2(e)/4]I_core(F). A006's whole determinant interface now has an independent reconstruction. The precise remainder is Psi, the signed joint congestion/scale-label functional with actual root-removal credit; full FEI still requires its arbitrary-overlap influence payment and a universally paid base reference. NEXT spreads core ownership to attack that same functional with the accepted determinant mass, rather than adding an isolated class estimate, because it targets the exact remaining obstruction to composition of a universal PI-J reference.
