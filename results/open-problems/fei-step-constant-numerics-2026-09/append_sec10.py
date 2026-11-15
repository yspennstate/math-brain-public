"""append section 10 (the cancellation-keeping region-1 enclosure) to THEOREM_NOTE.md and an entry to PROGRESS.md.
Refuses if the disk copies are not the versions on main (byte sizes), so a truncated note can never be extended.
usage: append_sec10.py <R1X_H96 line> <R3 line> <R2 line> <headline>   (each a short phrase with the measured figures)"""
import os, re, sys, time
F = r"~\brain-repo\06_math_research\fei_step_numerics_2026_09_20"
note = os.path.join(F, "THEOREM_NOTE.md"); prog = os.path.join(F, "PROGRESS.md")
EXPECT = {note: 17192, prog: 10241}   # byte sizes of the copies on origin/main at 14:0x on 2026-09-21
for p, n in EXPECT.items():
    if not os.path.exists(p): sys.exit("missing: %s" % p)
    s = os.path.getsize(p)
    if s != n: sys.exit("refusing: %s is %d bytes, main has %d" % (p, s, n))
if "## 10." in open(note, encoding="utf-8").read(): sys.exit("section 10 already present")
if len(sys.argv) < 5: sys.exit("need four arguments")
R1X, R3, R2, HEAD = sys.argv[1:5]
stamp = time.strftime("%H:%M", time.localtime())[:4] + "x"

SEC10 = """
## 10. The region-1 enclosure that keeps the cancellation (2026-09-21 STAMP)

Section 9 named the cure and it works.  fei_cert_r1x.py bounds Phi on a cell X x Y from below by the larger of two
enclosures, each rigorous in the same outward-rounded float64 arithmetic as before.

(a) The piecewise-linear part P = G_num(x) + G_num(y) - G_num(x+y) is linear on every piece of the subdivision of
    the cell by the lines x + y = node (the x and y sides of a node cell, and of its bisections, lie in one segment
    each), so its minimum is at a vertex of that subdivision: a corner, or a point where such a line meets an edge.
    Those vertices are evaluated with one-ulp interval coordinates, which gives the minimum exactly to rounding
    (against a dense grid: the bound is never above the grid minimum and within 3e-13 of it).
(b) The margin term c(1-p)(1-q) is monotone in each variable, so its minimum is at a corner.
(c) E is enclosed by the smaller of its interval evaluation and the mean-value form E(centre) + rx max|dE/dx| +
    ry max|dE/dy|, with dE/dx = p[8(1-q)(1 - x ln2) + 8qy ln2 + 8(1-q) ln2 - Psi'(pq) q ln2 + Psi'(p) ln2].
(d) The centred form Phi(centre) - rx max|dPhi/dx| - ry max|dPhi/dy|, where dPhi/dx = G_num'(x) - G_num'(x+y)
    + c ln2 p(1-q) - dE/dx with the slope of x's segment (exact) and the range of slopes of the segments met by
    x + y; Phi is Lipschitz, so the mean-value inequality holds with the essential supremum of the derivative.
    This form is second order in the cell width where Phi is flat, which is exactly where the old bound was tight.

Cross-check (crosscheck_r1x.py, cert_vi_h24k40.npz, c = 0.01, 251 random cells of widths h to h/32, 1,993 points at
40 digits): the bound never exceeds the true value; the slack between the sampled minimum and the bound has
median 7.7e-6 and maximum 1.8e-2, against a median of 0.10 and a maximum of 0.41 for the decoupled bound on the
same cells.  With the margin set to c = -0.2 (a way for the check to fail) every one of the 247 cells whose sampled
Phi is negative is flagged and none is bounded above its true value; that control also caught a real error, the
corner minimum of the margin term had been taken at (x0, y0), which is right only for c > 0.

Runs (BelowNormal, one core each):
    region 1, M = 24, c = 0.01     VERIFIED in 557 s: 1.62M node cells, 1.70M cells evaluated, deepest level 6
                                   (the decoupled bound needed 32.7M cells at its widest level and 951 s)
    region 1, M = 96, c = 0.003    R1X_H96
    region 3, M = 96, c = 0.003    R3_LINE
    region 2, M = 96, c = 0.003    R2_LINE
HEADLINE
"""
PROG = """
## 2026-09-21 STAMP - region-1 enclosure rebuilt to keep the cancellation
- fei_cert_r1x.py (exact piecewise-linear minimum over the cell's subdivision vertices, corner minimum of the margin term,
  mean-value E, centred form of Phi) and crosscheck_r1x.py (40-digit soundness, dense-grid tightness of the PL part, and a
  negative-margin control that must and does fail): CROSSCHECK PASS; the control found the c > 0 assumption in the margin
  term, fixed to a corner minimum.  Median slack 7.7e-6 against 0.10 for the decoupled bound.
- M = 24, c = 0.01: region 1 verified in 557 s at deepest level 6 (the old bound: 951 s, deepest level 13).
- M = 96, c = 0.003: R1X_H96; region 3: R3_LINE; region 2: R2_LINE.
- HEADLINE
"""
SEC10 = SEC10.replace("STAMP", stamp).replace("R1X_H96", R1X).replace("R3_LINE", R3).replace("R2_LINE", R2).replace("HEADLINE", HEAD)
PROG = PROG.replace("STAMP", stamp).replace("R1X_H96", R1X).replace("R3_LINE", R3).replace("R2_LINE", R2).replace("HEADLINE", HEAD)
open(note, "a", encoding="utf-8", newline="\n").write(SEC10)
open(prog, "a", encoding="utf-8", newline="\n").write(PROG)
print("appended section 10 (%d bytes) and the progress entry (%d bytes)" % (len(SEC10.encode()), len(PROG.encode())))
