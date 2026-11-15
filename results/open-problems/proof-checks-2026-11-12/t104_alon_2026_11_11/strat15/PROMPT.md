# STRAT15: close the T104 5+1 class for every N >= 7 (a connected five-vertex carrier with both top eigenvalues plus N-5 isolated vertices)

Context in this folder:
- STRAT14/ : the finished proof for connected n = 5, D = 2. It contains STRAT13/ (the finished proof of the 5+1 class at N = 6,
  region (11); STRAT13 contains STRAT12, which contains STRAT11, which contains STRAT10 and STRAT9 if present) and STRAT8/.
  Read STRAT14/RESULT.md, STRAT13/RESULT.md, STRAT12/RESULT.md, STRAT11/RESULT.md and STRAT10's RESULT/FINALIZE first.
- The shared chart. STRAT14/verify_targets.py proves, with C_N(q) the STRAT10 polynomial and q = N-6:
      C_N(q) = 10(N-2)^2 D^2 Delta T_N,  C_N(-1) = 2 Cface (n = 5),  T6 = C_N(0)/(160 D^2 Delta).
  So the 5+1 class with N-5 isolated vertices is the same canonical chart with target C_N(q), quadratic in q, and N >= 7 is q >= 1.
- What is already known for N >= 7 (STRAT9, STRAT10): T >= 0 when b/a <= 3/25, when a <= 129/250 (uniform all-N ceiling from the
  STRAT10 sextic bound), under the all-N ratio ceilings (ceiling_table.csv), and on 24,458 of the 24,708 STRAT10 positive leaves
  (those certified for every N >= 6). The pressure family of STRAT10 (verify_family.py) has T -> 0+ at the corner r = a = 1 for every
  N >= 6, so the corner needs a local bound uniform in N. The disconnected equality cases (two edges of weight 1/2 plus isolates; a
  balanced triangle plus isolates) are equality points for every N (STRAT7 padding: X2 = 2N B/(N-2),
  X3 = (1-lambda)[D(N-1)(N-4)lambda - 2D(N-2) + 2N h]/(N-2)^2; S5 = 0 gives T >= 0 for every N).
- STRAT12 and STRAT13 certified their boxes, ball and collars for N = 6 only (target C_N(0)). STRAT11's corner ball is N = 6 only.

Task:
1. Write C_N(q) = c0 + c1 q + c2 q^2 exactly on the chart. Decide how to certify all q >= 1 at once: e.g. a seventh Bernstein variable
   u = 1/(q+1) in (0, 1/2] after multiplying by (q+1)^2 (degree two in u), or sign conditions on c2 and on C at q = 1 together with the
   derivative at q = 1. The limit N -> infinity (u = 0) must be included: prove T_infinity >= 0 on the region too, or show the
   certificate covers u = 0. Say exactly which statement you certify.
2. The region to cover for N >= 7: every leaf of the final STRAT13 N = 6 cover that is not already certified for every N >= 6
   (the STRAT10 non-all-N positive leaves, the STRAT12 certificates, the STRAT13 collar leaves, the STRAT11 corner ball), each now with
   q in [1, infinity). List them first with counts.
3. Local bounds uniform in N: the corner r = a = 1 (as STRAT11) and the nine equality limits (as STRAT13), with explicit rational
   constants and radii valid for every N >= 7 including the limit. If a constant degrades to 0 as N -> infinity, say so and find the
   right scaling (for example bound (N-2)^2 T_N or C_N(q)/(q+1)^2 instead of T_N).
4. Close the rest with exact Bernstein + Farkas certificates on the STRAT10 necessary constraints, now in the extended variables,
   splitting as needed.
5. If C_N(q) < 0 at a feasible rational point for some integer N >= 7, that is a COUNTEREXAMPLE to T104: report it with an exact
   replay and stop. A negative value only at non-integer q is not a counterexample; report it and restrict to integers.
6. Write replay_all.py: replay STRAT14 and STRAT13 unchanged (byte-identical copies), then every new certificate, ball and collar, in
   exact arithmetic (Fraction or exact Q(sqrt d)). Run it and record the time.
7. If everything closes, state the theorem: T >= 0 for every graph in the 5+1 class (a connected five-vertex component carrying both
   top eigenvalues, the other N-5 vertices isolated) for every N >= 7, naming each hypothesis and the replay for each region. Combined
   with STRAT7 padding say whether this proves every disconnected graph at D = 2 whose components have at most five vertices, for every
   N. Else list exactly what remains.

Rules: label every statement PROVED (exact replay script named), NUMERICAL, or OPEN. An LP or float search may find candidates; no PROVED
statement trusts floats. 4 worker processes at most, peak memory under 2.5 GB, this Mac is shared. Append to LOG.md after each step and keep
RESULT.md current. Do not edit STRAT14/ or anything inside it (copy what you reuse). Normal speed only.
