# STRAT12: close the 13,368 OPEN leaves of T104 5+1 region (11), N=6, by constrained Bernstein certificates

Context in this folder:
- STRAT10/ (cover_face.py with ROOT, necessary(), polynomials(); zero_face.py; the box cover and its verify scripts).
- STRAT11/ (RESULT.md, replay_all.py, remaining_open_boxes.json = the 13,368 OPEN leaves after STRAT11's corner ball).
- diag_all.json + open_box_diag.py: a NUMERICAL triage (20,000 samples per box, float version of necessary()
  without the scale ceiling). Read STRAT11/RESULT.md and STRAT10/RESULT.md first.

What the triage says (NUMERICAL, cross-checked in exact rationals at the ten worst points):
- 8,122 open boxes have NO feasible sample: they look empty, but the existing interval tests do not exclude them.
- 5,246 open boxes have feasible samples; the N=6 numerator (polynomials()[0]) is positive at every one, and the worst
  relative margin min T/(det*t^3) is 23.6 (1% quantile 62.8). Zero negative samples. So the cover is not stopped by
  T going near 0; it is stopped by bounding T over the WHOLE box, including the box's infeasible part.

Task, in order:
1. For each open box B, with the feasibility constraints g_k >= 0 of cover_face.necessary() (orientation, order, rows,
   edges g_ij, spectral, rank, ratio 529*Delta - 60*tau^2 > 0, the scale ceiling; polynomials in the 6 coordinates
   (t, v1, z1, v2, z2, z)), solve a small LP:
   (a) EXCLUSION: find rational lambda_k >= 0 with  sum_k lambda_k g_k  having every Bernstein coefficient on B
       strictly negative (so no point of B is feasible).
   (b) POSITIVITY: otherwise find rational lambda_k >= 0 (products g_k*g_l allowed if needed) with
       T - sum_k lambda_k g_k  having every Bernstein coefficient on B strictly positive (so T > 0 on B ∩ feasible).
   Round the LP solution to rationals and verify the Bernstein signs in EXACT arithmetic. If neither LP succeeds,
   split B in half along its widest coordinate and retry, to a depth you choose; report the depth used.
2. Write the certificates to a JSON (box, kind, lambda as rational strings) and a replay script that rechecks every
   one in exact arithmetic with no floating point. Run it and record the time.
3. Report: boxes closed by exclusion, by positivity, after splitting, and any leaf still OPEN, with the open chart
   volume before (3333609/32768) and after. If a leaf has a feasible exact rational point with T <= 0, that is a
   COUNTEREXAMPLE: report it with replay.
4. If everything closes, write replay_all.py that reruns STRAT11's replay plus the new certificates, and state the
   full theorem for region (11) at N=6 with every hypothesis named.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. Exact rational arithmetic
(fractions / SymPy Rational) in every PROVED replay; an LP solver may find candidates in floats but the replay never
trusts them. This Mac is shared with four other runs: use 4 worker processes (multiprocessing; the box set is embarrassingly
parallel), nice 5, and keep peak memory under 3 GB. Save as you go: append to LOG.md after each step, keep RESULT.md current, checkpoint the
certificate JSON every 500 boxes so a restart resumes. Do not edit STRAT10/ or STRAT11/. Normal speed only.
