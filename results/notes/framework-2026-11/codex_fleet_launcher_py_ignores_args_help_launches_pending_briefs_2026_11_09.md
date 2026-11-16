---
name: codex_fleet_launcher_py_ignores_args_help_launches_pending_briefs_2026_11_09
description: "[VERIFIED] No: launcher.py in codex_fleet/20261108_pro ignores its arguments, so --help launches every pending brief; read the source instead"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T13:21:12+04:00
  status: verified
  evidence: "FSYM48 launched by launcher.py --help, 9 Nov ~10:35"
---

Does `launcher.py --help` in ~/codex_fleet/20261108_pro print usage? No (9 Nov 2026 ~10:35, an agent): the launcher ignores its arguments, so `--help` launched every pending brief (here FSYM48, which was meant to launch anyway).

How to apply: never pass a flag to launcher.py to learn what it does; read its source (head -40) instead, and only run it when every brief in briefs/ without a worker folder is meant to start.

