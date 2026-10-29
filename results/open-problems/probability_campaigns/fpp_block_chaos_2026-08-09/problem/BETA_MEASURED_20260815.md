# beta measured for the first time - and it does NOT touch the wall, for a reason worth stating.
# 2026-08-15 pass 16. chi = 1/3 UNMOVED.

## 1. What was measured

(L1') E[Delta_L^2 | U_L] <= beta Var(X_n) is the wall (CRUX 9.3: "the wall persists INSIDE (L1)"),
and fires 3 and 5 established that (L1'), the variance ratio D_Mn/D_n and constant-A doubling are one
object seen three ways. Nobody in this campaign had measured beta. It is a RATIO of two variances -
dimensionless - which is the same property that made (L2') laptop-testable.

Numerator from the saved pairs; denominator Var(T(0,(n,0))) simulated separately, 30000 reps each,
same weight law (U[1,2]), exact Dijkstra.

    block n   occ    E[D^2|U] (num)   Var(X_n) (den)    beta      E[T_n]   E[T_n]/n   Var/n
        4    3.95        0.58290          0.33085      1.7618     5.999     1.4998    0.0827
        6    6.04        0.78588          0.49834      1.5770     8.995     1.4992    0.0831
       10   10.08        1.13713          0.78560      1.4475    14.972     1.4972    0.0786
       14   14.05        1.40070          1.01704      1.3772    20.914     1.4939    0.0727

CONTROLS, run because a sim that flatters is lying. E[T_n]/n is flat at ~1.50 and drifting down as
the geodesic gains room to optimise - a sane time constant. Var(X_n)/n starts at 0.0827 against the
straight-path value 1/12 = 0.0833 (a sum of n iid U[1,2] with no optimisation) and then FALLS to
0.0727 - the sim reproduces the trivial baseline at the smallest size and shows superconcentration
beginning as n grows. Both controls pass, so the denominator is trustworthy.

## 2. The reading

beta is BOUNDED and DECREASING: 1.7618 -> 1.5770 -> 1.4475 -> 1.3772, with decrements -0.185,
-0.130, -0.070 that are themselves shrinking. Both numerator and denominator grow (x2.40 and x3.07
respectively over the range) and beta falls because the DENOMINATOR grows faster - stated explicitly
because tonight's standing error was reporting a ratio without saying which side moved.

A one-parameter correction fits all four points: beta ~ beta_inf + c/n with beta_inf ~ 1.22,
c ~ 2.15 (predicts 1.583 and 1.439 at n = 6 and 10 against observed 1.577 and 1.448). LABELLED AS A
DESCRIPTION OF THE MEASURED RANGE, NOT AN ASYMPTOTIC CLAIM - a two-parameter fit on four points

## 3. Why this does NOT touch the wall, said before anyone reads it as progress

The obstruction in (L1') is PROVABILITY, not truth. CRUX 9.3, verbatim: "(L1) at ANY constant beta is
hard for the same reason the wall was hard: it compares a single block's influence against Var(X_n),
whose only unconditional lower bound is c log n. Proving E[Delta_L^2] <~ log n is far beyond current
technology."

(L1') is what KPZ predicts and nobody doubted it holds. Measuring that it holds at block scale 4-14,
in a regime 17 orders of magnitude below l_0 ~ 1e18, confirms the FACT and leaves the PROOF exactly
where it was. This measurement moves the wall not at all, and I would rather say so than let a clean
table read as progress on chi.

WHAT IT IS GOOD FOR, honestly and modestly:
 - it is a NUMBER where the campaign had none - beta ~ 1.4 and falling, so anyone chasing a proof
   with an explicit constant now knows the target is a little above 1, not 10 or 100;
 - it rules out the (already implausible) scenario of beta being large or growing at accessible
   scales, which would have been a cheap way to learn that the whole per-block reduction was aimed
   at something false;
 - it is a mild CONSISTENCY CHECK on 9.3's own reasoning. 9.3 notes that Efron-Stein plus (L1) gives
   Var(X_Mn) <= (beta/2) M D, so "beta <= 1 would prove the halving with no engine, no chaos and no
   lemma at all - which means (L1) at beta <= 1 must be false or unprovable". Measured beta sits
   ABOVE 1 at every point and its decrements are shrinking toward a limit that the fit puts near
   1.22 - i.e. converging from above, not crossing. Consistent with 9.3. It could not have refuted
   9.3 either way (beta <= 1 at small n would say nothing about the asymptotics), so this is
   corroboration of a weak kind and is recorded as such.

## 4. Limits

Block scale 4-14 against l_0 ~ 1e18. Square blocks, not the engine's tall thin W ~ sqrt(nQ). One
weight law. M = 4 in this geometry where the engine wants M large. And the deepest one: nothing
about a measured beta bears on whether a beta can be PROVED, which is the entire obstruction.

Related: CRUX_iteration_arithmetic.md 9.3 and 9.5; POSITIVE_PART_IS_GAP_CAPPED_20260815.md (the
(L2') arc, whose method lesson - report the level and say which side moved - is applied here).
