---
name: math_transport_scan_cuts_slugs_and_dash_i_hides_numpy_2026_11_14
description: "[VERIFIED] ingest-many refused slugs from math_transport scan? scan prints names cut at 64 chars; resolve the full file name first. ModuleNotFoundError numpy? you ran python -I, which hides user site-packages"
metadata:
  type: project
  created: 2026-11-14
  created_at: 2026-11-14T18:57:51+02:00
  status: provisional
  evidence: ""
---

math_transport.py scan prints each waiting memory's slug cut to 64 characters. Feeding those lines to ingest-many refused 3 of 9 on 14 Nov (no such memory); the full names had to be resolved from the memory folder (ls <prefix>*) before they went in. The six short ones went in at 18:3x, the three resolved ones at 18:42 (claims de9dbf83, b9619160, 63170067), store total then 416.

Second trap the same hour: python -I hides user site-packages, and numpy lives there on this workstation, so math_transport status and math_claim_vecs died with ModuleNotFoundError. The -I advice is for code that reads downloaded files; our own brain tools run without it.

Third, from the same evening: codex_local_1108/run_one.py gave a brief two network retries, and WBAB3_J4 (blind judge) used both and stopped at 18:33 with no line saying it had given up. It now retries RUN_ONE_NET_RETRIES times (default 4), waiting 3, 6, 9, 12 min, and writes 'gave up after N network retries' when it stops. Status: verified by the log lines; the retry change is untested until the next drop.

Related: [[a_card_that_drops_input_must_name_it_2026_11_14]] (a tool that drops input must say so: the scan cut names silently, the runner stopped silently) and [[retry_reads_the_status_not_the_work_2026_07_15]].
