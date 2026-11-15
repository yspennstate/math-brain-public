---
name: math_store_title_search_misses_en_dash_titles_2026_11_11
description: "Math store title search for a duplicate missed a card? Hyphen search misses en-dash titles (Curry–Howard); normalize dashes and accents before landing; dash_dupes.py"
metadata:
  type: project
  created: 2026-11-11
  created_at: 2026-11-11T05:58:08+02:00
  status: verified
  evidence: "E31 recall: Curry-Howard-Lambek claim_ce0b70ed rank 2 behind claim_c80f567f 'Curry–Howard correspondence'; dash_dupes.out; 183 dash titles counted 11 Nov"
---

A title search with `lower(title) like '%curry-howard%'` misses a card titled "Curry–Howard correspondence": the en dash (U+2013) is a different character from the ASCII hyphen, and SQLite's lower() and LIKE do not fold it. On 11 Nov the E31 card writer searched the hyphen form, found nothing, and landed "Curry-Howard-Lambek correspondence" (claim_ce0b70ed) next to an existing Wikipedia-extract card claim_c80f567f. Recall ranked the old card first and the new one second. The two were linked (E31b, semantic_association plus depends_on Proof theory) rather than merged, because the new card adds the Lambek side.

Scale: 183 live claim titles contain an en or em dash (11 Nov 05:4x); accented names (Kähler, Néron, Martin-Löf) have the same problem with an ASCII search word.

How to apply: before landing a concept card, search titles with dashes normalized (replace – and — by -) and with the accented spelling as well as the ASCII one. math-brain-build/local/ct_e431/dash_dupes.py does the dash check for a batch's id files (it compares every consecutive name pair, so "Curry-Howard-Lambek" catches "Curry–Howard"); accent_check.out shows the accented query. A second guard is the recall check after landing: a new card at rank 2 behind a near-identical title is the sign.

Also learned: the builder's add_claim_batch refuses an empty batch, so a links-only batch now goes through store.add_edge (ct_e431/_tail.py, 11 Nov).

