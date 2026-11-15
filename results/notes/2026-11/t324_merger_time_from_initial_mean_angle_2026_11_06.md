---
name: t324_merger_time_from_initial_mean_angle_2026_11_06
description: "T324 two-cluster merger time (SA attention on the circle): from the actual initial cluster-mean angle the reduced ODE gives it to 0.3 pct; the collapse shifts each mean by -beta mu3/6"
metadata:
  type: project
  created: 2026-11-06
  created_at: 2026-11-06T02:56:58+02:00
  status: provisional
  evidence: ""
---

T324 Target 1 asks about metastable clustering under normalized self-attention (Q=K=V=I) on S^1, with two clusters. Measured 6 Nov 2026 02:4x by an agent. Files are in 06_math_research/frontier/rows/T324: merge_check3.py, merge_check4.py, their _out.txt files, and the DOSSIER section of that date.

**The earlier reading was wrong.** The 16 Oct check 2 found that the merger time T_full drifts away from the reduced point-mass ODE's passage time: the ratio ran 0.92-1.14 at beta 4-20 unless the ODE was restarted after the collapse. It explained this as the fast phase moving each cluster mean by about w0/sqrt(n). In fact the drift came from measuring the angle from the nominal cluster centres. Uniform draws on [c-w0, c+w0] put the actual circular means about w0/sqrt(3 n_k) away from c. Measured from the actual initial angle D_0, T_full/T_red(D_0) is 0.997-1.0006 in all 16 runs, and it moves toward 1 as beta grows.

**What the collapse itself does is small, with a closed form.** One cluster's mean moves by -beta mu3(0)/6, where mu3 is the third central moment of the offsets.
- The shift comes from the order-beta d^2 term of the softmax weights, with the collapse v ~ e^(-t). The beta-free cubic terms cancel by antisymmetry.
- Checked sample by sample: the ratio of measured to predicted shift is 0.993-0.998 at beta w0^2 = 0.02 and 0.91-0.97 at 0.32. The formula fails past beta w0^2 ~ 1.

**Method lessons.**
1. Measure a coupled angle from the configuration that was actually drawn, not from the design parameter.
2. After the collapse the cluster widths reach 1e-16, and the n-token system is then exactly the point-mass system. So a five-digit match after that point says nothing about the slow phase. What Target 1 actually claims is decided in the O(1) collapse window.

**Target 1, restated:** T_merge = T_red(D_0)(1+o(1)) provided beta^2 mu3 -> 0 and beta w0^2 -> 0.

**What would change this:** a merger time that misses T_red(D_0) by more than beta sin(D_0) times the mu3 shift at small beta w0^2. Untested: K >= 3, random initial data, d > 2.

Related: [[t242_resnet_rank_one_blocks_match_m4_only_d_over_ml_2026_11_06]] carries the same lesson: measure the noise floor before reading a gap.


**K = 3 (6 Nov 03:2x).** The K-point-mass reduced ODE from the actual initial means matches the token merger time to 0.1-0.4 pct (16 runs). The closest pair's own clock is enough only when cos dAB - cos dAC is large against 1/beta; otherwise it misses by 10-29 pct, and the third cluster always SLOWS the merger (it pulls A away from B). First-order size: (1/2) sin dAC exp(-beta(cos D0 - cos dAC)) / (2 sin D0 + sin dAC/2), measured/formula 0.94-0.99 at beta 32. Lesson from the first try: the denominator first carried sin dAC and read 1.16-1.19 high - the receding of A from C while it closes on B halves that term. Files merge_k3*.py in the row.

**Unequal masses, both sides (6 Nov 03:2x).** A cluster C beside A adds (mC/mA) sin dAC exp(-beta(cos D0 - cos dAC)) / (k (2 sin D0 + pA sin dAC)) with k = mB/mA + mA/mB and pA = mB^2/(mA^2+mB^2), the share of the closure A covers; a cluster beside B adds the mirror term; they add. Checked in 8 cases to 0.97-0.98 at beta 32 (merge_k4.py); the equal-mass form at unequal masses is 1.5-2.2x off.
