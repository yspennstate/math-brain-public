---
name: lean_worker_parks_24h_on_a_limit_message_with_no_reset_time_2026_11_10
description: "[PROVISIONAL] Codex picture workers started before an account's reset parked to tomorrow 19:07? A limit message with no reset time parks lean_worker 24 h; read 'resuming at' in lean_workers.log, relaunch after limits.log's reset"
metadata:
  type: project
  created: 2026-11-10
  created_at: 2026-11-10T19:11:15+02:00
  status: provisional
  evidence: ""
---

Starting lean_worker.py picture workers before an account's reset can park them for a whole day. On 10 Nov 19:07 I started two workers each on acc4, acc5 and acc2 (all at their 24 h limit). acc4's limit message named its reset, so its workers parked to 01:38:39 as intended. acc5 and acc2 got a limit message with no time in it, and lean_worker parked them for 24 hours (to 11 Nov 19:07), which would have missed their 01:38 / 01:47 resets by most of a day. Nothing in the process list shows it; only the log's "parked: Codex usage limit, resuming at <time>" line does.

How to apply: after launching picture workers on a limited account, read logs/lean_workers.log for the "resuming at" time of every worker; a time 24 h out means the message carried no reset time. Stop those workers (your own, by PID) and relaunch after the reset named in _codex_img/pace/limits.log, or with a one-shot scheduled task (wscript //B, built with -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries, or it never starts on battery). Example: alexander_real45/launch_r45_codex.vbs takes the accounts as arguments; task R45agent_1111_0150.

