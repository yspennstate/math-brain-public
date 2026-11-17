---
name: parallel_audit_waiters_race_and_launch_nine_at_once_2026_11_17
description: "[VERIFIED] Several papers to audit? Separate wait_audit waiters race: 9 Opus audits started at 00:32 17 Nov, 5 refused yet logged 'launched'. Use one queue process that checks audit_runs.jsonl for start/refused"
metadata:
  type: feedback
  created: 2026-11-17
  created_at: 2026-11-17T00:47:34+02:00
  status: verified
  evidence: "audit_runs.jsonl 17 Nov 00:32: 9 start events within 20 s, 5 refused; waiter logs all said launched"
---

Ten wait_audit.py waiters started a minute apart each read the audit run log, saw fewer than two audits in flight, and launched; audit_opus.py's own two-at-a-time check reads the same log before its start line is written, so it admitted seven of them plus two others. Nine Opus audits ran together on a laptop with 2-4 GB free, and the five that were refused had waiter logs saying "launched", because the waiter printed on Popen, not on the wrapper's start event.

How to apply: queue several audits through one process that launches the next only after the previous one's start line is in audit_runs.jsonl, and retries a refusal (an agent's audit_queue.py does this, with an O_EXCL lock so only one copy runs). Read audit_runs.jsonl for start/refused, never a waiter's own "launched" line. The real fix is a lock inside audit_opus.py around check-and-start; that file is shared, so it belongs to its owner.

