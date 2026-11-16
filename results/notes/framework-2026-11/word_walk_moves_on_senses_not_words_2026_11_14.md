---
name: word_walk_moves_on_senses_not_words_2026_11_14
description: "A walk on a dictionary's flat neighbour lists drifts from one meaning to another (soot -> c -> cocaine), and the gloss it prints can name a different sense from the example line beside it. Two fixes: neighbour links are kept per sense, so the walk leaves a word only through the sense it entered by; and the example line is chosen by the six words either side of the target, scored against the offered sense minus the best other sense. Drug and soda offers from soot fell from 18 to 1 in 300 rounds."
metadata:
  type: project
  created: 2026-11-14
  status: verified
---

The fault. WordNet's flat neighbour list for a word joins every sense of it, so a walk could enter a word in one
meaning and leave in another: soot -> c (the carbon symbol) -> cocaine; berth -> office -> curacy. Separately, the
tool printed sense 0 of each word and a random example line. WordNet lists senses in file order, not by frequency of
use, so gloss and line often disagreed: bunk glossed as a feeding trough beside a line about bunks on a ship; canvass
glossed as a narrative setting beside a line about sails.

Fix 1, sense states. The lexicon builder now writes, for each word, one list of links per sense (same synset, synset
relations, sense relations), each entry naming the target word and its sense, plus each sense's part of speech. The
links are symmetric, so a Metropolis-Hastings walk on them still has the intended stationary law. The walk starts in
the seed sense closest to the page (a random sense when there is no page) and leaves a word only through the sense
it arrived by. The old flat list is kept unchanged, so older readers see the same graph. 6,715 of 121,482 senses have
no links and hold the walk in place.

Measured over 300 rounds of six offers (fixed seed, beta 0.7, no page context): from soot, drug and soda words 18 -> 1
(coke as fuel remains), carbon 5 -> 1; from berth, curacy, magistracy and deanery were replaced by bunk, wharf,
mooring and dock; from canvass, sails-only offers became canvas, poll and survey.

Fix 2, the example line. Each offer remembers the word it stepped from; its sense is the one sharing a synset with
that word, otherwise the gloss closest to the page by shelf word vectors. Each candidate line is scored on a window
of six words either side of the target: cosine to the offered sense minus the best other sense. A word whose best
margin is below zero is dropped rather than shown with a wrong line. Scoring the whole sentence was worse (it passed
a line about a setter dog under the typesetter sense). On ten cases judged by hand: right on crock, setter (dropped),
bunk, berth and canvass; wrong on smut (dropped, though an early twentieth-century novelist uses it to mean soot) and
cylinder (a churn line under the piston sense).

Limits. Ten hand cases are few; a set of fifty or more, or a sense-tagged corpus such as SemCor (Miller et al. 1993),
would settle the line rule.

How to apply: any walk or neighbour search on a dictionary should move on (word, sense) states, never on words; and a
gloss shown beside an example should be checked against the example's local window, not the sentence.

Related: [[word_walk_dictionary_walk_weighted_to_the_shelf_2026_11_14]],
[[same_synset_offers_keep_meaning_word_slot_draws_from_them_2026_11_15]].
