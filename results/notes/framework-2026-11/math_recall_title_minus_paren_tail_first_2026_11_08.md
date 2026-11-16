---
name: math_recall_title_minus_paren_tail_first_2026_11_08
description: "Yes since 8 Nov: math_recall puts a card first when the wording is its title minus the parenthetical tail ('Hanson-Wright inequality' had ranked its card 12th, in neither title index); tail-removed titles hit@1 109->147 of 150, 0 worse, full titles and controls 0 of 200 changed, real 4 of 477 better; MATH_RECALL_TITLE_STRIP=0 off"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:15:01+04:00
  status: verified
  evidence: "title_strip_ab_2026_11_08.py A/B json in tstrip/ab.json; framework 9db54e0489d0"
---

Does math_recall put a card first when the wording is its title minus a parenthetical tail? Yes, since 8 Nov 2026 (an agent). Before that, no.

Many store titles carry a gloss in parentheses: "Hanson-Wright Inequality (Concentration of a Quadratic Form)", "McDiarmid's (Bounded Differences) Inequality", "Hewitt-Savage 0-1 Law (Stronger Than Kolmogorov's, ...)". The whole-title index held only full titles. The contained-title loop of [[math_recall_title_inside_longer_wording_real_4_better_1_worse_of_469_2026_11_08]] did index the shortened titles, but it tried only word runs shorter than the wording, never the whole wording. So "Hanson-Wright inequality" was in neither index. Its card came 12th, under 11 lemma cards from one paper (arXiv:2505.20799, "...sparse Hanson-Wright inequalities"). Each of those cards carries the paper title in its body, which makes "hanson-wright" a common term. Writing the name with a space ("Hanson Wright inequality") put the card 1st, which is what gave the cause away.

Fix: the contained-title loop starts at the whole wording (MATH_RECALL_TITLE_STRIP, on by default, 0 turns it off). It is two edits, made by mk_title_strip_2026_11_08.py, which refuses if the live lines moved.

Measured in one process, off against on, arms alternating, usage logging stubbed (title_strip_ab_2026_11_08.py):
- Titles with the tail removed, as bare wordings: hit@1 went from 109 to 147 of 150, 0 worse.
- Full titles: 0 of 100 lists changed.
- Six-word body openings: 0 of 100 lists changed.
- Real wordings from the second machine's transcripts: 5 of 478 first cards changed, all better by hand (Hanson-Wright; McDiarmid; Hewitt-Savage in both spellings, where the theorem's card beat the general zero-one-laws card; Doob). The Hanson-Wright wording was my own probe, so 4 of 477 held out.

Live on the second machine. The pre-change copy is math_recall.py.pre_titlestrip_20261108, and with the switch off the output matches it. In brain-framework as 9db54e0489d0. The brain repo's dreaming mirror is not updated, because that is an overwrite and waits on git sync approval.

How to apply: when a card that obviously answers ranks low, try the wording with its hyphens as spaces and with the card's exact title. If either one lifts it, the cause is in the term or title lanes, not in the store. The same night turned up a second, separate miss: a name pair in the other order ("Hoeffding-Azuma") shares no term with the card, because the tokenizer keeps a hyphenated word whole. That one is measured on its own.

Added 8 Nov: the name-pair miss is fixed too, measured on its own on top of this rule. A two-part hyphenated term the lexicon lacks whose reverse it holds is also asked in the other order, as its own wording fused by rank (MATH_RECALL_PAIRSWAP=0 off; pre-change copy math_recall.py.pre_pairswap_20261108; framework 501e67cf5406). 150 swapped-order titles: hit@1 122 to 148, 0 worse. Full titles and controls: 0 of 200 changed. Real wordings: 1 of 480 changed, Hoeffding-Azuma, better. 'Hoeffding-Azuma concentration' still misses after the swap.

Third fix the same night (ATTEMPT_DEMOTE, MATH_RECALL_ATTEMPT_DEMOTE=0 off): an 'Attempt on X' proof record keeps the first slot only when a wording holds at least half of X's 3+-letter content words; otherwise the first non-attempt card leads and the attempt moves to second. Before it, 21 of 481 real wordings got an attempt first, 7 of them one long excited-random-walk record. A/B (attempt_ab_2026_11_08.py, generator mk_attempt_demote_2026_11_08.py): 150 open problems with their attempts as gold, hit@1 147 to 147 and 0 lists changed; full titles 0 changed; controls 0 rank changes. Of the 21 real changes, by hand 10 better (Wald, Polya, Matthews x2, Tanaka to Ray-Knight, total-progeny wordings to Kesten's tree), 2 worse (coupon-collector, hypercube mixing time), 9 neutral or junk wordings. Wald and the Z^d wording were the cases that prompted it, so not held out. Live; pre-change copy math_recall.py.pre_attemptdemote_20261108, switch off equal to it on 5 of 5 wordings; brain-framework b10f14f3f3e6.
