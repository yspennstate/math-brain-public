# T238 review: the quadratic-window second pass, with seed variance (agent C, 4 Nov 2026)

The check scripts and their outputs named below are in audit_C/.

Source: the second pass in this folder: NOTE_quadratic_window.md, window.py, win_*.txt, win2_*.txt. No conflict: I wrote
none of it.

What I ran. The source's window.py, byte for byte (window.py (the source's file), sha256 5928267cec99e2a2...), on more
seeds at the second pass's grid: seeds 3-8 at d = 8, 12, 16 and seeds 3, 4 at d = 24 (20 runs), all at n = d^2/4 and
c = 1e-3, 1e-2, 0.1 (t238_runs/w_<d>_<seed>.txt). Pooled with the source's eleven runs by t238_tab.py ->
t238_tab.json. Every run is normalised the way the second pass says: share(c) = dist_to_lazy(c) / lazy test
error. Local CPU only, about 20 minutes.

## Numbers (29 runs: 11 from the source, 18 here)

Share of the gap left at c (mean, sd over seeds; k seeds):

| c | d = 8 (k 8) | d = 12 (k 8) | d = 16 (k 8) | d = 24 (k 4) | d = 32 (k 1) |
|---|---|---|---|---|---|
| 1e-3 | 0.59, 0.35 | 0.76, 0.15 | 0.83, 0.08 | 0.87, 0.02 | 0.91 |
| 1e-2 | 0.31, 0.22 | 0.43, 0.19 | 0.47, 0.11 | 0.50, 0.04 | 0.58 |
| 0.1 | 0.03, 0.03 | 0.06, 0.06 | 0.04, 0.02 | 0.04, 0.01 | 0.05 |

OLS of share on log2 d over individual runs, per doubling of d: +0.18 (se 0.065) at c = 1e-3, +0.13 (0.052) at 1e-2,
+0.003 (0.013) at 0.1. Without d = 8: +0.11 (0.053), +0.08 (0.069), -0.02 (0.021).
Median test error at c = 1e-3: 0.015, 0.011, 0.0064, 0.0028, 0.0013 for d = 8, 12, 16, 24, 32 (Spearman with d over
the runs -0.39, p 0.04).

## Verdict, claim by claim

1. The correction itself (seed spread included, the first pass's "rich end moving down with d" withdrawn): ACCEPT.
   With eight seeds the first pass's falling share (d = 8 s1 0.92, d = 16 s1 0.71) is seed luck; the seed mean goes
   the other way.

2. "The window is fixed in c over d = 8 to 32": REVISE. The lazy edge is fixed: at c = 0.1 the share is 0.03-0.06 at
   every d with a flat slope. The rich side is not shown to be fixed. The mean share at fixed small c rises with d,
   2.7 and 2.4 standard errors on the full pool. Part of that is d = 8; without it the slope is 2.1 se at c = 1e-3
   and 1.2 at 1e-2. So the data lean towards the rich side moving (towards larger c, the opposite of the first
   pass's reading) but do not establish it. The d = 24 and 32 cells have 4 and 1 seeds, which is where a moving
   edge would show.

3. "Seed spread is as large as any trend": REVISE. True at d = 8 and 12. The spread shrinks fast with d (sd at
   c = 1e-3: 0.35, 0.15, 0.08, 0.02 for d = 8, 12, 16, 24) and by d = 16 it is smaller than the d = 8 to 32 change in the mean.

4. "Rich by 1e-3": REVISE. At d = 8, three of eight seeds are not rich at c = 1e-3 (shares 0.54, 0.10, 0.01). Seeds 4
   and 5 never recover the teacher at any c tried (test 0.46 and 1.09 at c = 1e-3, against lazy 0.80 and 1.10).
   At n = 16 = 2d the small-initialisation flow does not always find the rank-one teacher. The share then reads
   "lazy" for a reason that has nothing to do with c. This, and not a window shift, is most of the d = 8 effect
   in point 2.

5. "The rich side gets better with d" (0.044, 0.006, 0.002-0.003, 0.001): conclusion ACCEPT in the median, quoted
   support REVISE. The quoted values are seed 2 at d = 8 and 16. Seed 1 at d = 8 has 0.0009, better than both d = 16
   seeds (0.0214, 0.0055). The medians over all seeds fall monotonically (rank correlation -0.39, p 0.04 over 29 runs).

6. Minor. (a) The second-pass table mixes normalisations: its d = 8 s1, d = 12 and d = 16 s1 entries are divided by
   the c = 1e-6 distance (first pass), the rest by the lazy test error (d = 16 s1 at 1e-3: 0.71 against 0.69 under
   the stated rule). (b) Six c = 1e-3 runs (two of the source's, four of mine) stop at the 4e5-step cap with train MSE 1e-10 to 5e-9 instead of
   1e-10, and every first-pass run at c <= 1e-4 is capped (train up to 3e-7). The test errors those runs report are
   small and the shares would not change at the printed precision, but the README's "trained to 1e-10" is not true
   of them.

Scoped numerical verdict: in the quadratic surrogate at n = d^2/4 the lazy edge sits at c of order 0.1 at every
d = 8-32, robust across seeds. Whether the rich edge moves with d is open on this data, and the d = 8 runs are
confounded by recovery failure at n = 2d. More seeds at d = 32 and a d = 48 point, five seeds each,, at c = 1e-4 and 1e-3, is
the one experiment that settles it.

## The missing theoretical bridge to the catalog row

The row asks about a two-layer ReLU network (the 30 Oct note: ReLU student, He2 + He1 teacher,
both layers trained, fixed time t = 50). This experiment is a different model, and nothing in the package connects
the two. What a bridge would need:
- A reduction from ReLU to the matrix flow. The +- pair quadratic student is exactly x^T (P - Q) x with a closed
  matrix ODE. A ReLU student has no finite-dimensional closed form. One would need to show that the ReLU's degree-2
  Hermite part drives the dynamics for a He2 teacher, and control the He1 and higher parts. The catalog teacher has a
  He1 term that the quadratic student cannot represent.
- The hypentropy bias when the G(t) do not commute (the README says it is proved only in the commuting case).
- Finite width (here m = infinity) and other n/d^2 (here 1/4 only).
- The same stopping rule: train-to-convergence here, fixed function-space time in the ReLU note.
- A derived map between this c = alpha/d and the ReLU note's alpha (window 10-100, crossover 30-38). Neither note
  derives one.

The original row stays OPEN. No novelty certification and no change to the solved count.

## Addendum 4 Nov 15:4x: five more seeds at the large-d end (34 runs)

The extra job (t238_runs/run_extra_1104b.sh, same window.py, same grid) added seeds 5 and 6 at d = 24 and seeds 2, 3 and
4 at d = 32, so those cells now have k = 6 and k = 4. t238_tab.json re-run 15:4x.

| c | d = 24 (k 6) | d = 32 (k 4) |
|---|---|---|
| 1e-3 | 0.88, 0.02 | 0.91, 0.01 |
| 1e-2 | 0.51, 0.04 | 0.60, 0.04 |
| 0.1 | 0.04, 0.01 | 0.06, 0.02 |

Slope of share on log2 d over all 34 runs: +0.162 (se 0.048) at c = 1e-3, +0.133 (0.038) at 1e-2, +0.006 (0.009) at
0.1. Without d = 8: +0.108 (0.035), +0.108 (0.047), -0.006 (0.014). Median test error at c = 1e-3 for d = 24 and 32 is
0.0022 and 0.0012; Spearman with d -0.46, p 0.006.

What this changes in verdict 2: the lazy edge stays fixed (c = 0.1 flat at every d). The rich side now moves with d at
3.1 standard errors at c = 1e-3 and 2.3 at 1e-2 even with d = 8 left out, and the large-d cells are tight (sd 0.01-0.04),
so it is no longer a few-seed effect. The second pass's "window fixed in c over d = 8 to 32" should read: the lazy edge
is fixed in c = alpha/d; at fixed small c the run ends nearer the rich (min-nuclear) solution as d grows, so the rich
edge drifts to larger c. Caveat: nine runs stopped at the step cap with train loss between 1e-10 and 5e-9, all four
d = 32 runs at c = 1e-3 among them (2.9e-10 to 1.1e-9). Those runs are close to converged but not at the source's
1e-10 target; a longer cap at d = 32, c = 1e-3 is the one check that could still move the d = 32 cell.

The row stays OPEN; no change to the solved count.
