# Efron-Stein tightness vs granularity: not laptop-measurable, and my first harness violated a
# theorem. 2026-08-16 pass 17. NEGATIVE RESULT. chi = 1/3 UNMOVED.

## 1. What was attempted and why

CRUX 9.8's cross-note states the wall in the field's language: the halving's demand A2^+ <= C M D_n
against Efron-Stein's free A2^+ >= Var(X_{Mn}) means the wall is "Efron-Stein is ORDER-TIGHT for the
block partition at every scale", adding "At edge granularity BKS prove the opposite
(superconcentration by log n); GRANULARITY IS WHAT RECONCILES THE TWO."

That reconciliation is asserted, never measured. Define for a partition P

    R(P) := A2^+(P)/Var(X),   A2^+(P) = (1/2) sum_{L in P} E[Delta_L^2].

Efron-Stein gives R >= 1 for any partition; R = 1 exactly at the coarsest (one cell); BKS says R is
loose like log n at edge granularity. The SHAPE of R between those anchors is the provability
structure, so I measured it.

## 2. The first run violated a theorem, and the pre-registered sanity check caught it

Measured R at N=12 across cell sizes 1,2,3,4,6,12: 0.8450, 0.8157, 0.8858, 0.7720, 0.8770, 0.9141 -
ALL BELOW 1. R >= 1 is Efron-Stein, a theorem, so this is a defect in my measurement, not a finding.
The script had pre-registered "monotone decrease in k is a sanity requirement, not a finding - if it
fails, the harness is wrong and nothing else should be read", and it failed both tests (below floor,
and non-monotone). Nothing from that run was reported.

THE DEFECT, and it is embarrassing because I had already fixed it once tonight: Var(X) was estimated
from the SAME small expensive sample as A2^+ (220 reps at N=12, 120 at N=16). A variance from 220
draws carries ~9.5 percent relative error. Measured against a clean 20000-rep estimate the small-
sample denominator was 1.14918 where the truth is 0.88828 - a 29 percent overestimate, which pushed
the ratio under the floor. The beta measurement earlier the same night got this right by simulating
its denominator separately; I did not carry that across.

REPAIRED, denominator only, 20000 reps:
    N     Var (few reps)   Var (20000)    R old     R fixed
    12       1.14918         0.88828     0.8450     1.0932
    16       1.11442         1.10076     1.1151     1.1290
Both above the floor. The harness is sound; the estimator was not.

## 3. The negative result

At edge granularity BKS predicts R ~ log n, which is about 2.5 to 2.8 at N = 12 to 16. Measured
R = 1.09 and 1.13. The superconcentration looseness has NOT switched on at these sizes - Efron-Stein
is already nearly tight at edge granularity, so there is no interpolation from log n down to 1 to
observe and the granularity experiment has no signal at laptop scale.

That is worth recording precisely because it closes a line: do not spend compute on measuring
R(granularity) on this machine. The quantity the campaign wants to understand only becomes
non-trivial once the log n looseness is visible, which needs n far beyond anything reachable here.
It also explains the flat readings at N=16 (R = 1.115, 1.118, 1.117, 1.120, 1.064 across cell sizes
1,2,4,8,16) - not a measurement of the reconciliation, just noise around a ratio that is ~1.1
everywhere at this size.

## 4. The methodological point, which is the session's fourth instance of one shape

Tonight, in order: the compute governor's "growing at ~174/hour" was a difference of two jittery
totals (direct timestamps said ~4/hour); fire 8's paired excess grew half because its null fell;
fire 13's excess growth was 86 percent baseline movement; and this - a denominator estimated on too
few draws, breaking a theorem. All four are the same failure: THE BASELINE OR DENOMINATOR IS A
MEASUREMENT TOO, and it is the one nobody budgets samples for. Budget the denominator separately and
generously; it is usually the cheap half of the computation and always the half that decides the
ratio.

## 5. Standing

chi = 1/3 UNMOVED. (L1') remains the wall, and 9.3's obstruction - that (L1') at any constant beta is
unprovable because Var(X_n) is only known above c log n - is untouched by anything here. This fire
produced a negative result about what is measurable, plus a repaired harness, and nothing else.

Related: CRUX_iteration_arithmetic.md 9.8 cross-note (the claim this tried to measure);
BETA_MEASURED_20260815.md (which handled its denominator correctly and should have been the model).
