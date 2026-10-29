# Brief for referee W2: counter-check the W1 session's own corrections (WRITTEN 2026-08-12,
# NOT YET LAUNCHED - compute in memory-commit distress; launch when compute clears, ONE agent,
# a few minutes past the hour, task id logged before anything else, incremental writes to
# problem/REFEREE_W2_report.md, final message counts-and-paths only)

## Why this referee exists
Session 17556890 refereed CRUX 9.5-9.9 (report problem/CRUX9_wall_referee_20260812.md, ledger 34)
and in doing so AUTHORED new claims of its own: the D1 repair (constant 16), the factor-2 bracket,
and section 9.10 ((M2)'s far-remainder closure at sqrt(5 log n)). The campaign's law: the author's
hand-reading is exactly what fails; a repair that survives its own author is a hypothesis. These
need eyes that did not write them.

## Protocol - SEALED, derive-first (the claim-25 protocol, written to the brain as method)
Phase 1, BEFORE opening CRUX9_wall_referee_20260812.md or any [REF-W1] tag: from
MG2B_framework_lemma_draft.md (Definition 3.3, Lemma 4.2/4.3, Theorem 8.1, (M1)/(M2)/(9.2)) and
CRUX 9.5's hypothesis block ((L1'), (L2'), (L3)) ALONE, derive:
  (a) the exact support of Delta_L = X^Lambda - X (on which event is it zero?);
  (b) the sharpest constant c in "eps <= 1/(c kappa4 beta^2 C_occ)" that (L1')+(L2')+(L3)
      deliver through (9.2) - derive the A4 bound from scratch, deciding yourself whether any
      factor 1/2 is available;
  (c) the far-remainder requirement for (M2) analogous to 9.9's for (M1): what sigma_0^2 suffices?
Write these three verdicts to the report file FIRST, timestamped.
Phase 2: open the W1 report and the [REF-W1] tags, compare, and adjudicate every disagreement by
re-derivation, not by majority.

## Specific attack surfaces (from the W1 session's own doubts)
1. D1's bracket upper end: E[Delta^k] <= 2 p m_k rests on E[(Delta^-)^k] = E[(Delta^+)^k]
   (symmetry) plus (Delta^+) supported on U. Verify the symmetry step survives the canonical
   geodesic SELECTION (Remark 4.4's rule-dependence) - is (X, X^Lambda) exchangeable for a FIXED
   measurable tie-breaking rule, or only for symmetric rules?
   [NARROWED 2026-08-12, same session, by READING not deriving: MG2B Lemma 4.1(iii) proves the
   exchangeability outright via the swap involution, with "[deterministic selection; no uniqueness
   needed]" at (ii) - MG2B is refereed, so the symmetry step inherits that status for any fixed
   measurable rule. What remains of this surface: confirm that reading of 4.1(ii)-(iii) in one
   line, and note 1(U) o S = 1(Uhat) (the indicator is NOT swap-invariant - the bracket must and
   does route support through 4.3's (4.1), never through swapping the indicator). Spend the freed
   effort on surfaces 2 and 3.]
2. 9.10's per-block cap m4-type <= C^4 n^4: the (b-a)(b/a)(n+W) occupation cap is quoted for the
   OLD geodesic's occupation on U. Confirm the A4 far summand needs ONLY the positive part on U
   (it does per Theorem 8.1's definitions - verify), so the new-field geodesic's occupation is
   never needed there.
   [NARROWED 2026-08-12 by citation: MG2B line 120 defines A4 := Sum_Lambda E[1(U_Lambda)
   ((X^Lambda - X)^+)^4] - indicator and positive part are in the DEFINITION, so the definitional
   half of this surface is settled by reading. What W2 still owes here: the cap application
   itself - on U_Lambda, (Delta^+) <= (b - a_w) |gamma_can(omega) cap Lambda| via the old geodesic
   as candidate path in the resampled field, and the occupation lemma's (b/a_w)(n+W) applied to
   gamma_can. Check the candidate-path step and the constants, not the definition.]
3. The numeric witness (REFEREE_W1_check.py, seed 20260812, results REFEREE_W1_results.json):
   re-run it, and attack the harness - in particular whether geodesic-edge recovery via the
   predecessor tree can mislabel U on near-ties, and whether the 1e-15 slack in dijkstra's
   relaxation can flip a touched verdict. The zero-violation Lemma-4.3 count is the control;
   break it if you can.
4. The 9.8 cross-note (Efron-Stein order-tightness reading): verify MG2B line 111's identity says
   what the cross-note quotes (E[Z^2] = E[Var(X|w_others)]), including the indicator bookkeeping
   (Z carries 1(U); the conditional-variance side does not - reconcile via (4.1)).
   [NARROWED 2026-08-12 (loop fire 1): the reconciliation IS display (4.1) - Lemma 4.3 states
   (X^Lambda - X)^+ = 1(U_Lambda)(X^Lambda - X)^+ EVERYWHERE, so Z's indicator is definitionally
   redundant, E[Z^2] = E[((X^Lambda - X)^+)^2], and line 111's chain is Lemma 4.2 plus that
   display. This surface drops to a two-citation footnote check.]
5. D2's recount: four factors n^2, M, M^{3/4}, Mn -> n^3 M^{11/4}. Trivial; confirm or refute in
   one line.

## What NOT to do
Do not touch the store (read-only). Do not edit any campaign file except your own report. Do not
launch sub-agents. If a verdict contradicts a REFEREED item (MG2B, REF3), the refereed item wins
unless you can exhibit the defect in ITS proof - in which case stop and flag, do not repair.

## Discipline (the campaign's standing rules, they have all burned us)
utf-8 on every open; no bare open(); write incrementally; a zero-byte transcript is not death;
one agent at a time; log the task id first; the report's first line names this brief's sha.

## LAUNCH COMMAND (pre-staged loop fire 9, 2026-08-12 - use verbatim when compute clears)
Agent prompt, one agent, general-purpose, launched a few minutes past the hour:
---
Referee W2 for the FPP chi=1/3 campaign. Read
REFEREE_W2_BRIEF.md
and follow its SEALED derive-first protocol EXACTLY: phase 1 derives items (a), (b), (c) from
MG2B_framework_lemma_draft.md and CRUX section 9.5's hypothesis block ALONE, written timestamped
to problem/REFEREE_W2_report.md BEFORE you open CRUX9_wall_referee_20260812.md or read any
[REF-W1] tag; phase 2 then compares and adjudicates every disagreement by re-derivation. Note the
brief's [NARROWED] annotations: surfaces 1, 2 and 4 are citation-checks; spend your effort on
surfaces 3 (attack the numeric harness, re-run REFEREE_W1_check.py) and 5 (the one-line recount).
Write the report INCREMENTALLY as you work, utf-8 every open. Your final message: verdict counts
and file paths only, at most 12 lines. The report's first line names the brief's sha256.
---
