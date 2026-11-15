---
name: paper_audit_dies_in_seven_seconds_on_the_fable_limit_2026_11_12
description: "W43 paper audit came back with no REPORT.md? On 12 Nov the Fable limit (429 model_requires_usage_credits) killed every paper_audit run in 7 s; read session.json, don't relaunch or switch model, owner emailed, retry after 17 Nov 01:00"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T12:19:04+02:00
  status: verified
  evidence: "audits/reports/2026/11/12/paper_audit_*/session.json (4 runs)"
  lesson: true
---

paper_audit.py (W43 independent reader) is pinned to claude-fable-5-2 (MODEL constant, line 37), and on 12 Nov 2026 the Fable usage limit was reached. Every audit launched from about 10:00 to 12:15 that day died after one turn in about 7 s with no REPORT.md: paper 7 (p7build), paper 21, fei-one-coordinate and trace-ants dead_branches. Its session.json reads is_error true, api_error_status 429, api_error "model_requires_usage_credits", result "You've reached your Fable limit".

How to tell: the audit folder under audits/reports/<date>/paper_audit_<slug>/ has PROMPT.md, an empty session.err and a session.json, but no REPORT.md. paper_audit.py status shows rc1 with no report. Read session.json before you relaunch.

What not to do: relaunching does nothing until the limit resets. Do not switch MODEL to another model: the request names a Fable 5.2 auditor. Buying usage credits is the owner's decision, and the choice went to him by email. Its default is to run the audits again after 17 Nov 01:00. A paper waiting on W43 stays unposted until then, unless he answers.

Who it holds up: trace-reinforced-ants-dead-branches (pushed a52b6c0, ResearchGate post waiting), paper 7, paper 8.

What would change this: his answer to that email, or a clean audit run after the reset.

