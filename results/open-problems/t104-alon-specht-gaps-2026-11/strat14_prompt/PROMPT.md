# STRAT14: close T104 connected n = 5, D = 2 (the STRAT8 residual) with the method that closed 5+1 region (11) at N = 6

Context in this folder:
- STRAT8/ : the n = 5, D = 2 connected residual. Read STRAT8/RESULT.md (or t104_strat8_result.md if that is the name) first.
  global_cover.json partitions the canonical chart (volume 1152): 24,702 leaves with Cface >= 0, 10,208 excluded, 5,272 OPEN
  (open_boxes.json). Cface is the face polynomial whose sign is T for five-vertex connected carriers at D = 2.
- STRAT13/ : the finished proof for the 5+1 class at N = 6, region (11). It contains STRAT12/ (which contains STRAT11/ and STRAT10/).
  Read STRAT13/RESULT.md, STRAT12/RESULT.md and STRAT11/RESULT.md. That chain is:
  STRAT10 cover of the same canonical chart -> STRAT11 corner ball at r = a = 1 (T6 >= ||S-S0||/120 on 0 < ||S-S0|| <= 1/20800) ->
  STRAT12 exact Bernstein certificates with Farkas multipliers on the STRAT10 necessary constraints (exclusion: -sum lambda_k g_k
  positive on the box; positivity: T - sum lambda_k g_k positive), splitting to depth 16 -> STRAT13 collars at the nine equality limits
  (two disjoint edges of weight 1/2 plus an isolate; a triangle of weights 1/3 plus two isolates), with a chart that removes the
  eigenframe rotation and Farkas multipliers on the active edge weights giving T >= ||h||_1/12 near each limit. Replay: STRAT13/replay_all.py.

The STRAT8 tree and the STRAT10 tree have almost the same shape (40,181 vs 40,177 splits) because they cover the same chart; the
target differs (Cface for n = 5 without the isolate vs T6 for N = 6 with one isolate).

Task:
1. Compare the n = 5 target with T6: write down exactly how Cface and T6 (or C_N) relate on the shared chart (STRAT10 zero_face.py
   gives C_N quadratic in q = N-6; check whether n = 5 is that formula at another value or a different polynomial). Say which STRAT10-13
   tools transfer unchanged and which need a new computation.
2. Find the points of the closure of the STRAT8 OPEN set where Cface is 0 or where no strict certificate can exist: the corner r = a = 1
   (as in STRAT10/11), the disconnected equality limits (balanced triangle plus two isolates; two edges of weight 1/2 plus an isolate -
   STRAT4 proved these are the only equality cases among disconnected graphs at n = 5), and anything else. Prove local bounds there
   (corner ball as STRAT11, collars as STRAT13) with explicit rational constants and radii.
3. Close the 5,272 OPEN leaves with exact Bernstein certificates and splitting as in STRAT12, minus the balls and collars of step 2.
4. If Cface < 0 at a feasible rational point, that is a COUNTEREXAMPLE to T104 at n = 5: report it with an exact replay and stop.
5. Write replay_all.py: replay STRAT8 unchanged (temporary byte-identical copy), then every new certificate, ball and collar, in exact
   arithmetic (Fraction, or exact Q(sqrt d) numbers). Run it and record the time.
6. If everything closes, state the full theorem: T >= 0 for every connected five-vertex graph at D = 2, combining STRAT4, STRAT5, STRAT6,
   STRAT8 and this run, each hypothesis named and each region pointed to its replay. Else list exactly what remains.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find candidates; no PROVED
statement trusts floats. 4 worker processes at most, peak memory under 2.5 GB, this Mac is shared. Append to LOG.md after each step and keep
RESULT.md current. Do not edit STRAT8/ or STRAT13/ (copy what you reuse). Normal speed only.
