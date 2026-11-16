---
name: math_recall_title_drop_leading_the_fails_probes_0_real_changes_2026_11_08
description: "[VERIFIED] Should the title lane match a card title without its leading 'The' ('key renewal theorem' for The Key Renewal Theorem)? No: built probes 10 of 25 misses rescued (bar 13), 0 of 171 lost; 501 real wordings, 0 changed; not landed"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:47:01+04:00
  status: verified
  evidence: "title_the_ab_2026_11_08.py and ab_s1108.out (rule in the header, written before the run)"
---

Should math_recall's title lane match a card title with its leading "The" left out? Not by default: on built probes it rescues 10 of 25 misses, under the bar of 13 written before the run, though it loses nothing. Measured 8 Nov 2026 by an agent.

The miss. "key renewal theorem" put the generic "Renewal process" card first over "The Key Renewal Theorem (Smith's Theorem)" (5th for the longer "renewal theorem key renewal Blackwell"). The title lane matches a wording against whole titles (case, punctuation, a possessive and a parenthetical tail aside), but a leading "The" stays in the key, so "key renewal theorem" never equals "the key renewal theorem". Found on the W09 run of five probability questions; the other four put the right card first or within the top 7 (Doob, LIL, coupling from the past at 1; Chernoff bound 7th behind Bernstein and tensor Chernoff cards for a long wording, 1st for "Chernoff bound").

The fix tried. In a candidate copy (math_recall_cand.py) the title lane's sub-title index also holds each key with a leading "the " dropped, behind MATH_RECALL_TITLE_THE (default 0). With it on, "key renewal theorem" puts the Smith's Theorem card 1st. An exact plain title still wins: the whole-title index is read first, and only 8 of the 198 "The" titles have a plain-titled twin.

The tests, rule written before the run in title_the_ab_2026_11_08.py: on only if (a) at least half of the probe misses reach rank 1 and probes at rank 1 lose it at most once, and (b) no changed first card on real wordings is judged worse.
- Probes, 196 titles starting "The", asked without "The" and without the parenthetical tail: 171 at rank 1 already (0 lost with the flag on), 25 not, 10 of those rescued. (a) FAILS.
- Real wordings: 501 distinct wordings from the second machine transcripts, 0 first cards changed and 0 lists changed, so (b) holds trivially: no agent asked a "The" card that way.
- Of the 15 probes left unrescued, 9 are cards whose titles are sentences that open with "The" (conjecture statements, "The read-once FEI certificate's region-1 bound was rebuilt ..."), which no one asks by name; 5 are titles with a plain twin (Banach-Tarski twice, the continuum hypothesis, the self-avoiding walk, the probabilistic method), where a plain card already answers; 1, "N Problem", misses with the flag on and off. The rule counted them all, and the bar was not moved.

How to apply: ask a "The ..." card by its full title, or put the plain wording in one --or and the title in another. The switch was not put in the live file: with 0 real changes, the code would buy nothing. The candidate and the A/B (ab_s1108.out, ab_s1108.json) are in title_the_2026_11_08 for the next reader who finds a real miss of this shape.

Related: [[math_recall_title_minus_paren_tail_first_2026_11_08]], [[math_recall_title_inside_longer_wording_real_4_better_1_worse_of_469_2026_11_08]], [[math_recall_spaced_name_join_helps_probes_hurts_real_wordings_off_2026_11_08]].

