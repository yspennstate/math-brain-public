---
name: title_search_by_stem_not_phrase_possessive_missed_steins_method_2026_11_11
description: "Math-store title search for a duplicate came back 0? Search the stem ('stein', 'coherent shea'), not the phrase: 'stein method' missed Stein's method (181-link hub) and E45 landed a duplicate; merged as claim_14553327bf"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T09:47:03+02:00
  status: verified
  evidence: "math-brain-build/local/ct_e431: e45b_titles.out ('stein method 0'), e45_recall.out (hub claim_9cb7346473 rank 2), e45c_titles.out ('stein''s 51'), steinmerge_land.out (node 1/1, edges 185/185), sm_full.out and sm2.out (ranks after the merge); pushed in merge 0e6b8ea1"
  lesson: true
---

A title search that drops a possessive or searches the singular misses the card it was meant to find. On 11 Nov the E45 search
looked for "stein method" (the apostrophe was dropped to keep a single-quoted sed working) and for "coherent sheaf"; neither is a
substring of "Stein's method" or "coherent sheaves". Both returned 0, and E45 landed a Stein's method card next to the store's hub
card "Stein's method" (claim_9cb7346473, 181 links, a one-line body). The coherent sheaves gap was real; the Stein gap was not.

How to apply: before writing a card, search the shortest distinctive stem ("stein", "coherent shea", "planar map", "tiling"),
not the phrase, and read every hit whose title starts with the name. To keep an apostrophe inside a sed program, close and
reopen the quote: 'stein'"'"'s'. Recall, run right after landing, caught it: the new card ranked under the old hub.

The fix was a reviewed merge (ct_steinmerge.py, made from ct_adjmerge.py): one card titled "Stein's method", claim_14553327bf,
superseding both, with the fuller statement and all 183 live links copied. Measured after the merge: a long query in the card's
own words puts it first (score 73 against 46), but the bare query "Stein's method" no longer shows it in the top 8 (the short
"Technique: Stein's Method" card leads); the long body costs it rank on two-word queries. Not yet fixed. What would change it: a
title carrying the aliases, as the Technique cards do, measured on the same two queries before and after.


**Second instance, same day (11 Nov 10:1x):** E47 landed a duplicate decomposition-theorem card although the stem search FOUND the old one (claim_c121dc215a): the listing line held 5 matches and `cut -c1-230` hid the fifth. Read every match of a title search (one per line, never a width-cut joined line), and treat a count larger than the titles you can see as unread. Merged by ct_decompmerge.py into claim_a099854a7f1f708ead89f7c1d1069081.

Correction (11 Nov 10:3x): the second instance was not the 230-character cut. e41_titles.py printed only the four shortest titles of each stem, each cut to 44 characters, so the longer decomposition-theorem title never reached the screen. The listing tool is now titles_all.py in math-brain-build/local/ct_e431: it prints every non-arXiv match on its own line (up to 15) and counts the arXiv-like ones it leaves out. Read every line before writing a card.
