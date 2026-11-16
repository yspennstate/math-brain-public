---
name: fei_record_gate_no_single_truth_table_swap_beats_6_5218_gpu_2026_11_12
description: "[VERIFIED] FEI record gate 6.5218 (Numaro, 18 vars): does any single truth-table swap beat it? No, all 1.7e10 balance-keeping swaps checked on the worker machine GPUs (MLX), best -2.56e-4, 18x flatter than coin moves; two WHTs per row; two-swap beam ranks 1-10 + Mac rows also 0 hits (float32 undo reads above, float64 rejects)"
metadata:
  type: project
  created: 2026-11-12
  created_at: 2026-11-12T14:42:18+02:00
  status: verified
  evidence: "worker machine 1+2 ~/gpu_work/fei_swap sweep_0.log sweep_1.log DONE lines; code brain main 2e74af8b"
---

Is Numaro's 18-variable FEI record gate (PM(K33) host, nine coin sites, H/(I-1) = 6.521845710923047, I = 261/128) a local maximum when any two truth-table entries are swapped, not just when the coin layout moves? Yes for one swap: measured 12 Nov 2026 on the worker machine GPUs.

- Every balance-keeping swap f(x) <-> f(y) with f(y) = -f(x): 2^17 x 2^17 = 1.72e10 swaps, x over the +1 entries split 0:65536 on worker machine 1 and 65536:131072 on worker machine 2. No swap beats the record (no float64-checked hit). Best 6.5215902328 (-2.56e-4), reached by two mirror-image pairs, (590, 1102) and (133411, 291).
- The record is much flatter in truth-table space than in coin-layout space: the nearest coin move was -4.73e-3 (fei_numaro_k33_layout_strict_local_max_and_hot_anneal_scar_2026_11_06), the nearest single swap is 18 times closer. That is why a two-swap beam is worth running.
- Method: for a fixed x, with fh the normalised spectrum and s = 2 f(x)/N, fh'(S) = a_S + s chi_S(y), a_S = fh(S) - s chi_S(x). Then H over all y is sum_S (p_S + m_S)/2 + WHT[(p_S - m_S)/2](y), p_S = phi(a_S + s), m_S = phi(a_S - s), phi(v) = -v^2 log2 v^2, and I over all y is sum_S |S|(a_S^2 + s^2) + 2 s WHT[|S| a_S](y). Two length-2^18 transforms per x give the whole row: the full neighbourhood took 4 min on worker machine 2 (260 x/s) and 7 min on worker machine 1 (170 x/s) in MLX float32. GPU and float64 CPU agree to 5e-7 on checked pairs; anything within 2e-4 of the base is re-scored in float64.
- The same trick scores all single swaps of ANY Boolean gate in O(N^2 log N / 2) instead of O(N^3 log N): use it for other record candidates.
- GPU setup: neither Mac had a GPU library before 12 Nov 14:3x (no torch, no MLX), so every FEI search there ran on the CPU. MLX now in ~/gpu_venv on both (worker machine 1 0.32.4 on Python 3.13, worker machine 2 0.29.3 on Python 3.9). MLX on the GPU is float32 only.

Code: brain main 2e74af8b, 06_math_research/frontier/fei_gpu_swap_agent/ (swap_sweep.py, beam.sh, export_record.py). Runs: ~/gpu_work/fei_swap on both Macs. Next: ranked top-200 first swaps, then the two-swap beam (ranks 1-60 on the Macs, 61-200 offered to an agent on the workstation RTX).

What would change this: a two-swap or three-swap move above the record, or a different host on 9 variables.


Two-swap beam, 12 Nov 15:00-18:00: no two-swap move beats the record either, on every first swap tried so far. For each first swap the whole second-swap row is scored on the GPU (float32), and the top distinct values are re-checked in float64.
- Ranks 1-10 of the distinct first-swap list (workstation RTX, an agent; rank 1 is the pair (590, 1102)), three extra first swaps (brain e82e7e75), and seven beam_d rows on the Macs (worker machine 1: 130851/128291, 262097/216697, 131669/127972; worker machine 2: 261999/182055, 262095/182055, 262095/198265 and more running): 0 float64 hits above 6.521845710923047.
- The best second swap is always the undo of the first, which puts the record back. The float32 GPU value of the undo prints as 6.521845817566, above the record; that is float32 rounding, and the float64 re-check rejects it. Never report a float32 GPU maximum near the record as a hit.
- Re-check bug, found by an agent: swap_sweep.py first re-checked the first 50 near-record partners by index, not the 50 best. The control (the undo at (1102, 590) must come back at 6.521845710923047) failed until the re-check sorted by value. Every beam result above uses the sorted re-check.
- Rank the first swaps by distinct value: the mirror symmetry of the gate gives each score at two (x, y) pairs, so a plain top-k list spends half its budget on repeats.
- Running: a depth-3 beam on the RTX (an agent; ranks 1-10, drop the undo, keep the top 5 second swaps, full third-swap sweep from each; done around 18:50), and beam_d rows on both Macs to rank 32.

Related: [[fei_numaro_k33_layout_strict_local_max_and_hot_anneal_scar_2026_11_06]] (the coin-layout neighbourhood, 18x steeper).
