---
name: mps_torch_randn_tail_fault_2_to_minus_23_redraw_beyond_6_2026_11_15
description: "[VERIFIED] GPU (MPS) Monte Carlo shows rare huge outliers? torch.randn on Apple GPU gives |z|>7 about 2^-23 per draw (max 14.4); redraw |z|>6 before trusting a tail"
metadata:
  type: reference
  created: 2026-11-15
  created_at: 2026-11-15T15:09:58+02:00
  status: verified
  evidence: "T248 Monte Carlo: 23 of 2e8 draws |z|>7; iid control outliers gone after redraw (out_1115b)"
  lesson: true
---

On an M-series Mac mini, `torch.randn` on the Apple GPU (MPS, float32) returns |z| > 7 about once in 2^23 draws.
That is 23 values in 2e8 draws, the largest |z| = 14.37; a true Gaussian gives about 2.6e-12 per draw.
A Monte Carlo built on it gets fake outliers.
In the T248 iid control (Hermite-2 entries, N=500), λ_max came out near 43 in 1.5 pct of samples and near 22 in 5.9 pct at N=1000.
The bulk of the same run matched a float64 CPU run, median 1.44 against 1.30.
A random-matrix edge statistic sits right on the tail, so a single bad entry moves it by tens of TW units.

**Why:** most likely the float32 uniform reaching its smallest grid value inside the Box-Muller step (not confirmed in the source).
The fault test is `mps_randn_tail.py`.

**How to apply:** any MPS Monte Carlo whose statistic reads the tail (extreme eigenvalues, maxima, rare events) redraws every |z| > 6.
The helper is `randn()` in `tw_rcck_mc.py`; the true probability of |z| > 6 is about 2e-9 per draw.
Or draw on the CPU and copy over.
Test the generator's tail (count |z| > 6 in 1e8 draws, expect 0.2) before trusting a heavy tail from GPU samples.

Rerun with the fix (job 41_agent_t248_tw_mc_fixrng): the iid N=500 control has mean 1.50 and q95 4.5, with no wild values.
The network N=500 mean is 4.43, unchanged, because its excess is the weight-side edge shift of Remark 7.1 in the T248 paper.
The T248 paper is posted as Zenodo 10.5281/zenodo.24246777.

