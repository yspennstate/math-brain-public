---
name: row_file_already_merged_dedupe_by_samples_before_adding_2026_11_16
description: "[VERIFIED] About to add a worker's row file to an aggregate (skewness table, pooled stats)? Dedupe by the sample values first: P0108's a second machine n=2048 file (162 rows) was already merged verbatim into fpp_rows_mac1_collapse.jsonl; adding it again would have counted 2700 samples twice and moved n=2048 c=0.5 skew to -0.106 (se 0.022) from the true -0.116 (0.025)."
metadata:
  type: project
  created: 2026-11-16
  created_at: 2026-11-16T18:26:32+02:00
  status: provisional
  evidence: ""
---

On 16 Nov the public P0108 collapse table used n=2048 rows that existed only on the Macs. Two files were fetched: a second machine's fpp_rows_mac1_collapse_n2048.jsonl and a second machine's fpp_rows_mac2_collapse_n2048.jsonl. The first try pooled both with the public files and the table did not reproduce. A row-level check (key = n, c, tuple(T)) showed all 162 a second machine rows were already present, line for line, in the public fpp_rows_mac1_collapse.jsonl (the runner had appended the batch there), while the 368 a second machine rows (seed 11219) were new. Only the a second machine file was added. Rule: before pooling a row file, key every row by its sample values and count how many already exist in the pooled set; a seed or filename is not enough, since the same batch can sit under two names. Also check that the published table reproduces from the public files alone before changing it. Related: [[bootstrap_over_compacted_rows_splices_across_cut_months_2026_11_16]].
