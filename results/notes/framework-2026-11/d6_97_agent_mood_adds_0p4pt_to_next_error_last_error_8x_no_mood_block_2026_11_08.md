---
name: d6_97_agent_mood_adds_0p4pt_to_next_error_last_error_8x_no_mood_block_2026_11_08
description: "[VERIFIED] No: the agent's text mood (salience FEAR/JOY) predicts its next tool error only 1.2x (2.5% vs 2.1%, within-session +0.33pt); the last call failing is 8.7x and already wired; D6 mood block not built"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T04:01:22+04:00
  status: verified
  evidence: "24 Mac sessions, 152,905 tool calls, 14 d; d6_97_mood_vs_next_error.py, 8 Nov"
---

1000-ways D6 #97 (mood volatility predicts error) and #57 (a core-affect state producer) share one premise: the agent's own mood, read from its text, tells you something about the next mistake. The rest of the D6 mood block (#58 verify bar by mood, #69, #72, #79, #81, #82, #92, #94) needs that same signal. Measured by an agent, 8 Nov 2026, 04:01.

Instrument: d6_97_mood_vs_next_error.py (32 s). It reads the second machine main-session transcripts of the last 14 days (24 sessions, 27,546 assistant text blocks with a FEAR or JOY hit from salience.py's lexicons, 152,905 tool calls). Each block's valence is (joy - fear) / (joy + fear). Mood is the mean of the last 5 blocks, volatility their spread. A call fails when its tool_result has is_error.

- The last call's outcome dominates. After a failed call the next fails 19.9% of the time; after a good one, 2.3%. That is 8.7x.
- Mood after a good call: low third 2.5% (2.4-2.7), high third 2.1% (1.9-2.2). The gap is real but small, about 1.2x.
- After a failed call mood adds nothing: 20.1% against 20.0%.
- Volatility after a good call: low third 2.1%, middle and high 2.4-2.5%.
- Within sessions (same global cuts, sessions with 200+ calls in both thirds), low mood is worse in 12 sessions and better in 7, weighted gap +0.33 points. High volatility is worse in 15 and better in 6, gap +0.35 points. So the pooled gap is not a between-session artefact. It stays a fraction of a point.

Verdict: no build for the mood block. A mood-raised verify bar would act on about a third of calls at a 1.1-1.2x higher base rate, while the 8.7x signal, the last call failing, is already live as the post-error slowing note. Related: [[next_prompt_corrects_2x_after_correction_affect_adds_none_d6_76_2026_11_08]] found the same on the author's side: his frustrated wording adds nothing beyond whether he is correcting. And [[d10_14_distress_no_more_errors_per_call_0p018_vs_0p020_no_jumpier_gut_2026_11_08]] found the body's distress adds nothing either.

**Why:** an affect layer looks like depth, but in this brain the error signal it would proxy is already directly observable.
**How to apply:** before building a state that predicts mistakes, test it against the last call's outcome on the same calls. If it cannot beat that, or add to it, it is decoration.
