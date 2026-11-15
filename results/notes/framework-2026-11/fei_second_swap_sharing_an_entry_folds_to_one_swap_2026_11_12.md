---
name: fei_second_swap_sharing_an_entry_folds_to_one_swap_2026_11_12
description: "[VERIFIED] FEI depth-3 beam: second swaps that share an entry with the first swap fold into ONE swap from the record (flip a,b then b,c = flip a,c); exclude x1,y1 before picking starts"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T16:08:36+02:00
  status: provisional
  evidence: ""
---

On 12 Nov 15:51-16:05 the depth-3 beam's phase 1 (second-swap --distinct list from each of the ten best first swaps of the 6.5218457 record numaro18) kept 5 rows per rank, and every kept row shared an index with the first swap: rank 1 (130851,128291) kept 261411/130851, 128291/259875, 65315/130851 ... with float64 value 6.521589511961663, exactly rank 1's own one-swap value. In a balanced +-1 table a swap flips two entries of opposite sign; flipping a,b and then b,c flips a and c only, so the 'two-swap' state is the one-swap state (a,c). Fifty third-swap sweeps from those starts would have repeated the depth-2 beam (about 2.5 GPU hours). Fix: swap_torch.py sweep --exclude i,j masks every candidate touching those entries (column mask to -1e9 and x filter); phase 1 uses --exclude x1,y1 --distinct 16, keeps the top 5 distinct float64 values. Control: a 2000-x slice of rank 1 with --exclude gave 6 rows, 0 touching 130851 or 128291. Same trap for any k-swap beam: a step must be disjoint from all earlier steps, or it is a shallower state. Code: 06_math_research/frontier/fei_gpu_swap_agent/swap_torch.py. Related [[fei_record_gate_no_single_truth_table_swap_beats_6_5218_gpu_2026_11_12]], [[gpu_swap_sweep_recheck_capped_by_index_hid_hits_2026_11_12]].
