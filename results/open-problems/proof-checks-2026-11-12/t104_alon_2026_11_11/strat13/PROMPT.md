# STRAT13: close the last 9 OPEN leaves of T104 5+1 region (11), N=6, by local collar bounds at the disconnected equality limits

Context in this folder: STRAT12/ (certificates.json, obstructions.json, verify_obstruction.py, refine.py, RESULT.md, replay_all.py),
which contains STRAT11/ and STRAT10/. Read STRAT12/RESULT.md and STRAT11/RESULT.md (the corner-ball argument) first.

State (STRAT12, replayed exactly): 13,359 of 13,368 open boxes are closed by exact Bernstein certificates. Nine leaves at depth 16
remain (nodes 12091 12407 14175 15603 15773 19750 20736 21058 21550). Each contains a point of the closure where the connected
constraint is 0: five hold Q(sqrt5) two-edge limits, four (19750 21058 12407 15603) hold Q(sqrt15) limits (a triangle with weights 1/3
and two isolated vertices). At these points no strict certificate of either STRAT12 form exists (verify_obstruction.py).

Task:
1. For each limit point P (exact algebraic coordinates), compute the local expansion of T and of the active constraints near P on the
   feasible side (connected constraint > 0). Find the leading behaviour: show T >= c * (a positive local quantity, e.g. the connected
   constraint, or ||S - P||) on the feasible part of a ball/collar B(P, r) with explicit rational c, r, as STRAT11 did for the corner.
2. Cover each leaf box minus B(P, r) by the STRAT12 method (exact Bernstein exclusion/positivity with splitting); a box minus a ball
   is handled by splitting until every leaf is inside the ball or certified.
3. If at some limit T decreases into the feasible side (T < 0 at a feasible rational point nearby), that is a COUNTEREXAMPLE: report it
   with an exact replay.
4. Write verify_collars.py (exact arithmetic only: Fraction / SymPy algebraic numbers in Q(sqrt5), Q(sqrt15)), extend replay_all.py to
   run STRAT12's replay plus the collars, run it, record the time.
5. If all nine close, state the full theorem for region (11) at N=6 with every hypothesis named; else list what remains.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find candidates;
no PROVED statement trusts floats. 4 worker processes at most, peak memory under 3 GB, this Mac is shared. Append to LOG.md after each
step, keep RESULT.md current. Do not edit STRAT10/, STRAT11/ or STRAT12/. Normal speed only.
