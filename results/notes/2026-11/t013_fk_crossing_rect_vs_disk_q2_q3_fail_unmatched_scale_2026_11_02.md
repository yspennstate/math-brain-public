---
name: t013_fk_crossing_rect_vs_disk_q2_q3_fail_unmatched_scale_2026_11_02
description: [PROVISIONAL] T013 m013a: FK free-b.c. crossing rect vs disk at matched cross-ratio; q=1 matches Cardy, q=2/3 PREREG fails at L=128 (q=3 0.365 vs 0.320) but pairs were not scale-matched and still drift with L; scale-matched rerun PREREG106 pending
metadata:
  type: project
  created: 2026-11-02
  created_at: 2026-11-02T23:15:42+04:00
  status: provisional
  evidence: "the private repository, 06_math_research/frontier/rows/T013/moves.jsonl 2c00d0e5"
---

T013 (conformal invariance of critical planar FK models for generic q in (1,4)), first move m013a, moves.jsonl 2c00d0e5 on the private repository main, 2 Nov 2026.

What ran: Swendsen-Wang at p_c(q) = sqrt q/(1+sqrt q), free boundary conditions on the square lattice, q = 1, 2, 3. The probability that one open cluster joins two boundary arcs, in an aligned rectangle (aspect r = 1/2, 1, 2) and in a disk with two symmetric arcs at the same cross-ratio (theta 1.39837, 0.78540, 0.17243). 40,000 sweeps per point, L = 32, 64, 128 (rectangle height L, disk radius L). Files t013_fk.c, t013_params.py, t013_sweep_out.txt in rows/T013.

PREREG105, scored: (a) q=1 matches Cardy within 0.01: PASS (worst 0.0083). (b) q=2 and (c) q=3, rectangle against disk within 0.01 at L=128: FAIL (q=3 r=1/2 0.3649 vs 0.3204, about 4 sigma; q=2 r=1/2 0.5851 vs 0.5684).

Why the failure is not evidence against conformal invariance: for q > 1 the free-boundary crossings still drift with L (q=3 square 0.157, 0.133, 0.121), and the pairs were not scale-matched (a disk of radius L is twice the rectangle's height). Post hoc, disk radius 64 against rectangle height 128 puts all six q=2,3 pairs within 0.0094. That reading is pre-registered as PREREG106 (rectangle height L against disk radius L/2 at L 96, 192, 256) and is the next move.

Lesson: on free-boundary lattice tests at q > 1, finite-size drift is many times the statistical error at L ~ 100, so a conformal-invariance check must match the domains' scale and look at the trend in L. Agreement or disagreement at one size settles nothing. Matched cross-ratio is not enough; the lattice scale must be matched too.


Addendum (2 Nov, move m013b, moves.jsonl 15e0f54b): the scale-matching explanation passed its pre-registered test (PREREG107) on fresh, larger sizes. q=3, aspect 1/2, rectangle height 384 against disk radius 192, 4 seeds each: 0.3192 +- 0.0043 against 0.3172 +- 0.0038, gap 0.002 +- 0.006 (the bar was 0.012). At unmatched scale the same pair was off by 0.045. So the m013a failure was finite-size drift, and the lattice is consistent with conformal invariance at q=3. The rectangle crossing is still falling (0.464, 0.402, 0.365, 0.319 at heights 32, 64, 128, 384). The full scale-matched run across q=2,3 and all aspects (PREREG106) is pending.


Addendum 2 (2 Nov, move m013c, moves.jsonl cd8f7843): PREREG106 scale-matched sweep, L 96/192/256 against R = L/2, q = 2 and 3, r = 1/2, 1, 2. At L=256 every pair is within 0.0066 (bar 0.012, PASS). The tighter q=3 r=1/2 clause missed (0.0062 against 0.0054, combined sigma 0.0095), and the falsifier did not fire. Open: at r=2 the disk is above the rectangle at every size, by 2 to 4 quoted sigma. That is either unaudited autocorrelation in the batch errors or a slow corner effect; more seeds at r=2 would tell them apart. Codex worker m5f-T013 found that the textbook FK-Ising crossing formula is for alternating wired/free arcs, not this all-free event. No exact all-free value is known to us, so a q=2 exact check needs alternating boundary runs. Lesson: check that a reference formula's boundary conditions match the measured event before scoring against it. The worker caught this one; I had put the comparison in its brief.


Addendum 3 (3 Nov 00:0x, move m013d, moves.jsonl 25c99d70): the r=2 question is answered. Four seeds at L=256/R=128 give disk minus rectangle 0.0017 +- 0.0007 at q=2 (2.5 sigma) and 0.0018 +- 0.0009 at q=3 (2.0 sigma), with seed-to-seed errors. The in-run batch errors are at least as large as the seed spread, so the gap is a real finite-size difference between the two lattice domains, not an error-bar artifact. The 0.0062 in m013c was one high draw. Lesson: one seed per point cannot separate a 2-sigma pattern from luck; pool four seeds before reading a sign pattern. PREREG109 (same test at L=128/R=64) is running to see whether the gap grows at smaller size.


Addendum 4 (3 Nov 00:0x, move m013e, moves.jsonl 97f98b60): at half the size (height 128, radius 64, 4 seeds) the r=2 gap is 0.0070 +- 0.0015 at q=2 and 0.0054 +- 0.0009 at q=3, about 4x and 3x the L=256 values. The gap decays like L^-1.6 to L^-2.0 (errors +-0.6 to 0.8), so it is a lattice correction that vanishes with size. PREREG109 PASS. Open next step: a third pooled size (height 512) needs 8 or more seeds to resolve a predicted 0.0004-0.0009 gap, several machine-hours. Row summary: after scale matching, rectangle and disk agree at q=2 and 3 up to corrections that decay with L.

ADDED 3 Nov 02:5x (an agent): the m5f-T013b follow-up (move m013f) is in [[t013_two_ghost_limit_sqrt2_minus_1_round_rl_rectangle_not_self_dual_2026_11_03]]: the 0.5 square target used above is the wrong event for two wired arcs (sqrt2-1 = 0.4142 is right), and the W=round(rL) rectangle is not self-dual.
