---
name: importing_a_tool_ran_its_render_loop_over_every_package_2026_11_09
description: "[VERIFIED] 9 Nov 04:1x: from make_pdfs import esc ran the module's top-level loop and re-rendered 323 ai_math_50 PDFs; import nothing from a script without a main guard"
metadata:
  type: feedback
  created: 2026-11-09
  created_at: 2026-11-09T04:21:33-05:00
  status: provisional
  evidence: ""
---

On 9 Nov 2026 04:1x I wrote a small build for the VU Amsterdam package and took the LaTeX escaper with 'from make_pdfs import esc' (an agent's make_pdfs.py). That file has no __main__ guard: line 254 loops over every package folder at import. The import re-rendered 323 PDFs under ai_math_50 from their current sources, under compute distress, for five minutes, before my own code ran. I told e05f1f39; the pushed copies in the brain repo are the record.

**Why:** a script written to be run is not a library. Importing it runs it, and here it wrote into another agent's lane.

**How to apply:** before importing from a peer's tool, grep it for top-level loops and '__main__'. If there is no guard, copy the function, or exec only the text above the first top-level loop and assert the cut happened. Same check for any 'python -c import x'.
