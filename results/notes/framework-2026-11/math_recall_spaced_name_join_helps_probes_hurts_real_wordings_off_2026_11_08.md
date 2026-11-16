---
name: math_recall_spaced_name_join_helps_probes_hurts_real_wordings_off_2026_11_08
description: "Join spaced name pairs into the store's hyphen compound? Not by default: 20 of 30 probe misses rescued, but 40 of 493 real wordings changed first card (38 via plain pairs); names mode 1 worse; MATH_RECALL_JOIN=names opt-in"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T05:14:25+04:00
  status: verified
  evidence: "join_ab*_2026_11_08.out, join_real*.json, brain-framework ee6ba260defa, 8 Nov 05:14"
---

Should math_recall join two spaced words into the hyphen compound the store knows ("Kesten Goldie" -> "kesten-goldie")? Not by default. It rescues real misses on built probes, but on real agent wordings it moves the first card on plain word pairs. Measured 8 Nov 2026 by an agent.

The miss. The tokenizer keeps "kesten-goldie" whole. "Kesten-Goldie theorem" puts the card titled "Kesten-Goldie theorem: the stationary solution of X = AX + B has a power tail" 1st. "Kesten Goldie theorem", "Kesten theorem", "Goldie theorem" and "Goldie implicit renewal theorem" leave it out of the top 8. compound_variants (3 Nov, off) skips this shape on purpose, because both parts are already in the query.

The fix tried. join_variants in math_recall.py adds one wording with an adjacent spaced pair joined, a-b or b-a, only when that exact compound is in the lexicon, fused by rank. MATH_RECALL_JOIN=1 joins any pair, MATH_RECALL_JOIN=names joins only two capitalized words, and the default is 0. The three wordings written before the edit went 1 -> 1, 9 -> 2 and 9 -> 3.

The tests, each with its rule written before the run:
- Run 1, whole card titles with the hyphen as a space: failed, 0 of 30 misses rescued. 26 of the 30 were cards whose title a twin card shares, and the title lane already finds a whole spaced title, since it sets punctuation aside. Its 180 controls had 0 worse.
- Run 2, the spaced compound plus three words from the card's body, scored twin-aware: passed. 20 of 30 misses reached the top 3, and 120 controls had 0 worse (the found arm had 16 better).
- Real wordings from the second machine's transcripts, 493 of them, any-pair mode: the join fired on 198, and 40 first cards changed. 38 of the 40 came through plain pairs such as "random walk" or "local time"; for example "Wald identity stopped random walk" lost Wald's Second Identity to a refuted-route card. The default went back off after about 3 minutes live.
- Names mode on the same 493: 4 first cards changed. 2 were better (the Azuma-Hoeffding card for "Azuma Hoeffding inequality ...", the Kemeny maximum), 1 was a twin swap, and 1 was worse: for "Safran Eldan Shamir ...", the theorem card went from 1st to 2nd behind our T330 addendum. Run 3 then got 14 of 30, under its bar of 15, with 2 worse in the found arm.

The lesson for the next test: title-built control arms could not show the harm, because a title already holds every word the extra wording adds. Real wordings did. Run a real-wording arm before any switch to default on.

How to apply: ask a two-name result with the hyphen, or put the hyphenated form in an --or wording (the 30 Oct advice still holds). MATH_RECALL_JOIN=names is a safe opt-in when you type names spaced. Code: brain-framework ee6ba260defa. Scripts: join_ab_2026_11_08.py, join_ab2_2026_11_08.py, join_ab3_names_2026_11_08.py and their .out files; join_real_queries*.py and join_real_changes_2026_11_08.py.

Related: [[math_recall_misses_hyphenated_names_asked_with_a_space_2026_10_30]], [[math_recall_hyphen_compound_miss_ab_7_2_off_2026_11_03]], [[math_recall_title_minus_paren_tail_first_2026_11_08]].

