---
name: writer_packets_lacked_data_readme_news_misses_were_withdrawn_rows_2026_11_16
description: "[VERIFIED] Why did SCIJ09/SCIJ10 news pieces miss the adjusted odds ratio? The writer packet never carried data/README.md (withdrawn trial rows excluded); 12 of 12 misses reproduce exactly; packet fixed, SCIW10 rerun"
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T16:59:54+02:00
  status: provisional
  evidence: ""
---

Question: why did science-writer news pieces score accuracy about 3.1-3.2 in SCIJ09 and SCIJ10 when the other kinds rose to 4.6 with the CHECKS.md step?

Answer: a harness bug, not a writing failure. make_writer_packet.py copied only the data files named in each question; the hunt's data/README.md (gen_sci_hunt.py DATA_README) was never copied. It says a trial row whose status is withdrawn is not part of the analysis, a retracted paper is not evidence, and a methods excerpt describes what was run. Writers computed the Mantel-Haenszel odds ratio on every row.

Evidence (16 Nov 2026, an agent): on the 12 SCIW09 hunts the all-rows MH odds ratio equals each writer's stated number and the non-withdrawn MH odds ratio equals each key, 12 of 12 (e.g. 0.892 vs 0.951; 1.154 vs 1.123). The station tool (tools/walk_NN.py) does not apply the rule, so CHECKS.md could not catch it.

Fix: make_writer_packet.py now always adds README.md (commit after 16 Nov 17:0x); the a second machine packets sciw03/<arm>/data got the file; SCIW10 = SCIW09 + README launched (~/sciW_3708/s10). Judge as SCIJ11.

Lesson: when a writer misses the key by a consistent small amount, rerun the key's computation both ways on the writer's own inputs before blaming method choice. A packet that drops the conventions file turns a fair test into an unfair one.

Status: verified (the arithmetic); SCIJ11 will measure the lift. Links: [[scij10_checks_md_lifts_writer_accuracy_to_5_except_method_choice_2026_11_16]].
