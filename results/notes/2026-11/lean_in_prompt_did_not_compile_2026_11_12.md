---
name: lean_in_prompt_did_not_compile_2026_11_12
description: "Deploying Lean hooks to a dontAsk math test arm without checking compiles"
metadata:
  type: feedback
  created: 2026-11-12
  created_at: 2026-11-12T16:44:10+02:00
  status: provisional
  evidence: ""
  lesson: true
---

What happened: Input lines 127, 134 and 215-216 question why the Lean route did not help and ask for a fallback. The verified 4 October hard300 streams show 4 compiles on 2 of 300 problems, 61 permission refusals and 29 admission holds. At 21:22 only 2.4 GB commit headroom was available against a 3 GB floor.

Why it happened: Multiline quoted source with a newline followed by # was refused in dontAsk; other calls were correctly held by the memory gate. Naming the tool did not make it executable.

**Why:** A configured route was mistaken for an available route.

**How to apply:** Verify one-line Lean execution in the actual harness, count each failure cause, and use permitted recall/reasoning fallback without bypassing memory gates.

[[the_math_brain_lean_route_did_not_run_in_the_hard_test_2026_10_04]] [[owner_order_math_brain_uses_lean_and_tests_go_proof_heavy_2026_10_05]]

Drafted by Codex worker W19 of the 12 Nov 04:43 order (H20_1112), screened and filed by an agent. Provisional: the worker read the source, nobody re-measured it.

