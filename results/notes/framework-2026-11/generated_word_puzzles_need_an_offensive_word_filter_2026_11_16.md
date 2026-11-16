---
name: generated_word_puzzles_need_an_offensive_word_filter_2026_11_16
description: "[VERIFIED] Built crossword/cryptic hunts from the writing-brain lexicon: did slurs get in? Yes - fix is a gloss filter + build gate"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T00:33:25+02:00
  status: provisional
  evidence: ""
---

status: verified

The science scavenger hunts (scihunt_2026_11_15, gen_sci_hunt.py) drew crossword answers, definitions and cryptic fodder from writing_brain_data/dictionary/lexicon_v1/lexicon.json with only a length and frequency filter. That lexicon is WordNet-like and keeps slurs as ordinary entries. Found 16 Nov 00:0x when xword_forcing reported 43 empty cells: the clue was a hidden-word clue built on a racial slur, and a scan of the 37 built hunts plus the SCI01/SCI02 pilot found slurs as answers or fodder in about 28 of them (several racial and ethnic slurs and one ableist slur).

Fix (pushed b029fdea): clean_word() drops any lexicon word one of whose senses is glossed offensive / slur / pejorative / derogatory / disparaging / vulgar / obscene / insulting / contemptuous (369 words), plus an explicit list for slurs the dictionary leaves unmarked; build_100.py refuses a hunt whose player files carry a listed word. The first-version hunts were withdrawn and are never published. The 43 empty cells were also a checker bug: a play can read as both hidden and anagram, and check_hunt.wordplay now pools both readings.

How to apply: any generator that draws words from a dictionary (puzzles, test items, filler text, names) filters on the glosses before the first build, and the build itself greps its output for a block list. A frequency floor does not remove slurs; they are common words in old books.
What would change it: a lexicon with a register field would make the gloss regex unnecessary.
