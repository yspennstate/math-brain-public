---
name: word_walk_links_senses_not_words_drift_fixed_2026_11_14
description: "Word walk drifting into another meaning (soot -> c -> cocaine)? Fixed 14 Nov: lexicon.json has per-sense links 'e' and walk moves on (word, sense) states"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T16:30:46+02:00
  status: verified
  evidence: "commit 1bc1e9ff; 300 rounds x6 offers from soot, seed 7 beta 0.7: drug/soda words 18 -> 1; berth curacy/magistracy -> wharf/mooring/dock"
---

The flat neighbour list in lexicon_v1 joined every sense of a word, so a walk entered a word in one meaning and left in another: soot -> c (carbon symbol) -> cocaine, berth -> office -> curacy. build_lexicon.py (sense_edges) now writes, per word, 'e' = one list per sense of 'word:j' links (same synset, synset relations, sense relations; symmetric, so MH still targets pi) and 'q' = each sense's part of speech; 'n' is unchanged (identical on all 73,530 words), so older readers see the same graph. word_walk.py starts in the seed sense closest to the page (random sense with no page) and leaves a word only through the sense it entered by; sense_of uses the arrival sense. 6,715 of 121,482 senses have no links and keep the walk in place. Measured 300 rounds of six offers, seed 7, beta 0.7, no page: soot drug/soda offers 18 -> 1 (coke as fuel), carbon 5 -> 1, berth curacy/magistracy/deanery -> bunk/wharf/mooring/dock, canvass sails-only -> canvas/poll/survey. Not yet checked: the page command's stand-ins (copper -> centime) with a page context. Related [[word_walk_shows_walked_sense_and_matching_master_line_2026_11_14]] [[writing_brain_dictionary_and_word_walk_2026_11_14]].
