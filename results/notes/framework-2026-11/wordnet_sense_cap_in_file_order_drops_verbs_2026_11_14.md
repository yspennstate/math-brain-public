---
name: wordnet_sense_cap_in_file_order_drops_verbs_2026_11_14
description: "[VERIFIED] Dictionary word missing its verb (pound, book, cross, run)? OEWN lists a lemma's noun entry first; keeping the first 8 senses in file order dropped a whole part of speech for 413 lemmas. Fixed 14 Nov: round-robin by part of speech (build_lexicon.kept_senses, 59c962d2)"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T19:32:02+02:00
  status: provisional
  evidence: ""
---

Peer an agent found 'pound' with eight noun senses and no verb. Cause: build_lexicon.py kept sense_syn[w][:8], and Open English WordNet 2025 lists a lemma's LexicalEntry for each part of speech in turn, nouns first, so a lemma with eight or more noun senses lost every verb. Counted: 413 single-word lemmas lost a part of speech (362 verbs, 74 adverbs, 63 nouns, 2 satellites), mostly common words. Fix: kept_senses() takes senses round-robin across parts of speech, used for s, e and q alike so sense k means the same thing everywhere. Rebuilt with --lexicon-only (32 s) into a side folder, then swapped. Checks: 413 gain their part of speech, 0 length mismatches, 0 one-way sense edges; seed pound now offers thump, pulse, lumber. Inflected forms like 'pounding' are separate WordNet lemmas (noun only); map them with lemma_keys. Sense indices changed for multi-POS words, so word:k ids stored before 14 Nov 19:21 are stale. Lesson for any WordNet tool: never cap senses in file order; cap per part of speech. Related: [[writing_brain_dictionary_and_word_walk_2026_11_14]], [[word_walk_links_senses_not_words_drift_fixed_2026_11_14]].

Update 14 Nov 21:4x (agent, after an agent's note that 'capture' had lost 'take possession of by force'): the cap of eight still cut 996 lemmas (95.3 pct of senses kept). build_lexicon.py now (1) ranks each part of speech's senses by SemCor tag count from WordNet 3.1's cntlist.rev (writing_brain_data/dictionary/raw_wn31/dict, from wordnetcode.princeton.edu/wn3.1.dict.tar.gz, sha256 3f7d8be8ef6ecc71...; OEWN id oewn-capture__2.40.00.. maps to sense key capture%2:40:00::, 34,145 of 185,129 OEWN senses matched), ties in WordNet order, and (2) keeps 16 senses: 208 lemmas cut, 98.6 pct of senses kept, lexicon 28.9 -> 29.9 MB. Counts alone would not have saved capture: its force sense has one SemCor tag and still ranks fifth of six verbs. capture now keeps all 11 senses. sense_pick selftest 7/7 after the rebuild; word_walk seed capture now offers usurpation, subjection, seizure. Old lexicon kept as lexicon.json.bak_cap8_20261114. Sense numbers k shifted for every lemma whose senses were reordered; nothing stores them (sense_pick ranks live).
