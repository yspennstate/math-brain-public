# Verified-claims ledger (campaign, 2026-08-09)

Every mathematical assertion this campaign produced, with status, who checked it, and where its receipt is.
Written iteration 35. Status vocabulary: PROVED (with referee) / CORRECTLY DEDUCED / AUDIT VERDICT / OPEN.

## 1. Engine inequality (Var <= kappa A2 + sqrt(A4 Pbar)) on Z^2
- Status: PROVED, REFEREE-VERIFIED
- Checked by: hostile referee, independent zero-shared-code reimplementation on a harsher instance (4096 configs, non-identical block laws); A1-A8 all confirmed
- Receipt: problem/MG2B_framework_lemma_draft.md sections 1-8

## 2. Conditional halving (M1)(M2)(CH)+smallness => Var(X_Mn) <= (1/2) M Var(X_n)
- Status: PROVED AS DEDUCTION, REFEREE-VERIFIED
- Checked by: same referee; deduction chain re-derived
- Receipt: problem/MG2B_framework_lemma_draft.md section 9

## 3. Occupation lemma: geodesic edges in a box <= (b/a)*diam, tight at a=b
- Status: PROVED, REFEREE-VERIFIED (sharpened)
- Checked by: hostile referee; adversarial search (occupation-maximizing Dijkstra, annealing, serpentine gadgets) found zero violations; my 2b/a draft constant sharpened to b/a and two draft defects repaired
- Receipt: problem/CRUX_iteration_arithmetic.md section 5

## 4. Two-sided resampling consequence A2 <= 2(b-a)^2 C' M n(n+W), A4 analogue
- Status: PROVED - JUSTIFICATION SUPERSEDED IN PLACE (iter 61). The displayed bounds are unchanged,
  but the N'_ij machinery was never needed: framework Lemma 4.2 is the EXACT identity
  E[(X-X^L)^2] = 2E[((X^L-X)^+)^2] (swap symmetry), so the minus direction is free once the
  indicator is dropped first, and A2 is controlled by the OLD geodesic's occupation alone. The
  sentence "the two-sidedness is load-bearing" is STRUCK - the engine consumes only the positive
  part (Theorem 8.1 holds with A2 replaced by A2+ <= A2). Both referees were right about different
  objects: the iter-21 witness (X can drop when an untouched block is resampled) concerns the
  two-sided square and stands; the engine never uses it.
- Checked by: iter-21 referee (witness); iter-59 referee (D7); author re-derivation with the
  indicator subtlety written out (the load-bearing step is dropping the indicator BEFORE 4.2)
- Receipt: problem/CRUX_iteration_arithmetic.md section 5, second referee record

## 5. Theorem A: hypotheses H1-H4 + (M1)(M2)(M3)(CH) => Var(X_n) = O(n^{1-eps})
- Status: CORRECTLY DEDUCED, REFEREE-VERIFIED
- Checked by: hostile referee; 200k-trial algebra check + 221,858-case ladder check, zero failures; one stale-status defect of mine found and fixed
- Receipt: problem/MG2A_conditional_theorem.md

## 6. Remark: H4 (anti-concentration) => variance floor D_s >= (c4 delta4^2/4) Q_s^2
- Status: PROVED (the assembly's only new derivation)
- Checked by: referee re-derived; centering and constant confirmed; sup-domain technicality made explicit
- Receipt: problem/MG2A_conditional_theorem.md Remark 2.1

## 7. BSS arXiv 2604.01214 erratum 1: printed E[G^2] >= 2E[H^2] is false as printed
- Status: CONFIRMED, PUBLICLY DEFENSIBLE
- Checked by: referee verified the quote verbatim at their lines 1104-1107 and showed falsity from the paper's OWN Theorem 2.1 (at t=1 it forces Var=0)
- Receipt: problem/MG2B section 12(c); problem/bss_errata_note_draft.md

## 8. BSS erratum 2: display (14) factor-2 inconsistency; endpoint true, rescued by the sharp inequality
- Status: CONFIRMED, PUBLICLY DEFENSIBLE
- Checked by: referee recomputed the combination; both repair routes check out
- Receipt: same

## 9. MG2-C: the multiscale induction consumes only o(1)-slope estimates (WINDOW-o(1))
- Status: AUDIT VERDICT (full-paper coverage)
- Checked by: nine independent reading passes over the previously-unread spans; two findings double-discovered; two caveats named
- Receipt: LOG.md iteration 17; brain node bss2026_isotropy_audit...

## 10. The wall: required chaos strength falls short by ~n^2/log^4 n at today's unconditional inputs
- Status: ELEMENTARY, LINE-CHECKABLE
- Checked by: author's own arithmetic; referee reproduced the plug-in shape
- Receipt: problem/CRUX_iteration_arithmetic.md section 2

## 11. chi = 1/3 for planar lattice FPP
- Status: OPEN - NOT SOLVED, NOT CLAIMED
- Checked by: n/a
- Receipt: stated in every artifact

## -- Entries 12+ added iteration 72 (vocabulary extended: WITHDRAWN / PENDING REFEREE / MEASURED / HEURISTIC) --

## 12. C1 corner lemma, SHIFT route: threshold alpha > sqrt(2)-1 = 0.4142 on published inputs
- Status: MAJOR REVISION (iter 50); construction survived four invented attacks, bookkeeping did not
- Checked by: hostile referee - ten corrections, incl. threshold moved from 1/3 (assumed an
  envelope-scale alignment that is itself open) to 0.4142 on Alexander's published bound
- Receipt: problem/C1_corner_lemma_draft.md banner

## 13. CRUX sections 6/6b/6c (A4 <= B^2 A2 program): WITHDRAWN as a contribution
- Status: WITHDRAWN (iter 59). Algebra valid but near-trivial and already in section 5; named
  sub-target FALSE (D3 counting proof); "A4 eliminated" false (residual tail IS (M2)); my diagnosis
  that Section 2 mischarged the second moment was WRONG and struck from three places; route
  dominated by inserting the hypothesis a step earlier. Surviving product: the positive-part
  correction now in entry 4.
- Checked by: hostile referee, ten defects, two independent kills
- Receipt: problem/CRUX_iteration_arithmetic.md section 6d

## 14. Envelope-variance pinning: within the hypothesis set, alpha = chi exactly
- Status: CORRECTLY DEDUCED, REFEREE-VERIFIED (iter 68). Constant-strength chaos iff alpha <= chi;
  H1a forces alpha >= chi; D in the halving lemma is the TRUE variance (standing assumption, not a
  free parameter); n^{1-eps} is the OUTPUT of telescoping, never an input. Second independent kill:
  the inductive reading makes the entire apparatus idle.
- Checked by: hostile referee (did NOT read the source paper - verdict rests on three agreeing
  internal READs plus the engine's arithmetic; caveat preserved)
- Receipt: problem/CRUX_iteration_arithmetic.md sections 3b (resolved banner) and 7

## 15. The two-obstacle disjointness: STANDS, WIDER, AND CONDITIONAL
- Status: REFEREED (iter 68), supersedes both earlier statements of it. Wall's admissible set is
  the INTERVAL (0, chi], corner (shift route) needs alpha > 0.4142; disjoint IFF chi <= 0.4142
  (true variance exponent <= 0.8284) - weaker than KPZ, widely believed, UNPROVED. Never stated
  flatly. NOTE: the SALVAGED corner route (entry 16) conditionally moves the corner threshold to
  1/3, which under alpha = chi would turn the picture into "assembles when chi > 1/3" - the
  direction is clear, but whether the converse holds (the "iff") is one of the questions the
  running referee was explicitly told to attack; do not quote the biconditional until it returns.
  [REFEREE ANSWER, iter 79/80: the "IFF" is defensible only PACKAGE-RELATIVELY (relative to this
  hypothesis set and these routes - a different route could in principle assemble below 1/3), and
  the regime interval must be stated OPEN at the top: chi in (1/3, 1/2), because assembly AT
  chi = 1/2 self-refutes (linear variance contradicts the sublinear conclusion the assembly
  proves). Quote it as: "package-relatively, assembles exactly for chi in (1/3, 1/2)".]
- Receipt: CRUX 3b banner; STATE.md in-place supersession; all five copies carry the hypothesis

## 16. Corner route via mean/fluctuation split (salvaged note): CONDITIONAL threshold alpha > 1/3
- Status: REFEREED (verdict 23:46, iter 79/80) - SPLIT. Sections 0-8 ACCEPT: Claims 1-6, the cost
  formula and all of section 7 re-derived and hold; ONE side display struck (the section-4 "FLOOR"
  note is false without a kurtosis input - referee counterexample). Section 9 MAJOR: 9.1's
  class-wide pin is NOT delivered as displayed (s unbound, chaining floor missing, wandering-lower
  input unstated), so "every pathwise route is pinned at W_l" is FALSE AS WRITTEN and weakens to
  "the routes examined are pinned"; 9.2/9.3 survive as route-pins; 9.4 overstates a worst-case cap
  as a route yield. I3 DOWNGRADED from "verified in mechanism" to "no obstruction identified" (the
  predictable-quadratic-variation control - the hard core of Kesten - was summarized, not walked).
  Everything remains conditional on I8. Corrections not yet applied to the note file itself - the
  sketch referee still reads it as context; queued behind that verdict.
- Receipt: problem/C1_corner_route_REFEREE_iter72.md (33.9KB full report)

## 17. Splitting Lemma: one-wall deficit dominated by dyadic midline wandering
- Status: LEMMA CONFIRMED CORRECT BY HOSTILE REFEREE (iter 79/80) - fully re-derived including the
  random-split-point pathwise steps and exact e_2-invariance, with the Fekete step given a
  SELF-CONTAINED proof replacing the unverified Ahlberg citation. BUT the REFEREE'S WORST-DEFECT
  FINDING lands on MY framing of its consequence, and it is accepted in full: I called
  A_+(l) <= C l^{gamma'} an "unconditional-in-structure" bound on I8. NO gamma' < 1 is known
  unconditionally - sublinear half-plane geodesic depth is ITSELF open, per the referee's reading
  and mine, and the owed literature search WAS RUN (iter 80): wandering upper bounds route through
  curvature (the cost-of-wandering argument consumes a curvature lower bound), and the only
  unconditional KPZ-relation result found (BSS 2312.14143) is for rotationally invariant models,
  not the lattice. Absence confirmed at search depth (two queries + survey position; bounded, as
  always, by what the search saw) - so that "first unconditional upper bound on I8" DOES NOT
  EXIST as claimed. What is unconditional is only the
  INEQUALITY (deficit <= dyadic sum of wanderings); any polynomial bound from it is a CONDITIONAL
  main claim said the route eliminated. The negative reading, NARROWED by the full report (read
  iter 84): what is PROVED is that THIS dyadic chain cannot certify below the wandering scale
  (its own j=0 term floors its output - tautological for an upper-bound machine), plus the honest
  mini-class the referee defines (comparisons via CONNECTOR PATHS to the wall pay >= a E[x*] per
  scale, since every edge costs >= a). "The wall-splitting ROUTE is provably inadequate"
  overstated it - no route class was defined; corrected phrasing: "the natural dyadic argument is
  inadequate, and any connector-path variant pays the wandering". Threshold arithmetic all
  verified by the referee (gamma' = 1/2 -> alpha > 1/3; 2/3 -> 1/2; 3/4 -> 3/5; break-even with
  the shift route at gamma' = 0.5858).
- Receipt: problem/C1_corner_route_REFEREE_iter72.md; correction to the note's I8 annotation and
  STATUS AFTER 6.6 queued behind the sketch referee's read.

## 18. P2 pilot measurement (Uniform[1,2], wall pairs, l = 24..1536)
- Status: MEASURED - AND INDEPENDENTLY AUDITED (iter 79/80): the referee checked all seven rows
  against the raw JSON and scripts and they match to the digit. Two of MY descriptions corrected:
  (a) the Part1 control's local slopes CROSSED BELOW 1/2 (1.56 -> ... -> 0.35), they did not
  "converge from above" - consistent with the proved cap but my prose was wrong; (b) the
  top-octave crossing-fraction rise is 1.1 sigma, i.e. not established as still-rising. Also the
  truncation caveat promised in the pilot code's comments never made it into the note - owed.
  Substance unchanged: rig valid, magnitude 17x inside budget, exponent UNRESOLVED.
- Receipt: note section 6.5; scratchpad p2_pilot_results.json, seed 20260809; referee report

## 19. Solvable-world support for I8: half-space LPP boundary effects enter at fluctuation scale
- Status: HEURISTIC - STRENGTHENED BY THE REFEREE (iter 79/80): my own feared conflation of
  point-to-diagonal with wall-pair geometry FAILS - the half-quadrant (1,1)->(N,N) passage IS
  wall-pair geometry, so the analogy is tighter than I had credited. Three caveats now owed and
  recorded: the mean-vs-law inference needs uniform integrability; the phase (subcritical
  boundary) must be identified with our regime explicitly; and LPP's sign convention flips the
- Receipt: note section 6.6.4(b); referee report

## 20. g_+ = g for the half-plane (note's F3): PROVED SELF-CONTAINED
- Status: upgraded twice - first to a citation (Ahlberg, arXiv 1107.2280, cone shapes restrict the
  lattice shape), then the referee, unable to verify the citation's exact statement in-session,
  WROTE A SELF-CONTAINED PROOF of F3 instead. The claim now rests on a proof in our own report.
  SHARPER WARNING from the full report (read iter 84): do NOT cite Ahlberg for F3 at all without
  first checking his boundary-direction clause - e_2 is a BOUNDARY direction of the half-plane
  cone, and the citation's applicability there is UNVERIFIED. Until checked it is not even
  corroboration; the two-line self-contained proof is the only support.
- Receipt: problem/C1_corner_route_REFEREE_iter72.md; note section 6.6.4(a)

## Standing scope
No unconditional improvement of the lattice variance bound is claimed.
Nothing here solves chi = 1/3. The conditional theorem's hypotheses are all open on Z^2 today.
P-a's strong form remains gated on fluctuation-scale moment inputs; only the weak form follows unconditionally.
Entries 16-17 are conditional on a referee now running; nothing from them is exportable until it returns.

## 21. Diving-chain sketch (I8 from curvature): REFEREED REPAIRABLE
- Status: REPAIRABLE, corrections applied in place (iter 81). The feared fatal point - a
  first-order tilt leak in GEOM - DOES NOT EXIST: the chain telescopes exactly, and a slope lemma
  shows H2-pointwise-UPPER at e_2 plus convexity/evenness controls the tilted second difference,
  because the class fixed point keeps tilt-over-increment <= C_K - 1 = 2.02 at every level. MY
  STATED REASON for G2 ("the arc shrinks") was WRONG - corners can accumulate at e_2, referee
  counterexample - the conclusion holds for the ratio reason. THE CONVERGENCE: the referee's G1
  repair (re-type the far child as bulk; fixed point C_K = 3.019 at K=5, xi=3/4) is the SAME
  architectural fix as addendum Part 3, found independently - the strongest evidence yet for the
  architecture. Quantile defect = my self-caught slip, same repair, same price: honest bound
  A_+(l) = O(sqrt(l) (log l)^{max(1,2/theta)}); the single-log claim is struck. Corrected prize:
  the TRUE hypothesis set is H2-pointwise-upper at e_2 + arc-curvature AS CONSUMED BY the published
  wandering input + concentration + full-plane Alexander - no hypothesis NEW to the sketch's named
  inputs, but NOT "nothing beyond the program's H2" as first claimed. Still a SKETCH: a follow-up
  referee on the merged v2 (sketch + Parts 1-3 + these repairs, as one document) is owed before
  any export.
- Receipt: problem/I8_sketch_REFEREE_iter74.md (267 lines); corrections in the sketch file with
  [REF] tags

## 21b. Consolidated v2 (iter 82): problem/I8_from_curvature_v2_iter82.md
- One document, one hypothesis ledger: (H-curv) pointwise-upper at e_2 in profile form; (H-wand)
  with its HONESTY CLAUSE (arc-curvature enters through the wandering input's pedigree, stated
  once, not hidden); (P-Alex) and (P-conc) published. Two-spine dive, branching one, slope lemma
  as the hinge (one lemma, two jobs), A = 2 quantile reconciled. Conclusion: A_+(l) =
  O(sqrt(l)(log l)^{max(1,2/theta)}), hence I8, hence the corner threshold alpha > 1/3 -
  package-relatively, assembly exactly for chi in (1/3, 1/2). NOT YET REFEREED AS A WHOLE; the
  owed referee's four named targets are in the document's section 6.
- Receipt: the v2 file; sources listed in its footer

## 22. I3 candidate closure: the entropy route bypasses the QV gap entirely
- Status: WALK WRITTEN, PENDING REFEREE (iter 86). The corner referee's one named place for I3 -
  Kesten's predictable-QV bridge - is a feature of Kesten's 1993 route only. The modern
  Talagrand-strength presentation (ADH survey 3.4.2, the argument of Damron-Hanson-Sosoe's
  appendix) contains NO martingale and NO QV: Herbst + entropy tensorization + the
  Boucheron-Lugosi-Massart symmetrized LSI + optimizer combinatorics + ONE geometric input (an
  exponential moment on the geodesic-intersection count) - and for bounded weights on wall pairs
  that input is DETERMINISTIC via the refereed Claim 4 (#G_+ <= (b/a) r). Every step walked and
  labeled H-safe in problem/I3_entropy_route_walk_iter86.md; the t-range restriction matches the
  consumer's needs with room to spare; the lower tail is not consumed. CAVEATS: unrefereed; and
  the source was read through a lossy pypdf extraction - the walk file says so and demands the
  referee check against a clean copy. NO status copy updated anywhere (corner note, entry 16,
  STATE) - all correctly still read "no obstruction identified" until this walk survives review.
- Receipt: problem/I3_entropy_route_walk_iter86.md; scratchpad adh_survey_text.txt pages 47-49

## 23. v2 consolidation: REFEREED - MAJOR REVISION, statement-level repairs only
- Status: MAJOR REVISION (iter 88/89; report problem/I8_v2_REFEREE_iter83.md, relocated from the
  scratchpad byte-identical, sha 256d8927...). Every re-derived bound SURVIVES; no exponent moves.
  THE WORST DEFECT IS THE ONE I BRIEFED THE REFEREE TO HUNT: the consequence chain silently
  consumed I3, which appeared ZERO times in the "one hypothesis ledger" - fixed in place as
  (H-I3), and every v2 consequence is now explicitly conditional on I3's pending walk (entry 22).
  Statement-MAJOR: (H-wand) was scoped to the anchored class whose wandering the proof never
  consumes - re-scoped to the priced pairs. FAVOURABLE correction: the honesty clause was FALSE
  as a universal in the GOOD direction - the referee checked the fetched Newman-Piza source and
  its printed condition is a ONE-SIDED enclosing ball, so the imported pedigree is WEAKER than
  v2 claimed; the G3 tail-form citation debt is reinstated. Remaining v3 items: far-depth WINDOW
  (exact far-depth is not step-stable off s' = s; root's D = 0 branch was excluded), slope lemma
  re-wired (v2's chain never forms the tilted-base object; a simpler CENTERED bound does the job
  with better constants), one touching-account constant bug, two false K^xi-clearance claims to
  strike. Touching account and base case PASS as re-derived.
- The subagent also filed its own brain memory (i8_v2_referee_major_revision_np_one_sided) - the
  first referee of the campaign to write back to the shared brain unprompted.
- Receipt: problem/I8_v2_REFEREE_iter83.md; [V2REF] tags in the v2 file

## 24. hard_b1 head-to-head: first content-direction signal, and the first measured case of notes misleading
- Status: MEASURED, blind-graded, integrity-audited (iter 93). Faulted half n=8: none 3/8, placebo
  4/8, on 6/8; clean half 8/8 all arms, FP 0 everywhere. on-vs-placebo +2 (discordant 3:1,
  p=0.625, MAX DETECTABLE 4); on-vs-none +3 (4:1, p=0.375, max detectable 5). n=8 measures
  direction and size, NOT significance - stated in the scoreboard in those words. Mechanism
  audited per discordant: the three on-wins carried the governing theorem in-packet and named the
  key step; hb-02 is the program's FIRST measured instance of relevant notes MISLEADING (holding
  Scheffe, the on-arm approved the false mass-preservation step both other arms caught) - n=1,
  a sighting, not a rate. Store coverage 10 strong/6 partial/0 none; NO FPP contamination (the
  five campaign claims postdate the retrieval snapshot; none served). All 48 attempt-1 verdicts
  discarded for cause; 48 fresh calls verified served-by-haiku; arms_guard PASS; $2.62.
- Conduct: the agent respected the lease (staged in the scratchpad per pre-authorization),
  notified the mesh, cancelled its handoff explicitly, and wrote its own brain memory. Relocated
  under my claim iter 93: 53 files, every one sha-verified.
- Receipt: eval/hard_b1/results/HEAD_TO_HEAD.json + H2H_BLIND_TABLE.json + run/ tree

## 25. Combined referee (entropy walk + v3 document): BOTH REPAIRABLE - and both repaired in place
- Status: REPAIRED (iter 98; report problem/WALK_V3_REFEREE_iter94.md, relocated sha-verified).
  WALK: the real defect was mine in S8 - setting the variational parameter to the scale collapsed
  the Gaussian range to a bounded interval; the printed range was NOT delivered. Repair applied
  with the referee's explicit constants (a0 = 1 constant, lambda window (0, 1/(2b)), final bound
  exp(-a_w t^2/(16 b^3)) for t in (0, 4 b^2 sqrt(r)/a_w)) - zero exponent cost, and Claim 4's
  deterministic moment survives as the survey's auxiliary-lemma replacement. All-distances branch
  added (S9-a). FIDELITY CAVEAT CLOSED: the referee fetched DHS arXiv:1401.0917 Appendix A, which
  quotes BLM Theorem 6.15 VERBATIM in the consumed form. W1/W2/W5 passed; W6's premise was partly
  wrong in MY brief (the v3 recursion never consumes I3 - only the corner note's consequence
  chain does).
  V3 DOCUMENT: my iter-92 window repair OVER-SHOT - the solid interval soldered a dead band into
  the class that the re-scoped (H-wand) cannot price, and D = 0 below the root broke
  branching-one; the sketch referee's PUNCTURED window was load-bearing all along. Restored:
  {0} UNION [sigma W_{s'/K}, C_K d(K s')], tilt now DERIVED (t(s) had been undefined - patchwork
  finding 4), two-child step at D = 0 with contractive branching. Patchwork findings all fixed:
  the governing sigma definition finally carries /c (the bug the banner CLAIMED fixed was live in
  the definition that mattered), the vestigial fixed-point sentence marked idle, the stale attack
  list replaced with the four current surfaces. GEOM/touching/consequence chain passed.
- The night's recursion on this class: sketch referee punctures the window; I "simplify" to solid
  and break it; combined referee restores the puncture. The lesson is the same as the evening's:
  a repair that makes a refereed object SIMPLER is a hypothesis, not an improvement, until the
  reason for the original's shape is understood.
- Receipt: problem/WALK_V3_REFEREE_iter94.md; [REPAIRED iter 98] and [V3.1]/[V4-x] tags in both
  files

## 26. Localization draft: the constant chase (G-c) closed by hand
- Status: DERIVED (iter 114), PENDING REFEREE - the draft's referee brief shrinks from
  "re-derive with explicit constants" to "check this arithmetic".
- The display: P(dev >= sigma W_r) <= 18 C1 (b/a_w) r exp(-c'' c_- sigma^2) with
  c'' = c1/(6 sqrt(2 + b/a_w)); Form B absorbs the linear factor at
  sigma^2 >= (2/(c'' c_-)) log(18 C1 (b/a_w) r). U[1,2]: c'' = c1/12 (c1/24 absorbed).
  The exponent is r-free because the sqrt(r) the curvature penalty earns cancels the sqrt(r)
  the concentration normalization spends - the chi' = 1/2 vs xi' = 3/4 identity itself.
- One same-iteration correction told straight: the first range-ledger print mixed a squared and
  a linear constraint (C''' = min(delta^2, 3C2/c_-)); the audit pass showed the wlog
  delta <= min(1, 3C2/c_-) makes the single constraint sigma^2 <= delta^2 sqrt(r) imply both
  (P-conc) range checks, so C''' = delta^2 clean. Corrected in the draft in place.
- Receipt: problem/localization_tail_draft_iter106.md (G-c block + STATUS line); LOG iters 114.

## 27. Both seams of the conditional chain hand-passed - one missing sentence found, one of my
##     own claims corrected
- Status: CHECKED BY HAND (iters 115-116), PENDING the owning referees; tagged mine-not-acceptance
  in every bracket.
- Seam 1 (tail lemma -> v2): upper range CLEAN at all consumption scales (base case s0 = l^c,
  c <= 0.12, so sigma^2 = Theta(log l) sits inside delta^2 sqrt(r') for any fixed delta); lower
  range exposed the missing sentence - v2's A = 2 was chosen for its union blind to the lemma's
  Form-B threshold; compatibility line A >= max(2, C3 c'') recorded on both sides ([V5-1], and
  the draft's consumer contract). Wiring named: theta = 2, C = 1,
  c = (c''/2) c_- = c1 c_-/(12 sqrt(2 + b/a_w)).
- Seam 2 (walk -> corner note): coverage UNCONDITIONAL in r - at any z the deterministic branch
  (r < (z/b)^2) overlaps S8's range floor (r > (a_w z/(4b^2))^2) because a_w < 4b always; no
  smallness condition on the consumer's delta exists. Candidate instantiation bracket at the
  note's cost formula: S_+ = sqrt(r), theta = 2, c = a_w/(16 b^3), pending the walk's referee.
- The correction: my iter-114 G-c parenthesis claimed the walk supplies "exactly" the H-version's
  orientation - HALF-wrong (the walk's own not-covered section: T_+'s LOWER tail is not walked;
  legs-downward would need I2 + A_+(r') at child scales, the G-d revival architecture). Corrected
  in place iter 116.
- Receipt: [V5-1]/[V5-2] in problem/I8_from_curvature_v2_iter82.md; the S9-a overlap bracket in
  problem/I3_entropy_route_walk_iter86.md; the instantiation bracket in
  problem/C1_corner_route_attempt_iter60.md; LOG iters 115-116.

## 28. GEOM K-power discrepancy settled: referee's reading confirmed tight
- Status: DERIVED (iter 117), PENDING REFEREE (the [V5-3] bracket carries the arithmetic).
- Tight coefficient C_K^2 K + 2 K^{1-2xi} (with d(Ks') = sigma W_{s'} read from the definition).
  The document's K^{1+2xi} print is an upper bound iff K^xi >= C_K: FAILS at K = 4 (2.83 < 3.41),
  holds at K = 5 (3.344 > 3.019, ~22% loose), monotone beyond - valid exactly on the document's
  own K >= 5 range, i.e. by parameter choice, not robustness. Nothing downstream moves.
- Receipt: [V5-3] in problem/I8_from_curvature_v2_iter82.md; LOG iter 117.

## 29. Store salvage validated - and the first verdict was my instrument's own defect
- Status: MEASURED (iter 112). The dead verifier's staged rows are VALID: 52 rows = 25 verdict
  targets + 27 dedup-group context (22 canonicals, 5 inferiors, 0 unexplained), every row
  byte-identical to the live store (924/924 untouched). The 05:00 relaunch reuses the staging;
  clean provenance-stamped rebuild also on disk (digest 7287ad24cd98ff84...).
- The confession, on the record: my first validator printed SALVAGE INVALID with 10 "byte
  mismatches" and I narrated a poisoning story blaming the dead agent. The mojibake was
  manufactured by my own bare open() (cp1252 on Windows) at read time. A second reader with
  explicit utf-8 found zero mismatches. Retracted same fire; both wrong artifacts corrected in
  place; the lesson is now TWO firing reflexes (bare_open_reads_cp1252,
  corruption_verdict_needs_second_reader), both production-fired the same hour they were
  compiled (fires registered in instinct_fires.tsv).
- Receipt: scratchpad validate_salvage_b2.py (corrected, supersedes note inside),
  store_rows_for_verification_b2_clean.json (provenance block), MISTAKES.md 2026-08-10 entries,
  LOG iters 112-113.

## 30. Referee 1 (punctured window, two-child branching, dead band): TWO DEFECTS FOUND, REPAIRED
- Status: REFEREED (iter 149; report problem/REFEREE1_window_report.md 31KB, verdicts, and the
  re-derived from the definitions; every load-bearing number reproduced a second way.
- DEFECT 1, REPAIRED IN PLACE: K had NO UPPER BOUND. The document printed "Fix K >= 5" while the
  per-member window needs 2^xi <= C_K, capping K at 37 for xi = 3/4 and at 10 uniformly. An
  unbounded K was free to violate the window that same section defines. Now "5 <= K <= 10".
- DEFECT 2, NEW - no previous round found it: (H-wand)'s printed depth range FAILS TO COVER THE
  WINDOW'S DEEP END by a factor C_K K^xi = 10.09. Three earlier rounds checked the shallow end,
  found a mismatch, and repaired it; the deep end was never examined. Free to fix in kind, but a
  real hole until written - any consumer quoting the hypothesis at the deep members was quoting
  something the line did not supply.
- CONFIRMED, with reasons the document lacked: branching-one holds because the puncture stratum is
  a SOURCE with no incoming edges (far-depth map is constant, so no child ever has far-depth 0);
  the dependency graph is a PATH, not a tree. And the puncture is necessary ARCHITECTURALLY, not by
  estimate: any chain's last segment can be typed only as anchored (needs D = 0) or bulk (needs D
  at its own scale's quantile), so the punctured window is exactly the union of the two typings.
- OWED, now flagged in the document: read literally the sup recursion carries coefficient 2 at every
  level and survives by 0.001 in the exponent (l^0.4990 vs break-even c = 0.12176).
- INCIDENTAL: my iter-117 [V5-3] result independently reproduced by brute force (K = 5 valid, K = 4
  fails), with one of my constants sharpened - the second term is 2^{2xi} K^{1-2xi}, where I wrote
  2 K^{1-2xi}, small by 1.41 at xi = 3/4.

## 31. Referee 2 (entropy walk): ALL FOUR CONFIRMED, AND THE CONSTANT IMPROVED TWOFOLD
- Status: REFEREED (iter 154; report problem/REFEREE2_walk_report.md 22KB, verdicts, check script
  and its output, relocated sha-verified).
- CONFIRMED: (S3) tensorization - convention re-derived, and T_+ is a min over a FIXED path set, not
  a conditioned law, so the half-plane cannot break the product; (S5) - stronger than claimed, NO
  measurable selection is needed, membership in the geodesic intersection being Borel in the finite
  localized problem, and non-uniqueness only shrinks the intersection; (S8) - all four constants
  EXACT, reproduced symbolically and again via an independent variance-proxy parameterization, both
  branches agreeing at the endpoint, with the survey display re-derived from entropy duality so the
  walk no longer leans on that extraction; (S9-a) and the corner instantiation - overlap iff
  a_w < 4b with threshold ratio <= 1/16, not marginal, and neither z nor r enters.
- IMPROVED: Claim 4's DETERMINISTIC bound on #G_+ makes the variational step redundant, giving
  exp(-a_w t^2/(8 b^3)) on the same range - factor two better, and it DELETES the parameter whose
  mis-setting (a = r) was the original defect. The mechanism of the old bug is removed, not merely
  set safely.
- DEFECT, marked IN PLACE at its head rather than rewritten: S9-a's iter-98 sentence evaluates its
  condition at b r* where it must be b r, so as printed it is a covering argument that fails on
  exactly the small-r part it exists to cover. The iter-116 bracket below it is correct and was
  confirmed. Two smaller items recorded: the omitted precondition lambda <= 1/b, and "room to
  spare" holding only at the top scale.

## 32. The construction's scope has a number, and the number is the base case's price
- Status: DERIVED (iters 150-153), from referee 1's l_0 caveat.
- The class and (H-wand) both need o(1) chord tilts; the tilt binds at the BASE scale, where it runs
  ~44-88 at l = 1e6, ~19-38 at 1e30, above 1 at 1e65, and drops below 1 only past l_0 ~ 1e80-1e90.
  Consequence stated with the theorem: no numerical experiment at any reachable size can test the
  regime where the hypotheses hold - every machine-check in this campaign tests bookkeeping.
- DIAGNOSIS: the threshold is NOT geometric. It is a steep function of the base exponent c
  (1e85 at c = 0.12, 1e49 at 0.20, 1e31 at 0.30, 1e18 at 0.50, 1e10 at 0.80), and c is capped by
  the base case READ LITERALLY - the same coefficient-2 reading that referee 1's stratification says
  is wrong. If the owed sentence lands, it promotes the base case from lucky to proved AND drags the
  scope down by orders of magnitude. NOT CLAIMED: the base-case constraint under the stratified
  reading, which is the referee's territory.
- MY OWN ERRORS, kept: I first computed the threshold at the top scale (getting 1e7-1e9) and was
  about to record that the referee had overstated its case; and my iter-115 seam check covered the
  quantile and scale dimensions but never the ARC/TILT dimension, which is the one that pins the
  seam to l_0. Both corrected in place.

## 33. Referee 3 (localization lemma, the two-consumer object): SURVIVES, with corrections applied
- Status: REFEREED (iter 162; report problem/REFEREE3_localization_report.md + three check scripts
  with outputs, relocated sha-verified). Mechanism and every exponent CONFIRMED; my constants took
  four corrections and two new required conditions; one genuine hole closed by the referee's own
  curvature-free repair; one conditional narrowing exported to v2's ledger.
- Corrections (draft section 6, REF3-1..8): prefactor 12 C1 (b/a_w) r; C''' = delta^2/4; required
  wlog c1 <= 3 sqrt(2+b/a_w)/C3; r >= r_0 (range EMPTY below, measured 1e5.5-1e14); theta <= 2
  delta M and n_0 4-9 orders above my print in G-f(ii); G-f(i) justification defect repaired by the
  restricted union; G-b(ii)'s reading proved free for axis-aligned spans and FALSE by 4.5% for the
  tilted spans v2 consumes - v2 must declare the stronger reading or use the restricted union.
- The referee's repair: sites beyond j in [-delta r/2, r + delta r/2] die by CONVEXITY alone
  (excess >= g(e_2) x overshoot), no curvature consumed - the main new mathematics of the round.
- Seam: [V5-1] confirmed, vacuous under the new wlog. [V5-2] DEFECT (mine): asymptotic with
  unstated l_1 ~ 1e91-1e127, above v2's own scope threshold. Recorded at the bracket in v2.
- The queue's verdict pattern, three for three: re-deriving referees each found what previous
  rounds missed, and each returned something better than a verdict - a bound on K, a twofold
  constant, and here a curvature-free union repair.

## 34. CRUX 9.5-9.9 (the wall's (L1')/(L2')/(L3) reduction + far-block closure): REFEREED, SURVIVES
## WITH ONE FALSE IDENTITY REPAIRED - the delivered chaos constant is 1/(16 kappa4 beta^2 C_occ)
- Status: REFEREED 2026-08-12 by a fresh session (17556890) that authored none of it; every
  load-bearing step re-derived from MG2B's statements and the localization draft, not the prose.
  Report: problem/CRUX9_wall_referee_20260812.md (defects D1-D6, confirmations C1-C4).
- D1 (the sharp one): 9.5's support identity "Delta = 0 off U_L" is FALSE (MG2B Remark 4.4 has the
  correct support U union Uhat; the resampled field's geodesic can improve through an untouched
  block). MEASURED same day: off-U negative increments at 11-12 pct frequency on corridor blocks,
  15-20 pct of E[Delta^2] (seed 20260812, 6000 reps, zero Lemma-4.3 violations as harness guard).
  Damage bounded: p m_k <= E[Delta^k] <= 2 p m_k by symmetry + positive-part support, so the
  kurtosis forcing survives at p >= 1/(4 kappa4). Repair: A4 <= Sum p_L m4_L directly (no 1/2),
  C2 = kappa4 beta^2 C_occ, eps <= 1/(16 kappa4 beta^2 C_occ) - still a constant; the reduction's
  conclusion stands at half the printed constant.
- D2: 9.9's far-sum display drops one M (n^3 M^{11/4}, not M^{7/4}); the quantile and the
  O(M^{7/4}) near-band count are nevertheless CORRECT (the requirement divides by the target's M) -
  re-derived independently.
- D3: 9.9 quotes Form A's pre-REF3 range; corrected to (delta^2/4) sqrt(R) in place; conclusion
  unchanged.
- D4 (gap closed in kind): 9.9 closed only (M1)'s far remainder; (M2)'s closes identically one
  power of n later - new CRUX section 9.10, sigma_0 leading term sqrt(5 log n) instead of
  sqrt(3 log n), both hypotheses now needed only on the same O(M^{7/4}) axis blocks. Flagged as
  referee-derived, not independently counter-checked.
- D5: localization statement page was STALE (pre-REF3 prefactor 18, missing /4 range, missing
  floor/wlogs, status still NOT REFEREED) - synced with [SYNC 2026-08-12] tags; the draft remains
  authority. D6: the polylog block-height inflation walked against MG2B's H2 - no coupling breaks.
- Confirmations: 9.8's exchangeability identity and conditional step (C1); 9.7's three geometry
  answers with the chord-tilt accounting made explicit (C2); 9.6/9.7's boundary-pair debt is PAID
  by G-f + REF3 (C3); the (L3)-absence price eps <~ 1/n (C4).
- Conditionality now stated AT the claim: the extent-shrink of the wall (near-band-only (L1')) is
  c_--conditional; only the reduction arithmetic itself is hypothesis-free. chi = 1/3 unmoved.
- [REF-W2 DISCHARGE, 2026-08-12 ~06:2x - independent counter-check by a separate session, report
  problem/CRUX9_wall_referee_W2_20260812.md, derive-first.] BOTH owed items DISCHARGED. D1 repair:
  CONFIRMED on all four items, eps <= 1/(16 kappa4 beta^2 C_occ) exact, downstream quote sweep
  clean. 9.10 closure: CONFIRMED-WITH-REPAIRS - the n^5 M^{11/4} display and sqrt(5 log n) radius
  re-derived and match, but MY headings said "one power of n later" (it is TWO: cap n^2->n^4, far
  sum n^3->n^5) and MY scope block was INVERTED - the binding threshold is the quantile-in-range
  r_1 ~ (2q)^2 r_0 (measured 40-160x above r_0), NOT REF3's emptiness floor; closures hold for
  Mn >= r_1. Repairs applied in place with [REF-W2] tags. The referee chain caught the referee.
