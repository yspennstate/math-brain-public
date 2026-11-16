---
name: freezing_live_sidecar_digest_stops_long_brain_tests_audit2_2026_11_09
description: "Does freezing the live sidecar.sqlite digest work for a long brain test? No: any memory write rewrites it; AUDIT2 stopped at 53/72 (+391 links); pin a copy instead"
metadata:
  type: project
  created: 2026-11-09
  created_at: 2026-11-09T03:34:57+04:00
  status: verified
  evidence: "workers/AUDIT2-BUILD/evidence/amendment_01_sidecar_drift.json; harness/audit_freeze.py line 30"
---

No. A test harness that freezes the sha256 of the live sidecar.sqlite stops any run that outlives the next memory write, because the file is rewritten whenever any agent files a memory.

AUDIT2's scored run (Codex, 9 Nov) stopped after 53 of 72 attempts at 03:3x on "External graph generation drift". Links had gone from 243,298 at the freeze to 243,689 (+391, 0.16%). AUDIT1 used the same harness and got through only because it finished before a write.

Fix used: amendment 01 (evidence/amendment_01_sidecar_drift.json in workers/AUDIT2-BUILD). The sidecar moved from the strict external check to a recorded-not-enforced entry; the graph store manifest and release stay strict. The old freeze is kept as FREEZE.pre_amend01.json, and a 30 s digest log covers the resumed attempts. Analysis plan addition: report the score on all items and, as a sensitivity check, on the 26 items whose two attempts both finished before the change.

For the next harness: pin a copy (sqlite .backup to a frozen path, BRAIN_GRAPH_SIDECAR=<copy>, allowed in the sandbox policy) at freeze time, and digest the copy, not the live file.

Related: [[audit1_script_audit_brain_ties_bare_2026_11_09]]
