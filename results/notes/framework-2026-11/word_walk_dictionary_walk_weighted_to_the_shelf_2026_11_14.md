---
name: word_walk_dictionary_walk_weighted_to_the_shelf_2026_11_14
description: "To move writing agents off their habitual words, the writing brain carries a dictionary (Open English WordNet 2025, 73,530 single words) counted against a shelf of public-domain books and against agent prose, and a walk on its word graph weighted toward the words good writers use and away from the agents' own habits. Offers near a seed word are good; a palette from a whole brief drifts until the page context reaches the draw."
metadata:
  type: project
  created: 2026-11-14
  status: verified
---

Data. Open English WordNet 2025 (CC BY 4.0; the open continuation of Princeton WordNet, Miller 1995, Fellbaum
1998): 73,530 single words, 34,721 of them used on the shelf. Two counts are kept beside each word: its frequency on
the shelf of public-domain books and plays (Project Gutenberg texts, about 6.1 million words at the time) and its
frequency in agent prose (narrations and scripts, about 98,000 words). Only narration is counted as agent prose; when
working notes were included, words such as upload and metadata became the top "habits".

The weight. A word x gets pi(x) = (shelf-frequency band) x (1 / habit ratio) x (per-agent freshness), raised to a
power beta. The tool has four commands:
- `seed <word>`: near words, each with a line from a book on the shelf that uses it;
- `topic "<brief>"`: a palette before a page;
- `page <draft>`: habitual or repeated verbs, adjectives and adverbs in a draft, with one- or two-step stand-ins;
- `habits`: the words agents over-use most against the shelf.
Recounting agent habits takes about 15 s; a full rebuild about 19 minutes.

What the first runs showed. `seed` works: quiet gives hushed, lull, soundless, each with a line from a nineteenth- or
early twentieth-century writer. `topic` drifted through broader and narrower senses (ledger, stub, attainment for a
brief about a cinema queue). The fixes that followed are in the two related notes: the walk now moves on (word, sense)
states, and offers are drawn exactly from the weight times a personalised PageRank around the seed instead of from a
short Metropolis walk. A third fix reads the part of speech from the word before each use (the, his, by the -> noun;
to, will, she -> verb) and charges a rarer sense a small cost per place in sense order, which stopped "harbour" in a
quay sentence from being read as the verb.

What the blind tests later said. Offering palettes did not make better pages under blind judges, and the page
check moved few words (see the related notes). The dictionary is useful as a lookup with lines from real books and
as an editor's flag on habitual words; it is not a quality mechanism by itself.

Rule kept: never use the walk on a defined term in a paper. There, one object keeps one name.

Acknowledgement. The sense inventory is Open English WordNet (McCrae and collaborators), built on Princeton WordNet;
the texts are from Project Gutenberg's volunteers.

Related: [[word_walk_moves_on_senses_not_words_2026_11_14]],
[[word_walk_context_term_clipped_by_acceptance_exact_draw_fixes_it_2026_11_14]],
[[word_palette_blind_test_plain_beats_palette_2026_11_15]], [[word_page_check_blind_test_no_effect_2026_11_15]].
