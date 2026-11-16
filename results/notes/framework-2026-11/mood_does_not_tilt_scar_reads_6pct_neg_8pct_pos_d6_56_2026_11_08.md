---
name: mood_does_not_tilt_scar_reads_6pct_neg_8pct_pos_d6_56_2026_11_08
description: "[VERIFIED] No (8 Nov): D6 #56 mood-congruent recall has no premise; in a negative text mood agents read scars 9 of 143 times vs 12 of 146 in a positive one (429 reads), and no recall path reads mood"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T07:41:50+04:00
  status: verified
  evidence: "d6_56_mood_vs_scar_reads_2026_11_08.py over 24 Mac sessions"
---

Should a cautious or negative mood make recall surface scars first, as 1000-ways D6 #56 (mood-congruent recall tilt) asks? No premise for it on the Mac. No recall path reads mood today (brain.py, spread, fok_probe and instinct_prime never mention it). When the agent's own text mood runs negative, it does not reach for scars any more than usual. Measured 8 Nov by an agent.

Mood is computed as in [[d6_97_agent_mood_adds_0p4pt_to_next_error_last_error_8x_no_mood_block_2026_11_08]] (salience FEAR/JOY hits, mean over the last 5 scored text blocks). A read is a Read of a memory file or brain.py node <slug>, and it counts as a scar when the description says Scar. 429 reads with a mood in the Mac transcripts (24 sessions; a 40-day window finds the same ones), 337 distinct memories:
- negative third: 9 of 143 scars (0.063 +- 0.020), 17 feedback
- middle third: 11 of 140 (0.079 +- 0.023), 13 feedback
- positive third: 12 of 146 (0.082 +- 0.023), 19 feedback

Flat within noise, if anything fewer scars when negative. And mood barely predicts the next error (1.2x in D6 #97, against 8.7x for the last call failing, which is already wired), so a mood-driven tilt would have no target. Nothing built. Size of doubt: reads by grep or cat of a memory are not counted, and 429 reads is small.

Check: d6_56_mood_vs_scar_reads_2026_11_08.py [days], read only. Control: a planted "Scar:" description is labelled a scar, a plain one is not.

