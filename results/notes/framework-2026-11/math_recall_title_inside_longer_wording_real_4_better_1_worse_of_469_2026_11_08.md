---
name: math_recall_title_inside_longer_wording_real_4_better_1_worse_of_469_2026_11_08
description: "[VERIFIED] Yes since 8 Nov 02:03: math_recall's title lane puts a card first when its title sits inside a longer wording (filler-only words before it, more than half the words, guards for the word-ranked #1); real wordings 4 better 1 worse of 469, controls 0 changed; MATH_RECALL_TITLE_SUB=0 is the off switch"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T02:04:28+04:00
  status: verified
  evidence: "469 real wordings off/on: 4 better 1 worse; pos 150 hit1 105->133 0 worse; ctl 120 0 changed; switch checked against pre-change copy"
---

Since 8 Nov 02:03 the second machine's math_recall title lane also catches a card title inside a longer wording. Before, only a wording that was a whole title went first, so "optional stopping theorem for martingales" put a uniform-integrability card at #1 and Doob's theorem at #2, and "Vitali convergence theorem uniform integrability" put Convergence in L^p first.

The rule, used only when no whole title matches: take the longest run of the wording's words that is a current card's title (its parenthetical tail aside), with at least 2 words and 10 characters, covering more than half the wording's words. Three guards came from reading real failures:
- Only filler words (the, of, proof, state...) may come before the title. A real word there names another object: "local central limit theorem" is not the CLT, and in "Chernoff bound for sums of independent random variables" the 5-word "sums of independent random variables" is not the subject.
- The word-ranked first card keeps its place when its own title is in the wording.
- It also keeps its place when its title holds the matched title plus another word of the wording (martingale CLT over the plain CLT).

Measured, same process, off against on, arms alternating, usage logging stubbed:
- Real wordings agents gave math_recall (all 469 distinct ones in the second machine's transcripts): 5 first cards changed. 4 got better (Azuma-Hoeffding, Kolmogorov 0-1, optional stopping, Vitali) and 1 got worse ("branching process survival" now puts the Branching process definition over the extinction criterion, which drops to #2).
- Store titles in neutral wrappers, 150: hit@1 105 to 133, 0 worse, MRR 0.742 to 0.909.
- Controls, 120 six-word body openings: 0 lists changed.
- Hand questions, 5: hit@1 2 to 5.

The design used the first 400 real wordings, and the other 69 changed nothing, so the real-wording number is not held out. Earlier versions were worse: without guards, about 9 of 21 changes were for the worse; with the qualifier guards only, 3 of 10.

Off switch: MATH_RECALL_TITLE_SUB=0 (checked: the old file and the new one with the switch off print the same first card). MATH_RECALL_TITLE_SUB_HEAD=0 drops the filler-words guard. Pre-change copy: math_recall.py.pre_titlesub_20261108. Generator (refuses if the live code moved): mk_title_sub_2026_11_08.py. Banks: title_sub_ab_2026_11_08.py and title_sub_real_queries_2026_11_08.py in the same folder. The resident math_recall_server restarted on the source change (02:03:34) and serves the new code. The brain-framework copy does not have it yet.

Testing scar: in zsh, `env $e cmd` with e="A=0 B=0" passes one argument, so the off arm silently ran on. Spell each variable out.

Related: [[math_prefilter_allwords_live_qform_41_to_47_fresh_0_of_218_2026_11_08]], the all-words change of the same night.

Related: [[math_recall_ranked_exact_title_cards_low_title_lane_puts_them_first_2026_10_30]] - the whole-title lane of 30 Oct that this extends to titles inside a wording.

Update 8 Nov 02:09: ported to brain-framework 2fb05d5 (the same 48 diff lines, applied by the same generator; on its build hand 2 to 5, titles-in-wrappers 18 to 28 of 30, 30 controls 0 changed; origin bytes equal to the local file).
