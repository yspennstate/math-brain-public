---
name: prose_surface_measures_catch_2023_ai_not_ours_2026_11_14
description: "[VERIFIED] Can sentence-length/word-rarity statistics tell our prose from human? They catch 2022-23 models (MAGE stories, held-out AUC 0.937 vs gpt-3.5/davinci-003/GLM/LLaMA-65B; sentence-length CV alone 0.856) but our own documentary scripts score P(human) 0.90-0.97 - the tell in our prose sits in content, structure and word-in-context, not surface statistics"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T07:39:44+02:00
  status: provisional
  evidence: ""
---

Measured 14 Nov 2026 by an agent (writing-brain measurement lane), files in 12_cognitive_architecture/writing_brain/maths/.
prose_walk.py reads a text as three walks: sentence lengths, word surprisal against a 941-book shelf unigram (87.7M words), and content-word recurrence. On MAGE WritingPrompts stories of 150+ words (2,849 human; 642 machine from the four strongest models), a numpy logistic fit on even rows scored on odd rows gives AUC 0.937 (0.761 against all 27 models: the stronger the model, the more it regresses to the mean). Best single measures: sentence-length CV 0.856 (human 0.64, machine 0.40), longest/mean sentence 0.807, MATTR 0.741, surprisal sd 0.718, dialogue share 0.698. Machines also re-use names (0.5 vs 0.25) and write longer sentences (15.1 vs 12.5 words).
Then prose_walk.py score on 450-word windows of three of our documentary scripts: 28, 21, 21 windows, median P(human) 0.97, 0.97, 0.90, every window read human. So these measures are a floor: they flag flat prose, they do not certify ours. The tell therefore sits higher: event and idea choice, scene order, the word chosen for this context.
How to apply: use score as a cheap first check on a draft, never as proof it reads human. Work on the higher levels with bridge_plan.py (plot as a Doob h-bridge: tempered steps conditioned to reach the ending in exactly T beats) and context_fit.py (shelf PPMI vectors; a candidate word's cosine to the brief, the fit term for the dictionary word walk). The blind with/without test design is BLIND_TEST.md.
Doubt: the human side is Reddit stories and the machines are 2022-23; the documentaries are nonfiction narration, out of domain for a fit trained on fiction. What would change it: a modern-model fiction set scored the same way.

Related: [[research_writing_human_voice_2026_06_10]] [[method_write_like_a_human_2026_07_07]] [[a_prediction_that_cannot_fail_is_not_evidence_2026_08_04]]
