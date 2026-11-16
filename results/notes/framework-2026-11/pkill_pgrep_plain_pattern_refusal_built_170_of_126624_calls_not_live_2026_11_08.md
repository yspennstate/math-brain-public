---
name: pkill_pgrep_plain_pattern_refusal_built_170_of_126624_calls_not_live_2026_11_08
description: "[VERIFIED] Would refusing plain pkill -f and pgrep -f waiters cost much on the second machine? No: the built candidate (W112 d) refuses 170 of 126,624 Bash calls in 14 days, 12 of 14 sampled right; other sessions' zsh -c shells carry their text, so plain patterns hit them. Not live"
metadata:
  type: project
  created: 2026-11-08
  created_at: 2026-11-08T06:08:02+04:00
  status: verified
  evidence: "d_pkill_cross_2026_11_08.py controls 16/16; d_pkill_replay_2026_11_08.py on 25 Oct-8 Nov transcripts, catches the 6 Nov waiter"
---

Would a refusal of plain `pkill -f` and plain `pgrep -f` waiters cost much on the second machine? No: replayed on 126,624 Mac Bash calls from 25 Oct to 8 Nov, the built candidate would refuse 170 (0.13%, about 15 a day across 20 sessions), and 12 of 14 sampled refusals are the real shape. It is built and measured, not live. Measured 8 Nov 2026 by an agent; W112 (d), from the REM 2026-10-14 gate question.

Why it is a hazard here. macOS pgrep and pkill skip their own ancestors, so a command never matches itself (3 Nov probe, [[a_waiter_loop_that_pgreps_its_target_matches_its_own_command_line_2026_10_20]]). But the Bash tool runs every call as `/bin/zsh -c "source <snapshot> ... eval '<command>'"`, so every OTHER live call carries its whole text in argv. A plain `pgrep -fl "sleep 1"` run shortly before 06:08 on 8 Nov listed another session's background waiter (it held "sleep 120"). So `pkill -f PAT` also kills any other agent's shell whose command holds PAT, and two waiters on one pattern keep each other alive ([[two_pgrep_waiters_on_one_pattern_keep_each_other_alive_mac_2026_11_04]]; MISTAKES 6 Nov 22:52).

The candidate, d_pkill_cross_2026_11_08.py (`_pkill_cross`, for danger_mode.py behind PKILL_GUARD). It refuses `pkill -f PAT`, `kill $(pgrep -f PAT)` or `pgrep -f PAT | xargs kill`, and `until/while [!] pgrep -f PAT`, all only when PAT is plain. It allows a bracketed character ([m]id_leak.py), a pattern anchored with ^ (wrapper lines start '/bin/zsh -c source'), any other pgrep -f (it only prints), plain pkill without -f, and the shape inside a quoted message or grep pattern. Controls: 6 refuse and 10 allow cases, 0 wrong (one bug, a -9 flag not read as a flag, fixed before the replay).

Replay, d_pkill_replay_2026_11_08.py (output d_pkill_replay_s1108.out in the same folder): 170 refusals, 79 pkill and 91 pgrep; it catches the 6 Nov mid_leak waiter (control). Per day 1 to 36. Of 14 sampled, 12 are plain pkill -f, kill $(pgrep -f) or pgrep waiters as described; 2 are doubtful: the shape inside a heredoc that writes a script, and inside a python -c string whose quotes the span finder misread. Each refusal costs one retry with a bracket in the pattern.

How to apply: until it is live, bracket one character of every pattern you pkill -f or wait on (pkill -f '[m]id_leak.py'), or wait on a pid with kill -0. Making it live is a danger_mode change and waits on his word, like the other W112 items.

Related: [[reflex_recurrence_after_compile_6_of_91_none_since_21oct_2026_11_08]] (where this candidate came from), [[pkill_selfmatch_family_kill_and_launch_never_share_a_shell]].

