---
name: paper_audit_fable_limit_spent_run_reader_on_opus_2026_11_16
description: "[VERIFIED] Every paper_audit run ends rc 1 with no report in about 20 s? The Fable weekly limit is spent (session.json: 429 usage_limit_reached, resets 22 Nov 06:00 local time). Swap the reader model without editing the shared script: import paper_audit as P; P.MODEL='claude-opus-5-5'; P.run(tex)."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T16:01:04+02:00
  status: provisional
  evidence: ""
---

16 Nov 2026 15:4x-16:00 (an agent). paper_audit.py pins MODEL=claude-fable-5-2. From about 15:40 every run ended rc 1, no REPORT.md, session.json result 'You have hit your Fable limit, resets Nov 22, 6am', api_error_status 429. A retry loop every 10 min cannot succeed until 22 Nov. Fix used: a three-line wrapper that imports paper_audit, sets P.MODEL='claude-opus-5-5' and calls P.run(<tex>); run() reads the global at call time, so the swap takes. The reader is still a fresh headless session that did not write the paper, with the same prompt, caps (2 in flight, 6 GB free) and AUTHOR_RESPONSE.md hand-on; audit_index.json records the served model. Both Opus runs were still reading 45 s in, past the 18 s at which the Fable runs died. Check before relying on it: the served field of the index row should name claude-opus-5-5. The wrapper is a scratch file, not a change to the shared script.
