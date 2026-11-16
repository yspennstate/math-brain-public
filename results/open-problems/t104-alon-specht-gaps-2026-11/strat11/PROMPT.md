# STRAT11: close the corner (r,a)=(1,1) of T104 5+1 region (11), N=6

Context files in this folder: STRAT9/ (RESULT.md, its region (11) definition and replay scripts) and STRAT10/
(RESULT.md, cubic_moment_certificate.json, pressure_family.json, residual_map.json, exact_samples.json, LOG.md).
Read STRAT9/RESULT.md section (11) and STRAT10/RESULT.md first.

What STRAT10 found: on region (11), T > 0 at every sampled point, but the explicit family
U=(-4,1+s,1+s,1-s,1-s), W=(0,1,-1,-1,1), r=1, a=(5+s^2)/(5+10s-s^2) has T6 -> 0+ as s -> 0, so the residual
touches T=0 at the corner point P0 (s=0, r=a=1). Box splitting cannot close a region whose infimum is 0.

Task, in order:
1. Write T near P0 in local coordinates (s, the radial scale 1-r, 1-a, and the transverse directions allowed by the
   region's filters). Compute the exact first-order (linear) part L of T at P0 on the tangent cone C of region (11)
   at P0 (the cone cut out by the active filters and admissibility constraints at P0).
2. Prove L >= c * dist(., P0) on C with an explicit rational c > 0, by an exact LP / Farkas certificate
   (rational multipliers, replay in exact arithmetic). If L vanishes on some direction of C, go to second order on
   that face and certify the quadratic form is positive definite there (exact rational LDL or SOS).
3. Bound the remainder: give an explicit rational radius rho and a rational bound on the second (or third) derivative
   over the ball B(P0, rho) intersected with region (11), so that T >= (c/2) dist > 0 on that ball minus P0
   (T(P0)=0 is the boundary point, not in the open region). Interval arithmetic with rational endpoints is fine.
4. Cover region (11) minus B(P0, rho) with the STRAT9/STRAT10 box machinery (reuse their scripts); the margin away
   from P0 is positive by the sampling, so boxes should close it. Report the count of boxes and any leaf left OPEN.
5. If step 2 fails (some tangent direction has L < 0), that direction is a candidate for T < 0: follow it, find an
   exact rational point in region (11) with T < 0 if one exists, and report it as a COUNTEREXAMPLE with replay.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. Exact rational arithmetic
(SymPy Rational / fractions) for every certificate; no floating tolerance in a PROVED replay. Save as you go:
append to LOG.md after each step, keep RESULT.md current. Write replay_all.py that reruns every PROVED claim.
Do not edit STRAT9/ or STRAT10/. Normal speed only.
