---
name: headless_arm_crash_gate_session2_on_rc0_and_handoff_2026_11_11
description: "[VERIFIED] Grand-hunt arm score looks like a brain failure after a network drop? Session 1 died before its handoff and the launcher ran session 2 anyway; gate s2 on rc=0 + handoff file, resume crashed sessions in their own sid"
metadata:
  type: feedback
  created: 2026-11-11
  created_at: 2026-11-11T16:30:42+02:00
  status: provisional
  evidence: ""
---

On 11 Nov 11:09 laptop time the network dropped for a few minutes (claude -p died with "Can't reach the API server", ENOTFOUND). Three headless Opus arms of the seed-28 grand hunt died with it: the brain arm's session 1 had just opened station 19 but had not filed its handoff memory, the launcher then started session 2 anyway and it ran with no handoff (0 answered rows), and the bare arm's session 2 died after replaying stations 1-18.

The launcher (pilot_old_A.sh) chained session 2 after session 1 with no check, so a crashed session 1 silently became a "brain arm with nothing to carry" and its score looked like a brain failure.

Fix and rule:
- Session 2 starts only if session 1's claude.log ends in rc=0 AND the handoff memory file exists (grand_hunt_handoff_<hunt>_A.md, or the lower-case _a.md that brain.py remember may write). Otherwise the launcher exits 7/8 and prints the --resume command.
- A crashed headless session is resumed in its own session id (claude -p --resume <sid>) with a short "network dropped, carry on" prompt, never restarted cold (owner rule). The brain arm's session 1 was resumed only to file the handoff; session 2 was rerun fresh from a pristine copy. The bare arm's session 2 was resumed mid-run.
- Keep the dead attempt's files (s2_neterr/, score_neterr.json, transcript_neterr.jsonl) so the outage is visible in the record.
- Comparison caveat: a resumed session 2 is not the same treatment as a fresh one. Say which arm was resumed when you report brain vs bare.

Check before trusting any arm score: the last line of each claude.log is rc=0, and the session has a REPORT.json. An rc=1 line with an ENOTFOUND in claude.err means the run is invalid, not a result.

Scripts: scratchpad resume_A28.sh, resume_C28.sh (session an agent); launcher gate in pilot_old_A.sh lines 39-42.

